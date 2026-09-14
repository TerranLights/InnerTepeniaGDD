# Fragmentation Matrix — Expansion Ideas

**Status: brainstorm-stage. Nothing in this file is locked design** — it's a holding pen for possible further
development of `Fragmentation_Matrix.md`'s Bond/Grief system, generated 2026-09-14 at the developer's request.
Treat each idea as a candidate to formally fold into the main file (with numeric thresholds, per-cell dialogue,
etc.) when its turn comes, not as shipped canon yet.

**One item below is under active priority** — see Idea 2.

---

## ⭐⭐⭐ IDEA 2 — RETROACTIVE DISCOVERY: A COMPANION CAN LEARN WHO YOU USED TO BE EVEN IF THEY NEVER MET THEM

**IMMEDIATE PRIORITY, set by the developer 2026-09-14.**

### The correction this makes to existing doctrine

`Fragmentation_Matrix.md` currently states, as a clean structural property of the two-axis model:

> *"a companion recruited after the player's last re-spec never knew the earlier self, so their Grief axis is
> structurally locked at 0 — they can only ever occupy the top row of the grid. Nothing needs to be written to
> enforce this; it falls straight out of the axis definition."*

This was itself downstream of an earlier developer ruling, from a prior design session: **"it's not possible
for a companion to grieve the loss of a person (i.e., the player-character) that they never knew to begin
with."**

**The developer has now reversed that ruling, 2026-09-14, in their own words:**

> *"In previous conversations and design sessions, I'd said that 'it's not possible for a companion to grieve
> the loss of a person (i.e., the player-character) that they never knew to begin with.' In more recent times,
> I've come to realize that this is actually not necessarily true. In Fallout: New Vegas, one of the most
> iconic characters in the entire in-game universe is a gentleman by the name of Randall Clarke; a man who (at
> the time of the game, when the player is in the world) is a skeleton, as he died two centuries prior, and
> yet, he's one of the most memorable characters in all of fiction. If the player recruits a companion after
> he/she has already been re-speccing, not only would the companion notice that something was a bit 'glitchy'
> about the player-character, but also, there should be things, people, avenues, 'footprints', etc, in the
> in-game world that a companion could theoretically find out about and come to learn of who the player-
> character previously was prior to the companion meeting him/her. That should definitely be in the game."*

**Why Randall Clarke is the right reference point, not just a good anecdote:** nobody in *Fallout: New Vegas*
ever "witnesses" Randall Clarke — the player pieces him together entirely from terminal entries, his skeleton's
placement, a journal, and the geography of Vault 22/the caves around it. He's not delivered to the player as
exposition; he's *found*, and the finding is the characterization. That's the design bar for this mechanic:
**a post-re-spec companion's discovery of a past player-configuration should feel investigative and earned,
not like a stat unlocking a dialogue flag.**

### What this changes mechanically

`Fragmentation_Matrix.md`'s "clean structural property" was too clean — it assumed Grief could only be seeded
by *direct relationship-depth markers* (History Points, questline stage, approval — things that require having
actually known the player during that configuration). That's still true for **firsthand Grief**. What's new is
a second, parallel seeding path:

**Secondhand Grief** — a companion who never personally knew a past configuration can still accumulate a
(likely smaller, capped) Grief value by *discovering* that it existed, through evidence left in the world
rather than lived relationship.

This does **not** erase the top-row structural tendency entirely — a companion who discovers nothing stays at
Grief 0, same as before. It just stops treating Grief-0 as an unbreakable floor for late-recruited companions.
The floor becomes a *default*, not a *law*.

### Candidate sources of "footprints" — where discovery could come from

- **Physical/environmental evidence.** Belongings, correspondence, photos or holo-recordings, a room or
  personal effects tied to a specific past configuration, discoverable the way an item or terminal is
  discoverable in any exploration-driven RPG. The most Clarke-like of the options — found, not told.
- **NPC testimony.** A character who *did* know an earlier version of the player-character — not necessarily a
  companion, could be a shopkeeper, a faction contact, a stranger — mentions them unprompted or when asked, to
  a companion who never met that version.
