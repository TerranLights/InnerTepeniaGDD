# PTSD / Military Trauma Research — Extraction Checklist

**Purpose:** working extraction log for real clinical/psychological/ethical source material on combat trauma,
PTSD, TBI, military service, and reintegration — sourced from `to-be-integrated/books/PTSD/` (10 books, 42MB).

**Primary intended use, right now:** filling in the wide-open character profile of **[NAME TBD], the Cancer
district's single most-esteemed Upper Earth ex-military defector** —
`Worldspace/Characters/Humans/recruitable/Unnamed_Cancer_Defector/README.md`. As of this folder's creation,
nearly everything about him is still TBD: name, full backstory, chronic wartime injuries, voice, personal
questline. Confirmed so far: 1w2 Social Enneagram, MACHINE stats (Nerve 10, Engine 9, Investigation 7),
mid-to-late-30s/early-40s, Boone/Great Khans-style standing in Cancer (grudgingly respected there, contempt
almost everywhere else in Concordia). See that README for full existing context before using anything below.

**Secondary use, explicitly instructed by the developer:** this material may also apply to the **Outer Tepenia
trilogy** and the **Cryptograph Helix** novel series — both share this repo (`Neo-Races-and-Cultures/
Orbital_Cryptograph_Helix_Era/` is the existing crossover folder). **Standing instruction: keep anything that
even possibly applies in any form, even if it doesn't fit the Cancer defector specifically** — flag
cross-series/cross-context applicability explicitly in each file rather than silently discarding material that
isn't a direct match for one human ex-military character.

**Status: research only, not canon.** Same discipline as `Ice-Cold_Buddhism_Research/` and
`Vostok_Genetics_Research/` — nothing here is settled until the developer signs off.

**Resumability note:** this file is the source of truth for what's done. Full plaintext extractions of every
source (via `pdftotext -layout`, or `pandoc` for the one epub) live at
`/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/405de404-1bd0-4762-8637-e6227efc004b/scratchpad/PTSD_fulltext/`
— that's a session-scoped scratchpad, not part of the repo, so if it's gone in a future session, regenerate
from the source PDFs/epub in `to-be-integrated/books/PTSD/` before re-reading (2 minutes of work, not a blocker).

---

## Output files in this folder

**Status update, 2026-08-29, same session:** the first dispatch of 7 parallel agents hit a hard **session-wide
API usage limit ("You've hit your session limit · resets 11:10pm America/Los_Angeles")** partway through. Two
agents finished and wrote their files before being cut off; a third agent's rich sub-agent output survived in
the coordinating session's own context and was hand-consolidated into its file directly rather than lost. Four
books never got a usable pass. **Resume the four `[ ]` rows below once the usage limit resets** — don't
re-dispatch before then, it will just fail again immediately.

