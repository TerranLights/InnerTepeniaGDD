# Davis amendment re-derivation piece S1: the Step −1 input contract, its composition region and its read spec (2026-11-09)

> **Status: PROPOSED. Nothing here is applied.** Three independent readers (A, B and C) re-derived this piece from
> one frozen brief. A mechanical Round 2 check confirmed that each read its files. In Round 3 each reader
> cross-checked the other two. One merge writer then wrote this document under merge rule M-246 (developer ruling
> 2026-09-28, refined 2026-11-04). The first check's single reader is credited as K. No pass file, spec, census or
> source was edited (DR-101); every correction below is a docket row for the amendment note. Davis is read on its
> own terms. Where a source line names another location, that name is not written here.

Short names: **00.1** = `00.1_Step_MINUS-1_Input_Contract.md`; **00.1a** = `00.1a_RULING_Vision_Notes_and_Specs_L135-181.md`;
**SPEC** = Davis's spec; **CENSUS** = `Official_Population_Census.md`; **REGISTER** = `Founding_Register.md`;
**UEIC** = `Upper_Earth_Immigration_Composition.md`; **LOG** = `DEVELOPER_RULINGS_LOG.md`; **MAP** =
`.t8_S1_spec_numbering_map.txt`; **05** = `05_The_Input_Contract.md`; **ALR** = `Amendment_Layer_Rules.md`.
Pass-time numbering is the spec's numbering at the pass-completion commit d2dd2136 (MAP L1); current numbering is
the live spec's (260 lines). Finder credits: A, B, C (the three readers), K (the first check's reader).

## 0. In short

- **The composition region stands, and is now classified line by line.** Current SPEC L10-L81 (72 lines) passes 05
  §6.1 first and §6.3 second: 50 ADMITTED, 3 PARTIAL (L15, L16, L28), 19 INERT, none struck. L28's two pointers
  are DO-NOT-FOLLOW. All three readers gave the same verdict on every one of the 72 lines.
- **The pass-time L21 partial strike is retired** for lack of a target. The "(founding wave)" tag at L21 and L38
  needs no strike, and it is read only as "Australia is the Register's named founder".
- **L28 and L78 are provenance and scope notes that bind as limits.** L28's pool percentages, multipliers, draw
  range and seed are not shares. Its time-zone-window clause is a legal statement of method, used only as a limit.
- **The L15-L16 revision notes are read and not used.** The DR-90 step is "Arithmetic, NOT a migration"; the
  DR-68 step is arithmetic only PROVISIONALLY. Nobody is recorded as flowing into Davis.
- **Current read spec:** `1-3,5-8,10-111,114-144,146-158,167,172,177-179,200,202-203`, 161 lines (bound 166),
  zero carried strikes; it is also the LRANGE value. **Census read spec:** `33,390-396,506,650`, 10 lines (L506
  and L650 rest on the orchestrator's result only).
- **The published string at 00.1 L223 and L238 must not be run on today's file.** It would read current L112-L113
  (both FULL-struck) and L176 (excluded), and miss 27 admitted lines, G3's only line L167 among them.
- **On L176, both contract statements are right, each in its own numbering.** 00.1 and 00.1a mix two numberings
  without a marker, probably because of DR-85's citation-remap script (conditional).
- **§3.3's limit:** "share-weighted model" is killed; randomization narrows to two rows; "identical between
  censuses" survives on L78; the rest gives way to DR-104 items 1 and 2.
- **Figures:** Census I 1,210,432; retention 67.54% combined, 76.88% humans, 58.63% robots; spread 18.25 points.
  The majority still inverts (robots 51.20% at Census I, 44.45% at Census II). A finding may rest on the
  direction, never on the spread's exact size.
- **Stable in part:** totals, row membership and tiers hold; the exact shares of Taiwan, Mongolia, East Turkestan
  and Tibet are a reserved decision (PROVISIONAL).
- **Lines outside the region need attention:** current L8 is PARTIAL; L109 and L167 changed wording and are carried
  with their use held; L113 stays struck. G3 is conditional, and PROCEED stands on five countable generators.
- **Banner:** VALID and PROCEED stand as the verdict of their date. Three readers for this region is a standing
  rule (DR-74), not a provisional choice. The governing addresses are stale.

## 1. Findings re-derived

### AM-S1-F1 The line-by-line classification of current SPEC L10-L81

Order applied to every line: 05 §6.1 (circularity) first, §6.3 (ratification) second, then 05 §6's acceptance
properties. Rule shorthand: **§6.1 adm.** = the admissible column of 05 §6.1, the row for census, composition and
population change (05 L496); **§6.3 root** = ratified by root, `Cities/Specs/` and the census (05 L726-L730);
**§6 Sc / St / At** = the Scoped, Stable and Attributed properties (05 L461-L466); **§6.1d** = the suspect-heading
check. Finders: the verdict on every line was given identically by A, B and C; a ground credited to one reader
in brackets was added by that reader.

| line | verdict | rule (05 section) | one-sentence ground | disposition |
|---|---|---|---|---|
| L10 | INERT | — | Blank line. | confirmed by all three |
| L11 | INERT | — | Horizontal rule; no content. | confirmed by all three |
| L12 | INERT | — | Blank line. | confirmed by all three |
| L13 | INERT | §6.1d (checked) | The heading "Population & Composition" is not a suspect heading and makes no claim. | confirmed by all three |
| L14 | INERT | — | Blank line. | confirmed by all three |
| L15 | PARTIAL | §6.1 adm. → §6.3 root; §6 At | The current Census I figures (590,668 humans / 619,764 robots / 1,210,432) are admitted as the governing population (DR-4); the two revision parentheticals hold superseded figures and authoring notes and are read and not used; one names another location (another location: not used). | confirmed by all three |
| L16 | PARTIAL | §6.1 adm. → §6.3 root; §6 At | The current Census II figures (454,101 / 363,374 / 817,475) are admitted; both parentheticals are read and not used on the same grounds, and the second carries no date or ruling, so that clause also fails §6 Attributed [B]. | confirmed by all three |
| L17 | INERT | — | Blank line. | confirmed by all three |
| L18 | INERT | — | Tier-table header. | confirmed by all three |
| L19 | INERT | — | Table separator. | confirmed by all three |
| L20 | ADMITTED | §6.1 adm. → §6.3 root | Primary tier membership (five origins), byte-identical to CENSUS L394; the label is mechanical (L78). | confirmed by all three |
| L21 | ADMITTED | §6.1 adm. → §6.3 root; REGISTER rule 1 | Significant tier membership, identical to CENSUS L395; "(founding wave)" points to REGISTER L59 (Australia) and means only that (CENSUS L33; DR-88 item 2; DR-99 item 2); the pass's partial strike has no target here. | confirmed by all three |
| L22 | ADMITTED | §6.1 adm. → §6.3 root; §6 St | Notable tier membership (38 origins), identical to CENSUS L396 and in the table's order; four of its rows carry DR-85's open question. | confirmed by all three |
| L23 | INERT | — | Blank line. | confirmed by all three |
| L24 | ADMITTED | §6 At; §6.3 root | A source pointer into a ratified root; it is followed only within Davis's census read spec, never across other locations' rows [A, C; B adopted this in Round 3]. | confirmed by all three |
| L25 | INERT | — | Blank line. | confirmed by all three |
| L26 | INERT | §6.1d (checked) | Sub-heading; makes no claim. | confirmed by all three |
| L27 | INERT | — | Blank line. | confirmed by all three |
| L28 | PARTIAL; its two pointers DO-NOT-FOLLOW | §6 Sc, At; §6.3 rules 2, 3 and 6 for the pointers | A provenance and scope note that binds as limits; its process numbers are not shares; its window clause is a method statement used only as a limit; its scratch-folder and commit pointers are never followed. | confirmed by all three |
| L29 | INERT | — | Blank line. | confirmed by all three |
| L30 | INERT | — | Column header; defines the columns and makes no claim. | confirmed by all three |
| L31 | INERT | — | Table separator. | confirmed by all three |
| L32 | ADMITTED | §6.1 adm. → §6.3 root | Japan 10.42% (126,123 at Census I), an origin and a headcount weight; its lead over L33 is a same-tier gap resting on L33's random draw, so no finding rests on the order [A, C]. | confirmed by all three |
| L33 | ADMITTED | §6.1 adm. → §6.3 root | Sinian Federation 9.72% (117,596), an origin; one of the two randomized rows (×0.5719, L28), so its exact share is not data (DR-104 item 1). | confirmed by all three |
| L34 | ADMITTED | §6.1 adm. → §6.3 root | United Kingdom 9.36%, an origin; its share was raised by the Sinian Federation refill (L28) [C]; no same-tier gap finding. | confirmed by all three |
| L35 | ADMITTED | §6.1 adm. → §6.3 root | Germany 8.54%, an origin, the row as split from Austro-Bavaria (CENSUS L862) [A]; raised by the refill [C]. | confirmed by all three |
| L36 | ADMITTED | §6.1 adm. → §6.3 root | Korea 8.35%, an origin carrying both successor Koreas (CENSUS L850-L852) and the neutral district's people (CENSUS L878) [C]. | confirmed by all three |
| L37 | ADMITTED | §6.1 adm. → §6.3 root | Indonesia 5.74% (69,512 at Census I), an origin level with L38; no finding rests on the 37-person gap (DR-104 item 1). | confirmed by all three |
| L38 | ADMITTED | §6.1 adm. → §6.3 root; REGISTER rule 1 | Australia 5.74% (69,475), an origin and the Register founder (REGISTER L59; DR-19); the tag says nothing about arrival, size or character; raised by the refill [C]. | confirmed by all three |
| L39 | ADMITTED | §6.1 adm. → §6.3 root | Thailand 3.23%, an origin reasoned by headcount, no cutoff (DR-104 item 2). | confirmed by all three |
| L40 | ADMITTED | §6.1 adm. → §6.3 root | Vietnam 3.10%, an origin. | confirmed by all three |
| L41 | ADMITTED | §6.1 adm. → §6.3 root | Philippines 3.06%, an origin. | confirmed by all three |
| L42 | ADMITTED | §6.1 adm. → §6.3 root | Malaysia 2.95%, an origin. | confirmed by all three |
| L43 | ADMITTED (share OPEN) | §6.1 adm. → §6.3 root; §6 St | Taiwan 2.86%, a separate nation (CENSUS L877); its share is open under DR-85 (LOG L1529), so no finding depends on it (PROVISIONAL). | confirmed by all three |
| L44 | ADMITTED | §6.1 adm. → §6.3 root | Russia (core state) 2.78%, a successor row (CENSUS L857) and a separate origin; per CENSUS L858 it also takes part of the old Ukraine [A] (see AM-S1-N14). | confirmed by all three |
| L45 | ADMITTED | §6.1 adm. → §6.3 root | South Africa 2.75%, an origin. | confirmed by all three |
| L46 | ADMITTED | §6.1 adm. → §6.3 root | Romania 2.51%, an origin (Hungary split from it, CENSUS L871) [A]. | confirmed by all three |
| L47 | ADMITTED | §6.1 adm. → §6.3 root | Ukraine 2.20%, an origin (on how CENSUS L858 reads, see AM-S1-N14) [B]. | confirmed by all three |
| L48 | ADMITTED | §6.1 adm. → §6.3 root | New Zealand 1.69%, an origin. | confirmed by all three |
| L49 | ADMITTED | §6.1 adm. → §6.3 root | Idelsk-Uralia 1.67%, a successor row of the old Russia (CENSUS L857). | confirmed by all three |
| L50 | ADMITTED | §6.1 adm. → §6.3 root | Belarus 1.54%, an origin. | confirmed by all three |
| L51 | ADMITTED | §6.1 adm. → §6.3 root; §6 Sc | Kazakhstan 1.45%, an origin at a share set by the window rule (L28; CENSUS L881); the figure carries no Davis-specific signal and is never a comparison, and that limit never lowers the row's standing as an origin (DR-104 item 2). | confirmed by all three |
| L52 | ADMITTED | §6.1 adm. → §6.3 root | Bulgaria 1.42%, an origin. | confirmed by all three |
| L53 | ADMITTED | §6.1 adm. → §6.3 root | Austro-Bavaria 1.39%, a successor row (CENSUS L862-L863). | confirmed by all three |
| L54 | ADMITTED | §6.1 adm. → §6.3 root | Lithuania 1.18%, an origin; this number held the pass's "share-weighted model" note at pass time [C]. | confirmed by all three |
| L55 | ADMITTED | §6.1 adm. → §6.3 root | Estonia 1.17%, an origin. | confirmed by all three |
| L56 | ADMITTED | §6.1 adm. → §6.3 root | Latvia 0.89%, an origin. | confirmed by all three |
| L57 | ADMITTED | §6.1 adm. → §6.3 root | Manchuria 0.71%, the second randomized row (×0.5855, L28; DR-94); its exact share is not data; it was already reduced, so it is not open (CENSUS L877). | confirmed by all three |
| L58 | ADMITTED | §6.1 adm. → §6.3 root | Siberia 0.66%, a successor row of the old Russia (CENSUS L857). | confirmed by all three |
| L59 | ADMITTED | §6.1 adm. → §6.3 root | Donska-Kubania 0.64%, a successor row of the old Russia. | confirmed by all three |
| L60 | ADMITTED (share OPEN) | §6.1 adm. → §6.3 root; §6 St | Mongolia 0.40%, a piece of the old China in Davis's window plus its own pool (L28; CENSUS L845, L848); its share is open (LOG L1529). | confirmed by all three |
| L61 | ADMITTED | §6.1 adm. → §6.3 root | Künnarantaiga 0.38%, a successor row of the old Russia. | confirmed by all three |
| L62 | ADMITTED (share OPEN) | §6.1 adm. → §6.3 root; §6 St | East Turkestan 0.34%, a piece of the old China (CENSUS L845); its share is open (LOG L1529). | confirmed by all three |
| L63 | ADMITTED | §6.1 adm. → §6.3 root | Hungary 0.29%, a successor row (CENSUS L871). | confirmed by all three |
| L64 | ADMITTED | §6.1 adm. → §6.3 root | Northern Ireland 0.23%, a successor row of the old United Kingdom (CENSUS L866). | confirmed by all three |
| L65 | ADMITTED | §6.1 adm. → §6.3 root | Dagestan 0.12%, a successor row of the old Russia. | confirmed by all three |
| L66 | ADMITTED | §6.1 adm. → §6.3 root | West Papua 0.100%, a successor row of the old Indonesia (CENSUS L869). | confirmed by all three |
| L67 | ADMITTED | §6.1 adm. → §6.3 root | Aceh 0.096%, a successor row of the old Indonesia (CENSUS L869). | confirmed by all three |
| L68 | ADMITTED | §6.1 adm. → §6.3 root | Patani 0.095%, a successor row of the old Thailand (CENSUS L870). | confirmed by all three |
| L69 | ADMITTED | §6.1 adm. → §6.3 root | Chechnya 0.056%, a successor row of the old Russia. | confirmed by all three |
| L70 | ADMITTED (share OPEN) | §6.1 adm. → §6.3 root; §6 St | Tibet 0.047%, a piece of the old China (CENSUS L845); its share is open (LOG L1529). | confirmed by all three |
| L71 | ADMITTED | §6.1 adm. → §6.3 root | Kabardino-Balkaria 0.034%, a successor row of the old Russia. | confirmed by all three |
| L72 | ADMITTED | §6.1 adm. → §6.3 root | North Ossetia-Alania 0.026%, a successor row of the old Russia. | confirmed by all three |
| L73 | ADMITTED | §6.1 adm. → §6.3 root | Finland 0.020%, listed among the old Russia's successors (CENSUS L857); that the row carries only those people is a seed (see AM-S1-N15). | confirmed by all three |
| L74 | ADMITTED | §6.1 adm. → §6.3 root | Ingushetia 0.019%, a successor row of the old Russia. | confirmed by all three |
| L75 | ADMITTED | §6.1 adm. → §6.3 root | Karachay-Cherkessia 0.018%, a successor row of the old Russia. | confirmed by all three |
| L76 | ADMITTED | §6.1 adm. → §6.3 root | Tuva 0.013% (152 at Census I, the smallest row), an origin with no cutoff (DR-104 item 2). | confirmed by all three |
| L77 | INERT | — | Blank line. | confirmed by all three |
| L78 | ADMITTED (scope note) | §6 Sc; §6.3 root | Binding as limits, not G8 content: tiers follow mechanically from the shares, the 8 / 3 / 1 weights are retired, shares are identical between censuses, robots follow the human proportions, and shares are rounded (they sum to 100.004%). | confirmed by all three |
| L79 | INERT | — | Blank line. | confirmed by all three |
| L80 | INERT | — | Horizontal rule. | confirmed by all three |
| L81 | INERT | — | Blank line. | confirmed by all three |

**Tally:** 72 lines = 50 ADMITTED (L20, L21, L22, L24, L32-L76, L78) + 3 PARTIAL (L15, L16, L28) + 19 INERT + 0
STRUCK. DO-NOT-FOLLOW applies to two pointers inside L28. Four ADMITTED rows carry an OPEN share (L43, L60, L62,
L70). The tally was recounted by command in Round 3 over all three readers' tables (A and C), and each gave 50 /
3 / 19. One reader's Round 1 summary sentence gave other totals; it withdrew that sentence (section 9).

### AM-S1-F2 The composition region passes §6.1 first and §6.3 second

- **Pass's finding (location):** 00.1 L129 grounds G8 as "PRESENT — richest" at "L15–22, L30–52". The read spec at
  00.1 L223 and L238 admits pass-time "10-87", with an L21 PARTIAL (00.1 L244, L267). The pass's classification
  never saw the current 45-row table or the notes at L28 and L78.
- **Current inputs:** SPEC L10-L81 as tabled in AM-S1-F1. 05 L496 lists census, composition and
  population change as admissible. 05 L728-L729 ratify `Cities/Specs/` and the census by root. The 45 rows sum
  exactly to the L15 and L16 totals in all four columns (command output, all three readers). MAP L2 says the
  composition region "is different text and is NOT mapped here".
- **Re-derived (firm):** no line of L10-L81 is a prior culture-pass conclusion about Davis. Every content line is
  a census attribute, a composition attribute, a method or provenance note, or structure, so every line passes
  §6.1; every line then passes §6.3 by root, and none declares draft or suggestion status. Nothing is struck. The
  use limits that remain (the PARTIAL clauses, the DO-NOT-FOLLOW pointers and the OPEN shares) come from 05 §6's
  Scoped and Stable properties and from the rulings, not from §6.1 or §6.3. G8 is present on 45 rows (5 Primary,
  2 Significant, 38 Notable).
- **Why re-derivation was needed [K]:** the pass's classification was a content judgment on pass-time text.
  Admissibility is a property of content (05 L503), and a file is admissible only if every section of it is (05
  L514). Carrying the old admission over to text it never saw would be admission by address.
- **Pass locations affected:** 00.1 L129 (G8's ground needs current numbers; docket AM-S1-D11); 00.1
  L244 and L267 (the L21 strike retires; AM-S1-F3); 00.1 L223, L238 and L241 (numbering;
  AM-S1-F8).
- **What stays:** G8 "PRESENT — richest" stands, on more rows than before, and still counts toward the rule of
  three.
- **Disposition:** confirmed by all three (A, B, C); K reached the same outcome ("the region is admitted in full").

### AM-S1-F3 The L21 partial strike is retired; the tag at L21 and L38 needs no strike

- **Pass's finding (location):** 00.1 L267 strikes pass-time L21 as PARTIAL for the "only city in its cluster"
  clause, with the survival pointer "tier + figures at **L27, L37**"; 00.1 L244 repeats L21 in the PARTIAL list.
- **Current inputs:** SPEC L21 reads "| Significant | Indonesia, Australia *(founding wave)* |". No "only city" or
  cluster-ranking clause appears anywhere in SPEC L10-L81 (A's capped search returned 0; B, C and K read every
  line). CENSUS L33: "the tag says nothing about when people arrived." DR-88 item 2 (LOG L1555): "(founding wave)"
  "now means a nation named as a founder in the Founding Register, and nothing else." DR-99 item 2 (LOG L1660): the
  tag "means the establishing country named in the Register, not people who arrived in a wave"; DR-99 item 3 maps
  the Register's names onto table rows one to one, Australia to Australia [B]. REGISTER L59 names Australia for
  Davis, basis "extremely close… comparatively easy access", DR-19. REGISTER L8-L10: specs and census tags point
  to the Register and may not originate or restate a founding claim it does not hold.
- **The survival pointers now misdirect [K]:** on the current file, SPEC L27 is blank and SPEC L37 is Indonesia's
  row, so the pass's pointer sends a reader to a blank line and to another nation's figures. Australia's tier is
  at SPEC L21 and its figures at SPEC L38 (K; B gives the same two lines; C notes the pointers are pass-time
  numbers inside the replaced region and cannot be mapped).
- **Re-derived:**
  - The strike is **retired for lack of a target**; class: killed by evidence (the clause is gone from the
    region). **Firm** for the composition region.
  - Whether the clause moved into a line outside the region is **conditional**. Current L8 was read and does not
    carry it [B]; L109, L113 and L167 changed wording and are unread, so absence from the whole spec is not shown.
  - **Neither current L21 nor current L38 needs a strike (firm).** The tag restates a founder the Register holds,
    and under DR-88 item 2, DR-99 item 2 and CENSUS L33 it works as a pointer to REGISTER L59.
  - **Use limit (firm):** the tag supports only "Australia is the Register's named founder". It never supports
    arrival timing, arrival order, a wave of arrivals, an early cohort, the row's size (5.74%, level with
    Indonesia) or a founding-wave character. The founder's ground is REGISTER L59, on geography and access
    (DR-19), never the tag and never the real station.
  - The retired clause still sits in UEIC L598, outside every read spec (AM-S1-N13).
- **Pass locations affected:** 00.1 L244 (drop L21 from the PARTIAL list); 00.1 L267 (retire the row; tier and
  figures now at SPEC L21 and L38); 00.1 L269's roster (AM-S1-N9); 00.1 L190's founder
  (AM-S1-N7).
- **What stays:** Australia as Davis's founder, now grounded on REGISTER L59.
- **Disposition:** retirement, no new strike and the use limit: confirmed by all three. Strength of the clause's
  absence outside the region: conflict resolved to the narrower reading (A and C wrote the retirement firm
  without a condition; B kept the condition; C withdrew its stronger sentence that the clause "has left the spec").
  Misdirection of the survival pointers: found by one (K).

### AM-S1-F4 L28 and L78 are provenance and scope notes; L28's process numbers are not shares

- **Pass's finding (location):** 00.1 L179-L182 treat pass-time L54 as declaring a "share-weighted model" and
  pass-time L28 as declaring the "de-stacking randomization", with the scope "usable for named portable
  institutions; never readable as measured per-nation counts".
- **Current inputs:** 05 L465 (Scoped): "A pass that reads a source past its own stated limits has committed one
  of the seven recorded developer catches". SPEC L78: "the 8 / 3 / 1 share weights no longer produce the
  figures"; "Percentages are of this city's own human and robot population (identical between censuses), not
  Tepenia-wide. Robot figures apply the same proportions as the human population." SPEC L28 records the rework
  method, the pools "Hong Kong 0.88%, Macau 0.10%, Taiwan 2.92%, Mongolia 0.09%, North Korea 0.36%", the
  multiplier "0.5719 (random 0.55 to 0.65)" and the multiplier "0.5855 (a draw from 0.55 to 0.65, seed
  2026110215)".
