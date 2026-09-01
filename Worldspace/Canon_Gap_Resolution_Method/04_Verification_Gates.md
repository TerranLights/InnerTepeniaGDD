# Verification Gates, and the Live-File Schemas

> **⚠ Read `00_RUNBOOK.md` first.** These are its Step 8.

**Seven gates. Five descend from a specific recorded failure in this project; two are prospective and are
marked as such** — because a gate claiming a pedigree it does not have is exactly the kind of unearned
authority this project's own methodologies refuse to grant themselves.

*(Count corrected 2026-08-31: this header read "six" after Gate 7 was added — a completion claim that no longer
matched its own file, which is precisely the mismatch Gate 0 exists to catch, occurring inside the gate
document itself.)*

---

## Gate 1 — Premature closure *(prospective — no recorded instance yet)*

**Checks LAW A.** For every gap this run closed: **was it genuinely LIVE, or was it SCHEDULED, RESERVED, or
load-bearing-open?**

**Run it by re-reading the original flag's own wording**, not your triage note about it. The phrase *"TBD for
DLC 3 design"* means a later stage owns it; a triage note reading "TBD, open" has already lost that.

**Honest pedigree:** **no instance of premature closure has yet been recorded in this project**, because no
system has previously existed whose job was closing gaps. This gate is built from an empirical pattern rather
than a scar: a scan of one city's Specs file found nearly every TBD in it scheduled to a downstream stage.
**The risk is structural and predictable; the failure has simply not happened yet, and this gate exists so it
does not.**

**Report format:** every run states what it declined to close and why, alongside what it closed. **A run
reporting only closures fails this gate automatically.**

## Gate 2 — Wrong-tier deposit *(recorded: the Cape Adare deposit chain, M-51)*

**Checks LAW B.** For every deposit: **is its KIND correctly classified, and does its destination match?**

**Run it as the reverse question, which is sharper:** *if a cold synthesis pass read this destination file six
weeks from now, would it mistake anything I just wrote for an attribute?*

**Mechanical half, and it should be run mechanically:**
```bash
grep -n "CGRM:CONCLUSION-TIER" <every file this run touched>
```
**Every conclusion deposited into an attribute-tier file must return a marker pair. A conclusion deposit with
no marker is a Gate 2 failure regardless of how true it is.**

**Pedigree:** fully documented, eight weeks end to end — a Vision Notes session deposited civic-character
content into `Specs/Cape_Adare.md` on 2026-07-05; a cold location pass cleared that file as attribute-tier on
2026-08-31 and found the contamination only by reading further than the check required.

## Gate 3 — Derivation integrity *(recorded: the shared-constant error; the census column error)*

**Runs on Path 2 output only.**

1. **Was every input verified at its own source, not at a neighbor that agreed with it?** *(Recorded: a wrong
   era-length sat in 20 files across 8 locations, used as a causal premise in all of them. Every file agreed
   with every other file — so consistency-checking between them passed while all of them were wrong.
   **Agreement among siblings is not corroboration.**)*
2. **Was one row hand-checked against the source table?** *(Recorded: a census parse indexed the wrong column
   and returned 33 plausible rows, a sensible mean, and a sensible spread — all wrong. It did not error. **A
   plausible number does not invite suspicion the way a zero does.**)*