- **District/institutional record.** If a district's Fame/Infamy history is already tracked
  (`Reputation_System.md`), an in-fiction record of that history (a public notice board, a faction dossier, a
  rumor mill) is a natural, already-existing data source to surface as discoverable text rather than a new
  system.
- **Leyline chatter.** Ties directly into the *other* expansion idea below (Idea 5) — secondhand social-network
  echoes of a past configuration a companion never witnessed firsthand. These two ideas should probably be
  designed together rather than separately.
- **Other-companion banter.** A companion who *did* know the earlier self mentions it to one who didn't, in an
  overheard party conversation — reuses whatever banter-trigger plumbing already exists for companion-pair
  interjections (see Idea 6 below; same mechanism, different function).

### Proposed shape of the mechanic (not yet numerically designed)

1. **A "Discovery Depth" marker**, parallel to but structurally distinct from the existing Relationship-Depth
   Markers — measures *how much* a companion has uncovered (one rumor vs. a fully-pieced-together picture),
   not how close a relationship was. Feeds the same seeding formula shape
   (`Discovery Depth × Personality Grief-Multiplier`) but through a different input variable.
2. **A visible cap below firsthand Grief**, at least as a default assumption — a companion who *found out*
   about a lost version of you is not equivalent to one who *lived through losing them*. Whether that cap is a
   hard ceiling (e.g., discovered Grief maxes at Range 2, firsthand can reach Range 3) or a soft weighting is
   an open numeric question, but the asymmetry itself should hold.
3. **Player agency over disclosure.** The player should plausibly be able to volunteer the truth directly
   (accelerating or completing a companion's discovery), stay silent and let the companion piece it together
   on their own, or — more interestingly — actively obscure/deny it if asked. This gives the mechanic the same
   kind of player-facing choice-weight the rest of the re-spec system already has, rather than being a purely
   passive world-simulation layer.
4. **An investigation thread, not a single flag flip.** Modeled loosely on personal-questline structure
   (`Companion_System.md`'s Personal Questline Design Rule) — a companion who picks up a first footprint should
   have somewhere to take it (asking around, seeking out a second piece of evidence), rather than the discovery
   resolving in one dialogue node. This is what makes it feel like Clarke's Vault 22 rather than a codex entry.
5. **This plausibly unlocks Long Vigil eligibility for late-recruited companions**, which the current
   structural-lock rule explicitly forecloses ("they can only ever occupy the top row of the grid"). Whether
   that's desirable is worth a direct developer call once the mechanic is fleshed out further — a
   secondhand-discovery route to The Long Vigil would be a meaningfully different flavor of that state than a
   companion who lived through the loss themselves, and might deserve its own distinct named cell or a footnote
   on the existing one rather than being treated identically.

### Structural note

`Fragmentation_Matrix.md`'s own "structurally locked at 0" paragraph has been flagged as superseded (not
rewritten) pending this mechanic's formal design — see that file for the pointer back here. The full grid,
seeding formula, and Long Vigil sections in that file are otherwise unaffected; this only touches the one
structural claim about late-recruited companions.

---

## IDEA 1 — A Grief Ledger, Not a Single Grief Value

Currently Grief is seeded once, "over a specific earlier configuration this entity actually knew," and doesn't
shrink as Bond grows. But nothing in the current design addresses what happens across **multiple** re-specs.
Does a companion present for three separate re-specs carry grief for only the most recent lost self, or could
they be holding unresolved feeling about two or three past versions simultaneously?

**Proposal:** a Grief Ledger — one Grief entry per past configuration a companion actually knew, rather than a
single overwritable value. The **visible grid state** could still just reflect the highest (or most recent)
entry, so the existing 16-cell grid doesn't need to grow — but the underlying ledger would let:

- A heavily-re-specced late-game playthrough read as meaningfully heavier than a single-re-spec one, even at
  the same visible Grief tier.
- Calethina's arc (already flagged as having "the highest multiplier in the game" and a unique Direct
  Participation Count marker) have somewhere further to climb than a single terminal value — she could be the
  one character whose ledger is genuinely worth surfacing to the player directly, since she's present for
  every entry in it by construction.
