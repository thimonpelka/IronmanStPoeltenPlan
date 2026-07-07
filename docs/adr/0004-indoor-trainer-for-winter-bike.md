# ADR 0004 — Indoor Trainer for the Winter Bike Block

**Status**: Accepted
**Date**: 2026-07-07

## Context

Build 2 (2026-11-30 → 2027-02-28) is the threshold-bike emphasis block, and the macro
names the bike "the biggest time lever" for a sub-5:30. But the plan carried a standing
constraint — **"no bike sessions before work on weekdays (no indoor trainer)"** — and
the only bike slots are Thursday daytime and Saturday. In Vienna, December–February
means darkness by ~16:00 and frequent ice: the block that matters most was scheduled
in the least rideable months with no mechanism to execute it. A silent assumption of
year-round outdoor riding would realistically cost 30–50% of winter quality sessions.

Alternatives considered:

1. **Buy an indoor smart trainer** — removes weather/daylight risk entirely; threshold
   intervals become *more* controllable than outdoors; unlocks weekday-morning riding.
2. **Gym / spin bikes** — no purchase, but power numbers don't match the athlete's
   meter, position differs from the race bike, and Saturday long rides still die in
   January.
3. **Ride outdoors year-round** — cheapest; makes Build 2's quality work
   weather-dependent in exactly the block the macro says matters most.
4. **Restructure the plan** — shift bike emphasis to autumn/spring, hold bike at winter
   maintenance. Honest, but concedes the biggest time lever for the longest block.

## Decision

- **Buy a smart trainer (controllable resistance + power) by end of October 2026.**
  Build 2 starts 2026-11-30; late-October purchase leaves shakedown rides before the
  block depends on it. This is a plan milestone.
- **The constraint is rewritten**: *outdoor* bike sessions never before work on
  weekdays; *trainer* sessions may be scheduled on weekday mornings once the trainer
  exists. Standing preference remains: Mon/Wed mornings = gym, Tue morning = run,
  weekday trainer rides land **after work**.
- The 2-bike-sessions-per-week cap is unchanged.
- Winter prescription pattern: mid-week quality ride (sweet-spot/threshold) moves to
  the trainer by default from ~December; Saturday rides go outdoors when conditions
  allow, on the trainer (or split indoor/outdoor) when they don't.

## Consequences

- CLAUDE.md's key-constraint list and `schedule/weekly-template.md` are updated to the
  new wording (done 2026-07-07).
- `plans/macro.md` gains a milestone (trainer by 2026-10-31) and a winter-riding note
  in the Build phase.
- Weekly plans from ~December prescribe the mid-week ride as a trainer session in
  watts; long-ride prescriptions name an indoor fallback.
- FTP tests become executable in winter regardless of weather (relevant for the
  ~2026-12-18 and 2027-02-12 retests).
