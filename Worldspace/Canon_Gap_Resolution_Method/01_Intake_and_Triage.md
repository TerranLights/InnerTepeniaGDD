# Intake and Triage

> **⚠ Read `00_RUNBOOK.md` first. LAW A — an open gap is not a defect — governs this entire file.** Triage is
> where LAW A is actually enforced, and it is the step this system will be most tempted to rush, because every
> gap it correctly declines to touch looks, superficially, like work not done.

---

# 1. What counts as a gap

**A gap is a specific, answerable question about canon that someone actually needs answered.** All three
qualifiers are load-bearing:

- **Specific** — *"Cape Adare's land area is not stated anywhere"* is a gap. *"Cape Adare needs more depth"*
  is a wish, and belongs to a synthesis pass, not here.
- **Answerable** — there must be a plausible path (`02`) by which an answer could exist. A question whose only
  possible answer is invention is not a gap; it is a synthesis job or a developer decision.
- **Needed** — by a named consumer, a named pass, or the developer. **A question nobody is waiting on is not
  a gap; it is trivia.** This is the qualifier that keeps the registry demand-driven (§2).

---

# 2. ⚠ The scale problem, measured — and why the registry is demand-driven

**Measured 2026-08-31, repo-wide, excluding `graphify-out/` and `Reference/Materials/`:**

```
TBD occurrences:     2,872
Files containing TBD:  495
```

**An exhaustive registry of this project's open questions is not achievable and should not be attempted.** A
2,872-row index would take a project of its own to build, would go stale the day it was finished, and — worse
— would be *untrustworthy in the one way that matters*: nobody could tell whether a gap's absence from it meant
"resolved" or "never captured."

**Therefore: the registry holds only gaps admitted into the work queue** — either formally emitted by a
consumer pass, or surfaced by a deliberately scoped discovery sweep someone chose to run. **Discovery is a
procedure you run on a scope (§3), not a standing global index.** Everything else stays where it already lives,
in the file that already flags it, which is a perfectly adequate home for a question nobody is working on yet.

---

# 3. Scoped discovery — how to actually find gaps within a scope

**Scope first** (`00` Step 1): one location, one subsystem, one consumer pass. Then, in rough order of yield:

