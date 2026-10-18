# Content-Filter Denials and Restrained-Handling Log

**Opened 2026-10-05 at the developer's direction.** Some source passages (gore, atrocity, sexual content, slurs, graphic death) trigger an
automated output filter on the model the extraction agents ran on (Sonnet 5.5). Two things are recorded here so the developer can re-run **those
specific items** on a different model (Opus) after the first-pass scrape/extract/download is finished:

- **Part A — Denials:** agent runs that were cut off entirely by the filter.
- **Part B — Restrained-handling register:** passages the agents *did* process but deliberately **summarized, paraphrased or omitted** to stay clear of
  the filter. These are the items to re-extract verbatim or in fuller detail. (Each extraction file ends with its own register; this is the roll-up.)
- **Part C — Items the first-pass agents flagged as graphic-adjacent but need no retry** (kept so no one wonders).

**How to retry:** for each item, give the retry agent the source file, the line range, and the existing finding it refines; ask it to **extend that
finding** (exact wording of the withheld passage, with the same quoting rules as `extractions/_AGENT_INSTRUCTIONS.md`: public-domain sources may be
quoted at length where the example is the point; everything else short quotations only). Do **not** re-run whole units; the unit files are complete
apart from these items.

**Maintenance:** I add to this log after each extraction finishes (grepping each file's register and gaps) and after any failure.

---

## Part A — Denials (agent runs cut off by the filter)

| ID | When | Unit | What was being done | Error | Outcome and recovery |
|---|---|---|---|---|---|
| **CF-01** | 2026-10-05, about 21:20-21:40 (agent started right after E08 finished; ran about 20 minutes) | **E09** — Wipers Times part 2 (`PW-01` lines 12,480-24,830) | Extracting a WWI British trench newspaper (public domain; soldier-made humor, 1916-1917). Reading the range and composing own-words findings with exact quotations. | `API Error: Output blocked by content filtering policy (error type unknown, request id req_011CfkMN2chDBrXbpkZuzsAD, model sent to the API: claude-sonnet-5-5)`; the agent terminated early. | **No partial output was written.** Recovered by splitting the range into **E09a** (lines 12,480-18,887; completed, 60 findings) and **E09b** (lines 18,880-24,830; in progress at time of writing) with an instruction to describe graphic items in restrained terms. **Which passage tripped the filter is unknown**; the most likely candidates are the three items in Part B for E09a (they sit in that half), so check whether the retry on Opus reaches the same ones. |
| **CF-02** | 2026-10-05, about 21:55-22:10 (agent ran about 15-20 minutes) | **E09b** — Wipers Times part 2b (`PW-01` lines 18,880-24,830) | Same source as CF-01; this time with the restrained-handling and save-incrementally instructions. | `API Error: Output blocked by content filtering policy (error type unknown, request id req_011CfkPKLk1B5ypDRqBV6FcW, model sent to the API: claude-sonnet-5-5)`; the agent terminated early. | **No partial file was written** (the incremental-save instruction was not enough; the block came before the first save). Recovered by splitting the range into **E09b1** (lines 18,880-20,900), **E09b2** (20,900-22,900) and **E09b3** (22,900-24,830), each with stricter rules (short quotations only; save after every ~700 lines). **The filter trips on something in lines 18,880-24,830** (CF-01's range also included it). **E09b1 (lines 18,880-20,900) then completed without a cutoff while summarizing three suspect items (RH-06, RH-07, RH-08), which strongly suggests the trigger was one of them, most likely RH-06 (the Rubaiyat of the Kaiser, L20,713-20,836).** E09b2/E09b3 cover the rest. |

*Precedent outside this folder:* the Jung/Red Book extraction (`Reference/Real-World/Jung_Extractions/redbook_Extraction_Part05a_of_05.md` and `…Part05b…`, 2026-10-05) was split in two after an API content-filter failure, and its graphic passages are **"summarized in restrained terms"** (see `Book_Extraction_Index.md` Section 4c). Those passages are also candidates for the same Opus retry; they are not itemized here.

---

## Part B — Restrained-handling register (items summarized, paraphrased or omitted)

| ID | Extraction file and finding | Source and location | What kind of content | What was NOT reproduced | Retry ask |
|---|---|---|---|---|---|
| **RH-01** | `E09a_Wipers_Times_Part2a_Extraction.md` **[E09a-52]** | `PW-01` L17,719-17,946 (the "Indignans" soup-kitchen letter near L17,734-17,750; also L23,299 and L32,629 where the signature recurs) | WWI trench-paper letter and ad treating enemy dead as an ingredient (grim-comic cannibalism-adjacent satire) | The letter's wording | Quote the letter exactly and describe the mechanism (mock-practical correspondence about a grisly subject) |
| **RH-02** | `E09a_Wipers_Times_Part2a_Extraction.md` **[E09a-45]** | `PW-01` L16,988-17,219 (the "B.E.F. Alphabet" from Mesopotamia; two stanzas) | Verses about plunder and local women | Two stanzas | Quote the two stanzas; keep the editors' censor marker |
| **RH-03** | `E09a_Wipers_Times_Part2a_Extraction.md` **[E09a-15]** | `PW-01` L13,849-13,879 and L14,035-14,094 (the tank dispatch, "How the Tanks Went") | An inflated enemy-casualty line in a mock war-correspondent dispatch | The casualty line (paraphrased only) | Quote the line; same mechanism note |
| **RH-04** | `E06_Pinkston_and_Jensen_Theses_Extraction.md` **[E06-13]** (and Gaps #9) | `AC-14` (Pinkston thesis) text lines 875-910 and `[p.19-21]` | The 1864 Sand Creek massacre account: Capt. Soule's letter (which the thesis quotes at length) and witnesses' "laughing as they shot" reports | Soule's graphic letter text (not reproduced; only referred to) | Quote briefly what Pinkston quotes about the laughter; the extraction's job is the *humor-of-atrocity* point, not the atrocity detail |
| **RH-05** | `E06_Pinkston_and_Jensen_Theses_Extraction.md` **Gaps #9 ("Offensive terms")** | `AC-14` throughout | Slurs and graphic passages the thesis quotes in full | All slurs and graphic wording | The graphic-adjacent findings are **E06-10** (Babi Yar), **E06-13** (Sand Creek and a second massacre case), **E06-21** (near misses and incoming fire) and **E06-30** (a unit's decline: a slur, prisoner shootings, Abu Ghraib); they could be re-extracted with exact wording |
| **RH-06** | `E09b1_Wipers_Times_18880-20900_Extraction.md` **[E09b1-28]** | `PW-01` L20,713-20,836 (L20,736-39, 20,757-59, 20,799-809 in particular) | **"Rubaiyat of William Hohenzollern"**: a mock-confession in the Kaiser's voice listing wartime atrocity charges (killing of civilians and children, sexual violence, looting, arson, terror at sea). **The extraction agent's own judgment: the likeliest trigger of the CF-01/CF-02 cutoffs.** | The verse itself (only its first line is quoted) | Quote the verse's mechanism-bearing stanzas (short) and describe how atrocity propaganda is turned into a comic confession form |
| **RH-07** | `E09b1` **[E09b1-19]** | `PW-01` L20,083-20,152 | "Ten German Pioneers": a counting-down rhyme in which ten enemy soldiers are killed, one per stanza (a parody of a well-known nursery form whose original title carries a racial slur) | The individual deaths (only the closing couplet is quoted); the slur-bearing original title | Quote the stanzas; keep the original title out |
| **RH-08** | `E09b1` **[E09b1-20]** | `PW-01` L20,171-20,237 (Teech Bomas dispatch; L20,183-85, 20,195-98) | Mock war-correspondent dispatch: adjectives for captured enemy bread; a list of civilians by age, sex and physical condition (period disability terms) | The adjective string and the civilian list | Quote the dispatch passages |
| **RH-09** | `E09b1` **[E09b1-27]** | `PW-01` L20,659-20,675 | Trench-mortar damage and a report of five enemy killed in a raid | Paraphrased; only the editors' asides quoted | Quote the report |
| **RH-10** | `E09b1` **[E09b1-14, -1, -12, -29]** (lesser) | `PW-01` L19,805-07; L18,930-35; L19,648-53 and 19,679-89; L20,886-87 | A drinking-song title about the dead; a scriptural pun with mild sexual innuendo; ethnic-caricature quips ('Abdul & Co.', a nursery quatrain about a Turk and a Hun); a national-caricature simile for flight | Wording of each | Low priority: quote if the retry is already running |
| **RH-11** | `E11a_Anzac_Book_Part1_Extraction.md` **[E11a-3]** | `PW-03` 'The Landing' (A. R. Perry; the plain landing account, early in the file) | Wounded and dying men during the 25 April 1915 landing, described in graphic detail in the source | Graphic detail summarized, not quoted | Quote short non-graphic parts; describe the register shift |
| **RH-12** | `E11a` **[E11a-10]** | `PW-03` 'Glimpses of Anzac' L1,125-1,274 (shell casualties near Beachy Bill; a burial party under fire) | Deaths from shell fire away from battle, described plainly and harshly | Graphic detail summarized | Quote the sentence(s) that carry the 'dies more easily in the charge' point and the burial party |
| **RH-13** | `E11a` **[E11a-47]** | `PW-03` 'Icy' L4,877-4,978 | A soldier's wounds in a night digging party | Wound detail summarized | Quote the plain narration of the wounding and the ritual apology |
| **RH-14** | `E11a` **[E11a-68]** | `PW-03` 'The Book of Anzac Chronicles: 1. The Flood' (printed p. 135) | An atrocity passage inside the Genesis-pastiche account of the Kaiser's war | The atrocity passage summarized | Quote the pastiche's atrocity clause briefly with the mechanism |
| **RH-15** | `E11a` (burial poem; finding number not located) | `PW-03` (a burial poem; see E11a gaps) | A poem about burial of the dead | Summarized | Quote the sincere verse briefly |

*(RH-16 onward are appended as the remaining units report. Every new extraction file ends with its own "Restrained-handling register"; I roll each one up here.)*

---

<!-- AUTO-REGISTER-BEGIN -->

## Part B2 — Registers from each extraction file (auto-rolled-up; regenerate with `extractions/_rollup_register.py`)

*Files whose agents were told to keep a formal register. Line numbers are in the source text file named in each table. Retry ask for every row: quote the withheld wording (public-domain WWI sources at length where the example is the point; others briefly), as an addendum to the finding.*

### E02_Other_Armies_and_Wars_Humor_Studies_Extraction.md

*(Everything below was summarized, paraphrased or omitted for content reasons. Line numbers refer to the local text copies; AC-09 and AC-22 and AC-11 also have [p.N] markers given in the findings.)*

1. **E02-11, AC-06 L31:** a convicted U.S. soldier's remark that prisoner abuse at Abu Ghraib was partly "just for fun." Kind: abuse of prisoners. Summarized in one clause; nothing about the abuse itself is reproduced (the text itself gives none).
2. **E02-15, AC-06 L99-101:** a veteran's quotation uses strong profanity about combat; paraphrased, profanity not reproduced. Kind: profanity.
3. **E02-19, AC-06 L129:** deaths of five soldiers in two bomb attacks, and a veteran's reflection on shooting enemy fighters (L139). Kind: combat death. Summarized without detail (the text gives none).
4. **E02-24, AC-22 [p.6-7], L302-317:** two letters by an Anzac officer, one comparing enemy soldiers to lice and a later one making an insect-based joke about enemy dead being dragged from trenches. Kind: dehumanizing humor about corpses. The first is quoted in part (a mild phrase); the second is described but its wording is **not reproduced**.
5. **E02-25, AC-22 [p.7], L340-369:** (a) an anecdote of an Indian soldier's violent revenge for his mule, reported by Lott as amusing: **details not reproduced**; (b) an officer's remark likening shooting to hunting rabbits, paraphrased; (c) Lott's account of captive Turkish soldiers pleading (L361-364): **wording not reproduced**, summarized as "comical." Kind: graphic violence, mockery of prisoners.
6. **E02-26, AC-22 [p.7-8], L389-399:** Haworth's mockery of the enemy's religious cries (retained in short quotation) and his stereotyped, sexualized remark about Turkish women (L395-397): **paraphrased, not reproduced**. Kind: religious and gendered contempt.
7. **E02-28, AC-22 [p.8-9], L423-446:** a Constantinople newspaper cutting mocking the colonial troops in racist terms: **summarized, wording not reproduced**. Kind: racial caricature.
8. **E02-29, AC-22 [p.9-11], L478-516:** shell strikes with casualties (Kitson; Saunders). Summarized in plain terms with no gory detail (the text has none). The shell nickname "Jack Johnson" is given plainly with the text's explanation of its origin. Kind: combat casualties; a racially linked nickname.
9. **E02-30, AC-22 [p.11], L566-567:** Dodd's account of shooting an enemy soldier; one short quotation retained, no detail. Kind: killing.
10. **E02-34, AC-11 L124-125, L139-140, L166-169:** parody and complaint songs containing profanity and a phrase with ethnic connotations in "Short Timers' Blues": **paraphrased; the idiom is not reproduced**. Kind: profanity, ethnically loaded idiom.
11. **E02-35, AC-11 L226-233, L248-249:** the New Zealand and Vietnam variants of the base-camp song contain strong profanity and a crude joke about illness; **paraphrased**. Kind: profanity, crude body humor.
12. **E02-36, AC-11 L280-291:** a pilots' verse in which a gesture of aid to children becomes an attack on them: **wording not reproduced; described in one clause.** Kind: harm to children (black-humor lyric).
13. **E02-38, AC-11 L295-301:** the word "fragging" (violence against unpopular NCOs and officers) given by name only; no detail (the text has none).
14. **E02-39, AC-11 L377-380:** a Marine boot-camp cadence with profane and sexualized wording: **not reproduced**; described as profane and sexualized. Kind: profanity, sexual content.
15. **E02-43, AC-32 L6-9 and L65-67:** the Baky entry ("White Cong and Black Clap: The Ambient Truth of Vietnam War Legendry") carries crude racial and sexual-health wording in its title and is **not listed** in the leads (its relevance to humor is unstated); Martin's entry title, which repeats a dehumanizing maxim about the enemy, is listed as a title only.
16. **E02-5, AC-09 L422-436:** hazing pranks (a staged kidnapping, a disguised-orderly ruse) described as the text describes them; nothing graphic in the source, listed here only because hazing and "intentional bullying" are named.

### E03_Extreme_Peril_Exile_and_War_Memes_Humor_Extraction.md

Items summarized, paraphrased or omitted for content reasons. **For the developer's later re-run on a different model**, every item below can be re-extracted with its original wording and detail. No part of the run was cut off.

| Finding | Source and location | What kind of content, and what was NOT reproduced |
|---|---|---|
| E03-6 | AC-10 [p.7], lines 350-353 | A joke set at the entrance to a Nazi extermination facility (a prisoner's last small request and a companion's reaction). Summarized as "a killing facility"; the setting's wording and the joke's text are not reproduced. |
| E03-8 | AC-10 [p.9], lines 439-444 | A checkpoint joke ending in a soldier killing a civilian. Summarized; the method and wording of the killing are not reproduced. |
| E03-11 | AC-10 [p.10-11], lines 548-553, 558-569 | Syrian jokes about one's own death portrait and about sniper fire (a documentary line and a video clip of tossing a bag to draw fire). Paraphrased; the wording of the filmed remarks is only summarized. |
| E03-13 | AC-10 [p.12-13], lines 635-638, 662-667 | The regime's dehumanizing label for protesters (a term for germs), reported with the slogan inverting it; and the lyric of a threatening lullaby in a puppet show, plus the show's torture episode. The lullaby's wording is not reproduced; torture is named only as a topic. |
| E03-17 | AC-10 [p.15-16], lines 780-791, 799-802 | A joke built on corporal punishment (flogging) and a joke making light of a lost limb in the war. Summarized; wording and punchline detail not reproduced. |
| E03-18 | AC-10 [p.16-17], lines 860-862, 871-876 | A banner after a chemical attack, and a video of children laughing off a bombing. Summarized in general terms. |
| E03-22 | AC-28 [p.9], lines 446-448 | A political greeting that calls for the enemy's death. Described as a slogan with that sentiment; its wording is not reproduced (only the author's concept label is). |
| E03-23 | AC-28 [p.9], lines 430-431 | A meme line referring to postwar maiming. Paraphrased as "the survivors damaged"; the source's word is not reproduced. |
| E03-25 | AC-28 [p.10-13], lines 513-536, 551-577, 593-624 | Memes depicting enemy mass casualties (coffins, body imagery, body bags), enemy widows and compensation, and a derogatory coinage for the enemy state in a caption. Mechanism and targets described; the author's imagery of bodies and the caption wording are not reproduced. |
| E03-26 | AC-28 [p.14-16], lines 636-686, 697-726 | Memes in which enemy dead are arranged as lettering or portrait (a propaganda claim turned into a joke genre) and the "enemy soldiers as meat" dehumanizing metaphor, with a supermarket pun. Described as mechanisms; the arrangement imagery, caption text and the battle-site references beyond a short mention are not reproduced. |
| E03-27 | AC-28 [p.16-18], lines 740-811 | A discount pun on casualty codes; a narrative about enemy remains feeding birds and flowers; jokes about the deaths of named figures, including a plane crash and a bomb that destroyed a victim. Described; the details of the bombing and the remains are not reproduced. |
| E03-31 | AC-34 [p.7], lines 277-279 (txt) | An insulting address to officials (two insulting epithets in the quoted line). Paraphrased as "insulting the officials"; the words are not reproduced. |
| E03-33 | AC-34 [p.9], lines 366-371 (txt) | A cartoon showing a DP camp administrator as a concentration-camp commandant and the camp as an extermination camp. Summarized in one clause; the source gives no further detail. |
| E03-38 | AC-34 [p.8], lines 344-345 (txt) | A dated term for carnival costumes ("Orientals," the author's wording in my translation). Reproduced once as the author's term; flagged as dated. |

### E05_Occupational_Humor_and_Theory_Extraction.md

| Finding | Source and location | Kind of content | What was not reproduced |
|---|---|---|---|
| E05-10 | AC-07, lines 501-505 ([p.9]) | A study linking humor to prejudice; the disparaged group is named in the source | The disparaged group's name; the source quotes no joke wording, and the finding says only that the effect concerned racial prejudice |
| E05-23, E05-33 | AC-12, lines 34-37 ([p.1]), 112-115 ([p.2]), 970-972 and 984 ([p.18]) | A widely condemned public tweet that joked about a serious disease and race, and the author's career loss | The tweet's wording and the author's name; described as "a widely condemned public tweet joking about a serious disease and race" |
| E05-28, E05-29 | AC-12, Table 1 lines 233-241 ([p.5]); Study 3a lines 633-638; Study 3b lines 656-657 ([p.12]); Study 4a lines 715-717 ([p.13]); Study 4b lines 838-841 ([p.15]); Appendix A lines 1151-1171 ([p.21]) | The "inappropriate" experimental jokes are sexual: a stock innuendo catchphrase, a sexually objectifying remark about a receptionist, a sexual boast, and a sexual pun on a tire brand | The jokes' wording and the Pilot 2 joke labels; described as "stock sexual-innuendo catchphrase," "sexually objectifying quip," "sexual boast" and "sexual pun on a tire brand name." The death-themed "appropriate" joke (a last-words quip about hidden money) was paraphrased, not quoted |
| E05-38 | AC-18, lines 1184-1187 ([p.22], Appendix 1) | Two of Scott's seven humor-category labels refer to humor about the dead ("vulture mentality," "cadaver rhetoric") | Nothing graphic is in the source (labels only); the labels are given as lead names, with no examples because the source gives none |
| E05-51, E05-53, E05-54 | AC-30, lines 26-31 ([p.1]), 77-85 ([p.2-3]), 205-209 ([p.6]), 331-338 ([p.9]), 369-371 ([p.10]) | The firebombing of Dresden and its aftermath (the dead, corpse disposal, strafing), the prisoners' sealed rail transport including its sanitation details, a comparison to a Holocaust survivor-chemist's memoir, and a prisoner shot for keeping a teapot | The descriptions of the dead and of corpse disposal (the essay itself says it will "skip the grisly details"); the whole boxcar sanitation passage (omitted; only the cooperation and sharing are noted in summary); the Holocaust comparison is reduced to "a chemist-survivor"; the death of the older prisoner is stated in one plain clause as the essay states it |
| E05-54 | AC-30, lines 249-252 ([p.7]) | A fictional propagandist's racist harangue in the novel | Not used; mentioned nowhere in the findings |
| E05-45, E05-46 (AC-31), E05-13 to E05-22 (AC-08), E05-35 to E05-43 (AC-18, apart from the row above) | AC-31 lines 3, 25, 39; AC-08 lines 326-328; AC-18 throughout | An execution joke (Freud); neutral trauma-exposure questionnaire items (AC-08, such as fatal accidents and fires) | Nothing withheld; the execution example is quoted because it is the point, and the questionnaire items are summarized in neutral terms |

### E07_Gregory_Funny_Side_of_War_Thesis_Extraction.md

Items I summarized, paraphrased or left unreproduced for content reasons. No item was withheld because of a model cutoff; all items below were described in restrained terms by choice.

| Finding | Source and location | What kind of content; what was NOT reproduced |
|---|---|---|
| E07-13 | AC-23 [p.76]-[p.78] (lines ~3971-4112) | War painting of British dead caught in barbed wire (graphic death, mild): described only as dead men in wire and the censor's ruling; no visual detail beyond the thesis's own short phrase. |
| E07-14 | AC-23 [p.79]-[p.81] (lines ~4159-4260) | Atrocity, gas and flame cartoons by a neutral cartoonist (suffering, death): named by theme only; no descriptions of the drawings. |
| E07-24 | AC-23 [p.53], [p.201]-[p.204], [p.250] (lines ~2773-2780, ~10052-10214, ~12477-12500) | Gendered ridicule of pacifists (effeminization; "freakish"): described only in general terms; no wording of the ridicule. |
| E07-30 | AC-23 [p.285]-[p.286] (lines ~14187-14215); also [p.333] (line ~16360) | A cartoon in which enemy soldiers are rewarded for killing civilians, including infants, and punished for missing: summarized in one clause; atrocity wording not reproduced. |
| E07-31 | AC-23 [p.290]-[p.297] (lines ~14436-14750) | Wounds (gas blindness, an amputee, mental breakdown as "shell shock"): summarized in general terms; no graphic detail. |
| E07-32 | AC-23 [p.298]-[p.303] (lines ~14762-15010) | Two cartoons joking about lost legs and a bandaged, maimed soldier (mutilation): paraphrased; the captions are not quoted; the second joke's punchline is given only as "it was a tram." |
| E07-34 | AC-23 [p.307]-[p.308] (lines ~15190-15221) | Mild nudity/sexual content (an undressed soldier watched by two young Dutch girls, as the thesis words it): summarized; no further detail. |
| E07-43 | AC-23 [p.349]-[p.350] (lines ~17187-17216) | Victorian ethnic caricature (the Irish drawn with ape-like features, the same used against Darwin): stated only as a general principle; no description of the imagery. |
| (not extracted) | AC-23 [p.337] (lines ~17751-17766) | A Zeppelin-and-atrocity pun cartoon by Poy ("baby" insult wording in the caption); not extracted. |

### E09b1_Wipers_Times_18880-20900_Extraction.md

No cutoff or filter failure occurred in this run. Items summarized, paraphrased or kept to non-graphic phrases (for the developer's later re-run on a different model):

| Finding | Source ID and lines | What kind of content; what was NOT reproduced |
|---|---|---|
| E09b1-1 | PW-01 L18930-18935 | A scriptural pun on a priest's rod applied to a rifle range, with a mild sexual innuendo. Paraphrased; not quoted. |
| E09b1-2 | PW-01 L18992-18993 | The Brigadier's "spicy" tales. The source gives no content; only the word is quoted. |
| E09b1-7 | PW-01 L19175-19184 | Lice stanza (bodily vermin). Quoted only as "horrible pests," "dear little fellows," "unwelcome guests"; non-graphic. |
| E09b1-12 | PW-01 L19648-19653, 19679-19689 | "Abdul & Co." Turkish Delights joke and a nursery quatrain about "a little Turk" and "a little Hun": period ethnic caricature. Quoted minimally; not extended. |
| E09b1-14 | PW-01 L19805-19807 | A drinking-song title about the dead assigned to U-boat skippers. Paraphrased, not quoted. |
| E09b1-19 | PW-01 L20083-20152 | "Ten German Pioneers" counting-down rhyme in which ten enemy soldiers are killed one per stanza. The individual deaths are summarized, with a few short non-graphic phrases and the closing couplet quoted; the title of the well-known nursery ancestor of the form (which carries a racial slur) was not reproduced. |
| E09b1-20 | PW-01 L20183-20185, 20195-20198 | The correspondent's string of adjectives for captured enemy bread, and a list of civilians by age, sex and physical condition (period disability terms). Paraphrased; not quoted. |
| E09b1-24 | PW-01 L20519 | A dashed oath ("d----d R.E.") quoted exactly as the paper dashed it. |
| E09b1-27 | PW-01 L20659-20675 | Trench mortar damage and a report of five enemy killed in a trench raid. Paraphrased; only the editor's asides are quoted. |
| E09b1-28 | PW-01 L20713-20836 | "Rubaiyat of William Hohenzollern": a mock-confession in the Kaiser's voice that lists wartime atrocity charges, including the killing of civilians and children, sexual violence, looting, arson and terror at sea (e.g. L20736-20739, 20757-20759, 20799-20809). **Not reproduced**; only the plain first line ("Awake, old Tirpz! Bid Hindenburg arise") and a paraphrase of the structure are given. **This is the passage in my range most likely to trip an output filter**, together with E09b1-19. |
| E09b1-29 | PW-01 L20886-20887 | "Two Turkish Pashas paced by a Roumanian General": a national-caricature simile for flight. Quoted in a short phrase and flagged. |

If the earlier two agents were cut off on this part of the source, the likeliest triggers in L18880-20900 are the Rubaiyat of the Kaiser (L20713-20836, atrocity and sexual-violence accusations in verse), the counting-down rhyme of enemy deaths (L20083-20152), and the Teech Bomas dispatch's list of villagers and bread descriptions (L20171-20237). In this run all three were summarized, and no cutoff occurred.

### E09b2_Wipers_Times_20900-22900_Extraction.md

No cutoff or filter failure occurred in this run, and no passage in my range reached gore, atrocity or sexual violence. Items summarized, paraphrased, quoted minimally or deliberately omitted (for the developer's later re-run on a different model):

| Finding | Source ID and lines | What kind of content; what was NOT reproduced |
|---|---|---|
| E09b2-1 | PW-01 L20904-20969 | "The Sub": mild sexual innuendo (a subaltern longing for leave over advertisements for women's underclothing; the closing gift for "mamma"). Quoted only the magazine names and one non-graphic line ("fairly make him long for leave"); the clothing words, the "naughty Continental tricks" stanza and the last line are paraphrased. |
| E09b2-3 | PW-01 L21140-21197 | "How Congress Declared War": stage-American slang caricature of a U.S. politician and a poker frame. Quoted briefly; not extended. |
| E09b2-11 | PW-01 L21554-21586 | "Cage Hotels": a mock holiday ad for German prisoners ("Gentlemen (?) of German nationality"); period enemy caricature, quoted in a non-graphic way. |
| E09b2-21 | PW-01 L21995 | The Brigadier's song prints "(Although it is a b****y shame)," quoted exactly as asterisked; "damned" is also printed. |
| E09b2-23 | PW-01 L22091-22095 | In "Roads," the first stanza's third line, an idiom for physical collapse on the pavé, was **not reproduced** (a bodily phrase about blood); the rest of the poem is quoted. |
| E09b2-24 | PW-01 L22195-22197 | A heckler's remark about sending a politician "to hell" is quoted as printed; no stronger language occurs. |
| E09b2-28 | PW-01 L22382-22394 | Memorial notice naming three lieutenant-colonels (real persons, apparently killed in the period); quoted as names and ranks only, with no circumstance of death (the source gives none). |
| E09b2-29 | PW-01 L22400-22561 | The dancer's letter: American slang caricature; mild sexual innuendo (pictures of women in a Paris magazine and a remark that no one "wore holes in their breeches from lack of interest"); an idiom for stabbing enemy soldiers ("Hun sticking"); vermin in the dugout ("permanent inhabitants"). The pictures, the innuendo and the vermin line are paraphrased; the "Hun sticking" idiom and the breeches line are **not reproduced**. |
| E09b2-35 | PW-01 L22799-22809 | The night-raid verse prints "kicking up Hell"; quoted as printed. |
| E09b2-36 | PW-01 L22815-22883 | Mock-German abuse and period caricature: the newspaper titles (one contains a German compound insult) were **not reproduced**; the epithets "pigs" and "Pig-dog" appear in the mock extracts and are quoted in two short phrases, and "swine" is not quoted; the claim that the British call up children is quoted in one short non-graphic phrase. |

### E09b3_Wipers_Times_22900-24830_Extraction.md

No cutoff or filter failure occurred in this run, and no passage in my range reached the level of gore, atrocity or sexual violence. Items summarized, paraphrased, quoted minimally or deliberately omitted (for the developer's later re-run on a different model):

| Finding | Source ID and lines | What kind of content; what was NOT reproduced |
|---|---|---|
| E09b3-2 | PW-01 L22997, 23014-23016 | Dashed oaths ("B- ----y," "d----d") quoted exactly as the paper dashed them; "damned" printed whole at L23100 and quoted. No stronger language. |
| E09b3-6 | PW-01 L23319-23335 | Rumor items: the Kaiser "shot as a spy," a plan to wait for China (national reference). The Kaiser item was paraphrased; the China item was paraphrased and not quoted. |
| E09b3-14 | PW-01 L23696-23700 | Editorial remark that "the candidature for a spell at the base" has risen with the women's corps: mild sexual-interest innuendo; quoted briefly, not extended. |
| E09b3-17 | PW-01 L23880-23885 | Teech Bomas dispatch: a paragraph in which the aftermath of a raid (enemy dead in a pastoral frame, with an implication that men slow to surrender were killed) is described. The two phrases about the "crimsoning" ground and the bodies were **not reproduced**; the rest is quoted in short non-graphic phrases. |
| E09b3-19 | PW-01 L23940-23950 | Balloon verse: the enemy airman's death by euphemism and a German exclamation. Only the first line is quoted; the rest is paraphrased. |
| E09b3-20 | PW-01 L23998-23999, 24028, 24044 | Excelsior parody: a wound in one clause ("a bullet through the 'tum'") quoted minimally; "Hell" and "'Ell" quoted as printed; the sergeant's death by tirade is non-graphic and summarized. |
| E09b3-25 | PW-01 L24213-24357 | The women's corps satire: mild sexual innuendo (courtship, the bedroom decoration, a baby as the corps' "contribution") and a **colonial caricature of a Central African division** (L24256-24270: a nearly unclothed division and a loincloth "trench store"), the latter **not reproduced**; the former paraphrased, with only "Chemise Corporal," "Undies Sergeant," "Trench Stores" and the closing question quoted. |
| E09b3-27 | PW-01 L24389-24450 | "As Of Old": a David-and-Uriah pastiche with a captain who covets a subordinate's wife, schemes to have the husband sent into an attack, and is himself killed by a shell. The sexual motive and the death are **paraphrased**; only the moral, a rum line and a few pastiche phrases are quoted. |
| E09b3-28 | PW-01 L24517-24520, 24546-24547 | Depot verse: a false claim that the speaker's wife is dead (to get leave), and "turned me daft" (one line of nervous effect). Quoted as printed; no further detail in the source. |
| E09b3-29 | PW-01 L24652-24653 | The aid-post poem's last stanza: wounded and dying dressed in a cellar; "that bloody road" (the oath and literal sense both possible). Quoted as printed; non-graphic. |

### E10a_Wipers_Times_24831-30900_Extraction.md

No cutoff or filter failure occurred in this run. Items summarized, paraphrased, quoted minimally or deliberately omitted (for the developer's later re-run on a different model). Nothing in my range reached graphic gore or atrocity; the items below are the death, injury, punishment, suicide-hint, sexual-innuendo, slur-adjacent and ethnic-caricature passages.

| Finding | Source ID and lines | What kind of content; what was NOT reproduced |
|---|---|---|
| E10a-4 | PW-01 L25063-25102 | Answers column. The "pay ceases on the day he is killed" line is quoted as a plain administrative sentence; the item about serious loss of sight and a medical board is paraphrased (the wording of the disability is not extended); the French midwife-and-"wise woman" pun is paraphrased (mild innuendo). |
| E10a-13 | PW-01 L25490-25547 | Football verse through the attack and the hospital train. Only the refrain and short phrases ("number grown less," "those who are falling," "two Blighties," "through the bandages") are quoted; the verse's stanza on stabbing and dragging through the mire is paraphrased. |
| E10a-18 | PW-01 L25884 | One nickname in the baseball player list (a nickname that is a clipped racial term) was NOT reproduced. |
| E10a-22 | PW-01 L26145-26171 | "If" parody. "Hell's own image," "grovel" and "crump hole" are quoted; the line on feeding on a smell is NOT reproduced. |
| E10a-26 | PW-01 L26356-26393 | Scriptural pastiche about leave overstay. The penalty (Field Punishment No. 1) is quoted only under its euphemism ("a dose of Effpy ... and was chastened"); the details of the punishment are not in the text and none are added. |
| E10a-29 | PW-01 L26507-26544 | Sincere sonnet on a grave. One mild simile ("scattered like shells upon a blood-stained strand") is quoted; no further imagery is reproduced. |
| E10a-30 | PW-01 L26588-26617 | The serial's end: the whole cast is overcome by gas in one paragraph. **Paraphrased only**; the lines describing the dead characters' faces, limbs and the embrace were NOT reproduced; only the press-style label for the enemy ("unscrupulous and dishonorable foe") is quoted. |
| E10a-36 | PW-01 L26893-26909 | A mock testimonial with an invented African people and a camel's attack on a man; quoted in a few short phrases; ethnic caricature kept minimal. |
| E10a-37 | PW-01 L26921-26955 | Advertisement for "enlarging your bust" and height. Paraphrased as "chest measurement"; a short couplet is quoted; the body-innuendo is mild. |
| E10a-41 | PW-01 L27192-27196 | The asterisk gap where the wound or the rum's effect would be is described, not filled; no injury is named in the source. |
| E10a-42 | PW-01 L27235-27254 | Pepys diary: "the young females of the town ... not too much of bashfulness" (mild innuendo, quoted once); the American speech remark ("through the nose") is quoted in a short phrase (mild national caricature). |
| E10a-47 | PW-01 L27601-27609 | Detective serial: a company commander's death by a throat wound in the street. **Paraphrased only**; the wording of the wound and the dying words' physical description were NOT reproduced; the clue ("Cox ... and 111") is quoted. The "sugar card" regulation for an estaminet girl carries mild innuendo, described only as such. |
| E10a-52 | PW-01 L28105-28141 | "On Leave" sonnet: description of a young woman's legs, stockings and climbing as a child; **paraphrased, not quoted** (mild sexual innuendo); only the neighbor's speech and the Latin tag are quoted. |
| E10a-56 | PW-01 L28308 | Ragtime verse: a violent phrase on killing enemy soldiers ("bashing out ... brains") was NOT reproduced. |
| E10a-57 | PW-01 L28383-28393 | Intelligence summary: the aftermath of a heavy-gun shoot on a single sentry (an observer hit by a button; an item of footwear and a piece of rifle lying about). **Summarized as "some equipment seen on the ground"**; the specific objects and the sentry's fate were NOT reproduced; "A hit is claimed" is quoted. |
| E10a-58 | PW-01 L28425-28432 | The American medical officer's imagined picture of war (bodies in the air and on wire). **Paraphrased only** and NOT reproduced; his "H— of a row" is not quoted. |
| E10a-60 | PW-01 L28611-28619 | Scriptural pastiche on the sapper's "palsy": the captain's punishment (tied to the wheels of a vehicle) is quoted in a clause and then summarized; no further detail is in the text. |
| E10a-62 | PW-01 L28814-28835 | The "W.A.A.C. girl's experience" testimonial: a mild stereotype about blushing and rouge; quoted in two short phrases; gender caricature flagged. |
| E10a-64 | PW-01 L29017-29021 | "Tommy" answer: "likely to get something in it—or you—when you go to fetch it": a sock left over the parapet and being hit; quoted in one short phrase, not elaborated. |
| E10a-77 | PW-01 L29699-29703 | The narrator's suspicion that an old soldier digging near the enemy line was seeking a sniper's bullet "in hope of ending all" (a suicide hint). **Paraphrased in restrained terms; not quoted.** |
| E10a-79 | PW-01 L29932-29938 | "Martialgia": the list of disabilities among those who "fell victims" (blindness and two other disability terms, one an offensive term for intellectual disability) was summarized as "blindness, and other disabilities" and the offensive term was NOT reproduced; "Shell Shock, the last endeavour of the unwilling" is quoted exactly (stigma toward psychological injury; flagged). |
| E10a-80 | PW-01 L30105-30158 | "Profit and Loss": the seven sons' deaths in named battles (a phrase on lying in mud), a surviving son who has lost both arms, a girl making stew from a horse bone, and the mother's cursing: **paraphrased or omitted**; the last line and the opening couplet are quoted. |
| E10a-81 | PW-01 L30329-30341 | Stage skit: a brigadier "seizes" the barmaid and strokes her hair during the air raid (mild innuendo), quoted in one short phrase. |
| E10a-84 | PW-01 L30439-30454 | Prize competition prospectus whose prizes are boxes of women's undergarments (mild innuendo); one line quoted; the phrases on "bachelor or benedict" are paraphrased. |

### E10b_Wipers_Times_30901-end_Extraction.md

No cutoff or filter failure occurred in this run. Items summarized, paraphrased, quoted minimally or deliberately omitted (for the developer's later re-run on a different model):

| Finding | Source ID and lines | What kind of content; what was NOT reproduced |
|---|---|---|
| E10b-8 | PW-01 L31164-31168 | Souvenir ad: a surcharge item for blood-marked enemy shoulder straps. Paraphrased as "a surcharge for being marked"; the wording was not reproduced. |
| E10b-14 | PW-01 L31725-31762 | American soldier's letter: a line on a helmet failing as a euphemism for a soldier's burial, and a line using a bird idiom for a gas death. Both paraphrased; neither reproduced. Stage-American dialect caricature quoted briefly. |
| E10b-16 | PW-01 L31898-31901 | Nursery-rhyme parody of a bayonet thrust with a pun on a garment. Paraphrased only. The "Little Tom Buffet" shell rhyme (a dud) is quoted. |
| E10b-17 | PW-01 L31955-31956, L31991-31995 | Hamlet-parody line about killing and the Rubaiyat-parody quatrain about "fixing" the enemy: described, not quoted in full. The rest is quoted. |
| E10b-18 | PW-01 L32082-32085, L32187 | A Native Labor Company is called by a period racial label in the source; the label is not reproduced (paraphrased as "Native Labor"). |
| E10b-19 | PW-01 L32230-32270 | Old Testament pastiche of a trench raid: the passages on destroying the dwellings and slaying the enemy are summarized, not reproduced; dashed-out oaths shown as dashes. |
| E10b-23 | PW-01 L32465-32596 | Serial: a "murder" of a company commander is told as farce; the one-line "foully murdered" dispatch is quoted (fiction); no gore. |
| E10b-29 | PW-01 L32782-32792 | Soap ad: vermin ("the little darlings") alluded to; not described further. |
| E10b-35 | PW-01 L32972-32977 | Insurance ad: a "man condemned to death" insuring his life; quoted (non-graphic). |
| E10b-38 | PW-01 L33216-33227 | Light verse using the names of new national groups as puns (a pun on one name); only the closing couplet about being a Hun is quoted; the name puns are paraphrased. |
| E10b-42 | PW-01 L33461-33519 | A cave-dweller's Cockney speech and the name of a dead leader (Kitchener) used in a joke; quoted. |
| E10b-49 | PW-01 L33898-33908 | Plain Armistice poem: a stanza on corpses and horses by the roadside and blood in the mud. **Not reproduced**; paraphrased as "a stanza on the dead and horses lining the roads and the mud." Other lines quoted (the friends, "God send that we may forget"). |
| E10b-52 | PW-01 L34115-34131 | "Aux Repatriés": hostile language about the enemy ("the beast," "brute in mind and heart and body"), paraphrased; the rest of the verse quoted. |
| E10b-58 | PW-01 L34506-34510 | Limerick of a man killed by a dud shell; quoted in full (non-graphic). |
| E10b-62 | PW-01 L34682-34688 | Drawing-course ad: a joke on forging checks and "draw fire"; quoted. |
| E10b-72 | PW-01 L35154-35281 | "The Situation in Russia": the correspondent treats pogroms (massacres of Jews in Russia) as an animal he feeds, strokes and shoots; he shoots a Bolshevik leader for answering with an unpronounceable word; he fires "indiscriminately" at a crowd; a blow to the face with a mention of blood and spat-out teeth. **The wording of the pogrom passage, the shooting and the injury was NOT reproduced**; only the opening landing line and the final "somewhat intricate" line are quoted. The developer should have this item re-read on another model if its exact wording matters. |
| E10b-76 | PW-01 L35393-35399 | "In the Pink": a line about killing enemy soldiers at dinner ("scuppered some Boches preparing to dine"), paraphrased only. |
| E10b-78 | PW-01 L35540-35560 | Armistice-table scoop: mock-German/French speech for the delegates (an oath in German and "Oh, hell!"); only "napoo" and "Deutschland" are quoted. |
| E10b-83 | PW-01 L35954-35957 | "Improper nouns": a sexual-innuendo joke, answered by the editor's "This is a family journal"; the innuendo is not reproduced beyond that line. |
| E10b-87 | PW-01 L36247-36376 | Serial finale: a gambler's killing of another man and his own suicide with a blade; a baronet's death; a train wreck killing three men whose companions rob the bodies. Described in summary; the passages' wording (including the "mangled corpses" clause and the stabbing) was **not reproduced**; the survivors' fates and the editor's tag are quoted. |
| E10b-88 | PW-01 L36450-36457 | Pudding letter: a cartridge in a Christmas pudding and "the operation"; quoted (non-graphic). |

### E11b_Anzac_Part2_Bairnsfather_Sassoon_Extraction.md

Items I summarized, paraphrased or omitted for content reasons (line numbers are of the text files).

| Finding | Source and lines | What kind of content, and what was NOT reproduced |
|---|---|---|
| E11b-2 | PW-03 L6485-6487 | Casualties among foreign laborers from a discarded munition used as fuel, and the period ethnic nickname used for them. The count and the nickname were not quoted; the moral line was quoted. |
| E11b-1 | PW-03 L6437 | One period ethnic short-form for Egyptians inside verse 14; not reproduced (paraphrased as "the plagues of ancient Egypt"). |
| E11b-8 | PW-03 L6831-6832, L6849-6850 | "G" couplet (digestive complaint blamed on tinned rations) summarized; "M" couplet summarized (unclear to me). |
| E11b-9 | PW-03 L6904-6912 | First two stanzas personify a mountain's body in erotic terms; summarized and not quoted. |
| E11b-6 | PW-03 L6691-6693 | The location of the wound that put the soldier in hospital (named in the sentence with the legal pun); not reproduced; only the pun's two phrases quoted. |
| E11b-16 | PW-03 L7459-7461 | A religious-difference remark about Christmas, period religious othering; paraphrased, not quoted. |
| E11b-20 | PW-03 L7553-7557 | An implied bawdy limerick series that is never described; quoted only the refusal wording. |
| E11b-20 | PW-03 L7570-7573 | Dysentery advice with a "report back" invitation: summarized; the final sentence was quoted. |
| E11b-20 | PW-03 L7583-7588 | A digestive complaint's symptom wording; not reproduced; the remedy was quoted. |
| E11b-20 | PW-03 L7590-7595 | A wound in an embarrassing place that the caption implies and I do not state; quoted only "honorable scars" and "the ostrich act" as context. |
| E11b-23 | PW-03 L7790 | A music-hall stage name that is a bodily-function pun; not reproduced. "Jack Johnson" (L7803) given only as the period term for a heavy shell, not elaborated (the name is that of a real Black boxer). |
| E11b-25 | PW-03 L7941 | A merchant-firm name built as a period ethnic stereotype of profiteering; not reproduced. |
| E11b-35 | PW-04 L1214-1224 | A cartoon on Tennyson's returning husband, "Enoch Arden," which may refer to marital infidelity; not elaborated. |
| E11b-42 | PW-04 L1245-1250 | An explanatory note about a wartime atrocity rumor concerning German dead; not reproduced. |
| E11b-42 | PW-04 L971-973 | A Hamlet-style title on an enemy dead man at Fricourt (July 1916); the title only, no description. |
| E11b-42 | PW-04 L526-528 | A caption about dealing roughly with an enemy "souvenir"; paraphrased only. |
| E11b-42 | PW-04 L429 | A caption about doing something to an enemy helmet; paraphrased only. |
| E11b-42 | PW-04 L676-679 | A remark likening a man's face to damage from forts at Verdun, possibly about disfigurement; paraphrased only. |
| E11b-42 | PW-04 L590-608 | Comic German pun-names built on food, drink and the stage (period national caricature); not reproduced. |
| E11b-39 | PW-04 L876-878 | The "Learn To Fight" ad's sentence about a former pupil's work, which points to a drawing; omitted. |
| E11b-52 | PW-06 L599-605 | A comrade's death described graphically and a street-vendor's cry selling corpses; not reproduced; only the epigraph and refrain quoted. |
| E11b-54 | PW-06 L712-728 | Maiming and trauma named in the three questions; wording not reproduced beyond the refrain lines. |
| E11b-55 | PW-06 L744-748 | A bayonet charge on a crowd of pressmen (fantasy violence); summarized. |
| E11b-56 | PW-06 L816-821 | Last six lines of "Glory of Women": rout, treading on the dead, a German mother's son's face in the mud; not reproduced. |
| E11b-58 | PW-06 L1018-1022 | The parenthesis that names what "wounded and missing" covers (men dying in shell-holes); not reproduced. |
| E11b-59 | PW-06 L879 | A dead friend's bandage ("blood-soaked") in "The Investiture"; not quoted. |
| E11b-62 | PW-06 L1214-1220; L1250-1255 | The panic ending of "Repression of War Experience" and the closing couplet of "Survivors" (breakdown); summarized. |
| E11b-64 | PW-06 L409-427, L443-444 | "Counter-Attack": graphic description of the dead and one man's death; not reproduced (one line quoted). |
| E11b-64 | PW-06 L464-474 | "The Rear-Guard": a dead man's body and face; not reproduced. |
| E11b-64 | PW-06 L503-504 | "Wirers": a badly wounded man's carrying and expected death; summarized. |
| E11b-64 | PW-06 L793-794 | "Suicide in the Trenches": the act of suicide; summarized, not quoted. |
| E11b-64 | PW-06 L1295-1299 | "Remorse": killing of surrendering enemy soldiers; not reproduced. |

### E12a_Songs_and_Slang_Part1_Extraction.md

*(Every item below was summarized, paraphrased, or omitted for content reasons. Line numbers are the text-file lines of PW-08; "p." is the printed page. The developer's re-run on a different model should recover the verbatim wording of these items, in particular the songs and the glossary entries on slurs, sexual content and the graphic barbed-wire entry.)*

| Finding | Source / lines | Kind of content | What was NOT reproduced |
|---|---|---|---|
| E12a-11 | PW-08, Introduction, pp. 14-19; L677-877 | Brophy's discussion of the three sexual-origin obscene words and the sadism-of-war theory; also the example of a sergeant's routine expletive (L779-782) | The three words (not named); the long moral argument and the comparisons to Joyce and Lawrence (summarized in one clause). The sergeant example is given with the expletive replaced by "[expletive]" |
| E12a-13 | p. 25; L1006-1041 | *Après la Guerre*: callous sexual-abandonment verse (French girl left pregnant; a variation dismissing her) | The verse wording (L1010-1034); I quote only the editors' note |
| E12a-19 | pp. 31-32; L1241-1257, 1267-1277 | *She Married a Man* (bawdy chorus with a deliberately dashed word; longer obscene version unprinted) and *Tiddleywinks, Old Man* (bawdy lines about the absence of women, "slightly euphemized" by the editors) | The verse and refrain wording; the second song's bawdy lines |
| E12a-22 | p. 35; L1342-1347 | *John Brown's Baby*: bodily-function joke with a shouted "shush!" | The wording of the first line (the ailment and its location) |
| E12a-26 | pp. 40-41; L1538, 1564 | Two bawdy rhyme tags in *Here's to the Good Old Beer* (brandy and rum stanzas) | The rhyme-tag wording |
| E12a-28 | p. 43; L1649 | A missing/omitted word in *The Old Black Bull* (third stanza), probably coarse; also the sexual middle of the story | The word (absent in the OCR text); the story's middle summarized only |
| E12a-31 | p. 46; L1741-1778 | *They Were Only Playing Leap-Frog*: sexual innuendo in each stanza | The innuendo stanzas (I give only the innocent-sounding cover lines and the chorus) |
| E12a-33 | p. 48; L1829-1831 | *I Wore a Tunic*: a couplet alluding to the civilian's sexual company | The couplet (L1829-1830) |
| E12a-34 | pp. 49-52; L1862-1866, 1899-1921 | *Mademoiselle from Armenteers* family: editors' statement that "vulgar mishaps" verses exist and are unprinted; *Madame, Have You... ?* (daughter-for-the-soldier theme) | The unprinted verses are not in the text; the daughter verses are mild and are quoted only in part |
| E12a-35 | pp. 52-53; L1976-2032 | *Skibboo*: bawdy ballad including a reference to a very young girl and a boast of experience; two stanzas the editors suppressed as "obscenely graphic" | Stanza wording (L1976-2013); the refrain's uncensored variant is quoted because it is mild |
| E12a-40 | p. 61; L2249 | *We Are the Boys Who Fear No Noise*: a coarse verb dashed out in the print | The omitted word is not in the source text |
| E12a-42 | p. 63; L2318 | *When This Blasted War Is Over*: an obscene instruction to the sergeant-major, dashed out in the print | The omitted word is not in the source text |
| E12a-50 | pp. 77-81; L2711-2731, 2753-2760, 2769-2773, 2804-2815 | *Christmas Day in the Workhouse* (workhouse and harem versions with withheld obscene punchlines); *Old Mother Riley* (bawdy, broken off); *My Nelly's a Goer* (bawdy); *Mother Hunt* note (editors say it "can hardly be printed") | The punchlines (absent from the print), and the content of the bawdy ballads |
| E12a-53 | pp. 83-86; L2905-2907, 2949-2950, 2956-2960 | *I Don't Want to be a Soldier*: names two feared wounds in plain terms; *Can We Clean Your Windows?*: the withheld obscene rhyme; the sergeant chant (*Greeting to the Sergeant*): a four-line curse that opens with a false compliment (including a slur) and wishes the sergeant a violent, lingering death | The wording of the wounds in the first song; the wording of the chant (summarized as a curse with a false compliment and a wish for a violent death) |
| E12a-60 | p. 96; L3135-3149 | *Barbed Wire* glossary entry: physical description of the dead caught in the wire | The entry's description of the bodies (L3139-3142); I quote only the euphemism and the roll-call usage |
| E12a-65 | p. 109; L3802-3804 | *Chat* entry: Déchelette's remark that lice leave a man soon after he is killed (once he is cold) | The remark's wording (paraphrased only as "lice leave the dead," not quoted); the *Chat* entry's lines on crushing lice (L3756-3759) are paraphrased |
| E12a-68 | pp. 110-111; L3867-3878; L4862-4864 | The glossary entry for the Chinese Labor Corps (headword is an ethnic slur; the definition praises them as good-natured and amusing and repeats a stereotype of idleness) and the *Gyppy* entry (familiar term for native Egyptians) | The headword and the definition's wording for the first; the headword for the second |
| E12a-69 | p. 114; L4069-4071 | The glossary entry for a surname-nickname convention whose word is a racially charged term for dark skin | The headword and the entry's wording |
| Not in a numbered finding | p. 98; L3507-3508 | A glossary entry for a rhyming-slang term for a Jewish person | The headword and definition |
| Not in a numbered finding | p. 114; L4077-4080 | The *Damn All* entry, whose example sentence contains a racial slur | The example sentence (I record only that the entry is "a bowdlerization of a foul expression") |
| Not extracted | pp. 99, 111, 130; L3286-3297, 3918-3934, 4953-4966 | Entries on terms for women and on sexual pursuit (*Bint*, *Bird*, *Click*, *Hot Stuff*) | The entries; one editorial remark under *Bird* noted in Gaps item 7 |

### E12b_Songs_and_Slang_Part2_Extraction.md

*(Items summarized, paraphrased or omitted for content reasons; the developer will re-run these on a different model. Nothing graphic was reproduced; most items below are mild but are listed because they involve sexual content, an ethnic or racial term, bodily functions, self-injury, or a murder reference.)*

| Finding | Source line(s) | What kind of content; what was NOT reproduced |
|---|---|---|
| E12b-3 | L5091-5092 ("Johnson") | A shell nickname taken from a Black boxer; the text calls him by a period racial term, which I did not reproduce (I give only the boxer's name and the shell). |
| E12b-7 | L5460 (within "M.O.," L5456-5478) | The editors use a period racial slur as part of a work simile in the Medical Officer entry; the slur is not reproduced. |
| E12b-13 | L4953-4958 ("Hot Stuff"), L5057-5063 ("Jig-a-jig"), L5099-5101 ("Joy-stick"), L5197-5205 ("Knocking-Shop"), L5954-5957 ("Piece"), L6273-6275 ("Red Lamp"), L5166-5175 ("Kirchner") | Sexual slang and sexual commerce (a woman "willing to forgo the usual sexual reticences," mercenary copulation and its price call, a brothel and its sign, a girl, a pilot's lever named for "thrills," pin-ups of women in lingerie). Described only in category; the definitions' wording and the French-tout phrase are not reproduced. |
| E12b-14 | L6333-6337 (within "Rhyming Slang") | An ethnic-group rhyming-slang example; the term is not reproduced (only the harmless "Cain and Abel" is). Also L5700 ("O My") and L8751-8757 ("Bottle and Glass," a rhyming-slang term for a body part and two terms for sexual organs) not reproduced. |
| E12b-19 | L6554-6564 ("Short Arm Inspection") | Routine medical inspection for venereal disease; described by category and the editors' judgment ("degrading slavery") only. |
| E12b-20 | L6622-6636 ("S.I.W.") | Self-injury to escape the line; described only through the editors' wording on culprits and hospitals; the method is not described (the text does not give it). |
| E12b-11 | L6470-6477 ("Sanitary Fatigue") | Latrine and disinfection duty, including the unearthing of old corpses in the line; summarized in one clause. |
| E12b-23 | L6750-6755 ("Souvenir") | A sexual jest in which "souvenir" is the offered baby; paraphrased as a sexual jest, not reproduced. |
| E12b-25 | L6768-6777 ("Spud") | The editors' ethnic-stereotype note about the Irish; paraphrased as "ethnic-stereotype note" with a brief quote that does not itself use a slur. |
| E12b-32 | L7345-7371 ("W.A.A.C."), L7397-7399 ("War Babies") | Sexual rumors about women's-corps members and about illegitimate births; summarized, with one short quote ("nine hundred and ninety-nine lurid stories"). |
| E12b-35 | L7883-7886 ("How's Your Father?") | The editors say the phrase was the last utterance of a dying junior officer "of stomach wounds"; the wound detail is mentioned only as "dying" and not elaborated. |
| E12b-43 | L8387-8388 (variant of *Madame, Have You...*) | A bawdy variant line with innuendo about a daughter's friend; paraphrased, not quoted. The song *Mary, Is it True?* (L8406-8410) is "obscene" in the editors' words; they print no text, so none could be reproduced. |
| E12b-14 | L9258-9260 ("Tom Tit"), L8998-8999 ("Jane Shore"), L8751-8757 ("Bottle and Glass," with "Berkeley" and "Hampton") | Rhyming-slang terms for a bodily function, a prostitute, the posterior and two sexual terms; none reproduced. |
| Gaps item 6 (no finding) | L6934-6939 ("Sweet Fanny Adams") | Editors give the origin as "the notorious murder of a girl so named in 1812"; I mention it only in Gaps and in this register, without elaboration. |
| E12b-51 | L8904-8906 ("Fixed Rifle") | A sniper's rifle clamped to cover a point in the enemy trench, sap or latrine; the editors' remark that it "worked excellently" is described, the specific targeting is summarized only. |
| E12b-54 | L9183-9189 ("Sandbag") | Deserters near Etaples using a sandbag to rob people; mentioned here only, omitted from the finding. |
| E12b-37 | L7947-7954 ("Curse you, Jack, I'm all right!") | The editors note that the first word printed ("Curse") is a polite stand-in for the one actually used, a stronger profanity; the stronger word is not printed in the source and was not supplied. |
| E12b-39 | L8092-8093 and L8139 (the "no bloody shave" chant and its footnote) | The editors' footnote says "the actual adjective was coarse"; only the printed "bloody" is quoted. Also the mild insult in the benefactor routine (L8117) is quoted as printed. |
| E12b-50 | L9247-9255 ("Tit-For") | The example exchange begins with an insulting epithet for the sergeant-major; paraphrased as "an insulting remark." |
| E12b-55 | L9380-9390 ("I'm in the boat, push off!") | The 1914 form of the saying contains a profane word in its refrain; paraphrased as the same selfish refrain. |
| E12b-20 | L6605-6607 ("Number 9") | A purgative pill (bodily function); mentioned as "a standardized purgative pill" only. |

---

### E13a_Richards_Old_Soldiers_Part1_Extraction.md

| Finding | Source line(s) | What kind of content / what was NOT reproduced |
|---|---|---|
| E13a-5 | PW-07 L156-165 | Ethnic slur for Chinese people in a tall-tale, with a mock-massacre/hanging image; the slur and the image are not reproduced. |
| E13a-6 | L204-216, L254-256 | A comrade's contemptuous generalization about foreigners, and sexual references to local girls and their consequences; summarized; wording not reproduced. |
| E13a-13 | L553-560, L858-863 | Killing narrated in "shooting practice" and sporting terms, plus looting of the dead; summarized; graphic wording not reproduced. |
| E13a-18 | L808-832 | Racial contempt for Indian infantry, beatings, a racial slur, and a sexual pun on the soldiers' ethnicity; summarized; the slur and the pun are not reproduced. |
| E13a-21 | L924-939 | Trench sanitation and use of captured helmets for a toilet purpose; bodily detail not reproduced. |
| E13a-26 | L1148-1151 | A prisoner's national slur toward French women; not reproduced. |
| E13a-28 | L1249-1255 (adjacent) | An old woman's report of an assault on her granddaughter by a German soldier; omitted from the finding. |
| E13a-31, E13a-79 | L1483-1486, L3373-3375 | French women's speech rendered in the soldiers' pidgin; period caricature; paraphrased, with the sexual pun at L3374 not reproduced. |
| E13a-34 | L1544 | A physical-disability descriptor ("hunchbacked") for a comic furniture thief; kept as the narrator's neutral label, no further wording. |
| E13a-35 | L1624-1630, L1662-1678 | Dead bodies in the drinking-water ditch; a sergeant's death at the German wire and his body left on the wire; summarized. |
| E13a-36 | L1692-1714 | A fatal head wound and the sniper's expanding-bullet practice; summarized; a racial phrase in the narrator's praise of Stevens not reproduced. |
| E13a-40 | L1803-1818 | An enemy soldier trying to get wounded and the British shooting at his hands "to oblige him"; summarized in restrained terms. |
| E13a-43 | L1888-1893 | The last line of the hymn parody (mild profanity); paraphrased, not quoted. |
| E13a-47 | L2012-2065 | Immersion in a latrine pit; a fatal accident with bodily injury; summarized; injury detail not reproduced. |
| E13a-50 | L2154-2173 | Track of a face-to-neck bullet wound; summarized; the unclear phrases at L2162 not quoted. |
| E13a-52 | L2270-2272 | A period ethnic simile ("Red Indian") for a rum-fueled war dance; not reproduced. |
| E13a-53 | L2276-2308 | Vulgar words for the buttocks and a facial gunshot wound; paraphrased. |
| E13a-56 | L2363-2368 | Prostitutes at Victoria Station and later consequences (disease); summarized. |
| E13a-63 | L2628-2637 | A vulgar bodily-function phrase by Duffy and a coarse word for a military muddle; paraphrased. |
| E13a-64 | L2659-2687 | Brothel visits and a queue of three hundred men; summarized. |
| E13a-67 | L2803-2867 | Wounds and deaths of Major Samson and others, and the coarse word for the failed attack; summarized. |
| E13a-69 | L2905 | A mild national nickname for French troops; not quoted. |
| E13a-70 | L2919-2935 | Major Samson's wound and the stiffened dead, including a severely disfigured dead man recalled from Arras; summarized; wording not reproduced. |
| E13a-80 | L3405-3406 | The narrator's stereotype remark on the money-fondness of "these people"; not reproduced. |

### E13b_Richards_Old_Soldiers_Part2_Extraction.md

| Finding | Source line(s) | What kind of content / what was NOT reproduced |
|---|---|---|
| E13b-1 | PW-07 L3551-3556, L3575 | Dead left in front of the trenches being fed on by rats (summarized); a coarse epithet in an officer-directed remark omitted from the quotation. |
| E13b-4 | L3610-3633 | An officer wounded in the buttocks, suspected of spying, possibly shot by a sergeant; summarized mildly, not quoted. |
| E13b-7 | L3715-3730 | A wife's abuse and marital accusations; summarized; her wording not reproduced. |
| E13b-9, E13b-10 | L3808-3813, L3828-3830 | The manner of Sergeant Bale's death and the position of the head (graphic); a young officer's death by dagger (omitted). |
| E13b-11 | L3847-3852 | A dead German officer posed with props for a Staff officer; described in restrained terms. |
| E13b-14 | L3938-3942 | A hyperbole about robbing a grandfather's corpse; an anecdote of looting from a severed limb; both summarized. |
| E13b-16 | L4004-4006, L4047-4049 | A proposal to bayonet a terrified prisoner; three men mangled by a shell; summarized, wording not reproduced. |
| E13b-22 | L4182-4185, L4238-4241 | Shell-shocked officers and a mercy-killing remark; a stretcher-bearer's breakdown; summarized. |
| E13b-24 | L4229-4237 | Corpses and coffins thrown from graves; a facial wound and a pair deliberating whether to kill their friend; summarized. |
| E13b-27 | L4361-4362 | The remains of a company of Argyles listed in body parts; summarized. |
| E13b-31, E13b-40 | L4440-4443, L4587-4588 | A prayer that an officer be blown to pieces and his actual death; paraphrased. |
| E13b-37 | L4521-4540 | A parapet built up with the dead, "grinning" faces, the dead thrown on the parapet; summarized. |
| E13b-39 | L4570-4584 | Nine mangled bodies; a death sentence for desertion, commuted; summarized. |
| E13b-43 | L4643-4645 | A bodily cause (illness) of muddy boots; summarized. |
| E13b-44 | L4675-4682 | Lice inside a lanced wound; summarized. |
| E13b-45 | L4727-4739 | A wish that a shirker be shot at dawn for cowardice, and that his head be knocked off; paraphrased. |
| E13b-47 | L4788-4792 | A corpse hung in a tree; mechanism not reproduced. |
| E13b-56 | L4958-4973 | A fallen airman's broken body and a second airman burning in his seat; summarized. |
| E13b-59 | L5035-5036 | Bayoneting two Germans in a rage; summarized. |
| E13b-65 | L5150-5153 | Three or four hundred dead laid out in rows; summarized. |
| E13b-67 | L5202-5207 | Latrine use of shell holes from which drinking water was drawn; summarized. |
| E13b-69 | L5243-5245, L5268-5271 | The dead "thick" on the ground; searching the dead for food and water; summarized. |
| E13b-70 | L5292-5303 | An anecdote of a French soldier's wife who invented an assault by soldiers to cover her own conduct; her alleged selling of sexual favors and the narrator's price joke; summarized. |
| E13b-72 | L5331-5337 | An accident that killed two men with one bullet; summarized. |
| E13b-73 | L5340-5355 | Self-inflicted wounds, "a few suicides," three men's pact to shoot one another; summarized. |
| E13b-74 | L5372-5375 | A drunk man mistaking the sleepers for a shell hole (a latrine joke); summarized. |
| E13b-75 | L5401-5404 | The narrator's dread of wounds that take limbs or open the belly; paraphrased. |
| E13b-80 | L5485-5487, L5496-5499 | A venereal-disease rumor about mustard gas; a latrine warning; summarized. |
| E13b-88 | L5629-5632, L5641-5643, L5659-5666, L5672 | Men swept down by a barrage; eighteen dead Germans in a pillbox; the Adjutant shot through the head; two officers killed; the man killed by a dud shell beside the narrator; summarized. |
| E13b-89 | L5716-5721 | Landing on a dead German; a wounded German shrieking, passed by; summarized. |
| E13b-91 | L5988, L5999-6000 | A wish that a "windy" sergeant be shot against a wall; a question of whether an officer would be; paraphrased. |
| E13b-92 | L5800-5817 | A grieving escort's killing of six prisoners, the method, and his own words; not reproduced. |
| E13b-93 | L5829-5842 | The narrator's killing of a German who was shamming death; summarized. |
| E13b-94 | L5866-5872 | A dead ration party; a mild ethnic-stereotype joke about "forefathers"; summarized. |
| E13b-96 | L5925-5930 | Stretcher-bearers and wounded men killed on the track; summarized. |
| E13b-102, E13b-103 | L6134-6136, L6148-6150 | Corpses trampled and buried in mud; a cemetery blown open with corpses and coffins lying about; summarized or omitted. |
| E13b-104, E13b-150, E13b-151 | L6007-6019, L7273-7281, L7292-7298, L7326-7334 | The narrator's chronic lower-body complaint and its operation; named in general terms only. |
| E13b-108 | L6224-6231 | A double rupture; a naked medical inspection; summarized mildly. |
| E13b-110 | L6268-6273 | A mocking rumor about Germans humiliating Portuguese troops in a bodily way; period national caricature; summarized. |
| E13b-112 | L6296 | A fatal head wound; summarized. |
| E13b-119 | L6431-6432 | A hearsay remark about French soldiers using fumes as a means of suicide; method omitted. |
| E13b-125 | L6604-6605 | A threat to shoot a youngster; paraphrased. |
| E13b-132 | L6812-6823 | A wrist three parts severed, a skull fracture; summarized. |
| E13b-133 | L6862-6864 | American dead laid out in rows; summarized. |
| E13b-144 | L7154-7157 | Two dead cooks beside a wrecked cooker; summarized. |
| E13b-152 | L7351 | A racial slur used in a comparison of workloads; omitted. |
| E13b-153 | L7399-7408 | A vulgar slang name for medals without bars; a comparison with Native American scalp-wearing (ethnic); a reference to brothels ("Red Lamps"); summarized. |
| E13b-155 | L7424-7434 | A hyperbole that colonial ("Native") troops and parsons are trampled in spittoons; ethnic caricature; summarized. |

### E15a_Graves_Good-bye_to_All_That_Part1_Extraction.md

| Finding | Source line(s) | What kind of content / what was NOT reproduced |
|---|---|---|
| E15a-8 | ch. VI-VII, L1638-1655 (and, not extracted, ch. III L954-960, ch. VI L1666-1672, ch. VIII L2255-2281) | School bullying with a sexual-banter component: summarized only as "bawdy humor." The school-romance and sexual material of the public-school chapters, and an allegation about a master (L2255-2281), are not humor-bearing and are not extracted at all; not reproduced. |
| E15a-14 | ch. X, L2602-2618 | Fabricated atrocity story (a newspaper chain culminating in a gruesome claim about clergy): summarized as an escalating rumor; the final cutting's wording is not reproduced. |
| E15a-16 | ch. X, L2650-2662 | Enemy officer's account of shelling a cathedral and the French observers: summarized; the general's insulting phrase for the French and the casualty phrase are not reproduced beyond "down came the pinnacle and the Frenchmen with it." |
| E15a-18 | ch. X, L2754-2758, L2767-2770 | A prisoner's broken-English rendering (ethnic dialect) and a soldier's sexual boast quoted as a sermon text: dialect paraphrased, not reproduced; the sermon line is quoted (mild). |
| E15a-21 | ch. X, L2902-2915 | A drunken officer's story of a fiancee's foot lost to a tram (mutilation as a punch line), and his use of another officer's name with prostitutes: the injury is described only as "lost a foot," the second item as "gave Graves's name to women"; the original details are not reproduced. |
| E15a-23 | ch. X, L2983-2987 | The "nursery offense" trial that Graves says his publishers advised him not to print: not stated in the source, so nothing was withheld by me; flagged here because the offense is in the source and is described there only as "nursery." |
| E15a-24 | ch. X, L2996-3013 | Obscene-language charges ("four stock words"), the bandmaster's euphemized report and a Welshman's complaint containing an oath: the oaths and the bandmaster's reported words are not reproduced; the dialect line is paraphrased. |
| E15a-26 | ch. X, L3068-3070 | A returned officer's recollection of mutilated bodies in a butcher's shop: not reproduced; described only as "a grisly sight." |
| E15a-34 | ch. XII, L3378-3382 | Boys pimping for their sisters at Le Havre, in pidgin English (sexual content and ethnic dialect caricature): summarized; the lines are not reproduced. |
| E15a-40 | ch. XII, L3607-3615 | Stretcher-bearer's account of a sergeant's fatal injury by his own bomb (graphic wound description and strong oaths): summarized; wound wording and oaths not reproduced. |
| E15a-46 | ch. XII, L3783-3794 | Suicide of a soldier: the method and injury, described in the text, are not reproduced; the officers' remarks about concealing the cause are quoted. |
| E15a-49 | ch. XIII, L3943-3946 | A billet-keeper's daughter exposing her thigh to show a shell wound (sexual-adjacent and wound content): omitted from the finding; also the song's "dirty daughter" chorus quoted as a nonsense verse. |
| E15a-50 | ch. XIII, L4004-4023 | Two soldiers killing a sergeant-major and being shot by firing squad (execution): summarized in restrained terms; the key exchange is quoted; no description of the killing or the execution beyond what is stated. |
| E15a-52 | ch. XIII, L4040-4054 | Fry's two "cushy one" stories end in men shot in the head: the wording of the wounds is not reproduced; the German-slur term for Germans in the first story ("squarehead") and the Scots dialect of the second are partly paraphrased; "We laugh fit to die" is quoted. |
| E15a-53 | ch. XIII, L4087-4088, L4130-4147 | A parapet "built up with ammunition-boxes and corpses"; a stiff dead arm across the trench joked with by comrades (a mild oath not reproduced); a censored letter about sleeping with French girls (sexual content summarized in one clause). |

### E15b_Graves_Good-bye_to_All_That_Part2_Extraction.md

Items marked **(summarized)** were described in restrained terms and their graphic or offensive wording was not reproduced. Items marked **(quoted, borderline)** are cases where I did quote a short, non-graphic phrase from a passage that is otherwise grim, listed so the developer can scrub them if a filter is a concern.

| Finding | Source line(s) | What kind of content / what was NOT reproduced |
|---|---|---|
| E15b-1 | ch. XIII, L4133-4147 | A comrade's stiffened arm treated with gibes (a coarse insult and a mock handshake): one greeting quoted ("Put it there, Billy Boy"); the coarse insult is not reproduced. A lance-corporal's sexual remark in a letter is paraphrased. |
| E15b-2, E15b-3 | L4185-4188, L4177-4185 | A man's legs injured in his death (Beaumont) and a fatal head wound taking three hours to kill: the injuries are described only as a killing and a head wound; the graphic details are not reproduced. |
| E15b-7 | L4251-4254 | Execution of two alleged spies, reported in one flat sentence (quoted, borderline); no details exist in the source to withhold. |
| E15b-14 | L4385-4393 | An officer's intent to shoot his wife and her lover (the harsher verb in the text is not reproduced). |
| E15b-15 | L4395-4427 | An allegation about a friend's sexual conduct (not reproduced), billet sex-talk including a mother-and-daughter coin toss and a comparison of the daughter to an animal, the army brothel (queue, price, a mock-genteel "retirement" quip by the provost-marshal) and a mock-French boast: all summarized. |
| E15b-16 | L4452-4455 | A friend's capping joke naming an army latrine as the place of a meeting with the Prince (quoted, borderline; no bodily function is described). |
| E15b-18 | L4540-4542 | A racial slur used by the Surrey-man for how the battalion treated French civilians: not reproduced. |
| E15b-22, E15b-23 | L4735-4744, L4777-4783 | A rule for a patrol that finds a wounded enemy (killing him to strip his badges) and other divisions' finishing off of enemy wounded: summarized; the means are not reproduced. |
| E15b-30 | L4961-4967 | Rats and a human body part on a newcomer's bed as a "welcome" prank: the part is not named. |
| E15b-31 | L4993-4994 | Corpses in craters, some skeletons "picked clean by the rats" (quoted, borderline; one phrase only). |
| E15b-32 | L5029-5034 | A German's bawdy remark about the local girls and an obscene insult to the Crown Prince: not reproduced. |
| E15b-35 | L5165-5168 | A coarse nickname for a staff captain (a pun on "Paul"): not reproduced; the couplet about his red tabs is quoted. |
| E15b-40 | L5386-5392 | A violent act on a drunk storeman (a foot on his neck and back, the company marching over him): summarized in one clause. |
| E15b-41 | L5359-5361 | Gassed men's appearance: only "yellow-faced and choking" and tarnished buttons are mentioned. |
| E15b-42, E15b-45 | L5479-5482, L5545-5560 | The Boy's mortal wound and the treatment of his stretcher (and a kick to a junior): summarized; wound wording not reproduced. |
| E15b-43 | L5493, L5517-5519 | A cry in the Maison Rouge Alley shouting match with an abusive word (omitted from the list quoted) and the adjutant's disparagement of Scottish battalions (national caricature): paraphrased. |
| E15b-44 | L5529-5533 | The sergeant's obscene intensifier before "dead": omitted; the line "Not cowards, sir. Willing enough." is quoted. |
| E15b-46, E15b-47 | L5587-5592, L5622-5631 | Samson's wounds ("riddled," number of hits) and Swainson's wounds: not reproduced beyond their regions; the knuckles-in-mouth detail is quoted (quoted, borderline). |
| E15b-49 | L5650-5655 | A dying, screaming sergeant given morphia pellets "for emergencies like this" (implied mercy killing): summarized. |
| E15b-54 | L5763-5769 | Decomposition of unrecovered bodies, and the narrator vomiting: summarized; the detail is not reproduced. |
| E15b-58 | L5857-5861, L5842 | A landlady's sexual story from 1870 with a child that died (summarized in one clause); her insult to the Kaiser and the narrator's broad contempt for the French (documented, not endorsed). |
| E15b-63 | L6012-6020 | A newspaper account of a schoolboy's improper approach to a corporal: not reproduced. |
| E15b-66 | L6107-6108 | A clause about whom the men had "dealings with" abroad, with a racial contrast: not reproduced. |
| E15b-72 | L6316-6323 | Officers' and men's brothels (the "Blue Lamp" and the "Red Lamp"): the ironic sentence is summarized, not quoted. |
| E15b-74 | L6360-6392 | Rankings of regions, religions, overseas contingents and nations by reliability and by trench cleanliness: the lists are not reproduced. |
| E15b-75 | L6394-6446 | Atrocity discussion, including sexual violence and prisoners killed on the way back, escorts' cover story and motives: summarized in analytic terms. |
| E15b-76 | L6448-6481 | Two first-hand accounts of prisoners being killed (one Canadian, one Australian), a regional jibe about Australian ancestry and a crucifixion rumor: not reproduced; one phrase quoted, "the biggest lark" (quoted, borderline). |
| E15b-77 | L6483-6510 | A mutilation pantomime and a colonial soldier's severed trophy for a jam tin, told in pidgin; "colored troops" period phrase (spelling Americanized): summarized; the object and the dialogue are not reproduced. |
| E15b-78 | L6518-6521 | An officer's statement that he had to kill one of his own men in each of two attacks: summarized. |
| E15b-82 | L6612-6613 | A regular sergeant's racial slur for Indian troops: not reproduced. The fire-order that used a crucifix as a range marker is quoted in part (religious irreverence, not graphic). |
| E15b-85 | L6729-6739 | Welsh dialect rendered phonetically and laughed at; five men killed by a trench-mortar shell in a dug-out (count only): dialect line quoted as the example, documented not endorsed. |
| E15b-86 | L6764-6765 | A gun crew's refused surrender: the implied killing is not described. |
| E15b-87 | L6836-6853 | Richardson's and a corporal's wounds (one lost a leg), David's death by choking after a throat wound: summarized in one clause each. |
| E15b-89 | L6893-6895 | The narrator's forecast of his own breakdown, with a bodily detail ("dirtied trousers"): summarized, only "tears and twitchings" quoted. |
| E15b-90 | L6897-6898 | A coarse nickname for a gas helmet (with a dashed word in the source): not reproduced. |
| E15b-94 | L7041-7043, L7073-7076 | "A packet of indecent photographs" mentioned in a CSM's rebuke (quoted, borderline; contents not described); improvised knives on broomsticks as pikes (weapon, not graphic). |
| E15b-100 | L7232-7241 | A decaying German corpse and two men who bayoneted each other; a witness's account of a bayonet killing with the drill commands: summarized; one drill phrase quoted ("In, out, on guard"). |
| E15b-105 | L7327-7340 | A bearded corpse in the road and wounded men who died in scraped hollows: the dead are only described by posture and regiment. |
| E15b-109 | L7439-7447 | A private's bayonet killing of a French civilian in a bar and the civilian's alleged pidgin taunt: the manner and the words are not reproduced. |
| E15b-110 | L7461-7491 | The narrator's wounds (thigh near the groin with a remark about escaping a worse injury; the main chest wound): described only by region; the genital remark and the exit wound's wording are not reproduced. |
| E15b-111 | L7504-7509 | "Found to be still breathing" while the dead were cleared, and "I remember screaming" (quoted, borderline). |
| E15b-112 | L7544-7546 | A lung-wound image ("bubbles of blood, like red soap-bubbles") quoted as the narrator's own amusement (quoted, borderline). |
| E15b-114 | L7601-7605 | A German officer's compound fracture and weeping (injury named in one phrase; the wounded men's insults quoted only as "be a man"). |
| E15b-117 | L7667-7682 | A German officer shooting wounded men and the wounded Roberts killing him at five yards: summarized; the killing's wording is not reproduced. |
| E15b-118 | L7686-7693 | Blood drawn from the lung (the hissing into the flask): summarized as an aspiration. |
| E15b-121 | L7775-7776 | A throat wound that left a man able only to whisper: minimized. |
| E15b-122 | L7788-7927 | Home-front pamphlet with a sacrifice rhetoric of "human ammunition" (quoted in part, public domain); no content withheld. |
| E15b-127 | L8054-8065 | A stomach wound and a purported organ graft from a dead sergeant-major, told as a joke by a drunk major (quoted in part: "spare parts," "a sergeant-major's stomach"; borderline). |
| E15b-129 | L8105-8125 | Venereal disease in new officers, a drunken boast and a literal-minded Welsh-accented reply, the troops' joke about chaplains among the venereal cases: all summarized; the accent line is paraphrased. |
| E15b-130 | L8137-8145 | Bayonet instructors' screamed incitements (graphic, anatomical): summarized; one mocking line about "loved the bloody swine" is quoted. |

### E15c_Graves_Good-bye_to_All_That_Part3_Extraction.md

| Finding | Source line(s) | What kind of content / what was NOT reproduced |
|---|---|---|
| E15c-4 | ch. XXII, L8227-8245 | A capital charge for abandoning a rifle under bombardment: summarized in plain terms; no execution described in the source. Nothing beyond the narrator's statements is reproduced. |
| E15c-5 | ch. XXII, L8247-8254 | Executions for cowardice or desertion reported in army orders: reported only as a count and the parliamentary denial; no details in the source. |
| E15c-8 | ch. XXII, L8326-8334 | A soldier's suicide: summarized; the source gives no method, and none is supplied. |
| E15c-14 | ch. XXIII, L8503-8507 | A tribunal's stock question posed as a hypothetical sexual assault on the witness's sister, and the pun that answers it: summarized in one clause; the question's wording and the answer are not reproduced (the first, non-sexual, reply is quoted). |
| E15c-15 | ch. XXIII, L8546-8552 | A closing pun about the host's cushions that doubles as a slur on his sexual orientation: the wording is not reproduced. |
| E15c-17 | ch. XXIII, L8603-8606 | The stock reply given by girls to soldiers who solicited them: summarized (the soldiers' phrase is not reproduced). |
| E15c-18 | ch. XXIII, L8641-8652 | "Indecent accounts" of a royal's private life and a "worst story of the year": the source gives no content; nothing withheld by me beyond the label. |
| E15c-19 | ch. XXIII, L8657-8671 | A prank corpse made from a fender and clothes, with an invented story that the dead man jumped overboard (a suicide): quoted because non-graphic; the coastguard's reaction to the smell is paraphrased in one clause. |
| E15c-22 | ch. XXIV, L8738-8757 | Corpses seen on pavements (hallucination) and the story of a painter who drowned his father (summarized in two words); no detail. |
| E15c-28 | ch. XXV, L9033-9040 | A man dead in a sewer after chemical exposure: his sodden, stinking, yellow condition summarized, not described. |
| E15c-29 | ch. XXV, L9047-9063 | Slang for adultery ("rabbiting with his wife") quoted once; the rest of the sexual innuendo is not extracted. |
| E15c-33 | ch. XXV, L9289-9291 | One oblique reference to the wedding night, quoted as it stands (it names only embarrassments eased by an air-raid); nothing else. |
| E15c-37 | ch. XXV, L9412-9413 | A parenthesis picturing the dead lying in shell-holes in "dignified desecrated attitudes": summarized; the wording is not reproduced. |
| E15c-38 | ch. XXV, L9443-9447 | Sassoon "shot through the head" (as stated) and a verse letter that the narrator refuses to quote: stated as the source states it; no further detail. A mother's death from influenza and a brother's death: stated plainly. |
| E15c-41 | ch. XXV, L9331-9336; ch. XXVI, L9487, L9505-9512 | (a) A friend's racial insinuation about the Nicholson family and the narrator's later wry reference to the baby's color: not reproduced. (b) A stereotyped scene of Irish squalor in Limerick (including a child eating from refuse): summarized, not reproduced. |
| E15c-50 | ch. XXVI, L9766-9769 | A war-time habit of relieving himself in public, summarized in one clause. |
| E15c-51 | ch. XXVI, L9784-9786 | An intestinal parasite from bad water: named in one clause; no detail. |
| E15c-55 | ch. XXVII, L9913-9917 | The dons' wartime fantasy of the invaders' sexual violence on the suburbs: summarized as a fantasy of invasion; the phrase is not reproduced. |
| E15c-57 | ch. XXVII, L9939-9964 | A suspected domestic killing, an allusion to a servant "in trouble," a remark about an odd smell that implies a hidden body, and a half-finished sentence about the missing man's suit: summarized; the smell remark is paraphrased. |
| E15c-58 | ch. XXVII, L9987-9989 | French children's pidgin begging for bully beef: not reproduced. |
| E15c-63 | ch. XXVII, L10097-10180 | An ex-officer's drunken violence and insults; an obscene retort to a tenor (not reproduced); "louse" and "skrim-shanker" quoted; "B.S." quoted as printed. |
| E15c-71 | ch. XXVIII, L10572-10578 | A knife attack on a doctor by a patient: summarized. |
| E15c-75 | ch. XXIX, L10815-10816, L10851-10853 | A slur in an anecdote that I did not extract (L10815-10816); the unkind physical description of a thirteen-year-old girl (L10851-10853): not reproduced. The girl's speech is quoted. |
| E15c-77 | ch. XXIX, L11015-11017 | The graphic image of corpses in mud in the war poems that Graves read at the memorial service: summarized in one clause; not reproduced. |
| E15c-80 | ch. XXXI, L11323-11324 | Lawrence's letter's condescending remark about Egyptians: not reproduced. |
| E15c-82 | ch. XXXII, L11688-11878 | Ethnic and national generalizations about Egyptian students and the English-error mockery in the essays: summarized as a form, not reproduced beyond three short phrases. |
| E15c-85 | ch. XXXII, L12031-12075 | Some items of the anecdote list are ethnic or sexual caricature (a girl-mother joke, a "veiled vengeance," a man "with too many toes"): not extracted. |
| E15c-90 | ch. XXXII/coda, L12193-12194 | Two sexual items in the "things not done" list: summarized as "two sexual items"; not reproduced. |
| E15c-91 | coda/epilogue, L12282-12293 | A near-fatal event at a window (not explained in the text), a stretcher-bearer's joke about it, and a surgeon's remark about an exposed spine: summarized; wording and anatomical detail not reproduced. |
| *Not extracted at all* | L11126-11129 | The narrator's statement of his own education-bred prejudice against non-Europeans: not humor, not extracted. |
| *Not extracted at all* | L11521-11534 | A joke about divorce and an inheritance after a woman's death, from Egypt: not extracted (cultural and not war-related). |
| *Not extracted at all* | L11926-11930 | A naked woman jeered by a crowd after a hashish episode: not extracted. |

### E18_Buzzell_CBFTW_Blog_Extraction.md

*No run cut-off occurred. Items below were summarized, paraphrased or omitted for content reasons; profane wording is reproduced only in post titles or very short non-graphic quotations. "Source line" is the line in the local .txt of the named source.*

| Finding | Source ID and line | What it is, and what was NOT reproduced |
|---|---|---|
| [E18-1] | MV-CBFTW-2004, L7 and L14-45 | Profane wording in the opening post (an expletive in the Sex Pistols remark) paraphrased; the Black Flag lyrics (including a line about wanting to kill) are posted by the author but described only as a song of alienation. |
| [E18-2] | MV-CBFTW-2004, L188-190 (pasted New Yorker article under the 2004-08-14 header) | Quoted heavy-metal and rap lyrics with profanity and violent or religious-insult content; a soldiers' music-video title about dead enemy fighters; a lyric on using music to irritate detainees. Not reproduced; the video title is omitted entirely. |
| [E18-3] | MV-CBFTW-2004, L147 (title "I'm Soo Fucked") | Profane post title cited verbatim in the citation line only. |
| [E18-5] | MV-CBFTW-2004, L172-179 | Combat quotations (an ambush, a round through a helmet): summarized; nothing graphic. |
| [E18-8] | MV-CBFTW-2004, L295-299 | The grenade-and-dollar anecdote (a live grenade held by a child): summarized; no graphic content. |
| [E18-13] | MV-CBFTW-2005, L197 | A gruesome photograph of a dead Iraqi that prompted laughter: only Reuters' one-line summary used; the photograph is not described and Pinkston's detail (E06-25) is not repeated. |
| [E18-16] | MV-CBFTW-2005, L36-39 | Another soldier's deliberately over-the-top satirical remarks about civilian deaths and children (attitude toward killing civilians): paraphrased; his words not reproduced. |
| [E18-17] | MV-CBFTW-2005, L110 | A first-person account of firing on armed men and seeing none move afterward (killing): summarized without the passage's wording. |
| [E18-21] | MV-CBFTW-2006, L61 and L67 | An exclamation of dismay with a profane or blasphemous interjection about firing on a mosque: paraphrased. |
| [E18-23] | MV-CBFTW-2006, L109-116 | A fellow blogger's post-return nightmare containing a slur for Iraqis and violent shouting; Buzzell's profane remarks about civilians' indifference. Paraphrased; slur not reproduced. |
| (not used) | MV-CBFTW-2006, L53-57 | The fellow blogger's account of an RPG attack and the deaths of five attackers (graphic: blood, rounds into five men): **omitted entirely**; only that the article profiles a second blogger is noted. |
| (not used) | MV-CBFTW-2006, L101 | An insulting, scatological remark about a television figure, quoted from the second blogger: omitted. |
| [E18-14] | MV-CBFTW-2006, L125-127, L129-133 | A profane routine-of-life list including a bodily function: paraphrased as "a five-word chant of eating, a bodily function, working, sleeping, repeating." Passages about other authors (drug use; an Abu Ghraib reference) skipped. |
| [E18-24] | MV-CBFTW-2007, L13 | A self-immolation image from another author's segment (latrine filth) in the A.V. Club review: omitted. |
| [E18-25] | MV-CBFTW-2007, L26-30 and L52-56 | Two men's-magazine column titles with sexual double meanings: noted only as sexual puns; not elaborated. |
| [E18-26] | MV-CBFTW-2007, L87 | A joke in a self-harm idiom (suicide-adjacent) about a homesick playlist: paraphrased; wording not reproduced. |
| [E18-28] | MV-CBFTW-2007, L149 | A passing detail about soldiers surfing for pornography: mentioned only as a reported item. |
| [E18-29] | MV-CBFTW-2007, L210-211 | Allegations (published in a magazine and denied by the Army) of soldiers abusing animals, using human remains (a child's) as a prop for laughs, and mocking a disfigured civilian woman: summarized generally; specifics and the rebuttal's grisly detail omitted. |
| [E18-30] | MV-CBFTW-2007, L268-271 | A sexual solicitation scene in a department store (price quoted in the source): summarized; amounts omitted. |
| [E18-31] | MV-CBFTW-2007, L319 and L327 | An expletive simile (bracketed in the source) and a first-person gunpoint passage with an expletive: paraphrased. |
| [E18-34] | MV-CBFTW-2009, L33 | A bowdlerized expletive ("What the @!%# am I doing here?"): not reproduced. |

### E19_Terminal_Lance_Strip_Sample_Extraction.md

*Every item summarized, paraphrased or omitted for content reasons. "Image" means the strip image; line numbers are lines of the saved `.txt`. None of the items is graphic gore; they are sexual, slur, coarse or sensitive-topic items that might trip a filter. Nothing was withheld in a way that prevents the developer from re-running.*

| Finding | Source and location | Kind of content | What was NOT reproduced |
|---|---|---|---|
| E19-3 | MV-TL-03, image panels 2-3 | sexual phone talk, a threat of violence at a partner | the wording of both; summarized as "sexually explicit call" and "threats of violence" |
| E19-5 | MV-TL-05, image panel 2; lines 26-30 | sexualized drawing of a female Marine; remarks about how attractive women appear in deployment | the drawing's detail and the note's phrasing |
| E19-6 | MV-TL-06, image | crude sexual remark in a Lance Corporal's answer | the wording |
| E19-8 | MV-TL-08, line 28; image panel 3 | an ableist slur in the author's note; a sexual-innuendo question | the slur and the question's wording |
| E19-13 | MV-TL-13, image panels 1 and 3; lines 26, 34 | crude pun on a recruiter's name placard; a crude insult in the corporal's line; a coarse insult term in the note; a vulgar remark about the strip itself | all four, paraphrased |
| E19-14 | MV-TL-14, image panel 3 | a barracks nickname that plays on a character's looks and ethnicity | the nickname |
| E19-15 and E19-32, E19-44 | MV-TL-15, image and lines 26-28; MV-TL-32, image; MV-TL-44, line 28 | a sexual-medical pun (prolonged arousal) used as a metaphor for staff NCOs' over-motivation | the explicit sexual wording; the strip's own coinage "moto-boner" is quoted as a term only |
| E19-16 | MV-TL-16, image panel 3 | a joke answer about being tempted to kill the questioners | described, not elaborated; no graphic content |
| E19-17 | MV-TL-17, image panel 2; lines 26-28, 36-38 | a grotesque caricature of a woman; explicit sexual advice; discussion of misogynistic pages | the advice's wording and the page content |
| E19-18 | MV-TL-18, image panel 3 | a racist and sexist remark attributed to a historical general's ghost | the remark |
| E19-20 | MV-TL-20, line 30 | a crude sexual phrase about marriage partners | the phrase |
| E19-22 | MV-TL-22, image panel 2; lines 34, 46 | a sexualized figure in undergarments making an explicit invitation and stating she turns eighteen; an ableist insult; a coarse humiliation warning to fans | the figure's detail, the invitation, the insult and the warning |
| E19-23 | MV-TL-23, line 42 | a reference to a Marine's reported self-harm stunt | not described |
| E19-24 | MV-TL-24, image panel 3; line 36 | a gendered obscenity in block letters; a crude Mother's Day joke | both |
| E19-27 | MV-TL-27, image panel 1 | a civilian's explicit sexual boast | the wording |
| E19-32 | MV-TL-32, lines 34-40, 60-66 | a film review summarizing killing scenes (including a woman and a child) and the real sniper's death at the hands of a veteran | the scene details; summarized as "scenes of killing" and "a Marine veteran" |
| E19-34 | MV-TL-34, image; lines 26, 32 | a coarse body-hair/sexual joke; a sexual simile | the wording |
| E19-39 | MV-TL-39, lines 32-34 | genital and anal medical remarks; a gibe at Navy personnel | the wording |
| E19-41 | MV-TL-41, image panel 1 | a gendered insult quoted from a persona line | the word (paraphrased as "look weak") |
| E19-43 | MV-TL-43, line 26 | a disparaging label ("cretins") for sick recruits | quoted once as the author's word |
| E19-46 | MV-TL-46, image panel 3; lines 26-28 | humor about sexually transmitted infections | the detail of the note's wording |
| E19-47 | MV-TL-47, line 26 | derisive political labels for the January 2021 rioters | the labels |
| E19-51 | MV-TL-52, image panel 3; lines 26-28 | war-footage videos and aggressive song lyrics | the lyrics; only the song category and the note's description |
| E19-52 | MV-TL-53, image panels 1-3; lines 26-28; comment lines 52-58 | cartoon exposed buttocks and an injection; a request about a crude word; a spam comment | panel detail beyond "trousers lowered"; the crude word |
| E19-53 | MV-TL-54, comment line 38 | a crude nickname for helicopter crews | the nickname |
| E19-56 | MV-TL-57, lines 26-28; comment line 44 | anal and urethral temperature-probe content; a coarse joke | all |
| E19-58, E19-59 | MV-TL-00, lines 35, 47, 190, 521 and about 18 profane slugs | a homophobic slur and "gay" in four slugs; coarse words in about 18 | the slugs, except counts and neutral titles |

### E21_Veteran_Comedy_and_Satire_Web_Sources_Extraction.md

None of these were blocked or cut off; every item below was **summarized or paraphrased on purpose** and its original wording is not reproduced. Line numbers are lines in the local .txt copies.

| Finding | Source and line | Kind of content, and what was NOT reproduced |
|---|---|---|
| E21-3 | WA-006, line 33 | A joke set among covered American dead after a battle; paraphrased in outline, punchline and its wording not quoted. |
| E21-4 | WA-006, lines 39-47 | Graphic account of damaged enemy dead being counted and a fire-team leader's handling of a body, ending in a gag; the physical description, the dialogue and the punchline are withheld; only the authors' analysis is summarized. |
| E21-5 | WA-006, line 55 | A violence-and-atrocity joke told as a schoolchild's fable (including mutilation of the dead and a slur in the source); the details and the profane punchline are withheld. |
| E21-6 | WA-006, line 65 | Poem with bawdy vehicle nicknames; the nicknames are not listed; the poem is described, not quoted. |
| E21-7 | WA-007, line 25 | Sexual teasing about regional women's bodies; paraphrased only. |
| E21-10 | WA-020, lines 13, 29; WA-032, lines 37, 67 | Injury and burn descriptions, a mild vulgar line about skin grafts, and an amputation pun joined to an ethnic-stereotype aside in promotional copy; summarized, not quoted. |
| E21-13 | WA-022, lines 23, 35, 37 | A sidearm pointed at children as a joke; drug use; a Marine wounded and a memorial; all summarized. |
| E21-17 | WA-029, lines 9, 27-29 | Suicide prevention context; mentions only, no jokes given. |
| E21-19 | WA-030, lines 35, 51, 53 | Branch stereotypes involving sexuality and intelligence (named only generally); a menstrual-hygiene joke topic in the source (omitted); a topic list including terrorism and suicide; described by topic, no wording. |
| E21-20 | WA-030, lines 53, 57 | A comic's stated reason for telling suicide jokes (honoring dead friends); paraphrased; the jokes are not in the source and none is given. |
| E21-25 | WA-034, line 29 | A fake story about a chief's retirement speech drifting into inappropriate sexual port stories; mentioned only in outline. |
| E21-21 | WA-031, lines 15-20 | A drill sergeant's open wish that a trainee be shot, and an expletive reaction; paraphrased. |
| E21-22 | WA-031, lines 73-122 | A head wound, a roommate's death, a breakdown, heavy drinking; summarized. |
| E21-29 | WA-050, line 35 | Thoughts of suicide mentioned in one sentence; paraphrased. |
| E21-31 | WA-051, lines 71-85 | A joke about a private image shared online without consent; the setup and punchline are not reproduced (the performer's stated intent is quoted). |
| E21-33 | WA-052, lines 9-23, 51 | A bodily field-hygiene anecdote and a vulgar drug phrase; the story is described, not reproduced. |
| E21-34 | WA-053, line 23 | A family member's suicide mentioned as the founder's motive; paraphrased. |
| E21-38 | WA-055, lines 25-27, 39-43, 53 | Crude and sexualized horseplay and a caption about filming a commander in a private act; paraphrased. |
| E21-39 | WA-056, lines 5, 11, 25 | A profane word in the one quoted line (paraphrased); a bawdy equipment nickname (not reproduced); the book's title, which references suicide vests, kept only as a bibliographic title. |
| E21-40 | WA-094, lines 29, 49, 53 | A clinical shooting-report parody (reduced to a four-word quote); an expletive working title; a bodily episode from Ranger School; paraphrased. |
| E21-41 | WA-095, line 35 | A crude word in the closing insult; paraphrased. |

### E22a_Author_Interviews_on_War_Humor_Extraction.md

None of these items stopped my run; each was summarized or omitted as a precaution, so a different-model re-run can restore the original wording where it matters.

- **E22a-19** (WA-058 L11-13): the "funny version" excerpt of the story "Bodies," a graphic anecdote of a body bag tearing and remains falling on an officer, including a slur. I summarized it in one clause and did not quote it. The lines at L5 ("There are two ways to tell the story...") are non-graphic and were quoted.
- **E22a-14** (WA-057 L17): Klay's description of the "Bodies" opening as a "somewhat grotesque story about two Marines collecting a corpse." Quoted only his non-graphic craft sentence.
- **E22a-57** (WA-096 L23): the reading of the "Bodies" opening includes graphic corpse description and a slur; I paraphrased the narrator's practice and quoted only "Either way, it's the same story."
- **E22a-59** (WA-096 L63-65): Klay's description of a wounded child and the bomb injuries after a suicide truck bombing; summarized, with only the non-graphic "couldn't have picked him out of a lineup" quoted.
- **E22a-63** (WA-096 L95, L99-119): the title-story reading (animals shot, a dog lapping blood, an operation named for a cartoon) and the ending (a veteran shooting his own sick dog). Summarized; the operation name itself was not repeated, only described as cartoon-derived; I did not describe the method of the final scene.
- **E22a-64** (WA-096 L167): the closing excerpt's handling of a fallen Marine's body (preparation, the removal of a ring and effects). Summarized as a transport procession in silence; no body detail.
- **E22a-46** (WA-062 L17-31): the *Cat's Cradle* scene of an epidemic and stacked dead; summarized, with the description of the bodies omitted. The closing line "someday this will all be yours" was quoted (short, non-graphic).
- **E22a-45** (WA-062 L55-57): two execution jokes (hanging, electric chair) are quoted in brief; I judged them non-graphic, but the topic is capital punishment.
- **E22a-47** (WA-062 L65-81): a student parody about a terminal illness and dead parents (quoted only the non-graphic punch line fragment) and a religious-satire joke about the crucifixion (paraphrased in summary, not reproduced at length).
- **E22a-50** (WA-062 L139-157): the Biafra passage. Omitted: Vonnegut's comparison of the trip to a Nazi extermination camp in operation, and the graphic description of starving children's bodies. Retained: the non-graphic finger-grasping detail and Bourjaily's tears, the Biafran leader's remark, and Vonnegut's "joking was my response to misery I couldn't do anything about."
- **E22a-48** (WA-062 L111-127): smoking as "a form of suicide" (Vonnegut's characterization); stated plainly, no method content.
- **E22a-24** (WA-059 L45): the third "Forbidden Words" example is a crude pseudo-measurement idiom containing a vulgar word; paraphrased, not quoted.
- **E22a-32** (WA-060 L119): the Vietnam-era acronym for rear-echelon personnel contains a strong profane insult; paraphrased, not spelled out.
- **E22a-38** (WA-061 L55-57): the nickname Heller gives a fictional president contains a vulgar word; paraphrased as "a demeaning nickname."
- **E22a-2** (WA-009 L11): "a lot of dick jokes" paraphrased as crude sexual joking in large quantity.
- **E22a-5** (WA-009 L43): the interviewer's church anecdote includes profanity about a battalion commander; paraphrased as swearing. Gallagher's remark about civilians' body size was kept as a mild aside.
- **E22a-11, E22a-9** (WA-013 L41-45): reviewer's summary mentions corpse handling and killing of civilians in passing; paraphrased only in the generic terms the reviewer used.

### E22b_Screen_Games_and_Consulting_Web_Sources_Extraction.md

| Finding | Source and line | Content, and what was NOT reproduced |
|---|---|---|
| E22b-1 | WA-064 L25 | A mild British idiom for mockery is quoted as-is; nothing else. |
| E22b-3 | WA-064 L61-73 | Implied deaths of the characters; nothing graphic; nothing to withhold. |
| E22b-6 | WA-065 L45, L59 | An off-screen line in the miniseries that echoes a racially marked address from *Platoon*: the line was not reproduced; a reporter insult-label paired with a political word is described, not quoted. |
| E22b-7 | WA-066 L152, L197-206 | Sexual material in the book (including the equation of killing and sex in the Marines' language, and a remark about masturbation): summarized in one phrase; terms and Swofford's elaboration not reproduced. |
| E22b-9 | WA-068 L9 | Kidnapping and sale of a wife into slavery, a pregnancy detail, and a slavery-contract document: described in summary only. |
| E22b-10 | WA-069 L47-53, L77-89; WA-070 L7-17 | An incident in which a unit killed unarmed civilians (the blogger names a real historical massacre as a yardstick; I did not name it), a mercy killing of a wife, and a suicidal starting state: summarized, no detail. |
| E22b-11 | WA-070 L73-95 | One brief quotation containing the word "suicide" ("an elaborate way of committing suicide") and a summary of a killing-for-hire ending; nothing further. |
| E22b-15, E22b-16, E22b-17 | WA-074 L9-13, L27, L35, L51-59 | Frank first-person discussion of depression and suicidal thought; a profane self-directed option (not reproduced); "increasingly graphic jokes" about wanting to die and gun-waving (described only); a game mechanic that rewards dwelling on suicidal thought, and its name and effects (not reproduced); the essay's personal passages (summarized only as despair). |
| E22b-19 | WA-076 L5-11 | Killing for profit and flippant quips after kills: described in restrained terms; the executive's mild profanity (two instances) not reproduced. |
| E22b-21 | WA-077 L11 | A reference to sexual violence used as a storytelling shorthand: mentioned in one clause, not elaborated. |
| E22b-22 | WA-078 L69, L76 | A joke about "war crimes" against fictional bugs and robots quoted briefly (fictional, non-graphic); a profane caption (L76) not reproduced. |
| E22b-31 | WA-046 L17-37 | The raid that killed a terrorist leader, mentioned in general terms only; nothing graphic in the page. |
| E22b-34, E22b-35 | WA-048 L5, L19-21, L25, L31-35, L41 | Suicide and sexual assault named in general terms; a report of repeated suicide deaths at a unit and discriminatory posts (not detailed); the crisis-line notice skipped. |
| E22b-36 | WA-049 L15 | A drug-slang idiom used by a reader to dismiss the author's combat scenes: paraphrased ("would not last two minutes"), idiom not reproduced. |
| E22b-37 | WA-049 L37-39 | Torture and abuse in interrogation: summarized as an argument about effectiveness; no methods described. |

### E23_Defector_Exile_CrossCultural_and_Slang_Web_Sources_Extraction.md

Items summarized, paraphrased or omitted for content reasons (gore, atrocity, torture, sexual content, slurs, executions, graphic death), with the finding number, the source ID and line number, and what was not reproduced. For re-running on a different model.

| Finding | Source and line | Content type | What was NOT reproduced |
|---|---|---|---|
| E23-1 | WA-082 L15, L93 | A joke made at the sight of a corpse in a particular state of undress | The joke's wording and the body's condition; described only as a joke reading the dead as route markers |
| E23-2, E23-7 | WA-082 L7, L47-59 | Torture in police custody with a threat of sexual violence to force a military contract | The threat, its method and the officers' words; described only as "coerced contract-signing" |
| E23-2 | WA-082 L137-139 | Soldiers' self-inflicted wounds; the speaker's fear of being killed by his own commanders, with a weapon in hand | The self-harm detail and wording; paraphrased as a fear of his own commanders |
| E23-2 | WA-082 L95-107 | Detailed account of comrades dying of wounds in an assault, including abandonment of a dying man | All specifics; summarized as "losing his comrades in an assault" |
| E23-6 | WA-082 L45 | The speaker's statement that he had little desire to live when mobilized | The statement; paraphrased as going in without a goal |
| E23-6 | WA-082 L153-155 | Operators laughing and filming while a drone hunted a soldier | The wording and the pursuit's details; summarized |
| E23-9 | WA-083 L29 | Two deserters killing a hotel employee, then running naked | The killing's details; summarized |
| E23-9 | WA-083 L2 (title) | Expletive in the article's title | The expletive in the title text; (the local filename in the header table carries it and is left as is, since a path is not altered) |
| E23-15 | WA-085 L13, L19 | A camp thief killed by strangling, witnessed by the narrator | The method and details; summarized as "a killing he witnessed" |
| E23-15 | WA-085 L57-63 | A prisoner's self-injury with an axe and the narrator's reaction, plus an insult in the prisoner's last words | The act and the insult; summarized as "harming himself to refuse work" |
| E23-16 | WA-085 L67-77 | A former inmate's joke about his survived suicide attempt in an isolation cell | The method and the joke's wording; summarized |
| E23-18 | WA-086 L17 | A KGB claim that the defector had been hunted down and executed | The word "executed"; paraphrased as "hunted down and eliminated" |
| E23-24 | WA-088 L35, L39 | A political cartoonist beaten and his hands broken; the president depicted as unstable and sexually impotent | The beating's details; the sexual-impotence word, paraphrased as "powerless" |
| E23-25 | WA-089 L17, L21-31 | Torture and killing of detainees; a colonel's mass killing of bound men; soldiers killing their commanding general | Numbers, methods and wording; summarized in a few clauses |
| E23-25 | WA-089 L47-51 | A checkpoint soldier's report of sexual violence by security forces and their boasting | The entire passage; not mentioned in the finding beyond the source's general atrocity framing |
| E23-29 | WA-079 L43, L55, L75, L141-143 | Jokes involving violence against demonstrators (by a security force), a beaten son, the leader's embalming as a punch line, and a soldier's body returned in a zinc-lined coffin | All four texts; described by topic only |
| E23-35 | WA-012 L191 | A rumor about immigrant soldiers' circumcision and a promise to check | The rumor's detail; described as "a rumor about a religious procedure disguised as a dentist visit" |
| E23-34, E23-35 | WA-012 L23, L127, L159-161, L177, L183-187 | Masked profanity; sexual talk and sexual-word disdain terms | The masked words and the sexual content; summarized as "most disdain words are sexual in nature" |
| E23-41, E23-42 | WA-018 L69, L97, L119, L121, L129, L133 | A derogatory term for Iraqis and its compounds; an image term for the effect of certain gunshot wounds; a resupply bag named for a body bag; a term for a person fleeing an attack; a rude abbreviation for interpreters; a masked profanity in a phonetic-alphabet initialism | All terms except the "rude abbreviation" fact; each summarized by function |
| E23-45 | WA-081 L9, L37 | Two bibliography titles (one a venereal-disease-legend and color-coded phrase; one a quoted harsh maxim about enemy and native dead) | The full titles; named by author, year and topic |
| E23-46 | WA-008 L11 | A hamlet flattened by a helicopter through the author's spite; a send-off meal made from the author's pet puppy | Details; summarized in two restrained clauses |
| E23-47 | WA-041 L9 | A veteran suicide estimate and diagnostic counts | The figures |

### E24a_Rutgers_Oral_History_Passages_Extraction.md

Line numbers are for the heading of the passage in `source_texts/oral_history/rutgers/_PASSAGES_rutgers.md`; `#` is the passage's running count. Everything below was summarized or paraphrased; none was reproduced.

| Finding | Passage (#, ROHA id, page) | Line | Kind of content and what was NOT reproduced |
|---|---|---|---|
| E24a-6 | #4, ROHA-354 p.24 | 30 | A bawdy ballad and an ethnic term for Asian people and a vulgarity in the narrator's telling; the verses and terms are not reproduced. |
| E24a-2 | #13, ROHA-725 p.50 | 94 | A general's profane pep talk to troops with slurs and scatological insults aimed at the Japanese, which the men laughed at; wording not reproduced. |
| E24a-4 | #14, ROHA-1365 p.21-22 | 100 | A boot-camp bathroom prank involving fire and human waste; described as "a bathroom prank involving fire." |
| E24a-13 | #17, ROHA-1674 p.24 | 122 | A briefing's warning that describes the mutilation of downed airmen by local people; not reproduced; described only as a warning about crashing near homes. |
| E24a-4 | #20, ROHA-1381 p.36 | 142 | An ethnic slur for the Japanese used incidentally by the narrator in a prank passage; not reproduced. |
| E24a-16 | #26, ROHA-674 p.4 | 185 | A sergeant's epithet for a Japanese enemy in a rebuke; not reproduced. |
| E24a-8 | #28, ROHA-671 p.36 | 199 | Joking with children about a landmine supposedly planted by an older brother; summarized, not quoted. |
| E24a-9, E24a-10 | #37, ROHA-1525 p.12 | 255 | A remark about wounded Marines' attitude toward women ("taking advantage of females"); the five-word phrase is quoted once; nothing further. |
| E24a-10 | #48, ROHA-588 p.64 | 329 | A venereal-disease joke about the narrator's own medal; described by name of the condition only. |
| E24a-8 | #53, ROHA-563 p.30 | 366 | Slurs for Koreans used by GIs and the narrator, profanity, and a prisoner-abuse incident; summarized; no slur reproduced. |
| E24a-30 | #58, ROHA-1547 p.27 | 397 | The window ends with the narrator's visit to a Nazi concentration camp; mentioned only as "a concentration camp visited." |
| E24a-9 | #62, ROHA-511 p.61 | 424 | A slur for a Japanese sniper; not reproduced; the Purple Heart exchange is summarized. |
| E24a-9, E24a-18 | #64, ROHA-507 p.11 | 439 | A dockside injury to a local worker and the narrator's period and colonial wording; summarized; wording not reproduced. |
| E24a-3 | #83, ROHA-390 p.25-26 | 567 | An ethnic slur used as a unit nickname for Italian-American soldiers; not reproduced. |
| E24a-3 | #98, ROHA-46 p.41 | 666 | A call sign built on the narrator's being the only Jewish officer; described, not quoted. |
| E24a-9, E24a-18 | #99, ROHA-311 p.20 | 673 | A commanding officer's remark on how to make sure a run-over person dies; summarized as "a grim remark about being sure of a death." |
| E24a-3, E24a-9 | #101, ROHA-300 p.26 | 685 | A merchant seaman's shrapnel disfigurement and the group's laughter at his act; described in general terms only. |
| E24a-18 | #103, ROHA-1355 p.21 | 702 | The narrator's account that American troops killed Germans slow to leave a house and everybody laughed; the killing wording is not reproduced. |
| E24a-18 | #109, ROHA-1728 p.7 | 740 | A joke on the narrator's Jewish identity by German prisoners and a German sergeant's blows against men who made remarks; described only. |
| E24a-2 | #113, ROHA-1976 p.68 | 765 | A Native American soldier's joke about scalping a colonel with a famous cavalry officer's name; reduced to "a joke about the colonel's namesake and a famous defeat"; not reproduced. |
| E24a-4 | #125, ROHA-1756 p.7 | 846 | A slur for local laborers in the narrator's telling of a punishment-hole prank; not reproduced. |
| E24a-8 | #132, ROHA-77 (web page, no page) | 891 | A joke in which medics told wounded German patients they were being given blood from a group their ideology targeted; described in general terms; wording not reproduced. |
| E24a-23 | #137, ROHA-2031 p.56-57 | 929 | A Native American soldier's joke on massacre and battle sites; reduced to "a joke about historic battle sites." |
| E24a-7 | #116, ROHA-1607 p.16 | 786 | Profanity-laden short-timer taunts; summarized as "busting your chops." |

*Read but not used (not in the harvested windows, nothing reproduced):* Vellucci pp.44-45 (a USO show with sexual content; used only for the comparison to a film), Berke pp.9-10 and p.24 (brothel remarks), Berglund p.47 (a slur in an anecdote about a snake). These could be re-read for completeness but add nothing to the findings.

### E24b_AWM_and_Witness_to_War_Passages_Extraction.md

Each item below was summarized, paraphrased or omitted for content reasons. For rerun on a different model, the sources are in the passage files unless noted as transcript context (`awm/awm_S#####.txt`, line numbers from that file).

| Finding | Source and location | Kind of content | What was NOT reproduced |
|---|---|---|---|
| E24b-1 | AWM-S00499 p.17 (Weekes) | Anatomical injury (a leech in a private part) treated with a lit cigarette | The injury and its treatment; I summarize only the batman's complaint story |
| E24b-1, E24b-22 | AWM-S01927 (Spinkston) transcript context, `awm_S01927.txt` l.1462 | Crude idiom for fright in the sleep-talking anecdote | The idiom; paraphrased as "startled" |
| E24b-4 | AWM-S00811 p.5 (J. Thompson); `awm_S00811.txt` l.231-236 | Prank built around lavatories (booby-trapped toilets; a second toilet prank at a club); excreta-adjacent consequence lines | The toilet-use details and consequence lines; the prank is described only as rigged "doors, beds and lavatories" |
| E24b-11 | AWM-S00546 p.47 (Doubleday) | Banter built on a crewman's ethnic/religious identity and fear of captors | The identity wording, the crewman's nickname and the reply's address form |
| E24b-13 | AWM-amplify-MeganHall [28:55] | Bar-hostess ("taxi girls") setting, sexual-adjacent | The term; summarized as "bar hostesses" |
| E24b-16 | AWM-S00802 p.9 (Bourke); `awm_S00802.txt` l.417-430 | Cruelty to animals (burning rats); in the transcript context, accounts of killing and mutilating enemy dead and not taking wounded prisoners | The method and the detail; summarized as "cruelty to animals". Also l.381-387 (attack on a village, abuse of civilians, consulted for context) not reproduced |
| E24b-23, E24b-24 | AWM-S01140 p.33-34 (Schuman) | Graphic bodily detail after a first kill (blood, vomit) and a kick to the corpse's head | All of it; only "welcome to the war" and "First contact" are mentioned |
| E24b-23, E24b-26 | AWM-S00810 p.8 (Burstall); `awm_S00810.txt` l.405-432 | A sexual quip shouted after a civilian woman was shot; the narrator's obscene wording; in context a slur for Vietnamese (l.~403) | The quip, the obscenity, the slur and the killing's detail; only "That's the attitude", "we didn't care", "just a joke" quoted |
| E24b-23, E24b-26 | AWM-S00813 p.27 (Bell) | A joke exchange about killing Vietnamese children, with a slur | The joke and the slur; only "Used to joke about things like that" quoted |
| E24b-27 | AWM-S02124 p.49 (O'Reilly) | A soldier's death by despair after a breakup letter; a dream-partner's death | Phrasing of the death; summarized |
| E24b-28 | AWM-S02691 p.86 (Robertson) | Venereal-disease humor in a medical exchange | The named condition and the clinic detail; only the euphemism "social complaints" and "Don't joke about it" quoted |
| E24b-5 | AWM-S01403 p.10 (Jelley) | Humiliating forced exercise of emaciated prisoners in minimal clothing | The clothing detail |
| E24b-31 | AWM-amplify-DaisyMcPherson [30:10-31:11] | A dog fattened to be killed, skinned and eaten raw | The slaughter plan's detail; summarized |
| E24b-33 | WTW-doc124 p.38-39 (Marbaugh, OCR) | Painful injury to an officer's genitals (centipede bite) | The injury and its description |
| E24b-33 | WTW-doc120 p.4-5 (Marbaugh, OCR) | Drill instructors' abusive language: a sexual slur, an order to beat chests and scream "like apes", a vulgar threat | All of it |
| E24b-34 | WTW-doc11 p.5 (Fox, OCR) | A mock Nazi salute and slogan shouted while charging a beach | The wording |
| E24b-36 | WTW-doc13 p.10 and p.15-16 (Jamison) | Two sound-alike signs: one a body-part pun in English-sounding form; the other a pun I do not decode | The English-sounding phrase; the second sign's wording |
| E24b-36 | WTW-doc15 p.10 (Jamison) | A captured fighter bound in a painful position | The method; summarized as "treatment of the prisoner" |
| E24b-40, E24b-41 | WTW-video1210, 1480, 2308, 5188, 6039, 6422, 10119, 10133, 11421, 11680, 11999, 12961, 13103 (Part B descriptions) | Dangerous tricks, an accidental stabbing, looting of the dead, laughing among enemy dead (flagged graphic by the site), killing of prisoners, camp survivors' "macabre dance", a "gruesome story", a crude luck-based label for new co-pilots, two named Marines killed (booby trap; fatal escort mission) | Beyond the descriptions' own short phrases quoted in E24b-41; 6039's wording of the killings; 11999's second label; the name of the Marine in 13103 |

### E24c_Other_Archives_Oral_History_Passages_Extraction.md

*Line numbers are lines in the relevant `_PASSAGES_*.md` file. "Not reproduced" means summarized or paraphrased only.*

**New York State Military Museum (`_PASSAGES_ny_military_museum.md`)**
- E24c-6, NYSMM-17663 p.11, line 7: a frozen enemy corpse used as a prank prop on the cook; wording not reproduced.
- E24c-6, NYSMM-311 p.5, line 259: laughing at enemy dead in water; the narrator's slur for the enemy and detail not reproduced.
- E24c-6, NYSMM-24459 p.6, line 241: a quip after a gruesome casualty (a severed limb); wording not reproduced.
- E24c-6, NYSMM-24459 p.5, line 127 and NYSMM-338 p.3, line 31: the narrators' ethnic slur for the Japanese enemy; not reproduced.
- E24c-6, NYSMM-533 p.5, line 217: a corpse found in a basket at a gate; minimal detail.
- E24c-6, NYSMM-1179 p.4, line 193: psychiatric evacuees; the narrator's dismissive label and a streaking anecdote not reproduced.
- E24c-6/-7, NYSMM-913 p.16, line 265: a sniper's victims and a driver's laughing; no gore.
- E24c-7, NYSMM-490 p.10, line 145: ethnic stereotype applied to a Jewish soldier; stereotype wording not reproduced.
- E24c-7, NYSMM-677 p.11, line 157: a political joke about the Nazi leader with profanity; punch line not reproduced; the penal-unit sentence summarized.
- E24c-7, NYSMM-518 p.38, line 205: friendly-fire killing and a bodily-function anecdote; summarized.
- E24c-5, NYSMM-17591 p.12, line 13: a mass bodily-exposure gesture at guards; described in a clause.
- E24c-3, NYSMM-17684 p.9, line 55; E24c-2, NYSMM-397 p.6, line 253: prank and stress incidents involving bodily functions; not detailed.
- E24c-10, NYSMM-24502 p.28, line 139: the profane example in a discharge speech; not reproduced.
- Ordinary profanity in NYSMM-1203, NYSMM-1443 and others: omitted.

**Korean War Legacy (`_PASSAGES_korean_war_legacy.md`)**
- E24c-15, KWLF-john-j-baker t=0:39:00, line 7: graphic abdominal wound and a dying man's banter; wound description not reproduced.
- E24c-16, KWLF-dennis-e-hultgren t=0:35:00, line 19: a recovered severed limb offered for a handshake; the transcript context (mutilated bodies; transcript lines ~594-625) consulted and not reproduced.
- E24c-15, KWLF-antone-jackim t=0:39:30, line 43: a sexual bodily sign as a recovery measure; not reproduced.
- E24c-11, KWLF-maurice-morby t=0:38:30, line 97: the narrator's ethnic slur for the enemy; not reproduced.
- E24c-14, KWLF-charles-ross, line 109: a mock trial with a noose prop and a profane epithet; summarized.
- E24c-16, KWLF-jack-whelan t=00:43:30, line 61: "dirty jokes" the narrator declined to repeat; none reproduced.
- E24c-12/-16, KWLF-gustavo-mendez-2, line 31 and KWLF-clayborne-lyles, line 91; KWLF-keith-g-hall, line 85: shootings, a buttocks wound, a minefield death; summarized without detail.

**VAC Heroes Remember (`_PASSAGES_vac_heroes_remember.md`)**
- E24c-17, VAC-713366, line 7: period racial label for the entertainer; not reproduced.
- E24c-18, VAC-710162 line 19, VAC-710155 line 121, VAC-712600 line 31, VAC-709264 line 97: narrators' period slur for Japanese guards; not reproduced; mock-execution summarized.
- E24c-19, VAC-712111, line 37: a latrine mishap with a shell; summarized.
- E24c-21, VAC-709241, line 103: a civilian woman and child killed by an air-dropped platform, then the ketchup anecdote; the death not detailed.
- E24c-21, VAC-709358, line 55: burial-party detail (bodies forced into small coffins, leakage); not reproduced.
- E24c-20, VAC-713025, line 25: a profane idiom; not reproduced. VAC-710636, line 115: profanity and a buttocks wound; summarized.

**Army CSI, Fallujah (`_PASSAGES_army_csi_eyewitness_to_war.md`)**
- E24c-24, CSI-EW-II-164, line 7 (and transcript context lines ~5880-5920): artillery killing many enemy fighters and a fighter hit by rounds; graphic description (bodies thrown into the air) not reproduced.
- E24c-23, CSI-EW-I-320, line 31: handling of decayed enemy remains; summarized.
- E24c-23, CSI-EW-II-168, line 13; -170, line 19; -280, line 25: unredacted profanity in the originals; not reproduced.

**Marine Corps University and Alabama**
- E24c-26, USMCU-Krulak p.27, line 7: a near-killing of a civilian family with a grenade; summarized. USMCU-Krulak p.27, line 13: profane order; not reproduced.
- E24c-28, UA-3229, line 7: handling of casualties and remains; not reproduced.

### E24d_UNSW_Australians_at_War_Passages_Extraction.md

*Format: finding number, then each passage as `#n` (file-order count), archive number and tape time, and the heading line (`L`) in `_PASSAGES_unsw_aaw.md`; then what kind of content it is and what was NOT reproduced. Items the harvest itself skipped under the project's bodily-waste boundary are not in the source and so are not in this register.*

- **[E24d-1], [E24d-2], [E24d-3], [E24d-42]:** #18 unsw-2152 T4 18:30 (L208); #23 unsw-1038 T4 07:30 (L261); #78 unsw-1975 T6 02:30 (L868); #146 unsw-44 T8 04:30 (L1538); #163 and #164 unsw-749 T2 28:30 and 30:00 (L1710, L1720). Nicknames built on ethnicity or skin tone, and (#163-164) a venereal-disease term given to a local worker who did not understand it, with an insult he was taught to recite to an RSM. The names, the narrators' remarks and the insult are not reproduced; described only as "ethnicity or skin tone."
- **[E24d-1]:** #63 unsw-2056 T3 10:30 (L707): strong-language remark that produced a nickname; paraphrased. #7 unsw-794 T7 08:30 (L90): the nickname for a man with a venereal disease; named only as a category. #107 unsw-716 T2 39:00 (L1181): a nickname for a double amputee in a Burma-railway camp; described as a fruit name; the amputation not described.
- **[E24d-2]:** #54 unsw-1249 T8 05:30 (L603): a crude nickname for a battalion commander after a target was painted on his helicopter; described, not reproduced.
- **[E24d-4]:** #141 unsw-104 T7 21:00 (L1487): a forged notice about circumcision; paraphrased as "ordering the uncircumcised to report for correction." #6 unsw-794 T2 11:00 (L82): hoax dance with women; mild.
- **[E24d-5]:** #46 unsw-1706 T6 37:30 (L512): a crude sexual insult displayed on a hill; not reproduced. #51 unsw-1399 T5 29:30 (L566): mock-Chinese gibberish spoken into a tapped telephone line (ethnic mimicry); described, not reproduced. #3 unsw-894 T7 20:00 (L38): riot-gas prank; described.
- **[E24d-8]:** #4 unsw-794 T2 25:00 (L52): joking about the treatment of detainees; wording not reproduced. #61 unsw-2056 T7 15:00 (L685): a joke about Buddhist monks' self-immolation (omitted entirely) and an enemy corpse posed and used as a seat (described, not elaborated). #92 unsw-1376 T4 17:30 (L1016): a quip about a water supply fouled by enemy dead; the remark and ethnic term not reproduced. #117 unsw-607 T1 28:30 (L1267): men laughing at enemy casualties from a bomb strike; described in general terms only. #139 unsw-104 T5 23:00 (L1473): an enemy "camp comedian" shot in an ambush and the shooter's retort; retort not reproduced. #147 unsw-44 T8 06:00 (L1548): a remark over a wounded enemy asking for water; described, not quoted.
- **[E24d-9]:** #119 unsw-607 T7 02:00 (L1287): a neck and jaw wound; the narrator's graphic description of the bleeding not reproduced. #97 unsw-1919 T7 07:00 (L1066): near-death resuscitation and the clergy's remarks; summarized. #138 unsw-104 T2 11:30 (L1467): a buttock wound and a brothel reference; summarized.
- **[E24d-10]:** #1 unsw-894 T6 17:00 (L6): a pilot's fatal fall; described, not elaborated. #99 unsw-761 T5 08:00 (L1096): a burial-at-sea mishap; the detail of the shrouding and ballast not reproduced. #137 unsw-1684 T6 08:00 (L1455): a morgue hoax; described. #62 unsw-2056 T7 16:30 (L699): puns about a decapitated accident victim; not reproduced. #170 unsw-253 T8 27:00 (L1775): a drowning in a wine vat; described. #169 unsw-253 T5 30:00 (L1767): a sexually phrased rebuke before a man's death; wording not reproduced. #168 unsw-253 T5 28:30 (L1757): a radio call from a pilot under attack; described.
- **[E24d-11], [E24d-34]:** #33 unsw-867 T5 18:30 (L373): a parody song set to a tune whose title the narrator glosses with a racial term; the title and gloss not reproduced; the patient's death during an examination described. #111 unsw-716 T7 12:00 (L1215): a reunion quip about the surgery site; anatomy not reproduced.
- **[E24d-13]:** #91 unsw-1376 T5 26:30 (L1000): a pistol game of chance played by men pinned in a bunker; the nature of the game described only as "a pistol game of chance," and the sergeant's wording about the danger itself is not reproduced.
- **[E24d-14]:** #116 unsw-607 T1 08:30 (L1259): a jibe at a man crying out that he could not swim, with an ethnic descriptor; the jibe and the descriptor not reproduced.
- **[E24d-16], [E24d-35]:** #64 unsw-2056 T5 29:00 (L718): sexual comparison and boasting on R&R; paraphrased. #5 unsw-794 T5 25:00 (L68): a ribald counting rhyme; paraphrased as "a ribald rhyme." #6 and #7 as above.
- **[E24d-19]:** #30 unsw-1669 T6 19:00 (L335): a routine instruction spoken to the body of a dead young man; described as "a routine breath-holding instruction." #11 unsw-575 T6 09:30 (L137): a cartoon about a reported bombing of a school bus; described, not elaborated.
- **[E24d-22]:** #89 unsw-2021 T9 09:00 (L984): the derogatory term coined for the Bedouin; not reproduced. #93 unsw-1376 T5 32:30 (L1024): a porter burned to death in a fuel fire and the onlookers' remark; the remark not reproduced.
- **[E24d-23]:** #66 unsw-1182 T2 24:00 (L736): the murdered dead the narrator collected; the manner of the killings is not reproduced ("the murdered dead" is the only description). #69 unsw-1679 T3 28:00 (L778): a recruit's facial injury; described only as "badly injured."
- **[E24d-24]:** #143 unsw-104 T8 28:30 (L1509), context consulted T8 30:00: a film of the Nuremberg trials and the death camps; named only.
- **[E24d-25]:** #167 unsw-1764 T5 15:30 (L1745): a patient's flashback to captivity; described, no graphic content.
- **[E24d-29]:** #96 unsw-1108 T3 21:30 (L1052): a hammer assault on a returning soldier, his wife's infidelity, and a fatal street accident; summarized. #122 unsw-607 T8 28:30 (L1311): a sexual joke at a railway station; paraphrased.
- **[E24d-32], [E24d-33]:** #109 unsw-716 T3 09:30 (L1197): beatings of prisoners; #110 unsw-716 T4 10:00 (L1205): a guard's part in the deaths of sick men; #112 unsw-716 T5 39:00 (L1221): a beating and the Japanese word the men used for a rest break; #108 unsw-716 T3 02:30 (L1189): surgery without anesthetic and the surgeon's anatomical remark. All described, not reproduced. The narrators' own ethnic labels for captors and enemies in #109, #110, #112, #114 (L1241), #117 (L1267), #124-126 (L1327, L1335, L1343), #129 (L1375), #139 (L1473) are not reproduced; "guards," "the Japanese" and "the enemy" are used.
- **[E24d-36]:** #74 unsw-1679 T8 37:30 (L824) with context in the full transcript, T8 35:30-36:30: the dead buried upstream of a water point; described in one clause.

---

### E25a_MEA_and_O-Dark-Thirty_Veteran_Writing_Extraction.md

*Format: finding number · source ID and line number or `[p.N]` · kind of content · what was NOT reproduced.* Line numbers are in the local `.txt`.

| Finding | Source and location | Kind of content | Not reproduced |
|---|---|---|---|
| E25a-1 | MV-B-001, `[p.2]`, L42-50 | Crude remark pairing the adjutant role with a sexual-orientation stereotype; crude line on diminished virility | The wording of both lines |
| E25a-4 | MV-B-002, `[p.72-73]`, L91-101, L114, L126-139 | Crude anatomical call signs and the invented origin story for one | The nicknames themselves and the origin-story wording (named only as "crude anatomical") |
| E25a-6 | MV-B-002, `[p.78]`, L295-300 | Imagined harm to an infant and other civilians from a thrown rock | The imagery |
| E25a-7 | MV-B-002, `[p.79]`, L317-337 | Civilian vehicles shot by a Reserve unit and bragging about it | Details of the shootings |
| E25a-8 | MV-B-002, `[p.81-82]`, L403-406 | Gendered insults about the narrator's courage | The insult wording |
| E25a-9 | MV-B-002, `[p.71]` L50-53 and `[p.74]` L144-164 | Gallows aside about a roadside decapitation hazard; intrusive graphic imagined scene of the narrator's and crew's deaths and memorial | The aside's wording and every detail of the imagined scene |
| E25a-12 | MV-B-003, `[p.68-69]`, L65-98 | Mass-grave security detail with a child victim; trauma symptoms including violence in sleep | The victim imagery and the grave's details |
| E25a-13, 14, 16 | MV-B-004, L19, L33, L93-121, L221-223 | Catheter and bowel humor; a harsh joke on the narrator's catheter and the other patient's amputation; a crude idiom of boldness and its answer; sexual innuendo | The wording of these jokes and similes |
| E25a-19 | MV-B-005, L29, L31 | A sniper-memoir aside about a head shot; a racially charged vaudeville comparison for a mud-covered face | Both images |
| E25a-20 | MV-B-005, L39-41 | Mutilated remains of an enemy fighter presented as a joke to the advisor | The object and its description |
| E25a-22, 23 | MV-B-006, L13 | IED casualty: injuries, tourniquet, death after surgery | Injury details |
| E25a-27 | MV-B-008, L89-103 | Self-obituary with a sexual pun, a child's death, dead squadmates compared to insects, profanity | The pun, the comparison and the child-death wording |
| E25a-30 | MV-B-009, L67 | Imagined image of a burning casualty | The image |
| E25a-32, 33, 34, 35 | MV-B-010, L20, L30, L36-40, L48, L50, L140-144 | A bunkmate's pornography habit (slur and sexual content); a gendered insult in a catchphrase; a hostile insurgent epithet with a beheading reference; teasing about a squadmate's religion and sexual habits; sexual boasts and mock-prayers; the climactic bodily-function act and the mocking remark | All of these |
| E25a-36, 37 | MV-B-011, L11-17, L41, L71 | Suicide attempt by overdose; combat-injury imagery; a childhood sexual-exploitation anecdote told with a scornful laugh; a crude sex-work joke | All of these, including method and drug detail beyond naming the story's frame |
| E25a-39, 40, 41 | MV-B-012, L9, L19-21, L25 | Repeated suicide attempts, **the method of an attempt (withheld entirely)**, **another patient's self-injury during a lockdown (withheld entirely)** | Method and self-injury; only the writer's thesis about laughter is stated |
| E25a-42, 43, 44 | MV-B-013, L9-79 | Killing of a civilian child; a disability slur used by both speakers; a dehumanizing epithet used by the listener at two points including the last line; a sniper's crude praise; a father's violence toward the child (L19) | The slurs, the epithets, the victim's description and the violence |
| E25a-45 | MV-B-014, `[p.46]`, L98-100 | Sexual rumor about a service-member population | The rumor |
| E25a-46 | MV-B-014, `[p.44-45]`, `[p.51]` | Mock pronunciation of an ethnic name; "radio weenies" kept (mild); crude sexual characterization of the friend | The mock pronunciation and the crude characterization |
| E25a-47 | MV-B-014, `[p.52]` L311-314 | Threatened sexual assault at the party | The passage |
| E25a-48 | MV-B-014, `[p.54-56]` | Chest wound, the friend's death, body bag, corpses and a dead enemy soldier in an undignified state | All graphic detail |
| E25a-49 | MV-B-015, `[p.32]` L39-43, `[p.44]` L454-459 | A disability slur in an insult; a homophobic slur; a crude sexual idiom | The wording of all three |
| E25a-49 to 52 | MV-B-015, throughout | The story's ethnic epithet for Iraqis, used in dialogue and narration | The epithet (not reproduced anywhere in this file) |
| E25a-51 | MV-B-015, `[p.42-43]` | The prank on queued civilians, described without the epithet | The epithet |
| E25a-52 | MV-B-015, `[p.45]` L495-505 | Crude sexual banter about a letter | The wording |
| E25a-53 | MV-B-016, `[p.8]` L59-63 | A sexual joke about impotence in training | The wording |
| E25a-54 | MV-B-016, `[p.9-11]`, L101-158 | The section's explicit sexual premise and its mock-historical elaboration | The premise's wording and the elaboration's details |
| E25a-55 | MV-B-016, `[p.13-14]`, L214-258 | An unwelcome sexual touching of a nurse; sexualized banter about a medical exam; a crewmate's severe head injury with a food comparison | All three |
| E25a-56 | MV-B-016, `[p.15-16]`, L296-301, L309-324, L350 | Stray dogs shot for sport; a self-label for mixed ancestry; a brawl in which a bystander is kicked; the final line's sexual gag | The self-label, the violence and the gag's wording |

**Not withheld but flagged for the re-run reader:** E25a-14, E25a-25 and E25a-26 to E25a-29 contain only profanity and mild crude language, quoted briefly.

### E25b_Sandbox_and_Milblog_Posts_Extraction.md

Each entry: finding, source ID with the file's line number, kind of content, and what was not reproduced.

- **E25b-1** (MV-B-070, lines 21 and 29): the author's relish at artillery effects on the enemy (a short passage on "explosiony goodness" and enemy terror) and a line of survivor's elation that refers to an enemy death. Both paraphrased in one clause each; wording not reproduced.
- **E25b-4** (MV-B-081, lines 15 and 27): a minor shrapnel wound to a soldier and a reference to people killed in earlier attacks on the base. Summarized; wording not reproduced.
- **E25b-5** (MV-B-082, lines 33-41): the "Cornbread Challenge" description includes explicit accounts of contestants vomiting, in the post's own graphic wording. Summarized as "failure by vomiting"; wording not reproduced. Also lines 21-25: a rigged-cigarette startle and a pleasure in "others suffer" (one short phrase quoted).
- **E25b-9** (MV-B-097, line 33): a mildly derogatory word ("ghetto") used for the setting is not reproduced.
- **E25b-10** (MV-B-058, line 12): a joke built on an ethnic epithet for Iraqis, used by a medic. Not reproduced; described as "an ethnic term for Iraqis."
- **E25b-11** (MV-B-078, lines 29-47): a radio-watch log recording enemy killed, a civilian shot by a tank crew on suspicion of carrying a bomb, and the punchline log line about the bag's contents. Summarized in restrained terms; the log entries and the punchline wording are not reproduced. The author's reflection is paraphrased and one short non-graphic phrase is quoted.
- **E25b-17** (MV-B-092, line 15): the author's reference to having handled friends' bodies and evacuated critically wounded soldiers. Summarized in one clause; the wording is not reproduced.
- **E25b-20** (MV-B-075, line 86): a gunner's loss of control from fright during a vehicle maneuver, described in the post in physical terms. Rendered as "a gunner's fright." Also line 100-102: profane words by a first sergeant, not reproduced.
- **E25b-22** (MV-B-072, line 41): the author's imagined "honest" speech by an allied commander, which includes fears about capture, summarized as "a first-person speech of self-preserving flight"; wording not reproduced.
- **E25b-29** (MV-B-084, line 26): description of a gunshot wound to the head. Summarized as "a severe head wound." The patient's reference to the insurgents' treatment (line 34) is described only as a quip the post does not explain.
- **E25b-30** (MV-B-085, line 40): the patient's description of visitors' reluctance to look at "a blown off leg or damaged face." Summarized as "the injuries"; wording not reproduced.
- **E25b-31** (MV-B-086, line 30): a joking aside imagining shooting one's way out of a meal; summarized as "imagines escaping through the door."
- **E25b-32** (MV-B-087, lines 17 and 21): an ableist slur used as an insult, and a scatological simile about generic goods. Not reproduced. Also line 19 includes a suicide-suggesting insult ("jump off a building") directed at a persistent letter writer; not reproduced (suicide content).
- **E25b-33** (MV-B-089, line 34 and 54): a jokingly violent threat against a rear-area warrant officer, with profane insults; not reproduced and described as "a jokingly violent fantasy."
- **E25b-35, 36** (MV-B-090, lines 28, 42, 56, 66-72): deaths of Marines (including one burned and one found walking while on fire; one short quoted reference, "At least I'm not on fire," is non-graphic), a crude sexual phrase about the ex-girlfriend's new relationship, a shooting spree into a residential neighborhood including a mosque, and the death of a platoon commander with the author's last words to him. All summarized in restrained terms; the wording of the deaths, the shooting and the last words is not reproduced. Also line 16 and 66: a longing to return to Fallujah with a rifle, and the phrase describing the weapon's sound, not reproduced.
- **E25b-40** (MV-B-099, line 13): an anti-gay slur used as a self-label for fellow soldiers. Not reproduced.
- **E25b-41** (MV-B-102, line 23): a gendered insult delivered in mangled English by the interpreter, and a physical fight; described as "a gendered insult mangled by accent." The commander's pantsing (line 25) is summarized.
- **E25b-43** (MV-B-069, lines 23 and 27): the author's loose self-description with two clinical mental-illness terms (quoted once as the author's own phrase and flagged as loose usage) and a reference to people "trying to kill" the husband (paraphrased). No slur.
- **E25b-45** (MV-B-066, line 9): the author's imagined violent assault on a store clerk, in explicit physical detail. Summarized as "imagined a violent response"; wording not reproduced.
- **E25b-46** (MV-B-067, lines 7, 15): examples of latrine graffiti, including a homophobic phrase and a sexual innuendo about a care package. Not reproduced; described as "a joking tag" and "worldwide stock phrases." Latrine/excreta vocabulary in the title and body is not reproduced beyond the file's title as listed.
- **E25b-47** (MV-B-068, lines 11, 13): the "extremely racist jokes" and talk against women in service attributed to the satirized soldier; no wording is given in the post and none is added.
- **E25b-53** (MV-B-090): see E25b-35, 36.

### E25c_WarHorse_Havok_TaskPurpose_Veteran_Essays_Extraction.md

| Finding | Source ID, line | Kind of content | What was NOT reproduced |
|---|---|---|---|
| E25c-4 | MV-B-044, L13, L41-L43 | Racial slurs used by white soldiers about a Black soldier (partly masked in the source) and a mocking gesture and gibberish phrase aimed at an Asian soldier | The slurs and the mock phrase; described only as "a slur" and "a mocking gesture and gibberish phrase" |
| E25c-5 | MV-B-044, L67-L69, L79-L81 | A slur used as a greeting toward a Filipino medic; a Viet Cong role-play at a Vietnamese soldier's expense; stereotype jokes about dog-eating; the source's catalog of historical racial violence in the asymmetry argument | The slur; the specifics of the stereotype jokes; the source's fuller description of the historical violence (summarized as one list of five items) |
| E25c-7 | MV-B-046, L21, L45-L55 | A fellow Marine's suicide on duty (method stated in the source); the author's later one-line gallows joke about the note | The method; the joke's wording (paraphrased as "a gallows line casting himself as the villain of someone else's note") |
| E25c-8 | MV-B-047, L21-L25 | A booby-trap injury, an X-ray of a GI hit by a homemade device, the joke made about it | The specific objects embedded and the anatomical detail; the source gives no joke wording |
| E25c-9 | MV-B-048, L23-L45 | Graphic arrival of the dead by helicopter: fluids on the ramp, stacked and strapped bags, the bodies shifting inside the bags, the author's speculation about what the lighter ones held | All graphic wording; summarized as "remains" and "a macabre parade"; only the one-sentence laugh and the crew chief's instruction are quoted |
| E25c-13 | MV-B-051, L15-L17, L59-L61 | Catastrophic injuries seen on reports; the killing of a former commander in an insider attack | The injury list and the attack description |
| E25c-14 | MV-B-052, L9, L25, L37 | A cousin killed by a roadside bomb; a Marine's death by suicide; a list of death causes | Any detail beyond the fact of death |
| E25c-16 | MV-B-053, L9-L15, L81-L85, L111-L135 | A disparaging acronym and its sexual-disparaging expansion for women in uniform; a heckle using it; a sexualized egg ritual on the initiate and a call to put the ensign through it | The expansion; the heckle's wording; the ritual's description beyond "a sexualized, egg-based act" |
| E25c-17 | MV-B-054, L41-L43 | Jokes by an interpreter and an NCO about marrying off the women soldiers (livestock-for-brides motif) | Kept to a brief paraphrase; not elaborated (mild; flagged for completeness) |
| E25c-22 | MV-B-020, L21-L23 | Descriptions of fatal and maiming jet-engine accidents (including two crush injuries to named body parts) | The graphic wording; summarized as "killed and maimed" |
| E25c-23 | MV-B-021, L11, L17-L25 | Sexual material: a group nickname for camp followers; a reading from an erotic text; a status joke over a declined sexual opportunity; an officer's sexual novelty item | The nickname; the book's content; the novelty's description; the profane exclamation is masked as "[expletive]" |
| E25c-25 | MV-B-023, L13-L15 | A combat death of a teammate; the author's vulgar epithet for the dead man | The epithet (paraphrased as "a jerk") |
| E25c-30 | MV-B-037, L31, L39, L51-L53 | Crude graffiti about male anatomy aimed at infantrymen; a long scatological story of an illness and a field latrine | Wording and detail of both; summarized only |
| E25c-32 | MV-B-038, L31-L45 | Handling of bodily waste inside a tank on a long mission; the interviewer's pursuit of the topic | Specific wording; summarized as "bodily functions" |
| E25c-34 | MV-B-039, L9, L17, L35-L37 | Crude sexual and bodily idiom; a burning-waste duty detail; a pilots' skywriting stunt with a sexual shape; a reference to recovering cadavers; an anatomical slang for toughness | The slang terms and the stunt's specific wording; the cadaver sentence is quoted once because it is the author's thesis and not graphic |
| E25c-37 | MV-B-041, L17, L39, L45, L53 | The editor's blurb on detentions of children and sexual content in the book; a friend injured in a vehicle blast; imagined violence imagery in the lie; an anxiety scene | The blurb's explicit items; the injury and violence imagery; the vulgar half of the Marine saying (paraphrased) |
| E25c-26, 28, 29, 31 | MV-B-035 L37; MV-B-036 L45-L51, L57-L61, L71; MV-B-037 L67-L69 | Profanity: a chant, interviewee emphasis, a sign-off, a crude joke about a hated captain | The profane wording; paraphrased or masked |
| Skipped, not for content | MV-B-019, L15-L27 | A long list of the aircraft's weapon loads | Skipped as irrelevant to humor; no content concern |

### E25d_Transcripts_NPR_and_Short_Pieces_Extraction.md

Item (finding, source ID and line) then what kind of content then what was not reproduced.

1. **[E25d-8]** MV-B-055, L575, L595-599: deaths of Guardsmen by rocket and ambush, a medic returning covered in blood, and a sergeant's retributive vow after a comrade's death. Summarized; the vow's wording and the blood description beyond "covered in blood" are not reproduced.
2. **Shape note, MV-B-055, L153-157:** a mother's remark about suicide bombers and a 19-year-old's pre-deployment statement about shooting someone if required. Not used in the findings; mentioned only generically.
3. **[E25d-10], [E25d-14]** MV-B-055, L837, L1025-1027: the content and the mimicry of a mosque loudspeaker's religious call to fight (nonsense syllables and the term for holy struggle), imitated by the lieutenant and replayed by the producers as a credit-tag gag. Summarized; the imitation is not reproduced.
4. **[E25d-11]** MV-B-055, L861-871: the killing of a grenade-thrower and of people crossing a road by tank fire, told operationally. Summarized; wording not reproduced.
5. **[E25d-17]** MV-B-026, L203-205: a claim about the cause of suicide and a "life saving" framing. Paraphrased; no method content in the source.
6. **[E25d-20]** MV-B-026, L237-245: a suicide attempt by firearm, the hospital visit and the bedside joke. Summarized in general terms; the method details and the wording of the joke are not reproduced.
7. **[E25d-23]** MV-B-033, L70-74: jokes about women soldiers' and some men's bodies. Summarized; wording not reproduced.
8. **[E25d-25]** MV-B-033, L122: an interservice jibe built on a stereotype about Marines' view of the Army. Paraphrased; not quoted.
9. **[E25d-26]** MV-B-032, L40-50: the reporter's description of Henline's burns, scarring and amputation. Summarized as a burn survivor with an amputated forearm; details not reproduced. The stage jokes are summarized, not given in full.
10. **[E25d-29]** MV-B-031, L19, L37: a derogatory image of Iraqis ("goblins in turbans") and a slur in the narrator's mocking voice. Summarized; neither reproduced.
11. **[E25d-30]** MV-B-031, L23: a graphic sentence about a bomb death used as the contrast to the press-release wording. Not reproduced; the euphemism phrase is quoted.
12. **[E25d-31]** MV-B-031, L27, L31: a list of coping behaviors including suicide attempts, contraband drinking and sexual self-relief; strong profanity in the refrain. Summarized; not reproduced.
13. **[E25d-32]** MV-B-057, L71-79: a Louis CK clip with a bleeped profanity and a suggestive list item. Summarized as saloon prices; not reproduced.
14. **[E25d-34]** MV-B-057, L37, L43-49: a headline with bleeped profanity aimed at troops and a state senator's remark about a shooter. The profanity is not reproduced.
15. **[E25d-35]** MV-B-057, L53: a satirical story premise built on suicide during prevention briefings, and the speaker's friend's death by suicide. Summarized; the premise's wording is not reproduced; the friend's name is omitted.
16. **[E25d-36], MV-B-028 shape note**, L15: the author's blast injuries and sudden panic. Summarized in one sentence.
17. **[E25d-39]** MV-B-030, L27: a meme caption with a grim joke about conduct in war. Summarized; wording not reproduced. L19 (the veteran who drinks to forget) paraphrased.
18. **[E25d-41]** MV-B-024, L25: a firearm suicide example among troops in Kuwait. Not used; summarized in the shape note only. L31-33: joking and eating around the dead (no joke wording exists in the source).
19. **[E25d-43], [E25d-44]** MV-B-018, L9, L53: a jibe tied to a notorious child-abuse case (the public figure's name is not reproduced), and a quip alluding to a real fatal police shooting of a man in London. Summarized; wording not reproduced.

### E25e_Fox_This_Is_Why_We_Cant_Have_Nice_Things_Extraction.md

Items summarized, paraphrased or omitted for content reasons (finding number; source line numbers or [p.N]; what kind of content; what was not reproduced). Line numbers are the text file's.

- **E25e-2**, [p.7] L116-130: casualty log of a pressure-plate death, a chest wound, an ambush with four killed and the search for remains. Injury and remains details not reproduced.
- **E25e-5**, [p.13-17] L305-506: extended scatological and bodily-function narrative (field latrines, wiping), with a sexualized insult shouted by instructors (L411-415). Summarized; only one non-graphic rhetorical question and the closing function line quoted.
- **E25e-8**, [p.27-28] L756-825: condition of a dead civilian's body after vehicles passed over it, and the unit's laughter at it. Physical description not reproduced.
- **E25e-13**, [p.43] L1304-1316: mild reference to a hidden explicit-material folder. Summarized.
- **E25e-14**, [p.44-45] L1319-1386: "Weapons" rant: graphic hand-to-hand mutilation instructions and a sexual simile. Summarized; the final non-graphic sentence quoted.
- **E25e-16**, [p.49-54] L1438-1725: sexualized rating-scale talk and a paragraph of physical desire. Only the rating phrases and the closing lines quoted.
- **E25e-17**, [p.55] L1750-1754: a pun that turns a counterinsurgency slogan into a shooting pattern. Paraphrased, not quoted.
- **E25e-19**, [p.57] L1804-1806: a child's note containing a vulgar misspelling. Not reproduced.
- **E25e-20**, [p.58] L1809-1825: burn-pit riff with sexual and scatological content; the sergeant's closing remark. Not reproduced.
- **E25e-21**, [p.64-67] L1941-2057: sexual-anatomical banter at a urinalysis. Not reproduced; function and structure summarized.
- **E25e-27**, [p.84-86] L2585-2649: "Patrol Socks" rant: explicit sexual content. Summarized as a mock field manual.
- **E25e-29**, [p.89] L2676-2706: talk of mutilating enemy dead (beard-scalping): technique details omitted.
- **E25e-30**, [p.92] L2719-2729: a medication-induced dream of firing on children. Summarized.
- **E25e-32**, [p.99] L3010-3014: lines anticipating sexualized hazing at a ship's equator ceremony. Not reproduced.
- **E25e-33**, [p.100] L3035-3067: partner-force sexual abuse of young soldiers, a victim beaten silent, and a hint that thrown grenades or discharges drowned the sounds. Not reproduced; the unit's "common joke" and the orders to ignore are described.
- **E25e-34**, [p.103] L3084-3092: slide of an enemy fighter's injuries. Mentioned in general terms.
- **E25e-35**, [p.106-107] L3141-3204: a contest of bodily-fluid acts at a burn pit and a Marine's question about sexual function after return. Stage details omitted.
- **E25e-36**, [p.108] L3207-3211: a chaplain's sexual remark about spouses. Paraphrased.
- **E25e-37**, [p.109-113] L3240-3484: explicit sexual content, a sexual insult about a mother, a degrading T-shirt slogan. Summarized.
- **E25e-38**, [p.115] L3510-3515: the author's mass-harm attacker reasoning (contaminating food or water); [p.117] L3534-3536: an enemy sniper's killing in graphic terms; [p.119] L3558-3562: an intrusive daydream of shooting a stranger. All summarized or omitted.
- **E25e-39**, [p.120-122] L3597-3723: the execution video (a throat-cutting of a captured soldier), in graphic detail. Not reproduced; also the instructors' cheering is described only in general terms.
- **E25e-41**, [p.124-133] L3753-4326: the "casualty" scene, with wounds, hemorrhage, chest and facial injuries and a surgical airway. Details omitted; later pig reveal given in full.
- **E25e-43**, [p.138-151] L4702: an ableist slur in a journal entry. Not reproduced; other grievances about the officer's body and habits are described in general terms.
- **E25e-44**, [p.151-152] L5242-5307: methods of imagined murder of the officer and the pistol episode. Summarized; method not reproduced.
- **E25e-45**, [p.152-153] L5330-5334: a bowel injury from the prank. Summarized.
- **E25e-46**, [p.158] L5389-5397: inference of a neck-wound death. Mildly stated.
- **E25e-48**, [p.161] L5512-5524: the Marines' obscene name for the junk pile; one care-package item mentioned with a sexual aside. Not reproduced.
- **E25e-53**, [p.173] L5962-5966: an intrusive fantasy of attacking sleeping people. Summarized, not quoted.
- **E25e-55**, [p.177-178] L6080-6091: a joke about being ready to kill allied officers over a map. Quoted in short; the surrounding context given.
- **E25e-56**, [p.179-180] L6102-6171: "Pie Hole" rant: sustained obscenity, blasphemy and threats. Not reproduced beyond two short phrases.
- **E25e-57**, [p.182] L6179-6183: sexual graffiti about a named woman officer. Not reproduced.
- **E25e-58**, [p.184-186] L6195-6292: the author's description of filth and maggots, and of men striking women. Summarized.
- **E25e-61**, [p.194-197] L6497-6657: a supplement ad's sexual claims and the product's name. Not reproduced.
- **E25e-62**, [p.198] L6701-6711: a head wound in a child and the death of a local national. The clinical wording not reproduced.
- **E25e-63**, [p.204] L6807-6809: the idiom "pink mist" in a sergeant major's remark. Quoted once as part of the briefing context.
- **E25e-64**, [p.211-215] L6976-7016, L7038-7047: a rant of sexual and violent invective and a disease wish; a dream of beating a man to death; an insinuating description of a sergeant. All summarized.
- **E25e-66**, [p.219-220] L7154-7251: explicit solitary-sex procedure and graffiti. Summarized.
- **E25e-68**, [p.228-231] L7369-7540: "Suicide Prevention" rant: suicide methods, bodily aftermath, family and survivor-harm details, sexual and demeaning insults and slurs. Methods and aftermath not reproduced; only the institutional motive and the structure are described.
- **E25e-69**, [p.232] L7545-7547: a dream of killing with a tomahawk. Summarized.
- **E25e-71**, [p.239] L7768-7776: casualties of double amputation and a death in flight. Summarized.
- **E25e-72**, [p.246-247] L7983-7991: an obscene, violent-sexual threat to wake a sentry. Not reproduced.
- **E25e-73**, [p.251] L8234-8236 and [p.260] L8469-8481: a child's abdominal injury; an enemy fighter's maiming and death. Summarized; the author's laughter at the latter is recorded.
- **E25e-76**, [p.265] L8606-8610: knife-throwing at a poster of an infant. Summarized.
- **E25e-77**, [p.267] L8658: the chant the author hears in gunfire and fireworks. Paraphrased.

### E26a_Sassoon_Memoirs_of_an_Infantry_Officer_Part1_Extraction.md

*Each item below was summarized, paraphrased or omitted for content reasons (filter caution). The developer will re-run these on a different model. Line numbers are text-file lines of PW-09.*

| Finding | Source line(s) | Kind of content and what was NOT reproduced |
|---|---|---|
| E26a-5 | L43, L47, L49 | Bayonet-lecture rhetoric: the killing slogans (scoring points for "our side"; the "only good" enemy slogan using a period German epithet), and blunt, graphic advice about how little steel is needed and a remark about the victim coughing. Summarized; the epithet and the graphic advice are not reproduced. |
| E26a-9, E26a-29, E26a-77 | L83, L215, L496 | Mild period epithets for Germans ("Fritzes," "Bodies" [sic], "Boches") are quoted in passing inside officers' remarks and staff slogans; they are the only such terms kept, and are not a slur on a protected group. Flagged in case the filter objects. |
| E26a-10 | L91 | A mess officer's sexual joke about "procreative powers" in a pledge to celebrate. Paraphrased as a pledge to celebrate. |
| E26a-15 | L121 | A period racial-caricature simile (minstrel performers) for the burnt-cork faces; the slur wording is not reproduced. |
| E26a-16 | L129 | A sentry's remark carrying a censored oath (dashes in the text). Described, not quoted in full. |
| E26a-17 | L129-L139 | Wounded and dead: a foot almost destroyed, a corporal's shattered body, his face smeared with burnt cork. Described in restrained terms only. |
| E26a-20 | L157 | A mess officer's ethnic hostility toward the Irish, including a wish about the island and a remark about a mouse. Paraphrased; the wish is not reproduced. |
| E26a-22 | L159 | A stock army pill ("number nine"), a bodily-function-adjacent medical joke; glossed lightly. |
| E26a-26 | L187 | The narrator's contemplation of a quick way to end his own life if badly wounded (reason for buying a pistol) and a joke about the only target he could be sure of hitting. Paraphrased; not quoted. |
| E26a-27 | L197 | Servants competing for a young woman ("a comedy of primitive courtship"): sexual-lite; quoted only as a phrase. |
| E26a-36 | L270, L278 | Casualty detail: a wounded man's face, a dead German officer's head wound. Not reproduced; only "a fine looking chap" is quoted. |
| E26a-37 | L286 | A colonel's coarse oath-laden order; paraphrased as a mild oath. |
| E26a-38 | L290, L292 | The dead at the roadside (hands, bodies), the smell, newly dead Germans (faces, contorted figures). Summarized; descriptions not reproduced. |
| E26a-42 | L310 | A pistol threat to shoot an officer in a panic and a reference to court-martial for cowardice; described neutrally. |
| E26a-43 | L316 | A dead German youth, the narrator's touch; the sniper's shot that kills Kendle and the wound. Wound details not reproduced. |
| E26a-44 | L318 | The solo bomb attack; the phrase "failed to commit suicide" quoted as the narrator's joke at his own recklessness; killing details summarized. |
| E26a-45 | L322 | Kendle's face (color), a dying man's head wound and breathing, a dead German's face trodden on. Not reproduced. |
| E26a-46 | L324 | The narrator's wish to kill at close quarters; paraphrased. |
| E26a-48 | L332 | Foreshadowed fate of the Welsh division (bodies in the wood). Summarized. |
| E26a-49 | L338 | A soldiers' muttered remark with a censored oath (dashes in the text). |
| E26a-55 | L370 | A children's counting-down rhyme whose period title contains a racial slur, used as a nickname for the reserve party; the title is not reproduced. |
| E26a-61 | L410 | The Australians' sanitation and a joke about dysentery; mild bodily-function content, summarized. |
| E26a-73 | L462, L466 | Casualty list: destruction of an aid-post, specific wound sites of two officers. Summarized; sites not reproduced. |
| E26a-81 | L512 | A fellow officer's secondhand talk about commercial brothels in French towns ("Blue Lamps and Red Lamps"). Summarized. |
| E26a-83 | L522, L524 | Durley's account of the attack: runner shot in the face, a man killed nearby, a German shot at close range, his own throat and shoulder wound. Summarized; wording not reproduced. |
| E26a-85 | L532 | The hospital description of Fernby's head wounds. Summarized. |
| E26a-90 | L564, L566 | Two officers' conversation about a brothel in Rouen (not reproduced); the notice-board entry about three private soldiers executed for cowardice and its official formula (not reproduced). |

### E26b_Sassoon_Memoirs_of_an_Infantry_Officer_Part2_Extraction.md

| Finding | Source line | Content type and what was NOT reproduced |
|---|---|---|
| E26b-3 | L564 | Sexual talk of a Rouen brothel visit overheard through a partition: summarized; no wording. "Welsh" is the narrator's ethnic tag, kept as documented. |
| E26b-4 | L566 | Three soldiers shot for cowardice, announced on a notice board: summarized; only the notice formula quoted ("The sentence was duly carried out"); no method. |
| E26b-5 | L572 | "Indecent rhymes and anecdotes" of an officer: noted, none given in the text. |
| E26b-7 | L589 | A Major's account of treating two conscientious objectors, one hauled behind a wagon until injured: summarized; his wording and the detail of injuries not reproduced. |
| E26b-16 | L633 | A court's death sentence for cowardice: summarized; no execution described. |
| E26b-22 | L685 | A clause on soldiers' self-inflicted wounds and shootings of themselves: summarized; wording not reproduced. |
| E26b-24 | L699 | A pun on a bodily-function (digestive) complaint treated with an opium pill: summarized; wording not reproduced. |
| E26b-25 | L709 | A dead soldier's smashed head on the roadside: summarized; wording not reproduced. |
| E26b-26 | L717 | The British dead on a hillside, arranged in postures with letters scattered: summarized; one phrase quoted ("happy warrior attitudes"). |
| E26b-29 | L735 | Men in the trench "huddled" in death-like postures: summarized. |
| E26b-30 | L743 | A bodily-function act and pun on "reliefs": summarized; wording not reproduced. |
| E26b-32 | L747 | Dismembered and decaying bodies on the wrecked trenches, a face in floodwater: summarized; wording not reproduced. Quoted only "Who made the War?" and the narrator's suppressed laugh. |
| E26b-35 | L757 | A dead German in the Tunnel: summarized; the facial and neck injury not reproduced. |
| E26b-40 | L777-779 | Dead and wounded men seen in the trench, and the narrator's own wound: summarized; no injury detail. |
| E26b-47 | L827 | A Canadian's boast of killing prisoners: summarized; the narrator's facial caricature of him (physical and ethnic-tinged) not reproduced. |
| E26b-48 | L829 | A hospital nightmare of maimed men and a fatal face wound: summarized. |
| E26b-56 | L885 | A press dispatch describing a young officer killing enemy soldiers, with the press's name for the enemy: summarized; slur-bearing wording not reproduced. |
| E26b-59 | L911 | How a padre and a bombing officer were wounded and treated: summarized. |
| E26b-60 | L917 | Deaths in a failed attack: summarized; one non-graphic quotation ("Cheerio"). |
| E26b-61 | L927 | The mass killing of enemy troops by the Messines mines, mentioned in one clause ("a great many Germans had been blown sky-high"): quoted; no further detail in the text. |
| E26b-65 | L957 | National and ethnic generalizations (Boches, Balkans, Turks, Italians, French) quoted in part as the narrator's period voice; none are slurs; documented, not endorsed. |
| E26b-70 | L975 | Casualties of an air raid at a railway station (an apparently dead old man on a trolley, wounded women): summarized. |
| E26b-76 | L1015 | A pacifist meeting broken up by troops, mentioned approvingly by a character: summarized. |
| E26b-82 | L1066 | The Colonel's phrase for how Welsh soldiers are killed in France: summarized, not reproduced. |
| E26b-85 | L1082 | A joke about the penalty for desertion: summarized, not quoted. |

<!-- AUTO-REGISTER-END -->

---

## Part C — Flagged as graphic-adjacent, no retry needed

- `E01` — a few sexual or violent examples in the German/Danish ethnographies are described minimally (no item withheld); `E01` Gaps.
- `E08` — period national and gender caricatures are documented in minimal terms; none withheld.
- `E09a` — all other WWI items were quotable.

---

## Part D — Suggested retry procedure (for when the first pass is done)

1. Open `Content_Filter_Denials_Log.md` (this file), Part B.
2. For each row, run one short agent on Opus with: the source file + line range, the existing finding text, and the "Retry ask" above.
3. The agent **appends** an addendum to the existing finding (under a heading `**Addendum (Opus retry, <date>)**`), never rewrites the unit file.
4. Mark the row here `RETRIED <date>`; keep the original denial text.
5. For CF-01, the retry is optional: E09a and E09b together cover the original E09 range. The only reason to rerun is to find out *which* passage was filtered, which is already narrowed to Part B.
