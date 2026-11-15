# Amendment re-derivation OWN — Mirny's own lines: the road, the subnet's member list and the coastal supply line (Mirny review, 2026-11-11)

**What this re-derives.** Items **F-10** (a subnet member's road access withheld), **F-11** (the hub's member count not proposed) and **F-12** (the coastal supply line's grounding), as `Amendment_Notes_2026-11-11_Review.md` states them in section F (L96–L98) and assigns them in section H (L154–L156; piece `OWN`, L171). The one change under all three is A6, `DR-131` item 3 (`DEVELOPER_RULINGS_LOG.md` L1949).
**How it was made.** Three readers (A, B, C) re-derived the piece independently. Round 2 confirmed each reader's proof of reading (UNANIMOUS), and in Round 3 each reader found the other two CONSISTENT. This file is the single merge (`M-246`). Where no reader contradicts another, it takes the union, crediting each finding to its finder. Where they contradict, it takes the most conservative post-Round-3 view and names the split in the row. The round record is `Amendment_Rederivation_OWN_2026-11-11b_T8_Rounds.md`.
**Status.** Everything here is PROPOSED. Pass files are not edited (`DR-101`). Nothing is applied, and nothing is declared complete.
**Names.** In this file's own prose, the member that the highway file's spur section concerns is "the spur member", and Mirny's two Hwy 110 neighbors are "the west road neighbor" and "the east road neighbor". Other places' names appear only inside exact quotations, as relation and never as a measure.
**Abbreviations.** `P5` = `04_Phase_05_Relation_and_Geometry.md` · `ST14` = `Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md` · `ST8b` = `Amendment_Rederivation_ST8b_FreshPanel_2026-11-08.md` · `AB3` = `Application_Batch_3_CultureFile_and_Spec_2026-11-08.md` · `CRD` = `Cities/City_Relationship_Database.md` · `HWY` = `Infrastructure/Highways.md` · `LC` = `Local_Cultures/Mirny_Subnet/Mirny.md` · `DRL` = `DEVELOPER_RULINGS_LOG.md` · `RN` = `Amendment_Notes_2026-11-11_Review.md`.

---

## 2 · What no longer stands

### 2.0 · The change, and the one error under all three items

**The change (A6).** `DRL` L1949, `DR-131` item 3, reads: "**(3) A city's own lines, for every city (`DR-122` item 5):** its own files and entries, plus lines about shared things it is named in (its port, airport, road, cluster), excluding any clause grounded only in another city's lines."
- It is recorded for every city. The item says so, and the heading reads "A CITY'S OWN LINES DEFINED (ALL CITIES)" (L1944). The developer's selection is *"Own files + shared things it's in (Recommended)"* (L1948), with no list attached. (A, B, C)
- Mirny's re-runs did not apply it (`RN` L27: "No (the re-runs used `DR-122` item 5's shorter wording)"). (A, B, C)
- It does not replace `DR-122` item 5 (L1868: "**(5)** A single location's run takes a relation only from its own lines."). It defines that item's term. (B, C)

**What it defines.** The test has three parts (A), which fall into two halves that do different work (C):
- **Inclusion half:** (a) the city's own files and entries; (b) lines about shared things the city is named in.
- **Exclusion half:** (c) minus any clause grounded only in another city's lines.
- Neither half asks whether a line *names* another place. (A, B, C)

**The common error.** All three items read "its own lines" as "lines that name no other place". (A, B, C)
- That reading is the first half of decision 4's recommended wording: "***Keep lines that name other locations out of a single location's run; take a relation only from the location's own lines, and re-key the lists to them.***" (`ST14` L842). The same line records "The brief's rule kept them all out". (A, B, C)
- The ruling log recorded only the second half (`DRL` L1868, item 5). `DR-131` item 3, the later ruling recorded for every city, cites `DR-122` item 5 by number and defines its term. (A, B, C)
- Decision 4 names the very lines this piece turns on: "one member's road access to Mirny's road (`HWY` L272 to L283), the subnet's member list (`CRD` L49)" (`ST14` L842). (B; A in its F-11 section)
- **That `DEC-183` answers decision 4 is an inference. No reader read the decisions file.** The evidence:
  - the order of the answers at `DRL` L1867 (A, B, C);
  - `DR-122` item (6), "Band 5 keeps four common items" (L1868), matches `DEC-181`'s *"Keep four (Recommended)"* (L1867) and decision 2 (`ST14` L840) (C, confirmed by A and B in Round 3);
  - item (3), "Datasheet figures and live rows are corrected in place" (L1868), matches decision 3 (`ST14` L841) (B, Round 3).
- **Split, written narrow.** In Round 1, B wrote that the developer's "Yes (Recommended)" "accepted both halves". In Round 3, A found no passage for that, and C asked the merge to mark it as inference. **Written:** what `DEC-183`'s "Yes" accepted is not read. If it answered decision 4, it may have covered the whole recommended wording, but the log records only the second half.
- **Consequence.** Every Mirny line whose stated ground is "names other places" or "names other locations" loses that ground. What each line becomes is decided by the three parts. (A, B, C)

### 2.1 · F-10 · the spur member's road access — NARROWS (A, B and C agree with the item reader)

**Pass lines that narrow:**
- **`ST14` L607:** "**its lines name other locations, so it is not used here**". The ground falls, because naming is not the test. "Hwy 110 through Mirny is unchanged either way (`HWY` L199)" stands. (A, B, C)
- **`ST14` L609** (the PROPOSED addendum): "it names other locations and is not used here (AR-242)". This narrows the same way. (A, B, C)
  - "The null reads: present in the read set" holds.
  - "withheld by the one-location rule" holds only for the spur member's own access, and only on the new ground.
  - "Hwy 110 through Mirny is unchanged." holds.
- **`ST14` L335:** "A spur section for another location was inserted on 2026-10-21 (`HWY` L272 to L283, *not used (other location)*)". This is the same blanket mark on the survey line, and it narrows the same way. Neither the item nor its reader cited it. (A, B, C)
- **`ST14` L608:** "*Not carried:* B's Round 1 addenda that closed L207's sub-row and the null at L463 on `HWY` L278." Its ground (the names test) narrows. No reader of this piece read the addenda. (A, B, C)
- **`ST14` L825 (AR-242):** "*Instead:* not used (AS14-36)." A ruling recorded for every city now answers this in part. (A, B, C)
- **`ST14` L842 (decision 4):** its recommended first half does not match the recorded ruling (2.0). (A, B, C)
- **`P5` L463:** "| Relung Panen's road access | **Absent from the read set** | — |" (`ST14` L609 had already re-classed it). The null holds two objects, and under L1949 it splits (OWN-1). (A, B, C)
  - As worded, the null states another city's fact. Mirny's null is the Mirny-side relation. (B)
- **`P5` L207:** "Relung Panen's road access is not in the admitted set." The fallback-roads sub-row carries the same null and takes the same narrowing. (C, low)
  - No reader read this line at source. The merge opened it only to settle its words.
- **`ST8b` L426:** "the road between the members and Mirny (withheld by the one-location rule, `ST14` L607)". This narrows on two counts. (A, B, C)
  - (i) The ground falls, as above.
  - (ii) The clause was wider than its ground even under the old rule. `ST14` L607 withheld only "one subnet member's only overland link".
    - Mirny's own entry gives Hwy 110 to two members as direct neighbors: "**Direct highway neighbors:** Davis (west), Casey (east)" (`CRD` L340). Both are members by Mirny's own culture file (`LC` L235). (A, B, C)
    - `HWY` L199 with L201 places a third member on Hwy 110, at its northwest endpoint. (B, C)
    - These lines were admitted all along (`ST14` L335: "Hwy 110's route and Mirny's mainline place unchanged (`HWY` L199, L63)"). (B)
- **`ST8b` L643:** "**Lines cut from the seats' list because they name other places** thin the Neighbor's standpoint". The reason for the cut falls, and the cut set re-sorts under L1949 (B, C). "The Neighbor is cast through Mirny's own lines only (R14), and it says so." stands, with "own lines" read per L1949. (A, B, C)

