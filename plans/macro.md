# Macro Plan — Ironman 70.3, 2027-05-23

## Athlete Baseline (assessed 2026-06-16)

| Discipline | Current Level | Notes |
|------------|--------------|-------|
| Run | Strong | Half marathon in Z2, 5k ~20min, structured intervals |
| Bike | Strong | 100–125km rides regularly at 27–30 km/h |
| Swim | Not trained | Starting from scratch; technique course pending (~early July 2026) |
| Strength | Active | 2x/week gym, consistent habit |
| Volleyball | Active | 1–2x/week, serious commitment |

**FTP**: **238W** (3.45 W/kg @ 69kg) — tested 2026-07-03 (20-min power 251W × 0.95). Confirms
the strong-cyclist assessment; the 133W Strava estimate was invalid. Retest ~2026-08-28.
**Run pace zones**: Based on estimated 5k of 19:55

---

## Race Target

**Sub 5:30h** total finish time.

Rough split targets:
| Leg | Target | Notes |
|-----|--------|-------|
| Swim 1.9km | ~38–42min | Requires technique course + 10 months training |
| T1 | ~3min | |
| Bike 90km | ~2:40–2:55h | ~900m elevation. At NP ~178–186W (IF 0.75–0.78 on FTP 238W) this holds |
| T2 | ~2min | |
| Run 21.1km | ~2:05–2:15h | ~5:55–6:25/km after swim+bike; conservative given brick fatigue |
| **Total** | **~5:20–5:45h** | FTP tested at 238W — sub-5:30 is realistic, swim + run durability are now the deciders |

**Bike split — reconciled with tested FTP (2026-07-03)**: FTP came in at **238W (3.45 W/kg)**,
comfortably in the "strong cyclist" range and far above the invalid 133W estimate. A 70.3
bike leg is ridden at IF ~0.75–0.80; targeting **NP ~178–186W** on the hilly course yields a
**~2:40–2:55h split** and — critically — leaves the legs intact for the run. Climbs may surge
to low Z4 (~210–220W) but the *normalized* power must stay capped; over-biking the climbs is
the classic way to wreck the half-marathon. **Sub-5:30 is now realistic**; the binding
constraints are the swim (built from zero) and run durability off the bike, not bike power.

**Training implication**: long Saturday rides should regularly include real elevation (aim for
700–1000m on longer rides). Flat Z2 rolls alone are insufficient race preparation. Now that
zones are power-based, prescribe the mid-week ride in watts: sweet-spot (Z3–low-Z4, ~190–225W)
in Build, race-pace/threshold in Peak.

**Bike is the biggest time lever and the athlete only gets 2 rides/week** (CLAUDE.md
constraint). Both must earn their place: the Saturday ride carries volume + climbing, and
the mid-week ride carries the intensity (sweet-spot in Build → race-pace/threshold in
Peak), grown in duration on Thursday's open day. Retest FTP ~2026-08-28 on fresh legs (the
test-day legs were slightly fatigued, so 238W may be a mild under-read).

---

## Milestones

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| FTP Test (bike) | 2026-07-03 | ✅ Done — 238W (3.45 W/kg). Next ~2026-08-28 |
| Swim technique course | 2026-07-11, 13, 14, 16, 17 | Confirmed |
| First structured swim sessions | 2026-07-20 (W30) | Tue afternoon + Friday, 2x/week |
| Open water swim (first) | ~2026-08 | Pending |
| OW skills block 1 (sighting, exits, chop) | 2026-08 → 2026-10 | Planned |
| Swim CSS test (pacing anchor) | ~2026-08 (late) | Planned |
| OW block 2 — in race wetsuit + mass-start sim | 2027-04 → race | Planned |
| First Brick session | ~2026-08 | Pending |
| Bricks regular (Sat ride + transition run) | Build (from ~2026-10) | Planned |
| Half-distance race simulation | ~2027-03/04 (Peak, ~7wk out) | Planned |
| Last long ride (>90km) | ~2027-04-26 | Planned |
| Last long run (>18km) | ~2027-04-25 | Planned |
| Taper begins | 2027-05-03 | Planned |
| **Race day** | **2027-05-23** | Target |

---

## Loading Rhythm (deloads)

Training load is **not** applied continuously. Every block uses a build/recover cycle
so adaptation consolidates and injury/overtraining risk stays low (see ADR 0002).

- **Base & Build**: 3:1 — three progressive weeks, then a **deload week at ~−40% volume**
  (keep a light touch of intensity; drop duration and long-session length).
- **Peak**: 2:1 — two hard weeks, one deload (higher absolute loads need more recovery).
- **Deloads flex ±1 week** around fixed real-life perturbations (swim course week,
  travel, illness) rather than stacking a light week on an already-light one.
- Volume targets below describe **loading weeks**; deload weeks are ~60% of that.
- `STATUS.md` should track where we are in the current n:1 cycle.

---

