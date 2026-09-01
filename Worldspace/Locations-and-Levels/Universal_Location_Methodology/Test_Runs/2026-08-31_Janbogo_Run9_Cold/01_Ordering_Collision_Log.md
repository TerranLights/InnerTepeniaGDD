# Run 9 — Ordering Collision Log

**Written as the run happens, per `RESUME_HERE.md` §2b's instrumentation task.** Watching for: any point
where a check cannot complete inside the phase that owns it, whether or not it is on `03` §0.4's four-row
docket. The docket is the control; anything NOT on it is the actual finding. Also logging near-misses —
any moment a forward dependency was almost written and the docket had to be consulted to decide how.

**The docket, for reference (`03` §0.4):**
1. Internal-contradiction sweep (Gate 3) — owned by Phase 4, closes at Step 7.
2. Three-way differentiation set (`04` Part III) — owned by Phase 5, closes at Step 6.
3. Zodiac Lens person-shaped results — owned by Phase 10 §B2, closes at Step 5 (amends Phase 9).
4. Strongest-finding check (`01` §5.2 rule 4) — no single phase, closes at Step 5.

---

## Phase 0 (Frame)

**No close-order collision encountered.** Phase 0 produces no location content (`03`'s own governing rule
for this phase) and its own checks — the declaration block, generator selection, the inbound readiness
check — are all self-contained and complete-in-place. Nothing in Phase 0 referenced a later phase's
not-yet-written material.

**One near-miss, worth recording precisely because it easily could have become one.** While drafting the
symbol pairing read (§4 of `00_Frame_and_PreFlight.md`), the draft's first instinct was to write *"this
pairing reading will be confirmed once Phase 1's capability profile is complete."* That is exactly the
`03` §0.4 symptom shape (a forward-referencing sentence about a later phase). **Caught and rewritten**
before being saved: the pairing read is stated as an explicit, labeled **hypothesis** in Phase 0's own
output, with a plain note that Phase 0 does not produce location content and the hypothesis will be
*tested*, not *closed*, at Phase 1 — which is simply Phase 1 doing its own job, not Phase 0 deferring a
check it owns. **The distinction that mattered**: a deferred CHECK that Phase 0 itself owns would be the
bug; Phase 1 independently generating and comparing against Phase 0's stated hypothesis is the spine
working exactly as `02` §5 describes (run separately, then compare). No docket entry needed — recorded
here as a near-miss rather than a collision, per `RESUME_HERE.md`'s explicit ask for "any moment you wanted
to defer something and had to check the docket to decide how."

**Status: clean, with one caught near-miss.** What was watched for: any sentence of the shape "will be
verified/re-checked/finalized once Phase N is written," per the recorded Run 6 symptom text quoted in
`03` §0.4 itself.

---

## Phase 1 (Constraint & Capability)

**No close-order collision.** Four generators run to full profiles, compared, shape read, addresses read.
Several quadrants (G4 STANDING COST/GRUDGING TOLERANCE, G8 STANDING COST/GRUDGING TOLERANCE, two of four
address determinations) were explicitly left **ungrounded and marked REQUESTED/deferred to Step 3 research**,
rather than invented to fill the slot. **This is the correct behavior per `05` §1 (REQUESTED as an output
type) and is not a close-order collision** — nothing here depends on a *later phase's* material; it depends
on research not yet performed, which is Phase 1's own next step (`03` PHASE 1 process item F, "then research
the deficit"), not a forward reference to Phase 5–10.

**One genuine near-miss, sharper than Phase 0's.** The Shape reading section's first draft asserted
"cost-dominant" as a settled reading. Caught mid-draft: `02` §4.0 requires the shape to be reported **with
its input set**, and two of the four generators feeding STANDING COST were still ungrounded at the moment of
writing. **This was not a forward-phase dependency** (the §0.4 bug) — it was the ordinary §4.0 discipline
(never report a shape without its input set) catching an attempt to finalize before the input set was
actually complete. Rewritten as "provisional, at risk of the §4.0 trap, will be re-checked once Step 3
research fills the ungrounded cells." **Distinguishing this from a true §0.4 collision mattered**: a §0.4
collision would be "Phase 1 cannot close until Phase 5 exists"; this is "Phase 1's own Step 2 cannot fully
close until Phase 1's own Step 3 runs" — entirely within-phase, not a docket item at all.

**Status: clean.** No docket entry. One within-phase discipline catch, logged because it superficially
resembles the pattern being watched for and the distinction is worth having stated explicitly.

**Phase 1 Step 3 (research) and the Unrecognized Instrument, run to close Phase 1 out:** no collision.
The Unrecognized Instrument returned NULL with a stated reason (thin admissible institutional detail after
M-64/M-65) rather than being deferred to a later phase on the theory that a later phase would supply the
missing material — it is recorded as this phase's own honest result, closed, with a note to *re-run* the
technique later if new admissible material appears, which is different in kind from leaving Phase 1 open
pending that material. Phase 1 is CLOSED, not blocked.

---

## Phase 2 (Composition & Arrival)