| File | Source book | Pages | Status |
|---|---|---|---|
| `01_Military_Ethics.md` | *An Introduction to Military Ethics* (Bill Rhodes) | 177 | `[x]` **Done.** 507 lines. Retry succeeded after the session-limit reset |
| `02_Understanding_Combat_PTSD.md` | *Understanding Combat Related PTSD* (Walter F. McDermott) | 211 | `[x]` **Done.** 682 lines |
| `03_Haunted_by_Combat.md` | *Haunted by Combat* (Paulson & Krippner) | 201 | `[x]` **Done.** 190 lines |
| `04_Hidden_Battles_TBI_and_PTSD.md` | *Hidden Battles on Unseen Fronts* (Driscoll) — epub | ~10,528 lines plaintext | `[x]` **Done.** 264 lines |
| `05_Neuropsychology_of_PTSD.md` | *Neuropsychology of PTSD* (Vasterling & Brewin) | 352 | `[x]` **Done.** All 13 chapters read in full; Ch. 1-6/8/10/12 at full depth, Ch. 7/9/11/13 condensed with reasons stated. Includes a flagged, clearly-marked-speculative robot-cognition cross-application section |
| `06_Invisible_Wounds_of_War.md` | *Invisible Wounds of War* (RAND/Tanielian) | 499 | `[x]` **Done.** |
| `07_Treating_PTSD_Clinical_Handbook.md` | *Treating PTSD in Military Personnel* (Moore & Penk) — **two editions found**: 2011 1st ed. (401p) and 2019 2nd ed. (482p) | 482 (+401 spot-check) | `[x]` **~75% done, updated 2026-08-30.** 2nd ed. lines 1-14,950 of 21,422 now covered (front matter + Ch.1 in full, through Ch.18 opening). **1st-edition spot-check now complete** — 3 genuinely dropped chapters/appendices (VRET, Anger/Aggression/Violence, Appendices A-C) read in full and merged in. **Still not done:** 2nd-ed. Ch.18 continuation through Ch.23 (lines ~14,950-21,422 — sleep disorders, suicidal ideation, moral injury, complex trauma, posttraumatic growth). Moral injury (Ch.21) and posttraumatic growth (Ch.23) flagged as the two highest-priority chapters for any future pass. A second dispatch aimed at this range did not return usable results — resume at line ~14,950 if this thread continues |
| `08_Living_and_Surviving_in_Harms_Way.md` | *Living and Surviving in Harms Way* (Freeman, Moore, et al.) | 546 | `[x]` **Done.** 988 lines, full front-to-back pass, all 23 chapters. Low-yield chapters (Women in the Military, assessment instruments, pharmacotherapy dosing, military children, a veteran-support-website directory) explicitly compressed with reasons stated at each heading |
| `09_Military_Life_Four_Volumes.md` | *Military Life: The Psychology of Serving in Peace and Combat* (Adler, Castro, Britt, et al.) — TOC-triaged given size, not read at uniform depth throughout | 1072 | `[x]` **Done.** 1,248 lines, 87 findings. Full TOC (4 volumes/44 chapters) recovered and recorded since it exists nowhere else in this repo. Full depth on combat-stress/cohesion/leadership/captivity/indoctrination/courage/values chapters; lighter triage (reasons given) on the four synthesis chapters, Reserve-Component logistics, and Women-in-the-Military/Sexual-Orientation chapters (out of scope per `project_sexuality_rules` canon) |
| `10_Synthesis_Character_Application.md` | Cross-book synthesis — candidate backstory/injury/voice/questline material for the Cancer defector, plus a separate cross-series flag list | — | `[x]` **Done.** Identifies convergent threads across multiple independent source books (strongest: the defining wartime action, gradual erosion via a broken leadership promise, the polytrauma triad, isolation-from-tribe, and the romance-arc mechanics) rather than re-listing individual findings |

**All extraction and synthesis work in this folder is now complete.** Only remaining gaps: `07`'s missing
~30% (see its own row) and the never-started 1st-edition spot-check for that same book — both low-priority
follow-ups, not blockers — plus the separately-tracked dark-humor sourcing task (see "Developer insights"
below), which is deliberately out of scope for this pass.

---

## Duplicate/near-duplicate note

Two files under the same title turned out to be genuinely different editions (2011 vs. 2019, confirmed by
copyright-page comparison), not an accidental duplicate download — both are worth partial use; see `07`'s row
above.

## Developer insights, flagged for future research — not yet acted on

- **Dark humor, flagged 2026-08-29.** Developer's own observation, confirmed direction but explicitly **not**
  for this pass: the Cancer defector would plausibly have an **extremely dark sense of humor** — real, welldocumented
  military gallows humor, not invented quips. **Next step, when this thread resumes:** identify real-world
  source material specifically on military/combat gallows humor — memoirs, oral-history collections, stand-up
  or writing by veteran comedians, academic treatment of dark humor as a trauma-coping mechanism (note: none
  of the 10 books currently in `to-be-integrated/books/PTSD/` are dedicated to humor specifically — this needs
  a separate source search, not just a deeper read of what's already in hand) — and the developer noted this
  may also mean **seeking out people with former-military backgrounds directly** for help getting the voice
  right, not just reading about it. Not started. Do not synthesize this into his voice/dialogue until real
  source material (or direct input) is actually in hand — a guessed-at "dark humor" voice risks landing as
  generic edgy quipping rather than the real thing.

## Maintenance rule

Same as `Ice-Cold_Buddhism_Research/00_Extraction_Checklist.md` and `Reference/Real-World/
Book_Extraction_Index.md`: when a file in this folder is completed or changed, update its row here in the same
pass.
