# Zodiac Personality Substrate — Method and Sources

**Built 2026-08-29.** A data-extraction pass over eight astrology books, mined to serve as a **personality
design substrate** for Concordia's thirteen districts. Sibling in purpose to
`Regional-Characteristics/district_by_Enneagram_group_series.md`, which supplies each district's *psychological
motive*; this folder supplies **temperament family, material texture, shadow expression, and a conflict
geometry**.

---

## ⚠ THE BINDING CONSTRAINT — read before using anything in this folder

**The zodiac is not, and has never been, in-fiction in this project.**

No character or planner in Concordia's history ever intended to build districts mirroring the zodiac. The
districts developed organically, shaped by their own specific historical pressures. The zodiac is purely the
developer's out-of-fiction organizing shorthand — a way to keep thirteen districts from feeling like "the same
district with twelve different paint jobs."

**Therefore:**

- Everything in this folder is **design input**. None of it is lore.
- Never write in-fiction prose implying an in-world zodiac plan, astrological belief, or zodiac-derived naming.
- Anything the player actually encounters — signage, dialogue, item names, minigames — must use each district's
  **real in-fiction identity** (The Sanctuary, The Power Core, The Yards, The Labs, The Markets, The Frostlands,
  The Undergrid, Axis Mundi, and so on). Note that several districts (Cancer, Virgo, Libra, Scorpio,
  Sagittarius) still lack a settled in-fiction proper name and would need one first.
- The correct use of this material is: *read the substrate → derive district culture → write the culture in the
  district's own terms, with the zodiac scaffolding discarded.*

See `feedback_zodiac_districts_not_infiction` in project memory for the full standing correction.

## ⚠ SECOND CONSTRAINT — element-name collision

Tepenia already has an **eight-element robot elemental system** (with Platonic solids, Wu Xing, and Six
Perfections associations) assigned to **subnets**, and that system **is in-fiction**
(`Storyline/DLC-Questlines/Subnet_Symbolic_Associations.md`, `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Symbolic_Substrate/Robot_Elementals.md`).

The zodiac's **four classical elements** (Fire / Earth / Air / Water) in this folder are:
- a different system, of a different size,
- applied to **districts**, not subnets,
- and **out-of-fiction**.

Never conflate the two, and never write "the Fire district." Where this folder groups districts by classical
element, it is describing an out-of-fiction temperament family only.

---

## The corpus

Eight books, ~776,000 words, 2,884 pages, at `to-be-integrated/books/Zodiac/`.

| Source | Words | What it actually contributed |
|---|---:|---|
| Silva, *Zodiac Signs: The Ultimate Guide* | 349k | Omnibus of twelve single-sign books on an identical 9-chapter template. **Dominant source for shadow/dark-side material (226 hits) and decans (82).** Shallow prose, but the behavioral template — how a sign is recognized, at work, socially, what it needs, how its children are raised — maps unusually well onto district culture. Also the only real source on Ophiuchus. |
| Snodgrass, *Signs of the Zodiac* | 78k | Scholarly reference (Greenwood Press, 1997). **The best source for concrete texture:** myth, history, per-sign correspondences (stones, plants, colors, shapes, pathology), and influence on literature, art, and architecture. |
| Martin, *Mapping the Psyche* Vol. 2 | 73k | Aspect geometry and the twelve houses (life-domains). |
| Martin, *Mapping the Psyche* Vol. 1 | 66k | Jungian/psychological depth on planets and signs; rulerships. |
| Martin, *Mapping the Psyche* Vol. 3 (*Kairos*) | 64k | **Highest density of squares and oppositions in the whole corpus** (129/77) — the primary source for inter-sign conflict. |
| Silva, *Sun and Moon Signs* | 57k | Sign-combination logic; strong element coverage. |
| Tierney, *All Around the Zodiac* | 47k | Serious structural text; **best element/modality density in the corpus**. Strong on inter-element friction. |
| Emerson, *Behavioral Astrology* | 42k | Relationships between signs; decans. |

### Quality caveats — recorded honestly

- **Tierney is OCR'd from a scan.** Expect corrupted words (`elementhas`, `energg`, `acll tive`), dropped
  spaces, and stray line noise. Content is good and worth mining; individual quotations from it should be
  sanity-checked before being reused verbatim.
