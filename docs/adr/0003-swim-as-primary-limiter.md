# ADR 0003 — Swim Treated as the Primary Limiter

**Status**: Accepted
**Date**: 2026-07-02

## Context

The athlete is a **complete beginner swimmer** targeting a 1.9km open-water swim in
~10 months. Every other discipline is already at or near race level; swimming is the
one being built from zero. It is therefore the single highest-risk leg — not for the
time it costs (a slow swim leg is survivable), but for the **risk of not completing it
safely**, and for the anxiety/energy cost of an open-water mass start on an
under-prepared swimmer.

Two things in the current plan under-serve this risk:

1. **Frequency.** The plan (and CLAUDE.md constraints) cap swimming at **2×/week**. For
   skill acquisition in a new motor pattern, *frequency beats duration* — three short
   swims teach the stroke faster than two long ones. 2×/week is closer to a maintenance
   dose than a learning dose for a beginner.

2. **Open water is barely addressed.** The plan has a single "first open water swim
   ~Aug" milestone and nothing on sighting, wetsuit swimming, mass-start/contact
   practice, or the fact that OW season in Vienna is roughly **May–October** — the water
   is cold and largely unavailable over the winter, exactly when Build/Peak volume is
   highest.

## Decision

Treat swim as the priority discipline in Base and Build, and plan explicitly around the
open-water calendar.

### Frequency
- Keep the plan compatible with the 2×/week hard constraint, **but recommend the athlete
  relax it to 3× short swims** during Base and early Build while the stroke is being
  built. The freed **Wednesday evening slot after volleyball ends (~2026-07-29)** is the
  natural home for a third short technique swim without adding a new time burden.
- If 3× is not possible, keep 2× but bias both toward frequency-style short sessions with
  high technical density, not long continuous grinds.

### Open-water progression (front-loaded into warm months)
- **2026-08 → 2026-10** (first OW window): first OWS, then regular OW exposure while the
  water is warm — practise **sighting, straight-line swimming without lane lines,
  breathing in chop, and exits**. Get comfortable, not fast.
- **Winter 2026/27**: pool-only. Maintain and build endurance; keep OW skills warm
  mentally.
- **2027-04 → race**: second OW window. Practise **in the actual wetsuit** (a May race
  almost certainly means a wetsuit-legal, cold swim), plus **mass-start / drafting /
  contact** simulation. Do not let race day be the first wetsuit swim.

### Feedback loop
- A single 5-session technique course is a start, not enough feedback to self-coach for
  10 months. Schedule a **periodic feedback checkpoint every ~6–8 weeks** — a coached
  lesson or filmed stroke analysis — so errors don't groove in.
- Establish a **CSS (Critical Swim Speed) test** once continuous swimming is possible
  (~late Aug) to anchor swim pacing zones; retest on the testing cadence (see macro.md).

## Consequences

- `macro.md` swim targets change from "1–2×" / "2×" to reflect the frequency
  recommendation and the OW windows.
- CLAUDE.md's swim cap was **raised from 2× to 3×/week on 2026-07-02** (athlete approved),
  acting on this ADR's recommendation.
- Open-water sessions become scheduled milestones tied to the seasonal windows, not a
  single "someday" item.