- **Re-derived (firm):**
  - L28 and L78 are ADMITTED provenance and scope notes. They bind every later reading as limits under 05's
    Scoped property. They are not G8 content: neither adds an origin, a count or a share the table does not carry.
    The one composition fact in L28 (the old China's pieces in Davis's window: Mongolia, Manchuria, Tibet, East
    Turkestan) repeats rows L57, L60, L62 and L70 and explains why they are present [C].
  - **L28 does not mark its process numbers as unusable; the amendment must [A].** The pool percentages are
    pre-rework inputs: Hong Kong, Macau and North Korea have no rows of their own (CENSUS L846, L847, L851), and
    Taiwan's pool of 2.92% does not reproduce the table's 2.86% from the steps L28 states (2.92 × (1 − 0.0145) =
    2.8777, against 2.8629 from Census I humans; A, recomputed by B). The multipliers, the draw range and the seed
    are mechanism. **None of these is a share, a trend or an in-world event.** L28's list of refill recipients is
    method, never evidence about those communities [C]. Kazakhstan's 1.45% equals L51 and is read from L51 [A].
  - L78's tier rule was checked by command [B, C]: among the rows at 4.5% or more, the largest ratio gap is
    Korea → Indonesia at 1.4547, so Primary holds 5 rows and Significant the 2 remaining rows at 4.5% or more.
- **Pass locations affected:** 00.1 L179-L182 (the "L54" and "L28" citations and two of the clauses;
  AM-S1-K5, AM-S1-K4, AM-S1-K6).
- **What stays:** the principle that the composition is read within its own stated limits; the "identical between
  censuses" limit, now at L78.
- **Disposition:** confirmed by all three; K reached the same reading.

### AM-S1-F5 L28's "the share every city in its time-zone window receives" is a legal statement of method

- **Pass's finding (location):** 00.1 L272 strikes pass-time L117's "unusual in Tepenia" as "the only strike whose
  violation is an *implicit* normal naming no city".
- **Current inputs:** SPEC L28: "Kazakhstan was added on 2026-11-02 (`DR-93`) at 1.45%, the share every city in
  its time-zone window receives; every other row shrank in proportion." CENSUS L881 places that pool "within three
  zones of UTC+5" (the rest of the line names other locations: not used).
- **Re-derived (firm):** a legal statement of method, not an implicit normal. "Unusual in Tepenia" places Davis
  against a norm; this clause reports how Davis's own 1.45% was produced, by a placement rule keyed to Davis's
  own time-zone window. Under the one-sentence test, the statement that Davis's Kazakhstan row is 1.45%, set by a
  placement rule and not drawn for Davis, survives as a fact about Davis's data.
  - **Use:** admitted only as a limit. The 1.45% carries no Davis-specific signal, so no finding reads it as a
    measured or drawn quantity. DR-104 item 1 bars only same-tier gaps; this clause is the only line that tells a
    headcount reading the size is a placement constant [C].
  - **Barred use:** the clause may never ground a statement that Davis is typical, sits at a level with
    neighbors, or resembles any place; that would turn method into a normal.
  - **Guard [B, adopted by A]:** the limit never lowers L51's standing as an origin reasoned by headcount (DR-104
    item 2).
  - That REGISTER L59's "+5" cell names Davis's UTC+5 window is an inference: the Register's header row is not
    admitted, and CENSUS L881 and UEIC L598 corroborate it (C, Round 3).
- **Pass locations affected:** none; the clause is new.
- **What stays:** L51 as an origin at its headcount (8,587 humans and 9,010 robots at Census I).
- **Disposition:** confirmed by all three after Round 3. B's Round 1 wording ("read but not used", conditional) was
  withdrawn in B's Round 3 reply in favor of A's and C's firm reading.

### AM-S1-F6 L28's two pointers are DO-NOT-FOLLOW, as pass-time L91 was

- **Pass's finding (location):** 00.1 L271: pass-time L91 is DO-NOT-FOLLOW, "a legal line pointing at a 37-city
  comparison", target tiered WITHHELD.
- **Current inputs:** SPEC L28: "Method, every run and the research: `Sinian_Federation_Split_Scratch_2026-11-01/`
  (file `12_Rebalance_Run4.md`). The table that stood here before is in git commit `593510ab`." 05 L730: anything
  beyond the enumerated roots is "NOT YET ENUMERATED. The developer extends this list; a pass may not." ALR L28
  (DR-102): "the history stays in git". LOG L1530 records that the scratch folder holds the scripts and every
  run. CENSUS L884 points at the same folder.
- **Re-derived (firm):** both pointers are DO-NOT-FOLLOW; the line is read and the targets are never opened.
  - The scratch folder is not an enumerated ratified root, so it is unratified and demoted (05 §6.3). Its name
    marks it as working material. It holds the runs for other locations, so opening it would read other
    locations' figures, a comparison surface. It adds nothing a pass may use that the spec does not carry.
  - Commit `593510ab` holds the superseded table, the pass-time input whose L21 clause was struck. It fails 05's
    Stable property, and under DR-102 that history stays in git and is not an input.
  - CENSUS L884's pointer gets the same verdict.
  - The grounds differ from L91's (an unratified root and a superseded state, rather than a comparison), but the
    verdict is the same [B].
- **Pass locations affected:** 00.1 L246 (the DO-NOT-FOLLOW list should name current L115 and these two pointers).
- **What stays:** nothing is lost; L28's stated method and L78's rules carry all a Davis pass may use.
- **Disposition:** confirmed by all three.

### AM-S1-F7 The L15-L16 revision notes are process notes; the change they record is authoring arithmetic

- **Pass's finding (location):** 00.1 L108-L112: "The Census I → II change remains admissible `G8` material", a
  real in-world relocation and not an authoring artifact, verified by Davis's absence from the 2026-09-05 −10%
  redistribution set.
- **Current inputs:** SPEC L15's first parenthetical records a relocation of 2026-11-02 under DR-90 from another
  location (another location: not used), with former figures 575,738 humans / 606,493 robots / 1,182,231. Its
  second records 563,599 / 594,715 / 1,158,314 and "census updated 2026-10-28, `DR-68`". SPEC L16 has the same
  form; its second parenthetical carries no date or ruling. LOG L1575 (DR-90): "Arithmetic, NOT a migration." and
  national totals unchanged; DR-90 names its method as a population scenario's method, citing DR-68 and DR-69 (the
  scenario's location: not used). LOG L1339 (DR-68) adopts the scenario numbers; LOG L1341 records that "nothing
  in the census has been touched".
- **Re-derived:**
  - **Firm:** the parentheticals are read-but-not-used process notes; they hold superseded values, one names
    another location, and an amendment states the current fact (DR-102).
  - **Firm:** the DR-90 step is an authoring redistribution by its own ruling text, not an in-world flow into
    Davis. It is not relation, not G4 and not G8 flow material.
  - **Conditional, read as arithmetic PROVISIONALLY:** the DR-68 step. The admitted DR-68 lines say neither
    "arithmetic" nor "migration"; DR-90 calls its own method DR-68's. Reading the DR-68 step as an in-world
    inflow is killed for want of an admitted line [B]. Settling it needs DR-69 and the scenario file
    (AM-S1-Q4, AM-S1-R6).
  - **Firm:** the in-world Census I → II event, the orbital relocation, remains G8 material at the current
    figures, which are canon; DR-4 still fixes which figure the frame declares. But the pass's verification clause
    is true of the 2026-09-05 set only: Davis is a recipient in the DR-90 step (firm) and, per its own spec note,
    in the DR-68 step. The figures' magnitudes are therefore partly authoring arithmetic
    (AM-S1-N4).
  - The L15 attribution to DR-68 and the untagged L16 clause are source defects (AM-S1-N17).
- **Pass locations affected:** 00.1 L108-L112 (a qualifier; AM-S1-D6); 00.1 L64 and
  L70-L71 (superseded figures; AM-S1-K11).
- **What stays:** the pass's statement that DR-4 fixes which figure the frame declares without deleting the event.
- **Disposition:** confirmed by all three (the not-used status, DR-90 firm, DR-68 conditional).

### AM-S1-F8 The read spec on the current numbering, the +24 shift, and which statement about L176 is right

- **Pass's finding (location):** 00.1 L223 and L238 give `1-3,5-8,10-87,90-120,122-134,143,148,153-155,176,178-179`
  as 137 lines; L225-L226 say it "contains ZERO struck lines" and is the LRANGE value; L243 admits "L176 (premise
  only)"; L286 excludes "`Specs/Davis.md` L159–166, L168–171, L173–176, L181–199, L204–205".
- **Current inputs:** MAP L3: "pass-time L58-L236 equal current L82-L260 at +24 for 176 of 179 lines", with the
  wording of pass-time L85, L89 and L143 (now L109, L113, L167) changed, and L8 changed at the same number. MAP
  L31 gives the mapping. MAP L4: "Whether those two spec versions differ in line numbering before L58 or after is
  NOT verified here." LOG L1530 (DR-85): "line citations remapped with `Tools/remap_line_citations.py` base
  `593510ab` in the pass folders". 00.1a L232 records the spec as 181 lines on its date.
