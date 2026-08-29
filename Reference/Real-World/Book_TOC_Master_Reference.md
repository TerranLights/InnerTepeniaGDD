# Book TOC Master Reference

**Purpose:** a running, resumable index of every book/PDF/EPUB dropped into `Reference/Materials/books/`
across the large mid-2026-07 stash, so future sessions can pick specific books/chapters to extract from
without re-discovering what's available. Per the developer's explicit instruction (2026-07-19): "have a
look through the 'table of contents' pages for all the books, and just keep a reference of what's where,
and we can go through it over the course of multiple windows." **This is a catalog only — nothing listed
here is canon.** Titles, authors, and TOCs only; no content extraction/synthesis has happened except where
a dedicated `_Research/` folder is separately linked below.

**Status legend:** ✅ fully cataloged · 🟡 partially cataloged · ⬜ not yet started

---

## Status overview by folder

| Folder | Status | Files | Notes |
|---|---|---|---|
| `life skills/survival/` | ✅ | 27 | Re-cataloged 2026-07-23 — all 17 former "EPUB, unreadable" titles now have full TOCs |
| `medicine care and first-aid/` | ✅ | 4 | |
| `music theory and composition/` | ✅ | 10 | Re-cataloged 2026-07-23 — all former EPUB/100MB titles now have real TOCs |
| `psychology/` | ✅ | 10 | Re-cataloged 2026-07-23 — former EPUB titles now readable |
| `history/` (incl. `Mexican history/`) | ✅ | 13 | Re-cataloged 2026-07-23 — former EPUB titles now readable |
| `politics/` | ✅ | 4 | |
| `strategy/` | ✅ | 3 | |
| `metals, ores, and geosciences/` | ✅ | 21 | Re-cataloged 2026-07-23 — the "100MB" titles (Structural Geology, Structural Geological Atlas) both have real text layers, fully readable via `pdftotext` |
| `arcology and post-agrarianism/` | ✅ | 1 | Already deep-extracted, see `Davis_Geosciences_Research/` |
| `religion/` (incl. `Buddhism/`, `The Masks of God/`) | ✅ | 16 | Re-cataloged 2026-07-23 — all 4 former "EPUB, unreadable" titles now have full TOCs |
| `STEM/Biology/` (incl. `Genetics/`, `Evolutionary Studies/`, `bioinformatics/`) | ✅ | ~140 in scope | Complete 2026-07-19; re-cataloged 2026-07-23 — former DJVU/100MB/EPUB titles now readable (see Genetics/ and Evolutionary Studies/ entries) |
| `Memetics/` | ✅ | 14 | Flagged 2026-07-20 as Cryptograph Helix "2nd-level topic matter"; re-cataloged 2026-07-23 |
| `economics/` (incl. `Thomas Sowell/`) | ✅ | 16 | Complete 2026-07-23; re-cataloged same day — all 5 scanned Sowell titles now have real TOC/content via OCR |
| `philosophy/` (incl. `Arthur Schopenhauer/`, `Carl Gustav Jung/`, `ethics/`, `Marcus Aurelius/`) | ✅ | ~20 | Complete 2026-07-23; re-cataloged same day — former EPUB/DJVU/scanned titles now readable |
| `games/` (incl. `Chess/`, `Shogi/`) | ✅ | 4 | Complete 2026-07-23; re-cataloged same day — all titles now readable, directly relevant to the flagged Shogi+Chess synthesized-strategy-game minigame idea |
| `Language/` (incl. `psycholinguistics/`, `Sumerian/`) | ✅ | 27 | Complete 2026-07-23 |
| `Linux/` | ✅ | 10 | Complete 2026-07-23 |
| `Math_and_Computation/`, `Cpp/`, top-level singles | ⬜ | unknown | `Math_and_Computation/` (161 files) deliberately deferred by the developer 2026-07-23 ("that will probably eat up the rest of my allotment"); `Cpp/`/singles not yet reached |

**Tooling limitation corrected 2026-07-23:** what was previously flagged throughout this file as "EPUB,
unreadable" was a real but *fixable* tooling gap, not a hard limitation — EPUB is just a ZIP archive of
XHTML files, and `unzip` (already installed) extracts full, clean text plus a ready-made table of contents
(`nav.xhtml`/`toc.ncx`) every time. **DJVU** files are now also readable via `djvutxt` (developer installed
`djvulibre-bin`). **Scanned/image-only PDFs** (no text layer) are now readable via OCR (`pdftoppm` rasterizes
pages, `tesseract` reads them — developer installed `tesseract-ocr`) — slower per file than direct text
extraction, but no longer a hard wall. The **"exceeds 100MB" flag was specifically about the image-based
Read tool's own size ceiling — it never applied to `pdftotext`**, and several titles flagged this way
(Structural Geology, Structural Geological Atlas, Tonal Harmony, Genetics: A Conceptual Approach, Ancestral
DNA, Knots, The Consuming Instinct) turned out to have perfectly normal text layers all along. Every title
below previously marked unreadable/title-only has been re-cataloged with this full toolkit — remaining
"title only" entries are the small number that are genuinely still unreadable (a couple of 9-byte broken
download stubs, one true image-only manga guide, and titles simply not yet revisited).

---

## Life Skills / Survival (27 files)

### Bushcraft 101: A Field Guide to the Art of Wilderness Survival — Dave Canterbury
Introduction; Part 1: Gearing Up (Pack, Tools, Rope/Cordage/Knots, Containers/Cooking, Coverage,
Combustion); Part 2: In the Bush (Setting Up Camp, Navigating Terrain, Trees: The Four-Season Resource)

### Essential Survival Skills — DK/Dorling Kindersley (2011), foreword Colin Towell
Introduction; 1 Before You Go; 2 On the Trail; 3 Camp Craft; 4 Finding Water and Food; 5 In an Emergency

### Knots: The Complete Visual Guide — Des Pawson (2012) — re-cataloged 2026-07-23
A DK visual guide organized by knot category: Getting Started (rope construction/materials/maintenance,
terms and tools, techniques); Stopper Knots (Overhand, Figure-Eight, Stevedore, Monkey's Fist, Wall Knot,
Matthew Walker Knot, Diamond Knot); Binding Knots (True Lover's Knot, Sailor's Cross, Square Knot, Surgeon's
Knot) — continues into further categories beyond what was captured. The "100MB" flag was a Read-tool
limitation only.

### Prepper's Long-Term Survival Guide — Jim Cobb (2014)
12 chapters: Long-Term Events; Water; Food; Medicine; Hygiene; Staying Warm/Cool; Security; Tools;
Surviving Boredom; Barter and Trade; Community Survival Planning; Final Thoughts. Appendix: Checklists.

### The Survival Handbook: A Practical Guide to Woodcraft and Woodlore — Raymond Mears (1990)
Introduction; Possibles; Shelter and Protection; Fire; Water; Plants; Hunting; Tracking; Trapping and
Fishing; Cooking/Preserving/Storing Food; Cordage/Basketry/Pottery/Glue; Stone and Bone Working;
Hideworking; Hitting The Trail

### The Prepper's Water Survival Guide — Daisy Luther (2015)
13 chapters covering dehydration, municipal toxins, water-related illness, water plan/storage/acquisition/
testing/purification, emergency sources, sanitation, conservation.

### The U.S. Navy SEAL Survival Handbook — Don Mann & Ralph Pezzullo (2012)
15 chapters: SEAL/SERE Training; Elements of Survival; Jungle/Mountain-Arctic/Desert/Sea Survival; Basic
Tips; Water; Shelter and Fire; Food and Hunting; Weather; Navigation; Survival Medicine; Survival Kits; The
Mystery of Survival.

### U.S. Military Pocket Survival Guide Plus Evasion & Recovery (2009), rev. SFC Matt Larsen
Evasion; Navigation; Radio Comms/Signaling; Recovery; Medical; Personal Protection; Water; Food; Contact
with the Indigenous; Induced Conditions; Appendix: The Will to Survive.

### Wilderness Survival Handbook — Michael Pewtherer (2010)
Part I: Seven-Day Survival (Preparing, Shelter, Water, Fire, Navigation, Medical Emergencies); Part II:
Beyond Survival — primitive-skills chapters (long-term shelters, fire tools, food/drink, fishing, trapping,
hunting weapons/methods, hideworking, cordage, tools, containers, comfort/cleanliness).

### The following 17 EPUB files — re-cataloged 2026-07-23 via `unzip`, all fully readable

### 100 Deadly Skills Survival Edition — Clint Emerson (2016)
Part I: Personal Preparedness (Become Crisis Proof, Build a Personal EDC Kit, Train to Survive, Prepare a
Vehicle Go-Bag); Part II: Navigation (Environmental/Solar/Celestial/Magnetic Navigation); Part III: Survival
in the Wild — environment-specific chapters (Jungle, Arctic, Desert, Wetland, Mountain), each with its own
minimum EDC, water collection, fire-building, food-finding, and shelter-building entries (continues beyond
what was captured).

### 100 Deadly Skills — Clint Emerson (2015)
Part I: Mission Prep (Anatomy of a Violent Nomad, EDC Kit, Vehicle Bolt Bag, Concealable Compass/Holster,
Escape Tools, Rectal Concealment, Improvised Body Armor); Part II: Infiltration (Crossing Enemy Borders by
Sea/Air/Land, Caches, Scaling Walls, Blending In); Part III: Infrastructure Development — lodging,
transportation, improvised weapons (continues beyond what was captured). The tactical/espionage-survival
counterpart to Emerson's 2016 "Survival Edition" above, not a duplicate.

### 100 Skills You'll Need for the End of the World (as We Know It) — Ana Maria Spagna
An alphabetical almanac of skills (not chaptered survivalism) — entries include Animal Husbandry, Barbering,
Bartering, Basic First Aid, Beekeeping, Bicycle Repair, Blacksmithing, Cairn Building, Canning, Carving,
Cheesemaking, Composting, Dowsing, Dry Farming, Fence Building, Fire Making, and continues alphabetically.

### 2024 Water Survival Handbook: Ultimate Guide to Water Security, Filtration
6 parts: Critical Importance of Water Security; Finding Water Sources Off the Grid (rainwater harvesting,
natural springs, extracting water from plants, solar stills); Water Treatment Methods (filtration types,
purification methods); Safe Water Storage and Maintenance; Advanced Water Management Techniques (rationing,
long-term supply systems); Bonus: Water in Different Survival Scenarios (hot/cold climates, medical
emergencies).

### Advanced Bushcraft — Dave Canterbury (2015)
Chapter 1: Building Your Kit (Ten Cs of Survivability, Core Temperature Control); Chapter 2: Natural
Resources (Pine, Willow, Poplar, Oak, Sassafras, Birch, medicinal preparations); Chapter 3: Wooden Tools
and Simple Machines; Chapter 4: Advanced Firecraft (primitive fire starting, bow and drill, flint and
steel, solar fire); Chapter 5: Sheltering (continues beyond what was captured).

### Bushcraft 101 — Dave Canterbury (1st Ed, 2014) — EPUB copy
Same content as the already-cataloged PDF edition above (Part 1: Gearing Up — Pack, Tools, Rope/Knots; Part
2: In the Bush) — this EPUB confirms and slightly expands the tool chapter (Knives, Saws, Axes, safe
handling/sharpening) beyond what the PDF pass captured.

### Bushcraft First Aid — Dave Canterbury & Jason A. Hunt (1st Ed, 2017)
Introduction: What is Wilderness First Aid?; Chapter 1: Know Before You Go (emergency planning, stress,
infectious disease precautions); Chapter 2: Survival Skills for the Wilderness (the Ten Cs, five-minute
fire/shelter/water boil, common outdoor injuries); Chapter 3: The Emergency Scene (first approach, mechanism
of injury, AVPU, ABCs, vital signs, physical exam — continues beyond what was captured).

### Prepper's Survival Hacks — Jim Cobb (2015)
50 DIY projects organized by category: Water (transpiration bag, solar still, osmosis/layered filters); Food
Acquisition (pocket fishing kit, DIY MRE, bola, cold frame, seed tape); Cooking (buddy burner, brick rocket
stove, hobo stove, Altoids tin stove); Fire (wax melting, egg carton/cotton pad/self-igniting fire starters,
fire straws, baton firewood); Lighting (Altoids tin candle/oil lamp, crayon candles) — continues beyond what
was captured.

### SAS and Elite Forces Guide: Hunting — Chris McNab (2013)
7 chapters: Weapons; Tracking and Hides; Traps and Snares; Hunting with Dogs; Hunting Techniques: Birds;
Hunting Techniques: Land Animals; Butchering, Smoking and Preparing Food; plus an appendix on survival foods.

### SAS Survival Handbook: The Ultimate Guide to Surviving Anywhere — John "Lofty" Wiseman (3rd Ed, 2014) — 2 copies, confirmed duplicates
12 numbered chapters: Essentials; Strategy; Climate & Terrain; Food; Camp Craft; Reading the Signs; On the
Move; Health; Survival at Sea; Rescue; Urban Survival; Disasters — plus a Postscript. Both EPUB copies in
this folder share identical internal file structure (same ISBN-derived filenames) — genuinely the same
edition, not two different printings.

### SAS Urban Survival Handbook — John "Lofty" Wiseman
12 chapters: Essentials; Safety First; DIY/Craft Hazards; Poisons; Fire!; Security; Work & Play; In Transit;
Self-Defence; Terrorism; Disasters; Health.

### The Bushcraft Field Guide to Trapping, Gathering, and Cooking in the Wild — Dave Canterbury (2016)
Part 1: Packed-In Food (deciding what to bring, minimal-processing foods, whole foods, supplemental
foodstuffs); Part 2: Bushcraft Cooking Methods (fire-building, tools, quick bush tools, types of cooking);
Part 3: Living Off the Land (hunting/trapping fundamentals and beyond, butchering game, catching fish/frogs,
foraging, preserving foods); Part 4: Emergency Cooking (cooking with your engine, unconventional fuels,
stove-making, solar cooking); Appendix: Nutritional Values of Game Animals and Nuts.

### The Complete Survival Medicine Handbook
Chapters confirmed through "Common Emergencies in Children: What To Do?" and a closing Conclusion — a
practical home-medical-emergency guide (structure similar in spirit to the other survival-medicine titles
in this collection, distinct authorship).

### The Resilient Farm and Homestead — Ben Falk
An Innovative Permaculture and Whole Systems Design Approach. 7 chapters: Creating a Positive Legacy While
Adapting to Rapid Change; The Design Process and Site Establishment; Water and Earthworks; Fertility
Harvesting and Cycling; Food Crops; Adaptive Fuel and Shelter; Resilience and Regeneration for the Long
Haul. Appendices include a Resiliency Aptitude Quiz, a Homestead Curriculum Outline, an Emergency Skill
List, a Vulnerability Checklist, and a Vocabulary/Concepts glossary.

### The Survival Medicine Handbook: A Guide for When Help Is Not on the Way — Joseph Alton & Amy Alton (2nd Ed, 2013)
Section 1: Principles of Medical Preparedness (integrated medicine, wilderness vs. conventional medicine,
importance of community); Section 2: Becoming a Medical Resource (status assessment, likely medical issues,
medical supplies, natural remedies, essential oils, medicinal gardens — continues beyond what was captured).

### The Ultimate Guide to U.S. Army Survival Skills, Tactics, and Techniques (2011)
Part I: General Survival Skills (Psychology of Survival, Survival Planning and Kits); Part II: Survival
Medicine (fundamental first-aid criteria, basic measures, first aid for special wounds/fractures/climatic
injuries — a direct adaptation of official U.S. Army field manual content, continues beyond what was
captured).

### Non-book: `to_download.txt` — list of 7 zlibrary onion-URL download links, not a book.

---

## Medicine, Care and First-Aid (4 files)

### Brain Neurotrauma: Molecular, Neuropsychological, and Rehabilitation Aspects — ed. Firas H. Kobeissy (2015)
8 sections (Neuromechanisms; Management; Modeling; Imaging/Biomarkers; Neurocognitive/Neurobehavioral;
Neurorehabilitation/Neuroprotection; Mild TBI/Sport Concussion; Substance Abuse/Comorbid).

### Phantoms in the Brain — V.S. Ramachandran & Sandra Blakeslee (1998), foreword Oliver Sacks
TOC not reached within read range (front matter only).

### Physics in Biology and Medicine, 3rd Ed — Paul Davidovits (2008)
17 chapters: Static Forces, Friction, Translational/Angular Motion, Elasticity, Insect Flight, Fluids, Heat/
Kinetic Theory, Thermodynamics, Heat and Life, Waves/Sound, Electricity, Optics, Atomic/Nuclear Physics.

### The Tell-Tale Brain — V.S. Ramachandran (2011)
Intro: No Mere Ape; Phantom Limbs/Plastic Brains; Seeing and Knowing; Synesthesia; Mirror Neurons and
Civilization; Autism; Language Evolution; Aesthetics; Universal Laws of Art; Introspection/Soul; Epilogue.

---

## Music Theory and Composition (10 files)

### A Geometry of Music — Dmitri Tymoczko (2011)
Part I Theory (5 chapters incl. "A Geometry of Chords"); Part II History/Analysis (Extended Common
Practice, Functional Harmony, Chromaticism, 20th-C. Scales, Jazz); Conclusion; 6 Appendices.

### Contemporary Orchestration — R.J. Miller (2014/2015)
16 chapters: Preliminary Considerations through instrument families (Violin, Brass, Woodwind, Percussion,
Voices, Harp, Guitar), Orchestral/Wind-Ensemble/Musical-Theater scoring, Substitution guides.

### `d.txt` — not a book, 3 zlibrary onion links.

### Harmony, 5th Ed — Walter Piston (rev. Mark DeVoto)
Scales/Intervals, Triads, Harmonic Progression... through Nondominant Harmony, Neapolitan Sixth,
Augmented Sixth Chords, Other Chromatic Chords, Conclusion.

### Orchestration — Walter Piston (1955)
Part One: Instruments of the Orchestra (18 chapters by instrument); Part Two: Analysis of Orchestration
(Types of Texture I-VII); Part Three: Problems in Orchestration (Melody, Accompaniment, Chord Scoring,
Voice Leading/Counterpoint).

### Orchestration — Cecil Forsyth (1982) — re-cataloged 2026-07-23
List of Instruments; Classification of Instruments; Percussion Instruments; Brass Instruments; The
Trombones; Wood-Wind Instruments; Stringed Instruments; Addenda; Appendix.

### Principles of Orchestration — Nikolay Rimsky-Korsakov (1964) — re-cataloged 2026-07-23
Chapter I: General Review of Orchestral Groups (stringed instruments; wind instruments — wood-wind, brass;
instruments of little sustaining power — plucked strings, pizzicato, harp; percussion instruments,
determinate and indeterminate sound; comparison of resonance across orchestral groups); Chapter II: Melody
(melody in stringed instruments — unison/octave/three-four-octave grouping, thirds and sixths; melody in
the wood-wind) — continues beyond what was captured. With musical examples drawn from the composer's own
works.

### Taiko Boom: Japanese Drumming in Place and Motion — Shawn Bender (2012)
Part One: Emergence/Popularization of Taiko (drum makers, Osuwa Daiko/Sukeroku Daiko/Ondekoza genealogy,
Ondekoza→Kodo, festival creation); Part Two: Discourses (embodiment/race/place, gender, militarism/
nationalism debates); Epilogue: Taiko at Home and Abroad.

