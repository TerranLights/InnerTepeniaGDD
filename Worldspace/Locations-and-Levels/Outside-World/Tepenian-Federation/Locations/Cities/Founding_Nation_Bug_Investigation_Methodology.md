# Founding-Nation Bug Investigation Methodology

**What this is:** the reusable playbook for the country-wide culture re-check flagged BLOCKING in
`TODO.md`, written up 2026-07-13 after resolving Zhongshan, Sinheung
(files: `Sinheung`), and Shirayuki. Apply this exact process to every remaining city on that checklist
— it was refined through several real course-corrections on the first two cities and should not
need to be re-derived from scratch again.

**The governing rule this all serves:** `TerranLights/TepenianUniverseTimeline`'s
`Reference/No_National_Stereotypes.md` — a Tepenian city's real-world founding nation is a GPS
coordinate only, never a cause. This document is the *investigation method* for finding violations
of that rule that survived the 2026-07-12 sweep because they're demographic/factual bugs, not
stereotype-language bugs — the sweep caught bad *prose* ("German rigor"); this process catches bad
*facts underneath correct-sounding prose*.

**The scale of time that makes this rule necessary, not just a style preference:** the Falkland
Treaty was signed **June 21, 2564.** William Shakespeare was born April 23, 1564. **We are, today,
closer to the birth of William Shakespeare than we are to the signing of the Falkland Treaty.**
Expecting a Tepenian city's present-day culture to still resemble its founding nation's real-world
stereotypes is exactly as implausible as expecting modern English culture to still resemble
Shakespeare's England just because Shakespeare was English. That much elapsed time makes a founding
nation pure geography — a GPS coordinate marking where something started, never a live causal force
on what a culture looks like on the far side of that gap.