3. **Are comparative claims scored against the full set, as a z-score, rather than against a local group?**
4. **⚠ State what the numerator and the denominator each actually REPRESENT, before trusting the quotient.**
   *(Added 2026-08-31, from a real error inside this system's own first acquisition run.)* A density figure was
   computed correctly from verified inputs against a correct comparison set — and was still wrong, because it
   divided a whole population by a *downtown core* and read the result as the city's density, producing a false
   6.7× "implausibility" that dissolved once the frame was corrected. **Every input can be right and the figure
   still meaningless if the two quantities do not mean what the check assumes.** Checking inputs is not the
   same as checking framing.
5. **If a corrected figure was carrying an argument, was the argument rebuilt rather than renumbered?**
   *(Recorded: a cuisine finding justified by a "six-month polar night" survived a correction to ~60 days by
   swapping the number, leaving a weak claim standing. The real constraint was both different and stronger.)*

## Gate 4 — Research legitimacy *(recorded: the Sejong and Abowasa cases)*

**Runs on Path 4 and Path 5 output only.**

1. **GPS-only.** Is any real-world nationality being used as a *cause* rather than a location fact? **Sort into
   the three buckets before accepting:** station operator *(GPS only, never causal)* · the location's own
   current population table *(legitimately causal)* · essentialist national temperament *(always banned)*.
2. **The continuity check** — the specific form both recorded failures took: **does the claim assume cultural
   or demographic continuity from a real-world station's naming era through to Tepenian founding?** It cannot.
   The ~500-year First Interwar Period saw stations change national hands repeatedly.
3. **Divergence stated**, not resemblance implied.
4. **Did the research change a finding or merely ornament one?** Both are honest; they are not the same, and a
   100% change-rate should be checked rather than celebrated.

**Pedigree:** one city's attributes file asserted a continuous Korean cultural institution from its station's
name; another city's *entire founding narrative* rested on the same invalidated premise. **Both were written
after the project's audit sweep had closed, and nothing caught either for weeks** — which is also Gate 5's
whole reason for existing.

## Gate 5 — Provenance completeness *(partially grounded)*

**Every deposit carries a `[CGRM …]` tag naming date, path, and source.**

**Why this is a gate and not a style note:** an untagged deposit is **permanently indistinguishable from
pre-existing canon.** A later session cannot tell a researched fact from an assumed one, cannot re-verify it
without redoing the work, and — critically — **cannot find it in an audit.** The recorded blind spot this
protects against is real and named: *the sweep does not cover content created later.* **A tagged deposit is
findable in one command; an untagged one joins the corpus invisibly and is never checked again.**

```bash
grep -rn "CGRM" .    # every deposit this system has ever made, anywhere
```

## Gate 6 — Scope discipline *(grounded in established project practice)*

**Did this run stay inside its declared scope?**

**The boundary, which is a real distinction and not a technicality:** an incidentally-discovered **error** is
fixed *(established practice: fix adjacent bugs found incidentally, using the same propagation discipline)*. An
incidentally-discovered **gap** is *recorded and left* — because acquiring it means researching, deciding, and
depositing outside the scope anyone agreed to.

**And the propagation half:** where a fix touched a fact that appears in more than one file, **was every
implicated file checked, not just the one where the error was noticed?** *(Recorded twice: a fix naming three
wrong entities was propagated into one of them and left the others carrying the same false claim for days.)*

## Gate 7 — Cross-reference validity *(recorded: the copy-paste tag; the stale sibling counts)*

**Runs on Path 1 output only** — added 2026-08-31 during the readiness check, on noticing that **the path most
likely to run first and most often had no dedicated gate**, while Paths 2, 4 and 5 each had one.

1. **Copy-paste value migration.** Did the found fact arrive in a block of text this subject shares verbatim
   with a sibling? **Matching wording is not evidence of independent verification** — a fact can be correct for
   the entity it was copied *from* and wrong for the one it was copied *to*. *(Recorded: a "(founding wave)"
   tag sitting on the wrong nation, copied between two cities whose tier tables matched exactly.)*
2. **Stale counts and exclusivity claims.** Any "one of N," "the only X," "the first Y" found by
   cross-reference **must be re-verified against a current project-wide search, never inherited.** Sibling
   counts go stale silently as siblings are added. *(Recorded twice: one city claiming another was "Korea's
   only other center" when there were two others; a second claiming "Tepenia's two Korean cities" when there
   were three.)*
3. **Admissibility of the source, not just its content.** A fact found inside a conclusion-bearing section is
   not an attribute merely because an attribute was what you needed (`05` §6.1a–d — and note §6.1d exists
   precisely because a `Specs/` file, the tier most likely to be cross-referenced, turned out to be mixed).
4. **Did you read the hit, or trust the match?** Grep prioritizes; it never verifies.

---

# 8. The live-file schemas

## 7.1 `Gap_Registry.md` — the demand-driven work queue

**Holds only gaps admitted into the queue** (`01` §2), never an attempt at every open question in the project.

| Column | Contents |
|---|---|
| **ID** | `CGRM-nnn`, continuous, never reused |
| **Scope** | the location / person / subsystem / pass it belongs to |
| **Gap** | the question, in one sentence |
| **Source** | where it came from — a pass's REQUESTED block, a file's TBD, an Open Questions entry |
| **Triage** | `LIVE` · `SCHEDULED` · `SCAFFOLD` · `RESERVED` |
| **Path** | the acquisition path chosen, or `—` for non-LIVE |
| **Status** | `open` · `in progress` · `closed` · `unresolved` · `protected` |
| **Notes** | for SCHEDULED: the owning stage. For closed: the log entry reference |

**`protected` is a real, positive status, not a failure state** — it marks a gap this system has deliberately
declined to close, so the next session does not "helpfully" close it.

## 7.2 `Resolution_Log.md` — what was acquired, how, from where

**Append-only. Written as the work happens, never reconstructed afterward.** Per entry: the gap ID and
question · the path used and **which cheaper paths were ruled out, and why** · exact search strings verbatim
(Path 4/5) or the formula and inputs (Path 2) or the file and section (Path 1/3) or the developer's own words
(Path 6/7) · sources with links · **the KIND classification and the destination** · **open threads — what was
noticed and deliberately not chased.**

**The open-threads field is not optional.** The project's own research-log convention exists substantially
because *"a finished pass publishes conclusions and buries evidence,"* and the threads left deliberately
hanging are routinely the richest material a session produces.

## 7.3 `Developer_Ruling_Queue.md` — batched decisions

**Per entry, the five fields from `02` §7**: the question · why it is reserved · the constraints canon already
fixes · options with consequences, where natural · what is blocked and how badly.

**Once ruled: the ruling is recorded verbatim**, deposited per `03` §2, and the registry row closes. **A
paraphrased ruling is a lost ruling** — the developer's own wording repeatedly turns out to carry distinctions
a summary drops.