### The Study of Orchestration, 3rd Ed — Samuel Adler (2002)
Part One: Instrumentation (bowed strings, plucked strings, woodwind choir, brass, percussion, keyboard);
Part Two: Orchestration (scoring for orchestra/band, transcribing, score prep).

### Tonal Harmony, 8th Ed: With an Introduction to Post-Tonal Music — Kostka, Payne, Almén (2017) — re-cataloged 2026-07-23
6 parts, 28 chapters: Part One (Ch. 1-4) fundamentals; Part Two (Ch. 5-13) voice-leading principles; Part
Three (Ch. 14-15) diatonic seventh chords; Part Four (Ch. 16-17+) chromaticism/secondary functions; Part
Six (Ch. 26-28) introduction to post-tonal music (scales, chord structures, voice leading). The "100MB"
flag was a Read-tool limitation only — `pdftotext` reads it cleanly.

---

## Psychology (10 files)

### Cognitive Warfare — François du Cluzel, NATO ACT Innovation Hub (2020)
Advent of Cognitive Warfare (info→cognitive warfare, hacking the individual, participatory propaganda,
cyberpsychology); Centrality of the Human Brain; Militarisation of Brain Science (NeuroS/T); Towards a New
Operational Domain (Russian/Chinese CW definitions, NATO recommendations); Annexes on China/Russia.

### Fear of Intimacy — Robert W. Firestone & Joyce Catlett, APA (1999)
I. Foundations (Why Relationships Fail, Ideal Couple/Family); II. Psychodynamics (Inwardness, Fantasy
Bond, Withholding, Men, Women); III. Countering the Inner Voice (Voice Therapy method, pilot study).

### Manipulism and the Weapon of Guilt: Collectivism Exposed — Mikkel Clair Nissen (2015)
10 chapters incl. "Cold War II," "A New World Disorder," "A State of Psychopathy," "Big Mother's
Indoctrination Program."

### Susan Forward (with Craig Buck) — Toxic Parents (Bantam, 2002 printing)
Part 1: Toxic Parents (Godlike, Inadequate, Controllers, Alcoholics, Verbal/Physical/Sexual Abusers, Why
Parents Behave This Way); Part 2: Reclaiming Your Life (forgiveness, self-definition, confrontation,
healing incest wound, breaking the cycle).

### The Psychology of Religion: An Empirical Approach, 4th Ed — Hood, Hill, Spilka (Guilford, 2009)
TOC not reached within read range.

### The True Believer: Thoughts on the Nature of Mass Movements — Eric Hoffer (1951/2002)
Part 1: Appeal of Mass Movements; Part 2: The Potential Converts (Undesirables, Poor, Misfits, Selfish,
Ambitious, Minorities, Bored, Sinners); Part 3: United Action/Self-Sacrifice; Part 4: Beginning and End
(Men of Words, Fanatics, Practical Men of Action, Good/Bad Mass Movements).

### Thought Reform and the Psychology of Totalism — Robert Jay Lifton, M.D. (1961/1989)
Part One: The Problem; Part Two: Prison Thought Reform of Westerners (individual case studies); Part
Three: Thought Reform of Chinese Intellectuals; Part Four: Totalism and Its Alternatives.

### Dark Psychology Secrets: The Essential Guide to Persuasion, Emotional Manipulation, Deception, Mind Control, Human Behavior, NLP and Hypnosis (2019) — re-cataloged 2026-07-23
7 chapters: What Is Dark Psychology?; The Basics of Covert Emotional Manipulation (propaganda, NLP, pick-up
artist techniques, defending against covert manipulation); Analyzing Dark Psychology; Manipulation (steering
attention, the problem/reaction/solution cycle, gradation/postponement of changes); Hypnosis (self-hypnosis,
stage hypnosis, subliminal messaging); Persuasion; Deception.

### Toxic Parents — Susan Forward (1989 printing) — EPUB duplicate
Same content as the already-cataloged 2002 printing above (Part 1: Toxic Parents; Part 2: Reclaiming Your
Life) — confirmed a genuine duplicate, not a revised edition.

### The Human Magnet Syndrome: Why We Love People Who Hurt Us — Ross A. Rosenberg (2013) — re-cataloged 2026-07-23
15 chapters: The Inevitability of Our Future; Codependents, Emotional Manipulators and Their "Dance";
Emotional Manipulator & Codependent Relationship Dynamics; "The Odd but Natural Couple"; Introducing the
Continuum of Self Theory; The Emotional Manipulation Disorders; The Human Magnet Syndrome; Origins of
Codependency; Origins of Emotional Manipulation Disorders; Codependency; Narcissistic Personality Disorder;
Borderline Personality Disorder; Antisocial Personality Disorder; Why We Can Reach Codependents and Not
Emotional Manipulators; The "Golden Rule" of the Helping Professions.

---

## History (13 files, incl. `Mexican history/` subfolder)

### A Brief History of Afghanistan, 2nd Ed — Shaista Wahab & Barry Youngerman (2010)
12 chapters spanning prehistory through 2010 (Rise of Islam, Birth of Modern Afghanistan, 20th-C.
Monarchy, Coup/Revolution, Soviet Afghanistan, Mujahideen, Taliban Era, post-2001).

### A Brief History of Chinese and Japanese Civilizations, 4th Ed — Schirokauer, Brown, Lurie, Gay (2013)
(2 identical-content copies, different scan resolutions.) 25 chapters across 6 parts, ancient China
through postwar Japan/China to present.

### A Brief History of Korea — Mark Peterson & Phillip Margulies (2010)
8 chapters: prehistory→Silla unification, Unified Silla/Koryo, Choson (early/mid, late), Japanese Colony,
Liberation/Division/Korean War, South Korea's Democracy, North Korea.

### Born in Blood and Fire: A Concise History of Latin America, 4th Ed — John Charles Chasteen (2016)
11 chapters (Encounter, Colonial Crucible, Independence, Postcolonial Blues, Progress, Neocolonialism,
Nationalism, Revolution, Reaction, Neoliberalism) each with boxed "Countercurrents" sidebars.

### Ghost Soldiers — Hampton Sides (2002)
WWII Bataan Death March/Cabanatuan rescue narrative; no formal chapter TOC visible in front matter, opens
directly with Prologue (Dec. 1944, Palawan).

### In the Land of White Death: An Epic Story of Survival in the Siberian Arctic — Valerian Albanov, preface Jon Krakauer, intro David Roberts — re-cataloged 2026-07-23
A real 1917 Arctic survival memoir: Why I Left the Saint Anna; Preparations for the Sledge Expedition; Last
Day on Board the Saint Anna; Over the Polar Ice Pack; Death of Sailor Bayev; Further Discouragement,
Exhaustion; Drifting Southward; Land Ho!; Alexandra Land; The Fateful Journey to Cape Flora; Cape Flora,
Jackson and Ziegler's Camp; Preparing to Winter Over at Cape Flora; Ship Ahoy!; Leaving Franz Josef Land.
Directly relevant to Sagittarius/Frostlands survival-narrative material — a genuine first-person polar
survival account, not a how-to guide.

### The Secret History of the Mongol Queens: How the Daughters of Genghis Khan Rescued His Empire — Jack Weatherford (1st Ed, 2010) — re-cataloged 2026-07-23
Introduction: The Missing Chapter; Part I: Tiger Queens of the Silk Route 1206-1241 (4 chapters); Part II:
The Shattered Jade Realm 1242-1470 (5 chapters); Part III: Wolf Mother 1470-1509 (4 chapters); Epilogue:
The Secrets of History.

### Mexican history/ subfolder:

**A Brief History of Mexico, 4th Ed — Lynn V. Foster (2010).** 12 chapters: First Peoples/Pre-Columbian,
Diversity of Mesoamerican Civilization, Age of Conquest, Founding of an Empire (16th-C.), Colony of New
Spain, Bourbon Reforms/Independence, Years of Chaos, Porfiriato Dictatorship, Revolution of 1910,
Institutionalized Revolution, March toward Democracy, A More Democratic Mexico (2000-2009).

**Fire and Blood: A History of Mexico — T.R. Fehrenbach** (PDF + duplicate EPUB). Part One: The Tyranny of
Circumstance: The Amerindians (Ch.1 The Old Ones — Paleo-American migration; Ch.2 Farmers and Magicians —
origin of agriculture); continues through conquest and modern Mexico (later parts not reached in this
pass).

**The History of Mexico — Burton Kirkwood** (Greenwood Histories of the Modern Nations series, 2000). 11
chapters: Mexico Today, Early Inhabitants, The Conquest, Colonial Era (1521-1821), Wars of Independence
(1808-1821), Aftermath of Independence (1821-1876), The Porfiriato (1876-1911), The Mexican Revolution
(1910-1920), Consolidation of the Revolution, Revolution Moves to the Right (1940-1970), Search for
Stability (1970-1999). Plus Notable People and Bibliographic Essay appendices.

**The History of the Conquest of Mexico — William Hickling Prescott (1843)**, Modern Library edition. 7
Books: I. Introduction/View of Aztec Civilization (climate, succession/nobility/law, mythology, Aztec
hieroglyphics, agriculture/mechanical arts, the Tezcucans); II. Discovery of Mexico (Spain under Charles
V, Cortés's early life, embarkation, Cozumel/Tabasco, Doña Marina, Montezuma/his empire); III. March to
Mexico (Cempoalla, Tlascala, Cholula massacre, arrival in the Valley); IV. Residence in Mexico (Tezcucan
Lake, market/Great Temple, seizure of Montezuma); V. Expulsion from Mexico (*Noche Triste*); VI. Siege and
Surrender of Mexico; VII. Conclusion — Subsequent Career of Cortés.

---

## Politics (4 files)

### Routledge Handbook of Military Ethics — ed. George Lucas, foreword Gen. Martin E. Dempsey (2015)
37 chapters, 5 parts: I. Moral Foundations of the Military Profession; II. *Jus Ante Bellum*: Preparing
the Profession (incl. Selective Conscientious Objection, Military Culture and War Crimes); III. Military
Ethics and Professionalism Across Nations/Cultures (incl. Sun Tzu, PLA, Japanese Warfare Ethics); IV.
Contemporary Issues (Defense Systems Acquisition, Civilian-Military Chain of Command, Military Medical
Ethics, DADT, Gender/Sexual Assault); V. Emerging Challenges (Armed Humanitarian Intervention, Private
Military Contractors, Human Terrain System, Media/Law, Drones and Targeted Killings, Non-Lethal Weapons,
"Captain America and Iron Man: Biological/Genetic/Psychological Enhancement," "Just War Under CyberGaia").

### All Minus One: John Stuart Mill's Ideas on Free Speech Illustrated — ed. Richard V. Reeves & Jonathan
Haidt, art Dave Cicirelli (Heterodox Academy, 2018)
Illustrated/graphic-novel-format extract of ~half of Ch.2 of Mill's *On Liberty*. Structure: Introduction
(editors' framing of the free-speech debate) → "Mill's First Argument: 'The Opinion May Possibly Be
True'" (full illustrated text of Mill's fallibility argument, historical examples of truth suppressed by
persecution — Reformation, Christianity in Rome, Socrates). No further formal chapter breaks within the
15-page read range; a short, single-argument excerpt rather than a full-book TOC.

### The Federalist Papers — Hamilton, Madison, Jay, ed. Lawrence Goldman (Oxford World's Classics, 2008)
Introduction; Note on the Text; Synopsis of The Federalist Papers; Select Bibliography; Chronology of
Events 1763-1791; Map of the US c.1789; **THE FEDERALIST PAPERS** (all 85 essays); Appendix: The
Constitution of the United States (1787 and 1791); Explanatory Notes; Thematic Index.

### The Vision of the Anointed: Self-Congratulation as a Basis for Social Policy — Thomas Sowell (1995)
9 chapters: Flattering Unction; The Pattern; By the Numbers; The Irrelevance of Evidence; The Anointed
versus the Benighted; Crusades of the Anointed; The Vocabulary of the Anointed; Courting Disaster;
Optional Reality. Plus Notes and Index.

---

## Strategy (3 files/folders)

### I'll Make You an Offer You Can't Refuse: Insider Business Tips from a Former Mob Boss — Michael
Franzese (Thomas Nelson, 2009/2011)
(Two near-identical PDF copies in a dedicated subfolder.) 11 chapters: Mob Up Your Business; First, Nail
Down the Basics; Next, Beware Machiavelli's Trap; Use Solomon's Solution; Lead with Your Brain, Not Your
Mouth; Master the Art of the Sit-Down; Keep Your Eyes on the Bookies; Learn from Your Failures; Play It
Straight and Legal; Pick Your Philosopher: Machiavelli or Solomon?; Get the Right Idea About Success. Plus
Closing Thoughts, Afterword ("The Broken Business of Government"). Author is a former Colombo-family capo
(retired 1990s); book reframes his own organized-crime business experience as legitimate management
advice. **Likely relevant to the standing "Mafia culture and history" note flagged for Pisces**, despite
being filed under strategy rather than a dedicated crime-history folder.

### The Complete Art of War — Sun Tzu, Carl von Clausewitz, Niccolò Machiavelli, Baron de Jomini (Start
Publishing anthology, 2012)
Four bundled classic translations:
- **Sun Tzu, tr. Lionel Giles** — 13 chapters (Laying Plans, Waging War, Attack by Stratagem, Tactical
  Dispositions, Energy, Weak Points and Strong, Maneuvering, Variation in Tactics, The Army on the March,
  Terrain, The Nine Situations, The Attack by Fire, The Use of Spies).
- **Clausewitz, *On War*, tr. Col. J.J. Graham** — Books I-IV (Nature of War; Theory of War; Strategy in
  General — incl. Moral Forces, Boldness, Perseverance, Surprise, Economy of Forces; The Combat — incl.
  Effects of Victory, Retreat after a Lost Battle, Night Fighting).
- **Machiavelli, *The Art of War*** — 7 Books.
- **Baron de Jomini, *The Art of War*** — Definitions of Branches of the Art of War, Statesmanship in
  Relation to War, Military Policy, Definition of Strategy, Grand Tactics/Battles, Logistics, Formation of
  Troops, Conclusion, Appendices.

### The Prince — Niccolò Machiavelli, tr. Harvey C. Mansfield, 2nd Ed (University of Chicago Press,
1985/1998)
Introduction (Mansfield's extensive scholarly essay on Machiavelli's departure from classical/Christian
political morality); Note on Translation; Chronology; Map; **The Prince** — Dedicatory Letter + 26
chapters (I. Kinds of Principalities through XXVI. Exhortation to Seize Italy and Free Her from the
Barbarians); Appendix: Machiavelli's Letter of Dec. 10, 1513; Glossary; Bibliography; Index of Proper
Names.

---

## Metals, Ores, and Geosciences (21 files)

*Cross-reference: Davis-relevant extraction already deep-processed separately, see
`Davis_Geosciences_Research/01_Groundwater_and_Lake_Chemistry.md`. Several titles here are flagged as
better-fit for **Mirny** (industrial/quarrying identity, post-2026-07-16).*

- **Basic Geological Mapping, 4th Ed** — Barnes & Lisle (2004). Field equipment, geological/base maps,
  mapping methods, field measurements, rocks/fossils/ores, field notebooks, fair-copy maps, cross-sections,
  geological reports. General field-methodology text.
- **Environmental Science Demystified** — Linda D. Williams (2005). Atmosphere/ecosystems/greenhouse
  effect; hydrologic cycle/oceans/glaciers/water pollution; weathering/deserts/geochemical cycling/waste;
  fossil fuels/nuclear/solar/wind/hydro/geothermal energy.
- **Exploration Geophysics** — Gadallah & Fisher (2009). Geophysical techniques, seismic fundamentals/data
  acquisition/processing/interpretation, 4-D surveys. **Likely Mirny.**
- **Geochemistry: An Introduction, 2nd Ed** — Francis Albarède (2009). Elements, mass conservation,
  isotope fractionation, geochronology, element transport, natural-water chemistry, biogeochemistry,
  mineral reactions, solid Earth, Earth in the Solar System.
- **Geological Structures and Maps: A Practical Guide, 4th Ed** — Richard J. Lisle (2021). Maps, dipping
  beds, folding, faulting, unconformity, igneous rocks, cleavage. General methodology.
- **Groundwater Geochemistry** — Merkel & Planer-Friedrich (2005). PHREEQC modeling manual — see Davis
  research file for the one genuine narrative find (extreme halophiles/thermophiles table).
- **Groundwater Geophysics: A Tool for Hydrogeology** — ed. Reinhard Kirsch (2006). Petrophysical
  properties, seismic/geoelectrical/EM methods, GPR, magnetic resonance sounding, aquifer structures
  (pore/fracture/cave), saltwater intrusion, vulnerability mapping.
- **Hydrothermal Processes and Mineral Systems** — Franco Pirajno (2009). Water/hydrothermal fluids on
  Earth, wall-rock alteration, tectonic settings, intrusion-related/porphyry/epithermal/skarn/submarine
  systems, metalliferous sediments, orogenic systems. **Likely Mirny.**
- **Introduction to Geochemistry: Principles and Applications** — Kula C. Misra (2012). Crystal chemistry,
  thermodynamics, geothermometry, aqueous-solution/redox reactions, reaction kinetics, radiogenic/stable
  isotopes, core-mantle-crust and crust-hydrosphere-atmosphere systems.
- **Introduction to Optical Mineralogy, 2nd Ed** — William D. Nesse (1991). Light, petrographic microscope,
  refractometry, isotropic/anisotropic optics, uniaxial/biaxial optics, mineral identification by class.
  General lab methodology.
- **Magmatic Sulfide Deposits: Geology, Geochemistry and Exploration** — Anthony J. Naldrett (2004).
  Komatiite-related deposits, flood-basalt volcanism, Pechenga/Voisey's Bay/Jinchuan/Sudbury deposits, PGE
  deposits. **Likely Mirny.**
- **Metals and Society: An Introduction to Economic Geology** — Arndt & Ganino (2012). Ore classification,
  magmatic/hydrothermal/sedimentary-surficial deposits, future of economic geology. **Likely Mirny.**
- **Mineral Resources: From Exploration to Sustainability Assessment** — Manuel Bustillo Revuelta (2018).
  Exploration, evaluation, extraction, processing, environment/sustainability, mining software. **Likely
  Mirny.**
- **Principles of Geochemistry** — Giulio Ottonello (1997, transl.). Crystal-phase geochemistry
  (thermodynamics, defect chemistry, silicates), silicate melts, fluids (aqueous/gaseous), trace-element
  and isotope geochemistry methods.
- **Risk Management in Evaluating Mineral Deposits** — Jean-Michel Rendu (2017). Mining as risky business,
  Monte Carlo simulation, decision trees, resource modeling, geology/mining engineering/metallurgy/
  infrastructure/management chapters, triple-bottom-line utility. **Likely Mirny.**
- **Structural Geological Atlas** — Soumyajit Mukherjee, Narayan Bose, Rajkumar Ghosh, et al. — re-cataloged
  2026-07-23. Confirmed a genuine photographic/field atlas (not a chapter-based textbook) — captioned
  structural-geology field photographs (brittle shear planes, fault gouge, fracture systems) with precise
  real-world locations (e.g., Malani rhyolite/granite outcrops near Ratanada temple, Barmer Basin, India).