- **Re-derived:**
  - **The string (firm):** `1-3,5-8,10-111,114-144,146-158,167,172,177-179,200,202-203`, **161 lines**. It
    expands with no duplicates, sorted; it equals L1-158 MINUS {4, 9, 112, 113, 145} ∪ {167, 172, 177, 178, 179,
    200, 202, 203}; it equals the mechanical map of the pass-time string with the current region L10-L81 put in;
    it contains zero mapped struck lines and none of L286's excluded lines (read in current numbering). The bound
    is 166; LINES counts the admitted set, 161. The LRANGE value is the same string. Verified by command by A, B
    and C in Round 1, and recomputed by all three in Round 3.
  - **The +24 holds past the table (firm, on MAP):** pass-time L58-L236 map to current L82-L260, and the current
    file is 260 lines, 236 + 24. "205" is the highest number the contract cites; in current numbering it is
    pass-time L181, the end of the spec as it stood at the contract's date. Current L206-L260 are named nowhere in
    the contract (AM-S1-N12). K could not verify the shift past L81 from its own list; MAP now
    supplies it, as a mechanical comparison by the orchestrator, not a reader's reading.
  - **L176 (firm on the arithmetic; conditional on the cause):** both statements are right in their own
    numbering, and they name different lines. 00.1 L243 is pass-time: pass-time L176 is current L200 (identical
    text), admitted for its premise only. 00.1 L286 is current: its "L173–176" is pass-time L149-L152, never
    admitted. Read in current numbering, L286 overlaps the mapped admits nowhere and covers current L159-L205
    except L180 and L201 (pass-time L156 and L177). Read in pass-time numbering, it would overlap the admitted set
    at L176 and leave most of pass-time L135-L158 in neither list, which is incoherent. No line is both admitted
    and excluded. The defect is a file written in two numberings without a marker (AM-S1-N2). In
    the numbering a reader executes against the live file, current L176 is excluded and the premise-only line is
    current L200. That DR-85's remap script caused the mix is inferred, not checked in git (AM-S1-R4).
  - **Operating rule [A]:** under either reading, current L173-L176 are excluded and current L200 is admitted for
    its premise only, so the operating read spec is the same.
- **Pass locations affected:** 00.1 L223, L225-L226, L228, L238 and L241-L246 (numbering and counts); 00.1 L286
  (its numbering must be declared); 00.1 L251's "adjudicated line by line" cannot be confirmed for current L180
  and L201 and does not reach current L206-L260 [A].
- **What stays:** every pass-time strike and partial carries to its mapped line (AM-S1-K1); the
  pass-time string stays correct for the pass-completion spec, as a historical artifact [C].
- **Disposition:** confirmed by all three. A's Round 1 wording ("L243 is right; L286 is in the other numbering")
  was replaced in A's Round 3 reply by B's and C's wording, which is used here.

### AM-S1-F9 Where the census rows are now, and what CENSUS L392-L398 hold

- **Pass's finding (location):** 00.1 L248 admits the census at "392-398,496,613" (9 lines); 00.1 L64-L65 cite
  census L496 and L613.
- **Current inputs:** CENSUS L390 is Davis's block heading, L391 is blank, and L392-L396 are Davis's five-line tier
  table (header, separator, Primary, Significant, Notable), byte-identical to SPEC L18-L22 (`diff` by A, B and C).
  CENSUS L397-L398 are outside every reader's admitted range. Orchestrator result 3 places Davis's census rows at
  CENSUS L506 (Census I) and L650 (Census II); no reader read those lines. CENSUS L33 now defines the tag. CENSUS
  Section E (to L884, its last content line [B]) is the name key L28 points to.
- **Re-derived:**
  - **Firm:** CENSUS L392-L396 hold Davis's tier table, under the heading at L390.
  - **Not known:** what CENSUS L397-L398 hold. The tier table is complete at L396, where its last tier appears, so
    L397-L398 are not part of it (structural inference). Whose material they carry has no admitted ground and is
    not stated here.
  - **Conditional:** Davis's census rows are at L506 and L650, on the orchestrator's result only.
  - **Census read spec (all three): `33,390-396,506,650` = 10 lines.** L33 is added because the tag's meaning now
    governs SPEC L21 and L38. That the pass's seven-line span 392-398 now sits at 390-396 is an inference from its
    shape and needs a git comparison [C; B noted it fits the pass's "9 lines"].
  - **Conditional:** the old census spec run today would read L496 and L613, which are no longer Davis's rows
    [B, K]; this is a contamination route of the same kind as AM-S1-N1.
- **Pass locations affected:** 00.1 L248; 00.1 L64-L65 (AM-S1-D19, AM-S1-D4).
- **What stays:** the census remains a ratified root (05 L729).
- **Disposition:** the tier-table location and the 10-line spec: confirmed by all three. L397-L398: conflict
  resolved to the narrower reading (A wrote that they are not Davis's tier block and probably another location's
  material; B and C wrote that what they hold is unknown).

### AM-S1-F10 The region's use spec under DR-104 items 1 and 2, and what survives of §3.3's limit

- **Pass's finding (location):** 00.1 L179-L182 (quoted in AM-S1-F4): a share-weighted model, a
  de-stacking randomization, and the scope "usable for named portable institutions; never readable as measured
  per-nation counts".
- **Current inputs:** DR-104 item 1 (LOG L1703): "per-nation figures are weights for deriving a location
  (headcounts in the world), and no finding rests on a gap between two nations of the same tier; the "randomized
  for realism" ground now applies only to the Sinian Federation and Manchuria rows." DR-104 item 2 (LOG L1703):
  "All 45 rows of Davis's composition are origins; Phase 2 reasons by headcount, with no cutoff." SPEC L78 and
  L28 as quoted in AM-S1-F4. LOG L1529 (the four rows left open).
- **Re-derived use spec (PROPOSED; firm, except the open-row rule, which is PROVISIONAL):**
  - The per-nation figures are weights for deriving Davis, read as headcounts in the world (DR-104 item 1).
    Reason by each row's headcount, with the Census I counts as the governing figure (DR-4) [C].
  - All 45 rows are origins, with no cutoff (DR-104 item 2). The 10 rows under 0.1% count fully, down to Tuva's
    152 people at Census I. Every row counts and no row is the city: the Primary tier together is 46.39% of the
    city, the largest row 10.42%, and the Register-founder row 5.74% [A]. A minority row is never the whole.
  - No finding rests on a gap between two nations of the same tier (DR-104 item 1): not Indonesia against
    Australia (37 people apart at Census I), not any two Primary rows, not any ordering inside the 38 Notable rows.
  - Randomization sits in two rows only: the Sinian Federation (L33, ×0.5719) and Manchuria (L57, ×0.5855). No
    finding rests on their exact sizes. **The order of the two largest rows is itself a product of the Sinian
    Federation draw** [A, C]: on L28's figures, a draw above about 0.606 in the stated 0.55 to 0.65 range would
    have put the Sinian Federation first (A's approximation, which ignores the Kazakhstan step and the Manchuria
    refill; tie at 0.6058, recomputed by B and C). So "Japan is Davis's largest row" must never carry a finding
    (conditional arithmetic; the same-tier bar already covers it).
  - Shares are identical between the censuses, and robot figures follow the human proportions (L78). So there is
    **no per-nation retention finding and no per-nation robot-to-human finding**; both are flat by construction
    (per-row human retention 0.7666 to 0.7767, per-row Census I robot-to-human ratio 1.0464 to 1.0583, spread only
    by the rounding of small rows [A; recomputed by C]). Every retention or robot-share finding is city-level,
    from L15-L16.
  - Shares are rounded and sum to 100.004% (L78); the four counted columns sum exactly to the L15 and L16 totals.
  - Tier labels follow the shares mechanically (L78; DR-85 item 7) and the 8 / 3 / 1 weights are retired, so a
    tier label is never evidence beyond the shares, and no finding rests on a tier weight.
  - "(founding wave)" means the Register founder only (AM-S1-F3). L28's process numbers are never
    shares, and Kazakhstan's 1.45% is a placement constant (AM-S1-F4, AM-S1-F5). The
    L15-L16 parentheticals are not used (AM-S1-F7).
  - **PROVISIONAL:** the rows for Taiwan (L43), Mongolia (L60), East Turkestan (L62) and Tibet (L70) are present,
    but their exact shares and headcounts are OPEN, and no finding depends on them (AM-S1-Q5).
  - Composition names the stock; time, place, separation, struggles, goals and habits produce the culture. No row
    licenses a national stereotype or a source culture carried over intact [B, C].
- **What survives of §3.3's limit:**
  - "identical across both censuses by construction" **survives**, now grounded on L78 (firm; the per-column
    shares agree to within 0.0053 points [B]).
  - "share-weighted model" is **killed by evidence** (AM-S1-K4).
  - The "L54" and "L28" citations and the randomization clause: AM-S1-K5 and
    AM-S1-K6.
  - "never readable as measured per-nation counts" is **narrowed** (AM-S1-K7).
  - "usable for named portable institutions" is **superseded and widened** (AM-S1-K8).
- **Pass locations affected:** 00.1 L179-L182 (replace with this use spec; AM-S1-D14); 00.1 L164-L165
  (the sums; AM-S1-D12).
- **What stays:** §3.3's core move, that the composition is used under its own stated limits.
- **Disposition:** the use spec's core rules: confirmed by all three. The draw-dependent order: found by two (A,
  C). The Census I governing count: found by one (C). The stock-not-culture rule: found by two (B, C). The tier and
  share sums cited with a reader in brackets are single-reader figures, recomputed in Round 3.

### AM-S1-F11 Whether the region meets 05's Stable property while DR-85's question stays open

- **Pass's finding (location):** the pass treated its composition block as a stable input (00.1 L129, L164) [C].
- **Current inputs:** 05 L463: "Will this still say the same thing next month? An input still under active debate
  is a *reserved decision*, not an input". DR-85, not decided (LOG L1529): "whether China's four pieces and Taiwan
  decline too". CENSUS L877: "Mongolia, East Turkestan, Tibet and Taiwan were not reduced." SPEC L28: "City totals
  in all four columns are unchanged." SPEC L15 and L16 record two changes to Davis's totals (2026-10-28 and
  2026-11-02).
- **Re-derived (partly; conditional where marked):**
  - **Stable (firm):** the city totals in all four columns under the rework (L28); the membership of all 45 rows
    (DR-104 item 2).
  - **Stable (conditional):** the tier boundaries. B tested draws of 0.55 and 0.65 with the freed points going
    either to the rows at 4.5% or more outside Primary or to all 41 other rows in proportion; every scenario keeps
    5 Primary and 2 Significant rows, and Taiwan stays Notable (1.57% to 1.86%). C tested the four rows removed
    entirely: the largest ratio gap stays Korea → Indonesia (1.104, against 1.096 for United Kingdom → Germany).
    It stays conditional because no ruling sets the refill rule for the four open rows.
  - **Not stable:** the exact shares and headcounts of Taiwan (2.86%, 34,653 at Census I), Mongolia (0.40%,
    4,800), East Turkestan (0.34%, 4,055) and Tibet (0.047%, 572), together 3.647% and 44,080 people [C;
    recomputed by A and B]. Under 05 L463 these are a reserved decision, not an input. The shares of whichever
    rows would receive freed points would also move (up to about 1.64 points in all; under B's first scenario,
    Indonesia and Australia each reach up to 6.56%) [B].
  - **Four rows, not five:** Manchuria was already reduced (CENSUS L877) and is settled as a randomized row. K's
    question named the five rows DR-85 once covered and noted that only Manchuria was reduced.
  - **Exposure [B]:** any finding that rests on the Significant tier's combined share (11.48% now) is exposed to
    the open question and must be marked conditional.
  - **Change history:** Davis's totals changed twice in six days by authoring redistribution [A]; the block has
    been rewritten in at least four dated operations since the pass [K]. Nothing in the admitted lines schedules a
    further change for Davis, and none is ruled out [A].
  - With the PROVISIONAL answer to the first check's question (AM-S1-Q5), the region is usable now.
- **Pass locations affected:** none false; the contract predates the question [C].
- **What stays:** the block as the input.
- **Disposition:** partly stable, four open rows, tiers conditional: confirmed by all three. The Significant-tier
  exposure: found by one (B). The change history: found by one (A) and found by one (K), stated as union.

### AM-S1-F12 What the contract's banner may truthfully claim after the repair

- **Pass's statement (location):** 00.1 L5: "VALID — written on verified unanimous consensus". 00.1 L9-L10: "15 of
  15". 00.1 L11: "Nothing below rests on a single reader's claim to have read something." 00.1 L16-L17: the
  runbook's Step −1 at "L2390–2414" and 05 at "811 lines, in full". 00.1 L19-L21: the binding rulings folded in
  are DR-1, DR-3, DR-4 and 00.1a.
- **Current inputs:** ALR L27 (DR-101): "A finished pass's files are never edited." ALR L28 (DR-102): "An amendment
  note states the current fact with its source address". ALR L29 (DR-74): "Each amendment piece runs with three
  readers and the usual rounds". ALR rule 3: notices go at the end of a file, and only where a ruling permits; ALR
  L30 (DR-116 item 2): a pointer line is a pass-file edit applied only with the dockets [B]. The runbook's Step −1
  heading is now at L2429 (all three read it). 05 is now 823 lines (`wc -l`, all three). LOG L1530 records the
  citation remap.
- **Re-derived (conditional: it waits on the acceptance of this merge and on AM-S1-Q1):** the
  banner is not edited (DR-101). The amendment note may truthfully state:
  - The VALID verdict and its "15 of 15" are true of the 2026-09-13 run against the inputs as they then stood;
    their three-reader record is 00.1b, which is not re-verified here [B]. They are not a claim about today's spec,
    census, runbook or 05.
  - PROCEED stands. Even without G3 the pass has five countable generators (G2, G4, G5, G7, G8) against a
    threshold of three (00.1 L118-L129) [C; A adopted this in Round 3].
  - The composition region was replaced on 2026-11-02 (DR-85) and is re-classified by amendment piece S1 with
    three readers, as DR-74 requires (AM-S1-N5). "Nothing rests on a single reader's claim" holds
    for the region once this merge is accepted.
  - The mapped read spec rests on one mechanical comparison by the orchestrator (MAP), checked by S1's readers for
    internal consistency; no reader read the spec past L81 [A; B adopted this in Round 3].
  - The read spec published at 00.1 L223 and L238 is in pass-time numbering and must not be run on the current
    file; the current read spec is the 161-line string (AM-S1-F8).
  - Current L109 and L167 (admitted) and L113 (struck) changed wording, and no reader has classified their current
    text; current L8 is re-classified PARTIAL by S1 (AM-S1-N3).
  - Some line numbers in 00.1 and 00.1a were changed by a script on 2026-11-02 (LOG L1530), not by readers
    (AM-S1-N2).
  - The census citations L496, L613 and 392-398 are stale (AM-S1-F9).
  - Governing now: the runbook's Step −1 from L2429 (its end beyond L2454 is unverified [C]); 05 at 823 lines.
  - Rulings that now bear on the contract (union of the three lists): DR-19, DR-68 (provisionally), DR-74, DR-85,
    DR-88 item 2, DR-90, DR-93, DR-94, DR-99 items 2 and 3, DR-104 items 1 and 2, DR-105 item 5. DR-93 and DR-94
    are seen here only through SPEC L28 and CENSUS L877 and L881 [A].
- **The banner may NOT claim:** "137 lines"; zero struck lines for the old string run on today's file (it reads
  current L112 and L113); "verified mechanically" as a description of the read spec applied to the live file;
  "nothing rests on a single reader's claim" for L109, L113 and L167 as now worded, or for numbers a script changed
  [C]; the pass-time G8 arithmetic [B, C].
- **Pass locations affected:** 00.1 L5-L11 (a qualifier), L16-L17 (stale addresses), L19-L21 (incomplete ruling
  list); docket AM-S1-D1, AM-S1-D2, AM-S1-D3.
- **What stays:** VALID and PROCEED as the verdict of their date. Nothing in S1 touches Tier 0 presence, the
  generator count or G8's presence [A].
- **Disposition:** confirmed by all three. The single-reader statements carry their finders in brackets.

## 2. Killed or narrowed findings (class each: killed by evidence / killed for want of an admitted line)

### AM-S1-K1 The mapped read spec: the contract's strikes, partials and pointers carried to current numbering

A strike follows its text. Where MAP says the wording changed, the strike is kept and the change is reported,
because no reader may read a struck line to re-classify it.

