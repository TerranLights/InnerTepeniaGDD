# Differentiation Instrument — Quick Reference

> ⭐ **Tier U — corpus-wide, identical for every city.** Feeds every city's Step 6. Extracted in full from
> `04_QA_Gates_and_Differentiation.md` Part III (L417–517) and `00_RUNBOOK.md` §"Step 6" (L2843–2892), both
> re-read in full 2026-09-15. **Nothing below is Casey-specific, Davis-specific, or Mirny-specific — it is the
> same for all 37 cities and does not need re-extraction per city.**

## Governing rule — Part III is WRITE-ONLY during a per-location pass, ruled 2026-09-06

> *"In terms of your interpretation of Part III's 'anti-convergence' rule, yes, this is something we'll check
> for and decide at the very end. During the course of the ULM/CST/RWBEM, just follow the data wherever it
> leads for one single location on its own terms, and we'll worry about differentiation later."* — Developer,
> 2026-09-06

| | During a per-location pass | At the TERMINAL check |
|---|---|---|
| Adding this location's column | ✅ REQUIRED, same commit as the finding (Step 9, unchanged) | — |
| Reading another location's row | ⛔⛔ FORBIDDEN | ✅ this is the whole job |
| "Before writing a category, read its row" (III.2 step 1) | ⛔ REVOKED in-run | ✅ restored |
| III.4 substitutes | ✅ the ordinary path, for EVERY location | — |

**Why the table still gets filled:** *"A write-only table is not a dead table; it is a table under
construction... the table is FILLED DURING synthesis… it contributes nothing to the first city and everything
to the thirty-seventh."* A pass that reads a neighbor's row writes AROUND that neighbor — writing-around-a-
neighbor is still a neighbor-shaped decision, convergence arriving by the door marked anti-convergence.

**Scope:** `ULM/CST/RWBEM` only. The district instrument (`Cross_District_Differentiation_Table.md`) is
untouched and keeps read-before-write on its already-complete 13-district corpus.

## III.0 — "Noticed somewhere" is not "available where it is needed"

A differentiation instrument only works if the findings that distinguish its members have actually **reached**
it. Measured case: two cities in one cluster were assigned the same planetary symbol; the collision was noticed
and recorded correctly in one city's own culture file months earlier, but the cluster's purpose-built
differentiation guide contained zero mentions of symbols, planets, or elements — the one file whose entire job
was keeping them apart did not know.

Checklist when an instrument exists: (1) has anything been established about these locations since the
instrument was last updated — symbol assignments, census revisions, founding corrections, renames are the usual
stragglers; (2) a finding recorded in a file nobody consults during differentiation is not doing differentiation
work; (3) **propagation is part of the finding, not a follow-up** — the column goes in the same commit as the
finding, and so does anything discovered about a sibling along the way.

## III.1 — What the instrument is

One file per sibling set, listing each completed location's answer per category, so a new location can be
checked against a single file read instead of re-reading every sibling's full document. Exists because the
check gets more expensive with every location completed and would otherwise quietly stop being run — and
because it already failed once, when two districts were given nearly the same food custom a day apart.

## III.2 — How to run it (steps 1–2 terminal-only; in-run, jump to III.4)

1. ⏸️ *(terminal only)* Before writing a category, read its row.
2. ⏸️ *(terminal only)* If your answer rhymes with any entry, differentiate it explicitly and inline or change
   it — write the comparison as a table on at least four axes, including the **tense** axis (where and when the
   loss happens), the one most often skipped and the one that most often separates two locations that otherwise
   look identical.
3. **Name the axis the category answers on**, in bold, and confirm no completed sibling already uses it —
   *"different content is not differentiation; a different question is."*
4. After completing a location, add its column in the same commit.

## III.3 — Sibling sets of different sizes

| Set size | How to run it |
|---|---|
| Large (20+) | Full table; check the most recently written first — collisions cluster there |
| Medium (5–20) | Full table; expect most pairs to eventually be compared directly |
| Two | Write them together — two locations at opposite extremes of one faculty are each other's exact remedy, and the remedy is unacceptable, since taking it concedes the other's authority over that faculty |
| One (no siblings) | III.4 |

## III.4 — The no-sibling case, four substitutes in order of strength

1. **Its own earlier states** — a location with history is its own sibling set across time: differentiate the
   present frame against the founding frame and the crisis frame. Usually available, and the strongest.
2. **The nearest analogous location at another scale** — a unique station against the cities; a unique polity
   against its own sub-units.
3. **Real-world comparables**, with divergence stated explicitly per the source-not-specification rule.
4. **The generator-conflict method** (`02` §5) — needs no sibling set at all.

> A location with no siblings is at elevated risk of reading like the author's defaults, because nothing is
> pushing back. Say so in the pass, and run substitute 1 without fail.

## Destination addresses

- The 37 cities → `…/Cities/Cross_City_Culture_Differentiation_Table.md` (created 2026-09-04)
- The 13 districts → `…/Concordia-City/Districts/Cross_District_Differentiation_Table.md`
- ⚠ NOT this instrument: `…/Cities/Division_of_Industry/02_Cross_City_Industry_Differentiation_Table.md` — a
  different guard for a different pass (the necessary-industries bulk run); both exist, neither replaces the
  other

**⛔ Cells hold the AXIS, never the content.** No Step 9 dependency exists for when the axis becomes namable —
it's namable once Step 4's phases are written, per `00_RUNBOOK.md` §"Step 6" L2876–2877.
