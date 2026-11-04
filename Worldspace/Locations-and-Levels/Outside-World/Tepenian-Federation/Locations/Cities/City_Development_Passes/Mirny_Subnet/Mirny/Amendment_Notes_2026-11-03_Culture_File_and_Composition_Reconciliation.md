# Mirny · Amendment notes · 2026-11-03 · the culture file's rewrite, the composition rework and the pass

> ## STATUS: **FILED BESIDE THE PASS. Nothing in any pass file, in the amendment files, in the `DR-56` register or in any `.t8_*` file was changed.**
> Method: append-only, as `DR-74` set for this folder (*the pass files stay as they are*) and as the 2026-10-30 note did for the census change. Written 2026-11-03 under a one-off waiver of the 05:00–14:59 hours law (developer: *"reconcile Mirny's files"*; waiver given about 16:10). Every figure the pass records is **as recorded at the pass; the source has since changed.** The live value is given beside it. This note re-derives nothing and rules nothing.
> **Coverage, plainly:** the folder's non-scratch files hold about 25,000 lines. I did not read them all line by line. I searched them for the old frame (China as Primary, 24.24 %, "fourteen stocks", the DR-9 three-stock founding, the old census figures, other-city names, the false Concordia link), read every hit in context, and read in full the sections that carry the findings named in section 3. A finding that states the old frame in words I did not search for could be missed; the redo pass should treat section 3 as a floor, not a ceiling.

## 1 · What the live sources say now (read 2026-11-03)

