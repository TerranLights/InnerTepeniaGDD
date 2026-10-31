# Davis — Datasheet · Step −1 (Input Contract)

> ⚠ **DRAFT — Tier C.** Built by citing INTO `Davis/00.1_Step_MINUS-1_Input_Contract.md` (itself an already 📎 *Files cited by line number here may carry a pointer to their copy in the `DerivationMechanisms` repo at the very END of the file (put there so no cited line moves): check the bottom of a cited file.*
> T8-verified pass output, unanimous, `triple_read_verify.py` 15/15). **Not yet independently re-verified via a
> fresh 3-reader T8 dispatch of its own**, per `Mechanical_Extraction_Field_Guide.md`'s standing note. A value +
> its citation, nothing else — no synthesis added here.

| Category | Value | Citation |
|---|---|---|
| Identity / designation | Davis | `Specs/Davis.md` L1, L3 (via `00.1` §2) |
| Coordinates | ~68°35′S, 77°58′E | `Specs/Davis.md` L3, L60 (via `00.1` §2) |
| Location descriptor | Vestfold Hills, Ingrid Christensen Coast, Prydz Bay | `Specs/Davis.md` L3, L60 (via `00.1` §2) |
| Parent | Mirny Arcanet subnet, Tepenian Federation | `Specs/Davis.md` L5 + census L494/L617 (via `00.1` §2) *(census lines re-pointed 2026-10-30; the pass cited L496/L613)* |
| Population magnitude → band | 1,158,314 → Band 5 (Regional) *[as recorded at the pass (2026-09-16); 1,182,231 since `DR-68`; the band is unchanged]* | `Specs/Davis.md` L15; census L494 (via `00.1` §2) *(re-pointed 2026-10-30 from L496)* |
| Census I (governs, `DR-4`) | 563,599 H / 594,715 R / 1,158,314 *[as recorded at the pass (2026-09-16); live since `DR-68`: 575,738 H / 606,493 R / 1,182,231]* | `Official_Population_Census.md` L494 (via `00.1` §2.1) |
| Census II | 437,423 H / 344,173 R / 781,596 *[as recorded at the pass (2026-09-16); live since `DR-68`: 445,531 H / 351,912 R / 797,443]* | `Official_Population_Census.md` L617 (via `00.1` §2.1) *(re-pointed 2026-10-30 from L611)* |
| Specs `Status:` field | States a later-era condition, not an in-frame input | `Specs/Davis.md` L4 (via `00.1` §2.3) |
| Admitted read spec (numeric, paste into `sed`/`awk`) | `1-3,5-8,10-87,90-120,122-134,143,148,153-155,176,178-179` = 137 lines | `00.1` §4.1 |
| Excluded entirely | `Local_Cultures/`, `Local_Robot_Culture/` (read-last), `City_Megasheets/` (withheld), `Test_Runs/` (zero intake), `City_Vision_Notes/` (struck corpus-wide), `Specs/Davis.md` L135–142/144–147/149–152/157–175/180–181 | `00.1` §4.3 |
| Spec length now vs the ranges the contract classifies *(row added 2026-10-30)* | `Specs/Mirny subnet/Davis.md` is **236 lines** (`wc -l`; 236 since the commit of 2026-09-16 that added the port ruling). The two ranges above end at **L181**, so **L182–236 are in neither** (Economy & Industry continues to L206; Notable Locations L207; Notable Figures L215; Connection to Concordia L220; Legacy L225; Open Questions L230). Not classified here: that is Step −1's act | `Specs/Mirny subnet/Davis.md` (live headings as listed); `00.1` §4.1, §4.3 |
| Generators, present/countable | G1 lopsided (no) · G2 ✅ · G3 ✅ · G4 ✅ · G5 ⚠ (no volume) · G6 ⛔ recorded null · G7 ⚠ (research unbuilt) · G8 ✅ — six countable of eight | `00.1` §3 |
| Symbol pair | **BLANK** since the developer ruling of 2026-09-16 *(the pass, `00.1` §3.1, recorded Earth / Earth, column-anchored, as of 2026-09-11)* | `City_Symbol_Assignments.md` L112 (the BLANK row); the superseded Earth / Earth record L335–341 |
| `G3` — function, the whole of it | one line, L143: *"Davis is, above all, Tepenia's breadbasket and a prime ecological/limnological research hub…"* | `Specs/Davis.md` L143 (via `00.1` §3.2) |
| `G8` arithmetic (hand-verified) | combined 67.48% · human 77.61% · robot 57.87% · spread 19.74 pp *[as recorded at the pass (2026-09-16); live since `DR-68`, derived by hand 2026-10-30: combined 67.45% · human 77.38% · robot 58.02% · spread 19.36 pp]* | `00.1` §3.3 |
| `G2` physical facts | ~400 km² ice-free exposed rock, lakes, fjord-like inlets · mean −10.0 °C · wind ~5.6 m/s (out of katabatic regime) · 72.8 mm/yr precipitation, ~28 mm lands · 37-day polar night, 55-day midnight sun | `00.1` §3.5 |
| `G5` route | Hwy 110, the Coastal Cut Highway: Zhongshan → Davis → Mirny → Casey → Concordia · access type `ON` · Prydz Bay maritime entry · no throughput figure exists | `00.1` §3.5 |
| Founding condition (`G4`) | Australian exiles; documentary inheritance (journals/logs/manuals), no living institution survived | `Specs/Davis.md` L127, L129 (via `00.1` §3.4) |
| `REQUESTED` outputs of this step | `R-3` (temp endpoints on two columns) · `R-7` (45mm/45% conflation) · `R-8` (superseded column set) · `R-9` (stale S01 pointer) · `REQ-G6` (0-match null) · `REQ-G5v` (no throughput figure) · `REQ-G7r` (no research log — Step 3's job) | `00.1` §7 |

**Not mechanical / not included here:** the admissibility ruling's own reasoning, the contamination diagnosis,
the four-category classification logic, the verdict.
