# Tepenian National Holidays

**Established 2026-07-16.** Answers the open placeholder flagged in
`General-Overview-Notes/aspects_of_consideration.md` ("Tepenian holidays (e.g., Tepenian Independence
Day, Halloween, etc) [to-be-determined]"), scaffolded from a developer brainstorm dropped in
`to-be-integrated/possibilities_for_holidays.txt`. Also folds in the "Tepenian Saints" civic-observance
half of the still-open `TODO.md` item on that topic, and cross-references two holiday-adjacent
traditions already written into existing city lore that this document's framework retroactively
explains.

**Core framing:** unlike most real-world nations, Tepenia's holiday calendar isn't inherited wholesale
from any single founding culture — consistent with the project's binding **No National Stereotypes**
rule (see `feedback_no_national_stereotypes` and `TODO.md`'s compliance sweep), no holiday here reads
as "nation X's descendants celebrating nation X's heritage." What actually took hold, and why, sorts
into four distinct categories.

---

## Category 1: Civic/National Holidays

### Tepenian Independence Day — June 21

The anniversary of the Falkland Treaty (June 21, 2564), Tepenia's founding document. Southern
Hemisphere June 21 also happens to be the Antarctic winter solstice — a resonance worth leaning into
deliberately in future design work (the darkest day of the year as the day a nation of exiles chose to
call itself a nation), even though the treaty date itself wasn't necessarily *chosen* for that reason
in-fiction; that's an open question below, not settled canon yet.

**Established observance:** Hut Point remembrance in Scott and Fort McMurdo — residents lay candles,
flowers, and personal tokens at Hut Point, Scott's most sacred civic location (per `Specs/Scott.md` and
`TODO.md`'s Tepenian Saints item).

### Tepenian Saints Days

Pre-War (pre-2083) Antarctic explorers, venerated in Tepenian civic culture as "Saints" for
unknowingly preparing the home that exiles would later need. Honorific uses first name. Known roster
so far (per `TODO.md`):

- **St. Robert** — Robert Falcon Scott (city of Scott)
- **St. Ernest** — Ernest Shackleton
- **St. Roald** — Roald Amundsen (Amundsen Station)
- **St. Douglas** — Douglas Mawson (city of Mawson)
- **St. Richard** — Richard Byrd (city of Byrd)

**Scope note:** the *full* Saints framework (complete roster, individual feast days, how observance
varies city by city) is its own still-open `TODO.md` item ("Tepenian Saints — create dedicated culture
document") and is deliberately not duplicated here. This document treats Saints Days as a category
within the national holiday calendar; the deep-dive stays a separate piece of future work.

---

## Category 2: "Persisted Aesthetic" Holidays

Robots (regardless of which city or founding nation they trace to) celebrating specific human
historical aesthetic epochs whose imagery, tone, or general cultural enjoyment outlasted their own era
by a wide margin. Starter list, per the original brainstorm:

- Ancient Egypt
- America *(open question below — likely a historical-aesthetic period rather than the modern USA)*
- Victorian England
- Rome
- **Ancient Sumeria/Babylonia** *(added 2026-07-16)* — a particularly well-grounded addition, since
  robots already have an established, textually confirmed connection to this specific civilization:
  they speak Sumerian, inherited via their U.R.U.K./Uruk origin-lab lore (see `project_sumerian_flagged`
  memory note). This isn't a robots-broadly-admiring-antiquity pick like the other three; it's a direct
  extension of robots' own origin story, which makes it the strongest-anchored entry in this whole
  category.

**Why this is compliant with No National Stereotypes:** none of these read as a founding-population
group celebrating "their own" heritage — Ancient Egypt, Rome, and Sumeria/Babylonia aren't even among
Tepenia's 43
master-list founding nations, and Victorian England predates the modern UK's own founding-operator
role at any Tepenian city. These holidays exist because robots, with equal access to the entirety of
human history rather than a filtered inheritance from one ancestry, gravitated toward specific
aesthetic epochs on their own terms — closer to how a real-world Egyptian-revival or steampunk
subculture works than how a national heritage holiday works.

---

## Category 3: Internationally-Transcendent Holidays

Real-world holidays that, in actual history, broke free of a single originating culture and became
globally recognized (often via globalization/commercialization) well before Tepenia's founding.
Starter list, per the original brainstorm:

- Christmas
- Halloween
- El Día de los Muertos

Same "not nation-specific" logic as Category 2, different real-world mechanism: Tepenia inherited the
globally-diffused version of each holiday, not any one nation's originating version.

---

## Category 4: Celestial / Faction-Specific Holidays

Unlike the first three categories, these are explicitly **not universal** — tied to particular robot
religious factions or to a specific city's unique astronomical circumstances. Two examples already
exist in established lore and retroactively belong in this category:

### Deepest Cold (Dome Fuji)

The central communal observance of Ice-Cold Buddhism (see `Specs/Dome_Fuji.md` and
`Background-Lore/Cities/Mawson_Subnet/Dome_Fuji/Course_of_Events/Dome_Fuji_06_Deepest_Cold.md`): the
precise coldest point of polar night, fixed as the first calm, clear night after the winter solstice.
A genuinely religious, mandatory observance — and, because it's weather-dependent, one that can never
be scheduled with total certainty in advance, which is itself a documented point of doctrinal dispute
within the faith.

### Two Days a Year (Mirny)

A secular (not religious) civic observance, per
`Background-Lore/Cities/Mirny_Subnet/Mirny/Course_of_Events/Mirny_04_Two_Days_a_Year.md`: a few days
near each solstice where Mirny's precise position on the Antarctic Circle makes the sun graze the
horizon instead of fully rising or setting. Flagged in existing design notes as one of the city's few
genuinely war-proof cultural elements.

### The brainstorm file's own proposal (not yet written)

A day when a specific star, nebula, or galaxy feature touches either the South Pole or the Antarctic
Circle, depending on the observing faction's perspective. This is a strong candidate for a **third**
entry in this category, most naturally tied to either the simulation-theory religion or the
still-unnamed Sylvester James Gates-grounded religion (see
`Worldspace/Factions/basis collection - robot religions/Analysis_Notes.md`), and/or centered on
Kunlun's Observatory, already established as arguably Tepenia's primary sacred site. **Not yet
written — flagged 2026-07-16 as its own dedicated investigation in `TODO.md`** ("National Holidays —
Category 4 (Celestial/Faction-Specific) needs its own dedicated investigation"), since which faction(s)
would actually recognize it and what the specific astronomical event is are substantial enough
questions to warrant real design work of their own rather than a quick fill-in here.

---

## Scope Note — What's Deliberately Not Covered Here

This document is the *national framework*: the four categories and their known headline examples.
During this review, nearly every subnet's `Local_Cultures/[City].md` files turned out to already
contain their own scattered festival/tradition mentions, individually written city by city over the
course of this project. Systematically cross-referencing or folding all of that into this framework is
future work — it likely overlaps with the planned Phase 1c Cultural Iceberg research (Surface Culture
explicitly includes festivals/holidays as a subcategory; see `Neo-Races-and-Cultures/`), and wasn't
attempted here to avoid scope creep or duplicating that later pass.

---

## Open Questions

- **Category 2 — additional aesthetic epochs?** The brainstorm file left a blank line after Rome for
  more entries; Ancient Sumeria/Babylonia has since been added (2026-07-16). Further candidates worth
  considering, and what "America" is actually meant to represent (a period — Old West, Jazz Age, Space
  Race — rather than the modern nation) are both still open.
- **Category 2 — what does an actual observance look like?** None of the five aesthetic holidays have
  concrete practices attached yet (food, dress, decoration, ritual).
- **Category 3 — additional transcendent holidays?** The brainstorm file left this open too (Lunar New
  Year, Diwali, and Carnival are all real-world candidates with genuine global reach).
- **Category 3 — human vs. robot observance?** Do humans and robots mark these the same way, or
  differently?
- **Category 4 — moved to its own dedicated `TODO.md` item (flagged 2026-07-16)**, rather than staying
  a simple open question here — see "National Holidays — Category 4 (Celestial/Faction-Specific) needs
  its own dedicated investigation" for the full scope of what needs deciding (which faction(s), which
  specific astronomical event, and whether it's Kunlun-centered).
- **Independence Day's solstice date — deliberate or coincidental in-fiction?** Worth deciding
  explicitly whether June 21 was chosen by Tepenia's founders *for* its solstice significance, or
  whether that's a resonance the audience notices without it being an in-world intentional choice.
- **Does every city observe Independence Day identically**, or does the Hut Point remembrance ritual
  stay unique to Scott/Fort McMurdo while other cities mark the day differently?
- **The full Tepenian Saints framework** remains separate, still-open work (`TODO.md`).
