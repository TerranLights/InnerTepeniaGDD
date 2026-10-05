# Book Extraction Index

**Written 2026-08-29.** Every craft/reference book that has been **data-extracted** into this repo, where its
extraction actually lives, how deep it goes, and what uses it.

**Why this exists.** Twenty-three books have been extracted, but they sit in **three different places** and
most are per-book *sections inside two large consolidated files* rather than standalone documents. That is a
findability problem, not a coverage problem — while building the district Review Panel I twice reached for
material that was already extracted and concluded it was missing. **Check this index before mining anything.**

> **Distinguish two different files.** `Book_TOC_Master_Reference.md` catalogs **what books exist** in
> `Reference/Materials/books/` and what their tables of contents contain. **This file** records **which books
> have been read and distilled**, and where that distillation is. A book can be in the TOC catalog and not here.

> **Brought current 2026-10-04** *(developer request: "so that we know where to pick up").* The index had stopped
> at 2026-09-06 and was missing **two standalone extractions** (`Groundwater_Geophysics_Extraction.md` and
> `Environmental_Science_Demystified_Extraction.md`, both 2026-09-15) and **five topic-driven research folders**
> that each carry their own `00_Extraction_Checklist.md` (Davis geosciences, Ice-Cold Buddhism, Pisces Flood
> mechanism, PTSD/military trauma, Vostok genetics: **now Section 4b**). **Where to resume is Section 8.**
> Corpus on disk, counted 2026-10-04: **2,308** PDF/EPUB/DJVU files in `Reference/Materials/books/` (this file
> said 2,310 on 2026-08-29). **Roughly 55 to 60 books (about 2.5%) have been worked at some depth**: about 29
> with a full standalone or consolidated extraction, plus about 28 more at chapter or targeted depth inside the
> five research folders (counts approximate; some books appear in two places).

---

## 1. Where extractions live

| Location | Contains | Form |
|---|---|---|
| `Worldspace/Characters/Dolls/Character_Development_Methodology_-_DRAFT_Ideas.md` | **17 books**, 3,459 lines | Per-book `## From *Title* — Author` sections, plus cross-book reconciliation |
| `Worldspace/Characters/Dolls/Character_Development_Methodology_-_Villains_and_Antiheroes_-_DRAFT_Ideas.md` | **4 books**, 1,194 lines | Same convention |
| `Reference/Real-World/King_Warrior_Magician_Lover_Extraction.md` | **1 book** | Standalone |
| `Neo-Races-and-Cultures/_Method/Human_Universals_Extraction.md` | **1 book** | Standalone |
| `Reference/Real-World/*_Extraction.md` | **worldbuilding-track books, 2026-08-29 onward** | Standalone, one file per book |
| `Reference/Real-World/{Davis_Geosciences, Ice-Cold_Buddhism, Pisces_Flood_Mechanism, PTSD_Military_Trauma, Vostok_Genetics}_Research/` | **Topic-driven research folders (July to September 2026): several books each, chapter-level, with a `00_Extraction_Checklist.md` that is the source of truth for what is done** | Numbered writeups + a checklist; **see Section 4b** *(added to this index 2026-10-04)* |

> **A second track opened 2026-08-29: worldbuilding/culture extraction, distinct from the character-craft track
> above.** Of 2,310 eBooks in `Reference/Materials/books/`, 23 had been extracted before this date — all
> character-craft. The district-culture-synthesis program (13 zodiac districts) had been running entirely on
> live web research and the zodiac substrate with zero book support. This track targets that gap: philosophy,
> religion, history, economics, psychology, memetics, strategy, and related clusters, prioritized by relevance
> to active work (faction/religion design, district economies, survival culture, founding-era mass-movement
> psychology) rather than exhaustively. **Files land as standalone `*_Extraction.md`, one per book**, matching
> the King Warrior Magician Lover / Human Universals convention — not folded into the consolidated DRAFT files,
> which are character-craft-specific.

