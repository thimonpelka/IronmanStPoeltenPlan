#!/usr/bin/env python3
"""
Sync weekly training plan files to Google Calendar.

Usage:
    python scripts/sync_calendar.py                   # sync all plan files
    python scripts/sync_calendar.py 2026-W28          # sync a specific week
    python scripts/sync_calendar.py 2026-W28 2026-W29 # sync multiple weeks
    python scripts/sync_calendar.py --dry-run         # preview parsing only (no auth, no writes)
    python scripts/sync_calendar.py --clear           # remove all synced events (no re-sync)

First run: opens a browser window for Google OAuth. Saves a token to scripts/token.json
so subsequent runs are silent.

Put your credentials.json (downloaded from Google Cloud Console) in the scripts/ directory.
"""

import argparse
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
except ImportError:
    print("Missing dependencies. Run:  uv sync   (or: uv pip install google-auth-oauthlib google-api-python-client google-auth-httplib2)")
    sys.exit(1)

# ── Config ────────────────────────────────────────────────────────────────────

SCOPES                  = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/calendar.events']
TRAINING_CALENDAR_NAME  = 'Triathlon Training'
TIMEZONE                = 'Europe/Vienna'
EVENT_TAG   = 'triathlon-plan'   # stored in extendedProperties — used to find/delete synced events

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT  = SCRIPT_DIR.parent
WEEKS_DIR  = REPO_ROOT / 'plans' / 'weeks'
TOKEN_FILE = SCRIPT_DIR / 'token.json'
CREDS_FILE = SCRIPT_DIR / 'credentials.json'

# Google Calendar color IDs by sport
SPORT_COLOR = {
    'run':        '11',  # Tomato
    'ride':       '10',  # Basil (dark green)
    'swim':       '9',   # Blueberry
    'gym':        '7',   # Peacock (teal)
    'volleyball': '5',   # Banana
}

MONTH_NUM = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
    'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
    'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12,
}

# ── Auth ──────────────────────────────────────────────────────────────────────