- **Structural Geology** — Haakon Fossen (Cambridge, 2010) — re-cataloged 2026-07-23. 14 chapters: Structural
  Geology and Structural Analysis; Deformation; Stress; Stress in the Lithosphere; Rheology; Fracture and
  Brittle Deformation; Faults; Kinematics and Paleostress in the Brittle Regime; Deformation at the
  Microscale; Folds and Folding; Foliation and Cleavage; Lineations; Boudinage (continues). An applied
  textbook with industry links to petroleum and groundwater geology.
- **Subsurface Hydrology** — Pinder & Celia (2006). Fluid flow/mass transport, geologic setting, well
  hydraulics, numerical solutions, contamination, groundwater-surface-water interaction, remediation,
  multifluid flow.
- **World Geologic Atlas, Sheet 17 (Antarctica)** and **Sheet 18 (Antarctic Ocean)** — Choubert &
  Faure-Muret. Zip archives, format not yet confirmed (image plates vs. text) — worth checking directly
  for Vestfold Hills-specific detail.

---

## Religion (16 files, incl. Buddhism/ and The Masks of God (4 volumes)/ subfolders)

### A New History of Shinto (Blackwell Brief Histories of Religion) — John Breen & Mark Teeuwen
6 chapters: Alternative Approach to Shinto History; Kami Shrines/Myths/Rituals; History of a Shrine (Hie);
History of a Myth (Sun-Goddess/Rock-Cave); The *Daijōsai* (Imperial Accession Rite); Issues in
Contemporary Shinto.

### The Age of Spiritual Machines — Ray Kurzweil
Prologue; Part One: Probing the Past (Law of Time/Chaos, Intelligence of the Universe, Mind and Machines,
New Form of Intelligence, Context/Knowledge); Part Two: Preparing the Present (Building New Brains/Bodies,
1999); Part Three: To Face the Future (2009/2019/2029/2099); Epilogue.

### The Bonobo and the Atheist: In Search of Humanism Among the Primates — Frans de Waal (2013) — re-cataloged 2026-07-23
8 chapters: Earthly Delights; Goodness Explained; Bonobos in the Family Tree; Is God Dead or Just in a
Coma?; The Parable of the Good Simian; Ten Commandments Too Many; The God Gap; Bottom-Up Morality.

### The Moral Animal: Evolutionary Psychology and Everyday Life — Robert Wright — re-cataloged 2026-07-23
Introduction: Darwin and Us; Part One: Sex, Romance, and Love (6 chapters incl. Darwin's own marriage and
"The Darwin Plan for Marital Bliss"); Part Two: Social Cement (Families, Darwin and the Savages, Friends,
Darwin's Conscience); Part Three: Social Strife (Darwin's Delay, Social Status, Deception and
Self-Deception, Darwin's Triumph); Part Four: Morals of the Story (Darwinian and Freudian Cynicism,
Evolutionary Ethics, Blaming the Victim, Darwin Gets Religion).

### Buddhism/ subfolder:

- **Buddhism and Intelligent Technology: Toward a More Humane Future — Peter D. Hershock.** Buddhism as
  philosophical repertoire, AI history, intelligent-technology revolution, attention-capture futures to
  avoid, ethics of intelligence, Confucian/Socratic/Buddhist agency dimensions, humane becoming, data
  governance and education as middle paths.
- **Buddhism and Linguistics: Theory and Philosophy — ed. Manel Herat.** Buddhist philosophy of language in
  India, Zen language/reality/interpretation, medieval Japanese Buddhism as semiotics, object-hood in
  Buddhist philosophy, linguistic authentication of tradition, Buddhism and Chinese linguistics, tantric
  epistemology/ineffability.
- **Buddhist and Taoist Systems Thinking — Josep M. Coll.** Business-paradigm framing: ego-system→
  eco-system, TAO 4.0 adaptive thinking, Yin-Yang/Five Elements balance, T-Qualia learning, Zen business
  model, "Gaia Organization"/"Gaia Startup," abundance beyond triple bottom line, business mindfulness.
- **Rethinking Meditation: Buddhist Meditative Practice in Ancient and Modern Contexts** — re-cataloged
  2026-07-23. Part I: Thinking about Meditation (meditative practices ancient/modern, "Filters and Magnets,"
  meditation as cultural practice and as secularism, ethical subjects; Neural Maps and Enlightenment
  Machines — the "Enlightenment Machine," meditation as a science of mind, theater-of-the-mind vs.
  self-as-brain models; Meditation and Social Imaginaries); Part II: Meditation in Context (the Pali social
  imaginary — phenomenology/ethics of monastic mindfulness, corporeal and cognitive mindfulness — continues
  beyond what was captured).
- **The Buddhist Analysis of Matter — Y. Karunadasa (2020, Wisdom Publications), foreword Richard
  Gombrich.** Definition of matter/basic material factors, primary elements, secondary elements (2
  groups), classification/correlation, atomic clusters, time/temporality, ethico-philosophical basis.
- **The Buddhist Theory of Self-Cognition** (2022, Routledge) — re-cataloged 2026-07-23. 1 Introduction; 2
  Origin: Mahāsāṃghika (the origin of self-cognition, its Abhidharma, "All-Knowing Awareness," influence on
  Yogācāra, the Andhakas' arguments); 3 Refutation: Sarvāstivāda (awareness of a single moment, refutation
  of self-awareness, causality, epistemology, soteriology, self and other) — continues beyond what was
  captured.
- **The Four Noble Truths: Fundamentals of the Buddhist Teachings — HH the XIV Dalai Lama** (tr. Thupten
  Jinpa). Introducing the Four Noble Truths; Truth of Suffering; Truth of Origin of Suffering; Truth of
  Cessation; Truth of the Path; Appendix: Compassion as Basis for Human Happiness.
- **The Philosophy of Zen Buddhism — Byung-Chul Han (2022, Polity Press).** A Religion without God;
  Emptiness; No One; Dwelling Nowhere; Death; Friendliness.

### The Masks of God (4 volumes) — Joseph Campbell:

- **Vol. 1, Primitive Mythology (1960).** Prologue; Part One: Psychology of Myth; Part Two: Mythology of
  Primitive Planters; Part Three: Mythology of Primitive Hunters (incl. Shamanism, Paleolithic Caves); Part
  Four: Archaeology of Myth; Conclusion: The Functioning of Myth.
- **Vol. 2, Oriental Mythology (1962).** Part One: Separation of East and West; Part Two: Mythologies of
  India (Ancient, Buddhist, Golden Age); Part Three: Mythologies of the Far East (China, Japan, Tibet).
- **Vol. 3, Occidental Mythology (1965).** Part One: Age of the Goddess; Part Two: Age of Heroes (Levant,
  European West, 1500-500 B.C.); Part Three: Age of the Great Classics (Persian, Hellenistic, Roman); Part
  Four: Age of the Great Beliefs (Cross and Crescent, Europe Resurgent).
- **Vol. 4, Creative Mythology (1968).** Part One: The Ancient Vine; Part Two: The Waste Land; Part Three:
  The Way and the Life; Part Four: New Wine (incl. "The Death of 'God'").

---

## STEM/Biology (~140 files in scope) — ✅ COMPLETE (2026-07-19)