**The highway section, clause by clause (`HWY` L272 to L281):**
- **Member-side clauses.** These stay out. (A, B, C)
  - L272 is the heading, L274 the route ("Relung Panen → Casey (joining Hwy 110 at Casey)"), L276 the endpoints, and L280 reads "Exact length, surface and maintenance arrangement are TBD.".
  - Four clauses of L278 are member-side too: "A dedicated spur is the city's **only overland link**."; "It reaches east from Relung Panen to Casey and joins Hwy 110 there."; "Relung Panen is a spur off it, not a stop on it."; "The city has no port of its own as built (`Ports.md`)."
  - **Their ground: a split in Round 1, converged in Round 3.**
    - Round 1: A kept them out on both (b) and (c). B kept them out on the inclusion half and on the exclusion ground (B's OWN-D102). C held that only the inclusion half is shown: L278 carries its own ruling tag, and L281 says the spec field "quotes the ruling", so "grounded *only* in another city's lines" is not shown.
    - Round 3: all three now write C's ground, refined by B's point (B's OWN-Q101) that the same paragraph also restates L199 in an editor's words, so the tag does not by itself show that every clause under it is the ruling's own.
    - **Written:** they stay out because they fail the inclusion half. They are about the spur, a road Mirny is not named in. Whether the exclusion half also applies turns on the same ruling check as OWN-QD-1. The outcome is the same for all three readers.
- **"Hwy 110 itself runs Zhongshan → Davis → Mirny → Casey → Concordia"** repeats L199, which was already admitted as Mirny's road line. It stands. (A)
- **"The Denman Glacier crossing is not built; there is no western link to Mirny."** This clause names Mirny and is about what reaches Mirny by road, so it passes (b). (A, B, C)
  - Its ground: L278 opens with "`[CGRM 2026-09-01 · Path 6 · developer ruling]`", and L281 reads "Source: the `Highway access:` field of `Specs/Mirny subnet/Relung_Panen.md`, which quotes the ruling."
  - Two tests decide it: the exclusion half of L1949, and brief §3 / standing line 25 (only a ruling recorded for every city, or one naming Mirny, moves a Mirny conclusion). (C, A)
  - No reader has read the ruling's own record. This is OWN-QD-1.
- **Caution, kept by all three from the F-10 item reader.** The clause is read with its subject, the spur member. It says the spur member has no road westward to Mirny. It does not say that Mirny has no road to its west, which `HWY` L199 and `CRD` L340 contradict.

### 2.2 · F-11 · the hub's member count — FLIPS, conditional on OWN-QD-3 (A, B and C agree with the item reader; B makes the condition explicit)

**`AB3` L620, clause by clause** (B's breakdown; A and C concur):
- **"DEC-021 permits the members row"** stands. `DR-112` item 1 excepts "the high-confidence factual rows" (`DRL` L1778).
- **"but its only source is the relationship database's subnet member list, a line that names other places."** This stands as fact and falls as a bar.
  - `CRD` L49 is the row of a shared thing, the subnet. Its Subnet and Hub cells both read Mirny, and Mirny is listed first among the members. (A, B, C)
  - The row sits in the database's subnet table (section 2, L40), not in any city's entry. (A)
  - The count is grounded in the row itself. Only the row's two parentheses could reach (c), and the count needs neither of them. (A, B)
- **"No Mirny line states the count without naming them (`SPEC` L5 says only "subnet hub")."** This falls as a reason, because "without naming them" has no ground in `DR-131` item 3. As a statement it is also narrower than written.
  - It holds of the Mirny canon sources read (`CRD` L334 to L341, and the spec as the batch reports it). The culture file names its members together with its own stale count ("the other five Mirny subnet cities", `LC` L235).
  - It does not hold of Mirny's pass and amendment lines, which state the count without names: `P5` L308 "**The eight other members**, via the relay"; `ST8b` L637 "a single relay path for nine members' contact"; `ST8b` L426 "(five against nine)". (A, B, C)
  - A pass line cannot ground a canon correction, so this does not change the outcome under the old rule. (C, A)
  - So on 2026-11-08 the pass carried a count whose only source it held inadmissible that same day. The flip removes that inconsistency. (B)
  - **Split, written narrow.** C wrote that the sentence is "true only of Mirny's canon lines outside the culture file". In Round 3, A and B both found that muddled, because the culture file names its members. **Written:** the narrower statement above.
- **"By DEC-183 a single location takes a relation only from its own lines."** stands, with the term read per L1949. (A, B, C)
- **"So the count is not proposed, and `LC` L235's and L279's member text stays as it is."** flips under OWN-QD-3 (a) and holds under (b). (A, B, C)
- **"The single point of failure (D-6's other half) needs no change."** stands. (A, B, C)

**Lines carried with it:**
- **`AB3` L613,** "**Not used (other location).**", as it heads L616 ("S5 L452 [span]: the hub routes eight other members, not five; keep the single point of failure"). The mark falls for the member count, and L616's count matches `CRD` L49. (A, B, C)
- **`AB3` L617,** "DEC L376 [span]: a single location's run takes a relation only from that location's own lines". This stands, reread per L1949. (A, B, C; C docketed it)
- **`ST14` L842** lists "the subnet's member list (`CRD` L49)" among the lines decision 4 recommended keeping out. The later every-city definition takes it in, subject to OWN-QD-3. (A, B)
- **`ST8b` L426:** "The culture file's count of members routed through the hub (five against nine) is already docketed (D-6, `AS5` L452), with nothing to add." It has two slips.
  - **(i) A count slip, independent of the ruling.** "Five" counts the *other* members ("the other five", `LC` L235), while "nine" counts all members with Mirny (`CRD` L49; `ST8b` L637). [CALC] Like for like it is 5 against 9 − 1 = 8 other members, or 5 + 1 = 6 against 9 in all. `AB3` L616 has it right. (A, B, C)
  - **(ii) "already docketed … with nothing to add"** now reads "docketed, set aside, and proposable again". `AB3` L620 set D-6 aside on 2026-11-08 under `DEC-183`, and `DR-131` item 3 makes it proposable again. (C; adopted by A and B in Round 3)

### 2.3 · F-12 · the coastal supply line — NARROWS (A, B and C agree with the item reader, with one correction)

- **`P5` L321:** "**Supply:** all three receive Australian freighter shipments on one coastal supply line — Casey *"(raw materials, staged via Hobart)"* (`CRD` L159), Davis *"as part of the Mirny/Mawson subnet coastal supply line"* (`CRD` L182), Mirny (`CRD` L330)." **The "all three" half falls.**
  - The two receiving clauses rest only on the two neighbors' own entries, and the exclusion half removes them. `ST14` L340 had already marked those addresses "*not used (other location)*", but the conclusion was never narrowed to match. What falls is the count "three" and the identity of the other receivers. (A, B, C)
  - No line Mirny may use puts either neighbor back as a receiver. `DR-133` item 1 (`DRL` L1967), a ruling that names Mirny, lists Australia's four receiving nodes: Mirny is one, and neither road neighbor is among them. This does not show that the neighbors receive nothing. It shows that no line read places them as receivers. (B; A and C concur in Round 3)
- **`P5` L321, the sibling clause:** "Davis is, by developer ruling, Tepenia's principal Indian-Ocean-sector import port and receives through neutral transshipment (`PRT` L536, L130)". This falls. (A, B, C)
  - Its anchor L536 is among the ports file's "other locations' rows: *not used (other location)*" (`ST14` L337). (A, B)
  - L130 is not among Mirny's own Ports lines listed there. (A)
  - The ruling it cites concerns another city's port and does not carry (standing line 25). (A)
  - Delete that city's name and no claim about Mirny survives. The clause serves only as a contrast, which makes it a measure. (B, C)
  - "**Mirny's own relation is the direct one** (`PRT` L129)" stands without the contrast. (A, B, C)
- **`P5` L322, ground (2):** "(2) **supply**, three receiving points on one coastal supply line [IND, lookup file];". "Three" falls, and ground (2) no longer places the two neighbors on the line. Its disposition is OWN-QD-5. (A, B, C)
- **`P5` L309, the gap cell:** "a road direction, a supply line, a relay, a shared stock (P5-28)". "a supply line" falls as a tie with the west road neighbor, and `P5` L310's "as above (P5-28)" inherits the change (C). This line lay outside the item reader's span. (A, C; B adopted it in Round 3)
- **`P5` L309 and L310, the view cells:** "not stated / `CRD` L181 names Mirny only as *"Mirny (east)"*" and "not stated / `CRD` L158 names Mirny only as *"Mirny (west via Hwy 110)"*". (A, C; B adopted it in Round 3)
  - Each "only" is a claim about the whole of another city's entry, grounded only there. Each cell reads a neighbor's view of Mirny from that neighbor's own entry.
  - "Not stated" stands without them. The directions themselves stand on `CRD` L340 and `HWY` L199.
  - Confidence is low. The row read is a line about the shared road that names Mirny, so (b) arguably reaches it. Reading it as the neighbor's *view* rests on that entry alone. (A)
- **`P5` L328:** "the nation whose freighters supply the Mirny/Mawson coastal cities (`TWR` L993–994; `CRD` L330)". The plural does not stand on its `CRD` half, now L341, which names one receiving point and no other city. (A, B, C)
  - No reader read the `TWR` half. It should be checked; it is admissible for what it says of Mirny if it names Mirny. (B; A and C agree in Round 3)
- **Unchanged:**
  - `P5` L312, "raw materials **in** (`CRD` L330, hedged)", whose anchor is now L341. (A, B)
  - The quiet friction at L321: "Mirny's port primacy is **inferred from its switchboard** … not stated from its sea". (A, B, C)
  - The anchors `CRD` L329 and L330 at `P5` L321 and L312 now read L340 and L341 (`ST14` L340: "Mirny's entry moved 11 lines (old L323 to L330 → L334 to L341)"). (A)
- **`ST14` L340,** "the admitted L157 to L159, L180 to L182 and L323 to L331 now carry other locations' entries (*not used (other location)*)".
  - **Split.** A: the mark stands, now on (c). B: it stands on (c), and a shared line's name inside another city's entry admits nothing. C: it narrows to the clause test, not wholesale. C's Round 3 merge wording adds that road-direction lines in those entries naming Mirny "are admissible under (b) but add nothing beyond `CRD` L340 and `HWY` L199". In Round 3, A kept its view (C's wording "risks inviting reads of other cities' entries"), and B moved to C ("more precise … The outcome is the same").
  - **Written: the reading that claims least.** The mark stands for the receiving clauses Phase 5 took from those entries, now on the exclusion half and not on naming. Whether any other clause in those entries could be admitted is not tested here, because the entries were read by no reader, by design. Nothing here admits one.
- **`ST14` L337,** the ports file's "other locations' rows: *not used (other location)*". The mark rests on the names test. It should be re-tested under `DR-131` item 3, since a ports row about a shared thing that names Mirny is admissible. No reader read the ports file. (B; A and C concur in Round 3)

**Correction to the F-12 item reader** (A, C; B conceded in Round 3):
- The item reader paraphrased the surviving role as one that "ties it to the subnet's line" (`.review_F-12_reader.md` L61: "Mirny's surviving supply role ties it to the subnet's line").
- Mirny's own entry names the line "the Mirny/Mawson subnet coastal supply line" (`CRD` L341). The subnet table lists those two hub names as two separate subnets (`CRD` L48, L49; L42: "Six subnets, each named after its hub city.").
- So Mirny's lines do not say the line is Mirny's subnet's line alone. Which places and which subnet or subnets it serves is an open slot (OWN-QD-6).
- B's Round 1 repeated the paraphrase ("a line named for a subnet"). B withdrew it in Round 3, together with the second order and the ground-(2) re-grounding that leaned on it.

### 2.4 · Corrections to the item readers (merged)

- **F-10 reader, L102:** "My list does not show whether any other member's road line exists." On this piece's list it does: `CRD` L340, `HWY` L199, and `LC` L228 and L235 (A, B). ST8b L426's plural is therefore wrong in substance, not only in wording (A). The item reader also did not note the "five against nine" slip on the same line (B).
- **F-10 reader, L82:** it kept the member-side clauses out as "not a line Mirny is named in, and grounded in another city's lines". Only the first ground is shown (C; converged in Round 3, see 2.1).
- **F-10 reader, IQ-1001:** kept and sharpened (OWN-QD-1). **IQ-1002:** kept as a question (OWN-QD-2, where the split is named).
- **F-11 reader:**
  - It did not see `P5` L308, `ST8b` L426 or L637, where Mirny's folder already uses the count, or `ST14` L842, which names `CRD` L49. These strengthen its verdict and do not change it. (A, B, C)
  - Its L80, "It is true of Mirny's own files and entry", holds for Mirny's sources but not for its pass lines. (B, C)
- **F-12 reader:**
  - It paraphrased the line's two-part name (above).
  - Its span missed `P5` L309 (A, C).
  - It treated `DR-133` item 1 as neutral, but the ruling names Mirny as a receiving node (B).
  - All three readers now recommend against its IQ-1202 recommendation to hold ground (2) (OWN-QD-5).
- **All three item readers read the review note at 135 lines.** It now has 176.
  - Their citations still match: A6 at L27, F-10 to F-12 at L96 to L98, section E's last line at L75. (A, B, C)
  - Section G was already present at 135 lines: its last line, L135, "No ruling of these two days names them.", is the item readers' recorded last line. Only section H (L137 to L176) was added after. (A, C; B's "G and H" was corrected in Round 3)

---

## 3 · The re-derived findings (PROPOSED; nothing here is applied)

Ground tags: **[ADM]** an admitted canon line, cited · **[CALC]** arithmetic shown · **[D]** derivation · **[gap]** an open slot, written as one. Pass lines are cited as the pass's own words, not as canon. Every third order marked [D] is derivation at medium to low confidence, and a later reader should not cite it as canon.

### OWN-1 · The road between Mirny and the spur member (F-10)

**Proposed finding.** The pass's null at `P5` L463 holds two objects, and `DR-131` item 3 treats them differently. (A, B, C)
- **(a) The spur member's own road access** is not one of Mirny's lines. That covers the spur, its junction with Hwy 110, its "**only overland link**" and its lack of a port (`HWY` L272 to L281, apart from L278's two clauses about Mirny's road).
  - [ADM `HWY` L272–L281; `DRL` L1949] The lines are about a road Mirny is not named in, so they fail the inclusion half. Their stated carrier is the spur member's spec (L281).
  - It is another place's matter, not an open slot of Mirny's. (C)
- **(b) The road link between the spur member and Mirny.**
  - [ADM `HWY` L199; `CRD` L340; D] The spur member is not listed on Hwy 110's route (L199) and is not one of Mirny's direct highway neighbors (L340). This half was always readable from Mirny's own lines. (C; A and B in Round 3) A route line lists stops, not every place near it. (B)
  - [ADM, conditional on OWN-QD-1] `HWY` L278: "**The Denman Glacier crossing is not built; there is no western link to Mirny.**" If the clause is admitted, the slot closes in the negative: no direct road joins them. (A, B, C)
  - [gap] "Not built" gives no era and no plan. Whether a crossing exists in either Act, and whether it was ever intended, planned or refused, and by whom, is not stated. That is unwritten, not "never built". (B, C)
- **Hwy 110 through Mirny is unchanged.** [ADM `HWY` L199] "**Route:** Zhongshan → Davis → Mirny → Casey → Concordia"; [ADM `CRD` L339] "**Highways:** Hwy 110 — midpoint"; [ADM `CRD` L340] one direct neighbor west and one east. [CALC] L199 lists five places, and Mirny is the third of five. (A, B, C)

**Proposed null row in place of `P5` L463's class** (C's row, worded per A in Round 3): "One member's road link to Mirny | **Not listed on Hwy 110's route and not a direct neighbor** (`HWY` L199; `CRD` L340); **no direct link across the glacier** if OWN-QD-1 admits `HWY` L278 | that member's own route is not a Mirny line (`DR-131` item 3, inclusion half)".

