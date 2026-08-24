# Training Status

_Last updated: 2026-08-24_

## Current State

| Field | Value |
|-------|-------|
| Phase | Base (Phase 1) |
| Phase week | 11 of 15 (W35) |
| Plan week | 2026-W35 (Aug 24–30) — peak of the W33–35 load triple; 2nd brick |
| Loading cycle | 3:1 in Base/Build. **W33–35 = loading triple (current) → W36 deload + tests.** Then **W37–38 load → W39 camp (absorbs deload) → W40 Build-1 re-entry** |
| Weeks to race | ~39 |

## Fitness Snapshot (from Strava, reviewed 2026-08-04)

| Metric | Value | Source |
|--------|-------|--------|
| 5k | **20:40** (real, Silvesterlauf 2025-12-31) — Strava now predicts ~20:47, i.e. holding | Race + Strava. HRmax 192, threshold HR ~178 measured that day |
| **FTP** | **238W** (3.45 W/kg @ 69kg) | Tested 2026-07-03. **Retest W36, Sep 5** (fresh legs → may read higher) |
| Swim | **Progressing fast** — now **2×500m continuous** (Aug 21), pyramids to 400m; 3×/week held | Strava. From zero on Jul 11 |
| Long run (recent) | 21km (Aug 16), **23.3km (Aug 23)** @ Z2 | Strava — very consistent, volume creeping up |
| Long ride (recent) | 100km/733m (Aug 15), 104km/828m (Aug 22) | Strava — above plan; strong cyclist confirmed |
| Mid-week bike | ✅ **Old gap fixed** — sweet-spot done W33 (2×15) + W34 (3×12) @ 210–225W, power held | Strava |

### Bike Power Zones (Coggan, FTP 238W — set 2026-07-03)

| Zone | Watts | | Zone | Watts |
|------|-------|-|------|-------|
| Z1 Recovery | ≤131 | | Z4 Threshold | 215–250 |
| Z2 Endurance | 132–179 | | Z5 VO2 | 251–286 |
| Z3 Tempo | 180–214 | | Z6 Anaerobic | 287–357 |

Sweet-spot (88–94%) = **209–224W**. **Race bike target: NP ~178–186W (IF ~0.75–0.78),
surges to ~215–225W on climbs only.** Zones refresh after the W36 FTP retest.

### Run Zones (anchored to real data — Silvesterlauf 5k, 2025-12-31)

Re-derived 2026-08-04 from a real maximal effort: **HRmax ≈ 192, threshold HR ≈ 178**
(5k race avg HR 180, max 192, ~4:08/km). This replaces the max-formula bands.

| Zone | HR (bpm) | Pace (/km) |
|------|----------|-----------|
| Z1 Recovery | <135 | >5:45 |
| Z2 Endurance | 135–155 | 5:00–5:45 |
| Z3 Tempo | 156–168 | 4:35–5:00 |
| Z4 Threshold | 169–178 | 4:15–4:35 |
| Z5 VO2 / 5k | 179+ | <4:15 |

These are well-anchored: the summer Z3 tempo runs (160–166 bpm) were prescribed submaximal
and correctly sit *below* threshold — consistent with LTHR ~178, confirming threshold is
above ~166. No contradiction, no test needed. The only residual uncertainty is slow drift
since December (fitness has climbed), so recheck opportunistically — a hard parkrun/30-min
effort anytime updates the threshold line. HR/RPE wins on conflict.

---

## Recent Reviews

Full dated Strava-vs-plan reviews now live in [`logs/reviews.md`](logs/reviews.md) — this
file stays a current-state snapshot.

- **Latest (W33→W34, 2026-08-24):** adherence excellent; the W28→W32 gaps are closed and the
  mid-week quality-bike gap is fixed. ⚠️ Open items carried into Next Actions: **OW block
  behind** (prioritize W37/W38 Fri swims) and a **long-run HR wobble on Aug 23** to watch.

---

## Next Actions

