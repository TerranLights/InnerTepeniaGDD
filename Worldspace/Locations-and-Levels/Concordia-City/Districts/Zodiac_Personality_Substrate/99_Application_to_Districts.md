# Applying the Substrate to Districts

**Written 2026-08-29**, after the extraction pass completed. This file is the bridge: the other files are
reference, this one says how to actually use them without the scaffolding showing.

---

## 1. The one rule that governs everything else

**The zodiac is scaffolding. It comes down before anyone sees the building.**

The correct workflow is:

> read the substrate → derive district culture → **write the culture in the district's own terms** → discard
> the zodiac vocabulary entirely

A finished district entry should be indistinguishable from one written without this folder. If a reader of
`District_Canon_Reference.md` could reconstruct which sign a district maps to, the pass has failed.

Concretely, the following must never appear in district canon, questlines, dialogue, item names, signage, or
any player-facing text: sign names as labels, element names as district descriptors ("the Fire district"),
aspect vocabulary (square, trine, opposition, quincunx), modality vocabulary (cardinal, fixed, mutable),
planetary rulers, decans, or any in-world astrological practice, belief, or naming.

What *does* transfer is the **content**: a specific fear, a specific institutional failure mode, a specific
material palette, a specific reason two districts cannot hear each other.

**Worked example of the translation.** The substrate says Cancer has Saturn in detriment and Mars in fall,
therefore the district structurally cannot set limits and nobody in it fights for themselves. The district
canon says: *the Sanctuary has no mechanism for refusing a request, and residents who need something advocate
for a dependent rather than for themselves — a resident with no ward has no standing to ask.* Same finding.
No scaffolding.

---

## 2. What each file actually gives you

| File | Use it for |
|---|---|
| `01`–`12` (signs) | The primary source. One district's psychology, shadow, needs, and texture. Start here. |
| `13_Ophiuchus_Hub` | The Hub. Structurally different from the others — read its §1 before using it. |
| `A_Elements` | Grouping districts into four temperament families; **inter-family friction** |
| `B_Modalities` | How a district relates to **change**: initiates, holds, or dissolves. The most directly civic axis. |
| `C_Polarity` | Which districts have a **voice** and which do not. Largely redundant with Elements — its value is §5. |
| `D_Aspect_Geometry` | **The inter-district conflict and affinity system.** The spine for any relationship work. |
| `E_Decans` | Optional. Splitting one district into three sub-neighborhoods. Weakly sourced — treat as a menu. |
| `F_Rulerships` | **The best generator of structural district flaws.** See §4 below. |
| `G_Correspondences` | Material texture: stone, metal, color, plant, pathology. Filtered for Antarctic enclosure. |

---

## 3. The layer model — how the axes stack

Each district gets four independent readings that should agree in tone and differ in content:

1. **Enneagram** (already established, `Regional-Characteristics/district_by_Enneagram_group_series.md`) —
   *psychological motive*. Why the district wants what it wants.
2. **Element** — *temperament family*. How it processes experience.
3. **Modality** — *relationship to change*. Whether it starts, holds, or adapts.
4. **Dignity** (`F_Rulerships`) — *capability profile*. What it is structurally good at and structurally cannot do.

Where two axes agree, the trait is well-grounded. Where they disagree, that is usually a finding rather than an
error — see §6.

---

## 4. The most productive single technique: the dignity reading

This surfaced repeatedly during extraction and is the strongest generator in the folder. The pattern:

> A planet in **domicile or exaltation** in a sign = a faculty the district is structurally excellent at.
> A planet in **detriment or fall** = a faculty that works against the grain there, is distrusted, or has no
> institutional home.
> **The district's characteristic failure is what its weak faculty was supposed to prevent.**

It produces flaws that feel inevitable rather than assigned, and — critically — flaws with **no villain**,
which matches this project's established non-malice discipline. Examples the pass produced:

- **The Sanctuary** — Saturn detriment, Mars fall. Cannot set limits; nobody advocates for themselves.
- **Scorpio** — Venus detriment, Moon fall. Its structural deficit is *gentleness*; it can only import comfort
  or substitute endurance and call it care.
- **The Power Core** — Venus detriment, Saturn fall. Its two missing capacities (valuing others, patient
  discipline) are also its two natural adversaries.
- **The Markets** — Mercury holds *both* detriment and fall, the only such case in the system. Verification has
  no institutional home: contracts personal, provenance unrecoverable, disputes settled by reputation. Venus
  exalted gives it the highest valuing capacity in the table. It can price desire better than anyone in the
  city and structurally cannot keep a ledger.

---

## 5. City-level findings the substrate produced on its own

These emerged from **four different agents working from four different slices**, converging independently.
They are the most valuable output of the pass and they describe Concordia, not any one district.

### 5a. Concordia has a structural accountability hole

Four separate lines of evidence:

- **The Air grand trine.** The Circuit (information), the Government District (governance), and the Labs
  (research) are mutually trine — a closed, self-agreeing loop. Its documented failure mode is "mental
  inertia… a perpetual student": detachment mistaking itself for action. **Each member's corrective opposition
  sits outside the triangle**, so the three have no structural reason to check one another.
- **Polarity.** Every organ the city *speaks* through is Active; every organ it *survives* through — care,
  housing, industry, goods, maintenance — is Receptive, and has no native channel. Receptive distress is
  structurally silent until it is structural. Budget follows voice: capacity funded in advance, upkeep funded
  reactively after failure.
- **The Hub.** Every district has an opposition whose function is to check it. Ophiuchus has no aspects at all.
  **Nobody was ever assigned to check the Hub.**
