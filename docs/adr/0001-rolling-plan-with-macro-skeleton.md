# ADR 0001 — Rolling 4-Week Detail with Full Macro Skeleton

**Status**: Accepted
**Date**: 2026-06-16

## Context

The race is ~49 weeks away. Writing day-by-day session detail for the full 49 weeks upfront would be wasted effort — training load must adapt to what was actually completed (via Strava), upcoming life events, and how fitness evolves. At the same time, each new Claude session needs enough context to generate a coherent next block without asking the athlete to re-explain the whole plan.

## Decision

Maintain two layers of planning:

1. **Macro skeleton** (`plans/macro.md`): Full 49-week periodization — phases, volume targets, milestones. Written once, updated when circumstances change significantly. This is what makes the plan coherent across sessions.

2. **Rolling detail** (`plans/weeks/`): Only the next 3–4 weeks are written as day-by-day session files. Each new session, Claude reads Strava for the last 4 weeks, assesses actual vs. planned, and generates the next 3–4 detailed weeks.

## Alternatives Considered

- **Full detail upfront**: Too rigid. A session missed in week 3 cascades through the whole document.
- **No macro skeleton, fully dynamic**: Risks losing periodization coherence across sessions. Claude has no anchor for "where are we in the journey."

## Consequences

- Each session startup requires a Strava pull + comparison step before generating new weeks.
- The macro skeleton must be updated when major circumstances change (e.g. swim course delayed, injury, race goal revised).
- Weekly plan files older than ~6 weeks can be treated as historical record and don't need to be re-read during startup.