- [ ] **W36 FTP retest (Sat Sep 5)** — 20-min test on fresh legs → reset power zones (still worth it: the 238W was on tired legs)
- [~] Run threshold test — **downgraded to optional** (2026-08-04). Run zones now anchored to the real Dec 31 5k (HRmax 192 / threshold ~178). A hard parkrun or 30-min effort anytime would confirm the current threshold-HR line; no scheduled test needed
- [x] ~~Protect the Thursday sweet-spot ride~~ — ✅ done W33/W34, gap closed
- [ ] **Prioritize open-water swims on W37/W38 Fridays** — OW block behind (Aug OWS became pool swims); season closes ~Oct and the camp costs a week
- [ ] Schedule the first **swim CSS test** (400m + 200m TT) — overdue per macro cadence;
  continuous 500m is now comfortable, so slot it ~W37 (a good re-entry benchmark)
- [~] **Indoor smart trainer arrived ~Aug 2026** (ahead of the Oct 31 deadline) — now **set it up + do shakedown rides before Build 2** (ADR 0004); target online ~mid-Sep–Oct
- [ ] After W36 tests: update this file's zones, re-derive sweet-spot/tempo bands + run pace

## Detailed Plans Generated

| Week | File | Status |
|------|------|--------|
| 2026-W33 | plans/weeks/2026-W33.md | ✅ Done — sweet-spot bike landed; OW → pool |
| 2026-W34 | plans/weeks/2026-W34.md | ✅ Done — Thu sweet-spot protected; OW → pool |
| 2026-W35 | plans/weeks/2026-W35.md | **Current** — peak of triple; 2nd brick; 2×20min sweet-spot |
| 2026-W36 | plans/weeks/2026-W36.md | Upcoming — DELOAD + run test (Sep 1) + FTP retest (Sep 5) |
| 2026-W37 | plans/weeks/2026-W37.md | Written — **new 3+3 structure debuts**; final base load wk1; prioritize OW Fri |
| 2026-W38 | plans/weeks/2026-W38.md | Written — final base load wk2; eased weekend into camp; last OW |
| 2026-W39 | plans/weeks/2026-W39.md | Written — **VB CAMP (Sep 21–28)**; no tri training; absorbs deload |
| 2026-W40 | plans/weeks/2026-W40.md | Written (**provisional**) — Build-1 cautious re-entry post-camp |

_Next to write: **W41+ (real Build 1 progression)** — write after the camp (any niggles?) and
after the Sep 5 FTP retest re-anchors bike zones. W40 is provisional and should be refined then._

**⚠️ New weekly structure effective W37 (2026-08-24):** week reorganized to **3 swim / 3 bike /
3 run**. Changes vs. W33–36 (which keep the old layout): swim moved Tue→**Mon**; **Tue PM =
easy ~1h ride** (3rd bike); upper-body gym moved Mon→**Thu afternoon** (after the quality bike);
**Fri = easy/short 3rd run, skipped in brick weeks**. Wed lower gym + Thu quality bike + Sat
long ride + Sun long run all unchanged. The Tue ride and Fri run are *easy volume* — cut order
if overloaded: Fri run first, then Tue ride. See `schedule/weekly-template.md`. When writing
W37+, note this pushes to 3+3 bike/run vs. the macro's written 2+2 — watch total load after
the deload, especially with the heavy strength block continuing.

## Milestone Status

| Milestone | Status |
|-----------|--------|
| FTP Test | ✅ Done 2026-07-03 — 238W. **Retest W36 (Sep 5)** |
| Swim technique course | ✅ Completed 2026-07-11→17 |
| First structured swim | ✅ Done W30 (Jul 20/24) |
| Swim → 3×/week | ✅ Begins W32 (Wed slot, post-volleyball) |
| First brick session | ✅ Done 2026-08-01 (W31) — 90km + 4km run |
| First open water swim | ✅ Done 2026-07-27 (W31) — 594m; OW block 1 continues |
| Run threshold field test | Optional — zones anchored to real Dec 31 5k (HRmax 192). Confirm opportunistically via parkrun/hard 30min |
| Swim CSS test | Pending — schedule late Aug/early Sep |
| Race day | 2027-05-23 |