- **Modality.** The four Cardinal districts sharing one budget do not *experience* emergencies; they
  **manufacture** them, because initiators cannot tolerate deadlock and crisis is the only lever that breaks
  one.

Together: the districts that keep Concordia alive cannot speak, the districts that speak cannot be checked, and
the resulting deadlocks are broken by manufactured crisis. **No villain anywhere in it.**

This bears directly on an open question in `District_Canon_Reference.md` — whether Libra cultivates the
Perpetual Emergency or merely benefits from it, which canon says "cannot be answered." The substrate supplies a
third answer: *nobody cultivates it; the structure produces it, and the Government District merely holds the
convening lever.*

### 5b. The Undergrid and the Markets are the same faculty at opposite settings

Three agents converged here. Mercury **rules and is exalted** in Virgo; Mercury holds **both detriment and
fall** in Pisces. So District 12 and District 10 are maximum and minimum on the single faculty of
*verification* — the cleanest structural opposition the system produces, and the reason crackdowns on the
Markets strengthen rather than weaken it.

### 5c. Two narrative pairings that came out of the sources by accident

- **Judas → Matthias.** The apostolic correspondence gives Aquarius (the Labs) **Judas**, and Pisces (the
  Markets) **Matthias — the replacement elected to fill Judas's vacated seat.** Adjacent districts, linked as
  betrayer and successor.
- **Chiron → Asclepius.** Sagittarius (the Frostlands) *taught* Ophiuchus (the Hub). Their territorial overlap
  is therefore a teacher-pupil relationship in which the pupil surpassed the teacher and was destroyed for it.
- **The Hub's emblem is not its own.** The caduceus appears in the sources attributed to Gemini and to Libra's
  heraldry, and **never once to Ophiuchus.** The Information and Government districts hold the Hub's symbol.

### 5d. The largest unexploited design space

**None of the four district pairs canon has developed is a square or an opposition.** The existing Enneagram
pass found only affinity pairings. All **six oppositions and twelve squares remain completely unused** by
district canon. If more inter-district conflict is wanted, it is sitting there already derived in
`D_Aspect_Geometry.md` §5.

---

## 6. When the substrate disagrees with existing canon

**Canon wins. Always.** This folder is proposed reference, not established fact, and every district already has
Deep Dives, Vision Notes, and Canon Reference entries that outrank it.

But record the disagreement rather than silently dropping it — a mismatch is often the more interesting result:

- Where the aspect geometry and the Enneagram pass agree (the Labs/Circuit trine; the Sanctuary/Taurus
  sextile), the pairing is **doubly grounded** and safe to build on hard.
- Where they disagree, read them together before discarding either. The Power Core/Markets and Government
  District/Undergrid pairs are *semi-sextiles* — signs sharing zero structure — where the Enneagram found total
  overlap. Read jointly, that describes **two districts with identical motives and no shared language for
  them**, which fits the existing canon conflict material better than either axis alone.

---

## 7. Standing cautions

- **⚠ The Shadow is not the district — and this folder's weighting will mislead you if you let it.** The
  per-sign files give §3 Shadow heavy weight because the *extraction* brief prioritised capturing failure
  modes. **That is an artifact of extraction, not a claim about how much of a district is shadow.** Applying a
  sign file proportionally to its own section lengths yields a district that is largely pathology, which is
  wrong. A district runs on its own sincere idea of doing good, and that idea mostly works; the shadow is what
  that pursuit produces unintentionally and unnoticed, discoverable only by a player who genuinely
  investigates. Full rule and the three tests: `../Phase_Instructions/00d_Shadow_Proportion_Discipline.md`.
- **Everything at institutional scale is derivation.** The source books describe individuals, not populations.
  The per-sign files mark derived material; preserve that marking when it lands in canon.
- **Do not flatten source disagreements.** Several were deliberately preserved (whether Scorpio is possessive;
  whether Capricorn is a workaholic or leaves promptly; Snodgrass's contrarian Aquarius). They are design
  menus, not errors to resolve.
- **Aspects are a grammar, not a verdict.** A square is not "these districts hate each other." It is a specific
  kind of friction: same tempo, different subject, no shared vocabulary.
- **Antarctic enclosure filters the correspondences.** Some are impossible here (citrus), some invert
  (synthesisable diamond is cheap; non-synthesisable opal is precious). `G_Correspondences.md` flags these.
- **Five districts still lack a settled in-fiction name** (Cancer, Virgo, Libra, Scorpio, Sagittarius). They
  need one before any player-facing content, and the name must not derive from the sign.
- **The Hub is not a thirteenth sign in a twelve-sign system.** It is the one that was left out so the system
  could stay symmetrical. Do not give it aspects, an element, or a modality to "complete" it — the absence is
  the content.

---

## 8. Suggested order of work

1. Pick a district. Read its sign file end to end.
2. Read its dignity row in `F_Rulerships.md` §5–6 — that is where its structural flaw comes from.
3. Read its row in `D_Aspect_Geometry.md` §5 for its conflicts and allies.
4. Check `A_Elements` and `B_Modalities` for its temperament family and its relationship to change.
5. Pull material texture from `G_Correspondences.md`, filtered for enclosure.
6. **Cross-check against the district's existing Deep Dive, Vision Notes, and Canon Reference entry.** Canon
   wins; note disagreements.
7. Write the district's culture in its own vocabulary. **Discard the scaffolding.**
8. Optionally, use `E_Decans.md` if the district wants three sub-neighborhoods.
