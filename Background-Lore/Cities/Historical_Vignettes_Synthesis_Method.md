# Historical Vignettes — Synthesis Method

**What this is:** the explicit instruction sheet for writing `[City]_Historical_Vignettes_and_
Informational_Sheets.md` entries. Written 2026-08-02 after an audit found 86 of 108 already-drafted
entries (Halley + Palmer + Mirny/Casey batches) had drifted into restating the source `[City]_Physical_
Infrastructure_Attributes.md` file's own state-of-being facts instead of synthesizing actual history.
Companion to `Historical_Vignettes_Progress_Tracker.md` (scope/targets/pacing) — this file is about
*what makes an entry correct*, not how many to write or in what order.

---

## The one-sentence rule

**An entry is history only if something happened.** Not "this exists," not "this is how it works,"
not "this was built for that reason" — something occurred, at some point, to someone or something, with
a before and an after.

## The test

Before finalizing any entry, ask: **could the Physical Infrastructure Attributes file alone have
answered this?** If the entry's entire content is "here's what attribute #N is, does, or was designed
for," the Attributes file already said that — the entry adds nothing an attribute list couldn't already
contain, because attribute lists describe steady states, not events. Delete and redraft.

## Two valid entry shapes — and only two

1. **Narrative vignette** — a specific incident, decision, dispute, discovery, loss, or change,
   involving a named person or a datable/placeable event, with an actual before/after or resolution.
   Example (approved, Byrd pilot): *The Locked Ward* — something specific happened in that ward, to
   specific people, and the entry tells you what.
2. **Informational sheet — statistics or records only.** Valid *only* when it presents actual data
   synthesized across many instances (a count, a log, a survey, a portrait built from numbers or named
   cases) that reveals a real pattern over time. Example (approved, Byrd pilot): *Pre-Exile Find Log: A
   Statistical Portrait* — real figures, a genuine discoverable pattern, not a description of what a
   building is for.

**There is no third shape.** "An informational sheet on X's own function/design/role" is not a valid
entry type — see Red Flags below.

## Red flags — these mean drift, redraft before writing

- Any entry that opens with a bracketed disclaimer like *"(An informational sheet on X's own founding-
  era purpose/function/design/role, not a single incident/night/voyage.)"* — this phrasing is the entry
  explicitly opting out of having an occurrence, which is backwards. In the 2026-08-02 audit, every
  single entry using this exact disclaimer pattern was flagged as drift.
- Titles shaped like "Built to X, Not Y" or "What X Actually Does/Means/Involves/Provides" — these read
  as function summaries by construction, and in the audit, entries with these title shapes were drift
  without exception.
- The body explains *why* a system was engineered a certain way, or *what* an institution's ongoing
  role is, without narrating a specific moment when something happened.
- No named person, no date, no specific decision/dispute/discovery/change — just a description of an
  ongoing state, however well-written.
- Anything that could be produced by taking an attribute bullet and expanding it into two paragraphs of
  prose without adding a single new fact.

## Green flags — what a passing entry actually looks like

- A named person doing, deciding, discovering, losing, or building something specific, once, with real
  stakes.
- A dispute or negotiation with an actual outcome — not "how disputes get resolved here" in the
  abstract, but a specific one, or a specific pattern of specific ones.
- A discovery — someone found, noticed, realized, or uncovered something, at an identifiable point.
- A record or statistic that required synthesizing many data points into a portrait — not a description
  of what an institution does, but what its accumulated records actually show.
- An event with a real before-state and after-state — something changed, broke, started, stopped, or
  was decided, and the entry is about that change.

## Process check, every entry, before moving on

Ask directly: **"What happened here, when, and to whom?"** If the honest answer is "nothing happened,
this is just describing the thing," the entry fails and needs to be redrafted around an actual
occurrence pulled from (or plausibly synthesized from) the same source material — not abandoned, just
re-angled. Nearly every Attributes file has enough surrounding material (Full Extrapolation sections,
Cross-Reference Findings, Community Infrastructure notes, named placeholder figures) to support a real
incident or a real named person's story instead of a function summary — the fix is usually to find the
person or moment already implied by the attribute, not to invent one from nothing.

## Source material inventory — priority order, developer-confirmed 2026-08-02

### Tier 1 — `[City]_Full_Extrapolation.md` (top priority, check this first)