| pass-time (contract numbers) | current | text per MAP | status carried |
|---|---|---|---|
| 1-3 | 1-3 | identical | admitted; L3's operator parenthetical is a coordinate only (AM-S1-N8) |
| 4 | 4 | identical | FULL strike kept (00.1 L265) |
| 5-8 | 5-8 | L8 differs | admitted; L8 re-classified PARTIAL by S1 (AM-S1-N3) |
| 9 | 9 | identical | NULL/OPEN kept (00.1 L266) |
| 10-12 | 10-12 | identical | INERT |
| 13-57 (the composition region) | 13-81 | replaced; not mapped | classified in AM-S1-F1; the pass-time L21 PARTIAL is retired |
| 58-87 | 82-111 | identical except 85 → 109 (differs) | admitted; L84 and L86 PARTIAL (from L60, L62); L109 carried with its use held (AM-S1-N6) |
| 88-89 | 112-113 | 113 differs | FULL strike kept on both; the change at L113 is reported, not re-classified |
| 90-120 | 114-144 | identical | admitted; L115 DO-NOT-FOLLOW (from L91); L141 and L144 PARTIAL (from L117, L120) |
| 121 | 145 | identical | FULL strike kept |
| 122-134 | 146-158 | identical | admitted; L151 and L153 KEEP (from L127, L129) |
| 143 | 167 | differs | admitted; PARTIAL strike kept (the "in a way no other city can match" clause and the four-name roster, 00.1 L277-L278); its use is held until re-classified |
| 148 | 172 | identical | admitted |
| 153-155 | 177-179 | identical | admitted |
| 176 | 200 | identical | premise only (00.1 L243) |
| 178 | 202 | identical | first clause only |
| 179 | 203 | identical | premise only |
| 156, 177 | 180, 201 | identical | in neither of the contract's lists; not read |
| 182-236 | 206-260 | identical | never ruled on by the contract; not read |

```
Specs/Davis.md   READ SPEC, current numbering (PROPOSED, 2026-11-09):
                 1-3,5-8,10-111,114-144,146-158,167,172,177-179,200,202-203      = 161 lines (bound 166)
                 Bounds + strikes, for human reading only:
                 L1-158 MINUS {4, 9, 112, 113, 145}
                 ∪ L167 · L172 · L177 · L178 · L179
                 ∪ L200 (premise only) · L202 (first clause only) · L203 (premise only)
                 PARTIAL (line read; named clauses not used): L8 · L15 · L16 · L28 · L84 · L86 · L141 · L144 · L167
                 DO-NOT-FOLLOW: L115 · the two pointers in L28
                 Wording changed after adjudication: L8 (re-classified, S1) · L109 (admitted, use held)
                                                     · L113 (struck, kept) · L167 (partial strike kept, use held)
                 Never classified, outside the read spec: L180 · L201 · L206-260
Official_Population_Census.md   33,390-396,506,650                                = 10 lines (506, 650: orchestrator only)
```

- **Strict alternative [C]:** if the developer holds the two changed admitted lines out until they are re-read,
  the string is `1-3,5-8,10-108,110-111,114-144,146-158,172,177-179,200,202-203` (159 lines; it equals the mapped
  set minus L109 and L167, recomputed by A and B). It drops G3's only line (AM-S1-Q1).
- **Other pointers in 00.1 carried to current numbering [A]** (text identical by MAP unless marked): §2 L63 "L60"
  → L84; §3 L123 "L60; L70–91; L93–114" → L84; L94-L115; L117-L138; L124 "L143" → L167 (changed); L125 "L127,
  L129" → L151, L153; L126 "L155" → L179; L128 "L64, L68" → L88, L92; §4.2 L267 "L27, L37" → no mapping (the region
  was replaced; tier and figures now at L21 and L38); L270 "L71, L72, L79, L83, L84" → L95, L96, L103, L107, L108;
  L273 "400 km² at L60" → L84; §7 L329 R-3 "L74" → L98 (identical); L330 R-7 "L85" → L109 (changed) and "L86" →
  L110; L331 R-8 "L111" → L135 (identical). B's and C's dockets give the same R-3, R-7 and R-8 numbers.
- **On L176:** 00.1 L243 is right in pass-time numbering (current L200, premise only); 00.1 L286 is right in
  current numbering (current L176 = pass-time L152, excluded) (AM-S1-F8).
- **Disposition:** the mapped table, the string and its count: confirmed by all three. The strict alternative:
  found by one (C). The full pointer list: found by one (A); the R-3, R-7 and R-8 numbers: confirmed by all three.

### Killed or narrowed

| item | pass statement (location) | class | ground | disposition |
|---|---|---|---|---|
| AM-S1-K2 | The L21 PARTIAL strike and its survival pointer "L27, L37" (00.1 L244, L267) | **killed by evidence** | The clause is in no line of current L10-L81 (AM-S1-F3). The pointer lands on a blank line (L27) and on Indonesia's row (L37) [K]. | confirmed by all three (the strike); found by one, K (the pointer's misdirection) |
| AM-S1-K3 | "137 lines", zero struck lines, the LRANGE value and "(137) … bound (142)" (00.1 L223, L225-L226, L228, L238, L241-L246) | **killed by evidence** for the current file | True only for the pass-completion spec. The current figures are 161 admitted and 166 bound (AM-S1-F8); what the old string does on today's file is AM-S1-N1. | confirmed by all three |
| AM-S1-K4 | "share-weighted model" (00.1 L179) | **killed by evidence** | SPEC L78: "the 8 / 3 / 1 share weights no longer produce the figures". | found by two (B, C); A withdrew its Round 1 claim that it survives; K raised the same contradiction |
| AM-S1-K5 | The citations "L54" and "L28" as the lines that state the limit (00.1 L179-L180) | **killed for want of an admitted line** | The pass-time notes no longer exist at those numbers: current L54 is the Lithuania row and current L28 is the DR-85 rework note. Replaced by current L28 and L78. | conflict resolved to the narrower reading (C, adopted by B in Round 3; A classed the L28 statement as killed by evidence) |
| AM-S1-K6 | "de-stacking randomization" applied to the table (00.1 L180) | **narrowed** by evidence | Randomization now covers two rows only, the Sinian Federation and Manchuria (DR-104 item 1; current L28). | conflict resolved to the narrower reading (B and C narrowed it; A killed it by evidence) |
| AM-S1-K7 | "never readable as measured per-nation counts" (00.1 L182) | **narrowed** by evidence | DR-104 item 1 reads the figures as headcounts in the world for derivation. What survives: the figures are modeled, not measured [A]; no same-tier gap finding; no per-nation retention or robot-ratio finding; no exact-share finding on the two random rows or the four open rows (AM-S1-F10). | conflict resolved to the narrower reading (A and B narrowed it; C wrote "killed by evidence in its main part" while keeping the same survivors) |
| AM-S1-K8 | "usable for named portable institutions" (00.1 L182) | **narrowed** by evidence (superseded and widened) | DR-104 item 2: all 45 rows are origins, reasoned by headcount, with no cutoff. | confirmed by all three |
| AM-S1-K9 | "not an authoring artifact" and the verification against the 2026-09-05 −10% set (00.1 L108-L110) | **narrowed** by evidence | True of that set only. The current figures include the DR-90 step (arithmetic by its own text) and, per SPEC L15, the DR-68 step (AM-S1-F7). The in-world Census I → II event stands. | confirmed by all three |
| AM-S1-K10 | Any in-world inflow into Davis read from SPEC L15-L16 | DR-90 step: **killed by evidence**; DR-68 step: **killed for want of an admitted line** | LOG L1575: "Arithmetic, NOT a migration." No admitted line says people moved in the DR-68 step. | found by one (B); A and C hold the same substance (DR-68 arithmetic, conditional) |
| AM-S1-K11 | Tier 0 "1,158,314 → BAND 5" and the G8 arithmetic (00.1 L64, L70-L71, L164-L172) | figures: **killed by evidence**; band: conditional | Current: Census I 1,210,432; retention 67.54% / 76.88% / 58.63%; spread 18.25 points (AM-S1-N4). Band 5 is neither confirmed nor killed: `01` §2's thresholds are in no reader's list (AM-S1-R3). "Shares sum to 100.00%" narrows to 100.004% within rounding [B, C]. "All four per-nation columns sum exactly" survives [B, C]. "Worst row deviation 0.57 of a person" is **killed for want of an admitted line**, because the contract does not define the metric; the nearest computable metric is at most 2.98 persons (Indonesia) [A]. The majority inversion survives. | figures: confirmed by all three; band: conflict resolved to the narrower reading (B and C: conditional; A: the band's re-derivation killed for want of an admitted line); the 0.57 metric: found by one (A) |
| AM-S1-K12 | The census span "392-398,496,613" and census L496 and L613 (00.1 L248, L64-L65) | **killed by evidence** for the live file | Now `33,390-396,506,650` (AM-S1-F9). | confirmed by all three; K raised the same staleness |
| AM-S1-K13 | "`L8` … was CLEARED ON CONTENT" (00.1 L255-L257) | **narrowed** by evidence | The clearance was given to text that has since changed (MAP L3); current L8 is PARTIAL (AM-S1-N3). | conflict resolved to the narrower reading (A and B narrowed it; C killed it by evidence) |
| AM-S1-K14 | The contract's two statements about L176 (00.1 L243 against L286) | **narrowed** by evidence, to a numbering artifact | Both are right in their own numbering; no line is both admitted and excluded (AM-S1-F8). L243's "L176", read as a current number, is wrong: in current numbering it means L200 [C]. | confirmed by all three |

## 3. New findings

### AM-S1-N1 The published read spec, run on today's file, reads struck and excluded lines

- **Pass's statement (location):** 00.1 L221 heads the string "THE READ SPEC — paste this into `sed`/`awk`. Never
  reconstruct it by hand." 00.1 L231-L234 state the M-224 rule.
- **Current inputs (arithmetic, by command):** run on the current spec, the pass-time string reads current
  L112-L113 (pass-time L88-L89, both FULL-struck; 00.1 L270 gives their grounds) and current L176 (pass-time L152,
  excluded). It misses 27 admitted lines: current L88, L89, L121, L135-L142, L144, L146, L147, L149-L152,
  L156-L158, L167, L172, L177, L200, L202 and L203. G3's only line, L167, is among them. (B and C computed this in
  Round 1; A recomputed it in Round 3.)
- **Re-derived (firm):** the string is still correct for the pass-completion spec, but nothing at 00.1 L221-L238
  names the numbering it was computed in. A reader following the contract's own instruction today would read two
  fully struck lines and one excluded line, and would miss G3's only line. This is the M-224 failure in a new form:
  a numeric spec with no stated numbering frame [C].
- **K's prediction narrowed:** K (working without the map) predicted the old string would read the struck lines
  now at L112, L113 and L145. The arithmetic shows it reads L112 and L113 but not L145, which lies outside the
  string's "122-134" segment.
- **Also true [K]:** the old string's "10-87" segment covers all of current L10-L81, so even run unchanged it
  admits the whole current region and reads no struck line inside it.
- **Proposed addition to the M-224 rule [C; A endorsed it in Round 3]:** a numeric read spec names the commit or
  the line count it was computed against (AM-S1-Q9).
- **Pass locations affected:** 00.1 L221-L238 (a numbering-frame qualifier; AM-S1-D16); any other
  pass file that reuses the string (AM-S1-R8).
- **Disposition:** found by two (B, C); A confirmed it in Round 3. K's L145: conflict resolved to the narrower
  reading. K's point on the region: found by one (K).

### AM-S1-N2 00.1 and 00.1a cite the spec in two numberings, without a marker

- **Current inputs (read directly; whole-file entries):**
  - In 00.1, the citations written exactly as "`Specs/Davis.md` L<n>" with n above 57 are in current numbering:
    L286, L303 and L341. The other citations are pass-time: the lines carrying "L143" are L21, L124, L150, L242,
    L244, L277, L278 and L374, and the string at L223 and L238 and the §4.2 table are pass-time too. 00.1 L62 and
    L95 cite L1, L3 and L4, whose numbers did not change.
  - In 00.1a, the current-numbered citations are at L1, L58, L60, L75, L85, L124, L146 and L251. The pass-time
    "L143" appears at L73, L83, L135, L138, L152, L165, L196, L208, L221, L222, L239 and L255.
  - 00.1a's file name says "L135-181" while its title (L1) says "L159–205"; L251's "L159–205" and L226's
    "L135–181" name the same 44 lines [A]. The coverage table's heading at 00.1a L73 says "`Specs/` L143" while its
    column at L75 says "L167" [K]. 00.1a L232 records the spec as 181 lines, so "L159–205" could not have been
    written at the ruling's date [K].
  - LOG L1530 (DR-85): "line citations remapped with `Tools/remap_line_citations.py` base `593510ab` in the pass
    folders".
- **Re-derived:** **firm** that the two numberings are mixed in both files. **Conditional** that DR-85's remap script
  caused it: the pattern fits (only the exact file-qualified form moved; bare, bolded and colon-separated citations
  did not), and the script ran before DR-101 barred pass-file edits, but no reader checked git
  (AM-S1-R4). A reader of either file cannot tell from a citation which numbering it uses, so the
  amendment note needs a numbering key (AM-S1-Q3). The banner's "nothing rests on a single
  reader's claim" does not cover numbers a script changed [C]. Other Davis pass files probably carry the same split
  [B] (AM-S1-R8).
- **Pass locations affected:** 00.1 L286, L303, L341; 00.1a L1, L58, L60, L75, L85, L124, L146, L251 (current) set
  against the pass-time citations listed above (AM-S1-D28, AM-S1-D25,
  AM-S1-D24).
- **What stays:** both files, unedited (DR-101); a pointer in the amendment note names each citation's frame.
- **Disposition:** confirmed by all three. The complete 00.1a list is B's; A (which omitted L85) and C (which omitted
  L58) each withdrew its list in Round 3. The heading-against-column point at 00.1a L73 and L75: found by one (K).

### AM-S1-N3 Current SPEC L8 changed after the pass and is PARTIAL

- **Pass's finding (location):** 00.1 L255-L257: L8, a Significance field, "was CLEARED ON CONTENT".
- **Current inputs:** MAP L3: L8's text differs at the same number. Current L8 (read by A, B and C) has four parts:
  a clause that Davis shares Australian founding-wave heritage with two other locations of the parent subnet, with
  a parenthetical on a third (other locations: not used); a clause naming the real station's namesake, a real
  mariner, and his voyages; "located in the Vestfold Hills, one of the largest ice-free coastal areas in
  Antarctica"; and "Prydz Bay maritime access".
- **Re-derived (conditional):** current L8 is **PARTIAL**.
  - **Admitted:** the Vestfold Hills clause, as geography and a real-world comparable (legal, as 00.1 L268 ruled
    for pass-time L60), with Davis's climate class left open (AM-S1-N11); and the Prydz Bay access,
    a G5 attribute.
  - **Not used:** the heritage clause and its parenthetical (another location: not used). It fails the relation
    test: deleting the other names leaves only Davis's Australian founder, which REGISTER L59 already supplies.
    "Founding-wave heritage" is read only as "Register founder" (DR-88 item 2; DR-99 item 2). A spec restating
    other locations' founding claims meets REGISTER rule 1 (AM-S1-Q6) [B].
  - **Not used as an in-world input:** the namesake clause. It is the real station's naming history, a site-history
    fact (05 L337-L338, DR-28; REGISTER L11-L12: a real station, the program that ran it and its start year are
    facts about infrastructure). The station-builder is a coordinate only and may never ground the founder.
  - Which clause is new cannot be said: no reader can see the pass-time text of L8 [C].
- **Strength:** conditional. A gave conditional (single-reader until merged); B gave firm for the heritage clause
  and conditional for the namesake clause (the general site-history ruling lies outside its lines); C gave firm.
  The weakest strength after Round 3 governs, and no reply changed it.
- **Pass locations affected:** 00.1 L255-L257 (AM-S1-K13, AM-S1-D20); SPEC L8 as a
  source (AM-S1-D35).
- **What stays:** L8 stays in the read spec.
- **Disposition:** confirmed by all three.

### AM-S1-N4 The redistributions moved the retention spread by arithmetic alone

- **Current inputs:** SPEC L15-L16. The three readers' commands gave identical output:

```
pass-time    CI 1,158,314  CII 781,596  retained 67.48% (humans 77.61%, robots 57.87%)  spread 19.74  robot share 51.34% -> 44.03%
after DR-68  CI 1,182,231  CII 797,443  retained 67.45% (humans 77.38%, robots 58.02%)  spread 19.36  robot share 51.30% -> 44.13%
current      CI 1,210,432  CII 817,475  retained 67.54% (humans 76.88%, robots 58.63%)  spread 18.25  robot share 51.20% -> 44.45%
DR-68 step   CI +23,917 (humans +12,139, robots +11,778); CII +15,847; its own ratio: humans 66.79%, robots 65.71%
DR-90 step   CI +28,201 (humans +14,930, robots +13,271); CII +20,032 (humans +8,570, robots +11,462); its own ratio: humans 57.40%, robots 86.37%
both steps   CI +52,118 = 4.31% of current Census I; Census I grew 4.50% over the pass-time figure
```
  (Summary of the three outputs, not a pasted output; the 4.31% and 4.50% are C's and were recomputed by A and B.)
- **Re-derived (firm, as arithmetic):** the majority still inverts, and the direction stands: robots left at
  higher rates than humans. The pass's question (00.1 L175-L177) still stands and needs no second place to ask or
  answer. The DR-90 step's own ratio runs the other way (robots 86.37%, humans 57.40%), and the two steps together
  narrowed the spread by 1.49 points with no in-world cause.
- **Use rule (PROPOSED):** a finding may rest on the direction and on the inversion of the majority, never on the
  spread's exact size or on any difference between the pass-time and current figures. This is a reader rule, not a
  ruling, so the developer may relax it [C].
- **Pass locations affected:** 00.1 L64, L70-L71 and L164-L172 (figures; AM-S1-K11); 00.1 L174-L177
  (stands, with the magnitude qualifier; AM-S1-D13).
- **Disposition:** confirmed by all three. C withdrew its softer Round 1 wording (that a finding "should say" part
  of the size is arithmetic) in favor of A's and B's rule.

### AM-S1-N5 The three-reader question is already answered by a standing ruling

- **The first check's question:** must this region's re-derivation run under three readers, or may it be
  single-reader with the banner amended? It recommended three readers, PROVISIONALLY.
- **Current inputs:** ALR L29 (DR-74): "Each amendment piece runs with three readers and the usual rounds".
- **Re-derived (firm, ruling text):** three readers for an amendment piece is a standing rule, not a provisional
  choice. The single-reader alternative is not available. This piece is that three-reader run.
- **Disposition:** found by one (A). B and C carried the question as PROVISIONAL in Round 1 and withdrew that
  framing in Round 3.

### AM-S1-N6 Three post-table lines changed wording after the pass; G3 is conditional meanwhile

- **Current inputs:** MAP L3: the wording of pass-time L85, L89 and L143 (now L109, L113 and L167) differs. DR-88
  item 1 (LOG L1555): "15 other superlatives and named comparisons rewritten in place (no line added or removed)",
  across about 40 spec files (LOG L1557). Pass-time L89 was struck as a corpus superlative, and pass-time L143
  carried "in a way no other city can match"; both are DR-88 item 1's kind of target, so the changes are probably
  DR-88 rewrites (conditional) [B, C]. DR-104 item 4 (LOG L1703): "the numbers in use are 28 mm staying and 38%".
- **Re-derived:**
  - **L113** (pass-time L89, a FULL strike): the strike follows its text and is kept; the change is reported.
    Whether the strike still has a target needs a classification-only reader (AM-S1-Q1).
  - **L167** (pass-time L143, admitted with a PARTIAL strike; G3's only line, 00.1 L374): carried in the read spec
    with the strike kept, and **its use is held** until a reader admitted to it classifies the new text. **G3 is
    conditional** until then.
  - **L109** (pass-time L85, admitted; R-7's line): carried, and it **grounds nothing** until classified. DR-104
    item 4's "38%" is consistent with R-7's computed 38.5%, but whether L109 now carries it is unseen.
  - **PROCEED does not depend on G3:** G2, G4, G5, G7 and G8 make five countable generators against a threshold of
    three (00.1 L118-L129) [C]. If L167 no longer carries its statement, the count drops from six to five [B].
- **Pass locations affected:** 00.1 L124 and L150-L152 (G3 at "L143"), L277-L280, L330 (R-7) and L374-L376 ("G3
  rests on one line") [C]; docket AM-S1-D9, AM-S1-D27, AM-S1-D23.
- **Disposition:** the three lines and the strikes kept: confirmed by all three. The probable cause: found by two
  (B, C); A accepted it as conditional in Round 3. The interim use of L109 and L167: conflict resolved to the
  narrower reading. A withdrew "L109 read as a climate figure only" and left L167 as a developer question; B
  withdrew "L167 grounds G3 provisionally" and adopted C's "use held"; C held both.

### AM-S1-N7 G4's founder must stand on REGISTER L59, not on spec lines

- **Pass's finding (location):** 00.1 L125 grounds G4 at "L127, L129" (spec lines only); 00.1 L190: "Founding
  population: Australian exiles (L129)".
- **Current inputs:** 05 L96 and L493 (DR-19): founders come from the Founding Register only, stated on the city's
  own geography and access, never on the real station's operator, nation or start year. REGISTER L8-L10: other
  files point to the Register. REGISTER L59 names Australia for Davis.
- **Re-derived (firm):** the "who" (Australia) is grounded on REGISTER L59. The spec line (pass-time L129, now L153)
  may supply the condition (the exiles, the documentary inheritance), not the founder. Add REGISTER L59 to G4's
  ground. Any reading of "founding population" through the tag is barred (DR-99 item 2) [A]. Whether "exiles"
  survives stays open: whether current L153 still supports it, and whether the Register records any exile claim
  (L59's last cell is "—", and the header row is not admitted) (AM-S1-R7) [A, C].
- **Pass locations affected:** 00.1 L125 and L190 (AM-S1-D10).
- **What stays:** Australia as founder; G4 as present.
- **Disposition:** found by two. C stated it firm; A reserved it for another piece in Round 1 and, in Round 3,
  adopted C's firm reading. B adopted it in Round 3.

### AM-S1-N8 The real station's operator is an infrastructure fact only

- **Current inputs:** SPEC L3's parenthetical names the real station's operator [A]. 00.1 L269 keeps "AAD has
  operated Davis Station since 1957" as surviving content of pass-time L62 [C]. REGISTER L11-L12: a real station,
  the program that ran it and its start year are facts about infrastructure. 05 L493 (DR-19).
- **Re-derived (firm):** both survive only as infrastructure facts, a coordinate. They may never ground the
  founder, a population origin or culture. Davis's founder stands on REGISTER L59 alone. The read spec keeps L3
  for position; the amendment should state this use limit, which the contract (written before 05 cited the
  Register's rules) does not [A].
- **Pass locations affected:** 00.1 L269 (AM-S1-D22); SPEC L3 as admitted.
- **Disposition:** found by two (A for SPEC L3; C for 00.1 L269); B adopted both in Round 3.

### AM-S1-N9 The pass's "legal relation" call on the founding-wave roster predates DR-88 and DR-99

- **Pass's finding (location):** 00.1 L269 rules that "the subnet/founding-wave roster is **legal relation**"
  (pass-time L62, now L86; text identical by MAP).
- **Current inputs:** DR-88 item 2 (LOG L1555) and DR-99 item 2 (LOG L1660) later narrowed the tag to the Register
  founder and nothing else. REGISTER rule 1 (L8-L10).
- **Re-derived (conditional):** a roster of other places that share a founder is a shared attribute, not a flow
  [C], and is now a REGISTER rule 1 matter [B]. The current L8 counterpart fails the relation test
  (AM-S1-N3). No reader could read L86, so its classification is requested
  (AM-S1-R1, AM-S1-Q8).
- **Disposition:** confirmed by all three.

### AM-S1-N10 G1's pair is blank until Davis's Phase 10

- **Pass's finding (location):** 00.1 L122 and L133 give G1 as present but lopsided, with the pair "Earth / Earth".
- **Current inputs:** DR-105 item 5 (LOG L1712) and DR-104 (LOG L1704): the symbol pair stays blank until Davis's
  Phase 10 (DR-8, DR-8a).
- **Re-derived (firm, ruling text):** G1 no longer fits the contract. G1 never counted toward the three generators
  (00.1 L144), so the generator count is unchanged. Outside S1's scope; route to the piece that owns Tier 1.
- **Pass locations affected:** 00.1 L122, L133-L138 (AM-S1-D7).
- **Disposition:** found by one (B); A and C confirmed it in Round 3.

### AM-S1-N11 DR-104 item 4 leaves open a class the contract treats as settled

- **Current inputs:** DR-104 item 4 (LOG L1703) leaves open whether Davis is an ice-free oasis or a katabatic
  margin, with "the numbers in use are 28 mm staying and 38%"; DR-105 (LOG L1714) repeats it as not decided [C].
- **Pass statements affected:** 00.1 L196 ("out of the katabatic regime"); 00.1 L268's KEEP of the oasis clause
  and 00.1 L277-L279's "largest ice-free oasis" on L143's authority; 00.1a L268-L271, which rests a configuration
  repair on "out of the katabatic regime" [C].
- **Re-derived (firm that the ruling holds it open):** these need the qualifier "climate class open (DR-104 item
  4)". The ice-free area in current L8's comparable stands as a land-surface fact; the oasis or katabatic-margin
  class may not be asserted. The measured climate figures the contract cites stand [C]. Which downstream findings
  depend on the class is outside S1.
- **Disposition:** confirmed by all three (A reserved it for a G2 piece; B and C stated it). The 00.1a L268-L271
  location: found by one (C); A and B confirmed it in Round 3.

### AM-S1-N12 Current L180, L201 and L206-L260 were never classified by the contract

- **Current inputs:** 00.1a L232 records the spec as 181 lines on its date. 00.1 L286's exclusion list ends at
  pass-time L181 (current L205). MAP L1: the pass-completion spec has 236 lines.
- **Re-derived:** **firm** that current L206-L260 (pass-time L182-L236, 55 lines) appear in neither the read spec
  nor the exclusion list, and that current L180 and L201 (pass-time L156 and L177) are in neither list either. That
  is safe for reading, because the read spec is an allow-list; but these lines are unclassified, not excluded after
  examination (00.1a L191-L192: "A range may be excluded only after each span inside it has been classified").
  **Conditional:** whether the 55 lines were appended after L181 or inserted earlier. If any were inserted before
  L181, the contract's numbers would not equal the pass-completion numbers, and every mapping here would inherit the
  error (MAP L4's caveat) [C] (AM-S1-R5, AM-S1-Q7).
- **Pass locations affected:** 00.1 L284-L286 (AM-S1-D24).
- **Disposition:** confirmed by all three.

### AM-S1-N13 The composition file's Davis entry is superseded derivation and stays out of every read spec

- **Current inputs:** UEIC is not an enumerated ratified root (05 L726-L730), so it is demoted: a prompt or a
  check, never a ground [B]. UEIC L601: "The pool-based table above is the derivation before the rework." UEIC L598
  carries "sets founding wave character", a character claim and a founding claim outside the Register that
  contradicts the tag's current meaning (DR-88 item 2; DR-99 item 2), and a cluster comparison with other locations
  (another location: not used).
- **Re-derived (firm):** neither phrase is an input. The cluster comparison is very likely where the retired L21
  clause came from (conditional) [A]. The file is outside the contract's read spec and should stay out [C]. UEIC
  L601 corroborates the spec's tiers, but its wording "38 nations and smaller successor rows" can be misread as
  more than 38 rows; the 38 include the successor rows [B].
- **Pass locations affected:** none; a guard for later pieces. Source rows AM-S1-D37 and
  AM-S1-D38.
- **Disposition:** confirmed by all three. C withdrew its Round 1 sentence that the struck clause "has left the
  spec" (only the region was read). The L601 wording: found by one (B).

### AM-S1-N14 CENSUS Section E omits the continuing state for four splits Davis carries

- **Current inputs:** CENSUS L843 heads the key "Rows that carry its people now" [B]. Some entries include the
  continuing state (L862 for Germany; L866 for the United Kingdom); others omit it (L858 Ukraine, L869 Indonesia,
  L870 Thailand, L871 Romania). Davis carries Indonesia, Thailand, Romania and Ukraine as rows of their own (SPEC
  L37, L39, L46, L47).
- **Re-derived (conditional; source wording only):** read literally, L858 says the old Ukraine's people are now
  carried only by Russia (core state), which would contradict SPEC L47. Recommended reading: the key lists the rows
  that took a share, and the continuing state keeps its own row.
- **Disposition:** found by one (B); A and C confirmed it in Round 3 (A's L44 ground already used this reading).

### AM-S1-N15 Finland's row origin is a seed

- **Current inputs:** CENSUS L857 lists Finland among the old Russia's successors. The pre-rework UEIC derivation
  for Davis (L599) lists no Finland, but it is superseded (L601).
- **Re-derived (seed):** that Davis's Finland row (L73) carries only people of the old Russia's territory is a
  seed, not a finding [A].
- **Disposition:** found by one (A). B withdrew its stronger Round 1 wording ("here a Russia successor row"); C's
  wording matches A's.

### AM-S1-N16 SPEC L28's small textual defects, and the meaning of "top tier"

- **Current inputs:** SPEC L28 reads "This city: china's pieces in window", with "china's" in lowercase. Its
  Sinian Federation step sent the freed points to six named rows, four of them Primary now, while DR-85 item 3
  (LOG L1528) calls the recipients "rows at 4.5% or more outside the top tier" [K]. The Manchuria step uses the
  same phrase, and L28 says "tiers were relabeled from the new shares" only after that step [B].
- **Re-derived:** the lowercase "china's" is a typo (firm, low weight). Which rows "outside the top tier" meant at
  the Manchuria step is **ambiguous**: before relabeling, the top tier may have been the Sinian Federation alone or
  the five-row Primary [A]. L28 does not name the Manchuria step's recipients. The answer decides which rows a
  future decline of the four open rows would refill (AM-S1-F11).
- **Disposition:** the lowercase name: confirmed by all three. The "top tier" meaning: conflict resolved to the
  narrower reading (A: ambiguous; C: "can only mean the post-relabel Significant rows"; B: either meaning is
  possible; A's Round 3 reply found C's reading more probable but still conditional). The DR-85 tension: found by
  one (K).

### AM-S1-N17 SPEC L15's DR-68 attribution does not match DR-68's own record

- **Current inputs:** SPEC L15: "census updated 2026-10-28, `DR-68`". LOG L1341 records that "nothing in the census
  has been touched", and LOG L1342 lists the census as not edited. LOG L1575 names DR-69 alongside DR-68 for the
  method.
- **Re-derived (conditional):** the ruling that applied the census edit is outside every reader's list; DR-69 is
  the likely one. This is a source-attribution matter, not a Davis fact. SPEC L16's second parenthetical carries no
  date or ruling at all [B].
- **Disposition:** L15: found by two (A, B); C confirmed it in Round 3. L16: found by one (B); A and C confirmed it.

### AM-S1-N18 00.1a L135 cites 05 at numbers that have moved

- **Current inputs:** 00.1a L135 cites "`05` L728–731" for checking §6.1 first and ratification second. In the
  current 05, L726-L731 is the table of ratified roots, and the wording on checking circularity first is at 05
  L738-L741 [K]. 05 has grown from 811 lines (00.1 L17) to 823.
- **Re-derived (firm, an address error):** a pointer in the amendment note gives the current lines.
- **Disposition:** found by one (K).

### AM-S1-N19 Two of the pass's requests cite unchanged lines and remain open as text

- **Current inputs:** 00.1 L329 (R-3, "L74", now current L98) and L331 (R-8, "L111", now current L135) cite lines
  whose text MAP reports identical. 00.1 L330 (R-7, "L85", now current L109) cites a line whose wording changed.
- **Re-derived (conditional on MAP):** the defects R-3 and R-8 name are still present as text [A]. R-7's status is
  unknown (AM-S1-N6).
- **Disposition:** found by one (A); the mapped numbers: confirmed by all three.

## 4. Docket of proposed corrections (a table: location | what is wrong | proposed wording or pointer | confidence | disposition)

All rows are PROPOSED and none is applied. Pass-file rows are carried by the amendment note, never by editing the
pass files (DR-101); an amendment note states the current fact with its source address (DR-102); any pointer line
goes at the end of a file and only when the dockets are applied (ALR rule 3; DR-116 item 2). Source rows are for
the developer. **Confidence** follows the weakest a reader gave; where a reader used firm it is read as high,
and conditional as medium. Proposed wording follows the label Wording and is not a quotation; quotation marks in
this table mark text quoted from a source or a reader.

| item | location | what is wrong | proposed wording or pointer | confidence | disposition |
|---|---|---|---|---|---|
| AM-S1-D1 | 00.1 L5-L11 (banner) | Its claims hold only for the 2026-09-13 inputs and the pass-time numbering. | Pointer to the amendment-note statement in AM-S1-F12, with its list of what the banner may not claim. | medium | confirmed by all three |
| AM-S1-D2 | 00.1 L16-L17 (governing addresses) | The runbook's "L2390–2414" and 05's "811 lines" are stale. | Wording: the runbook's Step −1 now begins at L2429; 05 is now 823 lines. (The section's end beyond L2454 is unverified.) | high (start); end unverified | confirmed by all three |
| AM-S1-D3 | 00.1 L19-L21 (binding rulings) | The list lacks the rulings that now govern the contract. | Wording: add DR-19, DR-68 (provisionally), DR-74, DR-85, DR-88 item 2, DR-90, DR-93, DR-94, DR-99 items 2 and 3, DR-104 items 1 and 2, DR-105 item 5 (AM-S1-F12). | medium | confirmed by all three |
| AM-S1-D4 | 00.1 L62-L65 (Tier 0 table) | The magnitude, its census address and the parent's census addresses are stale; the position cites pass-time L60. | Wording: magnitude 1,210,432 (SPEC L15; census L506 per the orchestrator), band to be confirmed against `01` §2; position L3, L84; parent L5 plus census L506 and L650 (orchestrator; to verify). | medium (figure, addresses); low (band) | confirmed by all three |
| AM-S1-D5 | 00.1 L70-L71 (§2.1 code block) | Census I and II figures are stale. | Wording: Census I 590,668 H / 619,764 R / 1,210,432 (SPEC L15); Census II 454,101 H / 363,374 R / 817,475 (SPEC L16). | high | confirmed by all three |
| AM-S1-D6 | 00.1 L108-L112 (§2.3) | "not an authoring artifact" is true of the 2026-09-05 set only. | Wording: the figures since include the DR-90 redistribution (arithmetic, not a migration: LOG L1575) and, per SPEC L15, the DR-68 one (arithmetic, provisionally); the Census I → II event stays in-world G8 material at the current figures; its direction may ground findings, its magnitude may not. | high (DR-90); medium (DR-68) | confirmed by all three |
| AM-S1-D7 | 00.1 L122, L133-L138 (G1) | DR-105 item 5: the pair is blank until Davis's Phase 10. | Route to the piece that owns Tier 1. Wording: G1's pair is blank until Davis's Phase 10 (DR-105 item 5); it never counted. | high | found by one (B) |
| AM-S1-D8 | 00.1 L123, L126, L128 (G2, G5, G7 citations) | Pass-time numbers. | Wording: G2 at L84; L94-L111 and L114 (L109 wording changed; L112-L113 struck; L115 DO-NOT-FOLLOW); L117-L138. G5 at L6, L7, L179. G7 at L3, L88, L92. | high | G2's form: conflict resolved to the narrower reading (A mapped L94-L115 mechanically; B left out the struck and DO-NOT-FOLLOW lines); G5 and G7: found by two (A, B) |
| AM-S1-D9 | 00.1 L124, L150-L152 (G3 at "L143") | The line is current L167, and its wording changed after the pass. | Wording: current L167; wording changed after the pass; not yet re-read; use held; G3 conditional. | medium | found by two (A mapped the number; C added the note) |
| AM-S1-D10 | 00.1 L125, L190 (G4) | The founder is grounded on spec lines only; the lines are pass-time. | Wording: G4 at L151 and L153, with `Founding_Register.md` L59 (DR-19) as the ground for the founder. Whether "exiles" survives stays open (AM-S1-N7). | high | found by two (A, C) |
| AM-S1-D11 | 00.1 L129 (G8) | The ground "L15–22, L30–52" is pass-time. | Wording: SPEC L15-L16, L20-L22, L32-L76; scope notes L28 and L78. | high | conflict resolved to the narrower reading (C's form; A's and B's forms include inert lines, and A's lists the scope notes as G8 ground although all three hold that they are not G8 content) |
| AM-S1-D12 | 00.1 L164-L172 (§3.3 arithmetic) | Stale figures; "shares sum to 100.00%"; the "worst row deviation 0.57 of a person" metric is undefined. | Wording: columns sum exactly to SPEC L15-L16; shares sum to 100.004%, within rounding (L78); retained 67.54% combined (817,475 / 1,210,432), 76.88% humans (454,101 / 590,668), 58.63% robots (363,374 / 619,764); spread 18.25 points toward humans. Drop the 0.57 metric or define it. | high | confirmed by all three (figures); found by one, A (the 0.57 metric) |
| AM-S1-D13 | 00.1 L174-L177 (the inversion and its question) | Stands; needs the magnitude qualifier. | Wording: stands; robots 51.20% at Census I and 44.45% at Census II; a finding may rest on the direction, not on the spread's size (AM-S1-N4). | high | confirmed by all three |
| AM-S1-D14 | 00.1 L179-L182 (§3.3 scope limit) | The "L54" and "L28" attributions are dead; the limit is superseded by DR-104 items 1 and 2. | Pointer: replace with the use spec in AM-S1-F10. | high | confirmed by all three |
| AM-S1-D15 | 00.1 L196 (G2) | "out of the katabatic regime" is stated as settled. | Wording: add that the climate class is open (DR-104 item 4). | high | confirmed by all three |
| AM-S1-D16 | 00.1 L221-L223, L238 (the read spec string) | Pass-time numbering, with no stated frame; run on the current file it reads L112-L113 and L176 and misses 27 admitted lines. | Wording: pass-completion numbering; current read spec `1-3,5-8,10-111,114-144,146-158,167,172,177-179,200,202-203` (161 lines). | high | confirmed by all three (the string); found by two, B and C (the missing frame and the hazard) |
| AM-S1-D17 | 00.1 L225-L226, L228 (counts and verification) | "137 lines", zero struck lines and "(137) … bound (142)" hold only for the pass-time file. | Wording: 161 lines; expands to exactly L1-158 minus {4, 9, 112, 113, 145} plus {167, 172, 177, 178, 179, 200, 202, 203}; zero carried strikes; this string is the LRANGE value; LINES 161, bound 166; verified 2026-11-09 (S1). | high | confirmed by all three |
| AM-S1-D18 | 00.1 L241-L246 (bounds, partials, DO-NOT-FOLLOW) | Pass-time numbering; L243's "L176" reads wrongly as a current number. | Pointer to AM-S1-K1: PARTIAL L8, L15, L16, L28, L84, L86, L141, L144, L167 (L167 use held); the L21 strike retired (no target); DO-NOT-FOLLOW L115 and L28's two pointers; L243's numbers are pass-time (current L200, L202, L203). | high (numbers); medium (L8) | confirmed by all three |
| AM-S1-D19 | 00.1 L248 (census read spec) | The census rows moved; 397-398 are unread. | Wording: `Official_Population_Census.md` 33,390-396,506,650, 10 lines (L506 and L650 to verify; AM-S1-Q2). | medium | confirmed by all three |
| AM-S1-D20 | 00.1 L255-L257 (L8 cleared on content) | L8's text changed after the clearance. | Wording: current SPEC L8 is PARTIAL (S1); the other-location heritage clause and the real-site namesake clause are not used; the Vestfold Hills comparable and the Prydz Bay access are admitted; the Australian founding is read only as a pointer to `Founding_Register.md` L59. | medium | confirmed by all three |
| AM-S1-D21 | 00.1 L265-L268, L270-L275 (§4.2 table) | Pass-time numbers; the L21 row has no target. | Wording: L4 · L9 · L21 retired (no target) · L84 · L112-L113 (L113 wording changed; strike kept) · L115 · L141 · L144 · L145 · L151 · L153; L270's figure pointers become L95, L96, L103, L107, L108; L273's L60 becomes L84; L268's KEEP is subject to DR-104 item 4. | high | confirmed by all three |
| AM-S1-D22 | 00.1 L269 (pass-time L62, now L86) | The roster's "legal relation" call predates DR-88 and DR-99; the real station's operator and start year are kept without the DR-19 limit. | Wording: re-check the roster at current L86 against REGISTER L59, DR-88 item 2 and DR-99 item 2 (classification only); the operator and start year are an infrastructure fact only (DR-19; 05 L493; REGISTER L11-L12). | medium (roster); high (operator) | confirmed by all three (the roster); found by one, C (the operator line) |
| AM-S1-D23 | 00.1 L277-L280 (L143's authority) | "L143", "L120" and "L60" are pass-time; L167's wording changed; the oasis class is open. | Wording: L167 (wording changed; partial strike kept; use held until re-read), L144, L84; "largest ice-free oasis" is subject to DR-104 item 4. | medium | confirmed by all three |
| AM-S1-D24 | 00.1 L284-L286 (§4.3) | L286 is in current numbering inside a pass-time file; it omits current L180 and L201 and is silent on L206-L260. | Wording: current numbering (pass-time equivalent L135-L142, L144-L147, L149-L152, L157-L175, L180-L181); current L180, L201 and L206-L260 are not admitted, never classified and not read. | medium | confirmed by all three |
| AM-S1-D25 | 00.1 L303, L341 | "L167" is current numbering in an otherwise pass-time file. | Wording: current numbering; current L167 is pass-time L143 (the vision paragraph). | medium | confirmed by all three |
| AM-S1-D26 | 00.1 L329-L331 (R-3, R-7, R-8) | Pass-time numbers; R-7's line changed. | Wording: R-3 at L98 (text unchanged; still open); R-7 at L109 (wording changed; DR-104 item 4 gives 38% in use; status unknown) and L110; R-8 at L135 (text unchanged; still open). | medium | confirmed by all three (numbers); found by one, A (still open) |
| AM-S1-D27 | 00.1 L374-L376 ("G3 rests on one line") | That line has since changed. | Wording: L167 changed after the pass and is not yet re-read; PROCEED survives without G3 (five countable generators). | high | found by two (B, C) |
| AM-S1-D28 | 00.1a L1, L58, L60, L75, L85, L124, L146, L251, against the pass-time citations (L73, L83, L126, L135, L138, L148-L152, L165, L196, L208, L221, L222, L239, L252, L255) | Two numberings mixed without a marker; the file name against the title; L73's heading against L75's column. | Pointer: a numbering key in the amendment note; the eight lines named first are current, and all others are pass-time. | medium | confirmed by all three; found by one, K (L73 against L75) |
| AM-S1-D29 | 00.1a L232 | "181 lines with 135 admissible" describes the spec of 2026-09-11; the file is now 260 lines. | Wording: true of the 2026-09-11 spec; the current spec is 260 lines; current L206-L260 were never classified (AM-S1-N12). | medium | found by one (K) |
| AM-S1-D30 | 00.1a L135 | Cites "`05` L728–731" for the circularity-first rule. | Wording: 05 L738-L741 (05 is now 823 lines). | low (K raised it as a snag and gave no confidence) | found by one (K) |
| AM-S1-D31 | 00.1a L268-L271 | Rests a configuration repair on "out of the katabatic regime". | Wording: add that the climate class is open (DR-104 item 4). | high | found by one (C) |
| AM-S1-D32 | SPEC L15 (source) | Attributes the census update to DR-68, whose entry records the census as not edited. | Cite the ruling that applied the edit (probably DR-69; to be confirmed). | low | found by two (A, B) |
| AM-S1-D33 | SPEC L16 (source) | The second "was" parenthetical has no date or ruling. | Add the same attribution as L15's. | low | found by one (B) |
| AM-S1-D34 | SPEC L28 (source) | Process numbers are not marked as non-shares; "china's" is lowercase; "outside the top tier" is ambiguous at the Manchuria step. | Wording: mark the pool figures, multipliers, ranges and seeds as inputs to the method, not shares; capitalize the name; name the recipients of each step's freed points. | low | confirmed by all three (the lowercase name); found by one, A (the non-share marking); conflict resolved to the narrower reading (the "top tier" wording) |
| AM-S1-D35 | SPEC L8 (source) | Restates other locations' founding heritage (REGISTER rule 1). | Developer check (AM-S1-Q6); a Davis-only form would read: Australian founding (`Founding_Register.md` L59). | low | found by two (A, B) |
| AM-S1-D36 | CENSUS L858, L869, L870, L871 (source) | The key omits the continuing state, unlike L862 and L866. | Add the continuing state to each list, or head the column "rows that took a share" (B's wording). | low | found by one (B) |
| AM-S1-D37 | UEIC L598 (source) | "sets founding wave character" (a character claim and a founding claim outside the Register) and a cluster comparison. | Point to `Founding_Register.md` instead; if the developer wishes, rewrite the comparison as DR-88 did for the specs. | low | confirmed by all three |
| AM-S1-D38 | UEIC L601 (source) | "38 nations and smaller successor rows" reads as more than 38 rows. | Wording: 38 rows, successor rows included. | low | found by one (B) |

## 5. Questions for the developer (PROVISIONAL; each with a recommended answer and what is waiting on it)

The first check's three-reader question is not carried as a question: a standing ruling answers it
(AM-S1-N5). B's Round 1 question on the window clause is answered by the converged reading in
AM-S1-F5 and is not carried either.

### AM-S1-Q1 How are the changed lines L109, L167 and L113 carried until they are classified?

- **Question:** current SPEC L109 and L167 are admitted lines whose wording changed after the pass, and L113 is a
  struck line whose wording changed. Should the read spec carry L109 and L167 with their use held (161 lines) or
  leave them out until re-read (159 lines)? Must all three be classified by three readers before G3 and R-7 may be
  marked verified?
- **Recommended (the narrower):** carry L109 and L167 in the 161-line read spec with their use held: L167 grounds
  G3 only conditionally, and L109 grounds nothing. L113 stays struck. Dispatch a small three-reader piece (DR-74)
  with L109, L167 and L86 in span and a classification-only read of L113, as R-2 was read (classification only,
  never content; 00.1a L227). The strict 159-line alternative [C] would remove G3's only ground without evidence
  that the new text is inadmissible, so it is not recommended.
- **Split:** A left L167's interim use as a developer question (a provisional ground or held) and withdrew its own
  "climate figure only" use of L109; B withdrew its "provisional ground" for L167 and adopted C's form; C held
  both. All three recommend carrying the two lines and classifying them by three readers.
- **Waiting on it:** G3's verified status; R-7; the banner (AM-S1-F12); the LRANGE for later pieces.
- **Disposition:** conflict resolved to the narrower reading.

### AM-S1-Q2 The census read spec

- **Recommended:** adopt `33,390-396,506,650` (10 lines) after the orchestrator confirms that L506 and L650 are
  Davis's Census I and II rows and that L397-L398 lie outside Davis's block (classification only). Optional [C; A
  supports it]: admit Section E's name key (L843-L874, L877-L878) so that latest-period names can be read, with
  L881's founder clause and L883 not used and L884 DO-NOT-FOLLOW. B left the optional part as a developer question
  without a recommended answer.
- **Waiting on it:** every PROOF block over the census in later pieces.
- **Disposition:** confirmed by all three (the 10-line spec); found by one, C (the optional name key).

### AM-S1-Q3 How the mixed numbering in 00.1 and 00.1a is recorded, since DR-101 forbids fixing it in place

- **Recommended:** a numbering key in the amendment note, giving each spec citation's numbering (pass-time or
  current) and its current line, with the pass files never edited (DR-101, DR-102) [A, B, C]. Check the other
  Davis pass files for the same split [B, C] (AM-S1-R8). Separately, a methodology docket item:
  the citation-remap tool must remap a file's spec citations all or none, and must not run over finished pass
  folders without a ruling [A].
- **Waiting on it:** any reader who follows a citation in 00.1 or 00.1a; docket application.
- **Disposition:** confirmed by all three (the key); found by one, A (the tool rule).

### AM-S1-Q4 Is the DR-68 redistribution arithmetic, as DR-90's is, and which ruling applied it to the census?

- **Recommended:** yes, arithmetic and not an in-world inflow (PROVISIONAL), because DR-90 (LOG L1575) names
  DR-68's scenario as its own method and calls that method arithmetic. Cite the ruling that applied the census edit
  (probably DR-69).
- **Waiting on it:** AM-S1-F7 moving from conditional to firm; the qualifier at 00.1 L108-L112;
  whether any later finding may treat the 23,917 people of that step as arrivals [C]; the SPEC L15 source row.
- **Disposition:** confirmed by all three.

### AM-S1-Q5 Is Davis's composition block settled while DR-85's question stays open?

- **Recommended (the first check's answer, carried):** take the current block as the input; mark Taiwan (L43),
  Mongolia (L60), East Turkestan (L62) and Tibet (L70) as open; rely on DR-104 item 1's bar and the open-row rule so
  that no finding depends on their exact shares or headcounts, whatever the tier. Manchuria (L57) is already reduced
  (CENSUS L877) and settled as a randomized row, so four rows are open, not five.
- **Waiting on it:** DR-85's open question (LOG L1529); any finding on the Significant tier's combined share
  (AM-S1-F11).
- **Disposition:** confirmed by all three.

### AM-S1-Q6 Is current SPEC L8's shared-heritage clause a restated founding claim?

- **Question:** SPEC L8 says Davis shares a founding heritage with two other locations of the parent subnet. Under
  REGISTER rule 1, is that a restated founding claim the Register must hold?
- **Recommended:** this pass does not use the clause (another location: not used). The developer checks it against
  those locations' Register rows at the terminal differentiation stage. Davis's own reading is Australia, REGISTER
  L59.
- **Waiting on it:** nothing in S1.
- **Disposition:** found by two (A as a source docket row; B as a question).

### AM-S1-Q7 Should current L180, L201 and L206-L260 be classified?

- **Recommended:** record them as not admitted, never classified and not read. Adjudicate them line by line only
  if a later phase needs them (00.1a L191-L193's rule), never cut or admitted as a range. Have the orchestrator
  confirm from git that L206-L260 were appended after L181 (AM-S1-R5).
- **Waiting on it:** §4.3's statement; the banner; MAP L4's caveat.
- **Disposition:** confirmed by all three.

### AM-S1-Q8 Is the founding-wave roster at current L86 still "legal relation"?

- **Recommended (the narrower):** until a reader admitted to L86 classifies it, its roster grounds nothing beyond
  the Register founder (REGISTER L59).
- **Split:** C recommended answering no outright (read it like current L8's roster); A and B requested a
  classification and gave no recommended answer. The recommendation keeps C's interim use without its verdict.
- **Waiting on it:** the L86 row of the strike table (AM-S1-R1).
- **Disposition:** confirmed by all three (the question).

### AM-S1-Q9 Should the M-224 rule require a numeric read spec to name its numbering frame?

- **Recommended:** yes; a numeric read spec names the commit or the line count it was computed against [C; A
  endorsed it in Round 3]. This is a methodology change, and the developer decides it.
- **Waiting on it:** every later contract's read spec (AM-S1-N1).
- **Disposition:** found by one (C).

### AM-S1-Q10 The PROOF EXEMPT line for positional lines carrying the parent subnet's name or a cluster comparison

- **Question:** standing line 5's EXEMPT line says the forbidden name is "not reproduced elsewhere". REGISTER L59
  carries the parent subnet's name, which also appears in the mandated file paths, so the line cannot be literally
  true. UEIC L598 carries real-world place names and a cluster comparison.
- **Split:** for REGISTER L59, A added EXEMPT and withdrew it in Round 3 as untrue (adopting C's Round 1 reasoning);
  C omitted it in Round 1 and withdrew the omission in Round 3 (adopting A's and B's conservative choice); B added
  it and sent the wording to the developer. For UEIC L598, A and C added EXEMPT; B did not, since real-world places
  are legal comparables.
- **Recommended (C's Round 3 recommendation):** keep the EXEMPT line, and either amend the standing line to allow
  the name in file paths or rule that the parent subnet, a Tier 0 input, is not a forbidden name. Use EXEMPT for
  UEIC L598, because it also carries the cluster comparison.
- **Waiting on it:** the PROOF format of later pieces.
- **Disposition:** conflict sent to the developer.

## 6. Reserved findings and requests

- AM-S1-R1 **Request:** a three-reader, classification-only piece for current SPEC L109,
  L167 and L86 (L86 against DR-88 item 2 and REGISTER rule 1), and a strike-target test for L113. **Blocks:** G3's
  verified status; R-7; the L86 row. **Sensitivity [B]:** if L167 no longer carries its statement, G3 is ungrounded
  and the generator count falls from six to five, still above three. Disposition: confirmed by all three.
- AM-S1-R2 **Request:** reads of CENSUS L397-L398, L506 and L650; a classification-only read of L496
  and L613; and a comparison with the pass-time census L392-L398 [B; A and C asked for parts of this]. **Blocks:**
  the census read spec. Disposition: confirmed by all three.
- AM-S1-R3 **Request:** `01` §2's band thresholds, to confirm that 1,210,432 is still Band 5 and
  817,475 still Band 4. **Sensitivity [B]:** if the figure crosses a threshold, the band machinery DR-4 deferred
  applies to a different band. Disposition: confirmed by all three.
- AM-S1-R4 **Request (orchestrator):** a git check, for example the history of 00.1 L286 and of
  00.1a L1 and L58, of whether DR-85's remap script produced the mixed numbering. **Blocks:** the cause half of
  AM-S1-N2 and AM-S1-F8. Disposition: found by two (A, B); C named the same gap.
- AM-S1-R5 **Request (orchestrator):** compare the spec as of the contract's date (2026-09-13) with
  the pass-completion commit d2dd2136. Did pass-time L182-L236 exist then, and did any numbering shift before L58
  (MAP L4)? **Blocks:** the conditional half of AM-S1-N12, and every mapping here. Disposition:
  found by two (B, C); A named MAP L4's caveat in its limits.
- AM-S1-R6 **Request:** DR-69 and section 2 of the DR-68 scenario file. **Blocks:** AM-S1-Q4.
  Disposition: found by one (C); A and B named the gap in their limits.
- AM-S1-R7 **Request:** the Founding Register's header row, to learn what L59's cells "+5", "✅"
  and "—" mean, in particular whether the last column records exile groups. **Blocks:** the open "exiles" in
  AM-S1-N7; the "+5" inference in AM-S1-F5. Disposition: found by one (C).
- AM-S1-R8 **Request:** a list of every other Davis pass file that cites the old read-spec string
  or pass-time spec numbers. **Blocks:** the reach of AM-S1-N1. Disposition: found by two (B, C).
- AM-S1-R9 **Reserved:** the exact shares of Taiwan, Mongolia, East Turkestan and Tibet (05 L463: under
  active debate, a reserved decision, not an input). Also reserved and not adopted: whether the per-nation figures
  may ever ground a finding on the Significant tier's combined share while those rows are open [B]. Disposition:
  confirmed by all three (the four shares); found by one, B (the Significant-tier question).
- AM-S1-R10 **Reserved, unchanged from 00.1 L317-L319 [C]:** proper names of people, the
  demonym, the DLC, the disposal of the dead, G1's element meaning (DR-1) and early-Federation currency (DR-3);
  and Davis's climate class (DR-104 item 4). Disposition: found by one (C).
- **Research questions:** none. This piece needed no web research, and no finding here rests on a recalled
  real-world fact. The comparable "one of the largest ice-free coastal areas in Antarctica" is taken from SPEC L8 as
  written [C]. All three readers state this.

## 7. Limits

- **No reader read a spec line past L81.** Every statement about current L82-L260 rests on MAP (the orchestrator's
  comparison) and on the contract's own text. No reader can check whether L167's struck clause or L113's strike
  target survives, or what L109 now says.
- **MAP's own caveat is unresolved:** whether the contract's numbering (a spec of 181 lines) equals the
  pass-completion numbering (236 lines) for L1-L181.
- **CENSUS L397-L398, L506 and L650 were read by no reader;** L506 and L650 rest on the orchestrator's result.
- **The cause of the mixed numbering is inferred,** from the pattern and LOG L1530, not seen in git.
- **DR-69, DR-93 and DR-94 were in no reader's list;** they are seen only through SPEC L28, CENSUS L877 and L881
  and the DR-90 entry. DR-68's full mechanism (the scenario file) is not in any list.
- **`01` §2's band thresholds were in no list,** so Band 5 is conditional.
- **Only two pass files (00.1 and 00.1a) were in the lists.** Pass locations in Steps 0 to 10 that inherit the
  stale figures, the old read spec or the §3.3 limit are not listed here [C].
- **00.1b, the record behind the banner's historical claims, was in no list,** so "15 of 15" is neither verified
  nor disputed [B].
- **A's tie point for the Sinian Federation draw is an approximation** that ignores the Kazakhstan step and the
  Manchuria refill.
- **The tier-stability results assume a refill rule that no ruling sets** for the four open rows.
- **No finding characterizes robots beyond census counts.** The robot-physiology file and the two discipline files
  named in the readers' brief were in no reader's list; their principles were applied from the brief's text only.
- **Unchanged admitted lines outside the region (L1-L7, L9-L12) were not re-adjudicated.** L5 cites a culture
  README for its subnet correction; the pass admitted L5, and no reader reopened it [B].
- **This merge adds no finding of its own.** Every reading here comes from A, B, C or K. To check quotations and
  citations, the merge writer read SPEC L10-L81 and 00.1 L1-L24, L58-L73, L104-L197 and L218-L289; its final
  quotation check also passed every entry of the readers' list, at its admitted range, through a script that
  printed only the quoted strings it could not match (there were none). Nothing outside the readers' outputs and
  the merge brief's list was read.
- Everything here is PROPOSED.

## 8. Research log (every search string verbatim from the readers' logs, or: no web research in this piece)

No web research in this piece. All three readers recorded "no web research in this piece". The readers' local,
read-only commands (`sed -n` on admitted spans, `diff`, `grep` on whole-file entries, `wc -l`, and `python3 -I`
calculations) are recorded with their raw output in the readers' outputs; they are not web searches. The merge
writer ran no web search and no repository search; its only searches were over its own part files, and it read
only named files at named ranges (section 9f).

## 9. Merge record (a found-by / confirmed-by table for every item; every conflict and how it was decided; every withdrawal; anything a reader flagged as unclear in the brief)

Sources: A, B and C are the three readers' Round 1 outputs (items XA-, XB- and XC-); reply A, reply B and reply C
are their Round 3 cross-checks; K is the first check's reader (items XU4-). Readers' item numbers appear only
here, as the source of a point. The confirmed-by column counts a reader that held the point after Round 3, whether
it found the point in Round 1 or accepted it in its Round 3 reply.

### 9a. Found by and confirmed by, for every item

| item | source items | found by | confirmed by (after Round 3) | disposition |
|---|---|---|---|---|
| AM-S1-F1 | XA §1a; XB §1a; XC-201 (tally sentence withdrawn, reply C D-1); XU4-23 | A, B, C | A, B, C (tally recounted by command in replies A and C) | confirmed by all three |
| AM-S1-F2 | XA-1; XB-101; XC-202; XU4-17, XU4-23, XU4-28 | A, B, C, K | A, B, C | confirmed by all three |
| AM-S1-F3 | XA-2; XB-102; XC-203; XU4-6, XU4-7, XU4-8, XU4-18 | A, B, C, K | A, B, C | confirmed by all three; strength outside the region: conflict resolved to the narrower reading; pointer misdirection: found by one (K) |
| AM-S1-F4 | XA-3; XB-103; XC-204; XU4-10, XU4-11, XU4-26 | A, B, C, K | A, B, C | confirmed by all three |
| AM-S1-F5 | XA-4; XB-104 (withdrawn in part, reply B W2); XC-205; reply A row 2; reply C D-10 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-F6 | XA-5; XB-105; XC-206 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-F7 | XA-6; XB-106; XC-207; XU4-9 | A, B, C, K | A, B, C | confirmed by all three |
| AM-S1-F8 | XA-7; XB-108, XB-109, XB-110; XC-208; XU4-15, XU4-16, XU4-19; reply A row 4; reply C D-16 | A, B, C, K | A, B, C | confirmed by all three |
| AM-S1-F9 | XA-8; XB-111; XC-209; XU4-20; reply B A-3(ii); reply C D-12 | A, B, C, K | A, B, C | confirmed by all three; L397-L398: conflict resolved to the narrower reading |
| AM-S1-F10 | XA-9; XB-112; XC-210; XU4-21; reply B D13 | A, B, C, K | A, B, C | confirmed by all three; parts as credited in the item |
| AM-S1-F11 | XA-10; XB-113; XC-211; XU4-22; reply A row 19; reply B D14 | A, B, C, K | A, B, C | confirmed by all three; Significant-tier exposure: found by one (B) |
| AM-S1-F12 | XA-11; XB-115; XC-212; reply B D11; reply C D-17 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-K1 | XA §2a; XB-114, XB §2a; XC §2a | A, B, C | A, B, C | confirmed by all three; strict alternative: found by one (C); pointer list: found by one (A) |
| AM-S1-K2 | XA-12; XB-117; XC K1; XU4-7, XU4-18 | A, B, C, K | A, B, C | confirmed by all three; pointer: found by one (K) |
| AM-S1-K3 | XB-116; XC K8; A docket rows for 00.1 L223, L225, L228, L238; XU4-19 | A, B, C, K | A, B, C | confirmed by all three |
| AM-S1-K4 | XB-118; XC K2; XA-9(a) (withdrawn, reply A row 3); XU4-11, XU4-21 | B, C, K | A, B, C | found by two |
| AM-S1-K5 | XC K3; XB-118, XB-119 (refined, reply B D7); XA-13 | A, B, C | A, B, C (A's class differs) | conflict resolved to the narrower reading |
| AM-S1-K6 | XB-119; XC K4; XA-13 | A, B, C | A, B, C (A's class differs) | conflict resolved to the narrower reading |
| AM-S1-K7 | XA-9(c), XA-17; XB-120; XC K5; reply B D6 | A, B, C | A, B, C (C's class differs) | conflict resolved to the narrower reading |
| AM-S1-K8 | XA-17; XB-120; XC K6 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-K9 | XA-18; XB-121; XC K7 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-K10 | XB-122 | B | B (A and C hold the same substance) | found by one |
| AM-S1-K11 | XA-14, XA-15; XB-123; XC K11, XC-216 | A, B, C | A, B, C | confirmed by all three; band: conflict resolved to the narrower reading; the 0.57 metric: found by one (A) |
| AM-S1-K12 | XA-16; XB-111; XC K10; XU4-20 | A, B, C, K | A, B, C | confirmed by all three |
| AM-S1-K13 | XA-20; XB-124; XC K9 | A, B, C | A, B, C (C's class differs) | conflict resolved to the narrower reading |
| AM-S1-K14 | XA-19; XB-109; XC K12; XU4-15 | A, B, C, K | A, B, C | confirmed by all three |
| AM-S1-N1 | XB-116; XC-214; reply A row 5; reply C D-11; XU4-19, XU4-25 | B, C, K | A, B, C | found by two; K's L145: conflict resolved to the narrower reading; K's region point: found by one (K) |
| AM-S1-N2 | XA-21; XB-109, XB-126; XC-215; XU4-15; reply A row 9; reply B D5; reply C D-3 | A, B, C, K | A, B, C | confirmed by all three; L73 against L75: found by one (K) |
| AM-S1-N3 | XA-22; XB-125; XC-213 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-N4 | XA-23; XB-107; XC-216 (softer rule withdrawn, reply C D-5) | A, B, C | A, B, C | confirmed by all three |
| AM-S1-N5 | XA-24, XA-36; XB-135 (withdrawn, reply B W1); XC §5 (withdrawn, reply C D-4) | A | A, B, C | found by one |
| AM-S1-N6 | XA-26, XA-31; XB-127; XC-218; reply A row 7, row 14; reply B D3; reply C D-13 | A, B, C | A, B, C | confirmed by all three; cause: found by two (B, C); interim use: conflict resolved to the narrower reading |
| AM-S1-N7 | XC-219(1); XA-42; reply A row 11; reply B D8 | A, C | A, B, C | found by two |
| AM-S1-N8 | XA-28; XC-219(2); reply A row 12; reply B D9 | A, C | A, B, C | found by two |
| AM-S1-N9 | XA-2, XA-39; XB-128; XC-219(3), XC-226 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-N10 | XB-129; reply A row 10; reply C D-8 | B | A, B, C | found by one |
| AM-S1-N11 | XA-43; XB-130; XC-220; reply A row 13; reply B D10 | A, B, C | A, B, C | confirmed by all three; the 00.1a location: found by one (C) |
| AM-S1-N12 | XA-7, XA-41; XB-110, XB-147; XC-217, XC-225 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-N13 | XA-29; XB-131; XC-221 (sentence withdrawn, reply C D-2) | A, B, C | A, B, C | confirmed by all three; L601 wording: found by one (B) |
| AM-S1-N14 | XB-134; reply A row 15; reply C D-9 | B | A, B, C | found by one |
| AM-S1-N15 | XA-27; XB table L73 (withdrawn, reply B W3); reply A row 17 | A | A, B, C | found by one |
| AM-S1-N16 | XA-30; XC docket row for SPEC L28; reply A row 20; reply B C-3(ii), D12; XU4-S9 | A, B, C, K | A, B, C | lowercase: confirmed by all three; "top tier": conflict resolved to the narrower reading; DR-85 tension: found by one (K) |
| AM-S1-N17 | XA-25; XB-106(d), XB-133; XB table L16; reply C D-7, D-9 | A, B | A, B, C | L15: found by two; L16: found by one (B) |
| AM-S1-N18 | XU4-S8 | K | none of A, B, C (outside their lists' scope) | found by one |
| AM-S1-N19 | XA-26 | A | A | found by one |
| AM-S1-D1 | A, B and C docket rows for the banner | A, B, C | A, B, C | confirmed by all three |
| AM-S1-D2 | A banner row; B row for 00.1 L16-17; C row for 00.1 L16 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-D3 | XA-11 item 7; XB-115 item 7; C row for 00.1 L19-21; reply C D-17 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-D4 | A rows for 00.1 L64, L65; B row for 00.1 L62-65; C rows for 00.1 L64, L65 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-D5 | A, B and C rows for 00.1 L70-71 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-D6 | A, B and C rows for 00.1 L108-112 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-D7 | B row for 00.1 L122, L133-138 | B | A, B, C | found by one |
| AM-S1-D8 | XA §2a pointers; B row for 00.1 L123-129 | A, B | A, B | G2: conflict resolved to the narrower reading; G5, G7: found by two |
| AM-S1-D9 | XA §2a (L124); XC-218 | A, C | A, C | found by two |
| AM-S1-D10 | C row for 00.1 L125, L190; XA-42 | A, C | A, B, C | found by two |
| AM-S1-D11 | A row for 00.1 L129; B row for 00.1 L123-129; C row for 00.1 L129 | A, B, C | A, B, C (forms differ) | conflict resolved to the narrower reading |
| AM-S1-D12 | A row for 00.1 L164-L172; B row for 00.1 L164-171; C rows for 00.1 L164-165, L168-171 | A, B, C | A, B, C | confirmed by all three; the 0.57 metric: found by one (A) |
| AM-S1-D13 | A row for 00.1 L174; XB-107; XC-216 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-D14 | A, B and C rows for 00.1 L179-182 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-D15 | B row for 00.1 L196 and L268; C row for 00.1 L196; XA-43 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-D16 | A and B rows for 00.1 L223, L238; C row for 00.1 L221-238 | A, B, C | A, B, C | confirmed by all three; frame and hazard: found by two (B, C) |
| AM-S1-D17 | A rows for 00.1 L225, L228; B rows for L225-226, L228; C row for L225-226, L228 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-D18 | A row for L241-L246; B rows for L241-243, L244, L246; C rows for L241-246 and L243 against L286 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-D19 | A, B and C rows for 00.1 L248 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-D20 | A, B and C rows for 00.1 L255-257 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-D21 | A, B and C rows for 00.1 L265-275 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-D22 | A row for 00.1 L269; C row for 00.1 L269; XB-128 | A, B, C | A, B, C | roster: confirmed by all three; operator line: found by one (C) |
| AM-S1-D23 | A row for L277-L278; B row for L277-279; C row for L277-280 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-D24 | A and B rows for 00.1 L286; C rows for L284-286 and L243 against L286 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-D25 | A and C rows for 00.1 L303, L341; XB-109 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-D26 | A, B and C rows for 00.1 L329-331 | A, B, C | A, B, C | confirmed by all three; "still open": found by one (A) |
| AM-S1-D27 | C row for 00.1 L374-376; XB-127 | B, C | B, C | found by two |
| AM-S1-D28 | A, B and C rows for 00.1a; XU4-15 | A, B, C, K | A, B, C | confirmed by all three; L73 against L75: found by one (K) |
| AM-S1-D29 | K's affected sentences (00.1a L232) | K | — | found by one |
| AM-S1-D30 | XU4-S8 | K | — | found by one |
| AM-S1-D31 | C row for 00.1a L268-271; reply B D10 | C | A, B, C | found by one |
| AM-S1-D32 | A row for SPEC L15; B row for SPEC L15 | A, B | A, B, C | found by two |
| AM-S1-D33 | B row for SPEC L16 | B | A, B, C | found by one |
| AM-S1-D34 | A, B and C rows for SPEC L28 | A, B, C | A, B, C | lowercase: confirmed by all three; non-share marking: found by one (A); "top tier": conflict resolved to the narrower reading |
| AM-S1-D35 | A row for SPEC L8; B row for SPEC L8 | A, B | A, B | found by two |
| AM-S1-D36 | B row for CENSUS L858, L869-871 | B | A, B, C | found by one |
| AM-S1-D37 | B row for UEIC L598; C row for composition L598; XA-29 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-D38 | B row for UEIC L601 | B | A, B, C | found by one |
| AM-S1-Q1 | XA-31, XA-40; XB-136; XC-223, XC-224 | A, B, C | A, B, C | conflict resolved to the narrower reading |
| AM-S1-Q2 | XA-32; XB-111; XC-227; reply A row 16; reply B D19 | A, B, C | A, B, C | confirmed by all three; name key: found by one (C) |
| AM-S1-Q3 | XA-33; XB-138; XC-228 | A, B, C | A, B, C | confirmed by all three; tool rule: found by one (A) |
| AM-S1-Q4 | XA-34; XB-140; XC-222 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-Q5 | XA-35; XB-137; C section 5 (carried) | A, B, C | A, B, C | confirmed by all three |
| AM-S1-Q6 | XB-139; A row for SPEC L8 | A, B | A, B | found by two |
| AM-S1-Q7 | XA-41; XB-147; XC-225 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-Q8 | XA-39; XB-142; XC-226 | A, B, C | A, B, C (recommendations differ) | confirmed by all three |
| AM-S1-Q9 | XC-214; reply A row 5 | C | A, C | found by one |
| AM-S1-Q10 | reply A row 18; reply B D15, D16; reply C D-6, D-14, D-15 | A, B, C | none settled | conflict sent to the developer |
| AM-S1-R1 | XA-39, XA-40; XB-142; XC-230 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-R2 | XA-32; XB-143; XC-231 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-R3 | XA-38; XB-144; XC-231 | A, B, C | A, B, C | confirmed by all three |
| AM-S1-R4 | XA-37; XB-145 | A, B | A, B | found by two |
| AM-S1-R5 | XB-146; XC-233 | B, C | B, C | found by two |
| AM-S1-R6 | XC-231 | C | C | found by one |
| AM-S1-R7 | XC-232 | C | C | found by one |
| AM-S1-R8 | XC-229; XB-138 | B, C | B, C | found by two |
| AM-S1-R9 | XC-234; XB reserved line; XA-35 | A, B, C | A, B, C | confirmed by all three; Significant-tier question: found by one (B) |
| AM-S1-R10 | XC-234 | C | C | found by one |

### 9b. Every conflict, and how it was decided

Thirteen conflicts remained after Round 3. Twelve were resolved to the narrower reading, and one was sent to the
developer. Each is named in its row above; the decisions are gathered here.

- **The strength of the L21 clause's absence outside the region** (AM-S1-F3). A and C wrote the
  retirement firm without a condition; B kept the condition that the clause might have moved into L109, L113 or
  L167, which no reader can see; C withdrew its sentence that the clause "has left the spec". **Written:** firm for
  the region, conditional for the whole spec.
- **CENSUS L397-L398** (AM-S1-F9). A wrote that they are not Davis's tier block and probably another
  location's material; B and C wrote that what they hold is unknown, and both noted that the second half has no
  admitted ground. **Written:** not known; the structural point (the tier table ends at L396) is kept as inference;
  nothing is said about whose material they carry.
- **The class of the "L54" and "L28" citations** (AM-S1-K5). A: killed by evidence. C: killed for
  want of an admitted line; B adopted C's split in Round 3. **Written:** killed for want of an admitted line, which
  claims less than a disproof.
- **The class of the randomization clause** (AM-S1-K6). A: killed by evidence. B and C:
  narrowed to two rows. **Written:** narrowed.
- **The class of "never readable as measured per-nation counts"** (AM-S1-K7). A and B: narrowed. C:
  killed by evidence in its main part, with the same survivors. **Written:** narrowed.
- **Band 5** (AM-S1-K11). A classed the band's re-derivation as killed for want of an admitted line;
  B and C called the band conditional. **Written:** conditional, neither confirmed nor killed.
- **The class of the L8 clearance** (AM-S1-K13). A and B: narrowed. C: killed by evidence.
  **Written:** narrowed.
- **K's prediction that the old string reads L145** (AM-S1-N1). The three readers' arithmetic
  shows the old string reads L112 and L113 but not L145. **Written:** L112 and L113 only, among the struck lines.
- **The interim use of L109 and L167** (AM-S1-N6, AM-S1-Q1). A: L109 as a
  climate figure only (withdrawn) and L167 as a developer question; B: L167 as a provisional ground for G3
  (withdrawn); C: both held. **Written:** both carried with their use held; G3 conditional.
- **The meaning of "top tier" at the Manchuria step** (AM-S1-N16, AM-S1-D34). A: ambiguous. B:
  either meaning is possible. C: "can only mean the post-relabel Significant rows". Reply A: C's reading more
  probable but conditional. **Written:** ambiguous.
- **G2's ground** (AM-S1-D8). A mapped the pass's range mechanically (L94-L115); B left out the struck
  and DO-NOT-FOLLOW lines. **Written:** B's form.
- **G8's ground** (AM-S1-D11). A, B and C gave three forms. **Written:** C's form, the only one that
  leaves out the inert lines and keeps the scope notes outside G8, as all three hold.
- **The EXEMPT line** (AM-S1-Q10). A and C crossed in Round 3, each withdrawing toward the other's
  Round 1 choice; B sent the wording to the developer. **Sent to the developer**, with C's Round 3 recommendation.

**Strength applied under merge rule 4 (weakest after Round 3; not counted as conflicts):** current L8's PARTIAL
classification is conditional (A conditional, B mixed, C firm) (AM-S1-N3). The window clause is firm,
because B's Round 3 reply adopted A's and C's firm reading (AM-S1-F5). The cause of the mixed
numbering is conditional for all three. Docket confidences take the weakest a reader gave.

**Recommendation splits under merge rule 3 (not counted as conflicts):** for the L86 roster, C recommended "no" and
A and B gave no recommended answer; the narrower interim use is recommended without C's verdict
(AM-S1-Q8). For the census name key, C recommended an optional admission, A supported it, and B gave
no recommendation; C's recommendation is carried and marked optional (AM-S1-Q2).

### 9c. Every withdrawal

Each withdrawal was read as evidence for the narrower reading, never as a tie-break.

- **Reader A (reply A):** its claim that "share-weighted model" survives at L78 (row 3); its "L109 read as a climate
  figure only" (row 7); its list of 00.1a's current-numbered citations, which missed L85 (row 9); the EXEMPT line on
  its REGISTER PROOF block, as untrue in its second clause (row 18).
- **Reader B (reply B):** the PROVISIONAL status of the three-reader question (W1); "not used" for the window
  clause, replaced by "used only as a scope limit" (W2); "here a Russia successor row" for L73 (W3); "L167 grounds
  G3 provisionally", replaced by use held and G3 conditional (W4); "may be followed" for L24, replaced by "followed
  only within Davis's census read spec" (W5).
- **Reader C (reply C):** its tally sentence, 48 ADMITTED and 21 INERT, an arithmetic slip against its own table
  (D-1); its sentence that the struck clause "has left the spec" (D-2); its list of 00.1a's current-numbered
  citations, which missed L58 (D-3); its PROVISIONAL treatment of the three-reader question (D-4); its softer use
  rule on the retention spread (D-5); its choice to add no EXEMPT line under the Founding Register block (D-6).

**Peer corrections the author did not withdraw, applied in the merged text:**

- B's "G5's L177" (XB-116): G5's line is current L179 (00.1 L126 cites pass-time L155), and the old string happens
  to read L179 (reply A, row 6 and its section 6). The merged text does not repeat the slip.
- A's XA-21 lists 00.1 L238 among the lines citing "L143"; L238 carries 143 inside the read-spec string (reply C).
  The merged text uses the grep list.
- C's Section E range "L839-885": L885 is blank and the last content line is L884 (reply B, C-3(iv)). The merged
  text uses L884.
- B's XB-105 says the scratch folder holds the runs for all 38 cities; reply C calls the count a reasonable
  inference, not a quotation. The merged text says it holds the runs for other locations, without the count.
- K's verbatim quotation of SPEC L28 ends "from the final shares", while the line as read ends "from the new
  shares". The merge writer found this while checking quotations; it is a note on the record, not a finding. The
  merged text quotes the line as read.

### 9d. Points the readers flagged as unclear in their brief

- **Section 2's content is specified twice** (A, B, C): the heading says "Killed or narrowed findings" and the
  piece-specific note says section 2 is the mapped read spec. All three put the mapped read spec inside section 2;
  this merge does the same (AM-S1-K1).
- **The region's bounds** (A, B, C): the first check's question says L13-81 while the scope says L10-81. All three
  classified L10-L81; L10-L12 are INERT.
- **DR-68 and DR-90 "are not in this list"** (A, B, C): the question's wording said so, but both were in every
  reader's list and were used.
- **The census span** (A, B, C): the question asks about 392-398, but the admitted span was 390-396, so L397-L398
  could not be seen.
- **The three-reader question was framed as provisional** although DR-74 answers it (A) (AM-S1-N5).
- **The verdict vocabulary has no slot** for an admitted line whose current wording is unclassified (B).
- **00.1a's file name and title disagree** (A) (AM-S1-N2).
- **Standing line 5's EXEMPT wording** cannot be literally true for the parent subnet's name (C; A and B)
  (AM-S1-Q10).
- **Brief rules 6 and 7 name files that were in no reader's list** (the two discipline files and the
  robot-physiology file) (C).
- **REGISTER L12 ends mid-sentence at the span boundary** (B).
- **The Read display showed a phantom final line** on several whole-file entries (A, C); the readers used `wc -l`.
- **K: two amendment notes.** DR-104 item 3 sends readers to section F of the 2026-10-30 amendment note, while K's
  brief cited section C of the 2026-11-09 note (XU4-S7). K saw no conflict for its check.
- **K: the "top tier" tension** in DR-85 item 3 against SPEC L28 (XU4-S9) (AM-S1-N16).
- **Hooks:** the graphify `PreToolUse` hook fired on the readers' Reads and Bash calls and on this merge's. Every
  reader and this merge disregarded it under DR-6 (compliance, not override); no graphify command and no repo-wide
  search was run.

### 9e. What this merge did not copy, under the brief's rules

- **Other locations' names.** The names of other locations carried by SPEC L8, L15 and L16, 00.1 L65 and L269,
  CENSUS L881 and L883, UEIC L598, and LOG L1335, L1574 and L1575, and those inside the readers' PROOF blocks, are
  not written here. Each point is stated without the name, marked "(another location: not used)" where useful.
- **The parent subnet's name** appears in the file paths and in REGISTER L59. It is not written; the text says "the
  parent subnet", and files are named by short names instead of full paths.
- **The real namesake's personal name** in C's quotation of SPEC L8 is not reproduced (real-site history, not an
  input); the point is written without it.
- **Real-world port and city names** from UEIC L598, carried in the readers' PROOF blocks, are not reproduced.
- **The readers' PROOF blocks** are not carried into this merge; its brief gives the merged document no PROOF
  section. Round 2 and reply C's mechanical check (33 of 33 blocks passing) stand as the record that the readers
  read their files.

### 9f. Process notes

- **Reader A** created an empty stray file in the piece directory by a mistyped command; a hook blocked its removal,
  and A asked that it be removed (A snag 2). This merge did not touch it.
- **Reader B** wrote two helper scripts into a directory beside its staging directory and reports removing it (B
  snags 6 and 10); reply A could not confirm the removal. B's first tier-order check loaded the whole spec inside
  Python and used only admitted lines; B re-ran it on span-limited input (B snag 5).
- **Reader C** ran a mechanical PROOF check over all three outputs in Round 3: 33 of 33 blocks pass.
- **This merge** read the merge brief, the readers' brief, the three outputs, the three replies and K's output in
  full. It read SPEC L10-L81 and 00.1 L1-L24, L58-L73, L104-L197 and L218-L289 only to check quotations and line
  citations. It ran one search and one substitution over its own part files to make every key unique, a check
  that every reference has its definition (none unresolved, none defined twice), and a check of every quoted
  string in the parts against the sources at their admitted spans and the readers' outputs (all matched). It edited
  no file other than its own part files.

*End of the merged piece S1. Everything above is PROPOSED; nothing is applied.*