- **A ninth file was deleted.** The folder originally held two copies of Tierney. The 5.3 MB copy was an
  **image-only scan yielding zero extractable text** (84 images, 0 characters); the 72 MB copy has the same 84
  pages at higher resolution *plus* a text layer. The smaller file was strictly redundant and was deleted
  2026-08-29 with the developer's approval.
- **Coverage is even across the twelve signs** (1,109–1,833 mentions each), so no sign is under-served by the
  corpus itself. Where a per-sign file reports thin material, that is a real gap in the sources, not an
  extraction failure.
- **Ophiuchus is genuinely thin** — ~2,000 words corpus-wide. See below.

---

## Method

1. All eight PDFs converted to plain text (`pdftotext`).
2. **Per-sign slices** built mechanically. Silva's omnibus was segmented by sign-mention density in 50-line
   blocks (its `Part N:` headers exist only in the table of contents, not the body, and its chapter headings are
   inconsistent between signs — density segmentation proved robust where header-matching did not). The
   remaining seven books were sliced by paragraph-level keyword match with a ±4-line context window. Result:
   twelve balanced slices of 37k–63k words each.
3. **Cross-cutting thematic slices** built the same way for Elements, Modalities, Polarity, Aspect Geometry,
   Decans, Rulerships, and Ophiuchus.
4. One extraction agent per slice, working to a fixed 15-section template, instructed to prioritise shadow
   material and conflict geometry, to preserve concrete detail over generic summary, to record source
   disagreements rather than flatten them, and **to report gaps rather than pad**.

### Defects found in this method, and how they were fixed

The extraction agents caught several problems in the slicing itself. Recorded here because the same mistakes
are easy to repeat if this folder is ever extended.

- **The largest-run bug (found by three agents independently, fixed by a supplement round).** The Silva
  segmenter kept only each sign's *single largest* contiguous block and discarded the rest. Six signs — Gemini,
  Virgo, Scorpio, Capricorn, Aquarius, Pisces — therefore lost over half their Silva material, and Silva is the
  corpus's dominant source for **shadow content**, the single highest priority of this pass. Pisces had *zero*
  dark-side hits; Gemini and Virgo had three. **Fixed:** slices rebuilt using all blocks (~20–28k words each,
  up from ~7–15k), and all six files were revised by a second supplement pass. Every one now reports its
  dark-side gap closed.
- **Keyword slices miss passages that never use the keyword.** `_Elements.txt` was built on patterns including
  `\belemental\b` and "fire sign," and so missed Tierney's central passage on fire exhausting other elements —
  which says "elements" (plural) and names fire directly. The extracting agent correctly refused to attribute a
  quotation it could not find, and flagged it. The passage was then located in the source and restored to
  `A_Elements.md` §9 with verified wording. **Lesson: prefer over-inclusive patterns and accept the noise.**
- **A warning that over-claimed.** The correspondence brief was given a data-quality warning listing several
  suspected corruptions in Emerson's blocks. Three of those did not reproduce on inspection: the
  jade/peppermint "bleed" into Cancer is not text corruption (those values sit correctly under Capricorn — the
  per-sign agents were seeing a *slice-boundary* artifact of our own making), all twelve Tarot lines are
  present, and Aries's duplicate amethyst is independently corroborated by Snodgrass. Only two genuine
  corruptions exist: Cancer's `Element: Air` and Gemini's `Celestial Symbol: Deer`, both confidently
  correctable. **Lesson: a warning passed down to an agent is itself a claim, and should be checked, not
  trusted.** The agent was right to verify rather than accept.
- **Correspondences were reported truncated by every early sign agent — because they were looking in the wrong
  place.** Snodgrass's Appendix IV is keyed by **planet**, not by sign. Once that was understood, every sign's
  **metal** became recoverable through its ruler, and the derivation validated perfectly against the five signs
  that already had an independently-attested metal. This closed the metal gap for all twelve districts and
  falsified an explicit claim in `04_Cancer.md` that pearl, moonstone and silver "appear nowhere in the file" —
  they are all in the Moon row. Six sibling files were corrected accordingly.

### What the corpus genuinely does not contain

Distinct from our own defects above. Reported consistently and independently by nearly every agent:

- **Very little at collective or civic scale — but treat this claim with care.** These books overwhelmingly
  describe individual psychology and one-to-one compatibility rather than what a *population* of a temperament
  does, how it governs, or what institutions it builds. Most district-scale and institutional readings in this
  folder are therefore **derivation**, and the per-sign files mark them as such.

  **Qualified 2026-08-29.** An early, emphatic version of this note called it "the single largest limitation of
  the whole substrate." The supplement round showed that overstated: for Scorpio the "no civic or
  collective-scale material" verdict turned out to be **partly a slicing artifact**, and the recovered text
  contained institutional material after all (an employer loyalty-exclusivity rule, a two-stage tribe-admission
  test, an eighth-house resources/estates assignment, and the corpus's only description of this type
  *concentrated in numbers* — which is what a district actually is). Aquarius similarly gained six
  institutional footholds it was previously reported as lacking entirely.

  **The generalisable lesson, worth applying to any future pass:** a gap logged against a single source should
  trigger an extraction check before it is trusted. Several confident "the corpus is silent on X" findings in
  this folder were really "our slice was silent on X." The gaps that survived re-checking are real; the ones
  recorded before the supplement round should be re-verified before anyone relies on them.
- **Silva has real structural holes, not only slicing ones.** He has no dark-side or decan chapter for Virgo at
  all, and no "What Does the Aquarius Need?" chapter — confirmed against the fully reassembled text.
- **Decans are weak.** Only two of eight books mention them.
- **Ophiuchus is very thin** (~2,000 words corpus-wide, in two books).

---

## The thirteenth district

Concordia has thirteen districts; the zodiac has twelve signs. The **Hub (Axis Mundi)** has no sign.

Rather than leave it undefined, it is assigned **Ophiuchus, the rejected thirteenth sign** — decided
2026-08-29. The rationale is structural and unusually apt:

> Ophiuchus is real, historically acknowledged by the same civilizations that built the zodiac, and physically
> present in the sky along the ecliptic. It was omitted for **symmetry**: twelve signs give four elements × three
> signs, and three modalities × four signs, and map cleanly onto a twelve-month calendar. A thirteenth breaks
> every one of those patterns. It is excluded not for being insignificant, but because counting it would break
> the system everything else depends on.

That is already the Hub's established character — the district whose culture "grew from the absence of an
assigned identity altogether," which belongs everywhere and nowhere. Ophiuchus also *overlaps the range of
another sign* (Sagittarius), which gives a second hook: a district occupying space another district considers
its own.

Because the corpus is thin here, `13_Ophiuchus_Hub.md` leans more on derivation from structural position than
on source volume, and says so explicitly.

---

## File index

- `00_Method_and_Sources.md` — this file
- `01_Aries.md` … `12_Pisces.md` — the twelve signs, in zodiacal order
- `13_Ophiuchus_Hub.md` — the thirteenth district
- `A_Elements.md` · `B_Modalities.md` · `C_Polarity.md` — the temperament groupings
- `D_Aspect_Geometry.md` — the inter-district conflict and affinity system
- `E_Decans.md` — three sub-flavors per sign; candidate sub-neighborhood texture
- `F_Rulerships.md` — planetary rulers, including traditional/modern splits
- `99_Application_to_Districts.md` — how to actually use all of the above

### Sign → district mapping

| Sign | District | Role |
|---|---|---|
| Aries | 5 — The Power Core | raw survival / energy |
| Taurus | 2 — Taurus | residential / stability |
| Gemini | 9 — The Circuit | information / communication |
| Cancer | 1 — The Sanctuary | nurturing / protective |
| Leo | 3 — Leo | cultural / performative |
| Virgo | 12 — The Undergrid | maintenance / service |
| Libra | 8 — The Government District | diplomatic / balance |
| Scorpio | 4 — Scorpio | psychological / transformative |
| Sagittarius | 11 — The Frostlands | frontier / exploration |
| Capricorn | 6 — The Yards | industrial / ambition |
| Aquarius | 7 — The Labs | visionary / experimental |
| Pisces | 10 — The Markets | black market / underworld |
| *Ophiuchus* | 13 — Axis Mundi (Hub) | neutral crossroads / governance nexus |

---

## What is deliberately NOT in this folder

**No district canon was modified to build this.** `District_Canon_Reference.md`, the thirteen Deep Dives, the
thirteen Vision Notes, and `district_by_Enneagram_group_series.md` are all untouched. Expanding each district's
personality *using* this substrate is the next piece of work, and it is deliberately separate — this folder is
the reference, not the application.