Proposed answers to open questions; frequently names a placeholder Notable Figure with a specific
decision, discovery, or story attached. Every surviving HISTORY entry from the 2026-08-02 audit that
wasn't a pure attribute restatement came from here (Old Toby's prophecy, Ferreira-Whitcombe's platforms,
Joos Kaminari, the archivist who found the sealed compact). Best single source for named-person
vignettes — read it before anything else.

### What "synthesize" actually means here

These entries are new, standalone incidents derived from a city's own established state-of-being (its
configuration, industry, culture, geography, social scene) that plausibly could have happened given
those facts — the same way a specific building's attribute ("wind-rated structural reinforcement")
implies, but doesn't narrate, the actual day a specific storm tested it. The tiers below tell you *what's
true about the city*; the job is to invent the *specific occurrence* consistent with that truth — a
person, a dispute, a discovery, a decision, a record.

### Tier 2 — state-of-being (primary grounding)

- **`[City]_Physical_Infrastructure_Attributes.md`** — the city's configuration: buildings, systems,
  engineering, industry, quantities. The file every drifted entry was directly restated from — still the
  right grounding source, but only as the *fact* an occurrence gets built on top of, never as the
  entry's own content.
- **`Specs/[City].md`** — base facts (population, geography, climate). Check for a "Founding Story"
  subsection specifically, which may itself be occurrence-shaped.
- **`Local_Cultures/[Subnet]/[City].md`** — culture, holidays, tier tables, local social scene. A named
  holiday usually commemorates a specific real event — worth identifying what that event was.
- **`[City]_Community_Infrastructure.md`** — local industry and social infrastructure (Additions, Social
  Cohesion Mechanisms) — what exists to synthesize an occurrence around.
- **`[City]_Mega_Init.md`** — initial derivation notes, foundational descriptive facts.

### Tier 3 — occurrence material (sometimes already contains a usable incident)

- **`[City]_Cross_Reference_Synthesis.md`** — a mix. Some Findings describe an actual incident ("the day
  the Depot changed hands," a specific accidental discovery); others just connect two state facts
  analytically with no occurrence at all. Read each Finding individually — don't assume the file as a
  whole is usable.

### Tier 4 — ready-made occurrences (`Course_of_Events` specs) — lowest weight

- **`Background-Lore/Cities/[Subnet]/[City]/Course_of_Events/[City]_NN_*.md`** (11 files/city, all 35
  DLC cities) and **`[City]_Course_of_Events_Suggestions.md`** — genuinely occurrence-shaped (State of
  Affairs → Trigger → Conflict → Culmination → 2nd/3rd-Order Change), but this is a **separate,
  already-sequential methodology**, explicitly distinct from this one per the Progress Tracker's own
  opening note. These entries are supposed to be independent and non-sequential; pulling from an
  already-chained, timeline-anchored source works against that. Ranked lowest, not excluded outright —
  don't build a batch around this tier, and don't try to reconcile a drafted entry against it. Whether a
  standalone occurrence eventually lines up with a Course_of_Events chain is a future problem, not
  something to solve while drafting.

### Tier 5 — supplementary, check case-by-case, don't rely on by default

- **`Neo-Races-and-Cultures/[Subnet]/[City]/[City]_Catalog.md`** — mostly demographic weighting data;
  its "Synthesis Notes" (Phase 2) section occasionally has interpretive content worth a spot-check.
- **`District_Refugee_Diaspora_Composition.md`** (Concordia-side, cities with diaspora entries) — "brought
  with them" items sometimes name a specific transplanted practice or event.
- Companion/Notable Figures character files, where one connects to the city in question.
- **`README.md`** (per-city megasheet) — a static concatenation of the other files, not new content;
  skip as a source, it adds nothing the component files don't already have.

## Relationship to the war/destruction correction

This is a separate, additive rule to the earlier 2026-08-02 correction about not over-indexing on
war/ruins destruction as the default organizing fact (see the Progress Tracker's own Session Log entry
for that correction). Both rules apply together: an entry needs to be a genuine occurrence, **and** it
shouldn't default to "the war happened to this place" as that occurrence more than roughly once per
6-entry batch. A pre-war founding-era incident, a mid-history dispute, a specific discovery, or a
present-day person's specific circumstance are all equally valid ways to satisfy the history requirement
without leaning on destruction.
