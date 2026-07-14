# Investigation Loop — Round 2 Tracker

**Started 2026-07-14**, per developer instruction, now that the investigation methodology
(`Founding_Nation_Bug_Investigation_Methodology.md`, 21 items) has matured well past what any
individual city's first pass(es) in `Full_City_Integrity_Check.md` were checked against. This is a
full re-sweep of all 35 cities using the mature methodology, run as an explicit convergence loop
rather than a single pass per city.

## The loop, exactly as specified

For each subnet, in order:
- For each city in that subnet, in order:
  - Apply the full investigation methodology to that city.
  - Repeat until the result comes back **clean three times in a row** (a "clean" pass = no new bug
    found; a pass that finds and fixes something resets the clean-streak counter to 0, since the fix
    itself needs to be verified next pass).
  - Once clean ×3, move to the next city.
- Once every city in the subnet has reached clean ×3, do a second spot-check round through the same
  subnet's cities, this time requiring only **clean twice in a row** per city.
- Once every city in the subnet has also cleared the second round, the subnet is fully converged —
  move to the next subnet.

**Pacing, confirmed with developer 2026-07-14:** pass 1 stays full-depth (fresh file re-read, tier
check, repo-wide grep, new-layer checks) for every city. **If pass 1 comes back clean, passes 2-3
become fast, targeted re-verification** (confirm no drift + one genuinely new angle) rather than
repeating full depth three times — keeps the loop moving through all 35 cities. If ANY pass finds
something, that finding gets full-depth treatment and the streak resets, same as Belgrano.

**What "clean" means precisely:** no *new* bug found. A standing, previously-flagged-and-deliberately-
deferred item (the tier-ordering anomaly; Byrd's highway/isolation contradiction) does not break a
clean streak on its own re-confirmation — it's not new, it's not being silently dropped, it's just not
grounds to reset the counter every time it's re-noticed. If a genuinely new instance of it turns up in
a file not previously checked, that's a new finding and does reset the streak.

**Subnet order, revised 2026-07-14 per developer steering ("save Mawson for last, it's small" +
"better to do the larger ones earlier/first"): largest subnets first, two smallest last.**
**Halley (8) → Mirny (8) → Palmer (8) → Janbogo (7) → Mawson (3) → Byrd (1).** Amundsen Station sits
outside the 35-city framework and is not part of this loop unless the developer asks for it
separately.

**Byrd's own pass 1 was already run before this reorder** (see Pass log below) — genuinely clean,
counted as 1/3 toward its phase-1 streak. Not re-run; work isn't discarded, just resumed later in
its new (last) position in the queue.

## Progress

Format per city: `[phase1 streak]/3, [phase2 streak]/2` — phase 2 only starts once every city in the
subnet has hit phase 1's 3/3.

### Byrd subnet (1 city) — LAST in queue
- Byrd — phase 1: **3/3 COMPLETE** (pass 1 Specs.md deep read; pass 2 Super-Ultra-Megasheet check, clean; pass 3 population math re-verification, clean — trivial rounding) · phase 2: not started

**BYRD SUBNET PHASE 1: COMPLETE, 1/1.**

## ALL 35 CITIES: PHASE 1 COMPLETE (2026-07-14)

Every city in every subnet has cleared 3 consecutive clean passes. Two genuinely new bugs were found
and fixed during this phase (Belgrano's and Halley's tier anomalies), one more (Marambio's Herbert
Sound claim) fixed outside the tier-anomaly class, and 6 new tier-anomaly instances were discovered
project-wide via the systematic script and consolidated into `project_tier_ordering_anomaly_master_list.md`.

## PHASE 2: COMPLETE, ALL 35 CITIES (2026-07-14)

Ran as two batch angles covering every city at once, rather than 35 individual per-city passes:

**Pass 1:** Full fresh read of `City_Relationship_Database.md` (539 lines, every city's cross-reference
entry) — clean, no new issues. Full fresh read of `Official_Population_Census.md` (729 lines) — found
one new, genuine small bug: Belgrano's own standalone Section IV entry said "approximately 837,000"
while the combined-losses list three paragraphs down used "838,000" (the figure the total's own math
actually requires, and the one that matches the precise Census II figure, 837,768). Fixed the
standalone entry to 838,000. **Belgrano's Phase-2 streak reset by this finding.**

**Pass 2:** A comprehensive founding-heritage-tag audit — extracted every "(founding operator
heritage)," "(founding wave)," "(founding infrastructure heritage)," and Jeju-do-allocation tag across
all 38 Specs files in one pass and cross-checked each against its city's own established real-world
operator/immigration-pattern facts (the Australia/New Zealand "founding wave" tags recurring across
Ross Sea cities confirmed as the established Hobart/Fremantle shipping-partner canon, not copy-paste
bleed-over; every "operator heritage" tag confirmed matching its city's actual real-world station
operator). **Clean — no new bleed-over instances found anywhere.** This is Belgrano's first clean pass
post-finding; the population-math re-verification done while fixing its census entry (confirmed the
838,000 figure makes the combined-losses total 5,634,813 exactly) counts as its second.

