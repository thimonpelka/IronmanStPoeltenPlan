# Triathlon Training Plan

A personal, Claude-managed training plan for **Ironman 70.3 on 2027-05-23** (target:
sub-5:30h). The repo is the single source of truth for the plan; [Strava](https://strava.com)
is the source of truth for what was actually done.

This is a **planning repo**, not an app — most of it is Markdown that Claude Code reads and
updates each session. The only code is a Google Calendar sync script.

## How it works — two layers of planning

See [`docs/adr/0001-rolling-plan-with-macro-skeleton.md`](docs/adr/0001-rolling-plan-with-macro-skeleton.md).

1. **Macro skeleton** ([`plans/macro.md`](plans/macro.md)) — the full periodization:
   phases, volume targets, milestones, loading rhythm, discipline strategies. Changes
   rarely; keeps the plan coherent across sessions.
2. **Rolling detail** ([`plans/weeks/`](plans/weeks/)) — only the next ~3–4 weeks are
   written as day-by-day files (`YYYY-WNN.md`). Regenerated as fitness and life evolve.

## Repo layout

```
CLAUDE.md               ← instructions Claude follows every session (start here)
CONTEXT.md              ← domain glossary (terminology)
STATUS.md               ← current training state — read + updated each session
README.md               ← this file
schedule/
  weekly-template.md    ← standing weekly schedule + constraints
  irregular-events.md   ← one-time day blockers
plans/
  macro.md              ← periodization skeleton, phases, milestones
  strength.md           ← periodized gym program
  weeks/YYYY-WNN.md     ← rolling detailed weekly plans
docs/adr/               ← architecture decision records (why the plan is shaped this way)
scripts/
  sync_calendar.py      ← push weekly plans to Google Calendar
```

## Working with Claude each session

Claude follows the startup protocol in [`CLAUDE.md`](CLAUDE.md): read `STATUS.md` →
`macro.md` → schedule files → pull recent Strava → compare planned vs actual → generate
the next few weeks → update `STATUS.md`. Just tell it what changed (missed sessions,
blocked days, how things felt) and let it re-plan.

## Calendar sync

Pushes the sessions in `plans/weeks/` to a dedicated "Triathlon Training" Google Calendar,
color-coded by sport. Synced events are tagged, so re-running replaces them cleanly (no
duplicates).

```bash
uv sync                                        # install dependencies (first time)

uv run python scripts/sync_calendar.py --dry-run    # preview parsing (no auth, no writes)
uv run python scripts/sync_calendar.py              # sync all week files
uv run python scripts/sync_calendar.py 2026-W31     # sync specific week(s)
uv run python scripts/sync_calendar.py --clear      # remove all synced events
```

**Setup**: download OAuth credentials from Google Cloud Console (Calendar API enabled) to
`scripts/credentials.json`. First run opens a browser to authorize and saves
`scripts/token.json`. Both files are gitignored — never commit them.

Tip: run `--dry-run` after regenerating weekly plans to confirm sessions, times, and
durations parsed correctly before writing to your calendar.
