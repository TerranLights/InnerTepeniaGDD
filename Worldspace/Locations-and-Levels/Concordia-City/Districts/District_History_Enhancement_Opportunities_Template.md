# District History — Enhancement Opportunities: Spec Template

**Status: OFFICIAL, 2026-07-17.** Validated across two full test runs (Cancer, Scorpio), each run twice —
once against the core Megasheet/Deep Dive/Staging inputs, once more with `District_Vision_Notes/` added —
before being finalized. See "Validation status" below for what each round actually tested and changed.
This is now the standing method for the real 13-district pass.

**What this is:** a district-level counterpart to `Cities/City_History_Enhancement_Opportunities_Tracker.md`
— a second, flag-only pass hunting for ways to enrich each district's own pre-war history, now that every
district has a completed Deep Dive and a full pre-war Megasheet trio.

---

## Why a district version needs its own template, not a copy of the city one

The city method (`Cities/City_History_Enhancement_Opportunities_Tracker.md`) leans on two inputs no
district has: a per-nation Neo-Races Catalog, and a `Course_of_Events_Suggestions.md` holding 10 numbered
But/Therefore chains to diff new ideas against. Concordia's own `Neo-Races-and-Cultures/Concordia/` folder
is empty (just a `.gitkeep`), and no district has a Course_of_Events file. Districts are built from a
genuinely different set of documents, so the method has to be rebuilt around what actually exists for
them — not just relabeled.

---

## Scope constraint (unchanged in spirit from the city pass)

Every flagged idea must stay inside **Stage 1 only** — the ~250-year Second Interwar organic-formation
period (2564–2812) that `00b_Two_Stage_Methodology.md` already separates from Stage 2. No war fallout, no
present-day (≈2822–2827) material. This is the direct district equivalent of the city pass's
"pre-Long-Night-War only" rule, and it maps cleanly: Stage 1 *is* each district's own pre-war period,
the same way each city's Second Interwar Period history is its own pre-war period.

Anything that would require war-era framing is out of scope for this pass — that material already has a
home in each Deep Dive's own Stage 2 section, and in `Staging/`'s war-fallout findings.

### Standing rule: explicit Stage 2 exclusion, applied to every source, not just the Deep Dive

Validated by the Cancer and Scorpio test runs (`_Method/District_History_Enhancement_Test_Run_Cancer.md`,
`_Method/District_History_Enhancement_Test_Run_Scorpio.md`) as a real, recurring risk rather than a
theoretical one — several of the general-notes files this pass draws from freely mix Stage 1 and Stage 2
material, often in the same paragraph, without labeling which is which. Before citing *any* source detail
in this pass, positively confirm it belongs to Stage 1 — don't assume a detail is pre-war just because it
appears in a document that also contains pre-war material. This applies specifically to:

- **`Historical_Pressures.md` and `Historical_Inter-District_Effects.md`** — both files interleave
  founding-era and Long-Night-War-era entries under the same district heading, sometimes in the same
  bullet ("Post-Falkland... / Long Night War... / ongoing since..." all listed together). Check each
  individual entry's own dating before using it, not just the file or section it lives in.
- **`Staging/` entries** — per both test runs, a district's own Staging findings are more likely to
  resolve as "Stage 2, not applicable to this pass" than as a genuine duplication risk. Still check (a
  Staging item could in principle be Stage 1), but expect most districts' Staging entries to simply fall
  outside this pass's scope rather than to require careful differentiation.