**3.1 — Harvest the consumer's own REQUESTED block, if one exists.** The highest-quality source by a wide
margin: already specific, already needed, already stating what it blocks and what the pass did instead.
*(ULM's `05` §5 defines this format; Runs 6 and 7 both produced one.)*

**3.2 — Read the location's/subsystem's own "Open Questions" section**, where the convention exists. Most
`Specs/` files carry one and it is the project's own curated list of what it knows it doesn't know.

**3.3 — Grep the scope for flag phrasings, then READ every hit.** Grep prioritizes; it never verifies — the
standing project rule. Patterns worth sweeping:

```
TBD · to be determined · not yet established · not yet decided · unresolved
open question · needs a decision · flagged · deferred · not yet started
unknown · unspecified · undetermined
```

**3.4 — Check whether the scope has an entry in an existing proto-registry.** Two already exist and should be
consulted rather than duplicated:
- **`Reference/Real-World/City_and_District_Research_Topics.md`** — a per-location real-world research
  wish-list covering all 13 districts and 36 cities/stations, plus a folder-to-location map of which PDF
  collections are earmarked for which location. **This is the research path's own pre-existing backlog.**
- **`Reference/Real-World/Book_Extraction_Index.md`** — what has already been mined, so a deep-extraction path
  does not re-mine a book. *(This index exists because a book was twice assessed as unmined when it was not.)*

**3.5 — Do not widen the scope mid-run.** If the sweep surfaces gaps outside the declared scope, **record them
and stop there.** Fixing an incidentally-found *error* is correct (`04` Gate 6); *acquiring* an
incidentally-found *gap* is scope creep, and the difference is that an error is already wrong while a gap is
merely open.

## 3.6 ⚠ Person-scope discovery — different sources, different expected outcome

**A character scope reads a different file architecture than a location scope, and skews toward different
triage buckets.** Discovery sources, in order of yield:

1. **The character's own folder** — `Worldspace/Characters/Dolls/…/[Character]/README.md` plus its
   `Personal_Background/` file set (`Timeline.md`, `Relationships.md`, `Loyalties.md`, and siblings).
2. **The two fill-in sheets**, which function as the character equivalent of an "Open Questions" section by
   showing which fields were never filled: `Character_Spec_Fill-In_Sheet_Template.md` and
   `Companion_and_Romance_Questline_Fill-In_Sheet_Template.md`.
3. **The five-stage character methodology's own outputs** — `Worldspace/Characters/Dolls/Methodology/`
   (`00_Overall_Process_Scaffold.md`, `01`–`05`). A character stalled between stages has a gap shaped exactly
   like the input the next stage needs, which is the most precisely-specified kind of gap available.
4. **Sideways, into other characters' files.** A relationship is written from both ends, and frequently only
   one end wrote it. **This is the single highest-yield cross-reference source for person-scope** and has no
   location-scope equivalent.
5. **The character's home location's own canon** — where they are from constrains what they could plausibly
   have experienced, and that location's Specs may already answer a question the character's file leaves open.
6. **`Worldspace/Enneagram/README.md`** and the typing material, where a character's psychological gaps are
   the kind the project's own framework is built to fill.

**⚠ Expect the triage split to look different, and do not read it as a weak run.** Person-scope skews to:

- **RESERVED, heavily** — the project's **`TBN [descriptor]`** folder-naming convention is itself a
  pre-existing, machine-findable reserved-decision marker (`TBN [IT-021 white shirt Fenny]`,
  `TBN [FR-03 billiards Maria]`, and siblings). **Every one of those is a RESERVED gap the developer alone can
  close**, and this system's job for them is groundwork, never a name.
- **SCAFFOLD, heavily** — the per-character template file set means an unfilled `Timeline.md` or
  `Relationships.md` in a stub folder is an unfilled form, not an open question. *(The 2026-08-31 scan found
  31 `TBD` occurrences in `Dolls/z-template/` alone — pure scaffold, zero gaps.)*

**A person-scoped run that closes two gaps and routes six names to the developer has performed correctly.**

---

# 4. The four-way triage

**Every candidate gap is sorted into exactly one bucket before any acquisition work begins.** Sorting before
judging is the discipline the project's own General Investigation skeleton already names as item 2, and it
transfers here directly.

## 4.1 SCHEDULED — deferred to a named later stage. **Protect; do not close.**

**Recognition markers:** an explicit downstream owner in the text itself — *"TBD for DLC 3 design,"* *"deferred
until Phase 7,"* *"once all 13 districts clear all 8 phases,"* *"gated on [X]."*

**The empirical case for taking this bucket seriously:** a sample of `Specs/Rothera.md`'s own TBDs found
**nearly every one of them** carrying "TBD for DLC 3 design." These are not neglected questions. They are
correctly-sequenced ones, and the later stage will answer them with information this stage does not have.

**Action:** record in the registry as SCHEDULED with its named owner-stage. **Do not research it. Do not
prepare an answer "in case."** A prepared answer sitting in the registry exerts real pressure on the later
stage to adopt it, which is the foreclosure LAW A forbids, only slower.

**The one legitimate exception:** if the scheduled stage is *itself* about to run and its owner wants the input
prepared, that is no longer a scheduled deferral — it is a LIVE gap with a named consumer, and re-triages.

## 4.2 SCAFFOLD — an unfilled template slot. **Not a question at all.**

**Recognition markers:** the TBD sits in a template, stub, or boilerplate file; identical TBD counts recur
across sibling files (a strong mechanical tell); the text is a form-field rather than a sentence —
`TBD-NPC`, `**Demonym:** TBD`, `[Character Name] — X`.

**Empirical tell, worth using:** in the 2026-08-31 scan, ten sibling `Storyline/Minmax-Builds/` folders each
returned **exactly 27** TBD occurrences. Identical counts across siblings mean one template, copied — not
twenty-seven independent unanswered questions each.

**Action:** record the *file* as scaffold-bearing once, not each slot as a gap. **Filling a template is the job
of whatever pass owns that template**, not of this system.

## 4.3 RESERVED — requires developer authority. **Route, never settle.**

**Recognition markers:** a person's proper name; an official in-fiction name for a place; a specific date for
an observance; a scope or canon ruling binding beyond one location; anything the developer has explicitly
deferred. **One marker is already mechanical and should be swept for directly:** the project's own
**`TBN [descriptor]`** folder-naming convention for characters awaiting a name (§3.6) — every `TBN [...]`
folder is a RESERVED gap by definition.

**Action:** move to `Developer_Ruling_Queue.md` **with the groundwork already done** — see `02` Path 6. The
value this system adds to a reserved decision is not the decision; it is **arriving at the decision with the
constraints, the precedents, and the consequences already laid out**, so the ruling takes a minute instead of
an evening.

## 4.4 LIVE — genuinely open, genuinely wanted, answerable by some path. **Proceed.**

**Only LIVE items reach `02`.**

**Before accepting an item as LIVE, ask the LAW A question explicitly:** *is this gap's openness load-bearing
for anything?* A deliberately unresolved mystery, an intentionally ambiguous character detail, a tension the
project wants kept live — **these look exactly like LIVE gaps and must be checked for, not assumed absent.**
Where the answer is unclear, the item is RESERVED, not LIVE.

---

# 5. The triage record

**Every triaged item gets a registry row, regardless of bucket** — including the ones this system declines to
touch. **A SCHEDULED item recorded as SCHEDULED is a real output**: it tells the next session that this
question has been seen, understood, and correctly left alone, which is precisely the information that stops
the next session from "helpfully" closing it.

**Schema and the live file: `04_Verification_Gates.md` §7 and `Gap_Registry.md`.**
