# Mirny · Application Batch 2: datasheet corrections · 2026-11-08

> **UPDATE 2026-11-08 (later the same day): APPLIED.** The developer approved this batch and the orchestrator applied it after a second reader passed it (`DR-123`). The status text below is the text as first written, kept as the record of the "shown first" step.

> ## STATUS: **PROPOSED, shown to the developer first. Nothing is applied.** On 2026-11-08 the developer answered DEC-141, DEC-163 and DEC-182 with *"Correct in place, show first (Recommended)"*; `DR-122` item 3 records it: *"Datasheet figures and live rows are corrected in place, each change shown first."* This file shows every change: the current row exactly as it stands today (with its line number and SHA-256), the proposed row exactly as it would stand, the kind of change, the source line that proves it and the piece finding that proposed it. **No datasheet, pass file, piece, spec, census or other source was edited.** The apply script in section 8 has not been run on the datasheets.
> **Scope:** the datasheet changes proposed by three pieces: `Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md` (section 2.6, findings AS12-45 to AS12-50, docket DK12-45 to DK12-50, DEC-141), `Amendment_Rederivation_ST13_Phase3_2026-11-05.md` (AS13-31, AS13-32, section 7.4 decision 4 = DEC-163, AR-220) and `Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md` (AS14-47, AS14-48, section 7.4 decision 3 = DEC-182). The datasheets for the other steps and phases are out of scope: none of the three pieces lists a correction for them.
> **Rules kept:** records are never reworded (`DR-102`): a row that is not wrong stays exactly as it is, and a corrected row keeps its old value in a dated marker (git keeps the rest) · Mirny only; no other location is named in this file · no name is coined for any group or role, and the pass author's old word for the weather organization is not used · every new figure and phrase was checked against a source line opened for this batch, never taken from a piece's own number.

---

## 0 · Summary