- **`City_Refugee_District_Affinities.md`'s feeder-city rankings** — a district's top-ranked feeder
  cities are sometimes a **Stage 2 Override** (the file's own term), representing war-driven trauma pull
  rather than genuine pre-war cultural affinity. Scorpio is the confirmed example: its four best-known
  feeder cities (Belgrano, Palmer City, Zukelli, Casey) are explicitly flagged in the source file as not a
  real Stage 1 affinity. **Before using a district's top-ranked feeder cities for Lens 2, check the file's
  own "Stage 2 Overrides" section for that district's name.** If the top-ranked cities are override
  entries, drop down to the next-highest-ranked city that isn't, and use that one instead.

---

## Per-district inputs (the district equivalents of a city's Catalog + Mega_Init + 10 chains)

| Role in the city method | District equivalent |
|---|---|
| Neo-Races Catalog | *(no equivalent — see the "Feeder-city population culture" lens below for how this gets covered instead)* |
| Mega_Init | `District_Megasheets_PreWar/[NN]_[District]/[District]_Mega_Init.md` |
| Full_Extrapolation / Cross_Reference_Synthesis | `District_Megasheets_PreWar/[NN]_[District]/[District]_Full_Extrapolation.md` and `..._Cross_Reference_Synthesis.md` |
| 10 existing chains | `Deep_Dives/[NN]_[District]_Deep_Dive.md`'s own **Stage 1** section |
| (spot-check against known open work) | That district's own entries in `Staging/` (both the numbered Deep-Dive-findings table and the "new cross-district conflict threads" table) |
| (no city equivalent — a bonus source) | `District_Vision_Notes/[District].md` — the developer's own running record of direct-conversation creative vision, explicitly distinct from both `District_Canon_Reference.md` and the Deep Dive. Added 2026-07-17, after a survey turned up that it sometimes restates or lightly expands a detail the other three documents only name in passing (e.g. Cancer's own care-debt economy), without ever fully resolving it — worth checking before flagging an idea as "named but never elaborated," since Vision Notes is the one place a slightly fuller (but still unresolved) version might already exist. |

Read all of these before flagging anything. The Staging check exists purely to avoid re-flagging
something already sitting there at 🟡 — if an idea's already been raised in Staging, skip it or note the
overlap rather than re-proposing it.

---

## Step 1: "Already covered" summary

One paragraph per district, written before any new ideas are flagged, summarizing what Stage 1 (the Deep
Dive) plus the Full_Extrapolation's proposed answers plus the Cross_Reference_Synthesis's findings
*already* establish about that district's organic pre-war formation. This plays the same role the "existing
10 chains already cover" summary played in the city pass — it's the baseline every new idea has to be
checked against and differentiated from.

---

## Step 2: Five lenses, adapted from the city version