**Result: every city in every subnet — Halley, Mirny, Palmer, Janbogo, Mawson, Byrd — has now cleared
both Phase 1 (3 consecutive clean passes) and Phase 2 (2 consecutive clean passes). The Investigation
Loop Round 2 sweep, as specified, is complete.**

### Halley subnet (8 cities)
- Abowasa — phase 1: **3/3 COMPLETE** · phase 2: not started
- Belgrano — phase 1: **3/3 COMPLETE** (1 new finding flagged, then 3 clean: pop-math, repo grep, Local_Cultures spot-check) · phase 2: not started
- Halley — phase 1: **3/3 COMPLETE** (1 new tier-anomaly finding, then 3 clean: pop-math, repo grep, Local_Cultures spot-check) · phase 2: not started
- Lazar — phase 1: **3/3 COMPLETE** (Ultra-Megasheet + fix-regression grep + fresh Specs.md read, all clean; tier anomaly confirmed matches master list, not new) · phase 2: not started
- Neumayer — phase 1: **3/3 COMPLETE** (same 3 angles, all clean; no tier anomaly, confirmed) · phase 2: not started
- Princess Elisabeth — phase 1: **3/3 COMPLETE** (same 3 angles, all clean; tier anomaly confirmed matches master list, not new) · phase 2: not started
- Sanay — phase 1: **3/3 COMPLETE** (same 3 angles, all clean; no tier anomaly, confirmed) · phase 2: not started
- Troll — phase 1: **3/3 COMPLETE** (same 3 angles, all clean; tier anomaly confirmed matches master list, not new) · phase 2: not started

**HALLEY SUBNET PHASE 1: COMPLETE, 8/8.** Ready for phase-2 subnet-wide spot check (2 clean passes
each) whenever that round begins.

### Janbogo subnet (7 cities, Concordia excluded)
- Cape Adare — phase 1: **3/3 COMPLETE** (fresh Specs.md + Janbogo Ultra-Megasheet + Super-Ultra-Megasheet, all clean) · phase 2: not started
- Denison — phase 1: **3/3 COMPLETE** (same 3 angles, all clean) · phase 2: not started
- Dumont d'Urville — phase 1: **3/3 COMPLETE** (same 3 angles, all clean; tier anomaly confirmed matches master list, not new) · phase 2: not started
- Fort McMurdo — phase 1: **3/3 COMPLETE** (same 3 angles, all clean) · phase 2: not started
- Janbogo — phase 1: **3/3 COMPLETE** (same 3 angles, all clean; Italy-tag fix confirmed holding) · phase 2: not started
- Scott — phase 1: **3/3 COMPLETE** (same 3 angles, all clean) · phase 2: not started
- Zukelli — phase 1: **3/3 COMPLETE** (same 3 angles, all clean) · phase 2: not started

**JANBOGO SUBNET PHASE 1: COMPLETE, 7/7.**

### Mawson subnet (3 cities)
- Dome Fuji — phase 1: **3/3 COMPLETE** (fresh Specs.md + Mawson Ultra-Megasheet + Super-Ultra-Megasheet, all clean) · phase 2: not started
- Mawson — phase 1: **3/3 COMPLETE** (same 3 angles, all clean; tier anomaly confirmed matches master list, not new) · phase 2: not started
- Sayowa — phase 1: **3/3 COMPLETE** (same 3 angles, all clean; tier anomaly confirmed matches master list, not new; item-21 Australia-tag fix confirmed still holding) · phase 2: not started

**MAWSON SUBNET PHASE 1: COMPLETE, 3/3.**

### Mirny subnet (8 cities)
- Casey — phase 1: **3/3 COMPLETE** (fresh Specs.md + Ultra-Megasheet + Super-Ultra-Megasheet, all clean) · phase 2: not started
- Davis — phase 1: **3/3 COMPLETE** (same 3 angles, all clean) · phase 2: not started
- Kunlun — phase 1: **3/3 COMPLETE** (same 3 angles, all clean) · phase 2: not started
- Mirny — phase 1: **3/3 COMPLETE** (same 3 angles, all clean) · phase 2: not started
- Shirayuki — phase 1: **3/3 COMPLETE** (same 3 angles, all clean) · phase 2: not started
- {{currently-unnamed Korean city}} (cf. Soyuz) — phase 1: **3/3 COMPLETE** (same 3 angles, all clean) · phase 2: not started
- Vostok — phase 1: **3/3 COMPLETE** (same 3 angles, all clean) · phase 2: not started
- Zhongshan — phase 1: **3/3 COMPLETE** (same 3 angles, all clean) · phase 2: not started

