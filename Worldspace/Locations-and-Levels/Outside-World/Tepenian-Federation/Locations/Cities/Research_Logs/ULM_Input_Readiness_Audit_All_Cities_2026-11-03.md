# ULM input readiness audit, all cities (2026-11-03, evening)

**What this is.** A read-only check of whether every city has what the ULM needs: its spec and inputs, its Pre-Trip, and its 19 instant-reference datasheets, and whether those sheets agree with the sources as they stand after today's rulings. **Nothing was edited.** Run at 20:03 (bookkeeping, allowed at any hour; no ULM step was run).

**Tools run:** `audit_city_inputs.py --scope all` (34 cities, 40 tests each), `verify_city_sheets.py` on all 34 keys, and four currency checks written for this audit (scratch, in the session scratchpad: workforce, quoted `16` rows, census totals, language propagation).

## 1 · Presence and structure: passes everywhere except two cities
- **32 of 34 cities: 0 gaps, 0 FAIL.** All 19 datasheets exist, the Pre-Trip verification block reads 0 missing inputs and 0 failed line claims, the ledger exists.
- **Amundsen Station: 1 gap.** No picks entry in `Inspirational-Influences.md`. Known: the 34 proposed picks wait for the Byrd–Amundsen pair check. Not in the run.
- **Davis: 12 FAIL.** Only `Phase_10.md` exists in `Datasheets/`; the Pre-Trip is the old format (placeholders, no sections A–N); no ledger. Davis is a finished old-format pass outside the run; it would need a full rebuild before any re-run.
- **Not covered by the tools:** Concordia (district method), Shirayuki, Sinheung, Zhongshan (finished passes).
- Notes only (read, never strip): later-era words in Step_7 L13 across most cities; inference markers; 30 cities have empty concept-art folders (optional); 6 cities not named in the history files (known canon gap).

## 2 · Currency: what is current
- **Census totals** (Census I and II): every city's Step_0 sheet carries the current total (Esperanza 1,200,000; Casey 1,547,850; Amundsen Station and the rest). Relung Panen's census row lives in its own sections (not checked by this script).
- **Workforce** from `16`: current in Step_1_and_2, Phase_4 and Phase_7 of every city except Denison's Phase_7 (below) and Davis's Phase_7.
- **Casey** (the first run): fully current. Counts 464,639 / 210,834 / 491,945 on workforce 1,167,418 sit in Phase_7; population in Step_-1, Step_0, Phase_2, Phase_4, Phase_9.

## 3 · Currency: what is stale (found, not fixed)
**A. Quoted `16` summary row, old percentages. 22 lines in 8 cities.** Each quotes "Workforce · base% · MAND% · FREE%" from `16`'s summary table with the workforce right and the percentages from before the robot-term recount. The cited line now reads differently. In most of these cities the city's own determination row beside it is already current and governs, so the damage is a wrong quote, not a wrong governing figure.

| City | Sheets (line) | Quoted | `16` now |
|---|---|---|---|
| Amundsen Station | Phase_4 L14, Phase_7 L16, Step_1_and_2 L44 | 31.8 / 61.4 / 6.8 | L249: 33.2 / 60.1 / 6.7 |
| Belgrano | Phase_4 L14, Phase_7 L16, Step_1_and_2 L38 | 44.3 / 30.6 / 25.1 | L252: 45.4 / 30.0 / 24.6 |
| Lazar | Phase_4 L14, Phase_7 L16, Step_1_and_2 L34 | 41.0 / 0.0 / 59.0 | L284: 42.1 / 0.0 / 57.9 |
| Fort McMurdo | Phase_4 L14, Phase_7 L16, Step_1_and_2 L44 | 41.5 / 35.1 / 23.4 | L250: 42.6 / 34.4 / 23.0 |
| Pergamino | Phase_7 L16, Step_1_and_2 L32 | 39.3 / 18.2 / 42.5 | L266: 40.4 / 17.9 / 41.7 |
| Marambio | Phase_4 L14, Phase_7 L16, Step_1_and_2 L39 | 41.3 / 35.2 / 23.5 | L251: 42.4 / 34.5 / 23.1 |
| Palmer City | Phase_4 L14, Phase_7 L16, Step_1_and_2 L39 | 39.1 / 0.0 / 60.9 | L285: 40.2 / 0.0 / 59.8 |
| Contrapunto | Phase_7 L16, Step_1_and_2 L41 | 39.4 / 15.2 / 45.5 | L272: 40.5 / 14.9 / 44.6 |

**B. Denison: old workforce and base share.** Phase_7 L11 (and the matching lines in Step_1_and_2 L29–L30 and Phase_4 L11) say workforce 701,805 and base 53.2%. `16` now says 722,541 and 54.3% (L259). Phase_7 also lacks the new workforce figure entirely.

**C. Dumont d'Urville: two workforce figures.** `16` L279 says 341,560 is pre-trim and the live workforce is 307,404. The sheets carry both (Phase_4 L18 and L20 present 341,560 as matching; the live figure is also present). This looks deliberate, and I did not change it, but the Phase_4 line that says "no discrepancy" should be read against the live figure before Dumont's run.

