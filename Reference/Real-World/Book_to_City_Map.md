# Book-to-City Map (subject-level) — November To-Do N-6

**Written 2026-10-21.** Screens the book library **by contents** (the full text of each book, not its title) against the
79 research topics in `City_and_District_Research_Topics.md` (Part 0 national topics and Part 2 city topics).
It replaces the old title-based mapping as a *starting list*; it does **not** replace reading.

> **Read this first — how much to trust it.** The screen counts where a topic's rare words and phrases occur in a book.
> It cannot tell whether a book *answers* the topic. I reviewed every topic's top results by hand: **11 topics have a
> book that is plainly on subject, 21 have a weak or adjacent lead, 38 matched words only (noise), and 9 have nothing
> at all.** A high score alone is not a good sign: the single highest score for Halley's relocatable-station topic is a
> mobile-phone-network textbook ("mobile station"). The tiers below are my judgment after seeing the evidence words.
>
> **Why so thin:** about 1,765 of the 2,308 files are science, computing and mathematics. The library has almost nothing
> on Antarctic stations, polar engineering, or most of the sociology the topics ask for. **The real per-city source for
> nearly every topic remains the web research in ULM Step 3.** This map is for the handful of cases where a book helps.
>
> **Subject-level only.** Which *chapters* serve a given city depends on that city's Step 2 deficits, which do not exist
> yet. Re-run the screen per city after Step 2 (`Tools/map_books_to_topics.py`), against that city's own deficits.

## 1. Worth opening (11 topics)

- **NATIONAL N1** (topics file line 54) — WASTE TREATMENT
  - Life Cycle Assessment and Irrigation & Drainage Engineering are on subject (waste treatment as engineering). Environmental Science Demystified is already extracted.
  - 2.82 · Life Cycle Assessment - [] · {waste treatment ×58, waste ×813, treatment ×372}
  - 2.79 · Irrigation and Drainage Engineering - [] · {waste treatment ×21, waste ×191, treatment ×96}
  - 2.57 · Environmental Science Demystified (Linda Williams) (z-lib.org) · {waste treatment ×4, waste ×209, treatment ×61}
- **NATIONAL N1** (topics file line 58) — Subjects worth sourcing for `N1` when it is picked up (a wish list, not a plan): closed-loop and zero-export waste systems · thermal treatment and wha…
  - Both supply-chain texts discuss closed-loop systems and sourcing at length.
  - 7.38 · Sustainable Supply Chains - [] · {sourcing ×56, closed-loop ×64, energy cost ×3, waste ×212}
  - 6.11 · Environmental Science Demystified (Linda Williams) (z-lib.org) · {energy cost ×2, waste ×209, trade ×29, thermal ×30}
  - 6.05 · Global Supply Chain and Operations Management - (2nd Ed) [] · {sourcing ×217, closed-loop ×5, constraint ×48, handling ×42}
- **Troll** (topics file line 200) — Intermodal freight logistics engineering
  - Both supply-chain texts cover freight and intermodal logistics.
  - 3.88 · Sustainable Supply Chains - [] · {logistics ×260, freight ×67, intermodal ×16, engineering ×35}
  - 3.22 · Global Supply Chain and Operations Management - (2nd Ed) [] · {logistics ×196, freight ×15, intermodal ×5, engineering ×40}
  - 1.38 · Fundamentals of Business Process Management - (2nd Ed) [] · {freight ×7, logistics ×11, engineering ×24}
- **Contrapunto (formerly Sejong)** (topics file line 236) — Translation-driven settlement growth — inherited records in one language and newcomers speaking another draw translators, who draw their own networks…
  - Memes of Translation is wholly about translators and how ideas spread across languages.
  - 3.97 · Memes of Translation - The spread of ideas in translation theory - Andrew Chesterman [1997] · {translators ×247, language ×241, networks ×5, speaking ×11}
  - 2.76 · Forensic DNA Biology-- a Laboratory Manual - Elkins, Kelly M. [2012] · {another draw ×2, inherited ×10, draw ×9, growth ×2}
  - 2.38 · Ancestral Dna, Human Origins, and Migrations - Rene J Herrera [2018] · {settlement ×141, newcomers ×3, inherited ×19, records ×16}