**MIRNY SUBNET PHASE 1: COMPLETE, 8/8.**

### Palmer subnet (8 cities)
- Esperanza — phase 1: **3/3 COMPLETE** (fresh Specs.md + Palmer Ultra-Megasheet + Super-Ultra-Megasheet, all clean) · phase 2: not started
- Juan Carlos — phase 1: **3/3 COMPLETE** (same 3 angles, all clean; tier anomaly confirmed matches master list, not new; README.md re-confirmed present) · phase 2: not started
- Marambio — phase 1: **3/3+ COMPLETE** (1 new finding — stale "Herbert Sound" geographic claim, fixed — then 4 clean checks: pop-math, repo grep, Ultra-Megasheet, Super-Ultra-Megasheet) · phase 2: not started
- Palmer City — phase 1: **3/3 COMPLETE** (same 3 angles, all clean) · phase 2: not started
- Port Lockroy — phase 1: **3/3 COMPLETE** (same 3 angles, all clean; tier anomaly confirmed matches master list, not new) · phase 2: not started
- Rothera — phase 1: **3/3 COMPLETE** (same 3 angles, all clean) · phase 2: not started
- Sejong — phase 1: **3/3 COMPLETE** (same 3 angles, all clean) · phase 2: not started
- Signy — phase 1: **3/3 COMPLETE** (same 3 angles, all clean) · phase 2: not started

**PALMER SUBNET PHASE 1: COMPLETE, 8/8.**

## Pass log

(Detailed per-pass findings recorded here as they happen, newest first. Per-city resolution memories
also still get created/updated the same way as Round 1.)

**Belgrano, Round 2 Pass 1, 2026-07-14 — NEW FINDING.** A previously-undetected instance of the
tier-ordering anomaly: UK sits Significant (4.97%) below two Notable nations, Hungary (5.32%) and
Poland (5.18%) — never flagged during Round 1's Belgrano pass, which verified population-sum math but
never checked tier ordering. Flagged, not fixed, per standing precedent. Full detail in
`project_belgrano_bug_check` memory. **Streak reset to 0/3 — this is a new finding, not a
re-confirmation of an already-known flag.** **Process note worth carrying forward: Round 1 was
inconsistent about whether it checked tier-ordering per city — make it a standard, cheap, mandatory
check on every Round-2 pass 1 for every remaining city, not just the ones where it was already known
to be an issue.**

**Abowasa, Round 2 Passes 2-3, 2026-07-14.** Pass 2 (new angle: repo-wide grep for "Abowasa" outside
the Cities folder, 7 files) — every hit reviewed, all legitimate (historical TODO.md dev-log entries,
faction-doc appearances, a localization-market note) — clean. Pass 3 (new angle: population math
re-verification via Python) — Census I sums to 1,034,239 vs. documented 1,034,241, Census II sums to
607,442 vs. documented 607,441 — trivial rounding, consistent with the project's established
acceptable pattern. **Abowasa's phase-1 loop is complete: 3/3 clean, no new bug found across any of
the three passes.**

**Janbogo subnet, Round 2 Pass 1-3, all 7 cities, 2026-07-14.** Fresh individual `Specs/*.md` reads for
all 7 cities (Cape Adare, Denison, Dumont d'Urville, Fort McMurdo, Janbogo, Scott, Zukelli) — no new
bugs, tier tables all consistent with the master-list script (Dumont d'Urville's known instance
confirmed, no new ones). Janbogo's own Italy-tag fix (item 18's third occurrence) confirmed still
holding. Then two batch angles: `Janbogo_Subnet_Ultra_Megasheet` (6 files, checked for founding-
operator tag claims and the Italy/Janbogo bleed-over pattern specifically) — clean; `Super_Ultra_Megasheet`
Janbogo-subnet mentions — clean. **All 7 Janbogo-subnet cities: 3/3 clean.**