def get_service():
    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CREDS_FILE.exists():
                print(f"credentials.json not found at {CREDS_FILE}")
                print("Download it from Google Cloud Console → APIs & Services → Credentials.")
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(CREDS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        TOKEN_FILE.write_text(creds.to_json())
    return build('calendar', 'v3', credentials=creds)

# ── Parsing ───────────────────────────────────────────────────────────────────

def parse_duration_minutes(text):
    """Extract duration in minutes from strings like ~60min, ~1h, ~1:30h, ~3:15h.

    Hour formats are checked before the bare-minutes pattern on purpose: a multi-part
    session like a brick ("~2:30h ride ... 15min run") should resolve to the longer
    figure, not the first "15min" it stumbles across. Bricks report the ride portion
    (~2:30h); the short transition run isn't summed in — put a total in the header if
    you want the full block on the calendar.
    """
    m = re.search(r'~?(\d+):(\d{2})h', text)
    if m:
        return int(m.group(1)) * 60 + int(m.group(2))
    m = re.search(r'~?(\d+(?:\.\d+)?)\s*h\b', text)
    if m:
        return round(float(m.group(1)) * 60)
    m = re.search(r'~?(\d+)\s*min', text)
    if m:
        return int(m.group(1))
    return None

def detect_sport(text):
    for keyword, sport in [
        ('swim', 'swim'),
        ('volleyball', 'volleyball'), ('beach', 'volleyball'),
        ('gym', 'gym'), ('weight', 'gym'), ('strength', 'gym'),
        # 'brick' and 'spin' before 'run' so a brick/spin isn't mislabelled a run
        ('brick', 'ride'), ('spin', 'ride'), ('trainer', 'ride'),
        ('ride', 'ride'), ('bike', 'ride'), ('ftp', 'ride'), ('cycling', 'ride'),
        ('run', 'run'),
    ]:
        if keyword in text.lower():
            return sport
    return None

def default_time_and_duration(day_abbr, title):
    """Return (HH:MM, duration_minutes) based on day of week + session keywords."""
    sport = detect_sport(title)
    if sport == 'gym':
        return '06:30', 60
    if sport == 'volleyball':
        return '17:00', 120
    if sport == 'swim':
        return ('10:00', 60) if day_abbr == 'Sat' else ('17:00', 60)
    if sport == 'ride':
        return ('07:00', 195) if day_abbr == 'Sat' else ('07:00', 90)
    if sport == 'run':
        return ('07:30', 110) if day_abbr == 'Sun' else ('06:30', 60)
    return '07:00', 60

def is_session_paragraph(para):
    """True if a paragraph is a session header (not an inline description label)."""
    if not para.startswith('**'):
        return False
    # "**Label**: some text" = description label, not a session
    if re.match(r'\*\*[^*]+\*\*\s*:', para):
        return False
    return True

def parse_week_file(path):
    """Parse a weekly plan markdown file. Returns a list of session dicts."""
    text = Path(path).read_text()
    year_m = re.search(r'(\d{4})-W\d+', Path(path).name)
    file_year = int(year_m.group(1)) if year_m else datetime.now().year

    sessions = []
    header_re = re.compile(r'^###\s+(\w{3})\s+(\w{3})\s+(\d+)[^\n]*', re.MULTILINE)
    headers = list(header_re.finditer(text))

    year = file_year
    prev_month = 0

    for i, h in enumerate(headers):
        day_abbr  = h.group(1)
        month_str = h.group(2)
        day_num   = int(h.group(3))
        month_num = MONTH_NUM.get(month_str, 0)
        if not month_num:
            continue

        # Handle year rollover (e.g., a Dec→Jan week)
        if month_num < prev_month:
            year += 1
        prev_month = month_num

        try:
            date = datetime(year, month_num, day_num)
        except ValueError:
            continue

        content_start = h.end()
        content_end   = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        content       = text[content_start:content_end]

        # Split into paragraphs; identify which ones are session starts
        paragraphs    = [p.strip() for p in re.split(r'\n\s*\n', content) if p.strip()]
        session_starts = [idx for idx, p in enumerate(paragraphs) if is_session_paragraph(p)]

        for j, start_idx in enumerate(session_starts):
            # Collect this session's header paragraph + all following paragraphs
            # up to (but not including) the next session header
            end_idx      = session_starts[j + 1] if j + 1 < len(session_starts) else len(paragraphs)
            session_paras = paragraphs[start_idx:end_idx]

            header_para = session_paras[0]
            first_line  = header_para.split('\n')[0]
            bold_m = re.match(r'\*\*(.+?)\*\*(.*)', first_line)
            if not bold_m:
                continue

            bold_text = bold_m.group(1)

            # Skip rest days
            if re.match(r'rest\b', bold_text, re.IGNORECASE):
                continue

            # Detect explicit time prefix: "06:30 — Title" or "~17:00 — Title"
            time_m = re.match(r'~?\s*(\d{1,2}:\d{2})\s*[—–-]+\s*(.+)', bold_text)
            if time_m:
                explicit_time = time_m.group(1)
                title         = time_m.group(2).strip()
            else:
                explicit_time = None
                title         = bold_text.strip()

            # Strip a leading slot-label prefix ("Afternoon — Swim" → "Swim"),
            # but only when the day-part word is directly followed by the dash
            # (so "Morning Run — Tempo" keeps its "Morning Run" name).
            title = re.sub(r'^(Morning|Afternoon|Evening|Night)\s*[—–-]+\s*', '', title)

            sport             = detect_sport(title)
            full_text         = '\n\n'.join(session_paras)
            duration_min      = parse_duration_minutes(full_text)
            def_time, def_dur = default_time_and_duration(day_abbr, title)
            start_time        = explicit_time or def_time
            duration_min      = duration_min or def_dur

            # Strip markdown bold markers for a clean calendar description
            clean_text  = re.sub(r'\*\*(.+?)\*\*', r'\1', full_text)
            description = f'[{EVENT_TAG}]\n\n' + clean_text

            sessions.append({
                'date':         date,
                'day_abbr':     day_abbr,
                'title':        title,
                'start_time':   start_time,
                'duration_min': duration_min,
                'sport':        sport,
                'description':  description,
            })

    return sessions

# ── Calendar operations ───────────────────────────────────────────────────────

def get_or_create_training_calendar(service):
    """Return the calendarId of the training sub-calendar, creating it if it doesn't exist."""
    result = service.calendarList().list().execute()
    for cal in result.get('items', []):
        if cal.get('summary') == TRAINING_CALENDAR_NAME:
            return cal['id']
    new_cal = service.calendars().insert(body={
        'summary':  TRAINING_CALENDAR_NAME,
        'timeZone': TIMEZONE,
    }).execute()
    print(f'  Created calendar: "{TRAINING_CALENDAR_NAME}"')
    return new_cal['id']

def make_event(session):
    start_dt = datetime.combine(
        session['date'].date(),
        datetime.strptime(session['start_time'], '%H:%M').time(),
    )
    end_dt = start_dt + timedelta(minutes=session['duration_min'])
    fmt = '%Y-%m-%dT%H:%M:%S'
    event = {
        'summary':     session['title'],
        'description': session['description'],
        'start':       {'dateTime': start_dt.strftime(fmt), 'timeZone': TIMEZONE},
        'end':         {'dateTime': end_dt.strftime(fmt),   'timeZone': TIMEZONE},
        'extendedProperties': {'private': {'source': EVENT_TAG}},
    }
    color = SPORT_COLOR.get(session['sport'])
    if color:
        event['colorId'] = color
    return event

def delete_synced_events(service, calendar_id, date_min, date_max):
    """Delete all calendar events tagged with EVENT_TAG within the date range."""
    deleted = 0
    page_token = None
    while True:
        result = service.events().list(
            calendarId=calendar_id,
            timeMin=date_min.isoformat(),
            timeMax=date_max.isoformat(),
            privateExtendedProperty=f'source={EVENT_TAG}',
            pageToken=page_token,
            maxResults=250,
        ).execute()
        for ev in result.get('items', []):
            service.events().delete(calendarId=calendar_id, eventId=ev['id']).execute()
            deleted += 1
        page_token = result.get('nextPageToken')
        if not page_token:
            break
    return deleted

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Sync training plan to Google Calendar')
    parser.add_argument('weeks', nargs='*',
                        help='Week IDs to sync (e.g. 2026-W28). Defaults to all plan files.')
    parser.add_argument('--clear', action='store_true',
                        help='Delete all synced events without re-creating them.')
    parser.add_argument('--dry-run', action='store_true',
                        help='Parse and print what would be synced, without touching the '
                             'calendar (no auth needed). Use this to validate parsing.')
    args = parser.parse_args()

    if args.weeks:
        week_ids = args.weeks
    else:
        week_ids = sorted(
            p.stem for p in WEEKS_DIR.glob('*.md')
            if re.match(r'\d{4}-W\d+', p.stem)
        )

    if not week_ids:
        print('No week files found.')
        return

    # Parse all requested week files (local — no auth required yet)
    all_sessions = []
    for wid in week_ids:
        path = WEEKS_DIR / f'{wid}.md'
        if not path.exists():
            print(f'  Warning: {path.name} not found — skipping.')
            continue
        sessions = parse_week_file(path)
        all_sessions.extend(sessions)
        print(f'  {wid}: {len(sessions)} session(s) parsed')

    if not all_sessions:
        print('No sessions to sync.')
        return

    # Dry run: preview parsed sessions and stop before any calendar access.
    if args.dry_run:
        print('\n── DRY RUN — nothing written to the calendar ──')
        for s in sorted(all_sessions, key=lambda x: (x['date'], x['start_time'])):
            dur = f"{s['duration_min']}min" if s['duration_min'] else '?'
            sport = s['sport'] or '—'
            print(f"  {s['date'].strftime('%a %b %d')}  {s['start_time']}  "
                  f"{dur:>7}  [{sport:^10}]  {s['title']}")
        print(f"\n{len(all_sessions)} session(s) would be synced.")
        return

    service     = get_service()
    calendar_id = get_or_create_training_calendar(service)

    # Date range covering all parsed sessions
    dates    = [s['date'] for s in all_sessions]
    date_min = datetime.combine(min(dates).date(), datetime.min.time(), tzinfo=timezone.utc)
    date_max = datetime.combine(max(dates).date() + timedelta(days=1), datetime.min.time(), tzinfo=timezone.utc)

    # Clear existing synced events in the date range first
    deleted = delete_synced_events(service, calendar_id, date_min, date_max)
    if deleted:
        print(f'  Cleared {deleted} existing event(s)')

    if args.clear:
        print('Done (clear only).')
        return

    # Create events
    created = 0
    for s in sorted(all_sessions, key=lambda x: (x['date'], x['start_time'])):
        try:
            service.events().insert(calendarId=calendar_id, body=make_event(s)).execute()
            label = f"{s['date'].strftime('%a %b %d')}  {s['start_time']}  {s['title']}"
            print(f'  + {label}')
            created += 1
        except HttpError as e:
            print(f"  ! {s['title']} on {s['date'].date()}: {e}")

    print(f'\nDone. {created} event(s) created.')

if __name__ == '__main__':
    main()