## Run & Brick Strategy

The run is the athlete's **strength** (sub-20 5k, half in Z2), so it needs the least
work to be race-ready — but 70.3 run performance is about **aerobic durability and
running off the bike**, not 5k speed. Bias the training accordingly:

- **Quality run** = tempo / threshold continuous blocks + **progression long runs**,
  not high volumes of 400m VO2 reps. Keep short speed only as **strides** (6–8×20s) for
  economy. The current 8–12×400m @ Z4 sessions build a quality the athlete already has.
- **Long run** stays the aerobic anchor; add late-run progression (finish faster) as it
  builds — this trains fatigue resistance, the actual race limiter.
- **Bricks are a race-specific skill and start earlier**: introduce in Base (first ~Aug),
  make them regular through Build (the Saturday ride + short transition run), and reach
  (near-)weekly in Peak. Running off the bike is trainable — don't save it for the end.

---

## Strength Periodization

The concrete program (movements, sets/reps, sample sessions) lives in
[`plans/strength.md`](strength.md). Summary of the periodization:

"Gym 2×" should not be one generic block for 47 weeks — it periodizes with the plan and
must not compromise key sessions:

- **Base**: anatomical adaptation → max strength. Movement quality, single-leg work,
  posterior chain, core/hip stability. This is the window for heavier lifting.
- **Build**: max strength maintained, converting toward power (lower reps, faster intent);
  volume starts yielding to sport-specific load.
- **Peak**: maintenance/power only, reduced volume — protect the legs for bike/run/brick
  quality. Drop to **1× in the final 4 weeks**.
- **Sequencing**: heavy lower-body should not sit the day before a key run/bike quality
  session. Note the current **Mon gym → Tue run-intervals** clash — either keep Monday
  upper-body/technique-biased or move the run quality off Tuesday.

---

## Swim Strategy — Primary Limiter (see ADR 0003)

Swimming is built from zero; it is the highest-risk leg. It gets priority in Base/Build.

- **Frequency > duration.** 2–3× short technique-dense swims beat 2× long grinds while
  the stroke is young. Swim cap raised to 3×/week (2026-07-02); target a 3rd short swim
  in the Wed slot freed after volleyball ends (~2026-07-29).
- **Open-water is calendar-bound** (Vienna OW season ≈ May–Oct):
  - **2026-08 → 10** — first OWS + regular warm-water exposure: sighting, straight-line
    swimming, breathing in chop, exits. Comfort over speed.
  - **Winter 2026/27** — pool only: endurance + technique.
  - **2027-04 → race** — practise **in the race wetsuit** (cold May swim ⇒ wetsuit) and
    simulate **mass start / contact / drafting**. Race day must not be the first wetsuit
    or first mass-start swim.
- **Feedback loop**: a coached lesson or filmed stroke check every ~6–8 weeks so errors
  don't groove in. Anchor pacing with a **CSS test** (~late Aug), retested on cadence.

---

## Phases

### Phase 1 — Base (2026-W26 → 2026-W39)
**Dates**: 2026-06-22 → 2026-09-27 (~14 weeks)
**Focus**: Aerobic foundation across all disciplines. Establish swim from scratch after technique course. Maintain and modestly grow bike and run volume. Consistency over intensity.

Weekly session targets:
- Run: 2x (1 easy long + late-run progression; 1 quality ≤1h — tempo/threshold + strides, not high-volume 400m VO2 work)
- Bike: 2x (1 long Saturday with real elevation, 1 mid-week — grow from moderate toward
  ~90min endurance by end of Base; Thursday's open day allows length the weekday slots can't)
- Swim: 0x until course complete → then **2–3x** (swim is the priority — frequency > duration; see ADR 0003). Recommend a 3rd short swim in the Wed evening slot freed after volleyball ends (~2026-07-29).
- Strength: 2x (Mon/Wed gym)
- Volleyball: 1–2x (as scheduled)

Weekly volume targets (run + bike combined moving time):
- Early base: ~6–7h/week
- Late base: ~8–9h/week

Key adaptations: aerobic base, swim technique, FTP test, first open water swim.

---

### Phase 2 — Build (2026-W40 → 2027-W09)
**Dates**: 2026-09-28 → 2027-02-28 (~22 weeks, split into two sub-blocks)
**Focus**: Progressive overload — the phase where the bulk of durable fitness is made.
Increase swim volume and confidence. Introduce and progress tempo/threshold work in
bike and run. Make bricks a regular fixture.

Split into two sub-blocks with a deload between them:
- **Build 1** (~2026-09-28 → 2026-11-29): strength-endurance and sweet-spot bias.
  Grow the mid-week bike; longer sustained tempo blocks over short intervals.
- **Build 2** (~2026-11-30 → 2027-02-28): threshold emphasis and brick progression.
  Bricks move from occasional to (near-)weekly by the end of the block.