**D. Puerto Abrigo:** the `16` summary table lists it under its old name, Port Lockroy (workforce 701), and the sheets carry 701. Correct, but it is the only city I could not match by current name.

## 4 · Gap: today's language rule is in no sheet and no Pre-Trip
The Hawaiian-dominant rule, the supporting-tier definition and each city's set (within 12 points of the largest group) were set today and exist only in `Language_Blocs_By_City_2026-11-03.md`, `Language_Sets_By_City_Reference_2026-11-03.md` and `Amundsen_Station_Composite_Language_Blocs_2026-11-03.md`. **No datasheet or Pre-Trip in any of the 34 cities mentions them** (the only pass-folder mention is Mirny's held Phase 8 piece). The handoff says language is a fact of the place and is set early, and the datasheet rule is that sheets carry the data and not a pointer. Casey's run therefore starts without its language line (English alone).

## 5 · What I recommend, in order
1. **Casey first (it starts at 05:00):** add its language row (Hawaiian dominant; supporting tier English alone, English about 36% against Mandarin about 13%, roughly 22 points behind) to the Casey sheets. Casey has no stale quotes from section 3.
2. Fix the 22 stale quoted rows (section 3A) and Denison's lines (3B) from the current `16` table, then rerun `verify_city_sheets.py` for each.
3. Add each city's language row to its Step_0 sheet from the Language Sets reference (34 sheets).
4. Leave Davis and Amundsen Station alone until they enter the run.

All of items 1–3 edit existing sheets, so they wait for the developer's go-ahead.

---

## 6 · Fixes applied (2026-11-03, evening, at the developer's word "make all of the fixes")
Datasheets only; no pass file, spec, census, `16` or culture file was changed. **Not committed.** The checking scripts and the full change list are in the session scratchpad.

1. **Quoted `16` summary rows (3A): 25 lines in 9 cities corrected** to the current table (the 22 found plus Puerto Abrigo's 3 lines, which the first scan missed because its workforce has no thousands separator): Amundsen Station, Belgrano, Lazar, Fort McMurdo, Pergamino, Marambio, Palmer City, Contrapunto, Puerto Abrigo. Rerun: 0 stale quotes.
2. **Denison (3B):** Step_1_and_2 (Half B row and own-determination row) and Phase_7 now read workforce 722,541, Half B 54.3 / 11.4 / 34.3, and `16` §25 at 54.4 / 16.0 / 29.6 (the counts 393,030 / 115,329 / 214,182 sum to 722,541). **Found on the way:** `Specs/Denison.md` L172 still says 53.2 / 16.4 / 30.4 ("UNAFFECTED"). The sheet first flagged this; then, at the developer's word, `Specs/Denison.md` L172 was updated to 54.4 / 16.0 / 29.6 (same two lines, no line shift) and the sheet's flag was replaced by a plain citation.
3. **More stale data found by a second check** (each city's own determination section against its Phase 7 sheet), all fixed: Amundsen Station FREE 429 (6.8%) became 420 (6.7%); Puerto Abrigo's own-determination counts 287 / 21 / 393 became 295 / 20 / 386 (shares 42.1 / 2.8 / 55.1, distinctive tier 406) in Phase_4, Phase_7 and Step_1_and_2.
4. **Fort McMurdo:** its sheets carried only a line pointer to its own determination (§29). A data row (142,090 / 115,275 / 76,850 = 334,215; shares 42.5 / 34.5 / 23.0) was added to Phase_4, Phase_7 and Step_1_and_2.
5. **Dumont d'Urville (3C): no change needed.** Its Phase_4 line already records the pre-trim figure (341,560), the live figure (307,404) and flags the conflict as unresolved, which matches `16` L279.
6. **Language row added to Step_0 of 33 cities** (all but Davis, which has no Step_0 sheet). Each row states: Hawaiian dominant; supporting tier = every group within 12 points of the largest; the city's set; the share ranges; and the caveat that shares are national-origin shares, not speaker counts, and the nation-to-language mapping is recalled, unverified. Sets written: English alone in 24 cities and German alone in Sanay (the 12-point rule gave no second group); English and German (Neumayer); English and Spanish (Esperanza, Marambio, Pergamino, Contrapunto); English, German and Indonesian (Temirötkel); English, Mandarin, Indonesian and Japanese (Mawson, option A); English, Mandarin, Russian, French and Japanese (Kunlun, plus a 6.9% unmapped residue that is not a language); English, Mandarin, Indonesian, Japanese, Korean, Russian and Thai (Relung Panen). Casey: English alone.

**Verification after the fixes:** `verify_city_sheets.py` on all 33 cities: 0 FAIL, and the NOTE total unchanged (45). `audit_city_inputs.py --scope all`: only the two known gaps (Amundsen Station picks; Davis). Quoted-row check: 0 stale. Own-determination check: current in every city that has a section.

**Still not done (outside these fixes):** Casey's held Step −1 input contract (a pass file in the held review) still says the second-language slot is open; update it in the 05:00 review. The culture-file language lines for Mirny, Temirötkel, Mawson and Santa Luce are also still "second slot open". Davis and Amundsen Station stay as they are until they enter the run.