- **Mirny** (topics file line 248) — Katabatic wind engineering — the real Mirny Station is a famously wind-battered site, worth researching directly
  - Micrometeorology names katabatic flow directly (8 mentions) — a field text, not Antarctic-specific.
  - 4.88 · Micrometeorology_3rd_Edition_Thomas_Foken,_Matthias_Mauder_Z_Library · {katabatic wind ×3, katabatic ×8, wind ×598, station ×32}
  - 2.00 · The Manga Guide to Relativity - Hideo Nitta, Masafumi Yamamoto, Keita Takatsu (1st Ed) [2011] · {station ×43, wind ×13, engineering ×2}
  - 1.35 · Energy Harvesting and Energy Efficiency - [] · {wind ×334, station ×43, engineering ×109, site ×2}
- **Casey** (topics file line 254) — Highway logistics network design
  - Same two supply-chain texts (network design is a chapter-level subject in both).
  - 7.21 · Sustainable Supply Chains - [] · {logistics network ×14, network design ×36, logistics ×260, highway ×4}
  - 7.14 · Global Supply Chain and Operations Management - (2nd Ed) [] · {network design ×74, logistics network ×6, logistics ×196, network ×257}
  - 5.32 · Introduction to Digital Systems Design - [] · {network design ×42, network ×454, design ×252}
- **Shirayuki** (topics file line 269) — Postcolonial identity reclamation — communities reclaiming an externally-imposed founding myth as genuinely their own
  - Three books on postcolonial / founding-myth identity: Maps and Memes, Born in Blood and Fire, A Brief History of Korea.
  - 3.89 · A-Brief-History-Of-Korea · {founding myth ×4, founding ×26, myth ×24, communities ×3}
  - 3.80 · Maps and memes - redrawing culture, place, and identity in indigenous communities - Eades, Gwilym Lucas [2015] EPUB · {postcolonial ×10, reclamation ×9, communities ×99, myth ×2}
  - 3.41 · Born in Blood and Fire - A Concise History of Latin America (4th Ed) [2016] · {postcolonial ×65, founding ×4, communities ×14, genuinely ×2}
