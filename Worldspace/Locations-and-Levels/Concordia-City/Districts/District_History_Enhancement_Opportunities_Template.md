# District History — Enhancement Opportunities: Spec Template

**What this is:** a district-level counterpart to `Cities/City_History_Enhancement_Opportunities_Tracker.md`
— a second, flag-only pass hunting for ways to enrich each district's own pre-war history, now that every
district has a completed Deep Dive and a full pre-war Megasheet trio. **This file is the spec only.** It
has not been applied to any district yet — no `### [District]` sections, no flagged ideas, nothing written
against the actual district files. Review and adjust this template first; the actual per-district pass
starts only once this is approved.

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

---

## Per-district inputs (the district equivalents of a city's Catalog + Mega_Init + 10 chains)

| Role in the city method | District equivalent |
|---|---|
| Neo-Races Catalog | *(no equivalent — see the "Feeder-city population culture" lens below for how this gets covered instead)* |
| Mega_Init | `District_Megasheets_PreWar/[NN]_[District]/[District]_Mega_Init.md` |
| Full_Extrapolation / Cross_Reference_Synthesis | `District_Megasheets_PreWar/[NN]_[District]/[District]_Full_Extrapolation.md` and `..._Cross_Reference_Synthesis.md` |
| 10 existing chains | `Deep_Dives/[NN]_[District]_Deep_Dive.md`'s own **Stage 1** section |
| (spot-check against known open work) | That district's own entries in `Staging/` (both the numbered Deep-Dive-findings table and the "new cross-district conflict threads" table) |

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
| Resident character cultures | **Feeder-city population culture → history** | Districts have no per-nation Catalog, but `City_Refugee_District_Affinities.md` already establishes each district's top feeder cities. Use a specific feeder city's own established culture (from that city's own Megasheet) as population-specific texture, the same way the city pass used a specific nation's Cultural Iceberg finding. |
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

**Files read:** [Deep Dive], [Mega_Init], [Full_Extrapolation], [Cross_Reference_Synthesis]. [Any Staging
entries checked, named specifically.]

**Already covered (Stage 1):** [one paragraph]

1. **District civic function/economy → history.** [idea, grounded, differentiated]
2. **Feeder-city population culture → history.** [idea, grounded, differentiated]
3. **Real-world historical precedent.** [idea, grounded, differentiated]
4. **District personality/geography/architecture → history.** [idea, grounded, differentiated]
5. **Other.** [idea, grounded, differentiated]
```

---

## File structure

Only 13 districts (vs. 35 cities), so no subnet-style split is needed. One file:
`Districts/District_History_Enhancement_Opportunities.md`, holding a short purpose/method pointer back to
this template plus all 13 `### [District]` sections in zodiac order (Cancer through Virgo, then Hub last,
matching `Staging/00_Index.md`'s own ordering).

---

## Open questions before starting

1. **Order:** start with Cancer (already has both Deep Dive and pre-war Megasheet freshly re-read this
   session) and proceed in the same zodiac order Staging uses, or pick a different starting point?
2. **Hub's fifth lens set:** Hub has no zodiac sign and (per its own Deep Dive) no wound-response Stage 1
   story — confirm the five lenses still apply cleanly to it, or whether Hub needs a light adaptation note
   the way Amundsen Station got one in the city pass.
3. **Staging overlap handling:** when an idea would extend an existing 🟡 Staging item rather than being
   genuinely new, should that get logged here anyway (noting the connection) or skipped entirely as
   already-tracked? The city pass's Davis precedent (grounding new ideas in corrected canon rather than
   re-flagging a known issue) suggests: skip if it's the *same* idea, but a genuinely new angle on a
   Staging-adjacent topic is still fair game.