**On the two forms.** The consolidated DRAFTs are not a worse format — a large part of their value is the
**cross-book reconciliation** they carry (Weiland's Want/Need/Lie/Ghost reconciled against Truby's
Desire/Need, Boutros's Goal/Lesson, St. John's GMC; the "Composability Notes" sections that mark which systems
are orthogonal rather than competing). **That work would be lost by splitting them into per-book files, so they
are deliberately not being split.** This index supplies the findability instead.

---

## 2. Character craft — `Character_Development_Methodology_-_DRAFT_Ideas.md`

| Line | Book | Author | Depth |
|---|---|---|---|
| 107 | *The Anatomy of Story* | John Truby | Focused. Need vs. Desire, moral vs. psychological need, the Ghost, **four-corner opposition and the character web** |
| 193 | *Dynamic Characters* | Nancy Kress | — |
| 251 | *Characters, Emotion and Viewpoint* | Nancy Kress | **Partial** (chs. 3-4) |
| 299 | *The Art of Character* | David Corbett | **Partial** (chs. 6, 9, +) — functional-role catalog |
| 966 | *The Craft of Character* | Mark Boutros | — |
| 1102 | *Writing With Emotion, Tension, and Conflict* | Cheryl St. John | — |
| 1393 | *What Would Your Character Do?* | Eric Maisel | — |
| 1652 | *Writing Deep Scenes* | Alderson & Rosenfeld | — |
| 1729 | *Creating Character Arcs* | K.M. Weiland | Beat structure; the project's arc backbone |
| 1947 | *Creating Character Arcs Workbook* | K.M. Weiland | — |
| **2088** | ***Writing Archetypal Character Arcs*** | **K.M. Weiland** | **FULLY MINED — 585 lines, every chapter read individually.** The deepest extraction in the repo |
| 2674 | *Next Level Plot Structure* | K.M. Weiland | Chiastic/mirror structure; Four Story Worlds |
| 2764 | *The Last Fifty Pages* | James Scott Bell | — |
| 2896 | *Characters & Viewpoint* | Orson Scott Card | Three-tier character hierarchy; Sadist/Bully definition |
| 3091 | *Create A Character Clinic* | Holly Lisle | Superman vs. Gremlin fix; Sins catalog |
| 3191 | *Creating Characters: How to Build Story People* | Dwight V. Swain | — |
| 3312 | *Creating Unforgettable Characters* | Linda Seger | Four Elements of Relationship Sizzle |

### Weiland, *Writing Archetypal Character Arcs* — section map

The most-used extraction in the repo, and the base of the Review Panel's Panels A-C. Sub-sections, as offsets
from line 2088:

| Section | Contents |
|---|---|
| The Six Life Arcs | Maiden, Hero, Queen, King, Crone, Mage — **with ready-made Lie/Truth pairs per arc** |
| The Twelve Shadow Archetypes, individually | **Full psychological profiles**, not just labels |
| The Twelve Shadows as negative-arc content | Mapped onto the project's Disillusionment/Fall/Corruption taxonomy |
| The Six Flat/Resting Archetypes | Child, Lover, Parent, Ruler, Elder, Mentor |
| The Twelve Archetypal Antagonists | Six morally-orthogonal pairs |
| Practical Application | The closing chapter's "Five Considerations" workflow |

**The twelve shadows, for quick reference** *(each has a full profile at the line above)*:

| Life Arc | Passive shadow | Aggressive shadow |
|---|---|---|
| Maiden | **Damsel** | **Vixen** |
| Hero | **Coward** | **Bully** |
| Queen | **Snow Queen** | **Sorceress** |
| King | **Puppet** | **Tyrant** |
| Crone | **Hermit** | **Witch** |
| Mage | **Miser** | **Sorcerer** |

---

## 3. Villains and anti-heroes — `…_Villains_and_Antiheroes_-_DRAFT_Ideas.md`

