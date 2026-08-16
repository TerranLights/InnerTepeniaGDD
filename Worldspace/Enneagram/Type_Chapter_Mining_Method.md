# Per-Type Chapter Mining Method

**Purpose:** a repeatable process for mining each of the remaining 8 Enneagram types (2–9) into their own
`Type_N_The_Name/` folder, built from what was actually learned extracting Type One — including two rounds of
gaps the developer caught after a first pass looked "done." This file exists so those same gaps don't recur:
every named section from both source chapters has an assigned destination below, checked off against the
finished Type One folder as ground truth.

**Folder shape (confirmed on Type One):** `README.md` + `Core_Psychology.md` + `Subtypes.md` + `Growth_Path.md`.
Identical shape for every type.

---

## Step 1 — Locate both chapters

**The Wisdom of the Enneagram (gold standard).** Scanned PDF; page offset is **PDF page = book page + 10**,
confirmed against Chapters 1–8 (Type One starts PDF p.107 = book p.97; Type Two starts PDF p.135 = book
p.125). Book-page chapter starts, per the TOC: One 97, Two 125, Three 151, Four 178, Five 206, Six 233, Seven
260, Eight 287, Nine 314, Part III (spiritual practice, out of scope) 341. **Spot-check every chapter start
with a keyword search anyway** (`pdftotext -f <page> -l <page>` + grep for "TYPE <NAME>") before trusting the
arithmetic — scanned books can have irregular plate/insert pages that shift the offset locally.

**The Complete Enneagram: 27 Paths (secondary reference).** Native (non-scanned) PDF, no fixed page-offset
formula found. Types run in **reverse order** starting at Chapter 3 (confirmed: Chapter 3 = "The Point Nine
Archetype," Chapter 11 = "The Point One Archetype" at PDF p.363). Inferred mapping — **confirm each one before
use, don't trust the arithmetic blind**: Ch.3=Nine, Ch.4=Eight, Ch.5=Seven, Ch.6=Six, Ch.7=Five, Ch.8=Four,
Ch.9=Three, Ch.10=Two, Ch.11=One. Locate each chapter by grepping page-by-page for `"CHAPTER <N>"` and `"The
Point <Name> Archetype"`.

Extract each chapter's full text with `pdftotext -layout` (Wisdom) or plain `pdftotext` (Chestnut — no layout
needed, single-column) before reading, same as Type One.

---

## Step 2 — Section-by-section destination map

**Rule of thumb that caused the Type One gaps:** *Wisdom* gives each average-range pattern its own **named
essay section** (e.g. "Being Critical and Judgmental"). Do not silently fold these into Chestnut's shorter,
differently-named "Key Traits" — write each one up as its own labeled subsection in `Core_Psychology.md`,
cross-referencing Chestnut's overlapping trait by name where relevant. Compressing named sections into
paraphrase is exactly what got missed the first time.

### From *Wisdom* (per type chapter)