**Fully cataloged.** Ten parallel cataloging sub-agents were originally dispatched for this folder tree on
2026-07-19 and all ten failed, hitting the weekly/session API limit mid-run (error: "You've hit your
session limit · resets 4am (America/Los_Angeles)"). After the session window reset, the remainder was
completed via direct, sequential, one-task-at-a-time work (per the developer's explicit instruction),
using `pdftotext` (much faster than image-based Read for text-layer PDFs) with Read as fallback for
scanned/image-only files. See `STEM_Biology_Cataloging_Checklist.md` for the full per-folder status log.
`primates/` (23 files) and `Why is the Penis Shaped Like That` were dropped from scope by the developer as
belonging to a different, unrelated project.

**Live progress tracker:** `Reference/Real-World/STEM_Biology_Cataloging_Checklist.md` — granular per-folder
status log, now fully ✅. Background sub-agent delegation for this folder tree failed twice in a row
(10-way fan-out, then a smaller-batch retry) with a hard "session limit" API error — the remainder was
completed one task at a time via direct reads (`pdftotext` where a text layer existed, image-based Read as
fallback), which worked reliably throughout.

**Final subfolder structure, all ✅ done or explicitly dropped by the developer:**
- `STEM/Biology/` top-level files (16) — ✅ done, see writeup below (incl. Guyton & Hall's *Textbook of
  Medical Physiology*, Chakravarthy's *Demystifying the Brain*, *Computational-Biology.pdf*)
- `STEM/Biology/bioinformatics/` — ✅ already deep-extracted, see `Vostok_Genetics_Research/` (Brazma's
  *Living Computers*, Păun/Rozenberg/Salomaa's *DNA Computing*, that folder's `01_` and `02_` files)
- `STEM/Biology/Why is the Penis Shaped Like That - Jesse Bering` — **dropped**, developer confirmed
  2026-07-19 not necessary
- `STEM/Biology/Evolutionary Studies (Biology and Psychology)/` top-level (14 files) — ✅ done, see writeup
  below (several sex/mating-focused titles flagged by the developer as accidentally-included stray files
  from a different, unrelated project)
  - `.../The Handbook of Evolutionary Psychology, 2 Volumes` — ✅ done
  - `.../primates/` (23 files) — **dropped**, developer confirmed 2026-07-19: "that's for a totally
    different project altogether"
- `STEM/Biology/Genetics/` top-level files (18) — ✅ done, see writeup below; all subfolders ✅ done:
  `basics/`, `Ecological Genetics/`, `nanotech/`, `DNA [Genetic] Computing/`, `docs/`, `recombination/`,
  `synthetics/`, `forensics/`, `identification/`, `shit for later/`, `Bioinformatics/` (19 files, distinct
  from the top-level `bioinformatics/` folder above)

Also confirmed relevant per the developer's 2026-07-20 scope-expansion note (see `Vostok_Genetics_
Research/00_Extraction_Checklist.md`) and now covered: Guyton & Hall's *Textbook of Medical Physiology*,
several Biophysics/Biological Thermodynamics titles, `Computational-Biology.pdf`, molecular biology
primers — all cataloged in the `STEM/Biology/ top-level files` writeup below.

### Genetics/DNA [Genetic] Computing/ (12 files) — direct continuation of Vostok's DNA-computing grounding

- **A Biologist's Guide to Analysis of DNA Microarray Data** — Steen Knudsen (2002) — re-cataloged
  2026-07-23 via `djvutxt`. 1 Introduction (Hybridization, Affymetrix GeneChip Technology, Spotted Arrays,
  Serial Analysis of Gene Expression, Affymetrix vs. Spotted Arrays comparison); 2 Overview of Data
  Analysis; 3 Basic Data Analysis (Absolute Measurements, Scaling, Detection of Outliers, Fold Change) —
  continues beyond what was captured.
- **Advances of DNA Computing in Cryptography** — ed. Namasudra & Deka (2019). Intro of DNA computing in
  cryptography, public-key DNA cryptography, DNA-based security taxonomy, novel encryption schemes, cloud
  applications, security attacks, DNA computing algorithms.
- **Analytic Pattern Matching: From DNA to Twitter** — Jacquet & Szpankowski (2015). Probabilistic models,
  exact/constrained/generalized/subsequence string matching; digital trees, suffix trees, Lempel-Ziv
  compression.
- **Computing with Cells and Atoms: An Introduction to Quantum, DNA and Membrane Computing** — Calude &
  Păun (2000/2001). DNA computing (Adleman's Experiment, sticker systems, H systems), membrane computing
  (P systems), quantum computing (qubits, no-cloning theorem, quantum cryptography).
- **DNA Computing Models** — Ignatova, Martínez-Pérez, Zimmermann (2008). Theoretical CS + molecular
  biology background; word design; non-autonomous models (Adleman, filtering, sticker, splicing systems);
  autonomous models (algorithmic self-assembly, finite-state automaton, hairpin models); cellular DNA
  computing (ciliate computing).
- **DNA Computing: New Computing Paradigms** — Păun, Rozenberg, Salomaa (1998) — already the core Vostok
  source, see `Vostok_Genetics_Research/02_DNA_Computing.md`.
- **DNA Microarray Technology and Data Analysis in Cancer Research** — Li & Li (2009). Microarray tech,
  cancer applications, analytical methods incl. a novel SDL global optimization method.
- **DNA Microarray Data Analysis** — Tuimala & Laine, eds. (2003). Affymetrix/genotyping systems,
  experimental design, preprocessing/normalization, differential expression, cluster analysis, gene
  regulatory networks, promoter data mining.
- **DNA Microarrays and Gene Expression** — Baldi & Hatfield (2002). History of genomics, array
  formats/readout, statistical analysis (inference, dimensionality reduction, clustering), systems biology.
- **Natural Computing: DNA, Quantum Bits, and the Future of Smart Machines** — Shasha & Lazere (2010). A
  biographical-profile book on adaptive computing, DNA/"lifestuff" computing (incl. Ned Seeman, Paul
  Rothemund's DNA origami), and physics/speed computing scientists.
- **Statistical DNA Forensics** — Fung & Hu (2008). Probability/statistics, population genetics, parentage/
  kinship testing, mixture interpretation, lineage markers, mass-disaster identification.
- **Theoretical and Experimental DNA Computation** — Martyn Amos (2005). DNA as molecule of life, TCS
  primer, models of molecular computation, complexity issues, physical implementations (incl. Adleman's
  own implementation, DNA chess), cellular computing.

### Genetics/docs/ (2 files) — primary-source journal articles, directly complementary to the DNA Computing book

- **"Computing with DNA"** — Leonard M. Adleman, *Scientific American*, August 1998. Adleman's own
  first-person account of his 1994 experiment: the toolset (Watson-Crick pairing, polymerases, ligases,
  gel electrophoresis), the Hamiltonian Path Problem worked example, "Seven Days in a Lab," future outlook.
- **"Computing with DNA"** (Vicki Brower) + **"Back to the Roots"** (Jack Parker) — *EMBO Reports*, Vol.
  4 No. 1, 2003. Short analysis pieces: Adleman's experiment, Ehud Shapiro's programmable molecular Turing
  Machine, Eric Winfree's molecular tiles; a separate unrelated sidebar on GM-crop breeding.

### Genetics/recombination/ (4 files)

- **DNA Replication, Recombination, and Repair: Molecular Mechanisms and Pathology** — ed. Hanaoka &
  Sugasawa (2016). 21 chapters, 7 parts: DNA Replication, DNA Recombination, DNA Repair, Genome
  Instability/Mutagenesis, Chromosome Dynamics/Functions, Cell Cycle/Checkpoints, Interplay with
  Transcription/Epigenetic Regulation (incl. active DNA demethylation in cancer).
- **Molecular Biotechnology: Principles and Applications of Recombinant DNA**, 4th Ed — Glick, Pasternak,
  Patten (2009). Part I Fundamentals (development of the field, DNA/RNA/protein synthesis, recombinant DNA
  technology, PCR, bioinformatics/genomics/proteomics, gene expression manipulation, directed mutagenesis);
  Part II Microbial Systems (molecular diagnostics, protein therapeutics, nucleic acids as therapeutics,
  vaccines).
- **Recombinant DNA**, 2nd Ed — Watson, Gilman, Witkowski, Zoller (Scientific American Books, 1992). 25
  chapters: Development of Recombinant DNA Technology; DNA as Primary Genetic Material; Elucidation of the
  Genetic Code; Genetic Elements Controlling Gene Expression; Methods of Creating Recombinant DNA
  Molecules; The Polymerase Chain Reaction; Isolation of Cloned Genes; Complexity of the Genome;
  Controlling Eukaryotic Gene Expression; Movable Genes; In Vitro Mutagenesis; Transferring Genes into
  Mammalian Cells; Using Yeast to Study Eukaryotic Gene Function; Introduction of Foreign Genes into Mice;
  Genetic Engineering of Plants; Molecules of Immune Recognition; Moving Signals Across Membranes;
  Oncogenes and Anti-Oncogenes; Molecular Analysis of the Cell Cycle; Genes That Control the Development of
  Drosophila; The Genes Behind the Functioning of the Brain; Recombinant DNA and Evolution; Recombinant DNA
  in Medicine and Industry; Generation of Agriculturally Important Plants and Animals; Marshaling
  Recombinant DNA to Fight AIDS. (A `.djvu` duplicate copy of the same edition exists in the folder,
  unreadable with current tooling.)

### Genetics/synthetics/ (4 files)

- **DNA and RNA Modification Enzymes: Structure, Mechanism, Function, and Evolution** — ed. Henri Grosjean
  (2009). 16 chapters incl.: noncanonical nucleosides across the three domains of life; DNA methylation
  ("bug to beast"); restriction-modification systems; base-flipping (experimental + computational); DNA
  methyltransferase mechanisms/structures; DNA methylation and human disease/aging; antibody maturation via
  DNA uracils; the hypermodified DNA base J; active DNA demethylation (animals/plants); AlkB
  demethylation; APOBEC/ADAR cytidine and adenosine deaminases.
- **Gene Cloning and DNA Analysis: An Introduction**, 7th Ed — T.A. Brown (2016). Part I Basic Principles
  (vectors, DNA purification/manipulation, restriction enzymes, cloning vectors for *E. coli* and
  eukaryotes, obtaining a gene clone, PCR); Part II Applications in Research (sequencing genomes, gene
  expression/function, studying genomes); Part III Applications in Biotechnology (protein production,
  medicine, agriculture, forensic science/archaeology).
- **Molecular Themes in DNA Replication** — ed. Lynne S. Cox (2009). Conserved steps in eukaryotic DNA
  replication, AAA+ ATPases in loading replication factors, ring structures/six-fold symmetry (MCM
  helicases, PCNA sliding clamp), mechanisms for high-fidelity replication; explicitly flags mitochondrial
  genome replication, malaria-parasite replication targets, and cancer/ageing therapeutic angles.
- **Synthetic DNA: Methods and Protocols** — ed. Randall A. Hughes (2016). Part I computational design
  tools (STITCHER, codon optimization, DNA shuffling); Part II synthesis/assembly/cloning (overlap PCR,
  SpeedyGenes, BASIC modular assembly, ligase cycling reaction, PaperClip, Clonetegration, GoldenGATEway);
  Part III post-synthesis error-reduction strategies. Traces synthetic-DNA history from 1970s abiotic
  synthesis through the first functional synthetic DNA sequence (a 207bp tRNA) to modern engineered
  biological systems.

### Genetics/forensics/ (9 files)

- **Advanced Topics in Forensic DNA Typing: Methodology** — John M. Butler (2011, NIST). 18 chapters:
  sample collection/storage, DNA extraction/quantitation/PCR amplification, STR loci and kits, capillary
  electrophoresis, QA/validation, DNA databases, missing persons/disaster victim ID, degraded DNA,
  low-level DNA testing, SNPs, Y-chromosome/mitochondrial/X-chromosome/non-human DNA, new technologies,
  legal aspects and expert testimony. Appendices incl. familial DNA search privacy concerns.
- **A Guide to Forensic DNA Profiling** — eds. Jamieson & Bader (2016). 44 chapters in 4 parts: Background
  (intro to forensic genetics, DNA overview, electropherogram, biological stains, identification/
  individualization, transfer, lab accreditation, validation); Analysis & Interpretation (extraction,
  quantitation, amplification, mixture interpretation, degraded samples, ceiling principle, Y-STRs, expert
  systems, paternity testing, observer effects); Applications (databases, missing persons, familial
  searching, SNPs, mini-STRs, phenotype prediction, mtDNA, geographical ID by viral genotyping, microbial
  forensics, wildlife crime); Court (database controversy, evidentiary issues, communicating probabilistic
  evidence, report writing, expert examination/cross-examination, legal issues UK/USA, future
  technologies).
- **An Introduction to Forensic DNA Analysis**, 2nd Ed — Rudin & Inman (2001). Nature of physical evidence
  (fingerprints/DNA/blood typing), collection/preservation, short history of DNA typing, scientific basis
  (population genetics, molecular biology), overview of typing systems (RFLP, PCR-based incl. STRs/
  Y-STRs/mtDNA), lab procedures (extraction, automated systems), interpretation (mixtures, degradation,
  extraneous substances). Opens with a Sherlock Holmes epigraph; dedicated in part to 9/11 identification
  efforts.
- **Forensic Analysis of Biological Evidence: A Laboratory Guide for Serological and DNA Typing** — J.
  Thomas McClintock (2014). A hands-on lab-exercise manual: overview of forensic DNA analysis, biological
  sample types, alternate light source examination, forensic serology (saliva/blood/semen/urine
  presumptive tests), DNA extraction methods (Chelex, organic, salting-out, differential, kits), DNA
  concentration/purification, quality/quantity assessment, PCR, STR analysis, paternity case study.
- **Forensic DNA Biology: A Laboratory Manual** — Kelly M. Elkins (2013). 22 lab-exercise chapters:
  pipetting, serology, sampling, extraction, quality/quantity determination (gel, UV-Vis, fluorescence),
  real-time PCR, multiplex PCR primer design, capillary electrophoresis, random match probability
  computation, mtDNA SNP detection, BioEdit sequence analysis, RNA extraction, Y-STR typing, paternity/
  missing persons statistics, low copy number results, botanical DNA extraction, social/ethical/regulatory
  concerns, case studies.
- **Forensic DNA Evidence Interpretation**, 2nd Ed — eds. Buckleton, Bright, Taylor (2016). Biological
  basis for DNA evidence, framework for interpreting evidence, population genetic models, relatedness,
  validating databases, sampling effects, single-source/complex profiles, the continuous model,
  non-autosomal markers, parentage testing, disaster victim ID/missing persons/immigration cases, DNA
  intelligence databases.
- **Forensic DNA Typing: Biology, Technology, and Genetics of STR Markers**, 2nd Ed — John M. Butler
  (2005). 24 chapters across Biology/Technology/Genetics sections: DNA typing history, STR markers/kits,
  degraded DNA/PCR inhibition/mixtures/low copy number, SNPs, Y-chromosome/mtDNA/non-human DNA, separation
  methods, laboratory validation, CODIS, statistics/probability, profile frequency estimates, kinship/
  parentage testing, mass disaster DNA victim identification.
- **Forensic DNA Typing Protocols**, 2nd Ed — ed. William Goodwin (2016). Sample collection, RNA-based
  body-fluid identification (distinguishing menstrual/circulatory blood), DNA extraction from muscle
  tissue/skeletal remains, internal amplification controls, PCR product purification, INDEL marker
  analysis, mitochondrial control-region and whole-genome sequencing, rapidly mutating Y-STRs, HIrisPlex
  eye/hair-color-from-DNA prediction system, autosomal ancestry-informative marker sets (twice, theory +
  analysis), species determination via cytochrome b gene.
- **Fundamentals of Forensic DNA Typing** — John M. Butler (2009, NIST) — companion volume to *Advanced
  Topics* above. 18 chapters: overview/history, DNA biology/genetics basics, historical methods, sample
  collection, extraction, quantitation, PCR amplification, STR markers, separation/detection, genotyping/
  data interpretation, statistical interpretation, DNA databases, quality assurance, degraded DNA/
  mixtures/LCN, additional loci/non-human DNA, Y-chromosome/mtDNA lineage markers, applications, future
  trends.

### Genetics/identification/ (5 files)

- **Bioinformatics for DNA Sequence Analysis** — ed. David Posada (2009, Methods in Molecular Biology
  537). 17 chapters, tool-oriented: BLAST similarity searching, OrthologID gene orthology, MAFFT multiple
  alignment, SeqVis compositional heterogeneity, jModelTest model selection, PhyML maximum-likelihood
  phylogenies, Clann phylogenetic supertrees, Datamonkey selection detection, RDP3 recombination analysis,
  CodonExplorer codon usage, GenDecoder genetic code prediction, GeneID gene annotation, A-GLAM regulatory
  motifs, UCSC Genome Browser, SNP/SSR mining (SNPServer, dbSNP), CENSOR/RepeatMasker transposable
  elements, DnaSP sequence polymorphism analysis.
- **Cell-free DNA as Diagnostic Markers: Methods and Protocols** — eds. Casadio & Salvi (2019). Overview
  of cfDNA applications/isolation; liquid biopsy for cancer (ctDNA vs. CTC markers); cfDNA integrity, copy
  number variation, dPCR mutational analysis; epigenetic characterization/methylation-specific PCR; fetal
  and pediatric disease applications (rhabdomyosarcoma, maternal-plasma fetal-fraction quantification);
  cfDNA in physical activity monitoring; urinary cell-free DNA.
- **DNA Barcoding and Molecular Phylogeny** — eds. Trivedi, Rehman, Saggu, Panneerselvam, Ghosh (2018). 5
  parts: Advantages/Significance (biodiversity assessment, invasive-species ID); Barcoding of Microbes;
  Barcoding in Plants (forensic botany, red algae, aquatic biodiversity); Barcoding in Animals (mosquitoes,
  rays, elasmobranchs, fish taxonomy/fisheries, reptile conservation, avian species, ruminant mammals);
  Case Studies (marine actinobacteria, tropical river fish, climbing perch genetic variation, Saudi
  reptiles, sea buckthorn).
- **DNA Fingerprinting in Plants: Principles, Methods, and Applications**, 2nd Ed — Weising, Nybom, Wolff,
  Kahl (2005). A full rewrite of the 1994 first edition (which covered plants *and fungi*) given a decade
  of explosive growth in the field; documents the shift from hybridization-based to PCR-based methods
  (RAPDs/RFLPs superseded by microsatellites/AFLPs, with SNPs and DNA microarrays as the then-emerging
  frontier). 1600+ references.
- **Truth Machine: The Contentious History of DNA Fingerprinting** — Lynch, Cole, McNally, Jordan (2008).
  A science-and-technology-studies history, not a lab manual. 10 chapters + 5 "Interludes": forensic
  science as a "revolution," DNA profiling techniques, techno-legal controversy, admissibility/judicial
  metascience, molecular biology and technique dispersion, chains of custody/administrative objectivity,
  the UK National DNA Database, probability deconstruction in *R. v. Deen*, Bayesian/frequentist database-
  search controversy, "fixing controversy, performing closure," postclosure, fingerprinting as "an
  inversion of credibility." Opens with a *CSI: Crime Scene Investigation* epigraph (Gil Grissom's "the
  evidence doesn't lie") as a foil for the book's actual thesis — that DNA evidence's credibility was
  painstakingly, contentiously constructed, not simply self-evident from the science. Genuinely rich
  narrative material on the social/legal construction of forensic authority, a different register from the
  purely technical forensics-lab manuals cataloged above.

### Genetics/shit for later/ (7 files, developer's own folder name)

- **Ancestral DNA, Human Origins, and Migrations** — René J. Herrera & Ralph Garcia-Bertrand (2018) —
  re-cataloged 2026-07-23. 14 chapters tracing specific human migrations: The Nature of Evolution; Early
  Hominins; Origin of Modern Humans; The Exodus Out of Africa; The Settlement of the Near East;
  Neanderthals, Denisovans, and Hobbits; Dispersals into India; The Occupation of South East Asia,
  Indonesia, and Australia; The Austronesian Expansion; From Africa to the Americas; The Bantu Expansion;
  Modern Humans in Europe; The Agricultural Revolutions; The Silk Roads.
- **Elizabeth Blackburn and the Story of Telomeres: Deciphering the Ends of DNA** — Catherine Brady (2007,
  MIT Press). A scientific biography, 13 chapters (A Certain Sense of Self; Shedding Encumbrances; One of
  Gall's Gals; Revelations; Opportunism; Gold Rush; Entering the Fray; An Interlocking System; Dr. Jekyll
  or Mr. Hyde?; Members of a Guild; Citizen Scientist; Political Fallout; "You Have to Think It's Fun"),
  tracing Blackburn's telomere/telomerase discoveries (later 2009 Nobel Prize) through interviews with her
  and many collaborators (Gall, Greider, de Lange, Shampay, etc.).
- **From DNA to Diversity: Molecular Genetics and the Evolution of Animal Design**, 2nd Ed — Carroll,
  Grenier, Weatherbee (2005). The foundational "evo-devo" textbook. 8 chapters: A Brief History of Animals;
  The Genetic Toolkit for Development; Building Animals (gene regulation, insect/vertebrate body plans);
  Evolution of the Toolkit (Hox complex case study); Diversification of Body Plans and Body Parts; The
  Evolution of Morphological Novelties; Morphological Variation and Species Divergence (incl. stickleback
  skeletal evolution); From DNA to Diversity: The Primacy of Regulatory Evolution.
- **Genetics: A Conceptual Approach**, 6th Ed — Benjamin A. Pierce (2016) — re-cataloged 2026-07-23. A
  standard genetics textbook; confirmed Chapter 2 "Chromosomes and Cellular Reproduction" (sister chromatid
  and homologous chromosome separation) and extensive coverage of eukaryotic chromosome structure
  (centromeres, telomeres, replication at chromosome ends) and gene-mapping fundamentals throughout — full
  chapter-by-chapter TOC not extracted given the title's already-standard, widely-documented structure.
- **The Language of Life: DNA and the Revolution in Personalized Medicine** — Francis S. Collins (2010,
  then-NIH Director, former Human Genome Project leader). Introduction "We're Not in Kansas Anymore" opens
  with a real, vivid BRCA1/Charcot-Marie-Tooth family-testing narrative (the author's own family). 10
  chapters + 5 appendices: The Future Has Already Happened; When Genes Go Wrong, It Gets Personal; Is It
  Time to Learn Your Own Secrets?; Getting Personal with the Big C; What's Race Got to Do with It?; Genes
  and Germs; Genes and the Brain; Genes and Aging; The Right Drug at the Right Dose for the Right Person; A
  Vision for the Future. Appendices incl. "Genetics 101" and a personal history of the Human Genome
  Project.
- **The Making of the Fittest: DNA and the Ultimate Forensic Record of Evolution** — Sean B. Carroll
  (2006/2007, follow-up to *Endless Forms Most Beautiful*). Preface "Beyond Any Reasonable Doubt" frames
  DNA explicitly as forensic evidence for evolution. 10 chapters: Introduction (The Bloodless Fish of
  Bouvet Island); The Everyday Math of Evolution; Immortal Genes: Running in Place for Eons; Making the New
  from the Old; Fossil Genes; Déjà Vu: How and Why Evolution Repeats Itself; Our Flesh and Blood: Arms
  Races, the Human Race, and Natural Selection; The Making and Evolution of Complexity; Seeing and
  Believing; The Palm Trees of Wyoming. Opens Chapter/framing material with an actual forensic DNA gel-
  match photograph (crime-lab suspect identification) as its explicit rhetorical device.
- **The Molecules of Life: DNA, RNA, and Proteins** (Genetics & Evolution series) — Russ Hodge (2009,
  Facts On File), foreword Nadia Rosenthal. 5 chapters: The Physics and Chemistry of Life; How the Cell
  Stores and Uses Information (incl. a dedicated "DNA Computers" sidebar, p.72 — direct further
  cross-reference to Vostok's DNA-computing thread); Communication Between and Inside Cells; Traffic and
  Cell Architecture; Molecules of Immunity, Health, and Disease (incl. prions/Mad Cow Disease, "Can Cancer
  Be a Transmissible Disease?").

### Genetics/Bioinformatics/ (19 files — largest single subfolder)

*One file (`Bioinformatics for DNA sequence analysis`, Menlove/Clement/Crandall/Posada) is a duplicate
already cataloged under `Genetics/identification/` above — not re-listed here.*

- **Bioinformatics Algorithms Techniques and Applications** — eds. Mandoiu & Zelikovsky (2008). Genomics/
  proteomics algorithms anthology (part of a Chapman & Hall/CRC computer-science series).
- **Bioinformatics and Functional Genomics**, 3rd Ed — Jonathan Pevsner (2015). A major standard textbook;
  broad DNA/RNA/protein sequence, genomics, and functional-genomics coverage.
- **Bioinformatics** — Polanski & Kimmel (2007). General computational-biology textbook.
- **Bioinformatics: An Introduction**, 3rd Ed — Jeremy Ramsden (2015). General introductory text.
- **Bioinformatics: A Practical Guide to the Analysis of Genes and Proteins**, 2nd Ed — Baxevanis &
  Ouellette (2001). Classic practical-methods reference.
- **Bioinformatics Computing** — Bryan Bergeron (2003). Preface frames the book explicitly as "how
  information is represented and transmitted in biological systems" for computer-literate molecular
  biologists with little CS background — practical guide to sorting/searching algorithms (quicksort vs.
  bubblesort), machine learning, and distributed computing as applied to real biotech problems (Human
  Genome Project scale). Directly continues this collection's "silicon/carbon," DNA-as-information thread.
- **Bioinformatics: Concepts, Methodologies, Tools, and Applications** (3 vols) — ed. IRMA/Information
  Resources Management Association (2013). Massive multi-author reference anthology (1700+ pages),
  dozens of international contributors.
- **Bioinformatics for Beginners: Genes, Genomes, Molecular Evolution, Databases and Analytical Tools** —
  Supratim Choudhuri, with Michael Kotewicz on DNA optical mapping (2014). Ch.1 "Fundamentals of Genes and
  Genomes" covers DNA double helix, base-pairing rules, gene structure, epigenetic modification of the
  genome, ENCODE project findings.
- **Bioinformatics for Biologists** — eds. Pavel Pevzner & Ron Shamir (2011, Cambridge). 5 parts across 16
  chapters: Genomes (disease genetics, haplotype patterns, genome reconstruction "a puzzle with a billion
  pieces," dynamic programming, paternity/kinship "measuring evidence"); Gene Transcription and Regulation
  (replication/transcription, regulatory motifs, influenza species-jump prediction); Evolution (genome
  rearrangements, phylogenetic tree comparison — "Forest of Life," large-scale genomic-change
  reconstruction); Phylogeny (fig/wasp/gopher/louse coevolution, big-cat phylogenies, optimization
  heuristics); Regulatory Networks (biological networks, network inference).
- **Bioinformatics for Geneticists: A Bioinformatics Primer for the Analysis of Genetic Data**, 2nd Ed —
  ed. Michael R. Barnes (2007). 3 sections: Introduction (bioinformatics challenges, managing/manipulating
  genetic data); Mastering Genes/Genomes/Genetic Variation (HapMap, genome assembly, gene finding,
  comparative genomics); Bioinformatics for Genetic Study Design and Analysis (mutation ID in monogenic
  disease, genome-scan-to-culprit-gene, integrating genetics/genomics/epigenomics, statistical genetics
  tools).
- **Bioinformatics Programming Using Python: Practical Programming for Biological Data** — Mitchell L.
  Model (2009, O'Reilly). Programming-fundamentals-through-bioinformatics-applications textbook (Python
  3); notably includes a full chapter (Ch.8, "Structured Text") on **parsing an XML file for a complete
  genome** as a worked example.
- **Bioinformatics: The Machine Learning Approach**, 2nd Ed — Pierre Baldi & Søren Brunak (2001, MIT
  Press, "Adaptive Computation and Machine Learning" series' founding volume). A rigorous, foundational
  text: Bayesian probabilistic framework, neural networks (theory + protein secondary structure/DNA/RNA
  applications), Hidden Markov Models (protein/DNA/RNA applications), probabilistic graphical models,
  phylogenetic trees, **stochastic grammars and linguistics** (Ch.11 — formal grammars, the Chomsky
  hierarchy, and their application to biological sequences, a direct further cross-reference to the
  DNA-language thread already opened by Brazma's *Living Computers*), microarrays/gene expression.
- **Computing Skills for Biologists: A Toolbox** — Allesina & Wilmes (2019, Princeton). Opens with a
  Donald Knuth epigraph ("Science is what we understand well enough to explain to a computer. Art is
  everything else we do.") and is dedicated "to all biologists who think they can't code." 11 chapters:
  Unix, Version Control, Basic Programming, Writing Good Code, Regular Expressions, Scientific Computing,
  Scientific Typesetting, Statistical Computing, Data Wrangling and Visualization, Relational Databases,
  Wrapping Up.
- **Bioinformatics** (2 volumes) — ed. Jonathan M. Keith (2nd Ed, 2017, Humana Press/Springer, *Methods in
  Molecular Biology* series). **Vol. I: Data, Sequence Analysis, and Evolution** — Part I Data and
  Databases (genome sequencing, sequence assembly, protein crystallography, managing sequence data, genome
  annotation, working with ontologies, protein-domain classification); Part II Sequence Analysis (multiple
  sequence alignment, large-scale sequence comparison, genomic database searching, finding genes in genome
  sequence, sequence segmentation); Part III Phylogenetics and Evolution (measuring natural selection,
  inferring trees, identifying optimal evolution models, lateral gene transfer detection, genetic
  recombination analysis, species tree estimation). **Vol. II: Structure, Function, and Applications** —
  Part I Structure/Function/Pathways/Networks (3D protein modeling, inferring function from homology/gene
  order, noncoding RNA annotation, functional gene networks, genome-wide interaction networks, cancer
  module identification, metabolic pathway mining); Part II Applications (GWAS analysis, computational
  diagnosis, drug discovery, antibody repertoire sequencing, breast-cancer diagnosis); Part III
  Computational Methods (cell-signaling-pathway modeling, clustering, parameterized algorithmics for
  NP-hard biological problems, information visualization).
- **Integrative Cluster Analysis in Bioinformatics** — Abu-Jamous, Fa, Nandi (2015, Wiley). 6 parts, 24
  chapters: Introduction; Molecular Biology (living cell, central dogma); Data Acquisition/Pre-processing
  (high-throughput tech, databases, normalization, feature selection, differential expression); Clustering
  Methods (partitional, hierarchical, fuzzy, neural-network-based, mixture-model, graph, consensus,
  biclustering); Validation and Visualization; **New Clustering Frameworks Designed for Bioinformatics**
  (the authors' own original contributions: "Splitting-Merging Awareness Tactics" and "Tightness-tunable
  Clustering").
- **Intelligent Bioinformatics: The Application of Artificial Intelligence Techniques to Bioinformatics
  Problems** — Keedwell & Narayanan (2005, Wiley). 3 parts: Introduction (molecular biology basics,
  bioinformatics problems/challenges, AI/CS fundamentals); Current Techniques (probabilistic approaches,
  nearest-neighbor/clustering, decision trees, neural networks, **genetic algorithms**); Future Techniques
  (genetic programming, cellular automata, hybrid methods).
- **Machine Learning in Bioinformatics** — eds. Yan-Qing Zhang & Jagath C. Rajapakse (2009, Wiley Series
  in Bioinformatics). 20-chapter multi-author anthology: feature selection for genomic/proteomic data
  mining, gene selection/classification methods, kernel classifiers, fuzzy gene mining for cancer
  microarrays, protein structure prediction (consensus + kernel methods), promoter recognition/detection,
  microRNA supervised learning, computational haplotype analysis, SNP-disease association machine
  learning, nanopore cheminformatics, biomedical information fusion.
- **Introduction to Bioinformatics**, 4th Ed — Arthur M. Lesk (2014, Oxford). Opens with an *Antony and
  Cleopatra* epigraph ("In nature's infinite book of secrecy / A little I can read.") A major standard
  text: genome organization/evolution, scientific publication/archive systems, database
  architecture/access (ENTREZ, PIR, ExPASy), sequence/structure databases, alignment, protein structure
  prediction, systems biology, clinical implications. Same "genotype = phenotype − environment − life
  history − epigenetics" framing found across this collection's more conceptual texts.
- **Introduction to Bioinformatics** — Attwood & Parry-Smith (1999, Pearson/Addison Wesley Longman, "Cell
  and Molecular Biology in Action" series). An early, foundational textbook (predates the human genome's
  completion) explicitly framed around a hands-on Web-based practical exercise (identifying an "unknown"
  DNA fragment): Introduction (dawn of sequencing, biological sequence/structure deficit, homology vs.
  analogy), Information Networks (early Internet/WWW/EMBnet/NCBI orientation for biologists), Protein/
  Genome Information Resources, DNA Sequence Analysis (ESTs), Pairwise/Multiple Alignment, Secondary
  Database Searching, Building a Sequence Search Protocol, Analysis Packages. Preface delivers a
  notably blunt, still-relevant methodological warning: "don't always believe what databases/programs/
  Web servers tell you... think, question, and, above all, be critical of the information you gather."

### Genetics/ top-level files (18 files)

- **Advanced Topics in Forensic DNA Typing: Interpretation** — John M. Butler (2015, NIST), foreword Peter
  Gill. Third edition, third volume of the *Forensic DNA Typing* series (companion to *Fundamentals* and
  *Advanced Topics: Methodology*). 16 chapters across two parts: data interpretation (heterozygote balance,
  stutter, allele drop-out, stochastic thresholds, mixture interpretation, complex/low-template profiles)
  and statistical interpretation/reporting (probability theory, population genetics, mixture statistics,
  relationship/kinship testing, Y/X-chromosomal/mitochondrial lineage markers, laboratory report writing).
- **A Handbook for DNA-Encoded Chemistry: Theory and Applications for Exploring Chemical Space and Drug
  Discovery** — ed. Robert A. Goodnow Jr. (2014, Wiley). 19 chapters: combinatorial-chemistry history and
  the emergence of DNA-encoded chemistry, DNA-compatible chemistry, DNA-encoded library (DEL) foundations
  and synthesis exercises, the "DNA tag" as a chemical gene, analytical challenges, informatics for DEL
  production/screening, theoretical drug-discovery applications, hit-to-lead process, combinatorial-library
  visualization, screening large compound collections, dual-pharmacophore DELs, using DNA to program
  chemical synthesis/discover reactions/detect ligand binding, economics and outlook of DEL technology.
- **Data Mining for Bioinformatics** — Sumeet Dua & Pradeep Chowriappa (2012, CRC Press/Auerbach). Section
  I: Introduction to Bioinformatics (transcription/translation, Human Genome Project, sequencing
  technologies, functional/comparative genomics); biological databases and integration (GEO, PDB, data
  cleaning/integration); knowledge discovery in databases. Section II: feature selection/extraction
  strategies, feature interpretation for biological learning (gene expression normalization, mass
  spectrometry preprocessing). Continues through classification/clustering methods for bioinformatics data
  (not read in this pass).
- **DNA and Biotechnology**, 3rd Ed — Molly Fitzgerald-Hayes & Frieda Reichsman (2010, Academic Press). 16
  chapters: Roots of DNA Research, DNA Double Helix, DNA in Action, Tools of the DNA Trade, Working with
  DNA, Human Genomics, Bioinformatics, DNA Forensics, Exploring Cell Fate, Human Genetic Diseases, Gene
  Therapy, Stem Cell Research, Pharmaceutical Biotechnology, Animal Biotechnology, Agricultural
  Biotechnology, Genes and Race. A university-level textbook (UMass Amherst BMB program), aimed at making
  genomics/biotech genuinely accessible to non-specialists.
- **DNA and Your Body: What You Need to Know About Biotechnology** — Colin Masters (2005, UNSW Press). 11
  chapters: DNA/Growth/Differentiation, DNA and Disease, the Human Genome Project, DNA and Cloning
  (incl. Dolly), Genetic Engineering, Tissue Engineering (stem cells), DNA and the Adult Human Body, DNA
  and Ageing (oxygen free radicals, peroxisomes), Aberrant Development (incl. cancer), DNA and Proteomics,
  DNA and the Future (Junk DNA, bioinformatics, ethical issues).
- **DNA Beyond Genes: From Data Storage and Computing to Nanobots, Nanomedicine, and Nanoelectronics** —
  Vadim V. Demidov (2020, Springer). Explicitly a continuation of exactly this collection's "uncommon DNA"
  thread: DNA electronics, structural DNA nanotechnology, DNA computing, DNA data storage, DNA machines.
  Preface opens with the same Francis Crick "dat's the gene" anecdote and cites a 93%-of-people-know-DNA
  public-awareness statistic. Cover art depicts DNA-assisted fabrication of nanometer-scale electronic
  circuits. Epigraphs include Nadrian Seeman's "the exploitation of DNA for material purposes presents a
  new chapter in the history of the molecule" — a strong direct continuation of the DNA-computing/
  DNA-as-material thread already central to Vostok's grounding.
- **DNA Fingerprinting: An Introduction** (Breakthroughs in Molecular Biology series, vol. 2) — Lorne T.
  Kirby (1993, Oxford). 6 chapters: Introduction (definition, history, "a case for DNA," applications),
  Genetic Principles (DNA structure, reproduction, linkage, mutation, restriction endonucleases,
  recombinant DNA, repetitive sequence organization), Laboratory Organization, Specimens (collection,
  extraction methods), DNA Amplification (PCR), Analysis Techniques (restriction cleavage, gel-blot,
  electrophoresis, hybridization).
- **DNA Sequencing: From Experimental Methods to Bioinformatics** (Introduction to Biotechniques series) —
  Luke Alphey (1997, BIOS Scientific). Part 1: Basic Principles/Methods (chemical degradation/Maxam-Gilbert,
  chain-termination/Sanger-dideoxy, instrumentation, template preparation, gel electrophoresis,
  nonradioactive/semi-automated methods, troubleshooting); Part 2: Applications (confirmatory sequencing,
  sequencing PCR products, strategies for new sequence determination incl. primer walking and "shotgun"
  methods); Part 3: Sequence Analysis (bioinformatics/Internet basics, sequence databases, alignment and
  database searches, sequencing-project contig analysis, protein-function prediction) — contributed by A.
  Brass. A genuinely early (pre-Human-Genome-Project-completion) snapshot of the field.
- **DNA Vaccines: Methods and Protocols**, 2nd Ed — eds. W. Mark Saltzman, Hong Shen, Janet L. Brandsma
  (2006, Humana Press/Methods in Molecular Medicine). 5 parts: DNA Vaccine Design (incl. mRNA vaccination —
  a direct real-world precedent for what became the COVID-era mRNA vaccine platform, notable as a 2006
  publication); DNA Vaccine Delivery Systems (electroporation, needle-free injection, biodegradable
  microspheres, viral/nonviral hybrid vectors); Adjuvants; Applications (allergy, autoimmunity, neonatal/
  infant responses); Production and Quality Assurance. Preface traces DNA vaccination from Edward Jenner's
  smallpox vaccine (~200 years earlier) through early-1990s plasmid-DNA immunization breakthroughs to
  then-active Phase I/II human trials (HIV, malaria, HPV, hepatitis B, melanoma).
- **Fluorescence Spectroscopy in Biology, Vol. 3: Advanced Methods and Their Applications to Membranes,
  Proteins, DNA, and Cells** (Springer Series on Fluorescence) — eds. Martin Hof, Rudi Hutterer, Vlastimil
  Fidler (2005). Proceedings-style volume from the 8th Conference on Methods and Applications of
  Fluorescence (Prague, 2003). Part 1: Basics/Advanced Approaches (pulse vs. phase fluorometry,
  fluorescence nanotomography, solvent relaxation for micro-polarity/fluidity probing — incl. a dedicated
  "SR in DNA" section, total internal reflection fluorescence microscopy). Continues into membrane and
  protein/nucleic-acid fluorescence applications (not read in this pass).
- **Forensic DNA Evidence Interpretation** — eds. John S. Buckleton, Christopher M. Triggs, Simon J. Walsh
  (2004, CRC Press) — an earlier (1st edition, New Zealand/Australia-authored) companion to the 2nd
  edition already cataloged in `Genetics/forensics/`. 9 chapters: Biological Basis for DNA Evidence, A
  Framework for Interpreting Evidence, Population Genetic Models, Relatedness, Validating Databases,
  Sampling Effects, Mixtures, Low Copy Number, Nonautosomal Forensic Markers. Preface explicitly credits
  Bruce Weir and Ian Evett as having "set the standard for forensic thinking and testimony" and frames the
  book as "Evett and Weir compatible."
- **From Genes to Genomes: Concepts and Applications of DNA Technology**, 2nd Ed — Jeremy W. Dale &
  Malcolm von Schantz (2007, Wiley) — an earlier edition of the same title already cataloged (3rd Ed,
  T.A. Brown joining as co-author) in `Genetics/synthetics/`. 15 chapters: Basic Molecular Biology, How to
  Clone a Gene, Cutting/Joining DNA, Vectors, Genomic/cDNA Libraries, Finding the Right Clone, PCR,
  Characterization of a Cloned Gene, Analysis of Gene Expression, Products from Native/Manipulated Cloned
  Genes, Genomic Analysis, Analysis of Genetic Variation, Post-Genomic Analysis, Modifying Organisms/
  Transgenics.
- **Methylation: From DNA, RNA and Histones to Diseases and Treatment** — ed. Anica Dricu (2012, InTech,
  open access). 5 sections, 11 chapters: Gene Expression and Methylation (transcription factors/DNA
  methylation interplay); DNA-Methyltransferases structure/function (eukaryotic/prokaryotic); Protein
  Arginine Methylation in Mammals; Cancer Research through Methylation (tumorigenesis, circulating
  methylated DNA as cancer biomarkers, DNA methylation/stem cells/cancer, head-and-neck cancer
  pathogenesis); Bacteria/Viruses/Metals Methylation (host-mimicking bacterial transformation strategies,
  mRNA cap methylation in vesicular stomatitis virus, methylation of metals/metalloids in aquatic systems).
- **Paleogenomics: Genome-Scale Analysis of Ancient DNA** (Population Genomics series) — eds. Charlotte
  Lindqvist & Om P. Rajora (2019, Springer). Part I: Concepts/Technical Advances/Challenges (genome-scale
  aDNA analysis, paleoproteomics via soft-ionisation mass spectrometry, Ancient RNA, Ancient Epigenomics);
  Part II: Case Studies (ancient human pathogens, paleovirology, reconstructing past vegetation from lake-
  sediment aDNA, archaeogenomics/crop adaptation, herbarium genomics, paleogenomics of animal domestication
  — dog/cat/horse chapters, primate paleogenomics, structural variants in ancient genomes, genomics of
  extinction). Directly, explicitly continues Vostok's own "ancient sealed genetic material revealing
  hidden truth once sequenced" premise — a real, current (2019) academic field built on exactly that
  premise, complementing the earlier-found Svante Pääbo Nobel Prize precedent.
- **Plant Biotechnology and Genetics: Principles, Techniques, and Applications** — ed. C. Neal Stewart Jr.
  (2008, Wiley). 9 chapters (of a longer TOC): Plant Agriculture/Impact of Biotechnology, Mendelian
  Genetics and Plant Reproduction, Plant Breeding, Plant Development and Physiology, Tissue Culture,
  Molecular Genetics of Gene Expression, Recombinant DNA/Vector Design, Genes and Traits of Interest for
  Transgenic Plants, Marker Genes and Promoters. A comprehensive plant-biotech textbook, potentially
  relevant to Davis's agricultural-research identity as well as Vostok's genetics identity.
- **RNA and DNA Diagnostics** (RNA Technologies series) — eds. Volker A. Erdmann, Stefan Jurga, Jan
  Barciszewski (2015, Springer). Contents: electrochemical biosensors for miRNA/RNA detection, DNA/PNA
  probes for DNA detection, DNA for non-nucleic-acid sensing, aptamers in oncotherapy, SNP genotyping,
  environmentally responsive fluorescent probes for DNA/RNA hybridization detection, fluorescent nucleic
  acid analogues in clinical diagnostics, nanoconfined nucleic acid architectures. Preface frames nucleic
  acids' Watson-Crick programmability as "the central feature of nucleic acid technologies" — same core
  framing as the DNA Computing collection.
- **RNA Bioinformatics** (Methods in Molecular Biology 1269) — ed. Ernesto Picardi (2015, Humana Press).
  Part I: RNA Secondary/Tertiary Structures (free-energy minimization, structure prediction from
  multi-aligned sequences, RNA-RNA interaction prediction); Part II: High-Throughput RNA Sequencing Data
  Analysis (quality control, mapping, transcriptome quantification/assembly, alternative splicing, RNA
  editing detection, miRNA target prediction, metatranscriptomic data); Part III: Web Resources (ViennaRNA,
  RNA-editing exploration tools, UTR annotation, Rfam, alternative-splicing databases, computational design
  of artificial RNA molecules for gene regulation).
- **The Chemical Biology of DNA Damage** — eds. Nicholas E. Geacintov & Suse Broyde (2010, Wiley-VCH). Part
  One: Chemistry and Biology of DNA Lesions — Introduction/Perspectives, Chemistry of Inflammation and DNA
  Damage (reactive nitrogen species), Oxidatively Generated Damage to Isolated/Cellular DNA, Role of Free
  Radical Reactions, DNA Damage from Endogenously Generated Oxidative-Stress Products, Polycyclic Aromatic
  Hydrocarbons (multiple metabolic pathways/DNA lesions), Aromatic Amines/Heterocyclic Aromatic Amines
  (tobacco smoke to food mutagens), Genotoxic Estrogen Pathway. Cover art depicts a benzo[a]pyrene-damaged
  DNA site modeled in a human DNA-bypass polymerase's active site.
- **The Initiation of DNA Replication in Eukaryotes** — ed. Daniel L. Kaplan (2016, Springer). 26 chapters,
  a comprehensive real research-field survey: origin choice/replication timing (incl. epigenetic vs.
  sequence-dependent control, chromatin determinants, fork-directionality gradients), the Origin
  Recognition Complex, licensing of replication origins, coordination with histone synthesis, CDK/DDK
  roles, the Cdc45-Mcm2-7-GINS ("CMG") replication helicase, DNA replication checkpoint signaling, and two
  genuinely narrative-rich closing chapters: Meier-Gorlin Syndrome (a real human disorder caused by
  replication-initiation-factor mutations) and Mechanisms/Consequences of Break-Induced Replication.

### STEM/Biology/ top-level files (16 files)

*Discovery, this batch: `pdftotext` (a CLI tool already installed on this machine) works directly via Bash
for any PDF with a real text layer, and is dramatically cheaper/faster than the image-based Read tool —
use it first for future cataloging, falling back to Read only for scanned/image-only PDFs (confirmed on
the Manga Guide title below, which has no extractable text layer at all).*

- **Biological Physics: Energy, Information, Life** — Philip Nelson (2002 student draft, U. Penn). A
  physics-for-biology textbook: Part I "Mysteries, Metaphors, Models" (heat/free energy, entropy/
  temperature — "Heat flows to maximize disorder," the Boltzmann distribution), viscous drag at the DNA
  replication fork as a worked physical example. Opens with an Alexander Pope epigraph on cosmic order.
- **Biological Thermodynamics**, 2nd Ed — Donald T. Haynie (Cambridge). Energy transformation, First/Second
  Laws of Thermodynamics, Gibbs free energy applications (photosynthesis, glycolysis, citric acid cycle,
  oxidative phosphorylation, osmosis, Donnan equilibrium, hemoglobin, molecular pharmacology). Explicitly
  no-calculus-required, aimed at biology/biochemistry/bioengineering undergraduates.
- **Biophysics: An Introduction** — Rodney M.J. Cotterill (Danish Technical University). Chemical binding
  (quantum mechanics, Pauli exclusion, electronegativity), energies/forces/bonds, transport processes
  (diffusion, viscosity, thermal conduction), techniques/methods (X-ray diffraction, NMR, scanning
  tunnelling/atomic force microscopy, optical tweezers, patch clamping, molecular dynamics).
- **Biophysics DeMYSTiFieD** — Daniel Goldfarb (McGraw-Hill Demystified series). Introduction/history of
  biophysics, biophysical topics (molecular/subcellular, physiological/anatomical, environmental
  biophysics), biophysical techniques (ultracentrifugation, electrophoresis, size-exclusion chromatography,
  absorption/fluorescence spectroscopy, mass spectrometry, X-ray crystallography, NMR spectroscopy,
  electron microscopy). A self-teaching/quiz-format introductory guide.
- **Biotechnology Demystified** — Sharon Walker, Ph.D. (McGraw-Hill). Includes a chapter on Immunotherapy
  and Bioengineering Applications (nonspecific immune stimulation, antisera, monoclonal antibodies,
  nanobodies, antibody libraries, ELISA, autoimmune disease, cancer, addictive disorders, allograft
  rejection) — full front-to-back TOC not reached, but scope confirmed as a broad practical biotech primer.
- **Calculations for Molecular Biology and Biotechnology**, 3rd Ed — Frank H. Stephenson (2016, Academic
  Press/Elsevier). A practical math-for-the-lab reference; Chapter 1 "Scientific Notation and Metric
  Prefixes" confirms its applied, calculation-focused scope (concentrations, dilutions, molarity,
  centrifugation, radioisotope calculations are the genre standard for this kind of title).
- **Cell Biology, Genetics, Molecular Biology, Evolution and Ecology**, 14th Ed — P.S. Verma & V.K. Agarwal
  (2005, S. Chand, India — "Multicolour Edition," for Indian university B.Sc./M.Sc. Zoology/Botany/
  Biosciences courses). A genuinely massive single-volume survey (5 major parts): Cell Biology (23
  chapters: techniques, cell/organelles, cytoskeleton, cilia/flagella, cell division, reproduction,
  gametogenesis, fertilization, parthenogenesis, growth); Genetics (Mendel, genetic interaction, linkage,
  crossing over, gene mapping, multiple alleles, gene fine structure, sex determination, chromosomal
  mutation — continues beyond what was read); plus Molecular Biology, Evolution, and Ecology parts per its
  own front-matter summary.
- **Computational Biology** (Methods in Molecular Biology series) — ed. David Fenyö (2010, Springer/Humana
  Press). A multi-author methods anthology; chapters 15-19 confirmed: functional proteomics of the
  *Trypanosoma brucei* nuclear pore complex, inference of signal transduction networks from "double causal
  evidence," reverse-engineering gene regulatory networks (quorum sensing in a plant pathogen), parameter
  inference/model selection in signaling pathway models, and **genetic algorithms applied to in silico
  evolution of genetic regulatory networks** — this last one a direct further cross-reference to the
  genetic-algorithms thread already found in `Genetics/Bioinformatics/`'s *Intelligent Bioinformatics*
  title. Earlier chapters (1-14) not yet reached.
- **Demystifying the Brain: A Computational Approach** — V. Srinivasa Chakravarthy (Springer). A
  computational-neuroscience text: "The World at the Level of a Neuron" (electrochemistry, the explosive
  neural response, the Hodgkin-Huxley experiments, synaptic transmission as "the neuronal handshake"),
  "Networks that Learn" (why neurons are not logic gates). Genuinely relevant to the robot-consciousness
  creative-guiding-principle given its explicit computational framing of neural function.
- **Guyton and Hall Textbook of Medical Physiology**, 13th Ed — John E. Hall (2016, Elsevier) — **the
  single largest and most standard medical-physiology textbook in the English-speaking world.** Full TOC
  captured: 85 chapters across 15 Units — I. Introduction to Physiology: The Cell and General Physiology;
  II. Membrane Physiology, Nerve, and Muscle; III. The Heart (incl. ECG interpretation, cardiac
  failure/shock); [IV, cardiovascular continued]; V. Body Fluids and Kidneys (incl. acid-base regulation,
  diuretics); [VI, blood/immunity — Red Blood Cells, Immunity/Allergy, Blood Types, Hemostasis]; VII.
  Respiration; VIII. Aviation/Space/Deep-Sea Diving Physiology; IX. Nervous System A (sensory physiology,
  the eye, hearing, taste/smell); [X, presumably CNS-adjacent]; XI. Nervous System C (motor/integrative
  neurophysiology — cerebellum, basal ganglia, cerebral cortex, limbic system, sleep/epilepsy/psychoses,
  autonomic nervous system); XII. Gastrointestinal Physiology; XIII. Metabolism and Temperature Regulation
  (carbohydrate/lipid/protein metabolism, the liver, obesity/starvation, fever); XIV. Endocrinology and
  Reproduction (pituitary/thyroid/adrenal/parathyroid hormones, diabetes, male/female reproductive
  physiology, pregnancy/lactation, fetal/neonatal physiology); XV. Sports Physiology. **An exceptionally
  strong grounding resource for any city or faction whose medical/physiological detail needs real
  authority** — genuinely the standard reference doctors themselves study from.
- **Introduction to Experimental Biophysics: Biological Methods for Physical Scientists**, 2nd Ed — Jay L.
  Nadeau (2018, CRC Press, Foundations of Biochemistry and Biophysics series). Introduction/Background,
  Basic Molecular Cloning of DNA and RNA, Expression of Genes in Bacteria/Yeast/Cultured Mammalian Cells,
  Advanced Topics in Molecular Biology — a lab-methods-oriented biophysics text explicitly aimed at
  physical scientists crossing into biology (companion volumes in the same series cover single-molecule
  biophysics and biomolecular thermodynamics).
- **Organic Chemistry Demystified** — Daniel R. Bloch (2006, McGraw-Hill). Chapter 1 "Structure and
  Bonding" (atomic structure, electron energy levels, the octet rule, Lewis structures, valence bond
  theory, molecular orbitals, electronegativity/bond polarity, resonance structures, intermolecular
  forces) — a self-teaching quiz-format organic chemistry primer, general-purpose foundational chemistry
  rather than genetics-specific.
- **Physics of the Human Body**, 2nd Ed — Irving P. Herman (Springer, Biological and Medical Physics
  series; developed from the author's Columbia University engineering-school course). A genuinely
  wide-ranging applied-physics-of-the-body text: balance/walking/running/jumping biomechanics (inverted
  pendulum and bouncing-ball/pogo-stick models), muscle sliding-filament mechanics and evolution/fatigue,
  metabolism/energy/heat/work/power (ATP production and use), breathing mechanics, and sound/speech/
  hearing physics (auditory sensitivity, speech production energetics). Explicitly designed to be
  teachable at multiple depth levels (Chapters 1-10 in detail, 11-13 lighter, in a single-semester course).
- **The Manga Guide to Molecular Biology** — Masaharu Takemura & Sakura (No Starch Press, 2009) — has no
  extractable text layer (confirmed via `pdftotext` returning empty output), meaning it's fully scanned/
  image-based. **Update 2026-07-23:** the OCR toolchain (`pdftoppm` + `tesseract`) confirmed working
  elsewhere in this pass would very likely work here too — genuinely not attempted this pass (manga-format
  panels may OCR less cleanly than plain text pages, and this title wasn't prioritized), not a hard
  limitation. Title only, from filename — a real candidate for a future OCR pass.
- **The Manga Guide to Physiology** — Etsuro Tanaka & Keiko Koyama (No Starch Press, 2015). A genuine
  educational manga (illustrated/story-driven) with a real, substantial physiology curriculum underneath:
  Prologue, then 10 chapters — Circulatory System (ECG, blood pressure, lymphatic system), Respiratory
  System, Digestive System, [chapters 4-7 not captured], Musculoskeletal System (muscle fibers, joints,
  body-temperature regulation, bone metabolism), Cells/Genes/Reproduction (cell division, sexual
  reproduction), Endocrine System (hormone balance). A genuinely different register from the dense
  technical texts elsewhere in this collection — worth considering as a tonal model if any in-world
  in-universe "educational comic" artifact is ever wanted (Tepenia already has a robot-inhabited setting
  where accessible science-education media would plausibly exist).

### Evolutionary Studies (Biology and Psychology)/ top-level (14 files) + Handbook of Evolutionary Psychology, 2 Vol.

**Note on scope, 2026-07-19:** the developer clarified that several of the sex/mating-focused titles below
were pasted into this folder by accident, copied over from a different folder for a different, unrelated
project, and were never intentionally curated for this collection ("when I copy-pasted from the other
folder, I forgot to take those out"). Same status as the dropped `primates/` subfolder — not meaningfully
in scope here. Cataloged lightly below since partial data was already gathered, but not pursued further.

- **Evolutionary Psychology: The New Science of the Mind**, 6th Ed — David M. Buss (2019, Routledge) — the
  standard textbook of the field. 5 parts, 13 chapters: Foundations of Evolutionary Psychology; Problems
  of Survival (Combating the Hostile Forces of Nature); Challenges of Sex and Mating (Women's/Men's
  Long-Term Mating Strategies, Short-Term Sexual Strategies); Challenges of Parenting and Kinship; Problems
  of Group Living (Cooperative Alliances, Aggression and Warfare, Conflict Between the Sexes, Status/
  Prestige/Social Dominance, Toward a Unified Evolutionary Psychology).
- **The Red Queen: Sex and the Evolution of Human Nature** — Matt Ridley — TOC not reached in this pass
  (author bio only). A well-known popular-science book on sexual selection theory (Red Queen hypothesis).
- **Personality Psychology: Domains of Knowledge about Human Nature**, 6th Ed — Randy J. Larsen & David M.
  Buss (2017, McGraw-Hill). A substantial personality-psychology textbook (1000+ pages) — Introduction
  (Personality Assessment/Measurement/Research Design); The Dispositional Domain (Traits/Trait Taxonomies,
  Theoretical/Measurement Issues, Personality Stability/Coherence/Change); The Biological Domain (Genetics
  and Personality, Physiological Approaches, Evolutionary Perspectives on Personality); further domains
  (Intrapsychic, etc.) not fully captured. Genuinely relevant to companion/character-writing generally,
  not just Vostok.
- ~~The Consuming Instinct — Gad Saad~~ **Removed 2026-07-23, developer's request: "remove anything written
  by Gad Saad. I've decided I don't want his work."** File deleted from `Evolutionary Studies/`; no other
  Gad Saad titles found anywhere in the collection.
- **The Dangerous Passion: Why Jealousy Is As Necessary As Love and Sex** — David M. Buss (2000). 9
  chapters: The Dangerous Passion, The Jealousy Paradox, Jealousy on Mars and Venus, The Othello Syndrome,
  "If I Can't Have Her, Nobody Can," Secrets and Lies, Why Women Have Affairs, Coping Strategies, Emotional
  Wisdom.
- **The Evolutionary Biology of Human Female Sexuality** — Randy Thornhill & Steven W. Gangestad (2008,
  Oxford). *(Sex-focused title, likely misplaced per developer note above.)* 13 chapters incl. Concealed
  Fertility, Coevolutionary Processes (men's counterstrategies/women's responses), Reflections. Opens with
  a striking 1857 Victorian-sexology epigraph (William Acton) as a historical foil.
- **The Evolution of Desire: Strategies of Human Mating**, 2nd Ed — David M. Buss (2016). *(Likely
  misplaced.)* 10 chapters: Origins of Mating, What Women Want, What Men Want, Casual Sex, Attracting a
  Partner, Staying Together, Sexual Conflict, Breaking Up, Changes over Time, Harmony Between the Sexes.
- **The Evolution of Violence** (Evolutionary Psychology series) — eds. Todd K. Shackelford & Ranald D.
  Hansen, incl. a chapter by Buss & Duntley (2014, Springer). Multi-author anthology: Intimate Partner
  Violence, War Before Civilization, Violence in Literature, Evolutionary Perspectives on Child Welfare
  Law, Warfare and Human Nature, Sexual Selection/Intergroup Conflict, Evolutionary Behavioral Genetics of
  Violent Crime (TOC continues beyond what was captured).
- **The Handbook of Evolutionary Psychology**, 1st Ed — ed. David M. Buss (2005, Wiley), foreword Steven
  Pinker. Part I Foundations (Tooby & Cosmides on conceptual foundations, life history theory, domain
  specificity, methods, controversial issues); Part II Survival (locating places, predator/prey
  adaptations, adaptations to dangers from humans); Part III Mating (fundamentals of mating strategies,
  physical attractiveness, adaptations to ovulation) — TOC continues beyond what was captured.
- **The Handbook of Evolutionary Psychology, 2 Volumes**, 2nd Ed — ed. David M. Buss (2015, Wiley) — the
  2-volume expansion of the above (Vol. 1: Foundations; Vol. 2: Application), foreword Steven Pinker. Vol.
  1 Part I Foundations: Theoretical Foundations (Tooby & Cosmides), Life History Theory, Methods of
  Evolutionary Sciences, Evolutionary Psychology and Its Critics, Intuitive Ontologies/Domain Specificity;
  Part II Survival (TOC continues beyond what was captured).
- **The Mating Mind: How Sexual Choice Shaped the Evolution of Human Nature** — Geoffrey Miller (2001).
  *(Likely misplaced.)* 9 chapters: Central Park, Darwin's Prodigy, The Runaway Brain, A Mind Fit for
  Mating, Ornamental Genius, Courtship in the Pleistocene, Bodies of Evidence, Arts of Seduction, Virtues
  of Good Breeding.
- **The Murderer Next Door: Why the Mind Is Designed to Kill** — David M. Buss (2005/2014 edition). 9
  chapters: The Murdering Mind, The Evolution of Killing, The Dangerous Game of Mating, When Love Kills,
  Sexual Predators, Mate Poachers, Blood and Water, Status and Reputation, The Killers Among Us. A
  genuinely strong potential source for in-world criminal-psychology/murder-mystery quest writing.
- **Why Women Have Sex** (2 separate editions/scans present, 545pp and 401pp) — Cindy M. Meston & David M.
  Buss — *(likely misplaced per developer note above)* — no extractable text layer on either copy, titles
  only.

**Recommended next step:** this completes every folder flagged in scope for the STEM/Biology cataloging
pass as of 2026-07-19. All tasks on `STEM_Biology_Cataloging_Checklist.md` are now ✅ or explicitly
dropped by the developer.

---

## Economics (16 files, incl. `Thomas Sowell/` subfolder) — ✅ complete 2026-07-23

*Several titles in this folder are scanned/image-based PDFs with no extractable text layer — noted
per-title below, title only from filename, same convention as elsewhere in this reference.*

### The Wealth of Nations — Adam Smith (ElecBook Classics edition)
Introduction and Plan of the Work; Book One: Causes of Improvement in the Productive Powers of Labour
(Division of Labour, Origin of Money, Price of Commodities, Wages, Profits, Rent of Land — extensive
sub-parts); Book Two: Nature, Accumulation, and Employment of Stock (Division of Stock, Money as Capital,
Accumulation of Capital, Stock Lent at Interest, Different Employments of Capital) — TOC continues into
further Books beyond the read range.

### A Conflict of Visions: Ideological Origins of Political Struggles, 2nd Ed — Thomas Sowell (2007)
Part I Patterns (Role of Visions, Constrained/Unconstrained Visions, Visions of Knowledge and Reason,
Visions of Social Processes, Varieties and Dynamics of Visions); Part II Applications (Visions of Equality,
Power, Justice, Visions/Values/Paradigms).

### Applied Economics: Thinking Beyond Stage One, 2nd Ed — Thomas Sowell (2008/2009)
8 chapters: Politics versus Economics; Free and Unfree Labor; The Economics of Medical Care; The
Economics of Housing; Risky Business; The Economics of Immigration; The Economics of Discrimination; The
Economic Development of Nations.

### Basic Economics: A Common Sense Guide to the Economy, 5th Ed — Thomas Sowell (2014)
27 chapters across 7 parts: Prices and Markets; Industry and Commerce; Work and Pay; Time and Risk; The
National Economy; The International Economy; Special Economic Issues (incl. Myths About Markets,
"Non-Economic" Values, The History of Economics). Deliberately no graphs/equations — real-world examples
from countries worldwide, aimed at general readers.

### Conquests and Cultures: An International History — Thomas Sowell (1999) — re-cataloged 2026-07-23 via OCR
The third book of a trilogy that began with *Race and Culture* (1994) and *Migrations and Cultures* (1996) —
all three originally parts of a single manuscript Sowell began in 1982, which also spun off a fourth related
book, *Preferential Policies: An International Perspective* (1991). This volume covers the cultural
consequences of conquests specifically (as distinct from migrations) — the British chapter, for instance,
traces back to the Roman conquest of the island. Underlying theme across the whole trilogy: racial, ethnic,
and national groups have their own respective cultures that cannot be reduced to how "society" around them
has treated them.

### Economic Facts and Fallacies, 2nd Ed — Thomas Sowell (2011)
8 chapters: The Power of Fallacies; Urban Facts and Fallacies; Male-Female Facts and Fallacies; Academic
Facts and Fallacies; Income Facts and Fallacies; Racial Facts and Fallacies; Third World Facts and
Fallacies; Parting Thoughts.

### Inside American Education: The Decline, the Deception, the Dogmas — Thomas Sowell (1993, PDF + EPUB copies)
Part One: Schools (Impaired Faculties, Classroom Brainwashing, Assorted Dogmas); Part Two: Colleges and
Universities (Damaging Admissions, "New Racism" and Old Dogmatism, Ideological Double Standards, Teaching
and Preaching, Athletic Support); Part Three: Assessment (The Empire Strikes Back, Bankruptcy).

### Intellectuals and Society, 2nd Ed — Thomas Sowell (2015)
Part I Introduction (Intellect and Intellectuals, Knowledge and Notions); Part II Intellectuals and
Economics; Part III Intellectuals and Social Visions (incl. "A Conflict of Visions," Patterns of the
Anointed); Part IV Optional Reality (Filtering Reality, Subjective Truth); Part V Intellectuals and the
Law; Part VI Intellectuals and War (The World Wars).

### Knowledge and Decisions — Thomas Sowell (1980/1996 ed.)
Part I Social Institutions (Role of Knowledge, Decision-Making Process, Economic/Social/Political
Trade-Offs, An Overview); Part II Trends and Issues (Historical Trends, Trends in Economics/Law/Politics).
Central theme: decision-making mechanics and institutions determine what knowledge can be brought to bear,
not just what decision is made.

### Migrations and Cultures: A World View — Thomas Sowell (1997) — re-cataloged 2026-07-23 via OCR
Chapter 1: Migration Patterns — opens framing migration (100 million immigrants worldwide, 19 million of
them refugees) as a major, ancient social phenomenon distinct from conquest, covering voluntary migration,
forced/bonded migration (the Atlantic slave trade, Slavs across Europe), and mass expulsions/"ethnic
cleansing." Research drew on travel to 15 countries across 4 continents. First book of the same trilogy as
*Conquests and Cultures* above.

### Race and Culture: A World View, 2nd Ed — Thomas Sowell (1995) — re-cataloged 2026-07-23 via OCR
Preface confirms the book's central methodological stance: culture is treated primarily as "human capital"
(skills, work habits, saving propensities, attitudes toward education/entrepreneurship) rather than "real
culture" (music, art) alone, and race/ethnicity are treated as social rather than strictly biological
categories (e.g., discussing how the same person can be classified differently — "black" in the U.S. vs.
"branco" in Brazil — depending on which society's social categories apply). Explicitly challenges "social
science" doctrines that treat groups' outcomes as determined solely by their surrounding environment/society
rather than by their own transmitted cultural patterns.

### The Economics and Politics of Race: An International Perspective — Thomas Sowell (1985) — re-cataloged 2026-07-23 via OCR
2 parts, 8 chapters: Part I History — The Role of Race, The Overseas Chinese, European Emigrants, Blacks and
Coloreds; Part II Analysis — An International Perspective, The American Experience, The Third World, The
Past and the Future.

### The Quest for Cosmic Justice — Thomas Sowell (1999) — re-cataloged 2026-07-23 via OCR
Opens with a Socrates epigraph on justice. Central argument (from the title essay, developed from a 1996
lecture in New Zealand): "social justice" advocates conflate genuine injustice with cosmic/inherent
inequalities that no institutional arrangement can actually correct — confirmed section: "Inequalities and
Injustices." Also includes the essay "Visions of War and Peace" (developed from a 1987 *Encounter* article)
and "The Tyranny of Visions."

### The Vision of the Anointed: Self-Congratulation as a Basis for Social Policy — Thomas Sowell (1995, 2 copies)
Both copies in this folder are scanned/no text layer (317 pages each) — but the same title already has a
readable TOC captured in the original `politics/` folder catalog above: 9 chapters (Flattering Unction; The
Pattern; By the Numbers; The Irrelevance of Evidence; The Anointed versus the Benighted; Crusades of the
Anointed; The Vocabulary of the Anointed; Courting Disaster; Optional Reality).

**Cross-reference note:** "The Vision of the Anointed" now has 3 total copies across this collection (1 in
`politics/`, 2 here in `economics/Thomas Sowell/`) — all the same book, not separate editions worth
distinguishing.

---

## Philosophy (~20 files, incl. `Arthur Schopenhauer/`, `Carl Gustav Jung/`, `ethics/`, `Marcus Aurelius/` subfolders) — ✅ complete 2026-07-23

### Arthur Schopenhauer/ (2 files, 1 title in 2 volumes)

- **The World as Will and Representation [2 Volumes]** — Arthur Schopenhauer — re-cataloged 2026-07-23 via
  OCR (both volumes are scanned, 558 pages Vol. 1). Confirmed the Translator's Introduction with detailed
  German-term glossary notes (*Anschauung*, *Wahrnehmung*, *Vernunft*, *Vorstellung* — rendered
  "representation" over Haldane/Kemp's older "idea"), plus full editorial/textual history (Frauenstädt's
  1873 edition through Hübscher's definitive 1937 manuscript-based edition, this translation dated London,
  1957). A second, separate top-level copy of the same title (`The World as Will and Representation - Arnold
  Schopenhauer (2-vol)`, note the misspelled first name in the filename) also exists — presumed same
  content/format, not independently re-verified.

### Carl Gustav Jung/ (11 files)

- **Aion: Researches into the Phenomenology of the Self** (Collected Works Vol. 9ii). 10 chapters: The Ego;
  The Shadow; The Syzygy: Anima and Animus; The Self; Christ, a Symbol of the Self; The Sign of the Fishes;
  The Prophecies of Nostradamus; The Historical Significance of the Fish; The Ambivalence of the Fish
  Symbol; The Fish in Alchemy (TOC continues beyond what was captured). Also present: an EPUB duplicate
  (unreadable) and a separately-titled `The Collected Works of C. G. Jung — Aion` PDF (22MB, presumed same
  content, not independently re-verified).
- **Man and His Symbols** — conceived/edited by Jung, completed by his associates after his death (his own
  final work, finished ten days before he died). 5 parts + conclusion: Part 1 Approaching the Unconscious
  (Jung himself); Part 2 Ancient Myths and Modern Man (Joseph L. Henderson); Part 3 The Process of
  Individuation (M.-L. von Franz); Part 4 Symbolism in the Visual Arts (Aniela Jaffé); Part 5 Symbols in an
  Individual Analysis (Jolande Jacobi); Conclusion: Science and the Unconscious (von Franz).
- **Modern Man in Search of a Soul** (1933) — re-cataloged 2026-07-23. 11 essays: Dream-Analysis in Its
  Practical Application; Problems of Modern Psychotherapy; The Aims of Psychotherapy; A Psychological Theory
  of Types; The Stages of Life; Freud and Jung — Contrasts; Archaic Man; Psychology and Literature; The
  Basic Postulates of Analytical Psychology; The Spiritual Problem of Modern Man; Psychotherapists or the
  Clergy.
- **Symbols of Transformation** (Collected Works Vol. 5, 1952 rewrite of the 1912 *Wandlungen und Symbole
  der Libido*). Part One: Introduction, Two Kinds of Thinking, The Miller Fantasies: Anamnesis, The Hymn of
  Creation, The Song of the Moth; Part Two: Introduction, The Concept of Libido, The Transformation of
  Libido, The Origin of the Hero, Symbols of the Mother and of Rebirth, The Battle for Deliverance from the
  Mother, The Dual Mother, The Sacrifice, Epilogue; Appendix (the complete Miller fantasies).
- **Synchronicity: Nature and Psyche in an Interconnected Universe** — Joseph Cambray (2009, not Jung
  himself — a scholarly volume in the Fay Book Series on Analytical Psychology, examining Jung's
  synchronicity concept via field theory, systems theory, and complexity). Filename attributes this to Jung
  directly, which is a mislabel worth noting.
- **The Collected Works of C.G. Jung — Complete Digital Edition** — both the PDF and EPUB "files" are
  9-byte placeholder stubs, not actual book content (a broken/incomplete download, same category as the
  `to_download.txt` non-book files elsewhere in this collection).
- **The Red Book: Liber Novus** — 404 pages, Jung's famous illuminated/calligraphic manuscript — re-cataloged
  2026-07-23 via OCR. The editorial front matter (Ulrich Hoerni's foreword) is genuinely rich: the Society of
  Heirs' 2000 decision to release it for publication, Sonu Shamdasani as editor, the Philemon Foundation's
  role, and the reasoning for publishing at all (Jung's own text addresses "dear friends" — he never treated
  it as fully secret, and considered it central to the confrontation with the unconscious that produced all
  his later work). Structure: Liber Primus (referenced by facsimile folio number) and Liber Secundus
  (referenced by facsimile page number), plus the "Scrutinies" manuscript continuing where the calligraphic
  draft ends, containing the Seven Sermons.
- **The Undiscovered Self / Symbols and the Interpretation of Dreams** — re-cataloged 2026-07-23. Part I The
  Undiscovered Self (Presence and Future): The Plight of the Individual in Modern Society; Religion as the
  Counterbalance to Mass-Mindedness; The Position of the West on the Question of Religion; The Individual's
  Understanding of Himself; The Philosophical and the Psychological Approach to Life; Self-Knowledge; The
  Meaning of Self-Knowledge. Part II Symbols and the Interpretation of Dreams: The Significance of Dreams;
  The Functions of the Unconscious; The Language of Dreams; The Problem of Types in Dream Interpretation; The
  Archetype in Dream Symbolism; The Function of Religious Symbols; Healing the Split.

### ethics/ (1 file + a non-book download-link file)

- **Ethics 101: From Altruism and Utilitarianism to Bioethics and Political Ethics** — Brian Boone (2017).
  10 chapters: Ethics and the Ancient Greek Philosophers; The Divergent Greek Schools (Cynics, Skeptics,
  Epicureans, Stoics, Neoplatonism); Consequentialist Ethics (Bentham, Mill, utilitarianism); Deontological
  Ethics (Kant, Rawls); Virtue Ethics and Divine Command Theory (incl. Aquinas, ethical relativism); Eastern
  Moral Philosophies (Buddhist ethics, Confucianism, Ibn Sina, Taoist ethics); Negative Views on Ethics
  (Machiavelli, Sartre, Nietzsche, Schopenhauer, Wittgenstein); Other Moral Philosophers (Abelard, Voltaire,
  Locke, Shaftesbury, Spinoza); Classic Ethics Exercises (Trolley Problem, Prisoner's Dilemma, Sorites
  Paradox, Ship of Theseus); Applied Ethics (business, political, medical). A broad, accessible survey
  covering an unusually wide range of ethical traditions in one volume.
- `to_download.txt` — not a book, zlibrary download links.

### Marcus Aurelius/ (1 file + a non-book download-link file)

- **Meditations** — Marcus Aurelius, tr. Martin Hammond, intro Diskin Clay (Penguin Classics, 2006). Front
  matter and translator's introduction confirmed; the work itself is Marcus Aurelius's own 12 Books of
  private philosophical reflections (Stoic philosophy) — full internal Book-by-Book breakdown not reached
  within this pass's read range.
- `to_download.txt` — not a book, zlibrary download links.

### Top-level singles (7 files)

- **Everything Is F*cked** — Mark Manson — re-cataloged 2026-07-23. Part I: Hope (The Uncomfortable Truth,
  Self-Control Is an Illusion, Newton's Laws of Emotion, How to Make All Your Dreams Come True, Hope Is
  Fucked); Part II: Everything Is Fucked (The Formula of Humanity, Pain Is the Universal Constant, The
  Feelings Economy, The Final Religion).
- **Fashionable Nonsense: Postmodern Intellectuals' Abuse of Science** — Alan Sokal & Jean Bricmont (1998).
  Introduction, then chapters on Jacques Lacan, Julia Kristeva, Jean Baudrillard, Gilles Deleuze and Félix
  Guattari, Paul Virilio, and an Epilogue — the book's own structure is one chapter per postmodern
  intellectual figure whose scientific/mathematical citations are examined and critiqued.
- **How the Mind Works** — Steven Pinker (1998). 8 chapters: Standard Equipment; Thinking Machines; Revenge
  of the Nerds; The Mind's Eye; Good Ideas; Hotheads; Family Values; The Meaning of Life.
- **Impostures Intellectuelles** — Alan Sokal & Jean Bricmont (2nd Ed, 1999), DJVU + PDF copies — the French
  edition of *Fashionable Nonsense* above (same authors). DJVU copy re-cataloged 2026-07-23 via `djvutxt`,
  confirming the same one-chapter-per-figure structure in the original French (Sommaire): Préface à la
  deuxième édition; Introduction; 1. Jacques Lacan; 2. Julia Kristeva; 3. Intermezzo: le relativisme cognitif
  en philosophie des sciences; 4. Luce Irigaray; 5. Bruno Latour; 6. Intermezzo: la théorie du chaos
  (continues).
- **[Did My Neurons Make Me Do It?] Philosophical and Neurobiological Perspectives on Moral Responsibility
  and Free Will** — Nancey Murphy & Warren S. Brown (2007, Oxford). Preface confirmed (argues against
  neurobiological reductionism, combining philosophy of anti-reductionism with neuropsychological
  anti-Cartesianism) — full chapter TOC not reached within this pass's read range. Genuinely relevant
  material for the robot-consciousness guiding principle and for Identity Fragmentation's own
  echo-state/self-continuity themes.
- **The Subtle Art of Not Giving a Fuck** — Mark Manson (2016). 9 chapters: Don't Try; Happiness Is a
  Problem; You Are Not Special; The Value of Suffering; You Are Always Choosing; You're Wrong About
  Everything (But So Am I); [remaining chapters not captured in this pass].
- **The World as Will and Representation** — Arnold [sic — Arthur] Schopenhauer (2-vol single-file copy) —
  see the `Arthur Schopenhauer/` subfolder entry above; not independently re-verified as identical, but
  presumed the same underlying text.
- `to_download.txt` — not a book, zlibrary download links.

---

## Games (4 files, incl. `Chess/`, `Shogi/` subfolders) — ✅ complete 2026-07-23

**Directly relevant to the flagged-but-undesigned "Shogi + Chess synthesized strategy game" minigame idea**
(see `project_synthesized_strategy_game_minigame` memory) — this is the actual source material for that
future task, not just general reference.

### Chess/ (1 file)

- **How To Play Chess** — DK/Dorling Kindersley (2006/2016 ed.), consultant Aaron Summerscale. Introduction
  (The Object of the Game, Starting Positions); The Pieces (Rook, Bishop, Queen, Knight, Pawn, King,
  Special Moves); Winning Your First Games (Piece Value and Exchanging, Developing Your Pieces — TOC
  continues beyond what was captured). A visual, beginner-oriented guide (DK's signature illustrated style).

### Shogi/ (3 files)

- **Better Moves for Better Shogi** — Aono Teruichi, tr. John Fairbairn (bilingual Japanese/English edition,
  originally "The NHK Shogi Lectures" — step-by-step instruction series) — re-cataloged 2026-07-23 via OCR;
  confirmed title/subtitle, but the bilingual Japanese/English layout OCRs poorly for body content beyond
  that — a genuine remaining limitation of this specific title, not a tooling gap.
- **Japanese Chess: The Game of Shogi** — Trevor Leggett & Alan Baker — re-cataloged 2026-07-23. The Board
  and the Men (I. The Board; II. The King; III. The King's Bodyguard: Gold and Silver; IV. The Rook; V. The
  Bishop; VI. The Knight; VII. The Lance; VIII. The Pawn); Learning to Use the Pieces; The Paratroops
  (drop rule); The Value of the Pieces; Novice's Game; An Introduction to the Openings (Static Rook, Yagura,
  Ranging Rook openings); A Few Game Positions.
- **The Art of Shogi** — A.L. (Tony) Hosking (1996/97, The Shogi Foundation) — re-cataloged 2026-07-23 via
  OCR, yielding a full 11-part contents page: (1) Historical Introduction; (2) Piece Identification; (3)
  Rules of Movement (starting position, promotion, major/minor pieces, capturing, drops, checkmate); (4)
  Comparison of Shogi with Chess (starting position, captured-piece reuse, piece values); (5) Introduction to
  Shogi Strategy and Tactics; (6) The Endgame (hunting/harvesting the king, mating nets, checkmate problems
  and solutions); (7) Balancing Attack with Defence (static rook vs. ranging rook); (8) Castles (double
  static rook, ranging rook, anti-ranging-rook, Anaguma); (9) Attack! (rook's pawn exchange, bishop's
  diagonal, climbing/reclining silver, sacrifices); (10) Two Historical Games (the oldest recorded complete
  shogi game, 1607; an 1856 Edo Castle game); (11) Shogi Handicap Games (2-piece through rook-only handicaps).
  By far the richest and most systematically organized of the three Shogi titles — the natural primary
  source if the Shogi+Chess minigame task gets picked up.

**Updated note, 2026-07-23:** all 3 titles are now at least partially readable. *The Art of Shogi* in
particular has a genuinely complete, well-organized TOC — a strong primary source for the flagged
Shogi+Chess synthesized-strategy-game minigame idea. *Better Moves for Better Shogi*'s bilingual layout
remains a real, narrower OCR limitation (not a missing-tool problem).

---

## Language (27 files, incl. `psycholinguistics/`, `Sumerian/` subfolders) — ✅ complete 2026-07-23

### Top level (5 files)

- **Astrolinguistics** — Alexander Ollongren. Formal/mathematical approach to constructing messages for
  interstellar communication (METI/SETI) using Lincos-style logical languages.
- **Forensic Linguistics** — John Olsson. Front-matter/author-bio captured (Olsson is a founding figure in
  forensic linguistics, expert-witness casework); full chapter list not fully captured this pass.
- **Language and Time** — Vyvyan Evans. Three-part structure: Part I lays out the philosophical/linguistic
  background on time; Part II covers tense and grammatical aspect; Part III covers lexical semantics of time
  words. Full chapter breakdown within each part captured.
- **Language Change: Progress or Decay?** — Jean Aitchison. Three-part, 11+ chapter structure: the
  "decay/progress" debate framing, mechanisms of change (spread through a speech community, contact,
  simplification), and case studies of change in progress.
- **The Grammar of Names** — John M. Anderson. A syntactic/semantic theory of proper names within a
  dependency-grammar framework; chapters 4-9 captured (nominal categories, determiners, the syntax of
  names across languages), chapters 1-3 (the opening theoretical setup) not fully captured.

### psycholinguistics/ (7 files, all Ray Jackendoff or Jackendoff-adjacent)

- **A User's Guide to Thought and Meaning** — Ray Jackendoff (2012, OUP). Popular/accessible restatement of
  his semantics program. Part One: Language, Words, and Meaning (14 chapters — what's a language, word
  meaning, "objective" vs. "subjective" meaning, meanings vs. concepts, linguistic relativity); Part Two:
  Consciousness and Perception (what it's like to be thinking, tests of the "Unconscious Meaning Hypothesis").
- **Foundations of Language: Brain, Meaning, Grammar, Evolution** (2002). Part covering rules of grammar,
  lexical redundancy/inheritance hierarchies, then Chapter 4 "Universal Grammar" (poverty-of-stimulus
  argument, linguistic universals, genetics of UG, species-specificity evidence); Part II Architectural
  Foundations; Chapter 7 covers structure-constrained modularity and Fodor's modularity thesis; Chapter 8
  "An Evolutionary Perspective on the Architecture" (Bickerton's proposal, protophonology, phrase structure
  evolution); Part III Semantic and Conceptual Foundations opens with "Semantics as a Mentalistic Enterprise."
- **Language, Consciousness, Culture: Essays on Mental Structure** (2007, Jean Nicod Lectures). Chapter 2
  covers the "Parallel Architecture" framework directly — three founding themes of generative grammar, the
  "broken promise" that deep structure would be the key to the mind, "syntactocentrism" as a scientific
  mistake, phonology as an exemplar of Parallel Architecture, the lexicon/grammar distinction, words-and-rules.
- **Patterns in the Mind: Language and Human Nature** (2015 printing) — **scanned/image-only PDF (tiff2pdf),
  required OCR** (`pdftoppm` + `tesseract`, page 6). Full contents recovered: Part I The Fundamental
  Arguments (nature/nurture, argument for mental grammar, argument for innate knowledge); Part II The
  Organization of Mental Grammar (overview, phonological structure, syntactic structure, American Sign
  Language); Part III Evidence for the Biological Basis of Language (how children learn language, language
  acquisition in unusual circumstances, language and the brain); Part IV Mental Capacities Other Than
  Language (construction of experience, music and vision, language as a window on thought, social
  organization).
- **Semantics and Cognition** (1983, MIT Press, Current Studies in Linguistics series #8). Part I Basic
  Issues (Semantic Structure and Conceptual Structure; Sense and Reference); Part II Cognitive Foundations of
  Semantics (Individuation; The Syntax of Conceptual Structure; Categorization; Semantic Structure Is
  Conceptual Structure); Part III Word Meanings (Problems of Lexical Analysis; Preference Rule Systems);
  Part IV Applications (TOC continues beyond what was captured).
- **Simpler Syntax** — Peter W. Culicover & Ray Jackendoff (2005). Chapter 2 covers uniform lexical
  projection/passive, the Structure-Preserving Hypothesis, raising, government and binding, trace theory;
  Chapter 3 "Later History of Mainstream Syntax" (Late PPT, UTAH, Head Movement, the Minimalist Program,
  "Uniformity entails Generative Semantics"); Chapter 4 "Flat Structure."
- **The Architecture of the Language Faculty** (1997, Linguistic Inquiry Monographs series). Covers anaphora
  and binding inside lexical items; a chapter on morphosyntax vs. morphophonology, inflectional vs.
  derivational morphology, productivity/semiproductivity, "optimal coding" of semiproductive forms; a later
  chapter on lexical insertion of idioms, parallels between idioms and compounds, and Construction Grammar.
  This is Jackendoff's core statement of the "Parallel Architecture" (syntax/semantics/phonology as
  independent generative systems linked by interface rules) that recurs across several of the other titles
  in this subfolder.

### Sumerian/ (13 files/folders — directly relevant to existing lore's Sumerian-speech origin-lab canon,
see `project_sumerian_flagged` memory)

- **A Descriptive Grammar of Sumerian** — Abraham Hendrik Jagersma. Full modern reference grammar: history
  of the language/speakers, genetic/areal relationships, sources, dialects, "the death of Sumerian,"
  grammatical terminology and notational conventions; The Writing System (orthography, early development,
  spelling of syllable-final consonants/vowel length, transliteration); Phonology (the stops, affricates).
- **Introduction to Sumerian Grammar** — Daniel A. Foxvog (revised 2014, UC Berkeley). Contents: Preface;
  The Sumerian Writing System; Table of Syllabic Sign Values; Phonology; Nouns and Adjectives; The Nominal
  Chain; Pronouns and Demonstratives; Summary of Personal Pronoun Forms; The Adnominal Cases (Genitive and
  Equative); The Copula; Adverbs and Numerals; The Adverbal Cases; Introduction to the Verb.
- **Sumerian Grammar** — Dietz Otto Edzard (PDF + EPUB duplicate). Contents: The Sumerian Language (general
  characteristics, the "hopeless question" of Sumerian's linguistic affiliation, linguistic environment);
  How We Read Sumerian (spelling, classification/combination/evolution of cuneograms).
- **Ein Compendium sumerisch-akkadischer Beschwörungen** — Wolfgang Schramm (2008, Göttinger Beiträge zum
  Alten Orient Band 2, German). Not a grammar — a reconstructed collection of 21 Sumerian and
  Sumerian-Akkadian incantations/exorcism texts tied to the god Enki (Ea) and his son Asalluhi (Marduk),
  reconstructed mainly from Ashurbanipal's library at Nineveh (7th c. BCE) with some material tracing to the
  2nd millennium BCE. Structure: Ch. 1 Introduction (incl. "Der Inhalt des Compendiums" = contents overview);
  Ch. 2 Standard Text and Translation, one section per incantation (21 total).
- **An Introduction to the Grammar of Sumerian** — Gábor Zólyomi ("Zolyomi Sumer READER"). Lesson-based
  textbook structure: Lesson 1 Introduction (sources, writing system, dialects, Sumerian-Akkadian
  bilingualism); Lesson 2 Phonology (consonants, vowel harmony, syllable structure/stress); Lesson 3 The
  Nominal Template and Non-Adverbial Cases (ergative/absolutive, genitive, equative); Lesson 4 Genitive
  Constructions — each lesson includes "Further readings" and "Exercises."
- **Sumerian: The Descendent of a Proto-Historical Creole** — Jens Høyrup. Argues Sumerian arose via
  creolization. Contents: I. Introductory Remarks; II. The "Sumerian Problem"; III. Settlement Development
  and Creolization; IV. Sumerian? (phonology, lexicon, the sentence, gender/animacy, ergativity, the verb,
  the "pre-Sumerian substrate"); V. Conclusions?
- **Sumerian Lexicon** (Version 3.0) — John A. Halloran. A dictionary, not a grammar — 1,255 Sumerian
  logogram words and 2,511 Sumerian compound words, with notes on cuneiform sign readings and homophone
  notation conventions.
- **A Sumerian Reader** — Konrad Volk, with Silvano Votto & Annette Zgoll (2nd rev. ed., 1999, Studia Pohl:
  Series Maior #18, Pontifical Biblical Institute). Scanned PDF; a selection of annotated Sumerian texts for
  reading practice rather than a systematic grammar.
- **Sumerian Liturgical Texts** — Stephen Herbert Langdon. Scanned/OCR'd. Contents: Introduction; then a
  series of Sumerian liturgical texts in translation — an epic poem on the origin of Sumerian civilization, a
  lamentation to Aruru, a penitential psalm to the god Amurru, a lamentation on the invasion by Gutium, the
  Legend of Gilgamesh, and liturgical hymns to Ur-Engur, Dungi, and Libit-Ishtar/Ishme-Dagan.
- **A Sumerian Grammar and Chrestomathy** — Stephen Langdon. Scanned/OCR'd (page-number column badly
  garbled by the scan but chapter list intact). 11 numbered chapters plus preface/addenda/errata: Historical
  Outline; Origin and Characteristics of Sumerian Writing; Phonetic Elements and Sound-Changes; The
  Determinatives; Nouns and Adjectives; Pronouns; Numerals; The Verb; Conjunctions etc.; Adverbs; a Selection
  of Texts, followed by a vocabulary of principal roots and a syllabic-value list.
- **Sumerian Grammatical Texts** — Stephen Langdon (1917, University of Pennsylvania Museum Publications of
  the Babylonian Section, Vol. XII No. 1). Scanned. Not a modern textbook — a primary-source edition of
  ancient native Sumerian grammatical/lexical texts (bilingual sign-lists and paradigms), with a list of
  abbreviations for the cited cuneiform text corpora.
- **The Sumerian Language: An Introduction to Its History and Grammatical Structure** — Marie-Louise Thomsen
  (1984, 3rd printing, Copenhagen Studies in Assyriology Vol. 10). Full table of contents: Preface;
  Acknowledgements; Introduction; Grammar (opens with Phonetics) — the standard modern academic reference
  grammar of the language.
- **Sumerian Grammar** — Thorkild Jacobsen. Only 21 pages — a short typed/mimeographed lecture-handout style
  document (property of the American Schools of Oriental Research, per a repeating watermark that required
  rasterized OCR to see past). Covers Jacobsen's own analytical framework: the "nexus" relationship
  (ergative/subject roles), verbids, a detailed structure-of-the-verb system (modal prefixes, mode-of-awareness
  prefixes tied to the speaker's psychological "ken," personal/neuter comitative and locative infixes), and
  worked example sentences from Sumerian literary texts (Gudea Cylinder, Shulgi Hymn, the Aratta epic).

**Why this subfolder matters:** the developer's existing lore already ties in-game Sumerian speech to a
concrete in-fiction origin — the U.R.U.K. origin-lab (see `project_sumerian_flagged` memory, marked
RESOLVED). This is real source material for that thread if it's ever revisited in depth.

---

## Linux (10 files)

- **Basic Linux Terminal Tips and Tricks** (EPUB) — re-cataloged via `unzip`/`nav.xhtml`. 17 chapters: Linux
  Primer; File/Folder Navigation; History and Shortcuts; Scripts and Pipes; Using SSH; File Transfer;
  Network Scanning; System Monitoring; Hardware Details and /dev; Parsing Text; systemd; Vim; Emacs;
  Configure Bash; Tmux Workflow; Terminal Tools for Images/Videos; Extras.
- **Essential Linux Commands** — Paul Olushile (2023, Packt). 13 chapters across 4 parts: Part 1 Server
  Installations and Management Commands (Getting a CentOS Server Running; Linux User and Group Commands;
  File Compression and Archival Commands); Part 2 Frequently Used Commands I (Format and Disk Space; Linux
  Permissions; Filesystem Mount and Manipulation); Part 3 Frequently Used Commands II (File Content and
  Conversion; SWAP; Monitoring and Debugging; IPTABLES and Network Commands; File Transfer/Downloading/Log
  Files); Part 4 Linux Security and the Cloud (Exploring Linux Security; Linux in the Cloud — AWS EC2).
- **Linux Driver Development with Raspberry Pi: Practical Labs** — Alberto Liberal (2021). Hands-on kernel
  driver course: Preface; Ch.1 Building the System (bootloader, kernel, root filesystem, boot process,
  building an embedded Linux system for the Raspberry Pi); Ch.2 The Linux Device and Driver Model (bus/device
  drivers, sysfs, kobject infrastructure, Device Tree intro); Ch.3 The Simplest Drivers (hello-world module
  labs); Ch.4 Character Drivers; Ch.5 Platform Drivers (GPIO, pin control, Device Tree, RGB LED labs);
  Ch.6 I2C Client Drivers; Ch.7 Handling Interrupts in Device Drivers (IRQ domains, softirqs, tasklets,
  workqueues, kernel threads) — continues with further labs beyond what was captured.
- **Linux Shell Programming: Pocket Primer** — Oswald Campesato (2023, Mercury Learning). 10 chapters:
  Introduction (bash basics, `ls`/`cat`/pipes, environment variables); Files and Directories; Useful Commands
  (`join`, `sort`, `tr`, `find`, `tar`, IFS); Conditional Logic and Loops; Filtering Data with `grep`;
  Transforming Data with `sed`; Doing Everything Else with `awk`; Introduction to Shell Scripts and
  Functions; Shell Scripts with `grep` and `awk`; Miscellaneous Shell Scripts.
- **Mastering Linux Administration** — (2nd ed., Packt). Large reference spanning at least 4 parts:
  Part 1 Basic Linux Administration (Installing Linux; The Linux Shell and Filesystem; Software Management;
  Managing Users and Groups; Processes/Daemons/Signals); Part 2 Advanced Linux Administration (Disks and
  Filesystems incl. LVM; Networking incl. OSI/TCP-IP; Linux Shell Scripting; Securing Linux — SELinux,
  AppArmor, firewalls/nftables; Disaster Recovery, Diagnostics, and Troubleshooting); Part 3 Server
  Administration (Virtual Machines/KVM; Managing Containers with Docker; Configuring Linux Servers — SSH,
  DNS, DHCP, NFS, Samba); Part 4 Cloud Administration (begins with "Short Introduction to Cloud Computing").
- **System Programming in Linux** — (No Starch Press). 19 chapters: Core Concepts; Fundamentals of System
  Programming; Time, Dates, and Locales; Basic Concepts of File I/O; File I/O and Login Accounting; Overview
  of Filesystems and Files; The Directory Hierarchy; Introduction to Signals; Timers and Sleep Functions;
  Process Fundamentals; Process Creation and Termination; Introduction to Interprocess Communication; Pipes
  and FIFOs; Client-Server Applications and Daemons; Introduction to Threads; Thread Synchronization;
  Alternative Methods of I/O; Terminals and Terminal I/O; Interactive Programming and the ncurses Library.
- **The Embedded Linux Security Handbook** — (Packt). 3+ parts: Part 1 Introduction to Embedded Systems and
  Secure Design (Ch.1 Welcome to the Cyber Security Landscape; Ch.2 Security Starts at the Design Table —
  target buyer/user, compliance standards across healthcare/financial/retail/government sectors; Ch.3 & 4
  Applying Design Requirements Criteria — hardware selection, then operating system selection); Part 2
  Design Components (chapters 5-7, incl. security scanning/testing and building a UI); Part 3 The Build
  Chain, Appliance Lifecycle, and Continuous Improvement (chapters 11-12, incl. networking confirmation).
- **The Linux DevOps Handbook** — (Packt). 3 parts: Part 1 Linux Basics (Choosing the Right Linux
  Distribution; Command-Line Basics; Intermediate Linux — cron/systemd timers, package management across
  distros, user/SSH management; Automating with Shell Scripts); Part 2 Your Day-to-Day DevOps Tools
  (Managing Services in Linux — systemd, OpenRC, SysV init, Upstart); Part 3 DevOps Cloud Toolkit.
- **The Linux Memory Manager** — Lorenzo Stoakes (2025, No Starch Press, Early Access/in-progress edition,
  1300 pages). Full brief contents: Ch.1 Introduction; Ch.2 Physical Memory; Ch.3 Virtual Memory; Ch.4
  Process Memory; Ch.5 Memory Mapping; Ch.6 Page Faults; Ch.7 Reverse Mappings; Ch.8 Manipulating Userland
  Memory; Ch.9 The Page Cache; Ch.10 Writeback; Ch.11 Reclaim and Memory Pressure; Ch.12 Swap Memory; Ch.13
  The Out Of Memory (OOM) Killer; Ch.14 Practical Memory Management. A deep, single-subsystem deep-dive
  rather than a general admin reference.
- **Ubuntu System Administration Guide** — 13 chapters: Getting Familiar with the Ubuntu Ecosystem; Install/
  Upgrade/Configure Ubuntu Desktop; Environments and Window Managers (i3, custom shortcuts, dev tools);
  Setting up Firewall/VPN/Wi-Fi Networks; Preparing a Virtualization Environment; Up and Running with
  Kubernetes; Install Ubuntu Server on Metal/Cloud/Network; Keeping [the system updated/secure — title
  truncated in extraction]; Setup Advanced Network/Firewall/VPN Servers; Running a Virtualization Server
  Environment; Setup Webserver, Deploy and Run Webapps; [Ch.12 not captured]; Task Automations, CI/CD
  Pipeline, and Service Deployment.

---

## Not yet touched this pass

The following folders under `Reference/Materials/books/` were not surveyed in this cataloging pass at all:
`Math_and_Computation/` (161 files — deliberately deferred by the developer 2026-07-23, expected to be
large: "we'll need to set aside Math_and_Computation/ for some other time, because that will probably eat
up the rest of my allotment"), `Cpp/`, and the loose
top-level singles (`Evolutionary Psychology and Information Systems Research.pdf`, `Human Universals -
Donald E Brown`, `King-Warrior-Magician-Lover` — **partially mined 2026-08-29, see its own section below**, `Mythology - Matt Clayton`, `Some of the Dead Are Still
Breathing`, `sound_travelling_through_bone...`, `The Art of Character`, `The History of Our Universe in 21
Stars`, `The Routledge International Handbook of Dialectical Thinking`). Flag for a future pass if the
developer wants them included.

## King, Warrior, Magician, Lover — Robert Moore & Douglas Gillette (1990) — partially mined 2026-08-29

Reached for while building the district Review Panel, on the understanding that it had already been extracted.
**It had not** — it sat on the uncataloged list above with only its filename recorded. The PDF in
`Reference/Materials/books/` is an **image-only scan with zero extractable text** (`pdftotext` returns 0 words),
so it was read visually, targeted by chapter.

**Mined:** the four archetypal faculties and their **active-passive bipolar shadow** structure, which the book
states is uniform across all four — **King** (shadows: the Tyrant / the Weakling), **Warrior** (the Sadist / the
Masochist), **Magician** (the Manipulator / the Denying "Innocent" One), **Lover** (the Addict / the Impotent
Lover) — with sourced characterizations of each pole. Book pp. 60-67, 88-91, 108-111, 132-139. Captured in full
and in active use as a QA panel at
`Worldspace/Locations-and-Levels/Concordia-City/Districts/Phase_Instructions/00f_Review_Panel.md` §4b.

**Part I mined 2026-08-29 in a second pass**, completing the taxonomy. The four **immature precursors** and
their bipolar shadows, on the identical active-passive structure — **Divine Child** → King (High Chair Tyrant /
Weakling Prince), **Precocious Child** → Magician (Know-It-All Trickster / Dummy), **Oedipal Child** → Lover
(Mama's Boy / Dreamer), **Hero** → Warrior (Grandstander Bully / Coward). The complete sixteen-name system is in
the book's Figure 1 (pp. 16-17). Also captured: the developmental order, the **bipolar switching mechanic** (a
psyche possessed by one pole slides or jumps to the other), the pyramid-over-pyramid model of the Self, and the
Maya principle that boyhood structures are **built over rather than demolished** and keep generating. Two
corrections to the first pass came out of Figure 1: the Magician's active shadow is the *Detached* Manipulator
and the Lover's is the *Addicted* Lover.

**Conclusion checked and partly mined 2026-08-29 — third pass. This book is now finished for this project's
purposes.** Roughly the first half is usable and is concentrated in the "Techniques → Active Imagination
Dialogue" section: the **board-meeting framing** of a structured internal dialogue among differentiated
positions (a striking independent convergence with the Review Panel's own mechanism), the **Ego-as-referee
method** for adjudicating two positions that are *"both right, but both excessive"*, the discipline of writing
each voice **uncensored before deciding it**, the sharpening that one must ask **how** a shadow manifests rather
than **whether** it does, and the **persecutor stop-rule** (if the dialogue turns purely hostile, stop and
invoke a positive form first). Also one design insight — shadow forms *"really want… to be noticed, honored,
and taken seriously,"* and stop acting out once they are — and one worldbuilding line (p. 144) listing what a
civilization calls the four faculties on to do.

**Checked and deliberately not taken:** the other three techniques — **Invocation**, **Admiring Men**, and
**Acting "As If"** — are personal-development practices for an individual accessing his own psyche and do not
transfer to reviewing a place. The closing **"A Final Word"** is a polemic on contemporary gender politics and
carries no method. **Chapter 1** ("The Crisis in Masculine Ritual Process") remains unread and is not expected
to yield taxonomy or method beyond what Chapters 2-4 already gave.

**Framing note for downstream use:** the book presents these as archetypes of *the mature masculine*. In the
Review Panel they are used as **diagnostic axes for a place** — order, action, knowledge, connection — not as
claims about gender, and are not written as gendered when applied.

(`Memetics/` — 14 files — **was** covered, flagged 2026-07-20 by the developer as directly relevant to the
Cryptograph Helix novel series alongside DNA computing; see its own section below.)

## Memetics (14 files) — flagged as Cryptograph Helix 2nd-level topic matter

**Developer's direct words, 2026-07-20:** "DNA Computation literally is the foundational basis for the
entire Cryptograph Helix series, plus everything in the Memetics/ level is additionally a 2nd-level topic
matter for the Cryptograph Helix series." Cataloged in the same pass as the STEM/Biology sweep.

- **Consciousness: A Very Short Introduction** — Susan Blackmore (2005, Oxford VSI series). Why the
  mystery, the human brain, time and space, "a grand illusion," the self, conscious will, altered states,
  the evolution of consciousness.
- **Consciousness Explained** — Daniel C. Dennett (1991/1992). Part I Problems/Methods (explaining
  consciousness, phenomenology); Part II An Empirical Theory of Mind (Multiple Drafts vs. the "Cartesian
  Theater," time/experience, evolution of consciousness, "how words do things with us," architecture of
  the human mind); Part III Philosophical Problems (qualia, reality of selves).
- **Conversations on Consciousness** — Susan Blackmore (2006). Interviews with 20 leading consciousness
  researchers (Chalmers, Crick, Dennett, Penrose, Ramachandran, Searle, et al.).
- **Genes, Memes, Culture, and Mental Illness: Toward an Integrative Model** — Hoyle Leigh, MD (2010).
  Explicit "genetic-memetic model" of mental illness, memes' storage/evolution in the brain and external
  storage in culture/media/cyberspace, memetic-epigenetic diagnosis of psychiatric conditions.
- **Information Warfare: The Meme is the Embryo of the Narrative Illusion** — James Scott (2018/2019,
  Institute for Critical Infrastructure Technology). Digital influence operations, memetic theory/lifecycle,
  cognitive-bias-based audience targeting, guerilla information-warfare tools/techniques, named state
  threat actors (China's "Three Warfares," Russia's "Digital Maskirovka").
- **Maps and Memes: Redrawing Culture, Place, and Identity in Indigenous Communities** — Gwilym Lucas Eades
  (2015) — re-cataloged 2026-07-23. Part of the McGill-Queen's Native and Northern Series. 9 chapters: The
  Long Walk; Place-Memes: Indigeneity, Identity, and Performance; Cree Ethnogeography; Canada, Cartography,
  and Indigenous Peoples; Counter-Mapping Colonization; The Evolution of Critical Cartographic Inscription;
  Commemorative Toponymies of Trauma; Meme Maps; Towards an Indigenous Geoweb.
- **Memes of Translation: The Spread of Ideas in Translation Theory** — Andrew Chesterman (1997). Memes as
  "survival machines," evolution of translation memes, memes-to-norms, translation strategies/ethics.
- **The Electric Meme: A New Theory of How We Think** — Robert Aunger (2002). A special kind of
  inheritance, "the replicator zoo," memes as a state of mind, "escape from Planet Brain," the "techno-
  tango," rethinking replication.
- **The Meme Machine** — Susan Blackmore (1999), foreword Richard Dawkins. Universal Darwinism, evolution
  of culture, the "meme's eye view," the origins of language, meme-gene coevolution, religions as
  memeplexes, "into the Internet," the "ultimate memeplex."
- **The Selfish Gene**, 40th Anniversary Ed — Richard Dawkins (1976/2016). The seminal text: replicators,
  "immortal coils," the gene machine, Ch.11 "Memes: The New Replicators" (the coinage of "meme" itself),
  "the long reach of the gene."
- **The Selfish Meme: A Critical Reassessment** — Kate Distin (2005). "Cultural DNA," replication of
  complex culture, "memetic DNA," memes and the mind, science/religion/society through a memetic lens.
- **The World Made Meme: Public Conversations and Participatory Media** — Ryan M. Milner (2016/2017, MIT
  Press). Memetic logics/grammar/vernacular, race/gender/counterpublic contestation, pop/populism in public
  commentary — an internet-culture-era (rather than classical-biology-era) treatment of memetics.
- **Thought Contagion: How Belief Spreads Through Society** — Aaron Lynch (1996). "Self-sent message and
  mass belief," memetics and the social sciences, family-plan/sexually-transmitted/cult/health-related
  "thought contagions."
- **Virus of the Mind: The New Science of the Meme** — Richard Brodie (2009). Memes, mind/behavior,
  viruses, evolution, "sex: the root of all evolution," cultural viruses, the memetics of religion,
  "designer viruses (how to start a cult)," disinfection.
