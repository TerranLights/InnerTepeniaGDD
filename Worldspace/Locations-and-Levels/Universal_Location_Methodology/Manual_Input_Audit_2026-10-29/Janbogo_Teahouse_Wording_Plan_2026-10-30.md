# Janbogo — teahouse wording: survey and edit plan (2026-10-30)

Governing instruction (author, binding, all repos): `/home/kuroskalacs/Documents/Doll-Fi/media/y-files/session-instructions/Janbogo - not a city of teahouses.md`. Summary: tea, hospitality and togetherness are part of Janbogo's culture; Janbogo is not "the Teahouse City" or "a city of teahouses"; the teahouse Majyao ran is one famous establishment and a founding-era landmark, and **has no name yet**; no new identity is invented; removals are clean (no "[removed]", "formerly" or changelog notes).

**Status at 17:28 on 2026-10-30:** survey done; one wording fix applied (below); everything else is held for the 05:00–14:59 window because it edits claims about a place's culture (operating-hours law), or for the developer's call.

## A · Files the Janbogo ULM run reads, with teahouse-term hits

| File | Hits | Disposition |
|---|---:|---|
| Pass `00.0_Pre-Trip_Inspection.md` | 2 | **DONE 2026-10-30**: "Majyao's teahouse" (a search aid, written like a name) → "the teahouse Majyao ran (it has no name yet)". The second hit is the bare word `Majyao` as a search aid: fine |
| Pass `Datasheets/Phase_7.md` L21 | 1 | Quotes the developer's own concern "Janbogo cannot be an entire city of teahouses" (from the sweep file). **Question 2** |
| Pass `Datasheets/Phase_8.md` L12 | 1 | A count statement ("1 hit, L149, 'places to drink tea', in the teahouse paragraph at L147–L149; the teahouse is also named at `## Notable Locations` L167"). **Re-count after the spec edit** |
| Pass `Datasheets/Phase_10.md` L12–15 | 4 | Quotes from Majyao Bisyugota's character files (she ran a famous coffee and teahouse): consistent with "one famous establishment". **Leave** |
| Pass `Datasheets/Step_3.md` L11 | 1 | Copies the inspiration pick "Central Asian chaykhana (teahouse) tradition [PRIMARY]" from `Inspirational-Influences.md`. **Question 3** |
| Spec `Specs/Janbogo subnet/Janbogo.md` | 10 lines | **HELD (in-window).** Drafted replacements in section B |
| `Division_of_Industry/16_Per_City_Three_Tier_Run.md` §28 (L2882, L2885, L2890) | 3 | **HELD.** Quotes the culture file's §15 ("the centrality of teahouses and hosting institutions…") and argues "the teahouse tradition is nationally famous"; must be rewritten after the culture file's §15 is fixed, in that order |
| `Division_of_Industry_Sweep_2026-08-31.md` L72–76 | 2 | **HELD.** Same §15 quotation and the "teahouses as what drives it … exactly right" judgment; the developer-concern quote is **Question 2** |
| `Universal_Location_Methodology/Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` L1426, L1703 | 2 | L1426 is the developer-concern quote (**Question 2**); L1703 quotes the old spec text "the teahouse tradition as 'the district's most nationally visible expression'" (**HELD**, drop the clause) |
| `Concordia-City/Districts/Phase_Instructions/00b_General_Population_Discipline.md` L97 | 1 | Developer-concern quote (**Question 2**); not read by the Janbogo run |
| `Research_Logs/Janbogo_Research_Log.md` L68 | 1 | Output of the earlier cold test run (Run 9); zero-intake record. **Leave** |
| `Worldspace/Characters/Enneagram_Character_Index.md` | 1 | Hit is the name "Majyao Bisyugota". **Leave** |
| `Local_Cultures/Janbogo_Subnet/Janbogo.md` (read last, Step 5, as a check) | 30 | **HELD (in-window).** The author's "main one". Read and draft at 05:00 |
| `Local_Robot_Culture/Janbogo_Subnet/Janbogo.md` (read last) | 13 | **HELD (in-window).** Read and draft at 05:00 |