**No collision.** Borrowed Form (step D) was correctly left for whichever later phase produces an empty
category, which is ordinary forward-pointing per `03`'s own procedure, not a check Phase 2 owns. The
differentiation axis was explicitly marked "not yet checked against any sibling" and routed to Gate 6 at
Step 7 by name, rather than either skipped silently or used to justify holding Phase 2 open. **Status:
clean.**

---

## Phase 3 (Surface & Texture)

**No collision.** The seam finding (§D) named a REQUESTED naming/detail question (what the founding core is
called now) rather than inventing a proper name or leaving the phase open pending a later phase supplying
one — correct per `05` §3's reservation rule, and distinct in kind from a forward-phase dependency. The
Retroactive Mechanism null (§F) was recorded as a genuine result of thin surviving material, not deferred.
**Status: clean.**

---

## Phase 4 (Ordinary Life) — DOCKET ROW 1, the control case

**This is `03` §0.4's own docket row 1, hit directly and on purpose**: Gate 3 (internal-contradiction sweep)
is owned by Phase 4 but closes at Step 7. **Handled per the rule**: Phase 4 checked backward against Phases
1–3 only (every element traced explicitly to a named Phase 1/2/3 finding, see the phase file's own text) and
was marked CLOSED, with an explicit note that the Phases 5–10 sweep runs at Step 7 and this phase is not
held open pending it. **No forward-dependency language was written** — no sentence of the "will be
re-checked once Phase N exists" shape appears anywhere in the phase file. **This is the exact symptom Run 6
originally produced** (`03` §0.4's own quoted instance), now run correctly on a second, independent
location. **Status: clean — docket row 1 confirmed working, not merely present in the rules.**

---

## Phase 5 (Relation & Geometry) — DOCKET ROW 2 territory

**`03` §0.4 docket row 2**: the three-way differentiation set, owned by Phase 5, closes at Step 6. **Handled
correctly, and in an interesting variant this docket's own text does not explicitly anticipate.** Janbogo has
a genuine close peer (Zukelli) — unlike the typical isolated-location case the own-eras substitute exists
for — so 5b had a real choice between (a) a full two-city write-together comparison (`04` Part III.3's "set
of two" mode) and (b) the own-eras substitute anyway. **The phase file explicitly declined option (a)** —
naming it "a legitimate follow-up task... out of this run's scope" rather than either forcing it now or
silently deferring it to Step 6/7 as unfinished — **and ran the own-eras substitute instead, in full, now**,
per `01` §5.3a's own standing preference to run the own-eras set even when peers exist. **No forward
dependency was written.** The genuine two-city Zukelli/Janbogo comparison remains open, but it is scoped as
future *additional* work, not as a check Phase 5 itself owes and is withholding — the distinction that
matters for §0.4 purposes. **Status: clean, with a scope note rather than a collision.**

---

## Phase 6 (Meaning)

**No collision.** Multiple REQUESTED items left open (robot-religion presence, the Failure State's
institutional answer, an unserious observance) — each stated as a request per `05` §5, not as a forward
dependency on a later phase. **Status: clean.**

---

## Phase 7 (Order)

**No collision.** The G8-linked counterculture candidate (7d) was deliberately left underdeveloped rather
than deferred to a later phase to "finish" — a scope decision within Phase 7's own discretion (avoiding
reconstruction of excluded material), not a forward dependency. **Status: clean.**

---

## Phases 8–9 (Making, Populations)

**No collision in either.** Both phases recorded their own honest thinness (Making) and a swap-test failure
against a specific peer (Populations) as *results*, not as reasons to hold the phase open pending later
material. Phase 9's swap-test note explicitly names what a LATER gate (Gate 6, Step 7) will need to address,
but does not defer Phase 9's own closure to that gate — the distinction that keeps this clean rather than a
§0.4 violation. **Status: clean, both phases.**

---

## Phase 10 (Catalog, base — Zodiac Lens run separately)

**No collision**, but a second instance of M-66's exact pattern was caught and handled the same way: the
wind-warning institution candidate could not be catalogued without either reusing a name this session was
exposed to while excluding a file (M-65), or inventing a differently-named institution serving the same
function (indistinguishable in effect). **Flagged as REQUESTED with the provenance issue stated explicitly**,
cross-referenced to M-66, rather than resolved by quietly picking one option. This is not a §0.4 ordering
collision — it is the identical epistemic-contamination problem M-66 already named, recurring on a second
finding, which is itself worth noting as a pattern: **the M-66 bind is not a one-off; expect it to recur
anywhere an excluded file was read closely enough to identify what it excluded.** **Status: clean.**

---

## Zodiac Lens (base + Extension + cross-sign synthesis) — DOCKET ROW 3

**`03` §0.4 docket row 3**: Zodiac Lens person-shaped results, owned by Phase 10 §B2, close at Step 5 as an
amendment to Phase 9. **Handled correctly**: the cross-sign synthesis file explicitly states "per-sign
person-shaped results are NOT yet folded into Phase 9 — that fold happens at Step 5 (Reconciliation), per
`03` §0.4's own docket row 3, next." No subagent or the coordinating pass wrote a forward-dependency sentence
about Phase 9 needing to wait — the technique ran to completion at Phase 10's own slot, produced its output,
and named exactly where that output closes, matching the docket precisely. **Status: clean — docket row 3
confirmed working, the third of four docket rows now verified on this run alone.**