- A future "Reconciled"-style resolution mechanic (see Open Design Questions in the main file) resolve *one*
  ledger entry without erasing others — grieving a peace with self #2 doesn't require having made peace with
  self #1 too.

---

## IDEA 3 — A "Grief Confrontation" Beat at First Crossing Into Range 2/3

A one-time scripted beat, similar in shape to a personal-questline trigger, that fires the first time a
companion's Grief crosses into Range 2 or Range 3. Gives the player a binary choice: **sit with it** (acknowledge
what the companion is carrying) or **deflect** (change the subject, avoid the conversation).

This is a natural hook for the main file's own open question — *"whether Grief can ever be narratively resolved
down a tier... or whether it is genuinely permanent once seeded."* Under this proposal, confronting the beat
honestly could be the *only* legal path to a "Reconciled"-style downgrade; deflecting locks the Grief tier
permanently. That turns the IF-meter-style permanence rule into a real player choice with a real cost, rather
than a flat mechanical wall the player has no say over.

---

## IDEA 4 — Derive the Personality Grief-Multiplier Formulaically From Enneagram Type + Wing + Instinct

The four companions already calibrated in the main file (Ayako, Seica, Kendra, Calethina) all read as
Enneagram-driven in how their multiplier was derived — SP4w5's grief-into-action pattern, 8w7's present-focus,
etc. Rather than hand-calibrating every remaining companion and all 11 uncalibrated districts one at a time, a
base lookup table from **type + wing + instinct → default multiplier** would close that gap systematically,
the same way the single-stat rule already systematized the 26-skill list
(`feedback_skills_single_stat_rule`).

Hand-written overrides (like Seica's community-philosophy discount, which runs counter to her type's likely
default) would sit on top of the table for the cases where a character's specific worldview overrides the
general type pattern — the table gives a sensible starting point, not a replacement for judgment.

---

## IDEA 5 — Leyline Chatter as an Indirect Bond/Grief Nudge for Districts

Leyline (the national social-media network, mechanism still TBD per `project_leyline`) is an existing lore
concept that hasn't yet been given a gameplay hook. A district the player hasn't interacted with directly could
get a small, fractional relationship-depth-marker bump from *hearing about* a re-spec secondhand through Leyline
chatter, distinct from (and smaller than) the depth marker a district earns through direct Fame/Infamy history.

Cheap texture for the districts that would otherwise sit at a near-zero depth marker for the whole game, and —
as noted under Idea 2 above — this dovetails directly with the secondhand-discovery mechanic; the two should
probably share a design pass rather than being built as two unrelated systems that happen to overlap.

---

## IDEA 6 — Companion-Perception Ripple Through Existing Banter Systems

If two companions are present together and one is deep in Grief for a discarded configuration, that's a natural
trigger for a banter line from the other — *"have you talked to [X] about this?"* — reusing whatever
companion-pair banter/interjection plumbing already exists rather than building new systems.

Note this is mechanically the same delivery vehicle Idea 2 proposes for one of its discovery sources
("other-companion banter") — worth designing once, used for both functions (an already-informed companion
either commenting on a peer's Grief state, or *becoming* the source that informs a late-recruited peer in the
first place).

---

## Suggested build order, if/when this moves from brainstorm to formal design

1. **Idea 2 (Retroactive Discovery)** — priority, per the developer's direct instruction 2026-09-14.
2. **Idea 5 (Leyline)**, in tandem with Idea 2 — they share a design surface.
3. **Idea 6 (banter ripple)** — cheap, reuses existing systems, and is a dependency-lite companion to Idea 2's
   "other-companion banter" discovery source.
4. **Idea 1 (Grief Ledger)** — worth doing before numeric thresholds are locked, since it changes what the
   underlying data model needs to store.
5. **Idea 4 (Enneagram-formula multiplier)** — best done once more companions exist to test the lookup table
   against, so it isn't calibrated against only the four existing examples.
6. **Idea 3 (Grief Confrontation beat)** — depends on the main file's still-open "can Grief resolve down a
   tier" question being answered; natural to design alongside that ruling rather than before it.