**Orders.**
- *1st* [ADM `HWY` L278, conditional on OWN-QD-1]: no direct road joins Mirny and the spur member. The crossing that would carry one is named, and it is "not built". (A, B, C)
- *2nd* [D, medium]:
  - Mirny's own entry lists one highway (`CRD` L339), so any road traffic arriving at Mirny reaches it along Hwy 110, from one of its two directions. (A) This reads L339's one highway as all of Mirny's roads, which the entry does not say outright. (C)
  - Which direction, and where the spur member joins, are member-side clauses (L274, L276) and are not used (OWN-QD-2).
  - [D, on `CRD` L49 under OWN-QD-3 (a) and `P5` L308] The spur member is one of the eight whose contact passes "**through** Mirny both ways [ADM L184]" (`P5` L308). So on Mirny's lines the hub's one direct tie to it is the signal. (A, B, C)
  - Among the members, it is the one whose lack of a direct road is *stated*. For four others the road is unstated, not absent (OWN-2).
  - *Split, written narrow:* C wrote "the one that Mirny's lines tie to Mirny by the relay alone". A and B (Round 3) found "the one" overstated against C's own count, so it is written with the qualifier.
- *3rd* [D, low]: In an outage the members "meet the failure as silence" (`ST8b` L426). The pass's fallback is the road, and "**No travel time is written.**" (`P5` L207, as `ST14` L606 quotes it).
  - For the spur member that fallback does not run straight to the hub. Whatever it needs from Mirny during an outage cannot come by a direct road, and the route it would take is not on Mirny's lines. (A, B, C)
  - The unbuilt crossing costs nothing while the relay holds and is felt only when it fails (B). That is the shape the pass already gives the hub: "The hub is thought about only when it fails" (`P5` L317). (A, B)
  - It says nothing about what the member's residents think of Mirny, which stays blind (`ST8b` L426). (A)
  - *Split, written narrow:* A's "a place only by a detour" is dropped, because it presumes a road route that Mirny's lines do not give. (B, Round 3; converged)

