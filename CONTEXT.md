# Triathlon Training Plan — Domain Glossary

## Athlete

Thimon Pelka. Male, 69kg, Vienna, Austria. Target race: Ironman 70.3 on 2027-05-23.

---

## Race

**Ironman 70.3** — A triathlon consisting of:
- Swim: 1.9km
- Bike: 90km
- Run: 21.1km (half marathon)

Target finish time: **sub 5:30h**.

---

## Session

A single planned training unit. Every session has:
- a **sport** (Run, Ride, Swim, Strength, Volleyball)
- a **type** (e.g. Easy, Intervals, Tempo, Long, Brick, Technique)
- a **duration or distance target**
- optionally: a **zone** or intensity prescription

A session is **planned** when it exists in a weekly plan file. It becomes **completed** when a matching Strava activity is recorded.

---

## Brick Session

A single training block combining bike immediately followed by run, designed to simulate race-day neuromuscular transition. Scheduled periodically on Saturdays, increasing in frequency closer to race day.

---

## Pinned Session

A session locked to a specific day of the week in the weekly template. Pinned sessions do not move when the plan is adjusted. Examples: Gym on Monday and Wednesday mornings, long ride on Saturday.

---

## Floating Session

A session that has a prescribed role in the week (e.g. second run, interval bike) but whose exact day is determined by me based on available slots, recovery, and other anchors that week.

---

## Weekly Template

The recurring weekly schedule stored in `schedule/weekly-template.md`. Defines: which days have pinned sessions, what time windows are available each day, and any standing constraints (e.g. no bike before work on weekdays).

---

## Irregular Event

A one-time deviation from the weekly template that blocks or modifies a specific day in a specific calendar week (e.g. travel, holiday, tournament). Stored in `schedule/irregular-events.md`. Can be added by editing the file directly or by telling me in chat.

---

## Macro Plan

The full periodization skeleton for the training journey from now until race week. Stored in `plans/macro.md`. Defines training phases, weekly volume targets, and key milestones. Does not contain day-by-day session detail.

---

## Training Phase

A multi-week block with a specific physiological focus. Phases in this plan:

| Phase | Focus |
|-------|-------|
| Base | Aerobic foundation, establish swim technique, maintain bike/run volume |
| Build | Volume and intensity increase across all three disciplines |
| Peak | Race-specific intensity, brick sessions, longer race simulations |
| Taper | Volume reduction, sharpening, race preparation |

---

## Milestone

A named event or achievement that gates phase transitions. Examples:
- **Swim Course Completed** (~early July 2026, TBD): unlocks structured swim volume
- **First Open Water Swim**: marks swim readiness
- **Race Week**: final week before the event

---

## Weekly Plan

A detailed file for a specific ISO calendar week (e.g. `plans/weeks/2026-W26.md`). Contains the day-by-day session schedule for that week, prescribed zones/targets, and notes. Only 3–4 weeks of detailed plans exist at any time — new weeks are generated when I'm restarted in a new session.

---

## Status

The snapshot of current training state, stored in `STATUS.md`. Read at the start of every session to orient me. Contains: current phase, current week number in the plan, recent Strava-confirmed fitness metrics, and the next milestone.