Counts only for the next three; their lines were not printed:

| File | Hits | Disposition |
|---|---:|---|
| Megasheet `Janbogo_Physical_Infrastructure_Attributes.md` (+ `Janbogo_Mega_Init.md`, `Janbogo_Full_Extrapolation.md`, `Janbogo_Cross_Reference_Synthesis.md`, megasheet `README.md`) | 4 (+ others) | **Not edited.** Standing rule: megasheets are never edited; the compilation method is fixed instead, and they are rebuilt after all three methods. Withheld corpus-wide |
| `City_Vision_Notes/Janbogo.md` | 5 | Not an input at any step. **Question 4** |
| `Neo-Races-and-Cultures/Janbogo_Subnet/Janbogo/Janbogo_Catalog.md` | 26 | Downstream neo-race project, not an input. **Question 4** |

## B · Drafted spec edits (all within existing lines, so the spec stays 220 lines)

| Line | Replace | With |
|---|---|---|
| L123 | "Janbogo's renowned interior culture (teahouses, shared warmth)" | "Janbogo's interior culture of tea, hospitality and togetherness" |
| L149 | the whole paragraph ("The teahouse culture was its most nationally visible expression. … would never go.") | "Tea, hospitality and togetherness are part of its culture. At least one Janbogo teahouse was famous throughout Tepenia — known to people who had never been to Janbogo and would never go." |
| L151 | "the teahouse tradition, communal warmth" | "tea, hospitality, togetherness" |
| L153 | "Its teahouse culture and the quality of warmth and communal hospitality its people carried with them;" | "The quality of warmth and communal hospitality its people carried with them;" |
| L167 | "**Majyao's Teahouse** — the establishment famous throughout Tepenia;" | "**Majyao's teahouse** *(no name yet)* — one of the city's founding-era landmarks, famous throughout Tepenia;" |
| L175 | "her teahouse was a defining landmark of Janbogo's cultural identity and the most nationally recognized symbol of the city's character" | "her teahouse was one of the city's founding-era landmarks" |
| L178 | "translating the teahouse-scale interior-warmth principle into large-scale civic architecture" | "translating the interior-warmth principle into large-scale civic architecture" |
| L191 | — | none ("runs a teahouse"; a fact about her) |
| L205 | "The teahouse tradition survives through Majyao's establishment in Aquarius." | "Majyao's teahouse continues in Aquarius." |
| L214 | "What does Majyao's original teahouse in Janbogo look like now" | "What does the teahouse Majyao ran in Janbogo look like now" |

## C · Open questions for the developer

1. **Hours.** The remaining edits touch claims about a city's culture, which the operating-hours law restricts to 05:00–14:59. Default: apply them from 05:00 on 2026-10-31, in this order: the culture file's §15 and the other culture-file lines → the spec → `16` §28 → the sweep → `OBSERVATIONS` and `00b` → the pass sheets' counts; then re-run the author's grep and the sheet verifier. Or the developer waives the clock for this one cleanup.
2. **The developer's own concern, quoted.** `Phase_7` L21, the sweep L72, `OBSERVATIONS` L1426 and `00b` L97 quote "Janbogo [cannot be] an entire city of teahouses". Proposed: remove that example from each list and leave the other example (Zhongshan, the lake; Cape Adare, the hut), so the phrase no longer appears.
3. **Inspiration picks.** `Inspirational-Influences.md` lists the Central Asian chaykhana (teahouse) tradition as Janbogo's PRIMARY pick. Not touched: that file changes only on the developer's go-ahead.
4. **Outside the Janbogo run.** Vision notes, the neo-race catalog, Zukelli's culture files, the Casey catalog, Concordia's refugee-diaspora composition file, the DLC questline candidates, eight Background-Lore vignettes and two frozen Run 9 archive files also carry the framing. Not part of the Janbogo run's reads. Background-Lore is never edited; the archive is a frozen record.