**Survives:** Hwy 110 through Mirny (`ST14` L607, L609); "present in the read set" (L609); the withholding of the member-only clauses, on a new ground; `ST8b` L643's last sentence.
**Changes:** the ground for withholding; the null's single class, which splits in two.
**Open slots:**
- the Mirny-side clause (OWN-QD-1);
- how overland traffic between the spur member and Mirny runs (not on Mirny's lines under OWN-QD-2's recommended answer);
- a distance or travel time (`HWY` L280's "TBD" is member-side in any case);
- the crossing's era;
- P5-14's fallback row, which no reader read.

### OWN-2 · What Mirny's road lines give the Neighbor seat (F-10, the fresh panel)

**Proposed finding.** `ST8b` L426's "the road between the members and Mirny" is not one blind spot. Of the eight other members Mirny routes (OWN-3), the road lines show:
- [ADM `CRD` L340] two are Mirny's direct road neighbors, one on each side;
- [ADM `HWY` L199, L201 with `CRD` L49] one more lies further along Hwy 110, at its northwest endpoint. The southern terminus is listed in another subnet (`CRD` L50) and is not counted (C);
- [ADM `HWY` L278, conditional on OWN-QD-1] the spur member has no direct link;
- [CALC] 8 − 3 − 1 = **4** are not placed on Mirny's road lines in the canon spans read. (B, C)
  - `P5` L325, a pass line, places one of the four on another highway, on sources no reader read. That gives no road relation to Mirny. (C)
  - For the four, "not stated" is a gap in Mirny's lines, not a shown absence on the ground. (A, B, C)
- *Split, resolved:* A's Round 1 counted on `CRD` L340 alone (two direct neighbors, six not, five with no road relation). B and C counted `HWY` L199's third member, and A adopted 3 / 1 / 4 in Round 3. A's Round 3 also proposed splitting the four into one on another highway and three others. That is written here as C's note above, because `P5` L325 is a pass line on unread sources and places no road to Mirny.

**Orders.**
- *1st* [CALC on ADM]: Mirny's own lines give the road to Mirny for three of the eight, and, conditionally, its absence for one. (B, C)
- *2nd* [D]: For the three, Mirny is both a place on their road and the hub on their relay. For the spur member it is the relay only. For the four it is the relay only *as far as Mirny's lines go*. (C)
  - Mirny's relay reaches further than its road: [CALC] 8 − 3 = 5 of the eight are not on Mirny's highway as listed. The people who keep the relay up hold together places they do not drive past. (B)
- *3rd* [D]:
  - The seat can be cast two ways from Mirny's own lines: as someone who reaches Mirny along Hwy 110, and as someone whose only stated tie to Mirny is the relay. (B)
  - On Mirny's lines, the outage seen "from the served end" (`ST8b` L426) has two shapes: silence with a road that runs to the hub, and silence with no direct road. (C)
  - The stake the culture file names, "the single point of failure for the whole subnet's internal cohesion" (`LC` L235), is held mostly for places Mirny's road lines do not reach. They meet Mirny through the very thing it keeps running. (A, count corrected per B and C)
  - The keepers' standing is the one `P5` L318 states: "**The people who keep the relay up are invisible exactly while they succeed**". (A)
  - The rest of the seat's blind list is unchanged ("what any member's residents, of either body, think of Mirny; the members' own wind and weather"), because no line Mirny is named in states any of it. (A, B, C)

**Survives:** the seat's blind cells on residents' views and the members' weather. **Changes:** the road blind spot, which now has four cases. **Open:** the roads of the four (gap); the spur member's case (OWN-QD-1).

### OWN-3 · The hub's member count (F-11; conditional on OWN-QD-3 (a))

**Proposed finding.** Under L1949, the subnet row (`CRD` L49) is one of Mirny's own lines.
- **The subnet is a shared thing. Mirny is named in it three ways (its official name, the Hub cell, the first member listed), and Mirny's own lines claim it.**
  - It carries the official name: "Six subnets, each named after its hub city. **Official names** are the hub city names — used in Arcanet documentation, government records, and signage." (`CRD` L42). (B)
  - It is in the Hub cell and is the first member listed (L49). (A, B, C)
  - Mirny's own entry claims the role: "**Arcanet subnet:** Mirny ("Australian") — **hub city**" (L338) and "Hub of the Mirny ("Australian") Arcanet subnet" (L341). (A, B, C)
  - Mirny's own culture file sites the subnet's physical hardware at Mirny: "the physical Arcanet infrastructure making Mirny the hub of the entire subnet" (`LC` L279). (C)
- **The count rests on the subnet table,** not on any other city's entry, so the exclusion half does not reach it.
  - The row's two parentheses are not used. The first reasons from real-world station geography, which is a coordinate only (`DR-19`). The second is an authoring note on a later addition. (A, B, C)

**The counts.**
- [ADM `CRD` L49; CALC] Nine places are listed, Mirny first; 9 − 1 = **8 other members**. This matches `P5` L308 ("**The eight other members**"), `AB3` L616 ("eight other members, not five") and `ST8b` L637 ("nine members' contact"). (A, B, C)
- [ADM `LC` L235, L279; CALC] The culture file names five ("the other five Mirny subnet cities"); 8 − 5 = **3** are not named there.
  - They are the two that L49 marks "latter two joined 2026-07-05" and the one marked "added 2026-10-21" [CALC 5 + 2 + 1 = 8]. `LC` L235's correction is dated "Corrected 2026-07-04".
  - [D] All of these are authoring dates, not in-world dates. (A, B, C)
- **Both-are-true check: none.** No admitted line gives an in-world era in which the subnet had five other members.
  - The one candidate is `P5` L308's "under `ARC`, two members are barely on the network the hub exists to carry". It fails at its premise: a member that is barely on the network is still on it, and L308 counts all eight as routed through Mirny. (B; C prefers this reason in Round 3)
  - Even on a reading that drops those two, [CALC] 8 − 2 = 6 ≠ 5. (A)
  - So "five" is a stale count, an authoring lag, with no in-world meaning. Nothing is built on it. Canon (L49) outranks the culture file's count. (A, B, C)
- [ADM `DRL` L1778] The count is a factual row of the kind `DR-112` item 1 excepts from the hold, and DEC-021 permits the members row (`AB3` L620; no reader read DEC-021). [ADM L1779] "the date any correction is applied" is not decided. **PROPOSED only.** (A, B, C)

**Orders.**
- *1st* [ADM L49; CALC]: the relay at Mirny carries the contact of eight other member cities, not five. (A, B, C)
- *2nd* [ADM `LC` L235, `CRD` L337, `ST8b` L636; D]: the stake the culture file states reaches eight members' contact with one another. Its mechanism, "if Mirny's damaged relay infrastructure fails entirely, the other five Mirny subnet cities lose contact … with each other" (`LC` L235), applies to eight. (A)
  - The structure is unchanged: one damaged hub ("Damaged; partially operational", `CRD` L337), "the subnet's internal connectivity resting on one already-damaged city's continued partial operation" (`LC` L235), and "a hub relay with no admitted second path across the frame" (`ST8b` L636).
  - Mirny's own warnings ride the same relay ("The same relay also carries the city's own weather warnings", `LC` L235). (B)
  - What changes is the reach: three more dependents than the culture file tells. (B, C)
- *3rd* [D]:
  - **The result is small: the count changes the stake's reach, not its form.** Every pass line resting on that form stands: `P5` L308, `ST8b` L637, and `AB3` L620's single-point-of-failure clause. The stale count lives on in two culture-file lines only (`LC` L235, L279). (C)
  - [D, low] Mirny's own entry says "subnets are organized geographically, not nationally" (`CRD` L341). The eight are Mirny's to carry because of where they lie, not by origin. (B)
  - *Split, written narrow:* B also wrote "or by any choice of Mirny's". A (Round 3) found that a small overreach, since L341 does not say whose choice it was. C accepted B's line as [D, low]. The line is written without the "choice" clause.

**Survives:** D-6's other half (the single point of failure); `P5` L308's "eight other members" and `ST8b` L637's "nine members", which now stand on an admitted line.
**Changes:** `AB3` L620's conclusion flips, and the count becomes proposable. The text for `LC` L235 and L279 is OWN-QD-4.
**Open:**
- Under OWN-QD-3 (b), the count stays unproposed, and the pass's three counts (`P5` L308; `ST8b` L426, L637) have no admitted source. Each would then need a note. (B)
- Which two members are "barely on the network" (`ARC`, which no reader read).

**Reserved, not adopted (OWN-RS-1)** (A, B, C):
- If OWN-QD-3 is answered (a), admitting the subnet row also brings in the note at `CRD` L55, which names Mirny: "Characters from non-matching cities within these subnets (e.g., Rothera in the "American" subnet, Mirny in the "Australian" subnet) may find their subnet's nickname inaccurate or mildly irritating."
- That is a line about a shared thing Mirny is named in. Mirny's own entry gives the same nickname beside the official name (L338, L341). The network Mirny keeps carries Mirny's name officially (L42) and another nation's name informally, as its nickname. (B)
- *Not adopted:*
  - it lies outside the three items (A, C);
  - no reader knows whether the pass already uses it (A);
  - what residents hear and say belongs to the CST (B);
  - nothing here may treat the nickname as identity, since the note calls the names "informal terms — not official" (L55; `DR-19`) (A).
- It is kept as a reserve, not excluded.

### OWN-4 · The coastal supply line (F-12)

**Proposed finding.** On the lines Mirny may use, the coastal supply line has one named receiving point: Mirny.
- [ADM `CRD` L341, formerly L330] "**Hub port for Australian freighter shipments** (raw materials, staged via Hobart/Fremantle) — as the subnet hub, likely the primary receiving point for the Mirny/Mawson subnet coastal supply line". Three words carry the weight (A):
  - "primary" presupposes at least one other receiving point;
  - "likely" hedges Mirny's own primacy;
  - "as the subnet hub" grounds the primacy in the relay role.
- [ADM `DRL` L1967, `DR-133` item 1, a ruling that names Mirny] Mirny is one of Australia's receiving nodes ("Mirny stays a node in every one of these lines.", `RN` L47). The node count belongs to the NODE piece (F-15) and is used here only for Mirny's being a node. (B, C; A in Round 3)
- **Excluded:** the clauses that make the two road neighbors receivers (`P5` L321's `CRD` L159, L182). They are grounded only in their own entries. (A, B, C)
- **Not used:** `DR-133` item 2 (`DRL` L1967: "The subnet's coastal supply line reaches Zhongshan by the coastal highway, certainly"). It is recorded for another city (`RN` L75) and does not carry (standing line 25). A later reader may not infer from it that a leg of the line runs on Mirny's road. (A, B, C)
- **Not carried:** L341's tail, "same real-world logistics pattern as Halley (subnet hub, different nationality) receiving South African shipments". It uses another city as a pattern, which is a measure under the one-location law. (A, B, C)
- [gap] Which places the line serves besides Mirny, in which subnet or subnets, how, and where goods go after Mirny: none is named on Mirny's lines. *None is named here*, which is not the same as none existing, since "primary" implies more than one point. (A, B, C)
  - The line's name joins Mirny's with a second subnet hub's name (`CRD` L341; L48, L49). (A, C) This is OWN-QD-6.
  - The line is quoted by its own name and never paraphrased as "the subnet's" line. (A)

**Orders.**
- *1st* [ADM `CRD` L341; `DRL` L1967]: Australian freighters land raw materials at Mirny directly ("**Mirny's own relation is the direct one** (`PRT` L129)", `P5` L321). Mirny is, likely, the line's primary receiving point. (A, B, C)
- *2nd* [D]: "Primary receiving point" presupposes other *receiving* points. It does not say that goods leave Mirny onward, since other points may receive from the sea themselves. (A)
  - The onward leg and its mode are not stated on Mirny's lines, and no lean is written. (A, C)
  - *Split, written narrow:* B (Round 1) wrote that the onward leg "would leave by Hwy 110 or by sea" and that "The road is the one at Mirny's door". A and C (Round 3) found the lean ungrounded: by derivation it reaches the content of `DR-133` item 2, which does not carry. B withdrew the paraphrase that second order rested on (Round 3, X14). Written: not stated, with no lean.
- *3rd* [D]: Mirny's port primacy and its relay centrality are one fact stated twice on Mirny's own entry ("as the subnet hub"). (A)
  - The harbor has no ground of its own in Mirny's lines. Its tier is "**Not established in canon**" (`P5` L452), and its reciprocal export is "**Absent — recorded open by its own file**" (`P5` L450).
  - So the harbor is presumed important because the city is central, not central because the harbor is good. (A)
  - This is Phase 5's own quiet friction (`P5` L321: "Mirny's port primacy is **inferred from its switchboard** … not stated from its sea"). It survives and sharpens: with the other receivers gone from Mirny's lines, the only line that makes Mirny a supply hub derives that role from its relay role. (A, C; B concurs in Round 3)

**Survives:** Mirny's own supply relation ("the direct one"); the quiet friction; `P5` L312's "raw materials **in**" (anchor now `CRD` L341).
**Changes:** the count "three"; the two other receivers; the sibling clause on the west road neighbor's import port; the plural at `P5` L328, pending its check.
**Open slots:** the line's other receiving points; what its two-part name covers (OWN-QD-6); where goods go after Mirny, and by what mode; the `TWR` half of `P5` L328.

**Reserved, not adopted (OWN-RS-2)** (B's [D, low]):
- If both roles hold, two things sit at one damaged site (`CRD` L337): the subnet's contact (stated, `LC` L235) and the first landing of its Australian supply (hedged). That site's harbor tier is not established (`P5` L452), and the wind can shut it in season (`P5` L321).
- A shut harbor and a failed relay would then be failures of the same place.
- *Not adopted.* It rests on "likely", on an unstated season, and on the line serving the members, which is a gap. In Round 3, A held it reserved, B kept it only as a low addendum, and C accepted it as [D, low] but not as a finding. Written as the most conservative of the three: reserved.

### OWN-5 · The tie with the two road neighbors after "three" falls (F-12; `P5` L322, P5-28)

**Proposed finding.**
- **Ground (1), route:** stands [ADM `CRD` L340; `HWY` L199]. (A, B, C)
- **Ground (3), relay:** stands ("relay hardware" [ADM L184], per the pass). Under OWN-3, both neighbors are members whose contact the relay carries. (A, B, C)
- **Ground (2), supply:** "three receiving points" falls.
  - Recommended by all three after Round 3 (PROVISIONAL; OWN-QD-5): withdraw (2) from the tie's grounds and add a null row. The row (C) reads: "Whether the two road neighbors receive on the coastal supply line | **Not stated on Mirny's lines** | their own entries carry it; excluded by `DR-131` item 3".
  - Reasons:
    - the null table is the pass's own place for "not stated" (A);
    - `ST14` L341 reports that the shared connections file now grounds the two road neighbors' ties "on the Register, on Hwy 110 and on the relay hardware", with no supply among them (C). This is a supporting reason only, because the pass marks that file "**Not an input.**" (`P5` L322) (A);
    - membership in the subnet is not a supply tie, and the line's own name joins two subnets, so re-grounding (2) on membership would be a forced fit (A; B withdrew that re-grounding in Round 3);
    - the null row keeps "not stated here" from reading as "not so" (B, C).
- **`LC` L228, Mirny's own file:** "Fellow Mirny subnet coastal city, nearby along the highway network; a close working relationship given geographic proximity."
  - The content of that relationship is not stated. The supply line must not be poured into that empty content, because that would bring the excluded clause back in through Mirny's own file (no forced fit). (A)
  - "A close working relationship" is a pre-ULM characterization and is not adopted here. The file's corrections are held under `DR-112`. (B)

**Orders.**
- *1st* [ADM]: On its own lines, Mirny is tied to its two road neighbors by the road that runs through it (`HWY` L199; `CRD` L340) and by the relay that runs through it (`P5` L322, ground (3), [ADM L184]). (C)
- *2nd* [ADM `P5` L308, L309, L310]: On the lines read, Mirny's lines record no goods exchanged with either road neighbor as such. (C)
  - To the west: "no admitted flow between the two cities themselves" (`P5` L309).
  - To the east: "the eastern highways" are the materials' destination [ADM L174] (`P5` L310). That is a direction along the road, not a counterparty.
  - Nothing is recorded as coming back for the carrying (`P5` L308: "anything recorded as coming back for carrying it").
- *3rd* [D]: Mirny's lines record carriage for these two ties and do not record exchange. For the nearest neighbors, this sharpens P5-27's "Mirny is the medium, not a party" (`P5` L318). (C)
  - *Split, written narrow:* C wrote the ties as "carriage, not exchange", and B (Round 3) rated it the strongest third order. A (Round 3) objected that `LC` L228 states a "close working relationship" whose content is unstated, so the slot is open and not settled as carriage. **Written:** carriage is recorded and exchange is not. Whether the ties hold more than carriage is an open slot (`LC` L228), not settled as "carriage only".

**Survives:** the tie itself ("The ties are **kept**", `P5` L322); grounds (1) and (3).
**Changes:** ground (2).
**Open slots:** ground (2)'s disposition (OWN-QD-5); the content of `LC` L228's "close working relationship"; whether the two road neighbors receive on the line.

### 3.6 · The one-location test on every sentence kept or proposed (A, B, C)

- **"Mirny's road is Hwy 110, on which it is the midpoint."** No other city is named. Survives.
- **(merged wording, unquoted) One member's own road access is not one of Mirny's lines.** This is a claim about Mirny's read set. Survives.
- **(merged wording, unquoted) No direct road joins Mirny and the spur member; the crossing is not built.** Delete the member, and "no road reaches Mirny directly from one member of its subnet" survives. Relation (what does not flow).
- **"Relung Panen is a spur off it, not a stop on it."** Delete the name and no claim about Mirny survives, and L199 already implies it. Not used. (C)
- **(merged wording, unquoted) Mirny's highway reaches three of the eight members it routes; four are not placed on it on Mirny's lines.** A claim about Mirny's road and signal survives. Relation, with no ranking. (B, C)
- **(merged wording, unquoted) The relay at Mirny carries the contact of eight other member cities; an outage silences all eight to each other.** No other city is named. Relation (what flows through Mirny, and in which direction).
- **"The eight are Mirny's to carry because of where they lie."** No other city is named. Kept, [D, low]. (B)
- **(merged wording, unquoted) Mirny is a hub port for Australian freighter shipments and likely the primary receiving point of the line its entry names.** The partner nation is named as a fact Mirny lives with, not as a measure. With the second hub's name deleted, the claim stands. Relation.
- **"Mirny's port primacy is inferred from its switchboard, not stated from its sea."** Survives. (C)
- **(merged wording, unquoted) On its own lines, Mirny's ties to its road neighbors record carriage, not exchange.** No neighbor is named, and the claim is about Mirny's relations. Relation. (C, with OWN-5's open slot)
- **Dropped:**
  - the transshipment clause (no Mirny claim survives deletion, and the contrast is a measure);
  - L341's "same real-world logistics pattern as …" tail (a measure).
- **Not used:** `CRD` L335 ("**Real station:** Mirny Station (Russia)"), which is a coordinate only (`DR-19`), and L341's founder clauses, which belong to the Founding Register's lines and not to these items. (A)

---

## 4 · Found by / confirmed by

"Confirmed by" names the readers who confirmed the point in Round 3 cross-checks or adopted it in their Round 3 merge view. "—" means no reader needed to confirm it, because all three found it independently, or that no confirmation was recorded.

| Key | Finding | Found by | Confirmed by | Split (if any) and how it was written |
|---|---|---|---|---|
| §2.0 | The names test is not the test; `DR-131` item 3 defines `DR-122` item 5's term | A, B, C | — | none |
| §2.0 | `DEC-183` = decision 4 (inferred) and its evidence | A, B, C (order of answers); C (item 6 ↔ `DEC-181` ↔ decision 2); B in Round 3 (item 3 ↔ decision 3) | A, B (C's evidence) | B's "accepted both halves": A found no passage for it, and C asked that it be marked as inference. Written: what the "Yes" accepted is not read. |
| §2.1 | `ST14` L335's blanket mark narrows (not cited by the item reader) | A, B, C | — | none |
| §2.1 | `ST8b` L426's road blind spot was wider than its ground | A, B (two direct neighbors); B, C (a third member on Hwy 110) | A (Round 3) | none |
| §2.1 | The ground for the member-side clauses is the inclusion half; the exclusion half turns on the ruling check | C; B (the editor-restatement point) | A, B (Round 3) | Round 1: A held (b) and (c), B the exclusion ground. Converged in Round 3 on C, refined by B. |
| §2.1 | `P5` L207's sub-row carries the same null | C | A, B (Round 3, at low) | none; the merge checked the line's words only |
| §2.2 | `AB3` L620's "No Mirny line states the count…" is narrower than written | A, B, C | A, B, C | C's "outside the culture file" wording was found muddled by A and B; the narrower statement is written. |
| §2.2 | "five against nine" mixes other members with all members | A, B, C | A, B, C | Confidence: A low in Round 1, high in Round 3; written high. |
| §2.2 | "already docketed … with nothing to add" now reads "proposable again" | C | A, B | none |
| §2.3 | `P5` L309's gap cell "a supply line" falls; L310 inherits | A, C (inheritance: C) | B; A on the inheritance (Round 3) | B missed it in Round 1 and adopted it in Round 3 |
| §2.3 | `P5` L309 and L310's view cells rest on the neighbors' entries alone | A, C | B (Round 3) | none |
| §2.3 | The transshipment sibling clause falls | A, B, C | — | none (grounds unioned) |
| §2.3 | `P5` L328's plural; `TWR` to be checked | A, B, C | — | B's "admissible if it names Mirny" adopted by A and C |
| §2.3 | `ST14` L340's mark on the neighbors' entries | A, B, C | — | A: stands; B: moved to C in Round 3; C: narrows to the clause test, with road lines "admissible under (b)". Written as the claim-least reading: the mark stands for the receiving clauses; nothing else is tested or admitted. |
| §2.3 | `ST14` L337's ports mark needs re-testing | B | A, C (Round 3, at low) | none |
| §2.3 | The line's two-part name ("the Mirny/Mawson subnet coastal supply line") | A, C | B (Round 3; withdrew its paraphrase) | B's Round 1 paraphrase withdrawn |
| §2.3 | Anchor re-key `CRD` L329/L330 → L340/L341 | A | B, C (Round 3) | none |
| §2.4 | Section G was present at 135 lines; only H was added | A, C | — | B's "G and H" corrected |
| OWN-1 | The null splits; member-side clauses out; the Mirny clause pending | A, B, C | — | none |
| OWN-1 | The `HWY` L199 / `CRD` L340 half was always readable; the replacement null row | C (A's wording) | A, B (Round 3) | none |
| OWN-1 | 2nd order: Mirny's one listed highway (`CRD` L339) | A | B, C (Round 3; C at [D], medium) | none |
| OWN-1 | 2nd order: the spur member's stated absence | C | — | A, B: "the one" overstated; qualified as the one *stated* absence |
| OWN-1 | 3rd order: the outage and no direct road | A, B, C | — | A's "detour" dropped (B, Round 3) |
| OWN-1 | [gap] "not built": no era, no plan | B, C | — | none |
| OWN-2 | Three on Hwy 110, one stated without a direct link, four unstated | B, C | A (Round 3) | A's Round 1 count (two and six) superseded; A's Round 3 split of the four folded into C's note on `P5` L325 |
| OWN-2 | The relay reaches further than the road; the keepers' standing | A, B | C | none |
| OWN-3 | Eight other members; the three unnamed are the later-dated ones; authoring dates | A, B, C | — | none |
| OWN-3 | Both-are-true check: none | A (arithmetic), B (premise) | C (Round 3, prefers B's reason) | Both written, B's reason first |
| OWN-3 | The subnet carries Mirny's *official* name (`CRD` L42) | B | A (Round 3) | none |
| OWN-3 | The relay hardware is sited at Mirny (`LC` L279) | C | A, B (Round 3) | none |
| OWN-3 | The count changes the stake's reach, not its form | C (A, B in substance) | — | none |
| OWN-3 | "The eight are Mirny's to carry because of where they lie" | B | C (Round 3, [D] low) | A: "or by any choice of Mirny's" overreaches; that clause is dropped |
| OWN-RS-1 | `CRD` L55, the nickname note: admissible, not adopted | A, B, C | — | none |
| OWN-4 | One named receiving point; `DR-133` item 1 used positively | A, B, C; B (positive use) | A, C (Round 3) | none |
| OWN-4 | `DR-133` item 2 and L341's "pattern" tail not carried | A, B, C | — | none |
| OWN-4 | 2nd order: onward leg not stated, no lean | A, C | — | B leaned toward Hwy 110; written with no lean |
| OWN-4 | 3rd order: port primacy and relay centrality are one fact | A | B, C (Round 3) | none |
| OWN-RS-2 | Two dependencies at one damaged site | B | — | A: reserved; B: low addendum; C: [D] low. Written as reserved. |
| OWN-5 | Ground (2) withdrawn; a null row added | C | A, B (Round 3) | Round 1: A held it without content, B re-grounded it on membership. Converged on C in Round 3. |
| OWN-5 | `LC` L228's relationship not filled with the supply line | A, B | — | none |
| OWN-5 | 3rd order: carriage recorded, exchange not | C | B (Round 3: the strongest) | A: `LC` L228 leaves the slot open. Written: carriage recorded, exchange not, with the rest an open slot. |

---

## 5 · Docket (proposed, never applied; pass files are not edited, `DR-101`)

| Row | File | Line | Proposed note (one sentence) | Confidence | Merges |
|---|---|---|---|---|---|
| OWN-DK-1 | `04_Phase_05_Relation_and_Geometry.md` | L463 | Under `DR-131` item 3 (L1949) the null splits: the spur member's own road access is not one of Mirny's lines (a road Mirny is not named in, carried by that member's spec, `HWY` L281), and the Mirny-side row reads "One member's road link to Mirny: not listed on Hwy 110's route and not a direct neighbor (`HWY` L199; `CRD` L340); no direct link across the glacier if OWN-QD-1 admits `HWY` L278". | medium (A: high for the split, medium for the second row) | A D1, B D101, C D203 |
| OWN-DK-2 | `04_Phase_05_Relation_and_Geometry.md` | L207 | The fallback-roads sub-row's "Relung Panen's road access is not in the admitted set." takes the same narrowing as OWN-DK-1. | low (no reader read the line; the merge checked its words only) | C D210 |
| OWN-DK-3 | `04_Phase_05_Relation_and_Geometry.md` | L308 | "**The eight other members**" stands on `CRD` L49 if OWN-QD-3 is answered (a); under (b) the count has no admitted source and needs a note saying so. | low (note only) | A D12, B D115 |
| OWN-DK-4 | `04_Phase_05_Relation_and_Geometry.md` | L321 | "all three receive …" narrows to Mirny's own entry (`CRD` L341: hub port, likely the primary receiving point for "the Mirny/Mawson subnet coastal supply line") and to `DR-133` item 1 (Mirny one of Australia's receiving nodes, by a ruling naming Mirny), with no other receiver named on Mirny's lines, because the two neighbors' receiving clauses are grounded only in their own entries and are excluded by `DR-131` item 3. | medium-high (A and C: high) | A D17, B D117, C D216 |
| OWN-DK-5 | `04_Phase_05_Relation_and_Geometry.md` | L321 | The clause on the west road neighbor's import-port role and transshipment (`PRT` L536, L130) rests on another location's rows and on a ruling about another city's port, and leaves no claim about Mirny when that city's name is deleted, so it is not used, and "**Mirny's own relation is the direct one** (`PRT` L129)" stands without the contrast. | medium | A D18, B D118, C D217 |
| OWN-DK-6 | `04_Phase_05_Relation_and_Geometry.md` | L321 and L312 | The anchors `CRD` L329 and L330 now read L340 and L341 (`ST14` L340). | high | A D19 |
| OWN-DK-7 | `04_Phase_05_Relation_and_Geometry.md` | L322 | Ground (2), "three receiving points on one coastal supply line", falls as a ground for the tie with the two road neighbors and, if OWN-QD-5 is answered as recommended, is withdrawn and recorded as a null row ("whether the two road neighbors receive on the coastal supply line: not stated on Mirny's lines"), with the tie standing on grounds (1) and (3). | medium (A: high that "three" falls; C: medium-high); the disposition per OWN-QD-5 | A D20, B D119, C D218 |
| OWN-DK-8 | `04_Phase_05_Relation_and_Geometry.md` | L309 (L310 by inheritance) | The gap cell's "a supply line" falls as a tie with the west road neighbor on Mirny's lines, and L310's "as above (P5-28)" inherits the change. | low-medium (C: medium) | A D21 (part), C D219 |
| OWN-DK-9 | `04_Phase_05_Relation_and_Geometry.md` | L309, L310 | The view cells' evidence ("`CRD` L181 names Mirny only as *"Mirny (east)"*"; "`CRD` L158 names Mirny only as *"Mirny (west via Hwy 110)"*") reads each neighbor's view of Mirny from that neighbor's own entry alone, a clause grounded only in another city's lines, so "not stated" stands without it, while the directions stand on `CRD` L340 and `HWY` L199. | low (A: low-medium) | A D21 (part), A D22, C D220 |
| OWN-DK-10 | `04_Phase_05_Relation_and_Geometry.md` | L328 | The plural "the Mirny/Mawson coastal cities" does not stand on its `CRD` half (now L341: one receiving point, no other city named), so `TWR` L993–994 is checked before the plural is kept; it is admissible for what it says of Mirny if it names Mirny. | low | A D23, B D120, C D221 |
| OWN-DK-11 | `Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md` | L607 | The ground "its lines name other locations, so it is not used here" is replaced by `DR-131` item 3's test: the member-side clauses of `HWY` L272 to L281 stay out because they are not about a shared thing Mirny is named in (whether the exclusion half also applies turns on OWN-QD-1's check), and the Mirny-naming clause of `HWY` L278 waits on OWN-QD-1. | medium-high for the ground (A and C: high); medium for the outcome (C) | A D2, B D102, C D201 |
| OWN-DK-12 | `Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md` | L609 | The addendum's "it names other locations and is not used here (AR-242)" takes the same correction as OWN-DK-11, "withheld by the one-location rule" holds only for the spur member's own access and on the new ground, and "The null reads: present in the read set" and "Hwy 110 through Mirny is unchanged." stand. | medium-high (A and C: high) | A D3, B D103, C D202 |
| OWN-DK-13 | `Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md` | L335 | The blanket mark "*not used (other location)*" on `HWY` L272 to L283 narrows to the clause test of `DR-131` item 3: L278's Hwy 110 route clause repeats the admitted L199, and its "no western link to Mirny" clause waits on OWN-QD-1. | medium | A D4, B D104, C D204 |
| OWN-DK-14 | `Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md` | L608 | The ground for not carrying B's Round 1 addenda on `HWY` L278 (the names test) narrows the same way, and whether any addendum carries for the Mirny-side clause is decided with OWN-QD-1 (no reader of this piece read the addenda). | low | A D7, B D105, C D205 |
| OWN-DK-15 | `Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md` | L825 | AR-242 is answered in part by `DR-131` item 3, a ruling recorded for every city: the spur member's own road access is not admitted, and what stays open is only whether the ruling behind `HWY` L278 makes its Mirny clause admissible (OWN-QD-1). | medium | A D5, B D106, C D206 |
| OWN-DK-16 | `Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md` | L842 | Decision 4's recommended first half ("Keep lines that name other locations out of a single location's run") is not what `DR-122` item 5 records (`DRL` L1868) and does not match `DR-131` item 3's later definition, so its second half stands read per L1949, and of its examples `HWY` L272 to L283 splits and `CRD` L49 comes in under OWN-QD-3 (a), while `HWY` L56 and `PRT` L826 are not tested here. | medium (that `DEC-183` answers decision 4 is inferred, not read; C: medium-high) | A D6, B D107, C D207 |
| OWN-DK-17 | `Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md` | L340 | "*not used (other location)*" on the two neighbors' entries stands for the receiving clauses Phase 5 took from them, now on `DR-131` item 3's exclusion and not on naming; whether any other clause in those entries could be admitted is not tested here, and nothing here admits one. | medium | A D24, B D121, C D222 |
| OWN-DK-18 | `Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md` | L337 | The blanket mark on the ports file's "other locations' rows" rests on the names test and is re-tested under `DR-131` item 3, since a ports row about a shared thing that names Mirny is admissible (no reader read the ports file). | low | B D122 |
| OWN-DK-19 | `Amendment_Rederivation_ST8b_FreshPanel_2026-11-08.md` | L426 | "the road between the members and Mirny (withheld by the one-location rule, `ST14` L607)" is not one blind spot: Mirny's own lines give that road for three members (`CRD` L340; `HWY` L199, L201), only the spur member's access was withheld (`ST14` L607), and that withholding now rests on `DR-131` item 3, with its Mirny-side clause pending (OWN-QD-1). | medium (B: medium-high) | A D8, B D108, C D208 (part) |
| OWN-DK-20 | `Amendment_Rederivation_ST8b_FreshPanel_2026-11-08.md` | L426 | "(five against nine)" sets the culture file's count of the other members ("the other five", `LC` L235) against all members with Mirny (`CRD` L49; `ST8b` L637), so like for like it reads five against eight other members (as `AB3` L616 has it), or six against nine in all. | high | A D10, B D109, C D208 (part) |
| OWN-DK-21 | `Amendment_Rederivation_ST8b_FreshPanel_2026-11-08.md` | L426 | "is already docketed (D-6, `AS5` L452), with nothing to add" now reads: docketed, set aside on 2026-11-08 (`AB3` L620), and proposable again under `DR-131` item 3 if OWN-QD-3 is answered (a). | medium (conditional on OWN-QD-3) | C D208 (part); adopted by A and B in Round 3 |
| OWN-DK-22 | `Amendment_Rederivation_ST8b_FreshPanel_2026-11-08.md` | L637 | "nine members' contact" stands on `CRD` L49 (Mirny and the eight) if OWN-QD-3 is answered (a); under (b) it needs the same note as OWN-DK-3. | low (note only) | A D11, B D116 |
| OWN-DK-23 | `Amendment_Rederivation_ST8b_FreshPanel_2026-11-08.md` | L643 | The reason for the cut ("because they name other places") falls and the seats' cut set re-sorts under `DR-131` item 3 (Mirny's own files and entries come back even when they name places, as do lines about shared things that name Mirny, and only clauses grounded only in another city's lines stay out), while "The Neighbor is cast through Mirny's own lines only (R14), and it says so." stands. | medium | A D9, B D110, C D209 |
| OWN-DK-24 | `Application_Batch_3_CultureFile_and_Spec_2026-11-08.md` | L620 | Under `DR-131` item 3 and OWN-QD-3 (a) the subnet row (`CRD` L49) is one of Mirny's own lines, so the count (eight other members) is proposable as a factual row under DEC-021, PROPOSED with its date undecided (`DR-112`, `DRL` L1779), while "No Mirny line states the count without naming them" (true of Mirny's canon sources, not of its pass lines `P5` L308 and `ST8b` L637) is no longer a test and the single point of failure stands. | medium (A and C: high); conditional on OWN-QD-3 | A D13, B D111, C D211 |
| OWN-DK-25 | `Application_Batch_3_CultureFile_and_Spec_2026-11-08.md` | L613 | The heading "**Not used (other location).**" no longer governs L616's count ("the hub routes eight other members, not five"), which stands on `CRD` L49 together with its "keep the single point of failure" under OWN-QD-3 (a). | medium (C: high); conditional on OWN-QD-3 | A D14, B D112, C D212 |
| OWN-DK-26 | `Application_Batch_3_CultureFile_and_Spec_2026-11-08.md` | L617 | "Own lines" in this span line now reads per `DR-131` item 3 (`DRL` L1949). | low (C: medium) | C D213 |
| OWN-DK-27 | `Local_Cultures/Mirny_Subnet/Mirny.md` | L235 | Proposed factual row (D-6, as `S5` L452 proposed it, not new): the five routed members and "the other five Mirny subnet cities" become the eight others of `CRD` L49, without the row's parenthetical reasons and worded per OWN-QD-4, with the stake sentence unchanged and the correction applied only on the developer's date (`DR-112`, `DRL` L1779). | medium (A: medium-high; C: high); conditional on OWN-QD-3 and OWN-QD-4 | A D15, B D113, C D214 |
| OWN-DK-28 | `Local_Cultures/Mirny_Subnet/Mirny.md` | L279 | The relay-hardware landmark's five routed members (pointer D-36) follow OWN-DK-27. | medium (C: high); conditional on OWN-QD-3 and OWN-QD-4 | A D16, B D114, C D215 |

*Confidence where the readers differ:* each row carries the lowest post-Round-3 rating, with the higher ratings named in brackets. The exception is OWN-DK-20: A and B rate it high in Round 3, and C rated its arithmetic high in Round 1. A's Round 1 "low" was withdrawn by A in Round 3.

---

## 6 · Questions for the developer

**OWN-QD-1 · Does the highway line "The Denman Glacier crossing is not built; there is no western link to Mirny." (`Highways.md` L278) count as one of Mirny's own lines?**
*Merges:* the F-10 item reader's IQ-1001; A's OWN-Q1; B's OWN-Q101; C's OWN-Q201.
- **What we know.**
  - The clause names Mirny and is about what reaches Mirny by road, so it meets the inclusion half of `DR-131` item 3.
  - The paragraph it sits in opens with "`[CGRM 2026-09-01 · Path 6 · developer ruling]`". But the section's stated source is another city's spec field, "which quotes the ruling" (L281).
  - The same paragraph restates L199 in an editor's words, so the tag does not by itself show that every clause under it is the ruling's own. (B)
  - Two tests decide it: the exclusion half of L1949, and the rule that only a ruling recorded for every city, or one naming Mirny, moves a Mirny conclusion (brief §3; standing line 25). (C, A)
- **A) Admit it.** The tag shows a ground beyond the other city's spec, so the clause is not grounded *only* in another city's lines. The null at `P5` L463 closes for the Mirny side (no direct road), and the Neighbor seat gains the line.
- **B) Withhold it.** If the ruling of 2026-09-01 was made for the other city, it does not carry, and the clause then rests only on that city's line. The null stays "present in the read set, withheld", now on `DR-131` item 3's exclusion ground.
- **C) Check first, then A or B.** The orchestrator, not a reader, reads the ruling at its own record, and no reader opens the member's spec.
  - If the ruling's own words name Mirny, or carry the clause, A follows, on two grounds: L1949, and a ruling that names Mirny.
  - Otherwise B follows.
  - If the ruling's only record is the spur member's spec field, the developer says whether the orchestrator may read that one field. (B)
- **Recommended (PROVISIONAL): C, then A or B as the ruling's own text decides.** All three readers converged on this in Round 3. The deciding fact is what the ruling itself says, and no Mirny reader has read it.

**OWN-QD-2 · Do the spur's junction lines (`Highways.md` L274, "joining Hwy 110 at Casey"; L276, "junction with Hwy 110") count as lines about Mirny's road?**
*Merges:* the F-10 item reader's IQ-1002; B's OWN-Q105; C's OWN-Q202. A resolved it without asking in Round 1.
- **A) No.** They are about the spur, a road Mirny is not named in, and their stated source is another city's spec (L281). They stay out, and how overland traffic between the spur member and Mirny runs stays an open slot.
- **B) Yes.** Any line about a junction on Hwy 110 is a line about Mirny's road.
- **Recommended (PROVISIONAL): A.** All three readers and the item reader agree. Under B, "its road" would take in every junction along Hwy 110, including other places' own access, which is what the exclusion half keeps out. Delete the names from L274 or L276, and no claim about Mirny survives.
- **Split on whether to ask it, written narrow.** In Round 1, A resolved this without the developer. In Round 3, C moved to A's Round 1 view: the one-location test settles it, so record it as a reading. A and B, in Round 3, kept it asked: the ruling puts "named in" on the shared thing, and Hwy 110 names Mirny (L199), so the reading choice is real. **Written: asked.** That is the form that claims least, because the merge does not settle a reading of the ruling on its own authority.