| Chapter location | Destination | Notes |
|---|---|---|
| Chapter title + nicknames/epithets | `README.md` header | |
| Riso-Hudson TAS (15-statement self-test) | *skip* | self-report tool for a live human test-taker; not usable for assigning type to an already-written fictional character |
| TAS scoring key → misidentification data ("[Type] most likely misidentifies as...") | `Core_Psychology.md` → **Misidentification** | keep — real differentiation data |
| Descriptor line, Basic Fear / Basic Desire / Superego Message sidebar | `README.md` table | cross-check against the Fear/Desire already in `../Foundations_and_Practice.md` — should match; flag if it doesn't |
| Main narrative/overview essay | `README.md` → **Overview** | merge with Chestnut's archetype-overview paragraph |
| Childhood Pattern (named anecdotes) | `Core_Psychology.md` → **The Childhood Coping Strategy** | merge with Chestnut's Early Coping Strategy; anecdotes go in unattributed, no names from the book |
| 2 Wing subtypes — healthy/average descriptions | `Subtypes.md` → **The Wings** | full |
| Wing subtypes' named real-world example lists | `README.md` → **Who This Type Looks Like** | trimmed to ~5 names per wing (developer's explicit call on Type One) — quick flavor, not the full 10-name list |
| 3 Instinctual Variants — average/unhealthy descriptions + nickname each | `Subtypes.md` → **The Instinctual Subtypes** | merge with Chestnut's deeper per-subtype treatment (see below) |
| The Wake-up Call | `Growth_Path.md` → **The Wake-up Call** | |
| Full 9-Level stack (paired labels + mechanism paragraph per level) | `Growth_Path.md` → **The Nine Levels of Development** | all 9, table format |
| The Social Role (named) | `Growth_Path.md` → **The Social Role** | |
| Named average-range essay sections (count/names vary by type — e.g. for One: Anger/Resentment/Frustration, Striving After the Ideal, Being Purposeful and Making Progress, Being Right and Pointing Out Problems, Order/Consistency/Punctuality, Self-Control and Self-Restraint, Being Critical and Judgmental, The Inner Critic and Perfectionism) | `Core_Psychology.md` → **The Average-Range Patterns, In Full** | **one named subsection per book section — this is the step that got compressed away the first time. Do not skip.** |
| Reflection/journaling callout boxes embedded in those essay sections | Check each one individually — see the callout-box rule below | |
| Disintegration narrative ("Reacting to Stress: X Goes to Y") | `Growth_Path.md` → **Integration & Disintegration** → Wisdom's framing | cross-ref the existing numeric chart in `../Enneagram_Dynamics.md` |
| The Red Flag + Warning Signs + named Potential Pathology | `Growth_Path.md` → **The Red Flag** | keep all 3 parts, including the named clinical disorders |
| "Practices That Help [Type] Develop" bulleted list | `Growth_Path.md` → **Practices & Techniques for Growth** → General practices (Wisdom) | full list |
| The [Type]'s Gifts | `Growth_Path.md` → **The [Type]'s Gifts** | |
| Path of Integration narrative ("X Goes to Y"), incl. the non-imitation caveat | `Growth_Path.md` → **Integration & Disintegration** → Wisdom's framing | **always preserve the explicit non-imitation caveat** ("integrating doesn't mean imitating the target type's average behavior") — it recurs every chapter and is load-bearing for companion-writing |
| "Transforming Personality into Essence" / closing Essence passage | *Check before skipping* | usually pure spiritual-practice color and safe to compress to nothing — **but for Type One this section contained the judgment-vs-discernment distinction**, a real structural idea, which got moved into "Being Critical and Judgmental" instead of dropped. Read it before deciding it's decorative. |
| Opening epigraph quotes | *skip* | decorative |

**The callout-box rule:** every named callout box (`SMALL CAPS TITLE`, boxed aside) gets *individually*
evaluated, not bulk-dropped:
- If it's a genuine repeatable exercise/technique (Type One examples: Broadening Your View, Identifying Escape
  Hatches, The Running Commentary, Compulsive Organizing, Unattainable Standards, Disappointment) → add as its
  own bullet under `Growth_Path.md`'s **Technique-by-pattern** or **General practices** section.
- If it's a pattern-naming aside with no separate exercise (Type One examples: Lonely Responsibility, Parenting
  Grown-Ups) → fold directly into the relevant prose paragraph (e.g. into the Social Role writeup), don't give
  it a bullet of its own.
- Never drop one without deciding which of the two it is first.

### From *Complete Enneagram* (per type chapter)