**A sharper version, confirmed 2026-07-24: the founding generation itself had zero living connection, not
just present-day Tepenians.** Real-world Antarctic research stations mostly date to the International
Geophysical Year (1957-58); even the oldest continuously-run station (Argentina's Orcadas, 1904) is still
roughly 600-660 years short of the Falkland Treaty (2564). **The station's real-world national origin was
already ancient history on day one of Tepenia's own existence** — the 2564 exiles who actually signed the
treaty had no living connection to whichever national team built the station they arrived at, before a single
day of independent Tepenian culture had happened yet. **Direct consequence for this methodology:** a city's
own founding-history narrative should never read as if the real-world station's construction and Tepenia's
founding happened in causal or temporal proximity — the station sat as inert, centuries-old infrastructure
long before any exile ever arrived at it.

---

## 1. The three-way distinction (read this before touching any file)

Every claim that names a nationality in a city's culture write-up falls into exactly one of three
buckets. Sort it correctly before deciding whether it's a bug.

1. **Which nation built the physical station** (Progress Station/Russia, Bharati Station/India,
   Mario Zucchelli Station/Italy, etc.) — the true GPS coordinate. Tells you where the city is and
   who built the original infrastructure. **Never reliable evidence of who lives there now, and
   must never be treated as a cause of present-day culture.**
2. **The city's actual, current population composition** — its own Section 1 tier table
   (Primary/Significant/Notable), sourced from `Specs/[City].md`'s Population & Composition
   section. A real, tracked, load-bearing demographic fact. **This IS a legitimate cause of
   present-day culture.** If a city's population is genuinely, continuously a given nationality,
   "this practice is [nationality] because the people carrying it forward are [nationality]" is
   simply true, not a stereotype violation.
3. **Essentialist national temperament** ("German rigor," "Russian dusha," "Song Dynasty
   principles reflect an inherent Chinese sensibility") — attributing a fixed personality/aesthetic
   essence to a nationality and using the essence, rather than the population's own lived history,
   as the explanation. **Always banned, regardless of whether #2 matches.**

**The check, every time:** is this citing #1 (banned) or #2 (fine)? If a sentence explains *why*
something is true by pointing at a nationality, is that nationality doing the explanatory work
because of *what people actually did* (#2, fine) or because of *what nation founded/operated the
physical station* or *an assumed temperament* (#1/#3, banned)?

**A trap inside this trap, found while applying it:** it is possible to overcorrect from #1/#3 into
denying #2 — e.g. framing a population's own carried-forward tradition as "pure coincidence" or
insisting circumstance alone explains everything "regardless of who they were." That's wrong too.
If the population doing something really is that nationality, say so plainly; don't hedge it into
vagueness in the name of avoiding stereotypes. See `feedback_no_national_stereotypes` memory for
the full narrative of how this was caught (the Zhongshan "regardless of who they were" episode).

---

## 2. The 7-point generative framework (for writing/rewriting culture once the facts are sorted)

Once a causal claim is confirmed to belong in bucket #2, ground *how* the specific practice takes
its specific form using this sequence, in order:

1. **Physical circumstance, not national temperament** — terrain, climate, wind, altitude, let
   physical facts force behavior/architecture/social patterns directly.
2. **Inherited infrastructure as circumstance, not culture** — what kind of station the founders
   walked into hands them tools and an institutional shape, a starting condition.
3. **The problem this specific group had to solve together** — the load-bearing move. The causal
   agent is *this particular group, solving this particular problem*, never their nationality.
4. **Function within the wider network** — what a city actually does (industrial hub, aviation
   gateway, archive-keeper) shapes daily rhythm and civic pride independent of who founded it.
5. **Historical turning points as events, not heritage** — redistribution, the war, treaty-era
   decisions reshape a city over time.
6. **Comparative contrast between cities** — two cities differentiated by how they answer the same
   structural question differently, more interesting than either city just "being" a nationality.
7. **Real-world echo as flavor, applied last, never as the seed** — once a practice is established
   as independently developed (or continuously carried by bucket-#2 population), it's fine to note
   it resembles a real tradition, as a coincidence or continuity, never as the origin.

---

## 3. The specific bug class this pass hunts for

**A city's cultural narrative citing a real-world station's or a *neighboring* city's nationality
instead of its own current, established facts.** Concrete pattern, found three times so far:

- Zhongshan's founding story cited "proximity to the former Russian Progress Station" — but
  Progress Station is a *different city's* (Sinheung's) founding site, and
  that city's population was independently re-derived to Korean-Primary, not Russian.
- Sinheung's entire document assumed a "dual Russian-Korean founding" and
  that the founders chose the name "Soyuz" — neither true; the city is singularly Korean-founded via
  Jeju-do, and "Soyuz" was a leftover placeholder never chosen by anyone who actually lived there
  (the city was later officially named Sinheung, 2026-07-14).
- Shirayuki repeatedly paired "Chinese and Japanese" as joint cultural threads (cuisine, music,
  fashion, a proposed music genre) despite China being the *smallest* of its five Significant-tier
  nations — a stale assumption surviving from before a population correction, never swept.

**Three named sub-patterns to check for specifically, because each has now recurred:**

- **Unsupported tier annotations.** A tier table entry tagged "(founding wave)" or similar with
  *no supporting text anywhere in that city's own Founding Story section*. Found and removed twice
  (Australia in Sinheung, Russia in Shirayuki) — both were leftover labels
  whose own justification had quietly disappeared or never existed. **Always cross-check every
  tier-table annotation against the actual Founding Story prose, not just against itself.**
- **Stale demographic assumptions in creative-content sections.** Cuisine/Music/Fashion/Arts
  sections written before a population re-derivation, describing the *pre-correction* demographic
  leader, never updated when Section 1's table changed. Found in three different forms: a flatly
  wrong "Chinese as the demographic default" claim in a Korea-Primary city, a "second cultural
  pillar" claim in a singularly-founded city, and a "Chinese and Japanese" pairing in a
  Japan-Primary city where China is the smallest Significant nation. **Whenever a city's population
  table shows signs of having been re-derived (search for "corrected," "re-derived," "re-tiered" in
  Section 1's own notes), assume the creative-content sections were NOT swept at the same time and
  check them explicitly.**
- **Internal numerical contradictions between `Local_Cultures` and `Specs`.** Not a stale-draft or
  unsupported-annotation issue — a flat factual error, where `Local_Cultures/[Subnet]/[City].md`
  asserts a tier leader or ordering that directly contradicts `Specs/[City].md`'s own percentage
  table. Found in Casey: three places claimed "Japan (leads T2)," including in the reasoning for a
  live design decision (a companion's candidate origin city), when Casey's own Specs table shows
  South Korea leading and Japan actually the second-smallest of six Significant-tier nations. **This
  one isn't caught by reading Founding Story prose — it requires literally re-adding up or
  re-comparing the percentages in Specs against every ordering claim in Local_Cultures.** Also a
  reminder that not every flagged concern turns out to be a bug: Casey's separately-flagged
  "diffuseness tied to demographic breadth" was checked and confirmed legitimate (bucket #2,
  genuinely flat population, framed as "real, not weaker") — don't assume every item on the
  checklist needs a rewrite; some just need verification and a clean bill of health.
- **Methodology-level GPS violations — a real-world station-operator nationality leaking into the
  population *math itself*, not just into prose.** Deeper than the other three: those live in a
  city's own creative-content files; this one lives in the shared source-of-truth,
  `Upper_Earth_Immigration_Composition.md`. Found at Sejong: China sat co-Primary (19.88%) in that
  file's own Sejong section, justified as "both reach KGI via Pacific/Atlantic routes" — but China
  appears nowhere else in the Palmer subnet, the document's own timezone/distance filter was never
  actually applied to it, and the real cause was almost certainly King George Island's genuine
  real-world Great Wall Station — exactly the operator-identity reasoning this document's own stated
  rule excludes ("Cities are analyzed as if ownership is irrelevant"). **When investigating a city,
  don't stop at that city's own files — check whether the master population-methodology file's
  entry for it actually obeys its own stated exclusion rules, especially for any nation that (a)
  appears in only one city and (b) traces to a real-world station on that city's exact site.**
  Fixing this required a full recalculation (proportional rescaling of the remaining nations, factor
  = 100/(100-removed%)), re-verified to sum to exactly 100%, propagated across every layer (Specs,
  Local_Cultures, all Megasheet files including README.md, and the master composition file itself)
  — the widest-blast-radius fix of any city on this checklist so far. Also surfaced a **downstream
  discovery**, not itself part of this bug class: fixing one number in the master file can leave
  *other, unrelated* prose in that same file stale (Sejong's removal exposed a separate, pre-existing
  "Sejong is the largest Tepenian city" claim that already conflicted with the developer's own Lazar
  population rebalancing work) — flag findings like this rather than silently fixing them; they're
  a different, wider staleness problem than the one this checklist targets.
- **A sibling of the operator-nationality violation: a historical *person's* nationality leaking into
  the population math, not a station operator's.** Found at Cape Adare, 2026-07-13:
  `Upper_Earth_Immigration_Composition.md` credited UK with an elevated Significant-tier share
  because Carsten Borchgrevink (St. Carsten, the explorer the city venerates) held British
  nationality — even though Cape Adare's own Specs/Local_Cultures files deliberately and repeatedly
  establish that his significance has nothing to do with his own nationality, and UK's actual
  resulting share (5.03%) was the *smallest* of its tier, not an elevated one — the note wasn't just
  a rule violation, it didn't even match its own city's data. **The GPS-only rule applies to any
  real-world figure a city's founding lore references — an explorer, a station namesake, a historical
  administrator — not just to the station's own operating nation. When a city's founding story
  centers a named historical person, check the master composition file for that person's own
  nationality quietly receiving credit.**
- **Sibling-city omission — a city's own "how many peers like me exist" count going stale.**
  Distinct from the other four: not a wrong fact about the city itself, but an incomplete count of
  *related* cities, missed because one of them was created/resolved after the count was originally
  written. Found at Sejong ("Janbogo is Korea's only other demographic center" — actually two
  others) and, wider, at Janbogo itself ("Tepenia's two Korean cities" — actually three, omitting
  Sinheung), including inside a full proposed creative section
  (`Janbogo_Full_Extrapolation.md`'s "Sejong Relationship" section, built entirely on a two-city
  premise). **When a city's file claims to be one of N sibling cities sharing some trait (same
  founding nation, same real-world basis, same structural role), verify N against a project-wide
  grep for that trait — don't trust the count as given, especially if any sibling was resolved or
  significantly changed after the claiming file was last touched.** Also surfaced a related, useful
  precedent: not every sibling relationship needs to resolve to the same shape — Janbogo/Sejong kept
  a "limited ceremonial contact" relationship while Sinheung genuinely had
  none (different founding mechanism, different subnet, no established connection) — a three-way
  count doesn't require a uniform three-way relationship.

**A cousin of the sibling-city omission pattern, found re-checking Shirayuki a third time
2026-07-13: sibling-exclusivity overclaims.** Where omission bugs undercount siblings ("two Korean
cities" when there are three), this pattern overclaims exclusivity — "the only Tepenian city founded
via institutional diplomatic engineering," when Sinheung shares the
identical Jeju-do mechanism. Found in five separate locations across Shirayuki's own files
(a headline One-liner, a Cross-Reference finding's core argument, a Full Extrapolation section, and
two dated Specs claims), none caught across two prior re-check passes — this kind of claim hides
well because each individual file reads as internally consistent; only cross-checking against the
*other* city's own corrected file surfaces it. **When a city's file claims to be "the only" one of
something, grep the rest of the corpus for the same claim before trusting it — the same way sibling
counts need verifying.** A developer catch of a stale section *heading* (not body text — "The Early
Relationship With Sinheung and Zhongshan," bare "Sinheung" instead of the bracket convention) then
triggered a repo-wide heading grep, which surfaced a serious, unrelated bug entirely outside
Shirayuki's own files: Mirny's own Section VIII described "the two Russian communities" between
Mirny and Sinheung as a defining relationship — wrong, since
Sinheung was never Russian-founded. Mirny wasn't even on that day's
checklist. **Headings need the same naming-convention check as body prose — they're easy to
overlook precisely because they read as labels rather than claims.** See
[[project_shirayuki_recheck_exclusivity_and_mirny_bug]].

**The widest-blast-radius bug found in this entire sweep, discovered on a third re-check of
Sinheung, 2026-07-13: staleness compounds upward through synthesis layers
that cite lower layers without re-verifying them.** Every prior fix in this methodology targeted a
single city's own files. This one was different: a `Mirny_Subnet_Ultra_Megasheet` (6 files,
subnet-wide, never previously checked) was built extensively on the pre-correction "dual founding"/
"self-named" premise — not passing mentions, but load-bearing analytical structure (a whole
"five distinct mechanisms" taxonomy that needed merging to four, arguments about naming built on a
now-false "chose once already" premise). The bug then propagated one level higher still, into the
single project-wide `Super_Ultra_Megasheet` sitting above *every* subnet's own Ultra-Megasheet,
inherited via uncritical citation. **Any city that belongs to a subnet with its own Ultra-Megasheet
needs that Ultra-Megasheet checked too, not just the city's own file layers — and if a project-level
synthesis document exists above that, check it as well.** Staleness doesn't stay contained to the
city it originated in; it flows upward through every document that cites the layer below it as
settled fact rather than re-verifying the citation. See
[[project_soyuz_recheck_ultra_megasheet_gap]].

**A sibling lesson, found re-checking Juan Carlos 2026-07-13: negative claims need re-verifying
just as much as positive ones.** The first-pass resolution memory stated *"No README.md exists for
this city's Megasheet (like Casey)"* — wrong. A `README.md` existed the whole time, created
2026-07-08, sitting in the same folder as the three component files, entirely unfixed. The
`find`-based file search that produced the "no README" conclusion had been run once, early on, and
never re-run at the point the fix was actually applied. **"I checked once and found nothing" is not
the same claim as "there is nothing" — re-run the search at fix time, not just at investigation
start, especially for any city where a sibling city's genuine absence (Casey truly has no README)
makes the negative feel like an unremarkable default.** See
[[project_juan_carlos_recheck_readme_gap]].

**A related but distinct staleness pattern, found re-checking Shirayuki 2026-07-13 — not the
nationality-bug class itself, but worth watching for during the same sweep:** a file's own header or
metadata contains an "updated on [date]" note acknowledging some fast-moving fact changed (a city
finally getting its real name, a status flip), but the body text below was never actually swept to
match. `Shirayuki_Mega_Init.md`'s header said "Naming note, updated 2026-07-08" — correct — while its
own "What's Actually Open" section, three paragraphs down, still listed the name as "the single
largest open item, deliberately deferred." Same gap in `Full_Extrapolation.md` (an entire section
built on the now-false premise) and `Cross_Reference_Synthesis.md`. README.md's own top note claimed
"updated to the final name in all three source files" — also not actually true until this re-check
fixed it. **Don't trust a file's own "this has been updated" claim; check the body text explicitly,
the same way the header claims to have already done.** See
[[project_shirayuki_recheck_naming_staleness]].

**A reusable technique, not a sixth bug pattern:** when two cities are established as deliberate
structural/demographic mirrors of each other (Zukelli and Janbogo explicitly are — "almost a mirror
of Janbogo's" per Zukelli's own Section 1), diff their parallel sections directly against each
other, not just each one against its own internal population table. A claim can be individually
plausible in isolation and still be an overclaim relative to the sibling city's more careful version
of the same claim. Found this way at Zukelli: Local_Cultures' Language section claimed Italian was
"the civic default" despite not even being Zukelli's largest Significant-tier nation, a stronger
claim than Janbogo's own parallel section made for Korean under an equivalent (arguably stronger)
demographic case. An internal-only check might have missed it, since "founding language persists
somewhat" is true in both cities — the bug was specifically in *how strongly* one sibling's version
claimed it.

---

## 4. The investigation checklist, per city

1. **Pull the city's own Population & Composition table** (`Specs/[City].md`) — confirm what
   tier/percentage each nation actually holds *today*, and read any notes on *how* that table was
   derived (organic tiering vs. hand-corrected — a corrected table is where stale sections hide).
2. **Read the Founding Story** (`Local_Cultures/[Subnet]/[City].md` Section 2, and `Specs/[City].md`
   Founding section) — confirm every nationality named in the tier table's annotations is actually
   supported by this prose. Flag any tier annotation with no textual backing.
3. **Read the "deeper cultural apparatus"** — architecture, cuisine, fashion, music, arts/crafts,
   social contract, private life — checking every nationality mention against the *current* tier
   table (not memory, not vibes — the actual numbers). Flag anything citing a nation whose weight in
   the table doesn't justify being singled out over its peers at the same or higher tier.
4. **Grep is not enough — read the sections.** A keyword search for one exact phrase
   ("Chinese and Japanese") will miss a paraphrase of the same bug ("Chinese, Japanese, and...").
   Grep to prioritize where to look, but actually read every flagged section's surrounding prose.
5. **Check every layer independently**, not just the Local_Cultures sheet: `Specs/[City].md`,
   `Local_Cultures/[Subnet]/[City].md` (32 sections), `City_Megasheets/.../[City]_Mega_Init.md`,
   `..._Full_Extrapolation.md`, `..._Cross_Reference_Synthesis.md`, and `README.md`. Each has
   independently drifted in past cases — a fix in one does not propagate to the others.
   **Confirmed the hard way at Zhongshan, 2026-07-13: a resolution memory claiming "all layers
   checked" is not itself evidence the check happened.** The original Zhongshan fix session touched
   Local_Cultures and all three Megasheet files correctly, then apparently never actually re-read
   `Specs/Zhongshan.md` before declaring the city resolved — it sat with the old, unfixed content for
   over a week while marked `[x] RESOLVED` in `TODO.md`. **Re-read the live file yourself, every
   time, even for a city your own memory says is already done — especially the primary Specs file,
   the one layer it's easiest to assume must obviously already be correct. **This distrust applies at
   the single-instance level too, not just the whole-file level** — confirmed at Shirayuki's fourth
   re-check pass (2026-07-13), where a prior pass's own writeup claimed two identical exclusivity-bug
   instances in `Specs/Shirayuki.md` were both fixed, but only one actually was. A memory saying
   "fixed" is not evidence, whether the claim covers a whole file or one bullet point within it.
   **Sharper corollary, confirmed at Sejong's fourth pass:** checking a file for one specific bug
   pattern and finding it absent is not evidence the file is clean of every bug pattern. Sejong's
   third pass explicitly checked `Localization_Language_List.md` for stale China/co-Primary claims,
   found none, and declared the file "checked clean" — but a completely different bug (the Korean
   sibling-omission pattern) sat one line away, untouched. A "checked clean" note should specify *what
   was checked for*, and later passes should re-read content fresh rather than trust even a
   narrowly-true "no stale X found" claim to mean "no bugs of any kind."**
6. **`README.md` is a stale, hand-concatenated snapshot** of the other three Megasheet files, not a
   live include. Fixing the three component files does NOT fix README.md — it must be regenerated
   (re-concatenated) afterward, or it will silently keep serving the old, wrong version.
7. **Check adjacent/meta files before assuming a fix is new.** `Tri-Cities_Region.md` already had
   the correct Jeju-do mechanism, written a full week before this bug was independently
   rediscovered on Zhongshan — it just never propagated into the individual city files. Always
   check region/cluster-level overview docs for canon that's already correct but un-synced.
8. **When founding-nation ≠ current-Primary-nation, check for precedent before inventing a
   resolution.** Sayowa (Japan-founded, later demographically diluted by ordinary Chinese
   immigration) is the established precedent pattern for organic dilution — different in kind from
   Sinheung's pattern (founder and current-Primary are the same nation,
   Korea, just not the nation that physically built the station). Don't assume every
   founder/current-nation mismatch needs the same fix; check which pattern actually applies.
9. **Confirm the resolution direction with the user before rewriting**, especially when the fix
   requires real creative development (not just re-causation of already-good content) — ask whether
   the city should read as singularly one-nation-dominant (Zhongshan/Korean-city pattern) or as
   genuinely diffuse (Sayowa pattern) before generating 32 sections of new material.
10. **Save the resolution to memory and mark the TODO.md checklist entry**, including which files
    were touched and which weren't yet verified — see the project's per-city resolution memories
    (`project_zhongshan_singularly_chinese_resolution`,
    `project_currently_unnamed_korean_city_resolution`, `project_shirayuki_bug_check_resolved`) as
    templates for the writeup format.
11. **On a late re-check pass, widen the sweep to top-level storyline/design docs, not just
    per-city and per-subnet files.** Confirmed at Zhongshan's fourth re-check pass (2026-07-13):
    `Storyline/DLC_Overview.md` — never on any per-city file list, since it isn't filed under any
    single city's own folder — still repeated the exact "Soyuz self-named by its founders" and
    "Shirayuki... the only city founded this way" bugs already fixed everywhere else in the corpus.
    A city's own reference network extends past its Local_Cultures/Megasheet/City_Relationship
    files into whatever top-level overview documents mention it in passing — grep those explicitly
    once the per-city layers are confirmed clean, don't assume they're out of scope just because
    they're not filed under the city. This applies equally to `Worldspace/Factions/*.md` — confirmed
    the same day, one city's own re-check later: `City_Origin_Factions_Second_Interwar.md`'s
    Larsemann Hills Compact section had three stacked founding-nation errors (including a previously
    unseen "dual Russian and Australian founding" variant for Sinheung) that
    directly violated that document's own stated method banning founding-nation-as-causal-explanation.
12. **On a late re-check pass, run at least one repo-wide grep for the city's name with no path
    restriction — not just within `Locations/Cities/`.** Confirmed at {{currently-unnamed Korean
    city}}'s fifth re-check pass (2026-07-13), the first time any pass for this city searched outside
    the Cities folder: it immediately found the "Russian-founded" error in `Dev-Road-Map/
    Localization_Language_List.md` (a dev-facing planning document) and in a companion doll's own
    character file (`Characters/Dolls/.../Lyuba.../README.md`). This bug class isn't confined to city
    documentation — anywhere a city gets name-dropped as flavor or justification is a place the same
    stale founding-nation claim can hide, including files nobody would think to check because they
    aren't "about" the city at all.
13. **A "grep outside the Cities folder" pass has a structural blind spot: cross-reference files
    that live *inside* `Locations/Cities/` but aren't part of any single city's own dedicated file
    set.** Confirmed at Sejong's fifth re-check pass (2026-07-13): `City_Relationship_Database.md`'s
    own Sejong entry carried the same stale bug already fixed in a dev-facing doc outside the Cities
    folder, untouched the whole time because a grep scoped to "outside Cities" never looked at it, and
    no single-city file-list ever included it either. Files like `City_Relationship_Database.md`,
    `Official_Population_Census.md`, `Upper_Earth_Immigration_Composition.md`,
    `City_Refugee_District_Affinities.md`, and `Inspirational-Influences.md` need their own explicit
    check, separate from both "the city's own files" and "everything outside the Cities folder."
14. **A city's own Full Extrapolation or Cross-Reference Synthesis can correctly flag a bug and even
    correctly propose the fix — and that fix can still sit unapplied to the actual source file for
    days or weeks.** Confirmed twice in one afternoon, 2026-07-13: Signy's `Signy_Full_Extrapolation.md`
    Section IX (written 2026-07-08) explicitly diagnosed a "damaged vs. intact" status contradiction and
    concluded "should defer to the confirmed intact status" — the correct answer — but
    `Local_Cultures/Signy.md` itself still said "damaged" five days later, because nobody had gone back
    and actually edited it. Marambio's `Marambio_Cross_Reference_Synthesis.md` Finding 1 (also
    2026-07-08) diagnosed a stale "one concentrated strategic asset" destruction justification and
    explicitly flagged it as "worth a phrasing update for `Specs/Marambio.md`" — still unapplied five
    days later, and also present, unfixed, in the very document that had diagnosed it
    (`Marambio_Full_Extrapolation.md` Section I made the identical stale claim as its own operative
    premise, one file over from the finding that named it a bug). **A correct diagnosis inside an
    analytical document is not a fix. Treat every "worth flagging for a phrasing update" or "should
    defer to X" note found in a Full_Extrapolation/Cross_Reference_Synthesis file as an open action
    item to verify against the actual target file — these documents are read far less often than
    Specs/Local_Cultures, so a correct call made inside one can go unactioned indefinitely.**
15. **This checklist's official target is nationality-causality bugs, but the same investigation
    process reliably turns up an adjacent, equally-real class of staleness bugs — status
    contradictions, highway-route/terminus errors, and "this data-quality gap is fixed elsewhere but
    the open-items list here doesn't know it" gaps. Fix these too when found, using the same
    propagate-to-every-layer discipline, rather than treating them as out of scope.** Confirmed across
    Kunlun (a genuinely superseded highway route surviving in the city's own files after being fixed
    on a sibling city's side), Vostok (`City_Relationship_Database.md` contradicting itself between two
    adjacent lines), Signy (a status contradiction flagged twice, fixed by neither flag), and Marambio
    (a destruction-justification predating a later-added dual-identity detail, plus a census gap already
    closed elsewhere but still listed open locally). The line to hold: fix these opportunistically when
    the same reading pass surfaces them, but don't go looking for them as a separate project — and when
    a developer raises a genuinely new creative-direction question mid-pass (e.g. "should this city's
    population table itself change"), log it as an explicitly deferred flag rather than resolving it
    unilaterally; see `project_esperanza_bug_check` and `project_marambio_bug_check` memories for the
    Argentina-proximity example of this distinction in practice.
16. **`README.md` files are located by filename-pattern search failure, not by omission — check every
    Megasheet folder directly, don't trust a city-name grep.** The standard file-location step for a
    new city (`find City_Megasheets -iname "*[CityName]*"`) will *never* match a plain `README.md`,
    because README.md's filename never contains the city's own name. This isn't a rare miss — it
    silently failed on every single city checked this way, discovered only when a *content* grep (for
    an unrelated string) happened to surface a README.md that a *filename* grep never could. Confirmed
    affected: Kunlun, Vostok, Signy, and Esperanza were all wrongly recorded as "no README exists for
    this city" — Casey suffered the identical miss earlier the same day, caught by coincidence rather
    than method. When Kunlun's, Vostok's, and Esperanza's READMEs were finally read, they turned out to
    be clean (up-to-date concatenations of already-fixed source files) — but Signy's and Marambio's
    both still carried real, previously-unfixed staleness, in Marambio's case including a bug that had
    never been fixed *anywhere*, not even in its own source file. **Always verify a Megasheet folder's
    actual contents with `ls` or `find <folder> -type f` on the folder itself, never a city-name
    filename pattern — and if a README.md turns up on a later pass that an earlier pass said didn't
    exist, don't assume it's therefore already clean; read it and diff it against its three source
    files like any other City_Megasheets file.** See [[project_marambio_bug_check]] for the full
    discovery and the resulting correction across five cities' tracker entries.
17. **Headline summary fields — One-liners, opening taglines, "Hard Facts" table headers — need the
    same explicit check as section headings, not just body prose.** Confirmed the hard way at
    Sinheung's fourth re-check pass (2026-07-13): `Local_Cultures/
    Mirny_Subnet/Sinheung.md`'s own One-liner — the single most prominent line in the entire 32-section
    file, sitting *above* every section — still read "a city that named itself after a spacecraft...
    ambition chosen deliberately over nostalgia," the exact self-naming error already corrected two
    pages below it in that same file's own Section 2. Three prior full re-reads of this file missed
    it. A One-liner reads as decorative framing, easy to skim past, but it's a factual claim like any
    other and needs the same verification as the body text it summarizes.
18. **A fourth variant of the operator/founder conflation: GPS-proximity between two neighboring
    real-world stations can itself smuggle in an unearned heritage claim, even in a "correction" meant
    to fix the more familiar version of this bug.** Confirmed at Janbogo's fifth re-check pass
    (2026-07-13): `Specs/Janbogo.md`'s tier table wrongly tagged Italy `(founding operator heritage)`
    — Italy's real operator heritage (Mario Zucchelli Station) belongs to neighboring Zukelli, not
    Janbogo (Jang Bogo Station, South Korea's operator), the third time this exact bleed-over had been
    found across the corpus. The first fix attempt retagged Italy as "operator-*adjacent* — shared
    Terra Nova Bay proximity to Zukelli," copying phrasing that had sat unchallenged in
    `Local_Cultures/Janbogo_Subnet/Janbogo.md` since at least the city's first pass. **The developer
    caught that this was itself still wrong**: Italy has no founding-population connection to Janbogo
    at all, adjacent or otherwise — the two stations' ~8km proximity is GPS coincidence, not a
    heritage channel of any kind, and the correct fix was to remove the tag entirely rather than
    soften it. **When two cities are established neighbors (shared bay, shared subnet, visible from
    each other), don't assume a nation's genuine founding role in one city licenses even a qualified,
    "adjacent" heritage tag in the other — a real GPS relationship between two cities is not itself a
    population-causal relationship, and proximity-flavored language can reintroduce the exact bug a
    fix was meant to remove.** See [[project_janbogo_bug_check_resolved]].
19. **A session's own notes claiming "corrected directly into [file list]" are not themselves evidence
    every listed file actually received the correction — the sharpest version yet of the "all layers
    checked is not evidence" lesson.** Confirmed at Halley's first re-check pass (2026-07-13):
    `City_Vision_Notes/Halley.md`'s 2026-07-04 session record states explicitly that a resolution
    (the Halley subnet's Arcanet nexus sits at Sanay, not Halley) was "corrected directly into
    `Specs/Halley.md`, `Local_Cultures/Halley_Subnet/Halley.md`, `Specs/Sanay.md`, and
    `Local_Cultures/Halley_Subnet/Sanay.md`" — four named files. It was only ever actually applied to
    Sanay's two files; Halley's own two files still carried the pre-resolution "not yet decided"
    placeholder nine days later, creating an internal contradiction between Halley's own primary
    Specs/Local_Cultures files and its later-compiled Mega_Init/Enneagram files (which correctly
    picked up the resolution from Sanay's side). The staleness had also spread into files the original
    session never touched at all — `City_Relationship_Database.md` (both cities' entries) and a
    Theoretical-Calculations shipping-logistics reference. **When a session note lists multiple target
    files for a correction, verify each file individually — a specific, confident file list is not
    more trustworthy than a vague "fixed everywhere" claim, it's just more checkable.** See
    [[project_halley_bug_check]].
20. **When a fix corrects a false claim that wrongly named multiple cities, check each wrongly-named
    city's own file/entry too — not just the file where the false claim was originally written.**
    Confirmed at Neumayer's first re-check pass (2026-07-14): Halley's own bug-check pass (2026-07-13)
    fixed `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`'s false claim that
    "Halley, Neumayer, Belgrano" were the Halley subnet's coastal receiving ports (the real answer is
    Belgrano and Sanay only), and correctly propagated that fix into `City_Relationship_Database.md`'s
    Halley entry — but never checked Neumayer's own entry in that same database, even though Neumayer
    was the *other* city wrongly named in the original error. Neumayer's entry still claimed it was "a
    coastal port receiving South African summer freighter shipments" for nine days afterward. A fix
    that names which entities were wrongly implicated should trigger a check of every one of those
    entities' own files, not just the file the error was found in and the file most directly tied to
    the correct answer. See [[project_neumayer_bug_check]].
21. **A founding-heritage tag can migrate onto the wrong nation via direct copy-paste between two
    cities that happen to share an otherwise-identical tier-table nation list — a new sub-variant of
    the operator/founder-conflation family, distinct from GPS-proximity smuggling (item 18).**
    Confirmed at Sayowa's second re-check pass (2026-07-14, part of the Mawson subnet sweep):
    `Specs/Sayowa.md` and `Local_Cultures/Mawson_Subnet/Sayowa.md` both read "Japan, Germany, France,
    UK, South Korea, Indonesia, Australia *(founding wave)*" — with the tag attached to Australia,
    even though both files' own prose is unambiguous that Japan (JARE/Syowa Station) is Sayowa's
    actual founding nation, with zero established Australian founding connection anywhere. The likely
    origin: `Specs/Mawson.md` carries the *exact same row text*, where the tag is genuinely correct
    (Australia truly is Mawson's own founding nation) — strong evidence the row was copied between
    the two cities' files at some point, with the tag riding along attached to the wrong nation in
    the new context. **When two cities' tier tables share an identical or near-identical nation
    list, check whether any founding-heritage tag riding along in that shared text actually belongs
    in the destination city, rather than assuming a match in wording means the underlying fact was
    independently verified for each city.** See [[project_sayowa_recheck_mawson_sweep]].
22. **Shared/aggregate files should be checked once as a batch angle covering every entity at once,
    not re-read once per entity.** Discovered running Investigation Loop Round 2 (2026-07-14): a
    single full read of `City_Relationship_Database.md` (539 lines) or `Official_Population_Census.md`
    (729 lines) verifies every one of the 35 cities' cross-reference entries simultaneously — reading
    either file 35 separate times, once per city, would have been pure waste. The same logic applies
    to any subnet-wide Ultra-Megasheet (already covered by item on synthesis-layer staleness above):
    checking it once clears that layer for every city in the subnet at once. **When a bug-hunt targets
    many entities that all share a small number of aggregate cross-reference files, budget one pass
    per aggregate file, not one pass per entity per file** — it's both faster and more thorough, since
    a full read of the whole file surfaces cross-entity patterns (see item 27) a narrow per-entity grep
    would miss.
23. **For any bug class that reduces to a checkable structural or numeric invariant, write a script
    to check the whole corpus at once rather than relying on repeated manual per-entity eyeballing.**
    The recurring tier-ordering anomaly (a Notable-tier nation's share exceeding a Significant-tier
    nation's) had been manually checked, inconsistently, across dozens of individual city passes —
    some passes explicitly eyeballed the tier table, most didn't think to. A ~40-line Python script
    parsing every city's own "Per-Nation Breakdown" table and checking the tier-boundary invariant
    found **6 previously-undetected instances in a single run** (Belgrano, Halley, Concordia, Dumont
    d'Urville, Juan Carlos, Sinheung), on top of the 7 already known from scattered manual catches. A
    judgment call ("does this city's culture-writing correctly attribute a practice?") genuinely needs
    a human read; a mechanical invariant ("does every Significant-tier share exceed every Notable-tier
    share?") does not, and manual checking of mechanical invariants is exactly where inconsistent
    coverage hides. **Whenever a bug class can be phrased as "for every X, check that Y holds," stop
    checking it by hand and write the five-minute script instead — it won't get tired, skip a city, or
    forget to look on a later pass.**
24. **Once a bug class is confirmed to recur across many entities, consolidate every known instance
    into one dedicated master-list document, rather than leaving them scattered across individual
    per-entity write-ups.** The tier-ordering anomaly had been independently re-discovered and
    re-described, slightly differently worded, in seven different per-city memory files before Round 2
    — workable, but it meant every new pass had to either re-derive "is this already known" from
    scratch or trust an incomplete mental list. Building one consolidated registry
    (`project_tier_ordering_anomaly_master_list.md`) the moment the script surfaced the full set solved
    two problems at once: it gave every future pass one place to check "is this already flagged," and
    it made the true scope (13 instances, not 7) visible for the first time. **The trigger for doing
    this: the second or third time you find yourself writing "same pattern as before, Nth occurrence"
    in a per-entity write-up, stop and build the registry instead of continuing to scatter instances.**
25. **A correction already applied in one section of a file does not guarantee it propagated to other
    sections of that *same file* describing the same fact.** Found at Marambio (2026-07-14): its own
    Notable Locations section correctly documented that an earlier "Herbert Sound" claim had been wrong
    and corrected to "Picnic Passage" — but the file's own Geographic Basis section, describing the
    identical geographic fact, still said "Herbert Sound," untouched. This is a tighter-grained version
    of item 6 (README doesn't auto-update) and item 14 (a diagnosis isn't a fix): here the fix genuinely
    *did* land, just only in the one section someone happened to be editing at the time. **When a file
    has multiple sections that could plausibly restate the same underlying fact (geography, population,
    founding, status), grep that file for every other place the fact might be restated before trusting
    that fixing it once means the file is now internally consistent.**
26. **When the same fact appears twice in one file — once as a detailed standalone entry, once folded
    into a summary total or list — verify the two figures are arithmetically consistent with each
    other, not just each independently plausible on its own.** Found at Belgrano's Section IV entry in
    `Official_Population_Census.md` (2026-07-14): the standalone entry rounded its population to
    "837,000," while the file's own combined-losses summary, three paragraphs down, used "838,000" —
    and only 838,000 makes the summary's own stated total add up correctly. Reading either number in
    isolation, neither looks wrong; the bug only surfaces by actually re-adding the summary's component
    parts and checking the total matches. **Whenever a document states both a set of individual figures
    and a computed total or list built from them, redo the arithmetic — don't assume a document that
    states its own total correctly derived that total from the figures printed nearby.**
27. **A systematic, corpus-wide audit of one tag or annotation pattern — extracting every instance at
    once and reviewing them side by side — distinguishes genuine cross-entity canon from copy-paste
    bleed-over far more reliably than checking each instance in isolation.** Run as Investigation Loop
    Round 2's own Phase 2 (2026-07-14): a single grep pulled every `(founding operator heritage)`,
    `(founding wave)`, `(founding infrastructure heritage)`, and Jeju-do-allocation tag across all 38
    Specs files into one list. Seeing them together made a pattern visible that checking any one city in
    isolation couldn't reveal: "Australia (founding wave)" and "New Zealand (founding wave)" recur
    across nearly every Ross Sea/Janbogo-subnet city regardless of that city's own real-world station
    operator — which, cross-referenced against the established Hobart/Fremantle shipping-partner canon
    (`TODO.md`, `City_Relationship_Database.md`'s own per-city shipping notes), turned out to be
    genuine, deliberate, project-wide canon (early-arriving immigration via a specific real-world
    gateway), not the copy-paste bleed-over item 21 would predict on first glance. **Before flagging a
    tag pattern that recurs across many entities as a bleed-over bug, pull every instance into one view
    and check whether it traces to an already-established cross-entity canon (a shipping route, a
    regional immigration pattern) before assuming it's an error — but also don't skip pulling every
    instance into one view in the first place, since that's the only way to tell the two apart.**

---

## 4A. Running this checklist as a repeatable convergence loop (added 2026-07-14)

Everything above describes *what* to check per entity. This section describes a *process* for running
the checklist repeatedly across a large entity set until the developer can trust the result, developed
and validated running "Investigation Loop Round 2" across all 35 Tepenian cities in one sitting.

**The loop structure:**
- Group entities into natural clusters (here: subnets). Order the clusters deliberately — the
  developer's own preference (largest clusters first, smallest saved for last) is a legitimate lever;
  re-sequencing mid-loop does not require redoing work already completed under the old order.
- Within a cluster, work one entity at a time. Apply the full checklist. **Repeat until the entity
  comes back clean *N* times in a row** — a pass that finds and fixes something resets that entity's
  clean-streak counter to zero, since the fix itself still needs independent re-verification.
- Once every entity in a cluster has reached its streak target, do a second pass through the same
  cluster at a *lower* streak target (fewer required consecutive clean passes) — a cheaper spot-check
  round, not a full repeat, since the first round already did the heavy lifting.
- Track live state (per-entity streak counts, a pass-by-pass findings log) in a **dedicated tracker
  file** separate from both the methodology document (this file) and the per-entity memory notes — see
  `Investigation_Loop_Round2_Tracker.md` for the format that worked. The tracker is what survives a
  context-window reset or a session boundary; don't rely on remembering streak counts.

**What counts as "clean" — this matters as much as the loop mechanics:** a pass that re-confirms an
already-known, already-flagged, deliberately-deferred issue (the standing tier-ordering anomaly; a
narrative contradiction the developer explicitly chose to leave open) is still clean — it isn't new,
isn't being silently dropped, and re-noticing it isn't grounds to reset the streak. Only a *genuinely
new* finding — an instance not already on record — breaks the streak. Get this distinction wrong in
either direction and the loop either never terminates (treating known issues as fresh failures) or
quietly stops catching real regressions (treating everything as "probably already known").

**Pacing — full depth doesn't mean full depth every single pass:** the first pass on any entity should
be genuinely thorough (a fresh thorough read, not a rubber stamp). If that first pass comes back clean,
the following passes toward the streak target can be lighter and faster — a different, narrower angle
each time (population-math re-verification, a repo-wide grep, a spot-check of one specific section) —
rather than repeating the same full-depth read three times over. The moment *any* pass at any depth
finds something, that finding gets full-depth treatment (root-cause it, fix it, check for the same bug
elsewhere) and the streak resets to zero from there. This kept a 35-entity, ~150-pass sweep tractable
in a single session without sacrificing thoroughness where it actually mattered.

**Angle types that proved genuinely productive, worth cycling through rather than repeating the same
one:** (a) a fresh full re-read of the entity's own primary file; (b) the shared subnet/cluster-level
synthesis layer, checked once per cluster per item 22; (c) the project-wide top synthesis layer above
that, same logic; (d) population/numeric math re-verified via script; (e) a repo-wide grep for the
entity's name outside its own folder; (f) a systematic corpus-wide script check for one bug class, per
item 23; (g) a systematic corpus-wide tag/pattern audit, per item 27. Different angles catch different
bug classes — a fresh read catches prose-level staleness, the script checks catch mechanical invariants
a read will skim past, and the tag audit catches cross-entity bleed-over a single-entity read can't see
at all by definition.

---

## 5. Naming convention for cities awaiting a real name

When a city's current filename/placeholder name (e.g. "Sinheung") was never actually chosen by the
population that lives there — verify this against the Founding Story before assuming it — refer to
the city as **`{{currently-unnamed [Nationality] city}}`** in conversation and in new prose, per
`feedback_currently_unnamed_korean_city_label` memory. Keep using the underlying filename for file
paths and cross-references; only the *prose label* changes. This convention already existed in
`Tri-Cities_Region.md` and `Inspirational-Influences.md` (as `{{ex-Sinheung}}`) before this session
independently reinvented it — check for an existing bracket-placeholder convention before assuming
one needs to be created.

---

## 6. Status

See `TODO.md`'s "BLOCKING — Country-wide culture re-check" section for the live, per-city
checklist. **As of 2026-07-13, every previously-`[x]` city was downgraded to `[~]`** after
re-checking Zhongshan (already marked resolved) found `Specs/Zhongshan.md` had been missed entirely
by the original fix — see [[project_zhongshan_recheck_specs_gap]] for the full story and the
methodological lesson. Developer directive: *"checking, double-checking, triple-checking,
quadruple-checking, quintuple-checking every single city... only the developer will clear a city
back to `[x]`."* Cities with substantive work already done this session (Zhongshan re-fixed;
Janbogo, Zukelli, Casey, Shirayuki, Sinheung, Juan Carlos, Sejong from
earlier passes) remain at `[~]` regardless of how clean a re-check finds them — re-verifying a city
and finding it fine does not itself restore `[x]`. Do not proceed to non-checklist work until every
city is confirmed by the developer.

**Investigation Loop Round 2, 2026-07-14 — complete.** Ran the full checklist above as a formal
convergence loop (see Section 4A) across all 35 cities in every subnet, requiring 3 consecutive clean
passes per city (Phase 1) followed by a lighter 2-consecutive-clean spot-check round (Phase 2, run as
batch angles per item 22 rather than per-city). Every city cleared both phases. Findings: two
previously-undetected tier-ordering-anomaly instances (Belgrano, Halley — flagged, not fixed, per
standing precedent), one geographic self-consistency bug (Marambio's Herbert Sound claim, item 25),
one arithmetic self-consistency bug (Belgrano's census figure, item 26), and — via the new
script-based check (item 23) — 6 more tier-anomaly instances discovered project-wide beyond the 7
Round 1 had found manually, now consolidated per item 24 in
`project_tier_ordering_anomaly_master_list.md`. Live loop state:
`Cities/Investigation_Loop_Round2_Tracker.md`. Items 22-27 and Section 4A above were all extracted
directly from running this loop — see that tracker file's own pass log for the full narrative each
item is drawn from. Amundsen Station (outside the 35-city count) was also re-checked, once, per
explicit developer request — clean on the first pass, no further re-check needed.

**DEEP-DIVE CONFIRMED COMPLETE BY THE DEVELOPER, 2026-07-14.** Every city in `Full_City_Integrity_Check.md`
(all 35, plus Amundsen Station) has been restored to `[x]`. This is no longer a BLOCKING item — see
`TODO.md`. The two standing, deliberately-deferred items (the tier-ordering anomaly and Byrd's
highway/isolation contradiction) remain open by the developer's own choice, not because any city is
still unverified.