**OWN-QD-3 · Is an Arcanet subnet one of the "shared things it is named in" (`DEVELOPER_RULINGS_LOG.md` L1949, whose examples are "its port, airport, road, cluster")?**
*Merges:* the F-11 item reader's IQ-1101; A's OWN-Q2; B's OWN-Q102; C's OWN-Q203.
- **(a) Yes.** The subnet row (`CRD` L49) is one of Mirny's own lines. The hub's member count can be proposed (F-11 flips), and the pass's existing counts (`P5` L308; `ST8b` L637) stand on an admitted line. The reasons:
  - the developer's selection has no list: *"Own files + shared things it's in"* (L1948) (A, B, C);
  - the subnet carries Mirny's name as its *official* name (`CRD` L42), the strongest sense of "named in" (B);
  - Mirny is the Hub cell and the first member listed (L49), and Mirny's own entry calls it the "**hub city**" (L338) (A, B, C);
  - a subnet is a group of places sharing one piece of infrastructure, the same kind of thing as the listed "cluster" (A, B);
  - Mirny's own culture file sites the subnet's physical relay hardware at Mirny (`LC` L279) (C);
  - decision 4 had already listed `CRD` L49 among "Lines that name other locations but carry Mirny's own relation" (`ST14` L842) (A).
- **(b) No.** The parenthesis is a closed list, so L49 stays outside, F-11 holds as `AB3` L620 wrote it, and the culture file keeps "five". The pass's counts at `P5` L308 and `ST8b` L426 and L637 then need notes. The reasons:
  - the parenthesis does not name a subnet;
  - decision 4 named `CRD` L49 explicitly, and the answer of 2026-11-08 was "Yes (Recommended)" (`DRL` L1867), so the earlier answer may have covered this exact line (B). (That `DEC-183` is decision 4, and what its "Yes" accepted, are inferred, not read.)