| Datasheet | Rows changed in place | Rows added (at the end) | UNPROVEN (not proposed) | Looked at, not changed (section 4) |
|---|--:|--:|---|---|
| `Datasheets/Step_-1.md` | 3 (L16, L26, L27) | 0 | 0 | 0 |
| `Datasheets/Step_0.md` | 6 (L14, L15, L16, L17, L18, L26) | 0 | 0 | 1 (L29) |
| `Datasheets/Step_1_and_2.md` | 4 (L8, L25, L26, L36) | 0 | 1 (the words "of each body" in the pieces' founders addendum) | 2 (L7, L33) |
| `Datasheets/Step_3.md` | 0 | 0 | 0 | 1 (L10) |
| `Datasheets/Phase_3.md` | 7 (L15, L16, L17, L18, L19, L20, L21) | 4 | 0 | 1 (L5) |
| `Datasheets/Phase_4.md` | 0 | 3 | 0 | 4 (L8; L20–L21; L25; L28–L30) |
| `Datasheets/Phase_5.md` | 4 (L17, L20, L25, L44) | 1 | 0 | 3 (L19; L22–L24; L30) |
| **Total** | **24** | **8** | **1** | **12 items** |

**In plain words.** The early-step sheets get two arithmetic fixes (the retention spread, 1.89 → 1.26 points, and the land needed at the live population, 137.5 and 196.5 → 140.35 and 200.51 km²), a note that the extent line they cite now holds the live row, the second census change (`DR-90`) beside the first, the supporting language as ruled (English and Russian, `DR-111`), the founders as the Register now gives them (Idelsk-Uralia also an exile group, `DR-99`) and the spec's real length (252 lines). The Phase 3 sheet gets the spec's real path, two corrected anchors and four rows of the spec's wind, precipitation and record-extreme figures. The Phase 4 sheet gets three rows: the live tiers, the language, the wind account. The Phase 5 sheet gets the colloquial name's ruled basis (`DR-47`), the spec path, the founders and one wind-account row on the relay. **Nothing else in any sheet changes.**

---

## 1 · How to read this batch

- **Line numbers** are those of the datasheets as they stand on 2026-11-08 (read about 10:50). Each current row carries its SHA-256 (of the line without its newline); the apply script refuses to touch a row whose hash differs.
- **Three rows are not reproduced** (`Phase_3.md` L21, `Phase_5.md` L20, `Phase_5.md` L25): the first two quote lines that name other locations, and the third carries withheld-source institution names, which are not inputs (`04_Phase_05_Relation_and_Geometry.md` L48) and which the Phases 4 and 5 piece also does not reproduce. For these three, this file gives the exact text replaced inside the row and its replacement; the script checks the whole row by its hash first, then replaces only that text.
- **Added rows go at the very end of each sheet**, under a dated heading, so no line that any pass file or piece cites moves (the reason the sheets' own pointer notes sit at the end, as their L5 says). The ST13 piece maps Phase 3's citations of the Phase 3 sheet to L13, L14, L22 and L26 to L29; those stay put.
- **The spec's path.** The live spec is `Cities/Specs/Mirny subnet/Mirny.md` (252 lines). `Cities/Specs/Mirny.md` does not exist on disk (checked 2026-11-08).
- **Short names:** ST12, ST13, ST14 = the three pieces named in the status box · `ANS` = `Amendment_Notes_2026-11-04_Answers_Carried_Forward.md` (the note of the developer's 2026-11-04 answers) · [CALC] = arithmetic done for this batch.
- **Kinds:** *arithmetic* (a figure recomputed from its stated inputs) · *ruling* (a developer ruling decides it) · *live source* (the source line now reads differently, or a path or anchor) · *new row* (DEC-163, DEC-182).

---

## 2 · Corrections in place (C-01 to C-24)

### C-01 · `Datasheets/Step_-1.md` L16 · spec length

**Finding:** ST12 AS12-50; docket DK12-50 (DEC-141). **Kind:** live source.

**Source line(s), opened 2026-11-08:** `Specs/Mirny subnet/Mirny.md`: 252 lines (line count, 2026-11-08). The 230-line copy of the same file is git `1a48edbc` (2026-10-13); compared line by line, its L46 to L230 sit at live L68 to L252 (+22): 180 identical, 5 with changed text at the same places (old L47, L69, L82, L112, L118).

**Current row, L16** (SHA-256 `541f8519992726840daff7277099a37bd0c78f9c7cc266e31253cb7dfe127090`):

```text
| Specs file length | 230 lines total (bound for any future read-spec computation) | Re-verified this turn |
```

**Proposed row, L16** (SHA-256 `4e7f0b12cabb0843b6cf0a257f93e1c959ef2a8e980bfc0c8451f10dbf25de5e`):

```text
| Specs file length | 252 lines total (bound for any future read-spec computation) *(corrected 2026-11-08, `DR-122`: 230 lines when this sheet was written; from old L46 on, every line now sits 22 lines lower)* | Re-verified 2026-11-08 (line count of `Specs/Mirny subnet/Mirny.md`; the 230-line copy is git `1a48edbc`) |
```

### C-02 · `Datasheets/Step_-1.md` L26 · Census I attribution

**Finding:** ST12 AS12-47; docket DK12-47 (DEC-141). **Kind:** live source.

**Source line(s), opened 2026-11-08:** `Official_Population_Census.md` L500: Mirny's Census I row carries two changes, `DR-68` (2026-10-28; *was 665,901 / 685,529 / 1,351,430*) and `DR-90` (2026-11-02), each recorded as arithmetic, not a migration. `Specs/Mirny subnet/Mirny.md` L15 carries the same two notes.

**Current row, L26** (SHA-256 `181aa072b84a418cd2f77ad87d329696257781d16af0c0d62d7409eb8213417b`):

```text
| Census I (repeat here, full derivation in `Step_0.md`) | 692,971 H / 710,578 R / 1,403,549 *(was 665,901 / 685,529 / 1,351,430 before the `DR-68` census change of 2026-10-28)* | `Specs/Mirny.md` L15 (§"Population & Composition"); cross-verified against `Official_Population_Census.md` L500 — **exact match, no discrepancy** (re-checked 2026-10-30) |
```

**Proposed row, L26** (SHA-256 `983b943a81c17230aaf1fe7861d22dcfae62e14a530a26ab2e32cc77e40f30e5`):

```text
| Census I (repeat here, full derivation in `Step_0.md`) | 692,971 H / 710,578 R / 1,403,549 *(was 665,901 / 685,529 / 1,351,430 before the `DR-68` census change of 2026-10-28; the live figures also carry `DR-90` of 2026-11-02)* | `Specs/Mirny.md` L15 (§"Population & Composition"); cross-verified against `Official_Population_Census.md` L500 — **exact match, no discrepancy** (re-checked 2026-10-30; attribution corrected 2026-11-08, `DR-122`) |
```

### C-03 · `Datasheets/Step_-1.md` L27 · Census II attribution

**Finding:** ST12 AS12-47; docket DK12-47 (DEC-141). **Kind:** live source.

**Source line(s), opened 2026-11-08:** `Official_Population_Census.md` L642: Mirny's Census II row carries `DR-68` (2026-10-28; *was 507,344 / 509,151 / 1,016,495*) and `DR-90` (2026-11-02). `Specs/Mirny subnet/Mirny.md` L16 carries the same two notes.

**Current row, L27** (SHA-256 `800ba7650c804429cb2a591a94207bf6130382edb88c86b14cce68083a57ff32`):

```text
| Census II | 524,022 H / 528,352 R / 1,052,374 *(was 507,344 / 509,151 / 1,016,495)* | `Specs/Mirny.md` L16 (§"Population & Composition"); cross-verified against `Official_Population_Census.md` L642 — **exact match** (re-checked 2026-10-30) |
```

**Proposed row, L27** (SHA-256 `e62caca3eef7050f3b94b1d2151056bf0772b3cb4aa1188ed8683d33f6b78dc8`):

```text
| Census II | 524,022 H / 528,352 R / 1,052,374 *(was 507,344 / 509,151 / 1,016,495 before the `DR-68` census change of 2026-10-28; the live figures also carry `DR-90` of 2026-11-02)* | `Specs/Mirny.md` L16 (§"Population & Composition"); cross-verified against `Official_Population_Census.md` L642 — **exact match** (re-checked 2026-10-30; attribution corrected 2026-11-08, `DR-122`) |
```

### C-04 · `Datasheets/Step_0.md` L14 · Census I attribution

**Finding:** ST12 AS12-47; docket DK12-47 (DEC-141). **Kind:** live source.

**Source line(s), opened 2026-11-08:** `Official_Population_Census.md` L500 (`DR-68` and `DR-90`, as for C-02); `Specs/Mirny subnet/Mirny.md` L15.

**Current row, L14** (SHA-256 `47a71720a2923911f3daac46e18b1a0168c211cad5e527fd85b335e386b440e9`):

```text
| Census I | 692,971 H / 710,578 R / **1,403,549** (revised 2026-07-04; `DR-68` 2026-10-28, was 665,901 / 685,529 / 1,351,430) | `Official_Population_Census.md` L500 — cross-verified against `Specs/Mirny.md` L15, exact match (re-checked 2026-10-30) |
```

**Proposed row, L14** (SHA-256 `d0fad77d081b4550396ce1ff2d4f9022934aef6347d664f38e1731e62e4f41c6`):

```text
| Census I | 692,971 H / 710,578 R / **1,403,549** (revised 2026-07-04; `DR-68` 2026-10-28, was 665,901 / 685,529 / 1,351,430; `DR-90` 2026-11-02) | `Official_Population_Census.md` L500 — cross-verified against `Specs/Mirny.md` L15, exact match (re-checked 2026-10-30; attribution corrected 2026-11-08, `DR-122`) |
```

### C-05 · `Datasheets/Step_0.md` L15 · Census II attribution

**Finding:** ST12 AS12-47; docket DK12-47 (DEC-141). **Kind:** live source.

**Source line(s), opened 2026-11-08:** `Official_Population_Census.md` L642 (`DR-68` and `DR-90`, as for C-03); `Specs/Mirny subnet/Mirny.md` L16.

**Current row, L15** (SHA-256 `5b05934ebd614add9e838469ed79b75c6dd95fa25b6f3af1a77d8cbc6f1beb44`):

```text
| Census II | 524,022 H / 528,352 R / **1,052,374** *(was 507,344 / 509,151 / 1,016,495)* | `Official_Population_Census.md` L642 — cross-verified against `Specs/Mirny.md` L16, exact match (re-checked 2026-10-30) |
```

**Proposed row, L15** (SHA-256 `5a30ebd5e0e5edfc8fcb9cb7b1f844a7e72755fb10ac4bedda1d0f03b51467a5`):

```text
| Census II | 524,022 H / 528,352 R / **1,052,374** *(was 507,344 / 509,151 / 1,016,495 before `DR-68` 2026-10-28; `DR-90` 2026-11-02)* | `Official_Population_Census.md` L642 — cross-verified against `Specs/Mirny.md` L16, exact match (re-checked 2026-10-30; attribution corrected 2026-11-08, `DR-122`) |
```

### C-06 · `Datasheets/Step_0.md` L16 · retention spread

**Finding:** ST12 AS12-45; docket DK12-45 (DEC-141). **Kind:** arithmetic.

**Source line(s), opened 2026-11-08:** `Official_Population_Census.md` L500 and L642: humans 524,022 ÷ 692,971 = 75.6196 %; robots 528,352 ÷ 710,578 = 74.3552 %; spread 1.2644, printed 1.26 [CALC]. The printed 1.89 is the spread of the interim rows that `Specs/Mirny subnet/Mirny.md` L15 and L16 record as the figures before `DR-90` (humans 515,452 ÷ 678,041 = 76.0208 %; robots 516,890 ÷ 697,307 = 74.1266 %; spread 1.8942) [CALC].

**Current row, L16** (SHA-256 `4be58f4c1f65bd5952df845987e1eb6f1a09b555cf30f75773d37741b8f3080c`):

```text
| Retention (computed; formula = retained ÷ Census-I count) | combined 74.98% · human 75.62% · robot 74.36% · spread **1.89 pp toward humans** | Computed from the two rows above: 1,052,374÷1,403,549 = 74.98%; 524,022÷692,971 = 75.62%; 528,352÷710,578 = 74.36% |
```

**Proposed row, L16** (SHA-256 `b09fbe827eef059d5dd1622c5713400bd1cfd1de651a3b55a3ed19fe66c3cce4`):

```text
| Retention (computed; formula = retained ÷ Census-I count) | combined 74.98% · human 75.62% · robot 74.36% · spread **1.26 pp toward humans** *(corrected 2026-11-08, `DR-122`: was 1.89, the spread of the superseded interim rows of 2026-10-28)* | Computed from the two rows above: 1,052,374÷1,403,549 = 74.98%; 524,022÷692,971 = 75.62%; 528,352÷710,578 = 74.36%; spread 75.62 − 74.36 = 1.26 (unrounded 75.6196 − 74.3552 = 1.2644) |
```

### C-07 · `Datasheets/Step_0.md` L17 · extent snapshot

**Finding:** ST12 AS12-46; docket DK12-46 (DEC-141). **Kind:** live source.

**Source line(s), opened 2026-11-08:** `Extent_and_Density_Per_City.md` (Universal_Location_Methodology folder) L611: `| **Mirny** | Mirny | 1,403,549 | 140 | 201 | **coastal ice** |`; header L603 (`| City | Subnet | Census I | @10k | @7k | Site |`); L631 ends *"(Census I of 2026-11-03; the census is the live source.)"*. The 2026-09-05 snapshot (1,351,430 · 135 · 193) is no longer on L611.

**Current row, L17** (SHA-256 `1e6543aff573f18715af2e2ec5e7dc41678988d521927c2c8200797b4ca91a33`):

```text
| Extent *(2026-09-05 snapshot; the census is live — note L631)* | Mirny · Subnet Mirny · Census I (snapshot) 1,351,430 · @10,000/km² **135 km²** · @7,000/km² **193 km²** · Site: coastal ice | `Extent_and_Density_Per_City.md` L611 (table header L603; snapshot note L631) |
```

**Proposed row, L17** (SHA-256 `5a9596cdefe97270cab60bab9a99a234d78d5aea08da4df7beda19fd0e31925d`):

```text
| Extent *(2026-09-05 snapshot; the census is live — note L631)* | Mirny · Subnet Mirny · Census I (snapshot) 1,351,430 · @10,000/km² **135 km²** · @7,000/km² **193 km²** · Site: coastal ice *(a record of the 2026-09-05 table. Corrected 2026-11-08, `DR-122`: the cited line now holds the live row, Census I of 2026-11-03: 1,403,549 · @10,000/km² **140 km²** · @7,000/km² **201 km²** · Site: coastal ice)* | `Extent_and_Density_Per_City.md` L611 (table header L603; note L631, which now reads *"Census I of 2026-11-03; the census is the live source."*) |
```

### C-08 · `Datasheets/Step_0.md` L18 · extent, computed

**Finding:** ST12 AS12-46; docket DK12-46 (DEC-141). **Kind:** arithmetic.

**Source line(s), opened 2026-11-08:** `Official_Population_Census.md` L500 (1,403,549): 1,403,549 ÷ 10,000 = 140.3549; ÷ 7,000 = 200.5070 [CALC]; `Extent_and_Density_Per_City.md` L611 prints 140 and 201. The printed 137.5 and 196.5 are 1,375,348 ÷ 10,000 = 137.5348 and ÷ 7,000 = 196.4783 [CALC], where 1,375,348 is the total before `DR-90` recorded on `Specs/Mirny subnet/Mirny.md` L15.

**Current row, L18** (SHA-256 `a89f5df808a10ff726ff921ac736424c885fa809ad14e2b5c41f078515440c1a`):

```text
| Extent at the live Census I (computed) | 137.5 km² @10,000/km² · 196.5 km² @7,000/km² | Computed: 1,403,549÷10,000 = 137.5; 1,403,549÷7,000 = 196.5 (Census I from `Official_Population_Census.md` L500; the two densities are the extent table's column heads) |
```

**Proposed row, L18** (SHA-256 `7b8518a5e004b2b42e36a4e3ed045d5c2a8098dda4bb44caec2d9c82678dd787`):

```text
| Extent at the live Census I (computed) | 140.35 km² @10,000/km² · 200.51 km² @7,000/km² *(corrected 2026-11-08, `DR-122`: was 137.5 and 196.5, computed from the superseded interim total 1,375,348)* | Computed: 1,403,549÷10,000 = 140.35; 1,403,549÷7,000 = 200.51 (Census I from `Official_Population_Census.md` L500; the two densities are the extent table's column heads; the table's own row, `Extent_and_Density_Per_City.md` L611, prints 140 and 201) |
```

### C-09 · `Datasheets/Step_0.md` L26 · supporting language

**Finding:** ST12 AS12-48; docket DK12-48 (DEC-141). **Kind:** ruling.

**Source line(s), opened 2026-11-08:** `DEVELOPER_RULINGS_LOG.md` L1769 (`DR-111`, 2026-11-04): *"Mirny's supporting tier is **English and Russian**, set by the developer as a Mirny special case ... not by the 12-point rule, which by actual speakers gives English alone. Hawaiian (later Tepenian) remains dominant."* Also `Amendment_Notes_2026-11-04_Answers_Carried_Forward.md` L10.

**Current row, L26** (SHA-256 `adef7975d1b19be41aeb718519c8ab93147f8903375cf501af8228a675c8a6a0`):

```text
| **Language** (set 2026-11-03) | Hawaiian (later Tepenian) is the dominant language. **Supporting tier: English** — a language not dominant but widely enough understood that business, social talk and general dealings can be done in it; the set is every language group within 12 percentage points of the city's largest group (range mid-points; nations sharing a language summed). Largest group: English 25.2–34.4. No other group is within 12 percentage points, so the supporting tier is that language alone. *These are shares of residents whose national origin is a nation of that language, not counts of speakers; the mapping of nations to languages is recalled general knowledge, not verified.* | `Research_Logs/Language_Sets_By_City_Reference_2026-11-03.md` (12-point addendum and rulings); `Research_Logs/Language_Blocs_By_City_2026-11-03.md` |
```

**Proposed row, L26** (SHA-256 `a16a9bab2d56bc0da6a8b6775d85b38e6b07c493ac44836c29c70572e9f40c5e`):

```text
| **Language** (set 2026-11-03) | Hawaiian (later Tepenian) is the dominant language. **Supporting tier: English and Russian** (set by the developer as a Mirny special case, `DR-111`, 2026-11-04; corrected here 2026-11-08, `DR-122`) — a language not dominant but widely enough understood that business, social talk and general dealings can be done in it; the 12-point rule's set is every language group within 12 percentage points of the city's largest group (range mid-points; nations sharing a language summed). Largest group: English 25.2–34.4. No other group is within 12 percentage points, so the 12-point rule alone gives English, as it does by actual speakers (`DR-111`). *These are shares of residents whose national origin is a nation of that language, not counts of speakers; the mapping of nations to languages is recalled general knowledge, not verified.* | `Research_Logs/Language_Sets_By_City_Reference_2026-11-03.md` (12-point addendum and rulings); `Research_Logs/Language_Blocs_By_City_2026-11-03.md`; `DEVELOPER_RULINGS_LOG.md` L1769 (`DR-111`) |
```

### C-10 · `Datasheets/Step_1_and_2.md` L8 · spec length in the draft box

**Finding:** ST12 AS12-50; docket DK12-50 (DEC-141). **Kind:** live source.

**Source line(s), opened 2026-11-08:** `Specs/Mirny subnet/Mirny.md`: 252 lines (line count, 2026-11-08), as for C-01.

**Current row, L8** (SHA-256 `baac4bac5b6c6d4a6911f76316bf5499ae31c61395eb99301a309f035480a326`):

```text
> detailed (230 lines) — this table extracts only what belongs to the physical/environmental capability
```

**Proposed row, L8** (SHA-256 `abeabb5c5ff871cf23ace9b24f717fcaf56ccae10dbf8de9d1dc44d452b0b30d`):

```text
> detailed (230 lines when this sheet was written; 252 lines on 2026-11-08, `DR-122`) — this table extracts only what belongs to the physical/environmental capability
```

### C-11 · `Datasheets/Step_1_and_2.md` L25 · extent snapshot (same row as C-07)

**Finding:** ST12 AS12-46; docket DK12-46 (DEC-141). **Kind:** live source.

**Source line(s), opened 2026-11-08:** `Extent_and_Density_Per_City.md` (Universal_Location_Methodology folder) L611: `| **Mirny** | Mirny | 1,403,549 | 140 | 201 | **coastal ice** |`; header L603 (`| City | Subnet | Census I | @10k | @7k | Site |`); L631 ends *"(Census I of 2026-11-03; the census is the live source.)"*. The 2026-09-05 snapshot (1,351,430 · 135 · 193) is no longer on L611.

**Current row, L25** (SHA-256 `1e6543aff573f18715af2e2ec5e7dc41678988d521927c2c8200797b4ca91a33`):

```text
| Extent *(2026-09-05 snapshot; the census is live — note L631)* | Mirny · Subnet Mirny · Census I (snapshot) 1,351,430 · @10,000/km² **135 km²** · @7,000/km² **193 km²** · Site: coastal ice | `Extent_and_Density_Per_City.md` L611 (table header L603; snapshot note L631) |
```

**Proposed row, L25** (SHA-256 `5a9596cdefe97270cab60bab9a99a234d78d5aea08da4df7beda19fd0e31925d`):

```text
| Extent *(2026-09-05 snapshot; the census is live — note L631)* | Mirny · Subnet Mirny · Census I (snapshot) 1,351,430 · @10,000/km² **135 km²** · @7,000/km² **193 km²** · Site: coastal ice *(a record of the 2026-09-05 table. Corrected 2026-11-08, `DR-122`: the cited line now holds the live row, Census I of 2026-11-03: 1,403,549 · @10,000/km² **140 km²** · @7,000/km² **201 km²** · Site: coastal ice)* | `Extent_and_Density_Per_City.md` L611 (table header L603; note L631, which now reads *"Census I of 2026-11-03; the census is the live source."*) |
```

### C-12 · `Datasheets/Step_1_and_2.md` L26 · extent, computed (same row as C-08)

**Finding:** ST12 AS12-46; docket DK12-46 (DEC-141). **Kind:** arithmetic.

**Source line(s), opened 2026-11-08:** `Official_Population_Census.md` L500 (1,403,549): 1,403,549 ÷ 10,000 = 140.3549; ÷ 7,000 = 200.5070 [CALC]; `Extent_and_Density_Per_City.md` L611 prints 140 and 201. The printed 137.5 and 196.5 are 1,375,348 ÷ 10,000 = 137.5348 and ÷ 7,000 = 196.4783 [CALC], where 1,375,348 is the total before `DR-90` recorded on `Specs/Mirny subnet/Mirny.md` L15.

**Current row, L26** (SHA-256 `a89f5df808a10ff726ff921ac736424c885fa809ad14e2b5c41f078515440c1a`):

```text
| Extent at the live Census I (computed) | 137.5 km² @10,000/km² · 196.5 km² @7,000/km² | Computed: 1,403,549÷10,000 = 137.5; 1,403,549÷7,000 = 196.5 (Census I from `Official_Population_Census.md` L500; the two densities are the extent table's column heads) |
```

**Proposed row, L26** (SHA-256 `7b8518a5e004b2b42e36a4e3ed045d5c2a8098dda4bb44caec2d9c82678dd787`):

```text
| Extent at the live Census I (computed) | 140.35 km² @10,000/km² · 200.51 km² @7,000/km² *(corrected 2026-11-08, `DR-122`: was 137.5 and 196.5, computed from the superseded interim total 1,375,348)* | Computed: 1,403,549÷10,000 = 140.35; 1,403,549÷7,000 = 200.51 (Census I from `Official_Population_Census.md` L500; the two densities are the extent table's column heads; the table's own row, `Extent_and_Density_Per_City.md` L611, prints 140 and 201) |
```

### C-13 · `Datasheets/Step_1_and_2.md` L36 · founding population

**Finding:** ST12 AS12-49; docket DK12-49 (DEC-141). **Kind:** ruling.

**Source line(s), opened 2026-11-08:** `Founding_Register.md` L57: *"**Founded by Idelsk-Uralia** (replacing Russia in the founding-nation role); **exile groups present: Idelsk-Uralia (also), Russia, Australia and the Sinian Federation (China)**"*. `DEVELOPER_RULINGS_LOG.md` L1660 (`DR-99`): Idelsk-Uralia *"also sent people"*; *"The founding share to carry is **23.24 %** ... founders remain a minority"*; L1742 (`DR-108` item 4): the spec's L174, L251 and L252 are to be corrected to follow the Register. `Specs/Mirny subnet/Mirny.md` L174 still reads *"with exile groups from Russia, Australia and the Sinian Federation (China) present"* (three groups): not yet applied.

**Current row, L36** (SHA-256 `d6476a9c7e57e3cc5752e94cc65ab9856eee2b678b8c8ebc0b59ba40e444b8c9`):

```text
| Founding population | Founded by Idelsk-Uralia, with exile groups from Russia, China (the Sinian Federation) and Australia (`DR-9`, `DR-46`, `DR-54`). Spec L174 was rewritten 2026-10-13 to match; the old *"Primarily Russian exiles…"* no longer stands. (Refreshed 2026-10-21 against the corrected spec and the Founding Register.) | `Founding_Register.md` L57 (Mirny row), L88 (the `DR-46` entry), L94 (the 2026-10-13 spec cleanup entry) (`DR-9`) |
```

**Proposed row, L36** (SHA-256 `ffcfcbe119915a8e8cbc318782f6732eeab16dafc87b89f2d32c09c38415424c`):

```text
| Founding population | Founded by Idelsk-Uralia (replacing Russia in the founding-nation role); exile groups present: Idelsk-Uralia (also), Russia, Australia and the Sinian Federation (China) (`DR-9`, `DR-46`, `DR-54`, `DR-99`). The founding share to carry is 23.24 %; founders remain a minority (`DR-99`). Spec L174 was rewritten 2026-10-13 to match `DR-46`; the old *"Primarily Russian exiles…"* no longer stands. (Refreshed 2026-10-21 against the corrected spec and the Founding Register. Corrected 2026-11-08, `DR-122`: Idelsk-Uralia is also an exile group, `DR-99`; spec L174 still lists three exile groups and lags the Register; its correction is ruled, not yet applied, `DR-108`.) | `Founding_Register.md` L57 (Mirny row), L88 (the `DR-46` entry), L94 (the 2026-10-13 spec cleanup entry) (`DR-9`); `DEVELOPER_RULINGS_LOG.md` L1660 (`DR-99`), L1742 (`DR-108` item 4) |
```

### C-14 · `Datasheets/Phase_3.md` L15 · coastal terrain: path

**Finding:** ST13 AS13-31 (a); docket DK13-31 (the path and anchors ride with DEC-141). **Kind:** live source (path).

**Source line(s), opened 2026-11-08:** The live spec is `Cities/Specs/Mirny subnet/Mirny.md`; `Cities/Specs/Mirny.md` does not exist (checked on disk 2026-11-08). Live L79 begins with the quoted sentence.

**Current row, L15** (SHA-256 `6abe535bb981835c6841228e5ab8ca812d57e06d8c185ba319dcdeb57619f240`):

```text
| Coastal terrain, stated directly | *"The coast here is rocky and exposed. Katabatic winds off the East Antarctic ice sheet funnel toward the coast with significant force"* | `Specs/Mirny.md` L79 |
```

**Proposed row, L15** (SHA-256 `8b6d23a57625bf7b5b53031bf7998a47e95127294eceb70bfb49e667e8e3ce03`):

```text
| Coastal terrain, stated directly | *"The coast here is rocky and exposed. Katabatic winds off the East Antarctic ice sheet funnel toward the coast with significant force"* | `Specs/Mirny subnet/Mirny.md` L79 |
```

### C-15 · `Datasheets/Phase_3.md` L16 · architecture: ring anchor and path

**Finding:** ST13 AS13-31 (a), (b); docket DK13-31. **Kind:** live source (anchor and path).

**Source line(s), opened 2026-11-08:** The live spec is `Cities/Specs/Mirny subnet/Mirny.md`; `Cities/Specs/Mirny.md` does not exist (checked on disk 2026-11-08). Live L184 is the architecture line (airlock entries). The contract's map row for old L162 (`00.1_Step_MINUS-1_Input_Contract.md` L333) says the ring survives in *"L174 chars 272–623"*; old L174 is identical to live L196 (git `1a48edbc` and `67d091af` against the live file), and live L196 chars 272–623 are the clause *"**Established 2026-07-05:** also a genuine industrial/construction engine ... at the sheltered industrial core inside the city's outer wind-fortified ring."*

**Current row, L16** (SHA-256 `ca6ab260fa8ce39d8af22ca5204364b0ebad323c5a509a691150e21d43b26605`):

```text
| Architecture | ⛔ **Not an input** — the whole line is EXCLUDED by the Step −1 contract (culture section); its airlock-entry detail is open as Q-2. The wind-shedding ring survives in the admitted economy text, L174 chars 272–623 | `Specs/Mirny.md` L184; `00.1_Step_MINUS-1_Input_Contract.md` §B L162 |
```

**Proposed row, L16** (SHA-256 `49a647a352fa8f36804f273053d9242757af56c3ffa936fb2b7fb3ddf6f97182`):

```text
| Architecture | ⛔ **Not an input** — the whole line is EXCLUDED by the Step −1 contract (culture section); its airlock-entry detail is open as Q-2. The wind-shedding ring survives in the admitted economy text, L196 chars 272–623 (the contract's old L174; anchor corrected 2026-11-08, `DR-122`) | `Specs/Mirny subnet/Mirny.md` L184, L196; `00.1_Step_MINUS-1_Input_Contract.md` §B L162 |
```

### C-16 · `Datasheets/Phase_3.md` L17 · building layout: path

**Finding:** ST13 AS13-31 (a); docket DK13-31. **Kind:** live source (path).

**Source line(s), opened 2026-11-08:** The live spec is `Cities/Specs/Mirny subnet/Mirny.md`; `Cities/Specs/Mirny.md` does not exist (checked on disk 2026-11-08). Live L190 is the developer-vision paragraph.

**Current row, L17** (SHA-256 `7fd39f8e366f76b4e4dca5a6bee8a428c6e25fa53c89189a54e727aa61c2d7fc`):

```text
| Building layout | ⛔ **Not an input at any step of the ULM** — developer-vision paragraph, post-ULM (`DR-10`) | `Specs/Mirny.md` L190 |
```

**Proposed row, L17** (SHA-256 `bbb6f859ac6dc55d95e155b26f014f399697bdb7de4de15efb10af80e0905bcf`):

```text
| Building layout | ⛔ **Not an input at any step of the ULM** — developer-vision paragraph, post-ULM (`DR-10`) | `Specs/Mirny subnet/Mirny.md` L190 |
```

### C-17 · `Datasheets/Phase_3.md` L18 · amenity texture: path

**Finding:** ST13 AS13-31 (a); docket DK13-31. **Kind:** live source (path).

**Source line(s), opened 2026-11-08:** The live spec is `Cities/Specs/Mirny subnet/Mirny.md`; `Cities/Specs/Mirny.md` does not exist (checked on disk 2026-11-08). Live L190, as C-16.

**Current row, L18** (SHA-256 `7e57aab16af771e20a064485611e2bf3acecda167499cfda0c353abaffe431d8`):

```text
| Entertainment/amenity texture | ⛔ **Not an input at any step of the ULM** — same developer-vision paragraph (`DR-10`) | `Specs/Mirny.md` L190 |
```

**Proposed row, L18** (SHA-256 `2091d948dc88b0b14497d8ad64f815a8dc292d2ddc19f8c5f66e93dc7ba4ae4c`):

```text
| Entertainment/amenity texture | ⛔ **Not an input at any step of the ULM** — same developer-vision paragraph (`DR-10`) | `Specs/Mirny subnet/Mirny.md` L190 |
```

### C-18 · `Datasheets/Phase_3.md` L19 · solstice light: anchor, quotation, path

**Finding:** ST13 AS13-31 (a), (c); AS13-32 (d); docket DK13-31. **Kind:** live source (anchor, quotation and path).

**Source line(s), opened 2026-11-08:** The live spec is `Cities/Specs/Mirny subnet/Mirny.md`; `Cities/Specs/Mirny.md` does not exist (checked on disk 2026-11-08). Old L132 is identical to live L154 (git `1a48edbc` against the live file), which begins *"- **The solstice grazing events:** on the winter solstice, the sun barely clears (or doesn't clear) the horizon"*; the phrase "sun-grazing events" is on live L205, a line the contract excluded. The contract's map row for old L132 (`00.1_Step_MINUS-1_Input_Contract.md` L307) reads *"SPLIT — 1–380 ADMITTED-DEMOTED"*. Live L77 and L107 to L108 carry the corrected light data.

**Current row, L19** (SHA-256 `2a3f0e42d05c7b13444b07d2eace405c13116d6de10b63a19d77fca4144a621c`):

```text
| The solstice light | ⚠ L132's "sun-grazing events" is residue of the retracted symmetric light model (ADMITTED-DEMOTED at Step −1, → R-2). The corrected data: **no polar night** — on the winter solstice the sun clears the horizon, low and briefly; **~29 days of midnight sun**, Dec 8 → Jan 5 | `Specs/Mirny.md` L77, L107–108 (corrected 2026-09-04); L132 demoted |
```

**Proposed row, L19** (SHA-256 `189e02f90ffc0e8c3a45804b12a9629d28fdc65a1532fd7fd37e4e289e9c152a`):

```text
| The solstice light | ⚠ L154's (the contract's old L132) "solstice grazing events" is residue of the retracted symmetric light model (ADMITTED-DEMOTED at Step −1, → R-2). The corrected data: **no polar night** — on the winter solstice the sun clears the horizon, low and briefly; **~29 days of midnight sun**, Dec 8 → Jan 5 | `Specs/Mirny subnet/Mirny.md` L77, L107–108 (corrected 2026-09-04); L154 (old L132) demoted *(anchor and quoted phrase corrected 2026-11-08, `DR-122`)* |
```

### C-19 · `Datasheets/Phase_3.md` L20 · blizzard and visibility: path

**Finding:** ST13 AS13-31 (a); docket DK13-31. **Kind:** live source (path).

**Source line(s), opened 2026-11-08:** The live spec is `Cities/Specs/Mirny subnet/Mirny.md`; `Cities/Specs/Mirny.md` does not exist (checked on disk 2026-11-08). Live L156 is the blizzards line; live L104 carries the clear-sky whiteout sentence.

**Current row, L20** (SHA-256 `9a6700c5bae3df3544b3c571b436e1bcdd60e732e1b00c97840afed9ead38d99`):

```text
| Blizzard/visibility conditions, stated directly | *"Blizzards: with katabatic winds and available surface snow, blizzard conditions can develop rapidly; visibility collapses quickly in major events"* · *"Whiteout here routinely occurs under a clear sky, because the snow is lifted, not falling"* | `Specs/Mirny.md` L156, L104 (cross-ref `Phase_1.md`) |
```

**Proposed row, L20** (SHA-256 `050a94b37fd14a96476e4db9499126c7a434093e18fbadb7acb8aac6a5ccfb51`):

```text
| Blizzard/visibility conditions, stated directly | *"Blizzards: with katabatic winds and available surface snow, blizzard conditions can develop rapidly; visibility collapses quickly in major events"* · *"Whiteout here routinely occurs under a clear sky, because the snow is lifted, not falling"* | `Specs/Mirny subnet/Mirny.md` L156, L104 (cross-ref `Phase_1.md`) |
```

### C-20 · `Datasheets/Phase_3.md` L21 · sea ice: path (row not reproduced)

**Finding:** ST13 AS13-31 (a); docket DK13-31. **Kind:** live source (path).

**Source line(s), opened 2026-11-08:** The live spec is `Cities/Specs/Mirny subnet/Mirny.md`; `Cities/Specs/Mirny.md` does not exist (checked on disk 2026-11-08). Live L155 is the sea-ice line the row quotes.

**Current row, L21:** not reproduced (see section 1); SHA-256 `b6e0df3b134e56812e9c0c6341e26f8d2c23e9ebfaae6461a56c40c84b3e4c4e`, 184 characters. **Text replaced inside the row, exactly:**

Replace (1):

```text
| `Specs/Mirny.md` L155 |
```

with:

```text
| `Specs/Mirny subnet/Mirny.md` L155 |
```

Proposed row's SHA-256 after the replacement: `5407242b0d73a1ffe90d9ef78a63bf6274ebb54d19910fe32d0a4cc5f8ac009d`.

### C-21 · `Datasheets/Phase_5.md` L17 · the subnet's colloquial name

**Finding:** ST14 AS14-48 (a); docket DK14-48 (DEC-141). **Kind:** ruling.

**Source line(s), opened 2026-11-08:** `DEVELOPER_RULINGS_LOG.md` L975 (`DR-47`, 2026-10-03): *"common people call the Mirny subnet 'the Australian subnet' because Australia is its leading founder"*; `04_Phase_05_Relation_and_Geometry.md` L107 item 4: `DR-47` gives the name *"an in-world basis, **partly superseding `DR-13`'s 'geographic only'**"*. `City_Relationship_Database.md` L334 is still Mirny's entry heading.

**Current row, L17** (SHA-256 `e8318e454ad3df752d463b085f4b0244750411e750274102d3c37e8f10035de9`):

```text
| `City_Relationship_Database.md` — Mirny's own header | Region: East Antarctic coast · Arcanet subnet: Mirny ("Australian", a geographic nickname only, `DR-13`) — **hub city**. The source's national label for the city rests on the station and is not carried (`DR-19`) | `City_Relationship_Database.md` L334–341 (entry heading L334) |
```

**Proposed row, L17** (SHA-256 `d72058892afd88836dd3816eade88349d8f33c0eb94645c1d635c8e4c17b6908`):

```text
| `City_Relationship_Database.md` — Mirny's own header | Region: East Antarctic coast · Arcanet subnet: Mirny ("Australian": common people call it "the Australian subnet" because Australia is its leading founder, an in-world basis, `DR-47`, partly superseding `DR-13`'s "geographic nickname only"; corrected 2026-11-08, `DR-122`) — **hub city**. The source's national label for the city rests on the station and is not carried (`DR-19`) | `City_Relationship_Database.md` L334–341 (entry heading L334); `DEVELOPER_RULINGS_LOG.md` L975 (`DR-47`); `04_Phase_05_Relation_and_Geometry.md` L107 item 4 |
```

### C-22 · `Datasheets/Phase_5.md` L20 · relay row: path (row not reproduced)

**Finding:** ST14 AS14-48 (c); docket DK14-48. **Kind:** live source (path).

**Source line(s), opened 2026-11-08:** The live spec is `Cities/Specs/Mirny subnet/Mirny.md`; `Cities/Specs/Mirny.md` does not exist (checked on disk 2026-11-08). Live L206 is the relay-hardware line the row quotes.

**Current row, L20:** not reproduced (see section 1); SHA-256 `a20f5952255c2fec9abf020cf13096efb5e4fb90e876b426111d35fa5aab4703`, 593 characters. **Text replaced inside the row, exactly:**

Replace (1):

```text
| `Specs/Mirny.md` L206 |
```

with:

```text
| `Specs/Mirny subnet/Mirny.md` L206 |
```

Proposed row's SHA-256 after the replacement: `2f0229b9f2573f07457d0058287e831cf7de10d7be253a985aff5828b05d5c9e`.

### C-23 · `Datasheets/Phase_5.md` L25 · founders in the civic-institutions row (row not reproduced)

**Finding:** ST14 AS14-48 (e); docket DK14-48. **Kind:** ruling.

**Source line(s), opened 2026-11-08:** `Founding_Register.md` L57 (four exile groups, Idelsk-Uralia among them); `DEVELOPER_RULINGS_LOG.md` L1660 (`DR-99`).

**Current row, L25:** not reproduced (see section 1); SHA-256 `ab8ed0ca77b8744f55f256a231b8a2ac4f708ffc1fcdb3e54714f0cac5dbadcf`, 692 characters. **Text replaced inside the row, exactly:**

Replace (1):

```text
names two of the three founding stocks
```

with:

```text
names two of the four founding stocks
```

Replace (2):

```text
with exile groups from Russia, China and Australia (`DR-9`, `DR-46`, `DR-54`)
```

with:

```text
with exile groups Idelsk-Uralia (also), Russia, Australia and the Sinian Federation (China) (`DR-9`, `DR-46`, `DR-54`, `DR-99`; `Founding_Register.md` L57)
```

Replace (3):

```text
*(refreshed 2026-10-21)*
```

with:

```text
*(refreshed 2026-10-21; corrected 2026-11-08, `DR-99`, `DR-122`)*
```

Proposed row's SHA-256 after the replacement: `f1323ceaf016479ef02b88e03d8837d8994c007807cb3ceb6c402b925869c7a0`.

### C-24 · `Datasheets/Phase_5.md` L44 · the flag's founders citation

**Finding:** ST14 AS14-48 (f); docket DK14-48. **Kind:** ruling.

**Source line(s), opened 2026-11-08:** `DEVELOPER_RULINGS_LOG.md` L960 (`DR-46`, Mirny: *"**Amends `DR-9`**"*) and L1660 (`DR-99`); `Founding_Register.md` L57.

**Current row, L44** (SHA-256 `42b4d13e329333bbfb4b8195c605da852365000f5fd31545b8f8d56931d480b9`):

```text
> the founders shared by geography and access (`DR-9`, `DR-19`), never on "heritage"; the tie is re-grounded,
```

**Proposed row, L44** (SHA-256 `612049cc8d8042edd14ac89c3133f45780f44cc18db4bddc0939a8d6e4170253`):

```text
> the founders shared by geography and access (`DR-9` as amended by `DR-46` and `DR-99`, `Founding_Register.md` L57, corrected 2026-11-08; `DR-19`), never on "heritage"; the tie is re-grounded,
```

---

## 3 · Rows added (A-01 to A-08)

Each block below is appended exactly as shown after the sheet's last line (its current last line and line count are checked first). The rows use the sheet's own three-column format.

### A-01..A-04 · `Datasheets/Phase_3.md` · appended after L29

**Decision and finding:** DEC-163 (ST13 section 7.4, decision 4; AR-220); ST13 AS13-31 coverage; docket DK13-31. **Kind:** new row.

**Current last line, L29** (SHA-256 `34ca317d2a54915423e94f9d2a7df6b12a432037ea0e0ba313a1a56c667f51d0`):

```text
quotes above are raw material for that work, not a substitute for it.
```

**Sources, by row (opened 2026-11-08):**

- **A-01:** `Specs/Mirny subnet/Mirny.md` L93.
- **A-02:** `Specs/Mirny subnet/Mirny.md` L104 (quoted with its bold marks removed, as the sheet's own quotations do).
- **A-03:** `Specs/Mirny subnet/Mirny.md` L94, L98, L99, L100, L101, L104.
- **A-04:** `Specs/Mirny subnet/Mirny.md` L92.

**Block appended (the first line is blank):**

```text

## Added 2026-11-08 (`DR-122`, DEC-163): the live spec's wind, precipitation and record-extreme rows Phase 3 rests on

*Placed at the end of the file so no cited line moves. Quoted from the live 252-line spec; each line opened 2026-11-08.*

| Category | Value | Citation |
|---|---|---|
| Prevailing winds, stated directly | *"katabatic from the south and southeast (off the East Antarctic plateau)"* · *"average wind speeds 10–14 m/s; sustained storms exceeding 40 m/s (144 km/h) have been recorded; wind is the dominant environmental feature of this city"* *(the clause ranking the station among others is not carried)* | `Specs/Mirny subnet/Mirny.md` L93 |
| Wind against cold, stated directly | *"WIND, decisively — the cold is NOT what defines this city."* · *"At -11.2 °C the cold is a backdrop."* · *"… mean wind 12.0 m/s: up to a third of snowfall evaporates before it lands, and most of the remainder is entrained and carried past."* *(the comparing words before "mean wind" are not carried; the clear-sky whiteout sentence is already quoted at L20)* | `Specs/Mirny subnet/Mirny.md` L104 |
| Precipitation and retention | Annual precipitation **527.1 mm** water equivalent (measured monthly normals) · Regime: KATABATIC MARGIN, *"snow flux, not snowfall"* · Falls (reaches the surface) ~527 mm/yr · Lands (accumulates and stays) **~200 mm/yr** (~38% retention) · Lost to sublimation and wind transport ~327 mm/yr · *"Retention ~38% — residents dig out from what arrived from upwind, not from what fell on them."* | `Specs/Mirny subnet/Mirny.md` L94, L98–L101, L104 |
| Record extremes | Record high **+8.7 °C** (Dec) · record low **-36.5 °C** (Aug) — NOAA NCEI GHCN-Daily station `AYM00089592`, direct, 0 km; daily observations 1973-2026 *(researched 2026-09-04)* | `Specs/Mirny subnet/Mirny.md` L92 |
```

After the append the sheet has 40 lines.

### A-05..A-07 · `Datasheets/Phase_4.md` · appended after L30

**Decision and finding:** DEC-182 (ST14 section 7.4, decision 3); ST14 AS14-47 coverage; docket DK14-47. **Kind:** new row.

**Current last line, L30** (SHA-256 `2d28fbd87b009456e1f961c120f7ffb845ab417ec7066d8658fb2d157c0c4396`):

```text
which exists yet for Mirny.
```

**Sources, by row (opened 2026-11-08):**

- **A-05:** `16_Per_City_Three_Tier_Run.md` L2110 (*"## 20. ✅ MIRNY — DETERMINED"*), L2114 (baseline 446,228, 42.2%), L2115 (mandated 244,334, 23.1%), L2116 (*"FREE — the character budget"* 366,502, 34.7%), L2118 (*"Distinctive tier: 610,836 (57.8%)"*), L2119 (*"robots × 15.75 ÷ 1,000 = 11,192 workers"*, `DR-97`), L2121 (*"developer ruling C"*), L2123 (the mandate table's column *"Share of distinctive"*), L2131 (*"Half B mandated only the Arcanet 20%"*), L276 (Half B: 1,057,064 · 42.2% · 11.6% · 46.2%); 446,228 + 244,334 + 366,502 = 1,057,064 and 244,334 + 366,502 = 610,836 [CALC]. `DEVELOPER_RULINGS_LOG.md` L1751 (`DR-109`: the robot term stays flat; *"the free tier (the character budget)"* for 34.7 % and *"the distinctive tier"* for 57.8 %); L1130 (`DR-56`: *"Q-65: ruling C stands as the developer's ruling"*). The quick reference L81–L85: file 16 applies §15 sector percentages to the distinctive tier. ST12 L967 (AQ-211): keep the tier figures PROPOSED until the developer says otherwise.
- **A-06:** `DEVELOPER_RULINGS_LOG.md` L1669 (`DR-100` (1): Hawaiian, later Tepenian, dominant everywhere); L1769 (`DR-111` (1), quoted at C-09); L1118 (`DR-56` item 5, verbatim: *"A human child would learn the dominant language of the society he/she grows up in ... if the child's parent(s) speak(s) a different language, then the child would learn both"*) and L1129. Speaker shares: `06_Result_Speaker_Shares_Mirny.md` L11 to L16, column *Best %* (header L9): English 32.8, Mandarin 16.2, Korean 13.5, Indonesian 12.1, Russian 9.4, Japanese 7.9; L18: *"Shares are not additive"*.
- **A-07:** `DEVELOPER_RULINGS_LOG.md` L1115 (`DR-56` item 2, verbatim: *"In the first generation or so of settlement, they're still learning how to deal with the wind. Once they have it figured out, they teach each other, set up signifiers with a weather report/relay system"*) and L1124 (recorded as: learned once, then taught); L1150 (`DR-57`: *"An organization of people of both bodies manages and curates the weather protocol for Mirny; the protocol is public knowledge any resident may learn"*; its *"undecided"* on the relay is superseded by `DR-76`); L1432 (`DR-76` (1) *"The weather warnings travel on the relay"*, (2) form and who runs it *"not known yet"*, (3) the signifiers *"to be researched in real-world sources"*); L1769 (`DR-111` (2) and (3): the organization a candidate role *"described by function only, with no place cataloged"*; who teaches open). ANS L14 (*"no title, office, seat or name"*), L15 (who teaches: open).

**Block appended (the first line is blank):**

```text

## Added 2026-11-08 (`DR-122`, DEC-182): live tier, language and wind-account rows

*Placed at the end of the file so no cited line moves. Each figure is quoted from the source line named in its row; read 2026-11-08.*

| Category | Value | Citation |
|---|---|---|
| `16_Per_City_Three_Tier_Run.md` §20 — Mirny's own tiers (the section that governs) | Of the 1,057,064 workforce: **Baseline** 446,228 (**42.2%**) · **Mandated** 244,334 (**23.1%**) · **Free — "the free tier (the character budget)"** 366,502 (**34.7%**); **"the distinctive tier"** (mandated + free) 610,836 (**57.8%**). These four percentages are shares of the workforce (the three tiers sum to it); the header's distinctive-tier convention (L8) is for a city's §15 sector shares. The baseline includes the robot-keyed term, robots × 15.75 ÷ 1,000 = 11,192 (`DR-97`); the robot term stays flat, no site factor (`DR-109`). §20's mandate is the developer's ruling C, which stands (`DR-56` Q-65); the Half B row (42.2% · 11.6% · 46.2%) mandated only the Arcanet 20%. The Mirny repass pieces still mark this set PROPOSED until the developer says otherwise | `16_Per_City_Three_Tier_Run.md` L2110, L2114–L2116, L2118–L2119, L2121, L2123, L2131; L276 (the Half B row, header L247); `DEVELOPER_RULINGS_LOG.md` L1751 (`DR-109`), L1130 (`DR-56` Q-65); `Corpus_Reference_Sheets/Division_of_Industry_Reliability_Quick_Reference.md` L81–L85; `Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md` L967 (AQ-211) |
| Language | Hawaiian (later Tepenian) is the dominant language (`DR-100`). **Supporting tier: English and Russian**, set by the developer as a Mirny special case, not by the 12-point rule, which by actual speakers gives English alone (`DR-111`). By actual speakers (best estimates; not additive): English 32.8% · Mandarin 16.2% · Korean 13.5% · Indonesian 12.1% · Russian 9.4% · Japanese 7.9%. A human child learns the dominant language of the society, and both languages if a parent speaks another (`DR-56` item 5) | `DEVELOPER_RULINGS_LOG.md` L1669 (`DR-100`), L1769 (`DR-111`), L1118 and L1129 (`DR-56` item 5); `Research_Logs/Mirny_Language_Speakers_2026-11-04/06_Result_Speaker_Shares_Mirny.md` L11–L16, L18 (a calculation; its own status line, L3, reads PROPOSED) |
| Wind account (rulings) | In the first generation or so the settlers had to learn the wind on their own; once they had it figured out they taught each other and set up signifiers with a weather report/relay system (`DR-56` item 2). An organization of people of both bodies manages and curates the weather protocol, which is public knowledge any resident may learn (`DR-57`); it is a candidate role described by function only, with no title, name or place (`DR-111`). The weather warnings travel on the relay (`DR-76`). Open: the warning's form and who runs it (`DR-76`); who teaches (`DR-111`); the signifiers, to be researched in real-world sources (`DR-76`) | `DEVELOPER_RULINGS_LOG.md` L1115, L1124 (`DR-56`), L1150 (`DR-57`), L1432 (`DR-76`), L1769 (`DR-111`); `Amendment_Notes_2026-11-04_Answers_Carried_Forward.md` L14, L15 |
```

After the append the sheet has 40 lines.

### A-08 · `Datasheets/Phase_5.md` · appended after L49

**Decision and finding:** DEC-182 (ST14 section 7.4, decision 3); ST14 AS14-48 coverage (the wind account: the warnings on the relay; the duty); docket DK14-48. **Kind:** new row.

**Current last line, L49** (SHA-256 `0faddef7709651725d570c2a238c7c0d3b7e63067900edd22d9180f470c64f59`):

```text
who-knows-it analysis — this phase's actual content.
```

**Sources, by row (opened 2026-11-08):**

- **A-08:** `DEVELOPER_RULINGS_LOG.md` L1432 (`DR-76` (1), (2), (5): *"'Best placed' = whoever is most strategically able to address a weather hazard ... capability and position for the hazard at hand, not nearness; applies to either body"*); L1116 and L1127 (`DR-56` item 3: *"no one is legally required to hand off a post or go out to restore the relay; people of both bodies do it from a strong community duty, and not doing so when one is best placed brings deep personal guilt"*); L1477 (`DR-80` (1): *"Guilt is not a sanction"*); ANS L26 (who goes out to restore the relay: *"Open."*, DEC-042).

**Block appended (the first line is blank):**

```text

## Added 2026-11-08 (`DR-122`, DEC-182): live wind-account row (the relay)

*Placed at the end of the file so no cited line moves. Read 2026-11-08.*

| Category | Value | Citation |
|---|---|---|
| Wind account — the relay (rulings) | The weather warnings travel on the relay, read as the relay or subnet network that carries Mirny's communication (`DR-76`); the warning's form and who runs it are not known yet. No one is legally required to go out to restore the relay; people of both bodies do it from a strong community duty, and not doing so when one is best placed brings deep personal guilt (`DR-56` item 3); guilt is not a sanction (`DR-80`). "Best placed" is whoever is most strategically able to address a weather hazard: capability and position for the hazard at hand, not nearness, either body (`DR-76`). Who goes out in practice is open (DEC-042) | `DEVELOPER_RULINGS_LOG.md` L1116, L1127 (`DR-56`), L1432 (`DR-76`), L1477 (`DR-80`); `Amendment_Notes_2026-11-04_Answers_Carried_Forward.md` L26 |
```

After the append the sheet has 57 lines.

---

## 4 · Looked at, not changed (with the reason; none is in the apply script)

| Datasheet and line | Piece and finding | Why it is not changed | If the developer wants it anyway |
|---|---|---|---|
| `Step_0.md` L29 (the "Not mechanical" note) | ST12 §1.7 (B and C tag L; no docket row) | A pre-run record, covered by the sheet's own L3 banner (*"kept as written"*); not wrong as a record | nothing proposed |
| `Step_1_and_2.md` L7 ("unusually") | ST12 AS12-50, DK12-50 | The piece's resolution is a reading note (*"read as a note about the file, never as a comparison of places"*), with no replacement text; the length figure on L8 is corrected (C-10) | the reading note stays in ST12 |
| `Step_1_and_2.md` L33 (Half B row) | ST12 AS12-49 | Settled in the piece: live and consistent; *"no row of its own for L33"* | nothing proposed |
| `Step_3.md` L10 (research log) | ST12 AS12-50, AR-204 | The missing index row belongs to the research-log README, outside the sheets; no docket row (C) | AR-204 |
| `Phase_3.md` L5 (draft note) | ST13 AS13-31 (d), low | The pointer note is spliced into a sentence L6 completes; the piece gives no replacement text, and the line is a header, not a data row. (The same splice sits in the L5 of `Step_0.md` and `Step_1_and_2.md`.) | a header fix, if wanted, in a later batch |
| `Phase_4.md` L8 (the citation gate: *"percentages are of the DISTINCTIVE tier"*) | ST14 AS14-47 (a), T | **Not wrong.** L7 to L8 attach the convention to *"a city's own SECTOR SIZES"*, and that is right: `Corpus_Reference_Sheets/Division_of_Industry_Reliability_Quick_Reference.md` L81–L85 (file 16 applies §15 percentages to the distinctive tier) and L88 (*"`16`'S CONVENTION GOVERNS"*); `16_Per_City_Three_Tier_Run.md` L2123 (the mandate's column *"Share of distinctive"*). The tier percentages are shares of the workforce; that fact goes into the added tier row (A-05), which says so | the piece's note text could be appended; not proposed (`DR-102`) |
| `Phase_4.md` L20, L21 | ST14 AS14-47 (b) | Live (refreshed 2026-11-03); L21's `16` L276 is Mirny's Half B row (opened) | nothing proposed |
| `Phase_4.md` L25 (the cold file as *"the governing mechanic"*) | ST14 AS14-47 (c); settled *"A (a record note)"* | Settled in the piece as a record note, not a correction. Phase 4 records the label as the `M-151` trap (`04_Phase_04_Ordinary_Life.md` L252, L361: *"`RP` governs; `CP` is the narrow companion, written for deep cold"*) | optional note, appended to the Category cell: *(this label is the `M-151` trap Phase 4 records: `RP` governs; the cold file is its narrow companion, written for deep cold — `04_Phase_04_Ordinary_Life.md` L252, L361)* |
| `Phase_4.md` L28–L30 ("this phase's actual content") | ST14 AS14-14, AS14-47 (d) | A pre-run record under the sheet's L3 banner; the CST hand-off row is outside the three row kinds DEC-182 asked about (tier, language, wind account) | optional row: *the everyday-life texture is handed to the CST; the record says "deferred to the CST", never "done"* (`DEVELOPER_RULINGS_LOG.md` L1742, `DR-108` (1); ANS L13) |
| `Phase_5.md` L19 (supply role; a withheld-source name in its quotation) | ST14 AS14-48 (b); settled *"— (a record note)"* | Settled in the piece as a record note | optional note: *(the institution name in this quotation is withheld-source and is not an input, `04_Phase_05_Relation_and_Geometry.md` L48)* |
| `Phase_5.md` L22–L24 (airport and port rows) | ST14 AS14-48 (d) | Live and correct (B, C) | nothing proposed |
| `Phase_5.md` L30 (the flag's quotation) | ST14 AS14-48 (f) | The flag stands as a record (the piece's words). Checked: the quoted phrase no longer occurs in either file it was found in (`grep -c "Australian-heritage"` returns 0 for `City_National_Connections.md` and for `City_Cross_Subnet_Relationships.md`, 2026-11-08) | optional note after L35: *the quoted phrase is no longer in either file (checked 2026-11-08); the flag stands as a record* |

**Also not proposed (optional rows outside DEC-182's question):** a CST hand-off row for `Phase_4.md` (above), and a row for the national power file's drafting in `Phase_5.md` (ST14 AS14-48 coverage and AR-240; the Geothermal file's L217 names it; neither file was opened here). DEC-182 asked only about tier, language and wind-account rows, and the ST14 coverage lists give `Phase_5.md` the wind account and the power file only, so `Phase_5.md` gets no tier or language row.

---

## 5 · UNPROVEN (not proposed)

1. **"23.24 % of each body"** (ST12 AS12-49's addendum; the header lines of ST12, ST13 and ST14). The live lines carrying 23.24 % are `DEVELOPER_RULINGS_LOG.md` L1660 (`DR-99`: *"The founding share to carry is **23.24 %** ... founders remain a minority"*), L1742 (`DR-108` (3), the Frame wording: *"a minority (23.24 %) of a long-run composition of 36 stocks"*) and `ANS` L18 (the same wording); none says "of each body", and neither do `Founding_Register.md`, `Official_Population_Census.md` or the spec (searched 2026-11-08). C-13 carries `DR-99`'s own words; "of each body" is left out.

**Not proven because shown wrong (not proposed):** the premise that `Phase_4.md` L8 is wrong (section 4).

---

## 6 · Found while verifying (outside the pieces; not proposed)

1. **`Step_-1.md` L15** gives the spec as *"`Cities/Specs/Mirny subnet/Mirny.md` — confirmed on disk at the current (post-reorg) path"*, which is right; ST12 AS12-50's *"own L15 gives the right path"* is confirmed. Nothing to fix. (Corrected 2026-11-08 after the second reader; this note first said the reverse.)
2. **The short path `Specs/Mirny.md`** stays cited, after this batch, in `Step_-1.md` L17 to L27, `Step_0.md` L14, L15, L24, L25 and `Step_1_and_2.md` L20 to L22, L27 to L32, L35, L37, L38 (C-02 to C-05 change only those rows' attribution). ST12 proposed no path fix for its sheets; only ST13 (`Phase_3.md`) and ST14 (`Phase_5.md` L20) did. A path sweep of the early-step sheets would be a later batch, on the developer's word.

---

## 7 · Snags (the recording law: failures, ambiguities, disagreements, dead ends)

1. **A split inside ST12:** its section 1.7 settles `Step_-1.md` L27 and `Step_0.md` L15 as untagged (B single, not carried), while AS12-47 and DK12-47 list both. They are included here (C-03, C-05): their *was* values are the figures from before `DR-68`, while the figures immediately before the live ones were the interim ones that `DR-90` replaced, so the rows read as if one change produced the live figures. The change only adds the attribution; nothing is removed.
2. **DEC-163's wording says "after the spec re-key (AR-220)".** AR-220 re-keys Phase 3's own citations (a pass-file docket, not applied). A-01 to A-04 cite live spec lines opened today, so they do not depend on it; if the developer prefers, hold A-01 to A-04 until AR-220 is applied.
3. **DEC-182's question names tier, language and wind-account rows for "the Phase 4 and Phase 5 datasheets".** The ST14 coverage lists split them: `Phase_4.md` gets tier, language and wind account; `Phase_5.md` gets the wind account (the relay). Followed the per-sheet lists, the reading that adds less.
4. **The brief for this batch mentioned tier, language and wind-account rows beside the Phase 3 piece.** ST13 proposes no such rows: AS13-31 finds the Phase 3 sheet untouched by the rulings in substance, and its decision 4 (DEC-163) asks only for the spec's physical wind, precipitation and record-extreme rows. None is added beyond those.
5. **"Workforce units".** The pieces and the robot-term piece (`Amendment_Rederivation_PRT_RobotTerm_2026-11-04.md` L8, PROPOSED) say "shares of workforce units"; file 16 prints *Workers* and *Share* (L2112). A-05 uses the source's own terms (the workforce, shares of it).
6. **The tier set's status.** File 16 heads Mirny's section *"DETERMINED"* (L2110); ST12 AQ-211 keeps the set PROPOSED until the developer says otherwise. A-05 states both.
7. **The old spec was opened from git, read only** (`git show 1a48edbc:` and `67d091af:` of the spec, to the session scratchpad), to prove the +22 shift, the ring's character span and old L132's text. No checkout, no change to the working tree.
8. **Lines opened in shared files were Mirny's only:** the census (L500, L642), the extent file (L603, L611, L631), the Register (L8 to L10, L57, L88, L94), file 16 (L247, L276, L2110 to L2178), the rulings log entries cited, `City_Relationship_Database.md` L334, `City_National_Connections.md` L268 (heading only) and a count-only search of two files. Searches for Mirny's lines in the census and extent files put some other locations' rows on screen; none is used or named. No other location's file or folder was opened.
9. **Graphify** was not used. **Tooling:** the generator, the hash list and a dry run of the apply script on copies of the seven datasheets were kept in the session scratchpad only; the dry run reproduced every proposed row and every appended block, and a second run aborted, as designed. No helper file was created in the repo.

---

## 8 · Apply script (NOT run; run only on the developer's word, after reviewing sections 2 and 3)

Python 3. It checks every target first (each row's SHA-256, each replaced text occurring exactly once, each new row's SHA-256, each sheet's line count and last line) and writes nothing unless every check passes. Run twice, it aborts on the first row (the hashes no longer match). An optional argument points it at a copy of the folder for a dry run.

```python
#!/usr/bin/env python3
# Mirny · Application Batch 2 (datasheets), 2026-11-08. NOT RUN. Apply only on the developer's word (DR-122).
import hashlib, pathlib, sys
D = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else
    "/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets")
def h(s): return hashlib.sha256(s.encode("utf-8")).hexdigest()
# (id, file, line, sha256 of the current row, the new row OR [(exact text replaced, replacement)] for rows not reproduced, sha256 of the new row)
EDITS = [
  ('C-01', 'Step_-1.md', 16, '541f8519992726840daff7277099a37bd0c78f9c7cc266e31253cb7dfe127090',
   '| Specs file length | 252 lines total (bound for any future read-spec computation) *(corrected 2026-11-08, `DR-122`: 230 lines when this sheet was written; from old L46 on, every line now sits 22 lines lower)* | Re-verified 2026-11-08 (line count of `Specs/Mirny subnet/Mirny.md`; the 230-line copy is git `1a48edbc`) |',
   '4e7f0b12cabb0843b6cf0a257f93e1c959ef2a8e980bfc0c8451f10dbf25de5e'),
  ('C-02', 'Step_-1.md', 26, '181aa072b84a418cd2f77ad87d329696257781d16af0c0d62d7409eb8213417b',
   '| Census I (repeat here, full derivation in `Step_0.md`) | 692,971 H / 710,578 R / 1,403,549 *(was 665,901 / 685,529 / 1,351,430 before the `DR-68` census change of 2026-10-28; the live figures also carry `DR-90` of 2026-11-02)* | `Specs/Mirny.md` L15 (§"Population & Composition"); cross-verified against `Official_Population_Census.md` L500 — **exact match, no discrepancy** (re-checked 2026-10-30; attribution corrected 2026-11-08, `DR-122`) |',
   '983b943a81c17230aaf1fe7861d22dcfae62e14a530a26ab2e32cc77e40f30e5'),
  ('C-03', 'Step_-1.md', 27, '800ba7650c804429cb2a591a94207bf6130382edb88c86b14cce68083a57ff32',
   '| Census II | 524,022 H / 528,352 R / 1,052,374 *(was 507,344 / 509,151 / 1,016,495 before the `DR-68` census change of 2026-10-28; the live figures also carry `DR-90` of 2026-11-02)* | `Specs/Mirny.md` L16 (§"Population & Composition"); cross-verified against `Official_Population_Census.md` L642 — **exact match** (re-checked 2026-10-30; attribution corrected 2026-11-08, `DR-122`) |',
   'e62caca3eef7050f3b94b1d2151056bf0772b3cb4aa1188ed8683d33f6b78dc8'),
  ('C-04', 'Step_0.md', 14, '47a71720a2923911f3daac46e18b1a0168c211cad5e527fd85b335e386b440e9',
   '| Census I | 692,971 H / 710,578 R / **1,403,549** (revised 2026-07-04; `DR-68` 2026-10-28, was 665,901 / 685,529 / 1,351,430; `DR-90` 2026-11-02) | `Official_Population_Census.md` L500 — cross-verified against `Specs/Mirny.md` L15, exact match (re-checked 2026-10-30; attribution corrected 2026-11-08, `DR-122`) |',
   'd0fad77d081b4550396ce1ff2d4f9022934aef6347d664f38e1731e62e4f41c6'),
  ('C-05', 'Step_0.md', 15, '5b05934ebd614add9e838469ed79b75c6dd95fa25b6f3af1a77d8cbc6f1beb44',
   '| Census II | 524,022 H / 528,352 R / **1,052,374** *(was 507,344 / 509,151 / 1,016,495 before `DR-68` 2026-10-28; `DR-90` 2026-11-02)* | `Official_Population_Census.md` L642 — cross-verified against `Specs/Mirny.md` L16, exact match (re-checked 2026-10-30; attribution corrected 2026-11-08, `DR-122`) |',
   '5a30ebd5e0e5edfc8fcb9cb7b1f844a7e72755fb10ac4bedda1d0f03b51467a5'),
  ('C-06', 'Step_0.md', 16, '4be58f4c1f65bd5952df845987e1eb6f1a09b555cf30f75773d37741b8f3080c',
   '| Retention (computed; formula = retained ÷ Census-I count) | combined 74.98% · human 75.62% · robot 74.36% · spread **1.26 pp toward humans** *(corrected 2026-11-08, `DR-122`: was 1.89, the spread of the superseded interim rows of 2026-10-28)* | Computed from the two rows above: 1,052,374÷1,403,549 = 74.98%; 524,022÷692,971 = 75.62%; 528,352÷710,578 = 74.36%; spread 75.62 − 74.36 = 1.26 (unrounded 75.6196 − 74.3552 = 1.2644) |',
   'b09fbe827eef059d5dd1622c5713400bd1cfd1de651a3b55a3ed19fe66c3cce4'),
  ('C-07', 'Step_0.md', 17, '1e6543aff573f18715af2e2ec5e7dc41678988d521927c2c8200797b4ca91a33',
   '| Extent *(2026-09-05 snapshot; the census is live — note L631)* | Mirny · Subnet Mirny · Census I (snapshot) 1,351,430 · @10,000/km² **135 km²** · @7,000/km² **193 km²** · Site: coastal ice *(a record of the 2026-09-05 table. Corrected 2026-11-08, `DR-122`: the cited line now holds the live row, Census I of 2026-11-03: 1,403,549 · @10,000/km² **140 km²** · @7,000/km² **201 km²** · Site: coastal ice)* | `Extent_and_Density_Per_City.md` L611 (table header L603; note L631, which now reads *"Census I of 2026-11-03; the census is the live source."*) |',
   '5a9596cdefe97270cab60bab9a99a234d78d5aea08da4df7beda19fd0e31925d'),
  ('C-08', 'Step_0.md', 18, 'a89f5df808a10ff726ff921ac736424c885fa809ad14e2b5c41f078515440c1a',
   "| Extent at the live Census I (computed) | 140.35 km² @10,000/km² · 200.51 km² @7,000/km² *(corrected 2026-11-08, `DR-122`: was 137.5 and 196.5, computed from the superseded interim total 1,375,348)* | Computed: 1,403,549÷10,000 = 140.35; 1,403,549÷7,000 = 200.51 (Census I from `Official_Population_Census.md` L500; the two densities are the extent table's column heads; the table's own row, `Extent_and_Density_Per_City.md` L611, prints 140 and 201) |",
   '7b8518a5e004b2b42e36a4e3ed045d5c2a8098dda4bb44caec2d9c82678dd787'),
  ('C-09', 'Step_0.md', 26, 'adef7975d1b19be41aeb718519c8ab93147f8903375cf501af8228a675c8a6a0',
   "| **Language** (set 2026-11-03) | Hawaiian (later Tepenian) is the dominant language. **Supporting tier: English and Russian** (set by the developer as a Mirny special case, `DR-111`, 2026-11-04; corrected here 2026-11-08, `DR-122`) — a language not dominant but widely enough understood that business, social talk and general dealings can be done in it; the 12-point rule's set is every language group within 12 percentage points of the city's largest group (range mid-points; nations sharing a language summed). Largest group: English 25.2–34.4. No other group is within 12 percentage points, so the 12-point rule alone gives English, as it does by actual speakers (`DR-111`). *These are shares of residents whose national origin is a nation of that language, not counts of speakers; the mapping of nations to languages is recalled general knowledge, not verified.* | `Research_Logs/Language_Sets_By_City_Reference_2026-11-03.md` (12-point addendum and rulings); `Research_Logs/Language_Blocs_By_City_2026-11-03.md`; `DEVELOPER_RULINGS_LOG.md` L1769 (`DR-111`) |",
   'a16a9bab2d56bc0da6a8b6775d85b38e6b07c493ac44836c29c70572e9f40c5e'),
  ('C-10', 'Step_1_and_2.md', 8, 'baac4bac5b6c6d4a6911f76316bf5499ae31c61395eb99301a309f035480a326',
   '> detailed (230 lines when this sheet was written; 252 lines on 2026-11-08, `DR-122`) — this table extracts only what belongs to the physical/environmental capability',
   'abeabb5c5ff871cf23ace9b24f717fcaf56ccae10dbf8de9d1dc44d452b0b30d'),
  ('C-11', 'Step_1_and_2.md', 25, '1e6543aff573f18715af2e2ec5e7dc41678988d521927c2c8200797b4ca91a33',
   '| Extent *(2026-09-05 snapshot; the census is live — note L631)* | Mirny · Subnet Mirny · Census I (snapshot) 1,351,430 · @10,000/km² **135 km²** · @7,000/km² **193 km²** · Site: coastal ice *(a record of the 2026-09-05 table. Corrected 2026-11-08, `DR-122`: the cited line now holds the live row, Census I of 2026-11-03: 1,403,549 · @10,000/km² **140 km²** · @7,000/km² **201 km²** · Site: coastal ice)* | `Extent_and_Density_Per_City.md` L611 (table header L603; note L631, which now reads *"Census I of 2026-11-03; the census is the live source."*) |',
   '5a9596cdefe97270cab60bab9a99a234d78d5aea08da4df7beda19fd0e31925d'),
  ('C-12', 'Step_1_and_2.md', 26, 'a89f5df808a10ff726ff921ac736424c885fa809ad14e2b5c41f078515440c1a',
   "| Extent at the live Census I (computed) | 140.35 km² @10,000/km² · 200.51 km² @7,000/km² *(corrected 2026-11-08, `DR-122`: was 137.5 and 196.5, computed from the superseded interim total 1,375,348)* | Computed: 1,403,549÷10,000 = 140.35; 1,403,549÷7,000 = 200.51 (Census I from `Official_Population_Census.md` L500; the two densities are the extent table's column heads; the table's own row, `Extent_and_Density_Per_City.md` L611, prints 140 and 201) |",
   '7b8518a5e004b2b42e36a4e3ed045d5c2a8098dda4bb44caec2d9c82678dd787'),
  ('C-13', 'Step_1_and_2.md', 36, 'd6476a9c7e57e3cc5752e94cc65ab9856eee2b678b8c8ebc0b59ba40e444b8c9',
   '| Founding population | Founded by Idelsk-Uralia (replacing Russia in the founding-nation role); exile groups present: Idelsk-Uralia (also), Russia, Australia and the Sinian Federation (China) (`DR-9`, `DR-46`, `DR-54`, `DR-99`). The founding share to carry is 23.24 %; founders remain a minority (`DR-99`). Spec L174 was rewritten 2026-10-13 to match `DR-46`; the old *"Primarily Russian exiles…"* no longer stands. (Refreshed 2026-10-21 against the corrected spec and the Founding Register. Corrected 2026-11-08, `DR-122`: Idelsk-Uralia is also an exile group, `DR-99`; spec L174 still lists three exile groups and lags the Register; its correction is ruled, not yet applied, `DR-108`.) | `Founding_Register.md` L57 (Mirny row), L88 (the `DR-46` entry), L94 (the 2026-10-13 spec cleanup entry) (`DR-9`); `DEVELOPER_RULINGS_LOG.md` L1660 (`DR-99`), L1742 (`DR-108` item 4) |',
   'ffcfcbe119915a8e8cbc318782f6732eeab16dafc87b89f2d32c09c38415424c'),
  ('C-14', 'Phase_3.md', 15, '6abe535bb981835c6841228e5ab8ca812d57e06d8c185ba319dcdeb57619f240',
   '| Coastal terrain, stated directly | *"The coast here is rocky and exposed. Katabatic winds off the East Antarctic ice sheet funnel toward the coast with significant force"* | `Specs/Mirny subnet/Mirny.md` L79 |',
   '8b6d23a57625bf7b5b53031bf7998a47e95127294eceb70bfb49e667e8e3ce03'),
  ('C-15', 'Phase_3.md', 16, 'ca6ab260fa8ce39d8af22ca5204364b0ebad323c5a509a691150e21d43b26605',
   "| Architecture | ⛔ **Not an input** — the whole line is EXCLUDED by the Step −1 contract (culture section); its airlock-entry detail is open as Q-2. The wind-shedding ring survives in the admitted economy text, L196 chars 272–623 (the contract's old L174; anchor corrected 2026-11-08, `DR-122`) | `Specs/Mirny subnet/Mirny.md` L184, L196; `00.1_Step_MINUS-1_Input_Contract.md` §B L162 |",
   '49a647a352fa8f36804f273053d9242757af56c3ffa936fb2b7fb3ddf6f97182'),
  ('C-16', 'Phase_3.md', 17, '7fd39f8e366f76b4e4dca5a6bee8a428c6e25fa53c89189a54e727aa61c2d7fc',
   '| Building layout | ⛔ **Not an input at any step of the ULM** — developer-vision paragraph, post-ULM (`DR-10`) | `Specs/Mirny subnet/Mirny.md` L190 |',
   'bbb6f859ac6dc55d95e155b26f014f399697bdb7de4de15efb10af80e0905bcf'),
  ('C-17', 'Phase_3.md', 18, '7e57aab16af771e20a064485611e2bf3acecda167499cfda0c353abaffe431d8',
   '| Entertainment/amenity texture | ⛔ **Not an input at any step of the ULM** — same developer-vision paragraph (`DR-10`) | `Specs/Mirny subnet/Mirny.md` L190 |',
   '2091d948dc88b0b14497d8ad64f815a8dc292d2ddc19f8c5f66e93dc7ba4ae4c'),
  ('C-18', 'Phase_3.md', 19, '2a3f0e42d05c7b13444b07d2eace405c13116d6de10b63a19d77fca4144a621c',
   '| The solstice light | ⚠ L154\'s (the contract\'s old L132) "solstice grazing events" is residue of the retracted symmetric light model (ADMITTED-DEMOTED at Step −1, → R-2). The corrected data: **no polar night** — on the winter solstice the sun clears the horizon, low and briefly; **~29 days of midnight sun**, Dec 8 → Jan 5 | `Specs/Mirny subnet/Mirny.md` L77, L107–108 (corrected 2026-09-04); L154 (old L132) demoted *(anchor and quoted phrase corrected 2026-11-08, `DR-122`)* |',
   '189e02f90ffc0e8c3a45804b12a9629d28fdc65a1532fd7fd37e4e289e9c152a'),
  ('C-19', 'Phase_3.md', 20, '9a6700c5bae3df3544b3c571b436e1bcdd60e732e1b00c97840afed9ead38d99',
   '| Blizzard/visibility conditions, stated directly | *"Blizzards: with katabatic winds and available surface snow, blizzard conditions can develop rapidly; visibility collapses quickly in major events"* · *"Whiteout here routinely occurs under a clear sky, because the snow is lifted, not falling"* | `Specs/Mirny subnet/Mirny.md` L156, L104 (cross-ref `Phase_1.md`) |',
   '050a94b37fd14a96476e4db9499126c7a434093e18fbadb7acb8aac6a5ccfb51'),
  ('C-20', 'Phase_3.md', 21, 'b6e0df3b134e56812e9c0c6341e26f8d2c23e9ebfaae6461a56c40c84b3e4c4e',
   [('| `Specs/Mirny.md` L155 |',
     '| `Specs/Mirny subnet/Mirny.md` L155 |')],
   '5407242b0d73a1ffe90d9ef78a63bf6274ebb54d19910fe32d0a4cc5f8ac009d'),
  ('C-21', 'Phase_5.md', 17, 'e8318e454ad3df752d463b085f4b0244750411e750274102d3c37e8f10035de9',
   '| `City_Relationship_Database.md` — Mirny\'s own header | Region: East Antarctic coast · Arcanet subnet: Mirny ("Australian": common people call it "the Australian subnet" because Australia is its leading founder, an in-world basis, `DR-47`, partly superseding `DR-13`\'s "geographic nickname only"; corrected 2026-11-08, `DR-122`) — **hub city**. The source\'s national label for the city rests on the station and is not carried (`DR-19`) | `City_Relationship_Database.md` L334–341 (entry heading L334); `DEVELOPER_RULINGS_LOG.md` L975 (`DR-47`); `04_Phase_05_Relation_and_Geometry.md` L107 item 4 |',
   'd72058892afd88836dd3816eade88349d8f33c0eb94645c1d635c8e4c17b6908'),
  ('C-22', 'Phase_5.md', 20, 'a20f5952255c2fec9abf020cf13096efb5e4fb90e876b426111d35fa5aab4703',
   [('| `Specs/Mirny.md` L206 |',
     '| `Specs/Mirny subnet/Mirny.md` L206 |')],
   '2f0229b9f2573f07457d0058287e831cf7de10d7be253a985aff5828b05d5c9e'),
  ('C-23', 'Phase_5.md', 25, 'ab8ed0ca77b8744f55f256a231b8a2ac4f708ffc1fcdb3e54714f0cac5dbadcf',
   [('names two of the three founding stocks',
     'names two of the four founding stocks'),
    ('with exile groups from Russia, China and Australia (`DR-9`, `DR-46`, `DR-54`)',
     'with exile groups Idelsk-Uralia (also), Russia, Australia and the Sinian Federation (China) (`DR-9`, `DR-46`, `DR-54`, `DR-99`; `Founding_Register.md` L57)'),
    ('*(refreshed 2026-10-21)*',
     '*(refreshed 2026-10-21; corrected 2026-11-08, `DR-99`, `DR-122`)*')],
   'f1323ceaf016479ef02b88e03d8837d8994c007807cb3ceb6c402b925869c7a0'),
  ('C-24', 'Phase_5.md', 44, '42b4d13e329333bbfb4b8195c605da852365000f5fd31545b8f8d56931d480b9',
   '> the founders shared by geography and access (`DR-9` as amended by `DR-46` and `DR-99`, `Founding_Register.md` L57, corrected 2026-11-08; `DR-19`), never on "heritage"; the tie is re-grounded,',
   '612049cc8d8042edd14ac89c3133f45780f44cc18db4bddc0939a8d6e4170253'),
]
# (file, current line count, sha256 of the current last line, lines appended)
ADDS = [
  ('Phase_3.md', 29, '34ca317d2a54915423e94f9d2a7df6b12a432037ea0e0ba313a1a56c667f51d0', [
    '',
    "## Added 2026-11-08 (`DR-122`, DEC-163): the live spec's wind, precipitation and record-extreme rows Phase 3 rests on",
    '',
    '*Placed at the end of the file so no cited line moves. Quoted from the live 252-line spec; each line opened 2026-11-08.*',
    '',
    '| Category | Value | Citation |',
    '|---|---|---|',
    '| Prevailing winds, stated directly | *"katabatic from the south and southeast (off the East Antarctic plateau)"* · *"average wind speeds 10–14 m/s; sustained storms exceeding 40 m/s (144 km/h) have been recorded; wind is the dominant environmental feature of this city"* *(the clause ranking the station among others is not carried)* | `Specs/Mirny subnet/Mirny.md` L93 |',
    '| Wind against cold, stated directly | *"WIND, decisively — the cold is NOT what defines this city."* · *"At -11.2 °C the cold is a backdrop."* · *"… mean wind 12.0 m/s: up to a third of snowfall evaporates before it lands, and most of the remainder is entrained and carried past."* *(the comparing words before "mean wind" are not carried; the clear-sky whiteout sentence is already quoted at L20)* | `Specs/Mirny subnet/Mirny.md` L104 |',
    '| Precipitation and retention | Annual precipitation **527.1 mm** water equivalent (measured monthly normals) · Regime: KATABATIC MARGIN, *"snow flux, not snowfall"* · Falls (reaches the surface) ~527 mm/yr · Lands (accumulates and stays) **~200 mm/yr** (~38% retention) · Lost to sublimation and wind transport ~327 mm/yr · *"Retention ~38% — residents dig out from what arrived from upwind, not from what fell on them."* | `Specs/Mirny subnet/Mirny.md` L94, L98–L101, L104 |',
    '| Record extremes | Record high **+8.7 °C** (Dec) · record low **-36.5 °C** (Aug) — NOAA NCEI GHCN-Daily station `AYM00089592`, direct, 0 km; daily observations 1973-2026 *(researched 2026-09-04)* | `Specs/Mirny subnet/Mirny.md` L92 |',
  ]),
  ('Phase_4.md', 30, '2d28fbd87b009456e1f961c120f7ffb845ab417ec7066d8658fb2d157c0c4396', [
    '',
    '## Added 2026-11-08 (`DR-122`, DEC-182): live tier, language and wind-account rows',
    '',
    '*Placed at the end of the file so no cited line moves. Each figure is quoted from the source line named in its row; read 2026-11-08.*',
    '',
    '| Category | Value | Citation |',
    '|---|---|---|',
    '| `16_Per_City_Three_Tier_Run.md` §20 — Mirny\'s own tiers (the section that governs) | Of the 1,057,064 workforce: **Baseline** 446,228 (**42.2%**) · **Mandated** 244,334 (**23.1%**) · **Free — "the free tier (the character budget)"** 366,502 (**34.7%**); **"the distinctive tier"** (mandated + free) 610,836 (**57.8%**). These four percentages are shares of the workforce (the three tiers sum to it); the header\'s distinctive-tier convention (L8) is for a city\'s §15 sector shares. The baseline includes the robot-keyed term, robots × 15.75 ÷ 1,000 = 11,192 (`DR-97`); the robot term stays flat, no site factor (`DR-109`). §20\'s mandate is the developer\'s ruling C, which stands (`DR-56` Q-65); the Half B row (42.2% · 11.6% · 46.2%) mandated only the Arcanet 20%. The Mirny repass pieces still mark this set PROPOSED until the developer says otherwise | `16_Per_City_Three_Tier_Run.md` L2110, L2114–L2116, L2118–L2119, L2121, L2123, L2131; L276 (the Half B row, header L247); `DEVELOPER_RULINGS_LOG.md` L1751 (`DR-109`), L1130 (`DR-56` Q-65); `Corpus_Reference_Sheets/Division_of_Industry_Reliability_Quick_Reference.md` L81–L85; `Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md` L967 (AQ-211) |',
    '| Language | Hawaiian (later Tepenian) is the dominant language (`DR-100`). **Supporting tier: English and Russian**, set by the developer as a Mirny special case, not by the 12-point rule, which by actual speakers gives English alone (`DR-111`). By actual speakers (best estimates; not additive): English 32.8% · Mandarin 16.2% · Korean 13.5% · Indonesian 12.1% · Russian 9.4% · Japanese 7.9%. A human child learns the dominant language of the society, and both languages if a parent speaks another (`DR-56` item 5) | `DEVELOPER_RULINGS_LOG.md` L1669 (`DR-100`), L1769 (`DR-111`), L1118 and L1129 (`DR-56` item 5); `Research_Logs/Mirny_Language_Speakers_2026-11-04/06_Result_Speaker_Shares_Mirny.md` L11–L16, L18 (a calculation; its own status line, L3, reads PROPOSED) |',
    "| Wind account (rulings) | In the first generation or so the settlers had to learn the wind on their own; once they had it figured out they taught each other and set up signifiers with a weather report/relay system (`DR-56` item 2). An organization of people of both bodies manages and curates the weather protocol, which is public knowledge any resident may learn (`DR-57`); it is a candidate role described by function only, with no title, name or place (`DR-111`). The weather warnings travel on the relay (`DR-76`). Open: the warning's form and who runs it (`DR-76`); who teaches (`DR-111`); the signifiers, to be researched in real-world sources (`DR-76`) | `DEVELOPER_RULINGS_LOG.md` L1115, L1124 (`DR-56`), L1150 (`DR-57`), L1432 (`DR-76`), L1769 (`DR-111`); `Amendment_Notes_2026-11-04_Answers_Carried_Forward.md` L14, L15 |",
  ]),
  ('Phase_5.md', 49, '0faddef7709651725d570c2a238c7c0d3b7e63067900edd22d9180f470c64f59', [
    '',
    '## Added 2026-11-08 (`DR-122`, DEC-182): live wind-account row (the relay)',
    '',
    '*Placed at the end of the file so no cited line moves. Read 2026-11-08.*',
    '',
    '| Category | Value | Citation |',
    '|---|---|---|',
    '| Wind account — the relay (rulings) | The weather warnings travel on the relay, read as the relay or subnet network that carries Mirny\'s communication (`DR-76`); the warning\'s form and who runs it are not known yet. No one is legally required to go out to restore the relay; people of both bodies do it from a strong community duty, and not doing so when one is best placed brings deep personal guilt (`DR-56` item 3); guilt is not a sanction (`DR-80`). "Best placed" is whoever is most strategically able to address a weather hazard: capability and position for the hazard at hand, not nearness, either body (`DR-76`). Who goes out in practice is open (DEC-042) | `DEVELOPER_RULINGS_LOG.md` L1116, L1127 (`DR-56`), L1432 (`DR-76`), L1477 (`DR-80`); `Amendment_Notes_2026-11-04_Answers_Carried_Forward.md` L26 |',
  ]),
]
text = {}
def get(f):
    if f not in text: text[f] = (D / f).read_text(encoding="utf-8").split("\n")
    return text[f]
for cid, f, n, old_h, new, new_h in EDITS:
    ls = get(f); row = ls[n - 1]
    if h(row) != old_h: sys.exit(f"ABORT {cid}: {f} L{n} differs from the recorded row; nothing written")
    if isinstance(new, str): row = new
    else:
        for old, rep in new:
            if row.count(old) != 1: sys.exit(f"ABORT {cid}: text to replace not found exactly once; nothing written")
            row = row.replace(old, rep)
    if h(row) != new_h: sys.exit(f"ABORT {cid}: new row differs from the recorded one; nothing written")
    ls[n - 1] = row
for f, nlines, last_h, block in ADDS:
    ls = get(f)
    if len(ls) != nlines + 1 or ls[-1] != "" or h(ls[-2]) != last_h:
        sys.exit(f"ABORT: {f} does not end as recorded; nothing written")
    ls[-1:] = block + [""]
for f, ls in text.items():
    (D / f).write_text("\n".join(ls), encoding="utf-8")
print(f"Applied {len(EDITS)} row changes and {sum(len(b) for *_, b in ADDS)} appended lines in {len(text)} files.")
```