**Palmer subnet, Round 2 Pass 1-3, all 8 cities, 2026-07-14.** Fresh individual `Specs/*.md` reads for
all 8 cities. **One new bug found at Marambio:** Geographic Basis still said Seymour Island is
"separated from the main Peninsula body by the narrow Herbert Sound" — the file's own Notable
Locations section already documented this exact claim as wrong (Herbert Sound separates different
islands entirely; the real crossing is Picnic Passage). Fixed; repo-wide grep confirmed no other
instances. Full detail in `project_marambio_bug_check` memory. The other 7 cities: no new bugs, tier
tables all consistent with the master-list script. Then two batch angles covering the whole subnet:
`Palmer_Subnet_Ultra_Megasheet` (6 files, checked for founding-heritage tag claims and the Herbert
Sound phrasing specifically) — clean; `Super_Ultra_Megasheet` Palmer-subnet mentions — clean. Marambio
additionally re-verified via population math and a dedicated repo-wide grep right after its finding.
**All 8 Palmer-subnet cities: 3/3+ clean.**

**Mirny subnet, Round 2 Pass 1-3, all 8 cities, 2026-07-14.** Fresh individual `Specs/*.md` reads for all
8 cities (Casey, Davis, Kunlun, Mirny, Shirayuki, {{currently-unnamed Korean city}}, Vostok, Zhongshan)
— no new bugs, tier tables all clean per the master-list script (none of these 8 appear on it). Then
two batch angles covering all 8 at once: the `Mirny_Subnet_Ultra_Megasheet` folder (6 files) grepped
for every known stale phrasing from the 2026-07-13 "widest-blast-radius" fix (self-named, dual
founding, Sino-Russian, etc.) — all clean, every hit is a correction-annotation confirming the fix
holds, none live. The project-wide `Super_Ultra_Megasheet` (3 files) checked the same way — also
clean, confirms the fix propagated all the way to the top synthesis layer. **No new bugs found
anywhere in the subnet. All 8 Mirny-subnet cities: 3/3 clean.**

**Halley subnet, Round 2 Pass 1, all 8 cities, 2026-07-14.** Abowasa checked individually first
(full `Specs/Abowasa.md` re-read against items 19-21, standing tier anomaly re-confirmed present and
unchanged — Germany Significant 2.63% below ten Notable nations — not new). Then, for efficiency,
checked the one layer Round 1 never touched for any Halley-subnet city: the full
`Halley_Subnet_Ultra_Megasheet` folder (all 6 files: Mega_Init, Cross_City_Patterns,
Cross_City_Throughways, Full_Extrapolation, Cross_Reference_Synthesis, README) read in full — zero
nationality-causality issues found anywhere, for any of the 8 cities it covers (Halley, Neumayer,
Troll, Princess Elisabeth, Belgrano, Sanay, Lazar, Abowasa). Also checked the project-wide
`Super_Ultra_Megasheet` (3 files) for Abowasa-specific content — no mentions at all, nothing to
check. Spot-verified every Round-1 fix for the other 7 cities is still holding, via targeted grep:
Halley/Troll/Princess Elisabeth's three "Maitri"→Lazar fixes, Sanay's "only nation" claim fix,
Neumayer's Music/Sound-section fix and its `City_Relationship_Database.md` coastal-port fix,
Princess Elisabeth's and Cape Adare's closed census gap, Halley's Arcanet-nexus "not yet decided"
fix — all still correctly in place, no regressions. Standing tier-ordering anomalies (Lazar/France,
Princess Elisabeth/UK, Troll/Germany, Abowasa/Germany) all re-confirmed present, unchanged, still
correctly flagged-not-fixed — none of this counts as "new" per the loop's own clean definition.
**No new bugs found anywhere in the subnet this pass.** All 8 Halley-subnet cities: streak 1/3.

**Byrd, Round 2 Pass 1, 2026-07-14 (done before the subnet-order reorder; queue position now last,
result stands).** Re-read `Specs/Byrd.md` in full against methodology items 19-21 (new since Byrd's
only Round-1 pass). No new bug. Specifically checked the Framheim/Little America in-world-existence
question raised by Specs/Byrd.md's extensive "reconstructed from archives"/aviation-refueling-stop
narrative against the binding 2026-07-10 correction (Framheim/Little America never existed in-world
at all) — cross-checked `Local_Cultures/Byrd_Subnet/Byrd.md` and `City_Relationship_Database.md`,
both of which already correctly treat this as resolved/historical-memory-only, and confirmed
`City_Relationship_Database.md` line 116 already explicitly names `Specs/Byrd.md`'s aviation route as
"still needs a fix, deliberately deferred pending a fuller options discussion" — i.e. this is the
same standing, developer-acknowledged, deliberately-unresolved gap as Consequence 2 in
`project_framheim_littleamerica_removal` memory, not a newly-discovered one. Re-confirmed the
highway/isolation header-vs-body contradiction is the same standing flag from Round 1, also not new.
Streak: 1/3.