- **Recommended (PROVISIONAL): (a).** All three readers agree. The later ruling is recorded for every city, defines the very term, and cites `DR-122` item 5 by number.

**OWN-QD-4 · If OWN-QD-3 is answered (a), how is the culture file's member text corrected (`LC` L235 and L279; dockets D-6 and D-36)?**
*Merges:* A's OWN-Q3; B's OWN-Q103; C's OWN-Q204.
- **(A) Count and names.** Name all eight other members as `CRD` L49 gives them, without the row's parenthetical reasons, and make "the other five" read "the other eight". This keeps the file's own form: each name is a relation (that member is routed through Mirny), not a measure. (A, C)
- **(B) Count and a pointer.** Write "the other eight cities of the Mirny subnet (`City_Relationship_Database.md` §2)", drop the names from L235, and let L279 point the same way. The five names went stale because the culture file kept its own copy of a list whose home is the database row, and a pointer keeps one copy. (B, Round 1)
- **(C) Hold it** for the post-ULM rewrite with the 39 held corrections (`DR-112` item 1). This contradicts the permission already given for factual rows (DEC-021; `DRL` L1778). (A)
- *Not offered:* the count corrected with the five names kept. That leaves a list that reads as complete and contradicts its own count. (A, B, C)
- **Recommended (PROVISIONAL): (A).** A and C recommend it, and B withdrew its (B) in Round 3 ("the post-ULM rewrite can change form"). B's single-copy argument stands as the reason for option (B). Whichever is chosen, the date of applying it stays the developer's (`DRL` L1779).