| City lens | District lens | Why it changes |
|---|---|---|
| Division of industry → history | **District civic function/economy → history** | Districts aren't nation-founded economies; each has its own established civic role (Cancer=caregiving, Aries=power, Capricorn=industry) and inter-district economic frictions (e.g. Cancer/Aries power allocation) that are frequently stated but rarely dramatized into a specific episode. |
| Resident character cultures | **Feeder-city population culture → history** | Districts have no per-nation Catalog, but `City_Refugee_District_Affinities.md` already establishes each district's top feeder cities. Use a specific feeder city's own established culture (from that city's own Megasheet) as population-specific texture, the same way the city pass used a specific nation's Cultural Iceberg finding. **Check for a Stage 2 Override first** (see the standing rule above) — skip past override entries to a genuine Stage 1 match. |
| Real-world historical precedent | **Real-world historical precedent** (unchanged in kind) | `District-Inspirational-Influences.md` plays the same role city Megasheets' Real-World Inspirations sections did — look specifically at Secondary/Supporting-tier picks, which tend to go uncited once a Primary pick anchors the district. |
| City personality/geography/geology → history | **District personality/geography/architecture → history** | Use the Mega_Init's Enneagram read plus its "What It Feels Like" section, cross-checked against `Regional-Characteristics/District_Prominent_Features.md`. Districts don't have geology of their own (they're all built on the same city), so this lens leans on built environment and civic temperament instead. |
| Other | **Other** (unchanged) | `Historical_Pressures.md`, `Historical_Inter-District_Effects.md`, or a Mega_Init "What's Actually Open" item the Full_Extrapolation didn't end up resolving. |

For each district, flag exactly 5 new ideas, one per lens, each:
- citing the specific source line it's grounded in (file + detail, not a paraphrase of the whole document)
- explicitly stating how it differs from what Step 1 already covers
- explicitly stating how it differs from that district's own Staging entries, where relevant
- explicitly stating how it differs from other already-completed districts' flagged ideas, once more than
  one district has been done (same cross-district differentiation discipline as the city pass)

**Flag only** — no new Stage 1 narrative drafted, no texture woven into the actual Deep Dive or Megasheet
files. This is a punch list for a future pass, exactly like the city version.

---

## Output format (per district)

```
### [District]

**Files read:** [Deep Dive], [Mega_Init], [Full_Extrapolation], [Cross_Reference_Synthesis], [Vision Notes].
[Any Staging entries checked, named specifically.]

**Already covered (Stage 1):** [one paragraph]

1. **District civic function/economy → history.** [idea, grounded, differentiated]
2. **Feeder-city population culture → history.** [idea, grounded, differentiated]
3. **Real-world historical precedent.** [idea, grounded, differentiated]
4. **District personality/geography/architecture → history.** [idea, grounded, differentiated]
5. **Other.** [idea, grounded, differentiated]
```

---

## File structure

**Split per district, 2026-07-17** — a single combined file was tried first (holding both Cancer and
Scorpio), but at ~60 lines per district × 13 districts, it was heading toward the same length problem that
triggered the city pass's own subnet split. Structure:
- `Districts/District_History_Enhancement_Opportunities.md` — thin index only: purpose/method pointer,
  links to each district file, and the progress checklist.
- `Districts/District_History_Enhancement_Opportunities/[NN]_[District].md` — one file per district,
  numbered to match `Deep_Dives/` and `District_Megasheets_PreWar/`'s own `[NN]_[District]` convention.

---

## Validation status

**Round 1 (core inputs only), 2026-07-17** — Cancer (a district with zero Staging entries) and Scorpio (a
district with one) both run against Deep Dive + pre-war Megasheet trio + Staging check. Both produced five
usable, well-grounded, well-differentiated ideas with no lens coming up empty. Scorpio's run additionally
surfaced the Stage 2 Override feeder-city risk and confirmed Staging overlaps tend to resolve as
wrong-stage rather than genuine duplication — both folded into the standing rule and Lens 2's row above.

**Round 2 (Vision Notes added), 2026-07-17** — both districts re-run with `District_Vision_Notes/[District].md`
added to the input table. Vision Notes contributed nothing to Lenses 1–3 in either case, but produced
strictly better-grounded material (explicitly developer-flagged as open, rather than inferred) for Cancer's
Lens 4 and for Scorpio's Lenses 4 and 5. Scorpio's own Vision Notes file also turned out to be the sharpest
real-world confirmation yet of the standing Stage 2 exclusion rule — its "recap" paragraph silently mixes
Stage 1 and Stage 2 institutions in the same breath, exactly the risk that rule was written to catch.

Full detail for both rounds, both districts: `_Method/District_History_Enhancement_Test_Run_Cancer.md`,
`_Method/District_History_Enhancement_Test_Run_Scorpio.md`. The composite (best-of-both-rounds) results
for both districts are now promoted into `District_History_Enhancement_Opportunities.md` — the real
tracker file — per the `Phase1c_Test_Run_Sanay.md` precedent of promoting a validated test run rather than
redrafting it from scratch. **No further structural changes pending. Template is final.**

## Pass complete — 13/13 districts, 2026-07-17

All three open questions from the pre-pass draft are now resolved by the finished pass itself:

1. **Order — resolved as planned.** Cancer and Scorpio (promoted from the test runs), then Taurus, Leo,
   Aries, Capricorn, Aquarius, Libra, Gemini, Pisces, Sagittarius, Virgo, Hub, in `Staging/00_Index.md`'s
   own zodiac order throughout.
2. **Hub's fifth lens set — resolved, no adaptation needed.** Hub has no zodiac sign and no wound-response
   Stage 1 story, but its Deep Dive and full pre-war Megasheet trio are exactly as dense as the other
   non-wound-response districts (Taurus, Capricorn, Sagittarius, Virgo). The standard five lenses applied
   cleanly with no Amundsen-Station-style scaled-down treatment required.
3. **Staging overlap handling — resolved, but only the simpler branch was ever exercised.** Across all 13
   districts, every Stage-1-relevant Staging entry (Leo's Cymatics finding, Sagittarius' Long Haul thread)
   turned out to already be substantially reconciled by its own district's Deep Dive or Full_Extrapolation,
   so the correct move was always full exclusion — "skip, already covered." The more nuanced branch this
   guidance also describes (log a genuinely new angle on a Staging-adjacent topic that *isn't* the same
   idea) never actually came up in practice. Worth keeping the guidance as written for any future district
   work, since it held up correctly every time it was tested — it just never needed its own harder case.

**Final tally:** 65 flagged ideas (5 × 13 districts), plus a per-district "notes for further elaboration"
sweep in `District_History_Enhancement_Opportunities.md` identifying 5 genuine developer-decision-pending
items (Leo's Star War, Capricorn's seven c. 2761 options, Gemini's Great Corruption, Pisces' Tolerance Pact
and Flood, Virgo's Deep Level), 2 smaller open factual gaps (Aries, Libra), and 1 district worth a fresh
Vision Notes session on thinness grounds alone (Sagittarius). Template validated, applied, and closed out.