| Line | Book | Author | Depth |
|---|---|---|---|
| 26 | *Bullies, Bastards And Bitches* | Jessica Morrell | The single most on-target source for morally complex characters; read in real but partial depth |
| 655 | *Fallen Heroes: Sixteen Master Villain Archetypes* | Tami D. Cowden | The sixteen villain archetypes — TYRANT, BASTARD, etc. **Note: Cowden's TYRANT is a different system from Weiland's and from Moore & Gillette's** |
| 845 | *The Anti-Hero in the American Novel* | David Simmons | — |
| 926 | *Heroes and Anti-Heroes in Medieval Romance* | ed. Neil Cartlidge | Turnus's Puppet-of-Ambition dynamic; the Liminality Payoff |

---

## 4. Standalone extractions

| File | Book | Depth |
|---|---|---|
| `Reference/Real-World/King_Warrior_Magician_Lover_Extraction.md` | Moore & Gillette, *King, Warrior, Magician, Lover* (1990) | **Effectively complete** — all 16 archetypes, the structural model, and the usable half of the Conclusion. Only ch. 1 unread. Source PDF is an image-only scan; read visually |
| `Neo-Races-and-Cultures/_Method/Human_Universals_Extraction.md` | Donald E. Brown, *Human Universals* | Feeds the Neo-Races/Cultures framework |
| `Reference/Real-World/The_True_Believer_Extraction.md` | Eric Hoffer, *The True Believer* (1951) | **Complete** — full text, all 4 Parts, 18 chapters, 125 numbered sections. First book of the 2026-08-29 worldbuilding-extraction pass. Endnote apparatus (~185pp of citations) not mined — bibliographic only |
| `Reference/Real-World/The_Meme_Machine_Extraction.md` | Susan Blackmore, *The Meme Machine* (1999) | **Complete** — full substantive arc, all 18 chapters through the book's own closing synthesis. Weighted deliberately: religion/transmission/internet/self chapters extracted in full depth, sex/mate-choice chapters (9-10) compressed as lower-yield for this project's purposes |
| `Reference/Real-World/Man_and_His_Symbols_Extraction.md` | Jung et al., *Man and His Symbols* (1964) | **⚠ PARTIAL, 2 of 5 sections — resume at p. 158.** Jung's own chapter (pp. 18-103) and Henderson's "Ancient Myths and Modern Man" (pp. 104-158) read in full and extracted. Von Franz's "The Process of Individuation" (flagged by the book's own intro as possibly the crux of the volume), Jaffé's visual-arts chapter, and Jacobi's case study **not yet read** |
| `Reference/Real-World/Buddhism_and_Intelligent_Technology_Extraction.md` | Peter D. Hershock, *Buddhism and Intelligent Technology: Toward a More Humane Future* (2021) | **Complete** — full text, Introduction + all 9 chapters, through the book's own closing section. Notes chapter also mined for substantive content beyond citation. Chapter 2 ("Artificial Intelligence: A Brief History") deliberately compressed — conventional AI/computing-history recap with minimal Buddhist content. Direct fuel for Ice-Cold Buddhism (karma-as-algorithm, "digital karma"/"karmic cloning" vocabulary, the six pāramitās) and robot consciousness (relational, non-brain-bound model of consciousness; explicit treatment of present-tense "minimally conscious" machines and future machine rights) |
| `Reference/Real-World/Groundwater_Geophysics_Extraction.md` | Reinhard Kirsch (ed.), *Groundwater Geophysics: A Tool for Hydrogeology* (Springer, 2006) | **Targeted, MODERATE-HIGH yield** *(500 pp.; extracted 2026-09-15 during Davis ULM Step 3)*. Hard-rock groundwater lives in joints and fissures while the rock body is nearly impermeable; coastal fresh water sits as a density lens on salt. ⛔ **Zero permafrost coverage.** Research, not canon. *(Added to this index 2026-10-04.)* |
| `Reference/Real-World/Environmental_Science_Demystified_Extraction.md` | Linda D. Williams, *Environmental Science Demystified* (McGraw-Hill, 2005) | **HIGH yield, from the title its own checklist rated lowest** *(431 pp.; 2026-09-15, Davis Step 3)*. The only one of the five geoscience volumes that covers frozen ground (permafrost, frost, periglacial; the Trans-Alaska refrigeration case; frost wedging in rock joints). **The file's headline is that the checklist's title-based rating was wrong.** Research, not canon. *(Added 2026-10-04.)* |