**OWN-QD-5 · Now that "three receiving points" falls, what happens to ground (2) (supply) of the tie between Mirny and its two road neighbors (`P5` L322, P5-28)?**
*Merges:* the F-12 item reader's IQ-1202; A's OWN-Q4; B's OWN-Q104; C's OWN-Q205.
- **(a) Withdraw (2)** from the tie's grounds, and add a null row: "Whether the two road neighbors receive on the coastal supply line | **Not stated on Mirny's lines** | their own entries carry it; excluded by `DR-131` item 3". The tie stands on (1) the route and (3) the relay hardware. (C)
- **(b) Keep a narrowed (2)** as Mirny's own supply role on the line, without placing the neighbors on it. Under this option the ground no longer connects to *those two* neighbors. (The item reader's (b); A's B)
- **(c) Hold (2) without admissible content,** as P5-28 already does for the tie's "cultural" half (R-60), until a Mirny line or a ruling places the neighbors on the line. (The item reader's recommendation; A in Round 1)
- **(d) Re-ground (2) on subnet membership:** both neighbors are members of the subnet whose line Mirny likely receives first. This needs OWN-QD-3 (a). (B in Round 1, withdrawn in Round 3: it rested on a paraphrase of the line's name as Mirny's subnet's line.)
- **Recommended (PROVISIONAL): (a).** All three readers recommend it after Round 3. The reasons:
  - the null table is the pass's own place for "not stated" (A);
  - the shared connections file grounds the two ties "on the Register, on Hwy 110 and on the relay hardware", not on supply (`ST14` L341; a supporting reason only, since the pass marks that file "**Not an input.**", `P5` L322) (C, A);
  - (d) would be a forced fit, because membership is not a supply tie and the line's name joins two subnets (A, B);
  - a null row keeps "not stated here" from reading as "not so" (B, C).

**OWN-QD-6 · What does "the Mirny/Mawson subnet coastal supply line" (`CRD` L341) cover?** *(Low priority: the developer may simply know.)*
*Merges:* A's OWN-Q5; C's open slot; B's Round 3 view (the question is optional; record the slot).
- **Why it is asked.** After the narrowing, Mirny's own entry is the line's only ground. The line's name joins two subnet hubs' names, and the subnet table lists them as two separate subnets (`CRD` L48, L49; L42).
- **A) One coastal line serving the coasts of both subnets,** with Mirny likely its primary receiving point.
- **B) A joint label for Mirny's own subnet's line,** of whatever origin.
- **C) Leave it open.** Quote the line by its own name, never paraphrase it as "the subnet's" line, and record which subnet or subnets it serves as unstated.
- **Recommended (PROVISIONAL): C,** until a ruling recorded for every city, or one naming Mirny, says what the line covers. A ruling recorded for another city does not settle it (`DR-133` item 2; `RN` L75).

