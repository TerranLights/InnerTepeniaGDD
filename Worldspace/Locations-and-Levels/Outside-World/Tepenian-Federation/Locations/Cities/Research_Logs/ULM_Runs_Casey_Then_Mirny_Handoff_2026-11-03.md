# Handoff for a fresh session: Casey's ULM run, then Mirny's remaining blocks (written 2026-11-03)

**Order the developer set (2026-11-03):** the 04–17 prose pass (done), the Amundsen Station town steps (composition and spec edits done; picks stay a draft pending the Byrd pair check), then **Casey**, then **Mirny**. Per the developer's choice, Casey and Mirny start in a **fresh session**, not in the long session that prepared them.

## Conditions (all binding)
- **Operating hours:** ULM only 05:00–14:59 (wrap-up from 13:59). Clock check first. Today's window ends 14:59; the next full window opens **2026-11-04 05:00**.
- **Fresh session, warm run, three Opus readers on every step and phase** (`DR` T8 ruling). No graphify during a cold run or inside any isolated reader; ignore the hook per the repo CLAUDE.md exception.
- **Web quota:** 1,000 calls per session shared by all subagents; ULM passes do their own research. Never work around a refusal.
- **Do not read** other cities' culture files or the differentiation table's other columns (write-only in-run).

## Casey (Mirny subnet): ULM Step −1, the input contract
**Read first, in this order (MASTER_Process_Tracker.md, "NOVEMBER 2026 RUN — CITY: CASEY", L363–L369):** (1) SESSION BOOT (L137) · (2) `Dev-Road-Map/November_To-Do.md` sections 3 and 4 · (3) Casey's `README.md`, Datasheets row first · (4) Casey's `00.0_Pre-Trip_Inspection.md` and `00.2_Position_Coverage_Ledger.md` · (5) Casey's `Datasheets/` (drafts; never a substitute for a primary read). Then build the reader list with `Tools/make_t8_required_list.py` and the standing brief lines from `T8_Standing_Brief_Lines.md`.

**State on 2026-11-03 (verified):**
- `audit_city_inputs.py --scope all`: 0 gaps for Casey (only Amundsen Station and Davis show gaps, both outside the run).
- `verify_city_sheets.py Casey --quiet`: 20 checks, 0 FAIL, 2 NOTE. The notes are to be **read, not stripped**: later-era words at Step_7 L13, Step_10 L10, Phase_3 L16, Phase_5 (now about L57); inference markers at Phase_3 L16 and Phase_5 L31.
- **Phase 5 hit rows read against the Connections file (done 2026-11-03):** every cited line matches. The old "Australian-heritage network" flag is gone from the source; Mirny and Davis are carried as clean rows (Founding Register, `DR-19`); the Phase_5 flag block is marked RESOLVED.
- **Numbers current:** `16` section 21, the `09` row and Casey's datasheets carry the recount with the robot term B3+B4 (`DR-97`): Casey baseline 464,639 (39.8%), mandated 210,834 (18.1%), free 491,945 (42.1%); population 1,547,850; workforce 1,167,418.
- **Language rule for any language line:** Hawaiian (later Tepenian) first; the second slot is whoever holds a majority; no majority → slot open (Casey's largest shares: see its spec). Language is a fact of the place, never deferred.
- **Stage order:** food, music and everyday life belong to the CST; holidays and religion come after the CST.
- **Casey's culture file:** one number-swap edit on 2026-11-03 (L286, Japan 6.18%, Korea Primary 11.95%); its composition now has five Primary nations.
- Relung Panen's spur ends at Casey: `Highways.md`, `Ports.md` L298/L300 and `Airports.md` L21–L23 changed today for Relung's gulf airport, but Casey's own rows are unchanged (Casey keeps no airport, `DR-82`).

## Mirny: the remaining blocks (not a new run; the pass is "run through Step 10; awaiting the developer's review; not declared complete")
Per MASTER_Process_Tracker (L369, L375) and the 2026-10-21 note: **after Casey**, (1) the **wind re-derivation** (first Mirny block), (2) the **cap-starved research** (second block), (3) the **"lived middle"**, then the developer declares it complete. Planet symbol and the Borrowed Form trigger (Q-74) stay held; symbols are determined after the locations are synthesized (developer, 2026-11-03).

**What changed in Mirny's inputs today (read before the blocks):**
- Composition: six Primary nations (UK 13.73%, Korea 13.71%, Indonesia 12.03%, Sinian Federation 12.00%, Japan 7.81%, Australia 6.96%); Russia (core state) 2.14%. The old "sole-Primary China" frame is gone.
- The Mirny **culture file was rewritten in 24 places** on 2026-11-03 (cross-city comparisons removed, language set Hawaiian-first with the second slot open, false Concordia Arcanet link fixed, the Zhongshan "rivalry" deleted and left open). Food, music and everyday-life passages were de-framed and left for the CST. Log: `Research_Logs/Temirotkel_Mirny_Leftovers_Applied_2026-11-03.md`. **Mirny's record and its T8 files are unchanged**, so its pass files describe a state the culture file no longer holds; the developer decides how to reconcile.
- `verify_city_sheets.py Mirny` still shows **4 FAIL from the older sheet format** (P2 step/phase blocks; P3 spine addresses in section D). They predate today and need the sheets rebuilt in the current format before any new Mirny step relies on them.
- Mirny's `16`/`09` rows were recounted (robot term included).
- Santa Luce and Concordia are not involved.

## Other open items that do not block either
Concordia geothermal flag (A, B or C); the Demilitarized Zone; Esperanza's extent; Troll's faction line (parked); the Byrd–Amundsen pair check; the 11 Relung tier changes are in the picks file; Relung Panen is outside the run.

## Files written today that a fresh session may want
`DR-96`, `DR-97`, `DR-98` in `Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md`; tracker S.0z in `Research_Logs/TEPENIA_Research_Tracker_and_Handoff.md`; `Language_Blocs_By_City_2026-11-03.md` (and `.csv`); `Robot_Term_Added_To_16_Before_After_2026-11-03.md`; `Downstream_Quotes_Updated_2026-11-03.md`.