- **Vostok** (topics file line 279) — Subglacial lake science — the real Lake Vostok is one of the most-studied subglacial lakes on Earth, extremely rich source material (extremophile biol…
  - Hydrothermal Processes and Mineral Systems mentions Lake Vostok and subglacial lakes by name (9 and 7 mentions) — the only book in the library that does.
  - 6.96 · Hydrothermal Processes and Mineral Systems (Franco Pirajno (auth.)) (z-lib.org) · {lake vostok ×9, subglacial lake ×4, subglacial lakes ×3, vostok ×10}
  - 3.73 · Food Analysis Laboratory Manual - (3rd Ed) [] · {source material ×26, science ×109, extremely ×18, source ×16}
  - 3.44 · Geochemistry An Introduction (Albarede F.) (z-lib.org) · {source material ×3, vostok ×3, lake ×24, earth ×321}
- **Zhongshan** (topics file line 286) — Cultural continuity and refinement (rather than change) over generations
  - Maps and Memes (cultural continuity across generations) is the best fit; the archaeology and ancestry texts are secondary.
  - 4.98 · Maps and memes - redrawing culture, place, and identity in indigenous communities - Eades, Gwilym Lucas [2015] EPUB · {cultural continuity ×9, cultural ×148, generations ×44, continuity ×29}
  - 2.78 · Handbook of Evolutionary Research in Archaeology - [] · {cultural continuity ×4, cultural ×1553, refinement ×6, generations ×42}
  - 2.36 · Ancestral Dna, Human Origins, and Migrations - Rene J Herrera [2018] · {cultural continuity ×3, cultural ×141, continuity ×47, refinement ×4}
- **Dome Fuji** (topics file line 332) — Sacralization of scientific/technical sites — real literature on research sites becoming pilgrimage destinations
  - A New History of Shinto discusses pilgrimage sites at length (22 mentions).
  - 2.15 · Travel Marketing, Tourism Economics and the Airline Product - [] · {destinations ×74, sites ×17, technical ×16, becoming ×10}
  - 2.05 · A-New-History-of-Shinto-Blackwell-Brief-Histories-of-Religion- · {pilgrimage ×22, sites ×47, technical ×3, scientific ×2}
  - 1.87 · Guide to Scientific Computing in C++ - (2nd Ed) [] · {destinations ×41, scientific ×81, technical ×4}
- **Byrd** (topics file line 344) — Heavy industrial robotics fabrication from raw materials
  - Robotics (2nd Ed) has a real industrial-robotics section; the Franceschetti text is broader.
  - 8.29 · Robotics - (2nd Ed) [] · {industrial robotics ×12, robotics ×91, industrial ×90, materials ×10}
  - 2.33 · Principles of Robotics & Artificial Intelligence - Donald R. Franceschetti [2018] · {robotics ×505, industrial ×70, fabrication ×3, materials ×126}
  - 1.84 · The Butcher's Guide to Well-Raised Meat-- How to Buy, Cut, and Cook Great Beef, Lamb, Pork, Poultry, and More - Joshua Applestone, Jessica Applestone, Alexandra Zissu · {fabrication ×20, industrial ×10, heavy ×7, materials ×3}

## 2. Weak or adjacent leads (21 topics) — open only if web research comes up short

- **Halley** (topics file line 163) — Relocatable/mobile station architecture — real precedent already exists (the actual Halley VI station moves on skis) and is worth researching directly
  - 5.80 · Principles of Mobile Communication - (4th Ed) [] · {mobile station ×69, station ×120, mobile ×298, architecture ×34}
  - 1.44 · Structural Geological Atlas (Soumyajit Mukherjee, Narayan Bose etc.) (z-lib.org) · {station ×15, mobile ×5, architecture ×3, exists ×2}
- **Halley** (topics file line 165) — Ice shelf glaciology — why a station needs to move at all
  - 2.25 · Environmental Science Demystified (Linda Williams) (z-lib.org) · {glaciology ×4, shelf ×30, station ×5, move ×37}
  - 1.70 · 2024_WATER_SURVIVAL_HANDBOOK_Ultimate_Guide_to_Water_Security,_Filtration · {shelf ×5, station ×2, needs ×28, move ×3}
- **Belgrano** (topics file line 174) — Post-military-base economic decline — company-town literature on bases outliving their purpose
  - 2.15 · Born in Blood and Fire - A Concise History of Latin America (4th Ed) [2016] · {economic decline ×2, economic ×129, decline ×6, bases ×6}
  - 2.15 · Born-in-Blood-and-Fire-A-Concise-History-of-Latin-America-Fourth-Edition- · {economic decline ×2, economic ×129, decline ×6, bases ×6}
- **Belgrano** (topics file line 177) — Aircraft boneyards — real aviation industry practice, a literal existing parallel
  - 6.34 · Travel Marketing, Tourism Economics and the Airline Product - [] · {aviation industry ×6, aircraft ×224, aviation ×17, industry ×125}
  - 4.88 · Principles of Microeconomics - [] · {aviation industry ×11, aviation ×14, industry ×67, aircraft ×4}
- **Lazar** (topics file line 180) — Urban agglomeration / city-merger studies — how two settlements become one metro area
  - 3.11 · Disability and Vocational Rehabilitation in Rural Settings - [] · {metro area ×10, metro ×13, urban ×754, settlements ×4}
  - 2.31 · Research Methods for the Digital Humanities - [] · {metro area ×2, metro ×2, urban ×3, area ×27}
- **Lazar** (topics file line 181) — Unplanned megacity growth dynamics
  - 3.66 · System Dynamics - [] · {growth dynamics ×5, dynamics ×416, growth ×163}
  - 1.07 · Graphene Science Handbook [Vol 5] - Size-Dependent Properties · {growth dynamics ×3, dynamics ×98, growth ×696}
- **Neumayer** (topics file line 184) — Structural engineering on shifting ice shelves — the real Neumayer III station uses a hydraulic platform system for exactly this, a direct real-world…
  - 6.21 · Fundamentals of Structural Engineering - (2nd Ed) [] · {structural engineering ×80, engineering ×127, structural ×342, shifting ×6}
  - 3.24 · The A-Z of the PhD Trajectory - [] · {structural engineering ×12, platform ×12, engineering ×26, structural ×24}
- **Esperanza** (topics file line 206) — Child development in isolated institutional settings
  - 2.73 · Natural Conflict Resolution - Filippo Aureli, Frans De Waal (1st Ed) [2001] · {child development ×49, child ×142, settings ×19, development ×282}
  - 2.68 · Why Chimpanzees Can’t Learn Language And Only Humans Can - Herbert S. Terrace [2019] · {child development ×6, child ×63, settings ×2, development ×50}
- **Pergamino (formerly Juan Carlos)** (topics file line 211) — History of census/vital-records systems and their political weight
  - 1.73 · Philosophy of Race - Naomi Zack [] · {census ×52, political ×124, weight ×5}
  - 1.62 · Economic Facts and Fallacies - Thomas Sowell (2nd Ed) [2011] · {census ×65, political ×36, weight ×3}
- **Palmer City** (topics file line 222) — Hedonic/pleasure-city urban planning history
  - 3.70 · Sustainability Science - [] · {urban planning ×11, urban ×105, planning ×71}
  - 2.98 · Micrometeorology_3rd_Edition_Thomas_Foken,_Matthias_Mauder_Z_Library · {urban planning ×5, urban ×98, planning ×17}
- **Port Lockroy** (topics file line 227) — Heritage preservation and adaptive reuse of former military sites — the real Port Lockroy is itself an actual preserved historic site/museum/post offi…
  - 6.84 · A-Brief-History-Of-Korea · {historic site ×2, post office ×2, military ×248, heritage ×18}
  - 5.27 · Research Methods for the Digital Humanities - [] · {museum ×180, heritage ×108, preservation ×89, reuse ×18}
- **Davis** (topics file line 257) — Controlled-environment/greenhouse agriculture in extreme climates — real Antarctic/Arctic greenhouse research is directly and immediately relevant giv…
  - 6.95 · Environmental Science Demystified (Linda Williams) (z-lib.org) · {extreme climates ×3, greenhouse ×121, antarctic ×17, arctic ×32}
  - 3.70 · The Making of the Fittest DNA and the Ultimate Forensic Record of Evolution - Sean B. Carroll [2007] · {antarctic ×57, arctic ×16, agriculture ×15, extreme ×8}
- **Davis** (topics file line 259) — Limnology and lake-sediment paleoclimate reconstruction — ties directly to Davis's own established lake-science research culture
  - 1.94 · Paleogenomics Genome-Scale Analysis of Ancient DNA - Charlotte Lindqvist, Om P. Rajora (1st Ed) [2019] · {paleoclimate ×2, limnology ×2, reconstruction ×34, davis ×11}
  - 1.72 · DNA Barcoding and Molecular Phylogeny - Subrata Trivedi, Hasibur Rehman, Shalini Saggu, Chellasamy Panneerselvam, Sankar K. Ghosh (1st Ed) [2018] · {limnology ×6, reconstruction ×10, davis ×6, culture ×22}
- **Shirayuki** (topics file line 271) — Textile/fashion arts history tied to research and education culture
  - 2.22 · Taiko-boom-Japanese-drumming-in-place-and-motion · {arts ×201, culture ×165, education ×62, tied ×6}
  - 2.12 · A-Brief-History-of-Mexico-4th-Edition · {textile ×10, arts ×5, education ×66, culture ×47}
- **Sinheung** (topics file line 274) — Large-scale advanced/additive manufacturing systems
  - 4.58 · Global Supply Chain and Operations Management - (2nd Ed) [] · {additive manufacturing ×15, manufacturing ×269, additive ×20, large-scale ×4}
  - 1.26 · DNA Vaccines Methods and Protocols - Mark W. Saltzman (2nd Ed) [2006] · {manufacturing ×35, large-scale ×28, additive ×2, advanced ×5}
- **Sinheung** (topics file line 275) — Sociology of communities that existed before being formally named (statelessness/undocumented community literature)
  - 1.32 · Maps and memes - redrawing culture, place, and identity in indigenous communities - Eades, Gwilym Lucas [2015] EPUB · {communities ×99, existed ×9, named ×52}
  - 1.20 · The-History-of-Mexico · {existed ×21, communities ×12, formally ×3, named ×19}
- **Dumont d'Urville** (topics file line 307) — Human-wildlife coexistence urban planning — the real station routes infrastructure around penguin colonies already
  - 5.15 · Sustainability Science - [] · {urban planning ×11, urban ×105, infrastructure ×18, planning ×71}
  - 3.65 · Micrometeorology_3rd_Edition_Thomas_Foken,_Matthias_Mauder_Z_Library · {urban planning ×5, urban ×98, station ×32, planning ×17}
- **Scott** (topics file line 316) — Preserved historic polar huts — the real Scott/Terra Nova hut is an actual heritage site, direct existing parallel
  - 4.41 · A-Brief-History-Of-Korea · {heritage site ×10, heritage ×18, historic ×11, site ×17}
  - 3.41 · Research Methods for the Digital Humanities - [] · {heritage site ×2, heritage ×108, historic ×5, preserved ×9}
- **Mawson** (topics file line 328) — Founder-population demographic drift and replacement sociology
  - 1.39 · Ecology, Genetics, and Evolution of Metapopulations - Ilkka A. Hanski, Oscar E. Gaggiotti (1st Ed) [2004] · {demographic ×207, drift ×126, replacement ×8}
  - 1.32 · Paleogenomics Genome-Scale Analysis of Ancient DNA - Charlotte Lindqvist, Om P. Rajora (1st Ed) [2019] · {demographic ×80, drift ×17, replacement ×13}
- **Dome Fuji** (topics file line 331) — Real Dome Fuji ice-core science — deep ice-core drilling and paleoclimate records, rich source material
  - 3.69 · Food Analysis Laboratory Manual - (3rd Ed) [] · {source material ×26, science ×109, deep ×2, source ×16}
  - 3.23 · Exploration Geophysics (Mamdouh R. Gadallah, Ray Fisher (auth.)) (z-lib.org) · {drilling ×48, dome ×6, records ×47, deep ×28}
- **Temirötkel (formerly Sayowa)** (topics file line 337) — Island-junction logistics — East Ongul Island's sea-ice and overland access to the mainland
  - 2.58 · Global Supply Chain and Operations Management - (2nd Ed) [] · {logistics ×196, mainland ×9, island ×22, east ×18}
  - 2.21 · Ancestral Dna, Human Origins, and Migrations - Rene J Herrera [2018] · {mainland ×29, overland ×3, island ×152, east ×727}

## 3. Noise — the scorer matched words, not the subject (38 topics; no book recommended)

For these, the top-scoring books are generic hits (e.g., an EU-law text for the Antarctic Treaty, gorilla memoirs for Mount Erebus, a Siberian survival story for Cape Adare and Cape Denison, a relativity manga for the space elevator). Treat these topics as **no book**.

- [Halley] Political science of figurehead/ceremonial authority
- [Santa Luce (formerly Abowasa)] Binational/co-founded settlement history — condominium territories, jointly-administered towns
- [Santa Luce] Consociational power-sharing governance models
- [Santa Luce] Intercultural neighborhood sociology at the household level
- [Belgrano] Rediscovered discipline — newcomers reviving an institution's practices from its surviving records, logs and m
- [Neumayer] Sociology and history of precision/metrology-obsessed institutions
- [Princess Elisabeth] Zero-emission/passive Antarctic architecture — the real Princess Elisabeth Antarctica station is literally a z
- [Utstein (formerly Princess Elisabeth)] Reliability engineering — single points of failure in fragile systems
- [Sanay] Port/harbor engineering on bedrock vs. ice foundations
- [Troll] Strategic literature on contested transport chokepoints
- [Esperanza] Company-town / rotational (FIFO) labor sociology
- [Esperanza] The real Esperanza Base is the only Antarctic settlement with children actually born there — worth pulling rea
- [Marambio] Strategic vulnerability of small, concentrated islands
- [Palmer City] Historiography of single inciting incidents that trigger wars (comparable to WWI assassination literature)
- [Puerto Abrigo (formerly Port Lockroy)] Postal service logistics history
- [Rothera] Distributed manufacturing and redundant factory siting
- [Rothera] Subterranean industrial architecture
- [Contrapunto] Cohabitation sociology in crowded, multi-national settings
- [Signy] Cold-climate bridge engineering
- [Davis] History of genuinely multi-disciplinary research institutions
- [Kunlun] High-altitude, extreme-cold engineering — the real Kunlun Station is China's highest Antarctic station
- [Kunlun] Post-national community formation — craft-guild/professional-identity sociology as a substitute for national i
- [Ariun Nuur (formerly Vostok)] Extremophile biology — life in extreme cold, sealed ecosystems
- [Ariun Nuur] Communities built around inherited records — living with logs, journals and maps left by people they never met
- [Janbogo] Katabatic-wind-resistant shielded architecture
- [Cape Adare] Real Cape Adare/Borchgrevink expedition history — the actual first overwintering site in Antarctica
- [Cape Adare] Adélie penguin colony ecology — Cape Adare hosts one of the largest real colonies on the continent
- [Cape Adare] Acoustic/community music culture
- [Denison] Extreme wind engineering — the real Cape Denison is the windiest place at sea level on Earth (Mawson's origina
- [Denison] Fused megastructure architecture for extreme climates
- [Dumont d'Urville] Small-island siting and sea-ice access on the Adélie coast — the real Petrel Island site's physical conditions
- [Fort McMurdo] Active-volcano hazard engineering and civil defense — Mt. Erebus is a real, active volcano near the real McMur
- [Fort McMurdo] Political geography of informal-to-formal capital transitions
- [Mawson] The real site's physical conditions at Mawson's coordinates — terrain, wind, sea-ice access
- [Temirötkel] Crossroads/waystation town sociology
- [Byrd] Subterranean/under-ice city engineering
- [Amundsen-Scott Station] Antarctic Treaty neutrality as a governance model — the treaty's own provisions, not any station's operating h
- [Amundsen-Scott Station] Space elevator / space-fountain engineering theory — directly ties to the existing Amundsen Tower project note

## 4. Gaps — no book above the bar (9 topics)

- [NATIONAL N2] THE MONEY SYSTEM
- [Neumayer] History-of-science literature on erased/uncredited contributors
- [Marambio] *(Antarctic paleoclimate/geology previously listed here as a research topic — struck per the developer's own correction
- [Signy] Remote-island supply-chain fragility and logistics
- [Mirny] Industrial-yard fortification and windbreak architecture
- [Casey] Truck-stop / waystation sociology — "non-place" transient culture literature (ties to Hub above)
- [Zhongshan] Buffer-state / small-power-between-two-larger-neighbors geopolitics
- [Scott] Small-town-next-to-metropolis sociology
- [Zukelli] Sister-city/twin-settlement sociology

## 5. Topics not scored — later-era wording (6)

Their own wording describes a war, ruin or destruction, so they sit outside the Second Interwar default scope.

- [Sanay] (line 196) Real case studies of port cities surviving wartime due to geographic/geological advantage
- [Pergamino] (line 212) Real historical cases of record-keeping institutions destroyed specifically to erase what they held
- [Janbogo] (line 291) Survivor's-guilt / witness-community trauma — real literature on communities that survive while neighbors are
- [Zukelli] (line 321) Sanctuary-town history — real case studies of towns destroyed/punished for harboring refugees
- [Byrd] (line 343) Single-supply-corridor logistics vulnerability — real besieged-city/lifeline-route history
- [Amundsen-Scott Station] (line 350) Network topology and articulation points — Amundsen Station being the single node connecting all six subnets,

## 6. Image-only books (36) — no text layer, so the screen could not see them
These need OCR before they can be screened. Most are physics/music/Sowell/Schopenhauer; none is likely to serve a city topic. Two (*Human Universals*, *King-Warrior-Magician-Lover*) are already extracted in this repo from another route. The list is in the scratchpad; regenerate with the extractor if wanted.

## 7. Cross-check against `Book_Extraction_Index.md`
- **Already extracted:** *Environmental Science Demystified* (own file; Davis greenhouse and glaciology topics). Do not re-mine for those topics.
- **Screened once, not mined:** *Micrometeorology*, *Exploration Geophysics* and *Hydrothermal Processes and Mineral Systems* were looked at inside the Davis geosciences folder as "general-purpose field texts" (Micrometeorology rated low). They were **not** read for Mirny's katabatic winds or Ariun Nuur's lake — the leads above are new uses.
- **Not in the index at all:** every other book named in section 1. None has been mined.
- The TOC master reference lists the Korea, Shinto, Latin America, Mexico, Sowell and *Maps and Memes* books (table of contents only); it has no entry for the supply-chain, robotics, life-cycle, translation or sustainability texts.

## 8. Method and limits
- 753 of 755 candidate books read (752 text files; 2 empty). Excluded as irrelevant: Cpp, Linux, Math_and_Computation, STEM/CSIT, STEM/math, STEM/algorithms, STEM/data science. **Say so if any should be screened.**
- Tool: `Universal_Location_Methodology/Tools/map_books_to_topics.py`; raw scores for all 79 topics (top 12 each) are in `Book_to_Topic_Scores_2026-10-21.json` beside this file.
- No chapter was read. Evidence words are counts, not findings.