**Not asked.** The F-12 item reader's IQ-1201 (whether another city's entry that names a shared thing carrying Mirny's name lets Mirny use that line). All three readers leave it unasked, because the result for F-12 is the same either way. All three lean to its option (a): the exclusion governs every clause about another city's receiving, and a shared line's name inside another city's entry does not admit that city's receiving clause.

---

## 7 · Limits

- **Read by no reader** (each known only through a pass line, the review note, or a ruling line):
  - `Ports.md` (only as `RN` L39 to L47 and `DRL` L1967 report it);
  - the ruling record CGRM 2026-09-01, Path 6;
  - the decisions file (DEC-021's and `DEC-183`'s own texts);
  - the two neighbors' entries (`CRD` L157 to L159, L180 to L182), left unread by design;
  - `TWR` L993–994 and `ARC`;
  - the spec (`SPEC` L5, L174, L184);
  - `S5` L452 (D-6's own text);
  - P5-14's fallback row;
  - `ST14` AS14-45 and snags 1 to 3, and B's Round 1 addenda (`ST14` L608);
  - the shared connections file at L274 to L278 (only via `ST14` L341);
  - `HWY` L56 and `PRT` L826 (decision 4's other lines) and the highway junctions index;
  - the fresh panel's seats list;
  - the culture file outside L228 to L240 and L272 to L285.
- **Inferred, not read.** That `DEC-183` answers `ST14`'s decision 4, and what its "Yes (Recommended)" accepted (section 2.0).
- **What the merge opened.** The merge re-derived nothing. To settle quotations it opened, read-only, only lines the readers cite: `P5`, `ST14`, `ST8b`, `AB3`, `CRD`, `HWY`, `LC` and `DRL` at the cited lines, and the item readers' outputs at their cited lines.
  - `P5` L207 was opened to settle the words of C's row OWN-DK-2, since no reader had read it at source.
  - That line also cites road lines for other members, using `HWY` anchors (L277, L278, L281) that now fall inside the spur section inserted on 2026-10-21 (`HWY` L272 to L283). Whether those anchors were re-keyed elsewhere was not checked. No finding here rests on them, and the count of four members not placed on Mirny's road lines (OWN-2) stands only on the readers' spans.
- **Conditional results.**
  - OWN-1's admitted clause, its first order and the closing of `P5` L463's second row depend on OWN-QD-1.
  - OWN-3, the count of eight in OWN-1 and OWN-2, and rows OWN-DK-3, OWN-DK-21, OWN-DK-22, OWN-DK-24, OWN-DK-25, OWN-DK-27 and OWN-DK-28 depend on OWN-QD-3.
  - The culture-file text depends on OWN-QD-4, and OWN-DK-7's disposition on OWN-QD-5.
- **The road counts rest on `HWY` L199 as a listed route and on `CRD` L340.** "Not on Mirny's highway as listed" means exactly that. It does not mean "no road". (B)
- **A figure not used.** `ST8b` L637's "about 248 years" has no basis stated on any admitted line (A and B, Round 3). No reader derived or used it, and it is not cited from this piece.
- **Scope.**
  - Australia's node count belongs to the NODE piece (F-15). Only Mirny's being a node is used here.
  - No station heritage is used. `CRD` L335's "Real station" is a coordinate only, and L49's real-world geography parenthesis is not an input (`DR-19`).
  - No population-origin material is excluded. The founder and exile-group clauses of `CRD` L341 and `P5` L328 lie outside the three items and are untouched, and the nickname note (`CRD` L55) is reserved (OWN-RS-1), not excluded.
- **Process notes for the round record** (not findings):
  - Reader B wrote two scratch files into its staging folder, against its brief. B recorded this in its own Limits, and A and C flagged it for the orchestrator. Neither file was opened or verified by the other readers or by this merge.
  - B dated section G of the review note as added after the item readers ran. A and C corrected this: only section H was added.
  - B's gloss "the capital" for Hwy 110's southern terminus has no line in the read set, and nothing rests on it (C).
- **Status.** Nothing here is applied, complete or ready. Every finding and every docket row is PROPOSED, and the date of applying any correction is the developer's (`DRL` L1779).