| Item | As recorded at the pass | Live now | Source |
|---|---|---|---|
| Census I | 665,901 H / 685,529 R / 1,351,430 (then, by `DR-68`, 678,041 / 697,307 / 1,375,348 per the 2026-10-30 note) | **692,971 H / 710,578 R / 1,403,549** (`DR-90`, the Esperanza relocation) | `Specs/Mirny subnet/Mirny.md` L15 |
| Census II | 507,344 H / 509,151 R / 1,016,495 (then 515,452 / 516,890 / 1,032,342) | **524,022 H / 528,352 R / 1,052,374** | spec L16 |
| Robot share | 50.73 % (Census I) | **50.63 %** robots, 49.37 % humans (Census I, DERIVED); Census II 50.21 % robots (DERIVED) | arithmetic on the two rows above |
| Tiers | **Primary** China · **Significant** Japan, UK, South Korea, Russia, Indonesia, Australia · **Notable** Thailand, Vietnam, Philippines, Malaysia, South Africa, New Zealand, Belarus (1 + 6 + 7 = fourteen stocks) | **Primary** United Kingdom 13.73 %, Korea 13.71 %, Indonesia 12.03 %, Sinian Federation 12.00 %, Japan 7.81 %, Australia 6.96 % · **Significant** (11) Philippines, New Zealand, Malaysia, Thailand, Taiwan, Idelsk-Uralia *(founding wave)*, Russia (core state), Vietnam, Belarus, South Africa, Kazakhstan · **Notable** (19) | spec tier list; `DR-85` |
| Weighted shares (the pass's 8 / 3 / 1 instrument, `DR-12`; a pointer, never a ground) | P 24.24 %, S 54.55 %, N 21.21 % (8 / 18 / 7 = 33) | 6 × 8 = 48, 11 × 3 = 33, 19 × 1 = 19, total 100: **P 48.0 %, S 33.0 %, N 19.0 %** (DERIVED) | spec tier list |
| Stocks | fourteen | **36** (6 + 11 + 19) | spec tier list |
| "No majority" | true under the weighting (China 24 %); census says only *dominant* | still true, now by direct reading: the largest single share is 13.73 % (UK) | spec table |
| Founders | `DR-9`: exiles from Russia, China and Australia (three co-founders) | Register L57: **founded by Idelsk-Uralia** (replacing Russia in the founding-nation role); **exile groups present: Russia, Australia and the Sinian Federation (China)**; `DR-46` (amends `DR-9`: *"the three exile groups stand; what is new is the founding nation"*), `DR-54` (establishing country) | `Founding_Register.md` L57 |
| Founding stocks by weight | China 8 + Russia 3 + Australia 3 = 14 of 33 = 42.42 % | Sinian Federation 8 + Australia 8 + Russia 3 + Idelsk-Uralia 3 = **22 of 100 = 22.0 %** (DERIVED, same instrument) | spec tier list; Register L57 |
| Language | Mandarin first (a *proposal* in the old culture file L105) | Hawaiian (later Tepenian) civic default; second slot open (no majority) | developer rule 2026-11-02; culture file L105 |

**Not touched by the rework:** the wind, the light, the relay, the site, `DR-56` / `DR-57` / `DR-76` and the two 2026-10-29 amendment files. Only what rests on who the people are, how many, and who founded the city is affected.

## 2 · The culture file was rewritten in 35 places; 51 of the pass's 89 culture-line items point at them

`Local_Cultures/Mirny_Subnet/Mirny.md` changed at these lines on 2026-11-03 (git diff against the 2026-10-13 version; **line counts unchanged, so every `LC:n` citation in the pass still resolves to the same line number, now holding new text**): L3, L24–26, L28–35, L41, L43, L45, L47, L55, L61, L75, L77, L80, L86, L89–90, L97, L105–106, L114, L122, L124, L130, L136, L144, L150–151, L163, L170, L178, L184, L190, L204, L220, L226–227, L229, L241–242, L287, L301.

`05_Reconciliation.md` compared the culture file's lines with the pass as **LC-1 … LC-89**. These 51 items quote text that has since been rewritten. Most were verdicts such as CONTRADICTION, CULTURE-ONLY or BOTH-TRUE; the rewrite now executes several of the pass's own recommended corrections (for example D-3, the China-alone-at-Primary and Chinese-majority lines, and the Mandarin-first language line). **Whether each item is now resolved is the Mirny block's call**; the table shows what the line says today.

| Item | Culture line | What the pass checked (as recorded) | Pass verdict (as recorded) | What the line says now |
|---|---|---|---|---|
| LC-1 | L3 | rename flag · the name is built on the real station and ship; the founding-tension identity may need replacing | **OUT OF FRAME** — a process note on a reserved decision, not a claim about Mirny; RV-1 already holds the request | *(Flagged 2026-07-08 for an eventual rename — see `TODO.md`'s "Mirny Rename" entry. **Updated 2026-11-03 for `DR-85`:** the national composition resembles the Russian st… |
| LC-6 | L22–26 | tier table · census tiers; Russia marked founding and naming heritage; Australia a founding wave | **MATCH** on the tiers (both transcribe the census; Tier 1); the Russia annotation is LC-7 | \| Primary \| United Kingdom, Korea, Indonesia, Sinian Federation, Japan, Australia \| |
| LC-7 | L25 | Russia as founder · Russia founded and named the city | **CONTRADICTION** — with Tier 1; the pass agrees with Tier 1 (`C-1`; `D-1`) | \| Significant \| Philippines, New Zealand, Malaysia, Thailand, Taiwan, Idelsk-Uralia *(founding wave)*, Russia (core state), Vietnam, Belarus, South Africa, Kazakhstan … |
| LC-8 | L28–30 | composition note · no American presence at any tier; China alone at Primary; Russia Significant | **MATCH** after delete-the-name (the claims about Mirny's tiers survive); the first-such-city and unlike-other-cities framing is **OUT OF FRAME** (co… | *No American successor region appears in Mirny's composition at any tier. No nation holds a majority: six nations are |
| LC-9 | L33–35 | other-city contrast · Mirny's founding nation set against two other cities' fates | **OUT OF FRAME** (comparison; collapses on delete-the-name) | that founded and named the city … ended up demographically Chinese by scale"] — superseded by `DR-85` and the Register |
| LC-10 | L35 | Chinese by scale · the city ended up demographically Chinese | **BOTH-TRUE** — none of the four scales settles it; different objects (the largest single community vs a majority); property: a Primary at about a qu… | (founding/naming heritage), Indonesia, Australia (founding wave)). The earlier comparisons to other cities were removed.* |
| LC-11 | L41 | station inheritance · exiles inherited a substantial, long-operating station | **MATCH** on inherited infrastructure (both from the spec; not independent) | Mirny Station was one of the oldest continuously occupied Antarctic stations in the real world, operating since 1956; who built it is a coordinate, not a founder. When t… |
| LC-12 | L41 | operator as founders · the operator nation's robots and allies inherited its era's infrastructure as one of the nation's footholds | **CONTRADICTION** — founders and operator-continuity framing against Tier 1 (`C-1`; `D-1`); the neighbor-station comparison is OUT OF FRAME | Mirny Station was one of the oldest continuously occupied Antarctic stations in the real world, operating since 1956; who built it is a coordinate, not a founder. When t… |
| LC-13 | L43 | name as statement · keeping the name declared a nation's presence from the continent's beginning | **CONTRADICTION** — against Tier 1 rulings (`C-3`; `D-2`) | The name was never in question. *Mirny* — the sloop that carried Fabian von Bellingshausen's 1819–1821 expedition, the first to circumnavigate Antarctica and among the f… |
| LC-14 | L45 | founders did not choose · they inherited the station's location | **MATCH** — the conclusion agrees; the ground differs (the file's is the station's location, a GPS fact; the pass's is assignment under the treaty [D… | The city's geographic position did the rest of the founding work on its own. Sitting within seconds of arc of the exact Antarctic Circle, Mirny occupies a genuine thresh… |
| LC-15 | L45 | flagship symbolism · the line and the flagship that first sighted the continent make the symbolism; comparisons with four other cities | **CONTRADICTION** on the flagship clause — namesake as meaning (`C-3`; `D-2`); the city comparisons are OUT OF FRAME | The city's geographic position did the rest of the founding work on its own. Sitting within seconds of arc of the exact Antarctic Circle, Mirny occupies a genuine thresh… |
| LC-16 | L47 | demographic shift · later Pacific-corridor immigration made China dominant; Russia settled into Significant | **CONTRADICTION** on the premise that a Russian-led founding was later overtaken by Chinese arrivals (`C-1`; `D-3`); the existence of a later Pacific… | As the exile generations passed, broad Pacific-corridor immigration produced a city with no majority nation: six Primary nations (the United Kingdom, Korea, Indonesia, t… |
| LC-18 | L55 | engineered competence · the wind is managed without drama; airlock entries, reinforced structures; neighbor comparisons | **BOTH-TRUE** — scale 1 (the public, built and written competence vs the private, untaught reading) (`BT-1`); the airlock detail is **CULTURE-ONLY** … | The city's relationship to this wind is unromantic and practical — architecture built against it, airlock entries, reinforced structures, a culture that treats severe wi… |
| LC-19 | L61 | minimal polar night · both polar night and midnight sun occur, about 4–5 days each | **CONTRADICTION** — physics against the ratified spec; the retracted model is not used (`C-2`; `D-4`) | Sitting almost exactly on the Antarctic Circle gives Mirny an experience of both polar night and midnight sun, but in genuinely minimal form — roughly 4–5 days around ea… |
| LC-20 | L61 | solstice grazing ritual · the grazing observed quietly as the year's defining ritual; proof of a liminal identity | **CONTRADICTION** on the physical premise (`C-2`; `D-4`); that the observance's object is a light event corroborates the derivation in P4-3. **Split … | Sitting almost exactly on the Antarctic Circle gives Mirny an experience of both polar night and midnight sun, but in genuinely minimal form — roughly 4–5 days around ea… |
| LC-22 | L75 | two thresholds · a geographic threshold and a settlement threshold (a small founding population beside a larger later one) | the geographic half **CULTURE-ONLY** (rests on the retracted symmetry); the settlement half **BOTH-TRUE** — scale 3; property: a founding cohort that… | Mirny's culture is organized around two overlapping thresholds: the geographic one (sitting exactly on the Antarctic Circle, belonging fully to neither the polar zone no… |
| LC-23 | L77 | founders Russian-heritage · the founding-era population predominantly of the founding nation's heritage | **CONTRADICTION** — with Tier 1 (`C-1`; `D-1`) | - **a. Settlement-era layering** — The city's founding-era population (the establishing country Idelsk-Uralia and the exile groups from Russia, Australia and the Sinian … |
| LC-24 | L77 | later waves arrived into an established city | **MATCH** — corroboration of a [D] and of a reserved finding; not adoption | - **a. Settlement-era layering** — The city's founding-era population (the establishing country Idelsk-Uralia and the exile groups from Russia, Australia and the Sinian … |
| LC-25 | L77 | coexist, not merge · old-small and new-large each stay visibly itself, in stable unresolved peace; other-city contrasts | **BOTH-TRUE** — scale 3 (Act 1 public, stock-coded layering vs a frame-long personal memory line that becomes the founding robots' in Act 2); the fil… | - **a. Settlement-era layering** — The city's founding-era population (the establishing country Idelsk-Uralia and the exile groups from Russia, Australia and the Sinian … |
| LC-27 | L80 | hub importance to Concordia vs post-war capacity | **OUT OF FRAME** (Concordia-framed; post-war) | - Between Mirny's self-understanding as structurally important to its own subnet (the relay that routes the other subnet cities' Arcanet traffic to one another, Section … |
| LC-28 | L86 | competence over romance · hardships are managed well, without narrative; neighbor contrasts | **BOTH-TRUE** — scale 1 (public competence vs the private reading; C adds scale 2, the Social Contract vs its own dissent seeds) (`BT-1`); the no-nar… | - **a. Competence over romance.** Mirny doesn't mythologize its hardships or perform its warmth — the wind, the cold, the threshold position are all simply managed, well… |
| LC-31 | L89 | public/private unremarked · the divide is standard; contrasts with two other cities | **MATCH** on the surviving claim (unremarked); contrasts OUT OF FRAME. **Split named:** A MATCH · B CULTURE-ONLY · C BOTH-TRUE scale 1 (reads publicl… | - **d. Public/private divide** — Standard and unremarked; no strong civic pressure toward either communal openness or ceremonial reserve. |
| LC-32 | L90 | privacy moderate; Arcanet use functional and administrative; personal use low-friction | **CULTURE-ONLY** — a seed for network etiquette (not in the admitted set) | - **e. Privacy as civic value** — Moderate; Mirny's Arcanet culture (see Section 24) skews heavily toward the functional and administrative given its subnet-hub role, le… |
| LC-34 | L97 | attracts types · administrators, communications specialists, engineers, and people of the founding nation's heritage drawn by its historical weight | the work types **CULTURE-ONLY** for later arrivals only (scale 3 keeps it off the founding stratum; corroborates the direction of RF-7 and RF-16); th… | - **The type this city draws:** People comfortable with ambiguity and threshold conditions — administrators, communications specialists, engineers suited to Mirny's wind… |
| LC-37 | L105 | languages · Mandarin primary, substantial Russian, four others | **CULTURE-ONLY** — a tier-3 proposal for R-21 and R-88; inferring a tongue from the Primary stock is the move P2 killed; the Russian emphasis rests o… | - **a. Primary language(s):** Hawaiian (later Tepenian) is the civic default, as in every Tepenian location. No nation holds a majority (the largest share is the United … |
| LC-38 | L106 | direct unornamented speech; two community languages fully fluent | **CULTURE-ONLY** — a register seed resonant with P8-27, not adopted. **Split named:** A CULTURE-ONLY · B and C MATCH on manner (grounds differ); merg… | - **b. Linguistic character:** Direct and unornamented — Mirny speech favors clarity, consistent with the city's function-first, competence-over-romance civic value. Whi… |
| LC-41 | L114 | wind-engineered building · airlocks, minimal exposed surface, reinforced structures; the operator-era station as the historical core, newer growth ou… | **CULTURE-ONLY** — a tier-3 answer on entries and orientation; it would place the station at the core, bearing on R-119 and Q-96; the operator label … | Aggressively wind-engineered, pragmatic and unmythologized — airlock entries, minimal exposed surface, structures oriented and reinforced specifically against the severe… |
| LC-43 | L122 | human cuisine · hearty preservation-oriented cold-weather food beside another stock's tradition, coexisting; a correction about another city | **CULTURE-ONLY** — a stock-repertoire seed (Act 1 form; the divergence operator still to apply); corroborates the direction of CAND-F1 (food that kee… | - **a. Human cuisine:** Hearty, preservation-oriented cold-weather cooking is part of the city's inherited station table (Russia and Idelsk-Uralia, together 4.28%, DERIV… |
| LC-45 | L124 | siligel unremarkable · robot intake is functional, no ceremony | **MATCH** after delete-the-name (the contrast collapses) | - **c. Robot cuisine / siligel culture:** Functional and unremarkable in the best sense — siligel preparation follows the city's general competence-first character, with… |
| LC-46 | L130 | performance outerwear · judged only on performance against the wind, not on what it signals | **BOTH-TRUE** — scale 1 (the stated public norm vs the private reading it reveals as a byproduct) (`BT-6`); the contrast is OUT OF FRAME; CAND-D1 not… | Heavily wind-engineered outerwear, rigorous, without identity-marker pride — Mirny clothing is judged purely on performance against the wind, not on what it signals abou… |
| LC-47 | L130 | station-era garments · garment structures from the founding-era station's wind conditions persist; Pacific colors and textile influence from later ar… | **CULTURE-ONLY** — admissible only if the founding era means the exiles' own, a tradition that starts with the city; a station-derived practice is no… | Heavily wind-engineered outerwear, rigorous, without identity-marker pride — Mirny clothing is judged purely on performance against the wind, not on what it signals abou… |
| LC-48 | L136 | separate music traditions · no single city sound | **CULTURE-ONLY** — a stock-repertoire seed at tier 3; Act qualification needed; the occasion CAND-S1 is not contradicted | Musical traditions of the six Primary nations and of the founding-era groups coexist, more separate than merged, with no dominant singular Mirny sound; the details are l… |
| LC-51 | L144 | wind-engineering craft · skilled, quietly regarded | **BOTH-TRUE** (`BT-5`). **Split named:** A and B BOTH-TRUE · C MATCH (a craft that makes an object carries regard; the pass adds that the reading, wh… | - **Crafts & material culture:** Wind-engineering craft, treated as pure competence rather than heroic identity — genuinely skilled, quietly regarded, not mythologized. |
| LC-52 | L150 | wind not narrated · near-constant, discussed less than elsewhere | **MATCH** after delete-the-name | - **Sound:** Wind, severe and near-constant, though Mirny residents discuss it little — present, managed, not narrated. |
| LC-53 | L151 | rock, sea air, cooking smells | **CULTURE-ONLY** — a smell seed (R-28); any adoption must say which body smells it (`RP` L9) | - **Smell:** Cold rock and sea air off the Davis Coast; a layered mix of cooking smells in residential areas, kept distinct from one another. *(Corrected 2026-11-03: [ol… |
| LC-56 | L163–168 | six sector shares · communications 20, technical 20, industrial 20, maritime 15, commercial 15, other 10 | **MATCH — circular / self-originated**: P7 Snag 5 traces `D16`'s figures to this very section; the pass's sector sizes and this file are one source; … | - Communications / Arcanet infrastructure: ~20% — a large sector, reflecting Mirny's subnet-hub role |
| LC-57 | L163 | unusually large sector · communications reflecting the hub role | the ranking is **OUT OF FRAME**; the surviving clause (the sector reflects the hub role) is a **MATCH**, with the caution that the sector's breadth e… | - Communications / Arcanet infrastructure: ~20% — a large sector, reflecting Mirny's subnet-hub role |
| LC-58 | L170 | vision construction engine · yards process materials trucked from the south into road materials and machinery; a spur to Concordia; quarries not shar… | **OUT OF FRAME** — a developer-vision paragraph dated 2026-07-05 (`DR-10`); its admitted substance already enters the pass through `SPEC` L174; see `… | **Developer vision, established 2026-07-05 — the subnet's construction engine.** Mirny's industrial yards process raw materials trucked in from quarries to the south, to… |
| LC-60 | L178 | allies settling · the founding nation's robots and their human allies settled the site; solidarity persisted; not a live political question | the single-stock founders clause **CONTRADICTION** (`C-1`; `D-1`); the robot-and-ally structure, shared-exile solidarity and no live politics **MATCH… | Founded on a shared-exile logic — the establishing country's robots and humans, with the exile groups from Russia, Australia and the Sinian Federation, settling the site… |
| LC-61 | L184 | robots in professions · robots concentrate in communications, technical and wind-engineering roles; pragmatic, undramatic | the concentration claim **CULTURE-ONLY** — a distribution `DR-4` suspends; as a general robot-culture answer it is the narrow-role error (`D-11`); th… | Robot residents concentrate heavily in communications, technical, and wind-engineering roles — professional competence culture without mythologized pride, in a register … |
| LC-62 | L190 | belief · Russian Orthodox heritage among families of that ancestry; Chinese-heritage secular and philosophical traditions, coexisting | **CULTURE-ONLY** — origin-faith seeds (Act 1 fresh; Act 2 ancestry), admissible after composition only through the divergence operator; no roster fai… | - Russian Orthodox heritage persists quietly among Russian-descended and Idelsk-Uralian families, alongside the secular, philosophical and religious traditions of the si… |
| LC-66 | L204 | dual-layered private life · smaller communities (the file lists Australia among them) navigate two layers | **CONTRADICTION** (Round 3 decision) — Tier 1 on Australia's place and the two-layer premise (`C-1`; `D-1`). **Split named:** A BOTH-TRUE scale 3 · B… | Because Mirny's founding-era population and its much larger, later-arriving population coexist rather than merge, the public/private divide plays out as follows — both g… |
| LC-68 | L220 | Upper Earth muted · relations muted; a neighbor comparison; the founding legend rests on an old expedition | muted relations **CULTURE-ONLY** (attitudes are in no admitted file; R-61); the expedition-legend clause **CONTRADICTION** — namesake as data (`C-3`;… | Muted — Mirny's civic energy is absorbed by its infrastructural responsibilities more than by active grievance politics. Its founding legend, anchored in a centuries-old… |
| LC-69 | L226 | rival and hub role · a rivalry with another member; Mirny holds the formal hub role | the hub role survives delete-the-name: **MATCH**; the rivalry is **OUT OF FRAME** (comparison) | - **Zhongshan:** A Mirny subnet city on Hwy 110, whose Arcanet traffic is routed through Mirny's subnet relay (Section 24). Mirny holds the formal hub role. *(Corrected … |
| LC-70 | L227–228 | neighbor temperaments · shares a temperament with one neighbor; a close working relationship with the western road neighbor | the temperament line **OUT OF FRAME**; the working relationship survives as a relation claim: **CULTURE-ONLY** (R-60, R-61) | - **Casey:** Fellow Mirny subnet city on Hwy 110, routed through Mirny's subnet relay. *(Corrected 2026-11-03: [old: "…shares Casey's practical, function-first temperame… |
| LC-71 | L229 | Concordia and diaspora · a spur road to Concordia; diaspora presence | **OUT OF FRAME** (Concordia-framed; diaspora) | - **Concordia:** *Corrected 2026-07-04 — the claim below previously stated Mirny and Concordia "share a subnet" with a surviving Arcanet link. They don't: Mirny is Mirny… |
| LC-73 | L241 | relay specialists exported · Mirny-trained relay specialists carry weight elsewhere | **CULTURE-ONLY** — a seed for R-81 (thematic; does not fill the non-thematic slot; `00b` exempts Export) | - Communications and infrastructure expertise — Mirny-trained relay and Arcanet specialists carry weight given the city's hub responsibility |
| LC-74 | L242 | wind-engineering export · a competence; a comparison | **CULTURE-ONLY**; the comparison OUT OF FRAME | - Wind-engineering competence, in a practical register without identity-performance |
| LC-84 | L287 | demographic-shift placeholder · a later shift to a Chinese majority | **CONTRADICTION** (Round 3 decision) — on the shift premise (Tier 1) and the majority wording (census) (`C-1`; `D-3`); the history itself is deferred… | - **[Placeholder — the demographic shift to a population with no majority nation]** — likely gradual rather than a single event, but a culturally significant era in the … |
| LC-88 | L301 | diaspora in Concordia | **OUT OF FRAME** (diaspora in Concordia) | Mirny-descended people in Concordia carry a specific, quiet awareness of connection — the Hwy 110 road link, and Mirny's relay role for its own subnet. *(Corrected 2026-… |
| LC-90 | L28–35 | comparative clauses · likenesses, contrasts and ranks against other cities | **OUT OF FRAME** — each fails delete-the-name; the Mirny clause beside each is reconciled in its own row above | *No American successor region appears in Mirny's composition at any tier. No nation holds a majority: six nations are |

## 3 · Findings that rest on the superseded frame: redo in the Mirny blocks

Marked **⚠ rests on the superseded frame (2026-11-03): redo in the Mirny blocks.** None is rewritten here; each stays as recorded. The wind, light, relay and site findings are not on this list.

| # | Finding (as recorded) | Where | What changed under it | Direction |
|---|---|---|---|---|
| R1 | **P2-4 · The founders are a minority of descent by stock count** (*3 of 14 stocks; 14 of 33 weights; "China is both a founding stock and the Primary"*), and the findings that cite it | `04_Phase_02` L235–L238, A.2 L110–L113, A.3 L120–L127, L395, L491, L550; `02_Spine` DEFICIT L75; `06_Differentiation` L133 (row *holds* `[B]`); `04_Phase_09` P9-2 L181, L207; Step 5 BT-12 L327, D-3 L356 | Founding groups by weight are now 22 of 100 (Sinian Federation and Australia both Primary *and* exile groups; Idelsk-Uralia the establishing country, Significant); 36 stocks, 32 non-founding. The *direction* (founders a minority) survives on the live numbers; the counts, the "China is both" clause and the strata remark do not | Re-derive on the live table |
| R2 | **Phase 2 A.1–A.4 · composition arithmetic and its limits** (tier list; 8/3/1 shares P 24.24 / S 54.55 / N 21.21; *"Fourteen stocks, no majority" is a property of the weight model, not a census datum*; A.4 annotation note) | `04_Phase_02` L96–L135, E-table L365 (*China Primary, weight 8*), L384 | Tiers, counts and weights all changed (section 1). "No majority" can now be read directly from the table (largest share 13.73 %) | Re-derive; the A.3 caution may relax |
| R3 | **P2-5 and Step 3 · only three of the fourteen stocks were researched, "exactly the three founding stocks"** (Russia, China, Australia route books and amended records); R-156 *the fourteen stocks' repertoires*; the Borrowed Form (§D) that speaks "for the founders only" | `04_Phase_02` L238–L242, L313, L321–L329; `03_Research` L108–L110; `02_Spine` L165; `ULM_AUTORUN_HANDOFF` L88, L108; `07_QA_Gates` L164 | The exile groups stand (`DR-46`), so those three studies stand as exile-group research. But the establishing country, Idelsk-Uralia, was never researched; the stock count is 36, not 14; "exactly the three founding stocks" is no longer true | Add Idelsk-Uralia to the cap-starved research block; restate the scope |
| R4 | **Phase 9 · the lens decision and the populations** (*"of any of fourteen stocks, none a majority"*; *"eleven of Mirny's fourteen stocks are not founding stocks"*; *"the Primary also a founding stock"*; robots 50.73 %) | `04_Phase_09` L20, L153, L174, L176, L180–L181, L193, L207, L225, L303, L313 | Counts and the Primary-also-founder clause changed; robot share is now 50.63 % (Census I) – see section 1; the born-here ancestry claim ("plural by construction") survives in direction | Re-derive the numbers and the P2-4-dependent clauses |
| R5 | **Phase 8 · the language question and the transplanted layer** (*"Phase 8's language question has a starting stock, not an answer (R-21)"*; P8-6 *fourteen stocks named, none written*; C-8 *Primary China*; the Primary "shapes the city's primary linguistic and cultural identity" with China as that Primary) | `04_Phase_08` L21, L169, L257–L259, L531, L585, L643, R-96 L843; Step 5 rows LC-37/R-21/R-88/Q-24 (L173, L474, L553, L589) | Language is no longer an open pass question about a Primary stock: Hawaiian is the civic default and the second slot is open (no majority). There is no sole Primary to give the city its linguistic identity | Re-frame R-21/R-88; redo L531's Primary reading |
| R6 | **Phase 7 · "by stock, tiers only" note** (*Primary — China; Significant — …*) | `04_Phase_07` L469–L471 | Tier list changed | Re-derive the note |
| R7 | **Step 5 · culture-file reconciliation** (LC-1 … LC-89; BT-12 *Chinese by scale, and no majority*; C-1 *who founded Mirny and who is the later wave*; D-3 *strike the sequence in which China arrives later*) | `05_Reconciliation` L144–L152, L173–L179, L198, L222, L291, L327, L356, L429, L474, L553, L587–L589 | The culture file now carries many of the corrections the pass recommended (section 2). The pass's *verdicts* about the old text are history; whether any CONTRADICTION is closed is not decided here | Re-run the LC comparison against the live culture file |
| R8 | **Symbol Review · Social half of Earth, and the Saturn / Earth reasoning** (*"fourteen stocks, no majority"*; *"a city of 1.35 million"*) | `Symbol_Review_2026-10-13` L14, L22, L42; `04_Phase_10` L425; `05_Reconciliation` L523 | "No majority" still holds (36 stocks, largest 13.73 %); the count and the population are stale. Per the developer (2026-11-03) symbols are determined after the locations are synthesized, so the pick stays provisional either way | Redo after the culture is re-synthesized |
| R9 | **Step 8 Review Panel · the panel's premises** (*"a city of 1,351,430"*) | `08_Review_Panel` L184 | Population only | Number refresh when the panel is re-cast |

**Founders (`DR-9` wording in the early files) are already recorded in the pass as stragglers** (`07_QA_Gates` E6 L37; Step 5 items (f) and (g) L715; `04_Phase_05` L105–L107; `04_Phase_09` L519; `06_Differentiation` PR-8 L266). `DR-46` is the governing source and this note adds nothing to that record except the live Register line and the weights in section 1.

**Not on the redo list (checked):** the other-city names in `04_Phase_05` (relay chain, Hwy 110 neighbours, "Denison — an engineering parallel ... held without an admissible reason" L351, R-60 L496) are relation lines or comparisons the pass itself refused; `00_Frame`, `00.1_Step_MINUS-1`, `01_Inherited`, `02_Spine` G4/G8 and `00.0_Pre-Trip_Inspection` carry `DR-9` wording and the old composition as recorded inputs (their own E6 straggler note applies). **The false claim that Mirny is the "only functioning intra-subnet Arcanet link" to Concordia is not repeated anywhere in the pass files** (searched: `intra-subnet arcanet`, `only functioning`); it lived only in the culture file L80 and L301, now rewritten.

## 4 · Inventory: every non-scratch pass line that states an old value (script search, 2026-11-03)

Categories: **COMP** = China / Chinese / Mandarin / sole Primary / 24.24 / fourteen stocks / China-Primary · **FOUND** = the `DR-9` three-stock founding wording · **POP** = a superseded census figure · **XCITY** = another city's name (listed to be read; relation lines are legal). The 2026-10-30 note's own table is omitted, and so are the two Pre-Trip files (`00.0_Pre-Trip_Inspection.md` and its AS_RUN copy), which were being rebuilt in the same hour by another piece of work. Many lines are quotations of the culture file or scan echoes inside `07_QA_Gates`; the live values are in section 1.

| File | Lines found |
|---|--:|
| `00.1_Step_MINUS-1_Input_Contract.md` | 18 |
| `00_Frame.md` | 12 |
| `01_Inherited.md` | 1 |
| `02_Spine.md` | 7 |
| `03_Research.md` | 3 |
| `04_Phase_02_Composition_and_Arrival.md` | 28 |
| `04_Phase_03_Surface_and_Texture.md` | 3 |
| `04_Phase_04_Ordinary_Life.md` | 3 |
| `04_Phase_05_Relation_and_Geometry.md` | 14 |
| `04_Phase_06_Meaning.md` | 6 |
| `04_Phase_07_Order.md` | 6 |
| `04_Phase_08_Making.md` | 13 |
| `04_Phase_09_Populations.md` | 14 |
| `04_Phase_10_Catalog.md` | 6 |
| `04b_T8_Rounds_Phase_10.md` | 4 |
| `04b_T8_Rounds_Phase_2.md` | 1 |
| `04b_T8_Rounds_Phase_5.md` | 3 |
| `04b_T8_Rounds_Phase_6.md` | 4 |
| `04b_T8_Rounds_Phase_7.md` | 4 |
| `04b_T8_Rounds_Phase_8.md` | 5 |
| `04b_T8_Rounds_Phase_9.md` | 2 |
| `05_Reconciliation.md` | 19 |
| `06_Differentiation.md` | 2 |
| `07_QA_Gates.md` | 86 |
| `08_Review_Panel.md` | 2 |
| `Amendment_Rederivation_P06_Meaning_2026-10-29.md` | 3 |
| `Amendment_Rederivation_P07_Order_2026-10-29.md` | 2 |
| `DR-56_Amendment_Register_2026-10-13.md` | 1 |
| `Symbol_Review_2026-10-13.md` | 3 |
| `ULM_AUTORUN_HANDOFF.md` | 4 |
| `ULM_AUTORUN_STATE.md` | 1 |


### `00.1_Step_MINUS-1_Input_Contract.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 15 | COMP,FOUND | > \| **(a)** \| ***"Exiles from a combination of Russia, China, and Australia."*** \| **R-1 / Q-1 RESOLVED.** **G4 "who" is now P… |
| 65 | POP | - Population magnitude (→ band): present — L15, Census I: 665,901 humans / 685,529 robots / 1,351,430. |
| 66 | POP | CENSUS I GOVERNS (DR-4, DRL L211–212). L16, Census II: 1,016,495 (admissible |
| 115 | COMP,FOUND | Founders: Russia, China, Australia (DR-9; R-1). The two placeholder |
| 227 | COMP | \| L20 \| ADMITTED \| G8 (Primary: China) \| 3-0 \| 05 L492; RB L2113–2115 \| |
| 314 | XCITY | \| L139 \| SPLIT — 1–41 ADMITTED · 42–102 EXCLUDED — CONCORDIA-FRAMED · 103–270 ADMITTED \| G2 (wind as the primary outdoor hazar… |
| 387 | COMP,FOUND | \| **C-4** \| G4 Founding condition \| **PARTIAL** \| L21 (78–119) · L148 · L150 (1–34, 362–612, 717–786) · L150 (702–716) and L1… |
| 391 | COMP,POP | \| **C-8** \| G8 Demographic composition \| **PRESENT** \| L13 · L15–L16 · L18 · L20 · L21 (1–46, 78–119) · L22 · L24 · L28 · L47… |
| 401 | COMP,FOUND | G4 "who": Russia, China, Australia (DR-9). **Missing or contested (none blocks):** the founding year (R-8) · an in-frame |
| 435 | COMP,FOUND | **R-1 · Who founded Mirny — RESOLVED by `DR-9`: exiles from Russia, China and Australia** (`Founding_Register.md`). |
| 441 | FOUND | 2. *Resolution:* the founders are all three stocks. L150 chars 702–716 is consistent with the ruling as one of the |
| 445 | FOUND | 4. *Still open in G4:* **when** (R-8) and **why**. Phase 2 builds its founding strata on the three stocks under a |
| 446 | COMP | China-Primary population. The station and its ship-name lineage are a coordinate only and bear on nothing, |
| 466 | XCITY | 1. *Missing:* one list. L184 chars 129–195 (corrected 2026-07-04): Zhongshan, Casey, Davis, Vostok, Kunlun. L229 |
| 467 | XCITY | chars 1072–1244 ("as of 2026-07-05"): Sinheung moved in "alongside Zhongshan and Shirayuki". |
| 545 | XCITY | L229 chars 762–916 → `Mirny_Full_Extrapolation.md` §VIII and `Specs/Sinheung.md` · L200 → `Specs/Janbogo.md` · |
| 564 | COMP,FOUND | residue* (excluded, RB L2130)? **Answered by `DR-9`:** exiles from Russia, China and Australia. → R-1. |
| 643 | COMP | \| U-3 \| Tier-share arithmetic 24.24 / 54.54 / 21.22 = 100.00 %, against 8/18/7 of 33 shares; Census I → II ratios 75.22 / 76.19… |

### `00_Frame.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 60 | POP | **Population band:** 5 — Regional (~1M–50M), approx. 1,351,430 — Census I: 665,901 humans / 685,529 robots. |
| 61 | POP | CENSUS I GOVERNS (DR-4). Census II, 1,016,495, is also Band 5: no band crossing. |
| 114 | COMP,FOUND,POP | L111) from Russia, China and Australia (`DR-9`, `DRL` L424). 1,351,430 residents at Census I: settled, not staffed. |
| 140 | POP | `EXT` L615: `\| **Mirny** \| Mirny \| 1,351,430 \| 135 \| 193 \| **coastal ice** \|` — under the ruling *"rock and/or ice, |
| 164 | COMP,FOUND | - **Form of words** (`RB` L2316): *a Russia-, China- and Australia-FOUNDED Tepenian city.* **Stock:** exiles from |
| 165 | COMP,FOUND | Russia, China and Australia (`DR-9`), under a long-run composition with China as Primary (`CEN` L376). **People:** |
| 229 | COMP,FOUND | \| D-6 \| **THREE-STOCK FOUNDING** — Russia, China, Australia (`DR-9`), under a long-run Primary of China (`CEN` L376) \| Phase 2… |
| 302 | XCITY | 107:**A second array exists: `…/Mirny_Subnet/Zhongshan_Sonnet/`, `23` files, deliberately held at Phase 3 as a |
| 421 | FOUND | - **RF-4 · Three founding stocks × RV-1.** *Found:* `DR-9` names the stocks and leaves the rename untouched (`DRL` |
| 483 | XCITY | \| Zhongshan \| L402 \| L492 \| L606 \| |
| 538 | COMP,FOUND | - **R-10 · The arrival order of the three founding stocks** *(B)*. *Missing:* `DR-9` names Russia, China and |
| 599 | COMP | communities; under `DR-9`, China is both a founding stock and the long-run Primary. Is the definition meant to |

### `01_Inherited.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 16 | COMP,FOUND | \| 2 \| **The founding by exile** — *"Settled: Post-Falkland Treaty"* (L150, 1–34); built on *"the genuinely substantial, functio… |

### `02_Spine.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 5 | POP | **Frame:** Second Interwar, pre-war · **Census I governs** (1,351,430; `DR-4`, `DR-16`) · **Founders:** exiles from |
| 6 | COMP,FOUND | Russia, China and Australia (`DR-9`) · **No research** (`00_RUNBOOK.md` L2564) · **No other city compared.** |
| 48 | FOUND | \| **STRENGTH** \| **A working station from day one** (`M` L150, 717–786). **A written record centuries deep** — journals, logs, … |
| 74 | COMP | \| **STRENGTH** \| **Fourteen stocks, no majority** — the largest (China) is 24.24 % by construction (`M` L20–22, L32, L47). **Ne… |
| 75 | FOUND | \| **DEFICIT** \| **The founders are a minority of descent** — the three founding stocks, the Primary nation and two of six Signi… |
| 148 | POP | 1,351,430 ÷ 135.14 km² = **10,000 / km²** · ÷ 193.06 km² = **7,000 / km²** (extent from `00_Frame.md`, `EXT` L615). |
| 165 | COMP | - **Borrowed Form:** which of the fourteen stocks carried a way of passing on unwritten skill or reading weather — |

### `03_Research.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 103 | FOUND | ## 6 · Borrowed Form — three founding stocks *(forms in the ancestral repertoire, never traits of the people)* |
| 108 | COMP | - **Chinese:** the Hainan fishermen's **route books** (更路簿) — memorized first, written later, every copy amended by |
| 110 | COMP | Russian and Chinese weather speech already split blowing snow **at head height** (白毛风, "white-hair wind"). |

### `04_Phase_02_Composition_and_Arrival.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 63 | COMP,FOUND | \| 4 \| Three-stock founding under a China-Primary population (`FRM` D-6; `CON` L445 item 4) \| §Founding strata; no order, none … |
| 98 | POP | colonization"*). Mirny: **665,901 humans / 685,529 robots / 1,351,430** (`CEN` L488; `CON` L391). **Tiers** (`CEN` |
| 99 | COMP | L374–376): **Primary** China · **Significant** Japan, UK, South Korea, Russia, Indonesia, Australia *(founding wave)* · |
| 100 | COMP | **Notable** Thailand, Vietnam, Philippines, Malaysia, South Africa, New Zealand, Belarus. Fourteen stocks: 1 + 6 + 7. |
| 103 | COMP,FOUND | background cultural texture."* **Founders** (`DR-9`; `CON` L15): exiles from **Russia, China and Australia**, three |
| 111 | COMP | tier shares: P 24.2424 % S 54.5455 % N 21.2121 % (CON L391 prints 54.54 / 21.22 so the column sums to 100.00) |
| 112 | COMP | founding stocks China 8 + Russia 3 + Australia 3 = 14 of 33 = 42.4242 % |
| 122 | COMP | nation's head count**; (2) *"Fourteen stocks, no majority"* (`SPN` §3 G8 [CORR]) is a property of the weight model, **not a censu… |
| 133 | COMP | and China is both a founder and the Primary. **Nothing rests on the annotation; Australia's founder status rests on `DR-9` |
| 186 | FOUND | \| **Assigned / posted** \| **Fits, derivatively.** Humans *"accompany that population"*; placement follows the robots' (II.3.2).… |
| 235 | COMP | - **P2-4 · The founders are a minority of descent by stock count.** *1st:* three of fourteen stocks; 14 of 33 weights is weight-s… |
| 237 | COMP | layer by weight is mostly material this pass cannot read. *3rd:* **China is both a founding stock and the Primary**, so the censu… |
| 240 | COMP,FOUND | - **P2-5 · Three stocks, three evolved forms of the amended record** (Step 3, [CORR]). Russia, China and Australia were the three… |
| 269 | FOUND | no culture"*): two bodies at near parity; three founding stocks and a Primary with a stated linguistic claim (language **open**, |
| 313 | COMP | - **China stock — route books.** Hainan fishermen's route books: memorized first, written later, every copy amended by its keeper, |
| 323 | COMP,FOUND | **Said plainly: only three of the fourteen stocks were researched, and they are exactly the three founding stocks.** The other el… |
| 329 | COMP | never "what Russians/Chinese/Australians are like." |
| 344 | POP | \| E8 \| **Anyone excluded by the site.** \| Nothing admitted places Mirny in the one category (`RP` L379) where altitude and col… |
| 365 | COMP | \| China \| **Primary** \| 8 \| **Not claimed from the census** (one tier list, no split by body); for the founders, rests on `FT… |
| 374 | FOUND | the totals, the tiers, the robot majority (50.73 %), the arithmetic with its limit, the three founding strata as strata, the exis… |
| 384 | COMP | for the wind like everyone else, of one of fourteen stocks with no majority under the weighting (a pointer only). **Not the typic… |
| 397 | FOUND | \| P2-4 minority of descent by stock count \| the three founding stocks \| the eleven, route unread \| |
| 443 | FOUND | - **Phase 9 (which populations exist).** Candidates the composition supports: the three founding strata (unordered, both bodies);… |
| 487 | FOUND | - **R-10 (existing) · Arrival order of the three founding stocks.** *Instead:* three co-founders, no order; P2-5 is robust to it.… |
| 491 | COMP | fourteen stocks). *Instead:* classify founders only. *Sensitivity:* **high — the largest hole in Phase 2.** |
| 503 | FOUND | grounds for the three stocks were not admitted here.)* |
| 524 | COMP,FOUND | 7. **Killed:** *Sentenced fits robots fully* (against II.2.2's "no finding") · *humans of the founding stratum chose Mirny* (agai… |
| 550 | COMP | \| Eleven of fourteen stocks are non-founders (the robust count) \| B \| all three \| |

### `04_Phase_03_Surface_and_Texture.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 9 | POP | **Frame:** Second Interwar, pre-war · Census I governs (`DR-4`): 665,901 humans / 685,529 robots / 1,351,430 · founders from `DR-… |
| 203 | POP | for a robot's nightly recharge is an indoor place held above freezing, in every month** [D]; at Census I that is 685,529 bodies, … |
| 255 | POP | results, equipment and techniques can cross the gap; personhood cannot. *1st:* a visible boundary between inherited and founder-b… |

### `04_Phase_04_Ordinary_Life.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 7 | POP | **Frame:** Second Interwar, pre-war · Census I governs (`DR-4`): 665,901 humans / 685,529 robots / 1,351,430 · founders from `DR-… |
| 90 | POP | 2. **A workforce unit is not a resident.** 1,018,480 units against 1,351,430 residents is 75.4 %; no claim is made about hours wo… |
| 139 | POP | - *Two energy services, no common unit.* *Human:* only humans eat (`D11`); the national setting is 2,800 kcal/day, a stated choic… |

### `04_Phase_05_Relation_and_Geometry.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 7 | POP | **Frame:** Second Interwar, pre-war (2564–2812; the Long Night War is the terminus) · Census I governs (`DR-4`): 665,901 humans /… |
| 103 | COMP | \| **Exile groups** \| *"exile groups present: Russia, Australia and the Sinian Federation (China)"* (`REG` L57); `DR-46`: *"the … |
| 107 | COMP,FOUND | **Consequences, stated once.** (1) Phases 2–4's three founding stocks are, under `DR-46`, the **three exile groups**; every findi… |
| 160 | XCITY | - *Candidate canon* (`TL` L210–330): before ~2614, *"Everything between Belgrano and Casey realistically would be working"* (L221… |
| 190 | POP | - *2nd.* The demand is standing and large: the prudent recharge default of 685,529 robots in every month, and the human half's he… |
| 207 | XCITY | - **The fallback is the road [IND + D].** Hwy 110 reaches Davis and Casey directly and runs west to the Zhongshan/Sinheung/Shiray… |
| 245 | XCITY | \| **b** \| **By road, Hwy 110** \| `Access type: ON` (`TPL` L6): **a mainline through-stop** on *"Zhongshan → Davis → Mirny → Ca… |
| 249 | COMP | \| **f** \| **Later stocks** (`P2` R-14) — **route level only, never a history** \| `UEIC` L137: Hobart / Fremantle serve the *"E… |
| 325 | XCITY | *1st.* Mirny supplies; Sinheung finishes; the nation values the finished product (`SPN` §6 #10 [CORR]). Sinheung lies on Hwy 4, s… |
| 348 | XCITY | \| Casey, Davis, Zhongshan, Ariun Nuur, Kunlun — relay (`CNC` L274–282, L293–294, L306–307, L323, L335, L350) \| the hardware, un… |
| 351 | XCITY | \| Denison — an engineering parallel (`CNC` L286–288, L478–479) \| comparison \| **held without an admissible reason** (R-60) \| |
| 469 | XCITY | - **RF-4 · Under Shape D, Mirny hosts a relay-point on the Belgrano–Casey chain, and that chain is separate hardware** — a second… |
| 496 | XCITY | - **R-60 · Ties held without an admissible reason or content:** Rothera, Santa Luce, Denison; Sinheung's consulting clause; the c… |
| 509 | XCITY | - **Q-47.** When Mirny's relay fails, who restores it — a Mirny body, a subnet body or a national one — and is there any fallback… |

### `04_Phase_06_Meaning.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 7 | POP | **Frame:** Second Interwar, pre-war (2564–2812; the Long Night War is the terminus) · Census I governs (`DR-4`): 665,901 humans /… |
| 28 | FOUND | \| 2 \| D-6, the three-stock founding → Phase 6 (`FRM`) \| P6-5; no stock's belief written (`NNS`; R-69) \| |
| 51 | COMP | Generators used: G4 (founding: a record with no living layer, the exile, the founders under `DR-46` — the ground of the Name, the… |
| 139 | COMP | **Claimed (each base-level, `DR-4`):** (1) **the Social Contract (P6-1)**, for everyone who crosses, both bodies; (2) **leisure a… |
| 159 | POP | The files' silence on Mirny's dead has two sources, **neither of them in-world:** the developer's reservation (`RV-4`) and the co… |
| 310 | COMP | - **R-69 · Faith and belief at Mirny:** adherents or meeting places of any roster member; human belief and affiliation; the fourt… |

### `04_Phase_07_Order.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 10 | POP | **Frame:** Second Interwar, pre-war (2564–2812; the Long Night War is the terminus; every `Status:` line and post-war section is … |
| 172 | POP | `D16` L2113–2114 lists Mirny's canon §15 composition: Communications/Arcanet ~20 % · Technical/scientific ~20 % · Industrial/manu… |
| 284 | POP | - *2nd.* None is an office. The treaty draft grants the capacity for local councils and laws and a path to self-government; nothi… |
| 350 | POP | \| Humans forbidden at two named extreme sites \| settled protective policy ("it is a genuine safety measure", `RP` L379) \| safe… |
| 469 | COMP | - **By body:** neither is a minority — 50.73 % robots, 49.27 % humans. **By stock, tiers only (`DR-12`; `CON` C-8):** Primary — C… |
| 471 | COMP | - *Act 1:* origin repertoires fresh; composition names the stock and no stock is given a political position (the sequencing rule)… |

### `04_Phase_08_Making.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 17 | POP | - Census I governs (`DR-4`): 665,901 humans / 685,529 robots / 1,351,430. Robots are 50.73 %, and every claim about people names … |
| 21 | COMP | - Primary: China. |
| 169 | COMP | - **C-8** (G8 composition): two bodies at 50.73 / 49.27; fourteen stocks as weights; Primary China. |
| 211 | POP | - **The human half (665,901)** eats from the national five-tier system: |
| 219 | POP | - **The robot half (685,529):** |
| 257 | COMP | ### P8-6 · The transplanted layer: fourteen stocks named, none written *[IND + CORR + D]* · **Act-sensitive** · both bodies |
| 259 | COMP | - *What is not admitted: any stock's food.* No dish is named and none is recalled. A recalled dish is a guess presented as fact, … |
| 457 | POP | - *[CALC]* Textiles are resident-keyed (`D08` L283). Robots are 685,529 ÷ 1,351,430 = 0.5073 → **50.73 %** of the wearers Mirny's… |
| 531 | COMP | - The Primary tier *"shapes the city's primary linguistic and cultural identity"* (`P2` L99, quoting the census [CORR]). At Mirny… |
| 585 | COMP | - *Stock form [RW via `RES` §6; resemblance only, never a carried fact]:* *"Russian and Chinese weather speech already split blow… |
| 643 | COMP | - The fourteen stocks' languages are named only as stocks (R-21, R-96); no tongue is written from a nation's name. |
| 673 | POP | **The typical resident, general answer first.** A robot or a human at near-equal odds: 685,529 ÷ 1,351,430 = 0.5073 → **50.73 % r… |
| 843 | COMP | - **R-96 · The fourteen stocks' repertoires as starting stock** — food, music, dress, craft, games and language, the founding exi… |

### `04_Phase_09_Populations.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 17 | POP | - Census I governs (`DR-4`): 665,901 humans / 685,529 robots / 1,351,430. Robots are 685,529 ÷ 1,351,430 = 0.50726 → **50.73 %** … |
| 20 | COMP | - Composition per Phase 2: Primary China; Significant Japan, UK, South Korea, Russia, Indonesia, Australia; Notable Thailand, Vie… |
| 95 | FOUND | \| `P2` Feeds \| three founding strata (unordered, both bodies); born-here humans; robots built here (if R-13); the founding-robo… |
| 153 | COMP | **The lens decision, made explicitly.** At 50.73 % robots neither body is "non-dominant," so the spine's question is asked of **e… |
| 174 | COMP,POP | - **Who the typical resident is.** A robot or a human at near-equal odds (685,529 ÷ 1,351,430 = 50.73 % robots; 665,901 ÷ 1,351,4… |
| 176 | COMP | - **What the census can and cannot say about kinds of people.** It gives the two bodies and fourteen stocks as long-run shares (`… |
| 180 | COMP | - *Canon.* The outer-city lens anchors robot culture in the Register's founding population (`SPN3` L1059–1060). Mirny's Register … |
| 181 | COMP | - *1st.* The founding lens anchors three of fourteen stocks (`P2` P2-4), and only in Act 1, when *"Origin cultures still FRESH"* … |
| 193 | COMP | - *The two Acts.* **Act 1:** she is still, in her own learned origin, one of the *"Japanese / Chinese / Russian / American / Mexi… |
| 207 | COMP | - *1st.* They are the only humans at Mirny for whom Mirny is the only place. *2nd [D].* **Their ancestry is plural by constructio… |
| 225 | COMP | - *Canon.* Eleven of Mirny's fourteen stocks are not founding stocks (`P2` A.2). Hobart was the port of transfer for people of bo… |
| 303 | COMP | - *Canon.* *Act 1* (2564 → somewhere in the 2600s, a hazy range, `DR-31`): people are still *"Japanese / Chinese / Russian / Amer… |
| 313 | COMP | - *Canon.* Fourteen stocks, as tier weights only (`CON` C-8; `DR-12`); *"a stock does not predict who ran the quarry"* (`P2` L368… |
| 523 | COMP,FOUND | 9. **Upstream inconsistencies recorded, not adjudicated:** `CON` C-4 (L387), `FRM` L164–165 and `SPEC` L152 still name Russia, Ch… |

### `04_Phase_10_Catalog.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 15 | POP | - Census I governs (`DR-4`): 665,901 humans / 685,529 robots / 1,351,430. Robots are 685,529 ÷ 1,351,430 = 0.50726 → **50.73 %** … |
| 258 | POP | \| C2-9 \| **Siligel, coolant, robot coffee, glitch-coolant, vapor products** \| siligel *"flan-set"* (via `P8` P8-1); the rest b… |
| 259 | POP | \| C2-10 \| **Human food from the national pantry** \| five tiers, none sited here (`P8` P8-1; `P4` P4-6) \| the human half (665,… |
| 425 | COMP | - **Planet — CONFIRMED, provisionally: Saturn.** Read from `PLA` L143–155: rings that are debris, not a solid structure; the leas… |
| 441 | POP | **Band 5, declared and not analyzed** (`DR-4`; `01F` L218). The spine's Band 5–6 rule says *delegate to sub-locations; catalog on… |
| 448 | POP | **`00b`'s narrow-object test [CALC].** Workforce units W = 685,529 + 0.5 × 665,901 = 1,018,479.5 ≈ 1,018,480 (`P4` A). The Commun… |

### `04b_T8_Rounds_Phase_10.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 80 | XCITY | agent2 ⛔ LMID MISMATCH claimed='> ⚠ **`⏸️` is a deliberate hold with a named filler, not an ' actual='> Zhongshan.**' |
| 161 | COMP,FOUND | [00.1_Step_MINUS-1_Input_Contract.md:15] is now present, by ruling (hard canon, rb l2786): the founders were exiles from russia, … |
| 162 | FOUND | [00.1_Step_MINUS-1_Input_Contract.md:15] (l150 chars 702-716) is consistent with the ruling as one of three stocks |
| 272 | XCITY | - **G1** (the Planet + Element pair) was cited in earlier phases as deferred and is **used for the first time here**, at §B3 of P… |

### `04b_T8_Rounds_Phase_2.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 128 | FOUND | Contradictions → the most conservative current (post-Round-3) view, the split named. Population-origin material → DEMOTED, never … |

### `04b_T8_Rounds_Phase_5.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 131 | COMP,FOUND | [00.1_Step_MINUS-1_Input_Contract.md:15] is now present, by ruling (hard canon, rb l2786): the founders were exiles from russia, … |
| 132 | FOUND | [00.1_Step_MINUS-1_Input_Contract.md:15] (l150 chars 702-716) is consistent with the ruling as one of three stocks |
| 208 | COMP,FOUND | [04_Phase_05_Relation_and_Geometry.md:105] a russia-, china- and australia-founded tepenian city |

### `04b_T8_Rounds_Phase_6.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 104 | COMP,FOUND | [00.1_Step_MINUS-1_Input_Contract.md:15] is now present, by ruling (hard canon, rb l2786): the founders were exiles from russia, … |
| 105 | FOUND | [00.1_Step_MINUS-1_Input_Contract.md:15] (l150 chars 702-716) is consistent with the ruling as one of three stocks |
| 181 | COMP,FOUND | [04_Phase_05_Relation_and_Geometry.md:105] a russia-, china- and australia-founded tepenian city |
| 296 | POP | [04_Phase_06_Meaning.md:157] is false for the human half : 665,901 humans at census i and a senescence that |

### `04b_T8_Rounds_Phase_7.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 122 | COMP,FOUND | [00.1_Step_MINUS-1_Input_Contract.md:15] is now present, by ruling (hard canon, rb l2786): the founders were exiles from russia, … |
| 123 | FOUND | [00.1_Step_MINUS-1_Input_Contract.md:15] (l150 chars 702-716) is consistent with the ruling as one of three stocks |
| 199 | COMP,FOUND | [04_Phase_05_Relation_and_Geometry.md:105] a russia-, china- and australia-founded tepenian city |
| 314 | POP | [04_Phase_06_Meaning.md:157] is false for the human half : 665,901 humans at census i and a senescence that |

### `04b_T8_Rounds_Phase_8.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 153 | COMP,FOUND | [00.1_Step_MINUS-1_Input_Contract.md:15] is now present, by ruling (hard canon, rb l2786): the founders were exiles from russia, … |
| 154 | FOUND | [00.1_Step_MINUS-1_Input_Contract.md:15] (l150 chars 702-716) is consistent with the ruling as one of three stocks |
| 230 | COMP,FOUND | [04_Phase_05_Relation_and_Geometry.md:105] a russia-, china- and australia-founded tepenian city |
| 345 | POP | [04_Phase_06_Meaning.md:157] is false for the human half : 665,901 humans at census i and a senescence that |
| 490 | COMP | [04_Phase_08_Making.md:581] russian and chinese weather speech already split blowing snow |

### `04b_T8_Rounds_Phase_9.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 128 | COMP,FOUND | [00.1_Step_MINUS-1_Input_Contract.md:15] is now present, by ruling (hard canon, rb l2786): the founders were exiles from russia, … |
| 129 | FOUND | [00.1_Step_MINUS-1_Input_Contract.md:15] (l150 chars 702-716) is consistent with the ruling as one of three stocks |

### `05_Reconciliation.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 88 | COMP,POP | Mirny, read only through its own pass, is a Band 5 Settlement of 1,351,430 at Census I (665,901 humans, 685,529 robots; robots 50… |
| 144 | COMP | \| LC-8 \| `LC:28–30`, `LC:33–35` \| composition note · no American presence at any tier; China alone at Primary; Russia Signific… |
| 146 | COMP | \| LC-10 \| `LC:35` \| Chinese by scale · the city ended up demographically Chinese \| `P2` A.3 (no majority under the weighting;… |
| 152 | COMP | \| LC-16 \| `LC:47` \| demographic shift · later Pacific-corridor immigration made China dominant; Russia settled into Significan… |
| 173 | COMP | \| LC-37 \| `LC:105` \| languages · Mandarin primary, substantial Russian, four others \| `FRM` PA-9, Q-24; `P2` R-21, L296 (a na… |
| 179 | COMP | \| LC-43 \| `LC:122` \| human cuisine · hearty preservation-oriented cold-weather food beside another stock's tradition, coexisti… |
| 198 | COMP | \| LC-62 \| `LC:190` \| belief · Russian Orthodox heritage among families of that ancestry; Chinese-heritage secular and philosop… |
| 222 | COMP | \| LC-84 \| `LC:287` \| demographic-shift placeholder · a later shift to a Chinese majority \| `CEN` L36 (dominant, not majority)… |
| 291 | COMP | **C-1 · Who founded Mirny, and who is the later wave** (`LC:25`, `LC:32`, `LC:41`, `LC:47`, `LC:77`, `LC:178`, `LC:204`, `LC:287`… |
| 327 | COMP | **BT-12 · Chinese by scale, and no majority** (`LC:35` against `P2` A.3; `CEN` L36) `[A BT-11]`. *No scale; different objects:* t… |
| 356 | COMP | \| **D-3** \| `LC` §2 (`LC:47`), §30 (`LC:287`) \| Strike the sequence in which China arrives later and Russia leads the founding… |
| 429 | FOUND | \| `FRM` (RF-1…7) \| RF-7 the spec's dated partial member lists — `LC:235`, `LRC:203` carry the same five-member list (`C-4`) [A]… |
| 474 | COMP | \| PA-53 \| no language assumed \| **contradicts** — `LC:105` proposes Mandarin primary (tier 3); a proposal for R-21; PA-53 stan… |
| 523 | COMP | - **Planet — CONFIRMED, provisionally: Saturn.** Phase 10 tested the file's terms against Phases 1–9: a steep axial tilt that pro… |
| 553 | COMP | 3. **A proposed tongue and register** (Mandarin first, a second fluent community language, direct speech) — seeds for R-21, R-88,… |
| 587 | COMP | \| R-10 / Q-35 (arrival order of the founding stocks) \| `LC:41`, `LC:47`, `LC:77` \| the founding nation's stock first, China la… |
| 589 | COMP | \| R-21 / R-88 / Q-24 / Q-81 / Q-85 (language) \| `LC:105–108` \| Mandarin first, a second fluent language, others; low integrati… |
| 670 | POP | \| `LC` §17, `LRC` §§1, 3, 9 \| professional robots in communications, technical and wind-engineering roles; guild apprentices; r… |
| 719 | FOUND | - **Step 7 (the gates; Gate 3, internal contradictions).** Check the pass internally for: (a) Phase 10's axis clause on the ring … |

### `06_Differentiation.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 133 | COMP | \| **The founders are a minority of descent; the founding nation is a relation, not a stock** \| G4 × G8 \| the founding lens cov… |
| 266 | FOUND | \| PR-8 \| **Stragglers in the pass itself** (III.0's class: founding corrections, census revisions) — the early files still writ… |

### `07_QA_Gates.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 37 | FOUND | \| **E6** \| Founders: the Register (`DR-46`) governs every pass file. The Frame, Inherited, Spine and Phases 2–4 still write the… |
| 67 | COMP | Step 3: 132 of 198 research rows changed a finding (66.7 %; the 66.8 % in one draft counted a header row — corrected). Phase 10: … |
| 100 | COMP | **The closing test** — *could a person live an entire life here, unlike a life in any comparable place?* **Answered honestly (all… |
| 164 | COMP | - **R-156 · Research the fourteen stocks' repertoires as starting stock** (founding exile groups first) **and spend the picks the… |
| 306 | COMP | FRM:L165: ...Australia (DR-9), under a long-run composition with China as Primary (CEN L376). People:... |
| 310 | COMP,FOUND | FRM:L229: ...- Russia, China, Australia (DR-9), under a long-run Primary of China (CEN L376) \| Phase 2's founding strata; Phase … |
| 322 | POP | P2:L96: ...colonization"). Mirny: 665,901 humans / 685,529 robots / 1,351,430 (CEN L488; CON L391). Tiers (CEN... |
| 328 | POP | P2:L342: ...e altitude and cold would kill a human, and Mirny has 665,901 humans (CEN L488). The wind is a preparation gradient f… |
| 338 | COMP,POP | P9:L170: ...1,430 = 50.73 % robots; 665,901 ÷ 1,351,430 = 49.27 % humans [CALC on CEN L488]); of any of fourteen stocks, none a m… |
| 339 | COMP | P9:L172: ...ople. It gives the two bodies and fourteen stocks as long-run shares (CEN L33), no births or deaths (CEN L590), no sp… |
| 346 | COMP | S5:L142: ...an presence at any tier; China alone at Primary; Russia Significant \| CEN L374-376; P2 A.1 \| MATCH after delete-the… |
| 347 | COMP | S5:L144: ...majority under the weighting; China about 24 % by weight, a pointer); CEN L36 (Primary = dominant, not majority) \| B… |
| 349 | COMP | S5:L220: ...demographic-shift placeholder · a later shift to a Chinese majority \| CEN L36 (dominant, not majority); P2 A.3; DR-4… |
| 350 | COMP | S5:L325: ...BT-12 · Chinese by scale, and no majority (LC:35 against P2 A.3; CEN L36) [A BT-11]. No scale; different objects: the… |
| 358 | POP | 488:\| 7 \| Mirny \| Mirny \| 665,901 \| 685,529 \| **1,351,430** \| *(revised 2026-07-04)* \| |
| 359 | POP | 603:\| 6 \| Mirny \| Mirny \| 507,344 \| 509,151 \| **1,016,495** \| \| |
| 457 | COMP | 43:374 \| Primary \| China \| |
| 462 | POP | 50:488 \| 7 \| Mirny \| Mirny \| 665,901 \| 685,529 \| **1,351,430** \| *(revised 2026-07-04)* \| |
| 465 | POP | 56:603 \| 6 \| Mirny \| Mirny \| 507,344 \| 509,151 \| **1,016,495** \| \| |
| 826 | COMP | ### P8-6 · The transplanted layer: fourteen stocks named, none written *[IND + CORR + D]* · **Act-sensitive** |
| 1114 | COMP,FOUND,POP | FRM:L114: ... L111) from Russia, China and Australia (DR-9, DRL L424). 1,351,430 residents at Census I: settled, not staff... |
| 1115 | COMP,FOUND | FRM:L165: ... Russia, China and Australia (DR-9), under a long-run composition with China as Primary (CEN L376)... |
| 1117 | COMP,FOUND,POP | FRM:L114: ... L111) from Russia, China and Australia (DR-9, DRL L424). 1,351,430 residents at Census I: settled, not staff... |
| 1118 | COMP,FOUND | FRM:L164: ...- Form of words (RB L2316): a Russia-, China- and Australia-FOUNDED Tepenian city. Stock: exiles from... |
| 1119 | COMP,FOUND | FRM:L165: ... Russia, China and Australia (DR-9), under a long-run composition with China as Primary (CEN L376)... |
| 1120 | COMP,FOUND | FRM:L229: ...\| D-6 \| THREE-STOCK FOUNDING - Russia, China, Australia (DR-9), under a long-run Primary of China ... |
| 1121 | FOUND | FRM:L421: ...- RF-4 · Three founding stocks × RV-1. Found: DR-9 names the stocks and leaves the rename untouched ... |
| 1122 | COMP,FOUND | FRM:L538: ...- R-10 · The arrival order of the three founding stocks (B). Missing: DR-9 names Russia, China and... |
| 1123 | COMP,FOUND | INH:L16: ...ing population (L152, 1-124, demoted). Founders per DR-9: exiles from Russia, China and Australia \| verdict + admiss… |
| 1124 | POP | SPN:L5: ...econd Interwar, pre-war · Census I governs (1,351,430; DR-4, DR-16) · Founders: exiles from... |
| 1125 | COMP,FOUND | SPN:L6: ...Russia, China and Australia (DR-9) · No research (00_RUNBOOK.md L2564) · No other city compared.... |
| 1126 | FOUND | SPN:L75: ...\| DEFICIT \| The founders are a minority of descent - the three founding stocks, the Primary nation and two of six S… |
| 1127 | FOUND | RES:L103: ...## 6 · Borrowed Form - three founding stocks (forms in the ancestral repertoire, never traits of the people)... |
| 1129 | COMP,FOUND | P2:L101: ...background cultural texture." Founders (DR-9; CON L15): exiles from Russia, China and Australia, three... |
| 1130 | COMP,FOUND | P2:L238: ...e stocks, three evolved forms of the amended record (Step 3, [CORR]). Russia, China and Australia were the three stoc… |
| 1131 | FOUND | P2:L267: ...no culture"): two bodies at near parity; three founding stocks and a Primary with a stated linguistic claim (language… |
| 1132 | COMP,FOUND | P2:L321: ...hree of the fourteen stocks were researched, and they are exactly the three founding stocks. The other eleven... |
| 1133 | FOUND | P2:L395: ...\| P2-4 minority of descent by stock count \| the three founding stocks \| the eleven, route unread \|... |
| 1134 | FOUND | P2:L485: ...- R-10 (existing) · Arrival order of the three founding stocks. Instead: three co-founders, no order; P2-5 is robust … |
| 1135 | POP | P3:L7: ...ensus I governs (DR-4): 665,901 humans / 685,529 robots / 1,351,430 · founders from DR-9 · GPS law applied (the real st… |
| 1136 | POP | P4:L5: ...ensus I governs (DR-4): 665,901 humans / 685,529 robots / 1,351,430 · founders from DR-9 · GPS law applied · no web res… |
| 1137 | FOUND | P5:L105: ...Consequences, stated once. (1) Phases 2-4's three founding stocks are, under DR-46, the three exile groups; every fin… |
| 1138 | COMP,FOUND | P9:L519: ...ot adjudicated: CON C-4 (L387), FRM L164-165 and SPEC L152 still name Russia, China and Australia as founders in DR-9… |
| 1139 | FOUND | S5:L427: ...ts - LC:235, LRC:203 carry the same five-member list (C-4) [A] \| RF-4 three founding stocks × the name - LC:3, LC:43… |
| 1140 | FOUND | S5:L715: ... DR-46 (FRM A.5; P5 Q-46) across every phase that still writes DR-9's three founding stocks; (g) the R-24 downstream … |
| 1296 | POP | P4:L137: ...mon unit. Human: only humans eat (D11); the national setting is 2,800 kcal/day, a stated choice (with a 2,400-3,200 g… |
| 1342 | COMP,FOUND | == POSITIVE CONTROL (founders): FRM L164 'Russia-, China- and Australia-FOUNDED' must hit == |
| 1345 | COMP,FOUND,POP | 07:L114: ... L111) from Russia, China and Australia (DR-9, DRL L424). 1,351,430 residents at Census I: settled,... |
| 1346 | COMP,FOUND | 07:L164: ...- Form of words (RB L2316): a Russia-, China- and Australia-FOUNDED Tepenian city. Stock: exiles from... |
| 1347 | COMP,FOUND | 07:L165: ... Russia, China and Australia (DR-9), under a long-run composition with China as Primary ... |
| 1348 | FOUND | 07:L421: ...- RF-4 · Three founding stocks × RV-1. Found: DR-9 names the stocks and leaves the rename ... |
| 1349 | COMP,FOUND | 07:L538: ...- R-10 · The arrival order of the three founding stocks (B). Missing: DR-9 names Russia, China and... |
| 1351 | COMP,FOUND | 08:L16: ...nding population (L152, 1-124, demoted). Founders per DR-9: exiles from Russia, China and Australia \| verdict + admis… |
| 1352 | COMP,FOUND | 09:L6: ...Russia, China and Australia (DR-9) · No research (00_RUNBOOK.md L2564) · No other city ... |
| 1353 | FOUND | 09:L75: ...\| DEFICIT \| The founders are a minority of descent - the three founding stocks, the Primary nation and two of six Si… |
| 1354 | FOUND | 10:L103: ...## 6 · Borrowed Form - three founding stocks (forms in the ancestral repertoire, never traits of the peo... |
| 1356 | COMP,FOUND | 11:L101: ...background cultural texture." Founders (DR-9; CON L15): exiles from Russia, China and Australia, three... |
| 1357 | COMP | 11:L110: ...founding stocks China 8 + Russia 3 + Australia 3 = 14 of 33 = 42.4242 %... |
| 1360 | COMP,FOUND | 11:L238: ...three evolved forms of the amended record (Step 3, [CORR]). Russia, China and Australia were the three stocks... |
| 1361 | FOUND | 11:L267: ...no culture"): two bodies at near parity; three founding stocks and a Primary with a stated linguistic claim (language… |
| 1362 | COMP,FOUND | 11:L321: ...e fourteen stocks were researched, and they are exactly the three founding stocks. The other eleven... |
| 1363 | FOUND | 11:L395: ...\| P2-4 minority of descent by stock count \| the three founding stocks \| the eleven, route unread \|... |
| 1366 | FOUND | 11:L485: ...- R-10 (existing) · Arrival order of the three founding stocks. Instead: three co-founders, no order; P2-5 is robust … |
| 1370 | POP | 12:L7: ...verns (DR-4): 665,901 humans / 685,529 robots / 1,351,430 · founders from DR-9 · GPS law applied (the real station is a… |
| 1371 | POP | 13:L5: ...verns (DR-4): 665,901 humans / 685,529 robots / 1,351,430 · founders from DR-9 · GPS law applied · no web research · no… |
| 1372 | FOUND | 14:L105: ...Consequences, stated once. (1) Phases 2-4's three founding stocks are, under DR-46, the three exile groups; every fin… |
| 1376 | COMP | 18:L221: ...- Canon. Eleven of Mirny's fourteen stocks are not founding stocks (P2 A.2). Hobart was the port of transfer for peop… |
| 1377 | COMP,FOUND | 18:L519: ...ated: CON C-4 (L387), FRM L164-165 and SPEC L152 still name Russia, China and Australia as founders in DR-9's pre-DR-… |
| 1379 | FOUND | 20:L427: ...5, LRC:203 carry the same five-member list (C-4) [A] \| RF-4 three founding stocks × the name - LC:3, LC:43 read the … |
| 1381 | FOUND | 20:L715: ...M A.5; P5 Q-46) across every phase that still writes DR-9's three founding stocks; (g) the R-24 downstream table (P7 … |
| 1504 | COMP,FOUND | == (d) single-founding-stock residues: 'Russia-founded' \| 'founded by Russia' \| 'Russian founders' \| 'Russia-, China- and Aust… |
| 1671 | POP | \| 7 \| Mirny \| Mirny \| 665,901 \| 685,529 \| **1,351,430** \| *(revised 2026-07-04)* \| |
| 1673 | POP | humans= 665,901 robots= 685,529 combined= **1,351,430** |
| 1675 | POP | `EXT` L615: `\| **Mirny** \| Mirny \| 1,351,430 \| 135 \| 193 \| **coastal ice** \|` — under the ruling *"rock and/or ice, |
| 1680 | POP | P = 665,901 + 685,529 = 1351430 |
| 1689 | POP | Census II check: 507,344 + 509,151 = 1016495 ; relocated = 334935 |
| 1693 | POP | residents 1351430 check 1,351,430: True |
| 1697 | POP | density back-check: 1,351,430/135 = 10011 ; /193 = 7002 |
| 1708 | POP | Census II 507,344+509,151 = 1016495 ; relocated 334935 ; retained 75.22% |
| 1737 | COMP | L374: \| Primary \| China \| |
| 1741 | POP | L488: \| 7 \| Mirny \| Mirny \| 665,901 \| 685,529 \| **1,351,430** \| *(revised 20 |
| 1743 | POP | L603: \| 6 \| Mirny \| Mirny \| 507,344 \| 509,151 \| **1,016,495** \| \| |
| 1789 | POP | P5:L5: ...Frame: Second Interwar, pre-war (2564-2812; the Long Night War is the terminus) · Census I governs (DR-4): 665,901 huma… |
| 1801 | POP | P6:L5: ...Frame: Second Interwar, pre-war (2564-2812; the Long Night War is the terminus) · Census I governs (DR-4): 665,901 huma… |
| 1966 | POP | 14:L5: ...Frame: Second Interwar, pre-war (2564-2812; the Long Night War is the terminus) · Census I governs (DR-4): 665,901 huma… |
| 1969 | POP | 15:L5: ...Frame: Second Interwar, pre-war (2564-2812; the Long Night War is the terminus) · Census I governs (DR-4): 665,901 huma… |

### `08_Review_Panel.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 13 | POP | Opened (all 20 entries of `.t8_required_08_Step8.txt`, in order, at their stated ranges; the readers' logs are in their archived … |
| 184 | COMP,POP | The panel is the pass's own author wearing nine costumes: it redirects attention and gives no second opinion. **It does not check… |

### `Amendment_Rederivation_P06_Meaning_2026-10-29.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 7 | POP | > **Frame:** Second Interwar, pre-war · warm run · Settlement · both bodies named in every claim about people · Act stated where … |
| 166 | FOUND | - **The Borrowed Form, re-read [RW; resemblance only].** Its trigger was the gap "no living teacher". After the first generation … |
| 335 | COMP,FOUND | 8. **Founders' wording differs between admitted lines:** `CON` L387 ("Russia, China and Australia") vs `DRL` L1081–82 (Idelsk-Ura… |

### `Amendment_Rederivation_P07_Order_2026-10-29.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 7 | POP | > **Frame:** Second Interwar, pre-war · warm run · Settlement · Band 5 · both bodies named in every claim about people · Act stat… |
| 316 | COMP,FOUND | 2. **Founders' wording differs between admitted lines:** `CON`/`FRM` "Russia, China and Australia" vs `DR-54` (Idelsk-Uralia; exi… |

### `DR-56_Amendment_Register_2026-10-13.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 35 | COMP | - **fourteen stocks, no majority**; two bodies at near parity with different prices for a misjudgment; |

### `Symbol_Review_2026-10-13.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 14 | COMP | - **Social:** assigned exiles, nobody chose the site (`P2` P2-1); fourteen stocks, no majority; two bodies at near parity; a hub … |
| 22 | COMP | \| **Earth** (rebuilt) \| Mostly empty; strength in the contacts, not the grains; effective stress, liquefaction when contact is … |
| 42 | COMP | - **Survives, independent of `DR-56`:** fourteen stocks with no majority and continuity built from handoffs (*fragments*); season… |

### `ULM_AUTORUN_HANDOFF.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 18 | COMP | - **Real contradictions (six), every one with Tier 1 canon or the ratified spec and none requiring a pass finding to be withdrawn… |
| 81 | COMP | 10. **QA findings (Step 7, FQ-104…FQ-110):** **DECIDED 2026-10-21: all defaults accepted; the wind-condition question is answered… |
| 88 | COMP | **Deferred to Max20x (developer, 2026-10-12):** the cap-starved Mirny research — R-156 (the fourteen stocks' repertoires; eleven … |
| 108 | COMP | 3. **After Max20x:** the cap-starved research: `R-156` (the fourteen stocks' repertoires; eleven never researched) and the picks … |

### `ULM_AUTORUN_STATE.md`

| Line | Category | Text (clipped) |
|--:|---|---|
| 86 | COMP | - 2026-10-12 ~19:00 · DEVELOPER: R-156 (research of the fourteen stocks' repertoires) and the cap-starved picks are deferred unti… |

## 5 · Stale by record: scratch and round files, not edited

- `.t8_*_reader*` and `*_round3_reader*` (reader outputs for Steps 5–10, Phases 2–10 and the two amendment pieces): **86 files.**
- `.t8_*_brief.md`, `.t8_*_CHECKPOINT.md`, `.t8_required_*.txt`, `.t8_Phase10_B3_pair.txt`: **41 files.**
- `*b_T8_Rounds_*` round records (they quote the pass as it stood): **17 files.**
- `_safeguard_probe/` and `assemble_merge5.py`, `assemble_qa7.py`: **29 files.**

All of these describe the pass at the time it ran and are archived at `Archive/ULM_Records/City_Development_Passes/Mirny_Subnet/Mirny/` (`DR-27`). They are not canon and not inputs; they are stale only as records. None was edited.