| Chapter location | Destination | Notes |
|---|---|---|
| Chapter title + epigraph quotes | *skip epigraphs* | |
| Archetype overview paragraph (superego framing, "fatal flaw") | `README.md` → **Overview** | merge with Wisdom's narrative |
| "[Type] Archetype in Homer's *Odyssey*" | `README.md` → one compressed paragraph, alongside the Dante parallel below | flavor only — do not expand into its own section or file |
| "[Type] Personality Structure" (Triad placement + core mechanism) | Woven into `Core_Psychology.md`'s opening | don't re-describe the Triad itself (already in `../Triads_Wings_and_Variants.md`) — only the type-specific mechanism detail is new |
| "The Early Coping Strategy" (named anecdote) | `Core_Psychology.md` → **The Childhood Coping Strategy** | merge with Wisdom's Childhood Pattern; anecdote unattributed |
| "The Main [Type] Defense Mechanism: [Name]" | `Core_Psychology.md` → **The Main Defense Mechanism: [Name]** | always its own named subsection |
| "The [Type] Focus of Attention" | `Core_Psychology.md` → **Focus of Attention** | |
| "The [Type] Emotional Passion: [Name]" | *Cross-check only* | should already match `../Foundations_and_Practice.md`'s Nine Passions table — flag, don't duplicate, if it doesn't match |
| "The [Type] Cognitive Mistake: '[belief]'" + bulleted core beliefs | `Core_Psychology.md` → **The Cognitive Mistake** | full bullet list |
| "The [Type] Trap: '[description]'" | `Core_Psychology.md` → **The Trap** | |
| "The Key [Type] Traits" (named, count varies by type) | `Core_Psychology.md` → **Key Traits (Chestnut)** | all named traits |
| "The [Type] Shadow" | `Core_Psychology.md` → **The Shadow** | merge with any Wisdom shadow material rather than duplicating |
| "The Shadow of the [Type] Passion: ... in Dante's *Inferno*" | `README.md` → same compressed literary-parallel paragraph as the Odyssey entry | flavor only |
| "The Three Kinds of [Type]s" subtype intro | `Subtypes.md` → one-line intro to **The Instinctual Subtypes** | |
| 3 Instinctual Subtype write-ups (nickname, mechanism, differentiation-from-confusable-types, anecdote) | `Subtypes.md` → **The Instinctual Subtypes** | merge with Wisdom's average/unhealthy descriptions per subtype |
| **Countertype flag** on one of the three subtypes | `Subtypes.md`, in that subtype's own entry | Chestnut-only concept, doesn't exist in Wisdom — never drop it |
| **Differentiation from confusable types** (e.g. "how to tell a Self-Pres One from a Six") | `Subtypes.md`, in that subtype's own entry | Chestnut-only, genuinely useful, always keep |
| "'The Work' for Type [X]" section intro | *skip* | purely transitional |
| "Self-Observation" (named patterns to notice, usually 3) | *Cross-check only* | should already be covered by `Core_Psychology.md`'s merged Key Traits / Average-Range Patterns — use as a completeness checklist, not a new content source |
| "Self-Inquiry and Self-Reflection" (reflective questions) | `Growth_Path.md`, folded into **Technique-by-pattern** as brief "self-inquiry prompts" | summarize rather than reproduce in full — the underlying questions ("why did this form," "what does it protect against," "what are the blind spots") are mostly the same generic meta-questions reapplied per pattern |
| "Self-Development" → "What to Do" (named techniques per pattern) | `Growth_Path.md` → **Technique-by-pattern (Chestnut)** | full — one subsection per pattern, every named technique. **This whole layer was missed entirely on the first Type One pass — check it explicitly.** |
| "The Inner Flow" (arrow-line reframe: growth-stress point / child-heart-security point) | `Growth_Path.md` → **Integration & Disintegration** → Chestnut's reframe | same two numeric directions Wisdom already gives — this is a different *reading* of them, not new numbers |
| "The Vice to Virtue Conversion" + per-subtype growth notes | `Growth_Path.md` → **Vice → Virtue** | full, including every subtype-specific note |
| "Conclusion" | *skip* | restates already-captured themes |

---

## Step 3 — General handling principles

- **Distill, never reproduce verbatim.** Original wording throughout, per this project's standing book-mining
  practice (see `../Foundations_and_Practice.md`'s own header).
- **Named interview-subject anecdotes** (e.g. Type One's Cassandra, Derek, Francis, Sally): fold the
  illustrative pattern into prose, unattributed — never quote the passage or use the book's name for the
  person.
- **Named real-world public figures** (Wing examples): relocate to `README.md`, trimmed to ~5 per Wing, framed
  as "quick examples of what this type looks like," not reproduced as the book's full list.
- **Literary parallels** (Homer, Dante): one compressed paragraph each in `README.md`, never their own file or
  section — flavor, not mechanism.
- **Cross-references, not duplication:** where a concept is already fully covered in `../Foundations_and_Practice.md`,
  `../Triads_Wings_and_Variants.md`, or `../Enneagram_Dynamics.md` (Centers, Hornevian/Harmonic groups, the
  Passion itself, the numeric Integration/Disintegration chart), link back to it rather than re-describing it
  inside the type folder.

## Step 4 — Completeness checklist (run before calling a type folder done)

By the end, `Core_Psychology.md` should contain, as separate headers: Childhood Coping Strategy · Main Defense
Mechanism · Focus of Attention · Cognitive Mistake (+ belief list) · The Trap · Key Traits (Chestnut) · **one
subsection per named Wisdom essay section** (varies by type, typically 6–8) · The Shadow · Misidentification.

`Subtypes.md` should contain: both Wings (healthy + average) · all three Instinctual Subtypes, each with a
merged mechanism description, its Countertype status stated explicitly (yes/no), and its differentiation notes
from confusable types.

`Growth_Path.md` should contain: Wake-up Call · Social Role (with any "naming" callouts folded in) · full
9-Level table · Red Flag + Warning Signs + Potential Pathology · General practices (Wisdom) · every genuine
callout-box technique as its own bullet · Technique-by-pattern (Chestnut) · Gifts · Integration & Disintegration
(both books' framings, side by side) · Vice → Virtue (+ per-subtype notes).

`README.md` should contain: nicknames · descriptor line · Fear/Desire/Superego Message/Passion/Virtue table ·
Overview paragraph · one compressed literary-parallels paragraph · Who This Type Looks Like (trimmed Wing
examples) · links to the other 3 files.

If a section in the checklist above has no content once a chapter is actually read, that's fine — not every
type's chapter uses every structural element. The checklist exists to force a deliberate "not present in this
chapter" decision, not to guarantee uniform length across all 9 types.