---

## 4b. Topic-driven research folders *(added to this index 2026-10-04)*

**A different shape from Section 4:** each folder pulls from **several books at chapter level** toward one
named design question, and keeps a `00_Extraction_Checklist.md` that is **the source of truth for what is done
and what is open**. All of it is research, **not canon**, until worked into a city's files by explicit decision.

| Folder (`Reference/Real-World/…`) | Serves | Books worked | Status |
|---|---|---|---|
| `Davis_Geosciences_Research/` *(`01_Groundwater_and_Lake_Chemistry.md` + checklist)* | Davis: hard-rock water, hypersaline lakes, frozen ground | Merkel & Planer-Friedrich *Groundwater Geochemistry* (modest) · Pinder & Celia *Subsurface Hydrology* (moderate) · Kirsch *Groundwater Geophysics* (mod-high; own file above) · Misra *Introduction to Geochemistry* (LOW: zero limnology, so the topics file's claim was wrong) · *World Geologic Atlas, Sheet 17 (Antarctica)* (an image plate; read directly) · Williams *Environmental Science Demystified* (HIGH; own file above) · Foken & Mauder *Micrometeorology* (low) | ✅ **All checklist items done 2026-09-15.** Not extracted on purpose: Albarede & Ottonello; Atlas Sheet 18; titles flagged **likely Mirny** (*Magmatic Sulfide Deposits*, *Metals and Society*, *Mineral resources from exploration to sustainability assessment*, *Risk management in evaluating mineral deposits*, *Exploration Geophysics*, *Hydrothermal Processes and Mineral Systems*); general-purpose field texts. ⏸️ Open thread: whether modern mapping revises the Prydz Bay `γPz` (Paleozoic granite) assignment |
| `Ice-Cold_Buddhism_Research/` *(files 01, 03, 04, 07, 08, 09 + checklist)* | The robot religion "Ice-Cold Buddhism" (Dome Fuji, Kunlun) | *The Buddhist Analysis of Matter* (Ch. 10) · *Buddhist and Taoist Systems Thinking* (Ch. 2-3) · Hershock *Buddhism and Intelligent Technology* (Ch. 1, 7; **the fuller whole-book extraction is the standalone file in Section 4**) · Byung-Chul Han *The Philosophy of Zen Buddhism* (Ch. 1) | 🟡 **Partial, 5 open rows.** Files `02`, `05`, `06` not written. **Open:** *The Buddhist Theory of Self Cognition* (EPUB), *Buddhism and Linguistics*, *Rethinking Meditation* (EPUB), the synthesis row, and the later chapters of the books above. ⚠ **The checklist calls the EPUBs "CONFIRMED UNREADABLE": that is stale.** EPUB has been readable via `unzip` since 2026-07-23 (`Book_TOC_Master_Reference.md`), so that blocker no longer applies |
| `Pisces_Flood_Mechanism_Research/` *(files 01 to 07 + checklist)* | The Flood (Pisces district): a plausible, constraint-checked mechanism | From `Math_and_Computation/`, `Linux/`, `Cpp/`: Thurner et al. *Introduction to the Theory of Complex Systems* · Gao et al. *Introduction to Network of Networks* · *Distributed Control of Robotic Networks* · *Pattern Theory* · *Superminds* · Ghosh *Distributed Systems* · *The Linux Memory Manager* · *System Programming in Linux* · *Asynchronous Programming with C++* · *Hands-On Network Programming with C* (about 10 titles) | 🟡 **Partial: 23 rows done, 17 open** (e.g. *Network of Networks* Ch. 5 §5.3 onward and Ch. 6; several *Math_and_Computation* titles at TOC or skim level only). ⚠ **This means `Math_and_Computation/` is NOT unmined**, whatever the "deferred" note in Section 6 implies |
| `PTSD_Military_Trauma_Research/` *(files 01 to 10 + checklist)* | The unnamed Cancer-district ex-military defector (and, secondarily, Outer Tepenia) | **Source folder is `to-be-integrated/books/PTSD/` (10 books), not `Reference/Materials/books/`:** Rhodes *Military Ethics* · McDermott *Understanding Combat Related PTSD* · Paulson & Krippner *Haunted by Combat* · Driscoll *Hidden Battles on Unseen Fronts* · Vasterling & Brewin *Neuropsychology of PTSD* · RAND *Invisible Wounds of War* · Moore & Penk *Treating PTSD in Military Personnel* · Freeman, Moore et al. *Living and Surviving in Harms Way* · Adler et al. *Military Life* (TOC-triaged) · plus a synthesis (`10`) | ✅ **Complete for this pass.** Gaps: `07` is missing about 30% of the 2nd edition; the 1st-edition spot-check was never started; the **dark-humor source search** (gallows-humor material; none of the 10 books covers it) is a separate task, not started |
| `Vostok_Genetics_Research/` *(files 01, 02 + checklist)* | The genetics hub **Vostok (now renamed Ariun Nuur, `DR-43`; the folder name was not changed)** | `Reference/Materials/books/STEM/Biology/bioinformatics/`: Brazma et al. *Living Computers, Replicators, Information Processing* (several chapters) | 🟡 **Partial: 3 rows done, 5 open** (e.g. Ch. VII "Evolution as a Ratchet of Information"; Ch. III; *Biocalculus* not yet opened) |

---

## 5. ⚠ Cross-system terminology collisions

**Four archetype systems are now in active use and they share names while meaning different things.** Always
name the system.

| Term | Weiland | Moore & Gillette | Cowden |
|---|---|---|---|
| **King** | a **Life Arc** — sacrificing power for the realm | a **faculty** — order, blessing, generativity | — |
| **Hero** | a **Life Arc** — the proving quest | an **immature precursor** to the Warrior | — |
| **Lover** | a **Flat Archetype** — oriented toward one other person | a **faculty** — connection, aliveness, vision | — |
| **Magician / Mage** | a **Life Arc** (Mage) — service beyond self | a **faculty** (Magician) — knowledge, technique | — |
| **Tyrant** | King's **aggressive shadow** | King's **active shadow** | a **villain archetype** (dark CHIEF) |
| **Coward / Bully** | Hero's **passive / aggressive shadows** | Hero's **passive / active shadows** | — |
| **Witch / Sorcerer** | Crone's and Mage's **aggressive shadows** | — | — |

**Convention:** write "the King *arc*" vs. "the King *faculty*"; "the Hero *arc*" vs. "the Hero *precursor*";
"Cowden's TYRANT" when that system is meant.

### A genuine convergence, worth more than the collisions

**Weiland and Moore & Gillette were written independently, sixty years and one discipline apart, and they
arrive at the same shadow pair for the same archetype twice over:**

- **Hero → Coward (passive) and Bully (aggressive).** Identical in both. Moore & Gillette's fuller name is the
  *Grandstander* Bully.
- **King → Tyrant (active/aggressive).** Identical in both.

Both systems also independently use an **active/aggressive vs. passive** bipolar shadow structure as their
organizing principle. **Two independent arrivals at the same structure is real evidence that the structure is
doing work**, and it is the strongest argument available for building the Review Panel on this base rather than
on an invented roster.

---

## 6. Not yet extracted, but present in `Reference/Materials/books/`

Per `Book_TOC_Master_Reference.md`'s uncataloged list. Flagged here so the next reach for one of these does not
repeat the mistake this index was written to prevent:

- *Evolutionary Psychology and Information Systems Research*
- *Mythology* — Matt Clayton
- *Some of the Dead Are Still Breathing*
- *The History of Our Universe in 21 Stars*
- *The Routledge International Handbook of Dialectical Thinking*
- `Math_and_Computation/` (161 files) — **deliberately deferred for TOC cataloging by the developer, 2026-07-23** *(its status in `Book_TOC_Master_Reference.md` is still ⬜; but see Section 4b: the Pisces research opened about ten titles in it, so "not yet mined" is not accurate)*
- `Cpp/` and the other top-level singles — ⬜ not yet cataloged in `Book_TOC_Master_Reference.md`

---

## 7. Maintenance rule

**When a book is extracted, add a row here in the same commit.** An extraction nobody can find is an extraction
that will be done twice — which has already happened once, on Moore & Gillette, and was the reason this file
exists. **It happened again:** by 2026-10-04 this index was 28 days stale (two extractions and five research
folders missing) and had to be rebuilt from the repo. **A new `*_Extraction.md` file, or a new
`*_Research/00_Extraction_Checklist.md`, without a row here is a defect.**

---

## 8. ⭐ Where to pick up *(as of 2026-10-04)*

**In priority order. Nothing below has been started except where stated.** *Hours:* book extraction is bounded
source-preparation, and these files declare themselves NOT canon, so it is read as **any-hour work**
(`project_ebook_prestaging_and_pace_standard`; stated, not assumed). The developer is finishing the Mirny ULM
pass first (2026-10-05).

1. **The all-cities book tally (queued 2026-09-15, NOT started; no tally or book-to-city map exists).** Tally
   `Reference/Materials/books/` (2,308 files) and map books to **all 38 cities up front**, so a city's Step 3
   finds its sources already mined instead of spending the 05:00-14:59 window on book mining (Davis's Step 3
   did). ⛔ **Check contents, not titles**: `City_and_District_Research_Topics.md` is title-matched and
   measurably unreliable (`M-234`: Davis found three of its ratings wrong, including the lowest-rated title
   being its highest-yield one). Method: `pdftotext` the volume (EPUB via `unzip`, DJVU via `djvutxt`, scans
   via `tesseract`) and screen it against each city's named subject terms; start from
   `Book_TOC_Master_Reference.md`; **check Section 1 of this file before mining anything.**
2. **Resume the partial research folders (Section 4b), most useful first:** **Pisces** (17 rows open, though the
   Flood already has a candidate mechanism, `06` and `07`) · **Ice-Cold Buddhism** (5 open; the two EPUBs are
   now readable, so the stale "unreadable" note should be fixed when the checklist is next touched) ·
   **Vostok/Ariun Nuur genetics** (5 open) · **PTSD** (`07`'s missing 30%; the separate dark-humor source
   search).
3. **`Man and His Symbols`: resume at p. 158** (von Franz's *The Process of Individuation*, flagged by the
   book's own intro as possibly the crux; then Jaffé and Jacobi).
4. **Close the TOC-catalog gaps** (`Book_TOC_Master_Reference.md`): `Math_and_Computation/` (161 files; the
   developer deferred it), `Cpp/`, the top-level singles, and the five titles listed in Section 6.
5. **Likely-Mirny geoscience titles** flagged during the Davis pass (Section 4b) are unread: if Mirny's own
   Step 3 wants them, they are already triaged there.
6. **Keep this index current:** add a row in the same commit as any new extraction (Section 7).

**Related, separate track (datasheets, not books):** per `Universal_Location_Methodology/Datasheet_and_PreTrip_Tracker.md`
(2026-09-30), 9 of 38 cities have a full 19-file Tier C datasheet set and 28 have neither datasheets nor a
Pre-Trip sheet. That is its own queue (`project_mechanical_extraction_datasheet_methodology`).