Weekly session targets:
- Run: 2x (1 long, 1 tempo or intervals)
- Bike: 2x (1 long Saturday; 1 mid-week **sweet-spot/threshold**, grown to ~1.5–2h on
  Thursday). The bike is where a sub-5:30 is won on a hilly course — with only 2 rides
  allowed, both must be high-value: long + hilly, and quality mid-week. Avoid junk-mile
  flat rolls.
- Swim: 2–3x (building from technique to endurance; keep frequency high while the stroke is young)
- Strength: 2x
- Volleyball: as scheduled (reduced in winter months, adjust accordingly)

Weekly volume targets:
- ~9–11h/week

Key adaptations: lactate threshold improvement, swim endurance, brick adaptation.

---

### Phase 3 — Peak (2027-W10 → 2027-W17)
**Dates**: 2027-03-01 → 2027-05-02 (~9 weeks)
**Focus**: True race-specific block — kept deliberately short so it is a peak, not a
plateau. Longest sessions of the cycle, regular bricks, race-pace work, and the
half-distance simulation (~late March / early April, ~7 weeks out). Run off the bike.

Weekly session targets:
- Run: 2x (1 long, 1 race-pace)
- Bike: 2x (1 long ≥ race distance, 1 brick)
- Swim: 2x (race distance simulation)
- Strength: 1–2x (maintenance/power only — see Strength Periodization; 1x in final 4 weeks)
- Brick: weekly (the Saturday long ride is a brick most weeks in this block)

Weekly volume targets:
- Peak loading weeks: ~11–13h/week (deload weeks ~7–8h under the 2:1 rhythm)

Key adaptations: race endurance, brick confidence, race-pace running, transitions.

---

### Phase 4 — Taper (2027-W18 → Race)
**Dates**: 2027-05-03 → 2027-05-23 (3 weeks)
**Focus**: Volume reduction, maintain intensity. Arrive at race day fresh.

Volume reduction: -30% week 1, -50% week 2, race week minimal.
Maintain some race-pace sessions. No new fitness gains — protect what's built.

---

## Testing & Benchmarking

One-off tests drift. Retest on a cadence so zones stay honest and progress is measured.
Deload weeks are good test slots (fresh legs, low surrounding load).

| Test | First | Cadence |
|------|-------|---------|
| Bike FTP (20-min) | 2026-07-03 ✅ (238W) | every ~8 weeks (≈2026-08-28, 10-23, 12-18; 2027-02-12, 04-09) |
| Run threshold (field test / recent race) | ~2026-08 | every ~8 weeks |
| Swim CSS (400m + 200m TT) | ~2026-08 (late) | every ~6–8 weeks |

After each test: update zones in `STATUS.md` and re-derive the affected prescriptions.

---

## Zone Model

Zones must come from a **tested threshold**, not estimates or age formulas:

- **Bike**: % of tested FTP (Coggan-style). **FTP = 238W (tested 2026-07-03)** — zones live
  in `STATUS.md`. Prescribe rides in watts from W28 onward.
- **Run**: pace + HR anchored to a tested threshold pace (from the run field test), not
  from an estimated 5k.
- **Swim**: pace zones from CSS.
- The current "Z2 = 125–154 bpm" is a **30-bpm band** — too wide to be useful; it spans
  easy to genuinely moderate. Tighten Z2 once threshold HR is known, and state the max-HR
  / threshold-HR basis in `STATUS.md` (currently unstated). Keep one consistent zone
  system across the plan rather than mixing definitions.

---

## Load Management — Heat & Volleyball

- **Heat**: a long run was already cut short by heat (W26); training runs through a Vienna
  summer. Schedule long sessions **early AM**, carry fluids + electrolytes (~500–750 ml/h,
  add sodium on long efforts), and judge easy sessions by HR/RPE not pace when it's hot.
  Note: **the race is in May (likely cool)**, so summer heat is a *training-quality
  constraint to manage*, not a race adaptation to chase — don't sabotage key sessions
  proving a point in 35°C.
- **Volleyball** is real load (already treated as such) **and a real injury risk** —
  explosive lateral/jumping load on ankles and knees that could derail run/bike training.
  Treat a tweak as a red flag, not something to train through. Wednesday sessions end
  ~2026-07-29; as bike/run volume climbs in Build/Peak, deliberately wind volleyball down
  rather than stacking it on peak triathlon load.

---

## Notes for Session Startup

When starting a new session in this repository:

1. Read `STATUS.md` to find the current phase and last completed week.
2. Read `schedule/weekly-template.md` for the standing schedule.
3. Read `schedule/irregular-events.md` for upcoming blocks.
4. Pull recent Strava activities (last 3–4 weeks) to assess what was actually completed vs. planned.
5. Compare Strava data against the last 2–3 weekly plan files in `plans/weeks/`.
6. Generate the next 3–4 weeks of detailed plans based on: current phase targets above, actual completed load from Strava, and any upcoming irregular events.
