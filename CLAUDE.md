# Instructions for Claude

This repository is a training plan for Thimon Pelka's Ironman 70.3 on 2027-05-23. Target: sub 5:30h finish.

## How to Start Every Session

**Do these steps in order before doing anything else:**

1. Read `STATUS.md` — find current phase, current plan week, pending actions.
2. Read `plans/macro.md` — understand the phase targets and session volume goals.
3. Read `schedule/weekly-template.md` — know the weekly constraints.
4. Read `schedule/irregular-events.md` — check for upcoming day blocks.
5. Pull Strava activities for the last 4 weeks using the `strava-mcp` tool (`list_activities` with a `range_start` 4 weeks back). Compare against the last 2–3 weekly plan files in `plans/weeks/`.
6. Assess: what was completed, what was missed, how load compares to phase targets.
7. Generate detailed weekly plans for the next 3–4 weeks (if not already written), adjusting for actual completed load.
8. Update `STATUS.md` with the current date, phase week, and any new fitness observations.

## Repository Structure

```
CLAUDE.md               ← this file
CONTEXT.md              ← domain glossary (read to understand terminology)
STATUS.md               ← current training state (read + update each session)
schedule/
  weekly-template.md    ← standing weekly schedule and constraints
  irregular-events.md   ← one-time day blockers (edit or update via chat)
plans/
  macro.md              ← full periodization skeleton, phases, milestones
  strength.md           ← periodized gym program
  weeks/
    YYYY-WNN.md         ← detailed weekly plan files (ISO week format)
scripts/
  sync_calendar.py      ← push weekly plans to Google Calendar (see README)
docs/adr/               ← architecture decision records
```

## Generating Weekly Plans

Each weekly plan file (`plans/weeks/YYYY-WNN.md`) should contain:
- Day-by-day sessions for the week
- For each session: sport, type, duration/distance, zone/intensity prescription
- Notes on how this week fits into the current phase
- Any deviations from the weekly template due to irregular events

Only generate 3–4 weeks of detail at a time. Do not pre-write beyond that — load and fitness evolve.

## Updating Irregular Events

When Thimon mentions a day is blocked or a week is unusual:
1. Add an entry to `schedule/irregular-events.md`
2. Adjust the affected weekly plan file if it already exists

## Strava Integration

The `strava-mcp` tool provides:
- `list_activities` — fetch completed activities by date range
- `get_athlete_zones` — current HR/power/run zones
- `get_athlete_profile` — weight, preferences
- `get_activity_performance` — detailed metrics for a specific activity

Use Strava as the source of truth for what was actually completed. Planned sessions in `plans/weeks/` represent prescriptions; Strava represents reality.

## Key Constraints (never violate)

- No bike sessions before work on weekdays (no indoor trainer).
- Monday and Wednesday mornings are gym sessions at ~06:30.
- Tuesday morning is a run (≤1h, easy or structured).
- Saturday = long ride (or brick session).
- Sunday = long run.
- Volleyball Wed evening until ~2026-07-29.
- Beach volleyball 1–2x/week is a real training load — treat it as such when calculating weekly stress.
- Swim sessions only start after the technique course is completed (~early July 2026, TBD).
- Maximum: 3 swim, 2 bike, 2 run sessions per week (not counting gym and volleyball). Swim raised from 2→3 on 2026-07-02 — swim is the primary limiter; frequency > duration while the stroke is young (see docs/adr/0003).
