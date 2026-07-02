# ADR 0002 — Loading Rhythm (Deloads) and Phase Rebalance

**Status**: Accepted
**Date**: 2026-07-02

## Context

The original macro plan (ADR 0001, `plans/macro.md` as of 2026-06-16) had two structural
problems that a fresh review surfaced:

1. **No recovery/deload weeks anywhere.** Base, Build, and Peak were described as
   continuous progressive load for 14 + 13 + 17 weeks. On top of 2× gym and 1–2×
   volleyball, uninterrupted progression over a ~47-week runway is a textbook
   overtraining / injury setup. Adaptation is consolidated during recovery, not during
   accumulation.

2. **Phase lengths were backwards.** Peak was the longest phase at **17 weeks**. Peak /
   race-specific load cannot be held for four months — that window becomes a plateau or
   a burnout, not a peak. Meanwhile Build (where the bulk of durable fitness is actually
   made) was only 13 weeks.

The taper dates were also internally inconsistent (phase table said 2027-05-04, the
milestone table said 2027-05-09).

## Decision

### 1. Adopt an explicit loading rhythm

- **Base and Build**: 3:1 cycle — three progressive weeks, then a **deload week at
  ~−40% volume** (intensity touched but not accumulated). The deload is a *planned*
  week in the macro, not something improvised when fatigue shows up.
- **Peak**: tighten to 2:1 — two hard weeks, one deload — because absolute loads are
  higher and recovery need is greater.
- **Taper**: the final 3 weeks (own phase).
- Deload weeks flex ±1 week around fixed real-life perturbations (e.g. the swim course
  week, travel) rather than doubling up on an already-light week.

### 2. Rebalance phase lengths

| Phase | Old | New | Dates (new) |
|-------|-----|-----|-------------|
| Base  | 14 wk | 14 wk | 2026-06-22 → 2026-09-27 |
| Build | 13 wk | **~22 wk** (Build 1 + Build 2, deload between) | 2026-09-28 → 2027-02-28 |
| Peak  | 17 wk | **~9 wk** | 2027-03-01 → 2027-05-02 |
| Taper | 3 wk  | 3 wk | 2027-05-03 → 2027-05-23 |

Build absorbs the extra weeks and is split into two sub-blocks (Build 1: strength-
endurance / sweetspot; Build 2: threshold + brick emphasis) with a deload between them.
Peak becomes a true race-specific block: race-pace work, long bricks, and the
half-distance simulation, then straight into taper.

## Consequences

- The rolling weekly planner (ADR 0001) must now place a deload every 3rd/4th week and
  every 3rd week in Peak. This should be visible in `STATUS.md` (which week of the
  current n:1 cycle we are in).
- Weekly volume targets in `macro.md` describe the *loading* weeks; deload weeks are
  ~60% of that figure.
- The half-distance race simulation moves into the Peak block (~late March / early
  April 2027), roughly 7 weeks out from race day.
- Taper is fixed at 3 weeks: 2027-05-03 → 2027-05-23. The milestone table is corrected
  to match.
