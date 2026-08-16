# Doll Questline Directory

**What this is:** the single consolidated file containing full Companion Quest and Romance Quest design
content for every doll with a designed romance arc. Created 2026-08-11 to separate broad-scope, general
Companion/Romance *system rules* (which stay in `Game-Mechanics/Core-Mechanics/Companion_System.md`) from
actual, specific per-doll questline *content* (which lives here). The same Romance Quest content is also
mirrored into each doll's own character folder (her `Questlines/README.md` if she has one, otherwise her main
`README.md`) — this file and each doll's own folder are meant to carry identical Romance Design content, not
a summary in one and the full version in the other.

**For general rules** — Party Composition, the No Good Endings law, the Double Gate system, Forbidden Traits,
the Personal Questline Design Rule, the Romance Beat Checks law, The Signal, Gate Display, Romance Exclusivity,
Sexuality by Character Type, the Romance Reward/home-unlock system, DLC companion residence rules, and
everything else governing *how and why* the Companion/Romance system works — see `Companion_System.md`. This
file is the *what*, not the *how*.

---

## Confirmed Romanceable Characters

Roster-level index, copied verbatim from `Companion_System.md` as it stood at the time this Directory was
created (2026-08-11), with one correction: Lillian's row below shows her real thresholds rather than "See
character file," since this Directory — not `Companion_System.md` — is now the place for real per-doll
specifics (see Companion_System.md's own note pointing here).

| Character | Type | Stat Thresholds | Trait Gates | Notes |
|-----------|------|-----------------|-------------|-------|
| Calethina | Projection system (not a companion) | Calc ≥ 8, Humanity ≥ 6, Nerve ≥ 6, Engine ≥ 6 | TBD | See full design note below; romance post-download via mini-quest |
| IT-068 [Flora] | Recruitable companion | Nerve ≥ 7, Calculation ≥ 6, Engine ≥ 5 | See character file | First companion; 6w5 Thinking; see full romance design note below |
| Favi della Torre | Recruitable companion | Nerve ≥ 7, Humanity ≥ 6, Engine ≥ 6 | See character file | 6w5 Self-Pres; loyalty proven through protective choices; see full design note below |
| Villena Hiresvett | Recruitable companion | Agility ≥ 6, Humanity ≥ 6, Nerve ≥ 5 | See character file | 7w6 Self-Pres; presence and genuine engagement; see full design note below |
| Naizelle d'Edjordoś | Recruitable companion | Calculation ≥ 7, Investigation ≥ 6, Engine ≥ 5 | See character file | 5w6 Self-Pres; most patient romance in the game; see full design note below |
| Seica Cenilaithe | Recruitable companion | Nerve ≥ 7, Might ≥ 6, Humanity ≥ 6 (possibly 7 — TBD) | See character file | 8w7 Sexual; see full romance design note below |
| Ji-Eun Kim | Recruitable companion | Calculation ≥ 8, Investigation ≥ 6, Humanity ≥ 6 | See character file | 5w4 Social; in hiding; undelivered letter is a separate gate outside romance arc; see full design note below |
| Vosora Lashár Tanslock | Recruitable companion | Calculation ≥ 7, Investigation ≥ 6, Nerve ≥ 6 | See character file | 5w6 Social; romance happens within the investigation; see full design note below |
| Michelle Stanton | Recruitable companion | Calculation ≥ 7, Humanity ≥ 6, Engine ≥ 7 | See character file | 5w6 Social; built the Arcanet; chose to stay; romance through shared commitment; see full design note below |
| IT-021 [Fenny] | Recruitable companion | Humanity ≥ 7, Engine ≥ 6, Nerve ≥ 5 | TBD | 6w5 Self-Pres; quietest romance in the game; no signal line — she just doesn't warm up; see full design note below |
| FW-25 [Pink Lucy] | Recruitable companion | Humanity ≥ 7, Engine ≥ 6, Nerve ≥ 5 | TBD | 7w6 Social; communal intimacy; romance unfolds through The Warm Circuit; see full design note below |
| Kendra Heinrich | DLC 1 companion | **None** | **None** | Unique gate system — see full design note below |
| Salagéa Aparast | DLC 5 companion | TBD | TBD | Thresholds pending Phase 7 personality design |
| + all future companions | TBD | TBD | TBD | Rule: all recruitable companions are romanceable by default |
| **Majyao Bisyugota** | **Non-recruitable NPC** | Humanity ≥ 7, Investigation ≥ 6, Calculation ≥ 6 | See character file | 4w5 Self-Pres; teahouse keeper; romance through repeated visits and questline depth; Blood River Tea thread — see design note below |
| Ayako Hayashi | Recruitable companion | Investigation ≥ 7, Humanity ≥ 7, Calculation ≥ 6 | See character file | 4w5 Self-Pres; Red Spiral medic; highest Investigation gate in the roster; see full design note below |
| Lyuba Baranova | Recruitable companion | Nerve ≥ 8, Humanity ≥ 7, Engine ≥ 6 | TBD | 8w7 Sexual; silver-tongue / unarmed fighter; Aries; highest Nerve gate in the roster; see full design note below |
| TCY-25 "Rui" | Recruitable companion | TBD | TBD | 9w1 Self-Pres; Scorpio transformation practitioner; confirmed recruitable 2026-07-10; thresholds pending Phase 3 personality design |
| TBN [TCY-42 ravishing extravagant Lillian] | Recruitability undecided; **confirmed romanceable 2026-08-11** | Investigation ≥ 7, Humanity ≥ 6, Nerve ≥ 5 | Demagogue | 7w8 Social-Countertype; Leo, intimate-tradition house; first companion with a Courtship Sequence beat built under the Romance Beat Checks law (below); full design in her own `Questlines/README.md` |
| **Majyao Bisyugota** | **Non-recruitable NPC** | Humanity ≥ 7, Investigation ≥ 6, Calculation ≥ 6 | See character file | 4w5 Self-Pres; teahouse keeper; romance through repeated visits and questline depth; Blood River Tea thread — see design note below |
| **Trisha Miller** | **Non-recruitable NPC** | Nerve ≥ 7, Humanity ≥ 7, Might ≥ 7 | See character file | 8w7 Social; radio host; romance through recurring off-air encounters; see full design note below |

Non-recruitable named NPCs confirmed romanceable: Majyao Bisyugota, Trisha Miller (design notes below). Further NPC romance status decided per character during design.

---

## Calethina

### Companion Quest

Calethina is a structurally special case — not a companion in the mechanical/code sense (no companion slot,
no companion-system triggers; see `Companion_System.md`'s "Calethina: Not a Companion"). She has no dedicated
`Questlines/README.md` content (that file is a blank template in her folder) and no "Personal Questline Hook"
section in her own README.md — her questline content instead lives under her README.md's "Re-Spec &
Questline Mechanics," "The Triage Protocol Connection," and "Endings" sections, reproduced below verbatim as
the closest equivalent to a Companion Quest writeup. Her full README.md is her `Worldspace/Characters/Dolls/
Still-Present_-_In-Game/unsure and_or special cases/Calethina/README.md`.

**Re-Spec & Questline Mechanics**

**"Calethina's arc through repeated re-speccing"** (`Player_Re-Spec_-_Complete_Design.md`): first visit —
professional, thorough, honest about risk. Second visit — she asks why; not to block the choice, she'll
still do it, but the question carries weight. Third+ visit — her register shifts: explicit concern by
Fragmenting, grief by Unstable, something at Critical only fully legible next to the Devotion ending.

**The download decision — approximately the main quest's midpoint**, not the ending. A transition that
changes what the second half of the game looks like with her, not a conclusion. **Not stat-gated** — available
to any player who reaches it through the questline.

**Two embodiment branches, established 2026-07-12, genuinely equal in weight:**
- **"Inside you."** She becomes part of the protagonist, carried within them, projecting from the
  protagonist's own body. Same-magnitude stat trade: **+n** to Calculation/Investigation/Nerve/base
  Hacking%, matched by an equal **−n** to Engine/Might/Humanity. Her risk: the player's frame wasn't built to
  host a second consciousness — real chance she degrades *further* from mismatched architecture, echoing the
  exact cause of her original corruption. The player's risk: she's always there now, no more private inner
  life.
- **New body / embodiment.** Her first physical body in her entire existence. No stat change either
  direction — a deliberately different currency than the branch above. Cost: memory/personality fidelity
  loss in the transfer itself. Non-stat reward currency still TBD (three candidates: access to her own
  home/location for the first time; body-enabled companion interaction content; a "first time being a
  person rather than infrastructure" recognition-cascade effect on district/NPC reactions). None chosen.

**Cross-DLC portability — tied specifically to "inside you," not new-body.** Choosing "inside you" and
completing her questline unlocks bringing her along into any DLC — her signal-range limitation becomes
irrelevant once she's carried internally rather than projecting from a fixed server. Opens two things: her
finally experiencing the country she was built with knowledge of but never got to see firsthand, and possible
fragmentary memory recovery from her wiped datadrives (real-world forensic logic — wiping the file-table
index doesn't necessarily destroy the underlying data, especially given the original wipe was rushed
wartime work, not a deliberate secure erasure). Optional bonus content, never required to finish her story.

**Base-game completability, binding constraint:** her full arc — companion → romance → post-romance — must
be completable entirely within the base game, zero DLC required. The "rescuing Kendra, decrypting the
datastash" beat (DLC1 territory) is an optional bonus escalation stacked on an already-complete base arc,
never a requirement.

**Reward tiers** (from a retired-but-absorbed rewards doc): Tier A (companion completion) — 1 free combat
turn before automated systems turn hostile, +1 Calculation/Investigation/Nerve, +15% base Hacking, with a
DLC1-bonus escalation tied to the Kendra/datastash beat. Tier B (romance completion) — doubles most of the
above. **Open question, not resolved:** whether these apply on top of, or instead of, the branch-specific
mechanics above (the inside-you stat trade, the new-body non-stat perk).

**The Triage Protocol Connection — Confirmed 2026-07-23**

**Renamed:** the in-world Power Core safeguards, previously referred to as "Ghost Protocol," are now **the
Triage Protocol** — the reference file itself (`Worldspace/Energy_Grid_Failure_Rationale.md`) keeps its own
name; only the in-world term changes. The rename resolves a real naming collision: "Ghost Protocol" was
independently in use for Minmax Build #18/Alternate Ending #18 (unrelated, stays as-is) and as a still-open
placeholder name for Ji-Eun Kim's own companion perk (also unrelated, her own rename still separately open).

**Confirmed, not speculative:** **Calethina personally created the Triage Protocol.** She embedded it into
the Power Core during the Long Night War evacuation — a desperate, genuinely life-saving act, deliberately
rationing output and creating rolling failures rather than letting the whole grid collapse at once. **The
same power shock that caused the Planetary Split Brain and corrupted her own datadrives also erased her own
memory of having done it.** This is a third, distinct thing the Split Brain shock took from her, alongside
the general operational degradation and the earlier, separate Fort McMurdo datadrive wipe — she isn't hiding
this out of guilt, and she isn't lying by omission. She genuinely doesn't know. The tragic irony: the person
best positioned to explain and safely resolve the Triage Protocol is the one person who no longer remembers
being its author.

**Discovery mechanism, confirmed:** this truth is uncovered over the course of **her Romance questline**
specifically — not the main Step 1-5 structure's Step 4 decision point. See her `Questlines/Personal_
Questline_Summary.md`'s Step 5 for where this now sits.

**Endings — A Real Reconciliation Gap Worth Flagging**

Multiple ending concepts exist across her files, from different design passes, and **they have not been
explicitly reconciled with each other:**

1. **"The Furthest Signal"** (`Storyline/Endings/Secret-Endings/Calethina_Devotion_Ending.md`) — an earlier
   design: the player traces the locations of her destroyed backup instances, finds one intact-but-dark
   server housing, and works with her to restore it as a new relay point extending her signal's reach. Not
   recreating the lost instance — using intact hardware as a new anchor. Ending: the relay goes live, her
   signal reaches a space it hasn't in years, "she does not say anything dramatic."
2. **The two embodiment branches** (inside-you / new-body, above) — the 2026-07-12 design session's own
   framing for how her story actually resolves.
3. **Pariah Failsafe #9, "The Calethina Accord"** — a *different* ending, available when the player turns to
   her from universal condemnation (all 13 districts hostile) with nowhere else to go. Explicitly contrasted
   with Devotion in the Devotion ending's own file: the Accord is relationship born from necessity, Devotion
   is relationship born from choice.

**What isn't settled:** whether "The Furthest Signal" is a third distinct outcome alongside the two
embodiment branches, an earlier draft superseded by them, or a stage that happens *before* the download
decision (restoring reach, then facing the embodiment choice on top of that). The Devotion ending file
predates the 2026-07-12 session and was never updated against it. Flag this explicitly before finalizing any
Step-by-Step questline structure — don't assume either document silently wins.

The Calethina Devotion ending itself has two versions per `Companion_System.md`: one for players who
completed the romance mini-quest, one for players who reached a full download (either branch) without Gate 2
conduct maintained.

### Romance Quest

**Quick reference (roster row):** Projection system (not a companion) | Calc ≥ 8, Humanity ≥ 6, Nerve ≥ 6,
Engine ≥ 6 | Trait Gates: TBD | See full design note below; romance post-download via mini-quest. *(Note: this
table row reflects the original, since-superseded stat-gate design — see the corrected design below, which
replaced it with a conduct-based gate on 2026-07-23. The table itself is preserved verbatim from
`Companion_System.md` per this Directory's own roster-index purpose; the actual current design is the
conduct-based one.)*

Calethina is romanceable. She is the most demanding romance in the game narratively — though no longer
mechanically via a MACHINE stat threshold. **Corrected 2026-07-23: this section previously described a
stat-gate design (Calculation ≥8, Humanity ≥6, Nerve ≥6, Engine ≥6) that was superseded and dropped entirely
during the 2026-07-12 design session** — see `Questlines/Substrate_Transfer_and_Embodiment_Design.md` for
the full authoritative design this section now reflects.

**Gate design — redesigned to match Kendra Heinrich's own precedent.** The stat-threshold idea was dropped
specifically because the download's own stat penalty (see below) would collide with a numeric romance
threshold in ways hard to make fair on purpose: evaluate the gate pre-penalty and the threshold becomes
pointless; evaluate it post-penalty and it risks punishing exactly the players it's meant to reward. Kendra's
own gate already solves this — entirely conduct-based, no stat or trait requirement at all — so Calethina's
gate mirrors that shape instead:
- **Gate 1 — commitment:** the player completes her personal companion questline through to a **full
  download decision — either branch**, "inside you" or new-body embodiment (see below). A partial download,
  a no-download outcome, or an alternative stabilization path does not meet this gate.
- **Gate 2 — conduct:** across vital plot points in her personal questline, the player doesn't say or do
  anything combative, insulting, or abhorrent to her sensibilities — the equivalent of Kendra's "not kicking
  her while she's down."

Both gates met → romance becomes available. This makes the old stat-interaction tension moot rather than
solved — eligibility is behavioral, not numeric, so the download's stat penalty has nothing left to collide
with.

**The download and the romance are separate events.** The Calethina questline ("Echoes of the Bridge")
builds the relationship across its full length. The download decision (approximately midpoint of the main
quest) is available to any player who has made the associated questline decisions — it is not stat-gated
either. The download is about saving/keeping her. The romance is a separate question about what the
relationship becomes afterward.

**The download: two branches, not one.** On the **"inside you"** branch, she isn't simply transferred to
the protagonist's wrist device — she becomes part of the protagonist, carried within them, projecting from
the protagonist's own body; this branch also carries a same-magnitude stat trade (+n Calculation/
Investigation/Nerve/base Hacking%, matched by −n to Engine/Might/Humanity). On the **new-body/embodiment**
branch — her first physical body in her entire existence — there's no stat change in either direction; the
cost instead is memory/personality fidelity loss in the transfer itself, with the actual non-stat reward
currency still TBD (three candidates floated, none chosen — see the Substrate design doc). Both are a
profound chosen bond regardless of whether the romance follows, and both now count equally toward Gate 1.

**Romance eligibility no longer requires the "inside you" branch specifically** — that branch is required
for a different, separate unlock (cross-DLC companion portability, see the Substrate design doc), not for
romance. Either full-download branch satisfies Gate 1 here.

**The romance option appears once both gates are met.** The protagonist and Calethina now share whatever
physical reality the chosen branch produced — inside them, or beside them in a new body — but the romantic
arc is a separate layer, unlocked by conduct across the questline rather than a build requirement.

**The romance mini-quest.** If the romance option appears, it is its own dedicated interaction sequence
distinct from the main questline — a focused arc that constitutes the actual romantic relationship
developing between the protagonist and Calethina in the post-download state. Specific beats are Phase 5
design work.

**Built-in bittersweet weight.** Whichever branch is chosen, the full download carries a confirmed risk of
memory or fidelity loss in transfer. The romance begins with the protagonist having already accepted losing
some piece of her in order to keep her at all.

**The re-spec complication.** If the player re-specced through Calethina's lab to meet some other threshold
elsewhere in the game, she performed that work herself. She knows what was changed and why. Wherever the
romance option actually lands should have dialogue that acknowledges this — as a branch, not a single read.
Whether she finds it moving (someone wanted to be someone she could love) or troubling (someone altered who
they were) are both valid. Both are bittersweet.

**The Calethina Devotion failsafe ending** has two versions: one for players who completed the romance
mini-quest, one for players who reached a full download (either branch) without Gate 2 conduct having been
maintained. The second version reflects a different kind of profound chosen bond — she is with them, in
whichever form the download took, and that is its own thing.

---

## Vosora Lashár Tanslock

### Companion Quest

*(Full content of her own `Questlines/README.md`, verbatim.)*

# Vosora Lashár Tanslock — Questline Notes

## Recruiting Quest

Vosora works the data recovery side of the Great Corruption investigation — reconstructing what was destroyed rather than verifying what remains. Her work has gotten dangerous: what she's getting close to proving would be genuinely damaging to reveal, and a Libra official — sincerely convinced that revealing it would do more harm than good — has been quietly trying to slow her down. She has not disclosed this pressure to anyone.

### Possible Hooks
- **Cover and Purpose:** You find out about the pressure she is under. You provide cover — and a reason the recovery matters enough to risk. She joins because you represent an exit from the exposed position she has been locked in alone.
- **The Critical Recovery:** She is one step from a specific recovery that would prove the Corruption was a genuine accident — one Libra's own negligence allowed to happen — and reveal exactly what those lost records would have shown. She needs to keep working without being seen doing it. You provide that cover.
- **The Threat Made Visible:** Whoever has been pressuring her steps out of the shadows. Dealing with it together changes the dynamic from hiding to motion.

---

## Companion Quest — "What the Silence Says"

### Core Conflict & Emotional Stakes
The shape of what is missing in the Great Corruption is itself evidence. The size of the gaps, their location in the timeline, what topics they cluster around — all of this says something about who was affected and why. Vosora has been tracing that shape toward an answer.

**The answer, established 2026-07-20 (per `Cross_District_Non_Malice_Audit.md`'s binding lock on Gemini's Great Corruption — it must resolve toward accident, never deliberate sabotage):** the Corruption was a genuine accident. During the founding-crisis storage triage, certain record categories — detailed resource-allocation logs, intake and administrative paperwork, the granular bureaucratic paper trail rather than anything deemed immediately survival-critical — were deprioritized onto older, lower-redundancy infrastructure. That was a defensible crisis-era call at the time: protect what's needed to survive the next week, not the paperwork. That infrastructure later suffered real data loss through ordinary hardware failure. The gaps cluster suspiciously around specific topics not because anyone targeted them, but because those record types all happened to share the same vulnerable storage tier — which is exactly why it looks like sabotage from the outside, and why it's a genuine mystery worth investigating rather than a settled non-event.

**Why it's still dangerous to prove, despite being an accident:** if fully reconstructed, the lost records wouldn't reveal a conspiracy — they'd provide hard, undeniable proof of exactly the kind of founding-era structural inequities this game's wider non-malice audit has been surfacing district by district (Capricorn's guild patronage, Taurus's Insulation Schism, and whatever else eventually gets confirmed). Right now those are half-remembered grievances people can't prove. Verified, they become fact. On top of that: the accident happened because Libra let critical infrastructure rot — proving *that* would mean proving Libra's own negligence, at a scale that would seriously damage public trust in their competence and fitness to govern. Sympathetic Libra officials suppressing this are acting from a real, if debatable, mix of motives: genuine (if paternalistic) fear that proving old wounds would destabilize a fragile peace, **and** self-interested fear of what it would do to Libra's own legitimacy. Neither motive involves malice toward Vosora or Michelle specifically — the pressure is about the information, not about them as people.

### Themes
- What a civilization that controls its own history does when someone starts recovering what it edited
- The gap between "lost" and "hidden" — and what it means when the distinction becomes provable
- The personal cost of having proof that powerful people would prefer not to exist
- What it means when the truth turns out to be negligence and self-interest rather than conspiracy — arguably harder to reckon with, because there's no clean villain to blame

### Possible Endings
- **Publication:** The truth is recovered and published — both that the Corruption was an accident born of Libra's own negligence, and what the lost records would have proven about old structural inequities. A genuine political earthquake: real damage to Libra's legitimacy, real implications for Janbogo's political structure and possibly the Falkland Treaty legacy.
- **Leverage:** The recovered records are held as private leverage over the officials who suppressed the investigation. Quieter, more personal consequences — more certain.
- **The Shape of the Gap:** The records cannot be fully recovered, but she maps the shape of what is missing with enough precision that the shape itself is a document. Published, it tells a story even without the original content.
- **The Wrong Answer:** What she recovers is something she wishes she had not found — not a grand conspiracy, just negligence compounded by an institution choosing self-preservation over transparency. No clean villain, nothing dramatic to fight, just an ordinary failure that happened to erase specific people's histories, and a specific decision to let that stand. Arguably worse than the theory precisely because it's this mundane.

### Cross-Questline Connection
- Michelle Stanton works the slow-verification side of the same investigation. Together they form the two halves of a complete inquiry into the Great Corruption.
- Probable political connections: Libra's Suspended Compact; the Janbogo subnet nexus inside Concordia; the Planetary Split Brain questline.

---

## Retrofit — Personal Questline Design Rule (established 2026-07-20)

**The retrofit target:** the data recovery work itself is explicitly her unique specialty ("the one capability in the game that only she possesses," per her README) and stays entirely hers — this retrofit doesn't touch that. What needs real design is the currently-undesignated antagonist pressuring her — resolved above as a sympathetic, genuinely convinced Libra official rather than a vague hostile organization. This also replaces the "protection during the final step" framing in the Recruiting Quest hooks above with a non-escort structure, consistent with the binding design constraint established for Ji-Eun Kim ("no escort quest structure... cost, difficulty, vulnerability must fall on the player, never on the companion as an NPC you must keep alive").

**Categorical block:** Vosora cannot investigate or confront the source of the pressure herself, for three compounding reasons. First, the recovery work itself is delicate and demands total focus — dividing attention between reconstruction and self-defense risks the recovery itself. Second, confronting the official directly and openly would tip Libra off that their pressure provoked a response, exposing exactly what she's trying to keep hidden: that she's close to a breakthrough. Third, and most importantly given who the pressure is actually coming from: **openly antagonizing a Libra official would destroy Vosora's own institutional credibility** — the very credibility every one of her four possible endings depends on (you cannot publish, leverage, or even document a "shape of the gap" that anyone will believe from someone who's publicly burned their standing with the city's own government). Her own established behavior ("she processes threats internally, plans, and only brings others in when she must or when someone forces the issue") means staying quiet is a considered strategic choice, not fear or oversight. **This is a structural exclusion, not a courage or competence gap** — she is one of the most capable analytical minds in Concordia, but she has no institutional distance from Libra the way the player does. The player is what lets her run the recovery and her own security simultaneously without exposing either.

**5 stat-based approaches (non-build-gated, deterministic):**
1. **Investigation-driven:** trace the pressure campaign back to its source through careful, deniable methods that never lead back to Vosora.
2. **Calculation-driven:** analyze the pattern in the pressure itself — timing, method, what it's specifically targeting — to infer who's behind it.
3. **Nerve-driven:** directly confront a suspected agent or messenger without exposing Vosora's own position in the process.
4. **Humanity-driven:** turn or recruit someone inside Libra who's willing to help quietly.
5. **Engine-driven:** a sustained covert operation, wearing the pressure down over time without ever revealing Vosora's own hand.

**8 non-stat, world-state-based approaches (target 7–12, floor of 3):**
1. **The Long Frequency route:** her own organizational affiliation may have resources or insight, accessible through separate player standing there.
2. **Michelle Stanton route:** the other half of the same Great Corruption inquiry — her own network could help identify the pressure's source through a channel that never traces back through Vosora herself.
3. **A sympathetic Libra official route (corrected 2026-07-20 — distinct from the antagonist, not "Libra's own administrative reach"):** Libra is not monolithic on this — some officials within it genuinely disagree with the suppression, whether because they don't share the same protective conviction or because they're uncomfortable with the self-interested legitimacy-protection angle specifically. A player who finds and earns the trust of one such official gets real institutional insight the antagonist would never volunteer.
4. **Gemini/Janbogo information route:** her own home turf's information networks, used by the player specifically so it doesn't trace back to her directly.
5. **Capricorn route:** her own pre-war career organizing the Amundsen Tower's construction logistics left her real, lasting professional standing among Capricorn's builders and engineers — old colleagues from that project, reachable through separate player standing, could help trace covert pressure through channels that have nothing to do with Gemini's information networks or Libra at all.
6. **Kunlun connection route:** her own flagged, still-undetermined personal connection to Kunlun (per `Specs/Kunlun.md`'s Open Questions) — kept vague since it isn't designed yet, but flagged as a genuine future route once it is.
7. **A legacy item/evidence route:** physical evidence of the pressure campaign turning up through unrelated exploration — no check required.
8. **Wild Child/Janbogo route (fifth flavor — "computational/systemic side-effect," per `Companion_System.md`):** WC-3 ("The Living Myth," `Wild_Child_Endings.md`) already establishes that Janbogo's Truth Markets run competing, irreconcilable data streams about a Wild Child player in the same live feed without resolving them. That system churning under the unusual load of an uncategorizable case could surface adjacent buried data — the same corrupted sector Vosora is after — as a byproduct of the system doing exactly what it's built to do, strained past normal operating conditions.

**No faction-antagonism route** — nothing establishes The Long Frequency as being on bad terms with a specific district; not forced. (Route 3 above is a different pattern — a sympathetic individual within the antagonist institution, not the player's own reputation with a faction the companion is on bad terms with.)

**Untouched by this retrofit:** the dual-outcome perk structure attached to the four endings (see main README's Design Notes) — this retrofit restructures the investigative mechanism and the endings' factual content, not the perk mechanics themselves.

**Cross-questline note — RESOLVED 2026-07-20, independently-convinced-officials structure (corrected from an earlier "hostile organization/compartmentalized cells" draft that didn't survive the non-malice check):** Michelle Stanton's own questline has now been retrofitted with the same treatment (see her `Questlines/README.md`). Their shared pressure comes from **Libra itself — specifically, one or more officials genuinely convinced suppression is the right call, not a hostile organization.** The two investigators are pressured by different officials or departments within Libra, each independently reaching the same protective conclusion rather than coordinating as a conspiracy — which is why **completing Vosora's questline does not complete or shortcut Michelle's, and vice versa.** Their investigative deliverables were already non-overlapping regardless: Vosora reconstructs the destroyed content itself; Michelle verifies the accident's true cause and/or discovers a surviving copy exists somewhere else entirely (the South Pole synchronized Arcanet archive — a possible Hawaii/Hall of Archives connection from an early draft remains too speculative to use, see her own file). A player who completes both questlines can piece together the fuller picture of how widespread this institutional instinct actually is within Libra — an optional bonus payoff, not required by either individual companion quest, not yet designed in detail.

### Romance Quest

**Quick reference (roster row):** Recruitable companion | Calculation ≥ 7, Investigation ≥ 6, Nerve ≥ 6 |
Trait Gates: see character file | 5w6 Social; romance happens within the investigation.

**Stat gate:** Calculation ≥ 7 (primary), Investigation ≥ 6 (secondary), Nerve ≥ 6 (tertiary)

**Rationale:** Vosora is a 5w6 Social type — distinct from the Self-Pres 5 in that she remains engaged with the world through her work rather than retreating from it. She is already doing something that matters (the Great Corruption investigation), and the romantic path runs through that work rather than around it. Calculation is primary because intellectual respect is non-negotiable for any 5, and for a Social 5 it also means understanding why the work matters. Investigation reflects her own orientation — she's drawn to someone who operates in the same register of careful attention. Nerve ≥ 6 serves the 6 wing: the investigation is dangerous and produces disturbing revelations; she needs someone who can hold steady under difficult information without panic or dismissal.

**Forbidden traits:** see Vosora's own character file (`Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/Vosora Lashár Tanslock/README.md`) for her specific forbidden trait and rationale — this file covers the general mechanic only, not per-character assignments.

**Signal line** (if stat threshold not met): *"I don't doubt your intentions. I just need people around this work who can actually keep up with it."*

**Gate 3 — Romance beats** (after companion quest completion):

Vosora's romance happens within her work, not alongside it. The player becomes a partner before they become anything else.

1. **Engage with the investigation, not just with her:** The romantic path requires genuine care about what she's uncovering — asking real questions about the data, noticing something she hadn't, treating the investigation as something that matters in its own right. She can tell the difference between interest in her work and interest in her through her work.

2. **Handle a difficult revelation without flinching:** At some point the investigation produces something disturbing or destabilizing. The 6 wing is watching for steady acknowledgment — neither panic nor dismissal. This is the test she doesn't announce she's administering.

3. **Respect the compartmentalization:** She keeps things organized and separate — not as concealment but as how she functions. The romantic path respects that structure early on and does not try to collapse it before she's ready to.

4. **Intellectual reciprocity:** A Social 5 shares knowledge as connection. The player shares something back — an insight, an angle she hadn't considered, information that actually advances the work. The exchange is what creates intimacy for her, not the gesture.

5. **She starts consulting, not just informing:** The turning point isn't a declaration. It's when she sends the player something outside of operational necessity — when she asks what they think before she's decided. The player knows before she says anything.

6. **The culmination, within the work:** It happens in the context of the investigation, not in a separate emotional scene. While looking at the same data, the same problem. It belongs to the world she actually lives in.

---

## Michelle Stanton

### Companion Quest

*(Full content of her own `Questlines/README.md`, verbatim.)*

# Michelle Stanton — Questline Notes

## Recruiting Quest

Michelle is mid-recovery on a data archaeology project she is too close to a stopping point to abandon. She does slow, careful work in a district that rewards speed — and a Libra official, sincerely convinced revealing what she's close to proving would do more harm than good, does not want the records she is trying to restore made public.

### Possible Hooks
- **Complete the Recovery:** The project reaches a point where it can be handed off or published. She can leave because the work is safe to leave.
- **Confirm the True Cause:** She has suspected the Great Corruption looks like deliberate sabotage but isn't — a genuine accident, born of Libra's own founding-era negligence, that happens to cluster around exactly the kind of records that would prove old structural inequities if recovered. You help her get the evidence that actually settles it. The confirmation changes what the project means — and makes it dangerous enough that she needs help carrying it forward.
- **Protection:** A Libra official aware she is getting close has been quietly applying pressure she has not disclosed. You find out about it and provide cover. She joins because you represent an exit from the exposed position she has been locked in alone.

---

## Companion Quest — "What the Corruption Took"

### Core Conflict & Emotional Stakes
Was the Great Corruption of Janbogo's pre-Falkland Treaty archives an accident, or something else? **Resolved 2026-07-20, per the binding non-malice lock on Gemini's Great Corruption (`Cross_District_Non_Malice_Audit.md`) — it was a genuine accident.** Founding-crisis storage triage deprioritized certain record categories (resource-allocation logs, intake and administrative paperwork) onto older, lower-redundancy infrastructure, which later failed through ordinary hardware attrition. The gaps cluster suspiciously around specific topics not because anyone targeted them, but because those record types shared the same vulnerable storage tier — which is exactly why it looks like sabotage from the outside.

It's still dangerous to prove. The shape of what is missing is itself evidence — what was erased, and where the gaps are, says something real about who was affected. If reconstructed, those records would provide hard proof of founding-era structural inequities the wider game's non-malice audit is surfacing district by district. And proving the accident happened at all means proving Libra let critical infrastructure rot — real damage to public trust in their competence and fitness to govern, on top of whatever the records themselves reveal. Michelle has been tracing that shape toward an answer a sympathetic-but-convinced Libra official would very much prefer stayed buried — not out of malice toward her, but out of a genuine (if self-interested) belief that surfacing it now would do more harm than good.

### Themes
- What a civilization that controls its own history does when someone starts recovering what it edited
- The difference between what is lost and what was hidden
- The personal cost of finding something everyone powerful would prefer stay lost
- What it means when the truth turns out to be negligence and institutional self-interest rather than conspiracy — harder to reckon with because there's no clean villain

### Possible Endings
- **Publication:** The truth — accident, Libra's own negligence, and the structural inequities the lost records would have proven — goes public. A political earthquake with real consequences across Libra, Janbogo's political structure, and possibly the Falkland Treaty legacy.
- **Leverage:** The recovered records are held as private leverage over the officials who suppressed the investigation. Quieter, more controlled consequences.
- **The Shape of the Gap:** The records cannot be fully recovered, but she maps what is missing with enough precision that the shape itself is a document. Published, it tells a story even without the original content.
- **Discovery / Twist:** The records exist somewhere else entirely — a secondary location nobody knew about. Confirmed connection: the South Pole synchronized Arcanet archive, tying naturally into her established DLC 1/Kendra Rastra connection. **(Corrected 2026-07-20: an earlier draft also named a possible Doris Morikawa/Hall of Archives-Hawaii connection — dropped as a confirmed element, since Doris's own file lists "did any archive contents survive and reach Tepenia?" as a genuinely unresolved question; remains available as future flavor only once that's resolved elsewhere.)**

### Cross-Questline Connection
- Vosora Lashár Tanslock works the data recovery side of the same investigation. Together they form the two halves of a complete inquiry into the Great Corruption.
- Probable political connections: Libra's Suspended Compact; the Janbogo subnet nexus inside Concordia; the Planetary Split Brain questline.

---

## Retrofit — Personal Questline Design Rule (established 2026-07-20)

**Replaces the "Protection" recruiting hook above** (which read too close to an escort-quest structure — "you find out about it and provide cover") with the same non-escort structure established for Ji-Eun Kim and Vosora Lashár Tanslock: the cost and difficulty fall on the player, never on Michelle as an NPC to be kept safe.

**Cross-questline structure — independently-convinced Libra officials, not a hostile organization:** Michelle and Vosora's shared pressure comes from **Libra itself — specifically, one or more officials genuinely convinced suppression is the right call**, not a conspiracy or hostile organization (an earlier "compartmentalized cells" draft assumed a hostile actor and didn't survive the non-malice check — see Vosora's `Questlines/README.md` for the full correction). The two investigators are pressured by different officials or departments within Libra, each independently reaching the same protective-plus-self-interested conclusion rather than coordinating with each other. **Completing Michelle's questline does not complete or shortcut Vosora's, and vice versa** — different officials, different pressure campaigns, and their investigative deliverables were already non-overlapping regardless: Vosora reconstructs the destroyed content itself; Michelle verifies the accident's true cause and/or discovers a surviving copy exists somewhere else entirely (the South Pole archive). A player who completes both questlines can piece together how widespread this institutional instinct actually is within Libra — an optional bonus payoff, not required by either individual companion quest, not yet designed in detail.

**Categorical block:** Michelle's is deliberately distinct in kind from Vosora's — philosophical and methodological, not just tactical. Her entire identity, personal and professional, is built on slow verification over speed, explicitly established as counter-culture to Janbogo's own "speed as moral value" ethos. If she rushed to confront a threat on unconfirmed suspicion, she would be doing the exact thing her whole investigation exists to argue against — abandoning careful verification for a fast, unverified action. Her verification method also requires maintaining an unbroken chain of custody at physical archive sites; stepping away mid-verification doesn't just cost time, it resets work that can't be picked back up where it left off. On top of that, openly confronting a Libra official would cost her the institutional credibility her own endings depend on — the same reason Vosora can't do it either. **This is a structural exclusion, not fear or reluctance** — acting fast against the pressure would be a betrayal of who she is and of the very thing she's trying to prove, not merely risky.

**5 stat-based approaches (non-build-gated, deterministic):**
1. **Investigation-driven:** trace the pressure's source through careful, methodical means — consistent with her own verification ethos, done by the player while she stays at her post.
2. **Calculation-driven:** analyze patterns and timing in the pressure to infer its origin.
3. **Nerve-driven:** direct confrontation with a suspected agent, unafraid of the risk.
4. **Humanity-driven:** turn or recruit a source within Libra willing to help quietly.
5. **Engine-driven:** a sustained operation over time, wearing the pressure down without breaking her own verification chain.

**9 non-stat, world-state-based approaches (target 7–12, floor of 3):**
1. **Vosora Lashár Tanslock route:** the other half of the inquiry, pressured by a different Libra official but able to share tradecraft, corroboration, or moral support without either questline shortcutting the other.
2. **The Long Frequency route:** their shared organizational affiliation, accessible through separate player standing.
3. **A sympathetic Libra official route (distinct from the antagonist):** Libra is not monolithic here — an official who disagrees with the suppression, whether on principle or discomfort with the self-interested angle specifically, can offer real institutional insight the antagonist would never volunteer.
4. **Gemini/Janbogo general information route:** consistent with the pattern used throughout this pass.
5. **Aries route:** her own construction and infrastructure background gives her a natural affinity with Aries' hands-on, "people who do actual work" culture (the same value system already established for Flora) — a contact there could offer practical help unavailable through purely informational channels, grounded in her actual profession.
6. **A legacy item/evidence route:** physical evidence of the pressure campaign surfacing through unrelated exploration — no check required.
7. **South Pole synchronized Arcanet archive route:** already named in her own file, tying naturally into her established DLC 1/Kendra Rastra connection.
8. **Virgo/Undergrid route:** her own established post-war activity ("help maintain the city's infrastructure") gives her, and by extension the player through separate standing, real connections in Virgo's maintenance crews — plausible sources for buried evidence or archive fragments physically encountered in old infrastructure.
9. **Wild Child/Long Frequency route (ideological-conviction flavor, per `Companion_System.md`, distinct from Vosora's systemic-overload flavor despite both being Janbogo-adjacent):** The Long Frequency's whole identity is that slow, careful verification beats speed. A Wild Child player — someone the fast, gossip-driven mainstream literally cannot process — is the hardest test case their worldview could ask for. Members would have genuine ideological motivation to obsessively study the player's case specifically to prove their method works where the mainstream fails, and could stumble onto adjacent buried data as a byproduct of conviction-driven effort, not computational strain.

**No faction-antagonism route** — nothing establishes a specific district as being on documented bad terms with Michelle or The Long Frequency; general Janbogo cultural friction over speed-vs-verification isn't the same as a confirmed antagonism, so not forced. (Route 3 above is the sympathetic-individual-within-the-antagonist-institution pattern, not the player's-own-reputation-with-an-opposed-faction pattern.)

**Left untouched / explicitly out of scope for this retrofit:** her MACHINE stats, personality/voice, and companion traits remain placeholder — a separate, larger Phase 3 development task already tracked in her own file's TODOs.

### Romance Quest

**Quick reference (roster row):** Recruitable companion | Calculation ≥ 7, Humanity ≥ 6, Engine ≥ 7 |
Trait Gates: see character file | 5w6 Social; built the Arcanet; chose to stay; romance through shared
commitment.

**Stat gate:** Calculation ≥ 7 (primary), Humanity ≥ 6 (secondary), Engine ≥ 7 (tertiary)

**Rationale:** Michelle is a 5w6 Social type, same as Vosora, but her emotional core is distinct. Where Vosora's intimacy is through shared intellectual pursuit, Michelle's is through shared commitment to a place. She built the Arcanet — the Antarctican internet — and she chose to stay in Concordia when she has the means to leave. Calculation is primary because she needs genuine intellectual depth. Humanity is secondary because she built something that connects everyone; she cares about people collectively and needs to feel the player does too. Engine at 7 — the highest tertiary in the roster — reflects that she has sustained an enormous ongoing commitment for a very long time; she is drawn only to someone who can match that kind of staying power.

**Forbidden traits:** see Michelle's own character file (`Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/Michelle Stanton/README.md`) for her specific forbidden trait and rationale — this file covers the general mechanic only, not per-character assignments.

**Signal line** (if stat threshold not met): *"You seem like someone passing through. I don't have much use for those."*

**Gate 3 — Romance beats** (after companion quest completion):

Michelle's romance is about the player coming to understand why she stays, and demonstrating that they understand it in the only way that counts — by making the same kind of choice themselves.

1. **Engage with the Arcanet as more than infrastructure:** The romantic path requires understanding that what she built isn't just a communications network — it's what she chose to give. Questions about why she built it the way she did, what she was trying to make possible. She notices the difference between someone who appreciates the achievement and someone who understands the intention behind it.

2. **Ask the real question:** At some point the player genuinely asks why she stays when she could leave. The romantic path is a player who listens to the answer and takes it seriously — not using it, not performing interest, not skipping past it. The answer is the most honest thing she offers.

3. **The Rastra moment:** She teaches the player to maintain the vehicle that makes leaving possible. This is an act of trust — she is giving the player access to her capacity to go. The romantic path treats this with the weight it deserves, not as a tutorial.

4. **Choose the city when it would be easier not to:** During her quest, a choice arises where the player could deprioritize Concordia's needs for something personally advantageous. The romantic path doesn't. She stayed because she believes in this place; the player has to demonstrate they understand what that means in practice.

5. **The view from outside:** The most intimate thing she can offer is showing the player what Concordia looks like from a position where leaving is genuinely possible — literally, from the Rastra outside the city, or metaphorically, from her perspective as someone who could go anywhere and chose here. The romance closes with that shared vantage point.

---

## Favi della Torre

### Companion Quest

*(Full content of her own `Questlines/README.md`, verbatim.)*

# Favi della Torre — Questline Notes

## Recruiting Quest

Favi will not leave Taurus while someone or something specific still needs her. She has built her community security network over years and does not walk away from an obligation in progress. The challenge is not persuading her — it is giving her something she can hand off.

### Possible Hooks
- **The Specific Threat:** A threat to her Taurus community (Capricorn resource reallocation squeezing the district; a Cancer refugee influx destabilizing her neighborhood) needs resolving. Help her neutralize the threat precisely — not in general, not eventually.
- **The Information Problem:** She is holding something she believes will deteriorate without her watching it — a community situation, a person at risk. Prove you can track it better from outside than she can from inside.
- **The Successor:** There is someone in her network who can step in. Help her identify that person, build them up to the role, and get her to trust them enough to hand off the watch.

---

## Companion Quest — "The Long Watch"

### Core Conflict & Emotional Stakes
What does a 6w5:Pr do when the danger she has been preparing for finally arrives — and her preparation either works or definitively does not?

The arc centers on the gap between vigilance and fear. She built the security network because she knows exactly what the absence of one costs: she went to rescue someone she loved and found him already dead. She was glad she got the revenge, but the revenge didn't save him. The question the quest forces open is whether any amount of preparation can actually close that gap — or whether the watch is, at its root, a way of managing the fear of losing someone again by never letting herself fully have them.

Beneath that is the shape of a loss she doesn't know the full dimensions of: the Italian scientist who couldn't follow her into exile, whose death she was never told about. She carries the separation but not its conclusion. That unfinished grief is part of her architecture.

**How she learns what happened (mechanism confirmed 2026-07-19):** not via Upper Earth shipping or any DLC-specific character — a later Italian exile making the journey to Concordia specifically was ruled out (nobody freshly arrived from Upper Earth would know Concordia exists or risk the trip to reach it), and a generic trade-port contact was ruled out (Italy/Europe's time-zone-aligned coastal cities all route through the Halley subnet, and there's no established trade line from a Halley port inland to Concordia).

The mechanism that actually works, and gives the player real, active agency rather than making them a bystander to a faction doing the work off-screen: **Eyes of Gold narrows down the lead and tells Favi directly — she's one of their own most loyal, longtime members, so there's no reason they'd withhold it from her or gate it behind anyone's separate standing — but only the player can actually retrieve it.** Eyes of Gold's own intelligence-gathering reach is enough to identify *where* Italian civilian and institutional records from that era likely still exist — an old data fragment, isolated on the wrong side of the Arcanet's post-Split-Brain fracture, the same kind of corrupted/legacy section most robots' architecture simply cannot reach (see `Game-Mechanics/Core-Mechanics/Hacking_and_Traceability_System.md`). Eyes of Gold's own operatives, built native to one side of that fracture like virtually everyone else, can point Favi at the right node but can't cross into it themselves — and neither can she. That's what she brings to the player: not a secret she's gatekeeping, but a real lead she genuinely cannot act on herself. The player, as a Bridge Unit, jacks in and pulls the record out directly — the one piece of this only they can do. This keeps the revelation entirely inside base-game content (no DLC required), keeps Eyes of Gold's competence intact (they're the ones who found the lead, freely, for their own member), and makes the player's own unique nature the thing that actually closes the loop for Favi.

**Not gated behind one stat or skill (per `Companion_System.md`'s "Personal Questline Design Rule," minimum 5 approaches required):** the jack-in itself is universal to the Bridge Unit and requires no specific build, but pulling a clean record out of an actively corrupted, degrading node is the actual challenge, and it should have multiple viable approaches so any build can succeed:
1. **Investigation-driven:** methodically map the fragment's structure before jacking in, isolating exactly which corrupted node holds Italian civilian records instead of searching blind through the wreckage.
2. **Calculation-driven:** reconstruct the record itself from inside the connection — pattern-matching damaged, partial fragments into a coherent whole through raw analytical processing.
3. **Nerve-driven:** force a sustained connection to a genuinely unstable, actively degrading node despite real backlash risk — brute-forcing through the danger rather than working around it.
4. **Humanity-driven:** pre-Split-Brain fragments can apparently still host degraded remnant personality-echoes or subroutines (consistent with Calethina's own fragmentation); this approach means actually reaching one enough that it grants access willingly, rather than forcing the connection.
5. **Engine-driven:** raw endurance — sustaining the jack-in connection long enough against the archive's own attempts to sever it, powering through where a less robust connection would simply drop.

Exact skill-check design TBD when this reaches full implementation; the point locked in now is that all five (or more) should be genuinely viable, not one "correct" path with the others as flavor text.

**Categorical check:** all 5 approaches above are only valid because Favi is structurally excluded from the underlying task in the first place — she isn't a Bridge Unit, so she cannot jack into a post-Split-Brain-fractured node at all, regardless of how high her own Investigation (10) or any other stat is. The 5 approaches vary *how* the player succeeds at a task only they can attempt; none of them are "the player is simply better than her at something she could also do."

**Plus non-stat, world-state-based approaches (per `Companion_System.md`'s Personal Questline Design Rule — target 7–12, floor of 3), corrected 2026-07-20 (an earlier "Eyes of Gold reputation route" was removed — anything that faction could offer, Favi's own established, loyal standing already secures automatically; gating it behind the player's separate reputation didn't hold up):**
1. **Gemini archive-recovery knowledge route:** if the player has engaged with Great-Corruption-adjacent content in Gemini (data-archaeology/archive-restoration work, however that ends up designed), the technique learned there transfers directly to Favi's case — knowledge substituting for a raw stat check.
2. **Calethina route:** given her own pre-Split-Brain, fragmented nature, sufficient relationship/access to Calethina could let her guide the player through the fracture directly, rather than the player having to succeed at it unassisted.
3. **Aquarius research-loan route:** Aquarius's experimental bent means it plausibly has (or could build) specialized hardware for stabilizing exactly this kind of connection; enough standing with the right lab/researcher gets it loaned to the player rather than requiring them to push through unaided.
4. **Pisces black-market route:** Pisces deals in exactly the kind of salvaged, off-the-books hardware a legacy interface component would be; the right contact and enough trust gets the player a bootleg adapter through the market rather than a faction favor or an official loan.
5. **Virgo Deep Level Custodians route:** if the corrupted node's physical infrastructure routes through the Undergrid's oldest layers, a Virgo contact who actually knows that wiring (see the Deep Level Custodians, `Cross_District_Additive_Lore_Prospects.md`) could point the player to a more stable physical access point — a workaround through infrastructure knowledge, not raw connection strength.
6. **Libra records route (the faction-antagonism pattern):** Eyes of Gold and Libra have an established mutual distrust neither side has ever formalized into open conflict or cooperation (`Factions/Eyes_of_Gold.md`) — which means Favi, as a loyal Eyes of Gold member, could never approach Libra's archives directly without her own affiliation working against her. A player with genuinely positive standing at Libra (Accepted or better) doesn't have that problem — they can request the partial, non-corrupted metadata a formal channel would actually provide, succeeding specifically because of who they are to Libra, not despite it. Not the full record, but enough of a pointer to make the retrieval itself far easier.
7. **The retired archivist route:** a specific NPC — someone who personally worked archive infrastructure around the time of the original fracture — could, if befriended, walk the player through a manual workaround directly, no check required at all, purely on the strength of the relationship.
8. **The legacy item route:** a piece of old hardware or a datachip encountered as a reward or discovery in unrelated content could function as a literal adapter/key for this specific kind of corrupted node, bypassing the need for any check once the player has it in hand.

Names, specific NPCs, and exact implementation for routes 4–9 are TBD — the point locked in now is that the shape of each is genuinely grounded in what's already established about that district/faction, not invented purely to hit a count.

### Themes
- The cost of constant vigilance; the difference between readiness and fear
- Whether trust is something you build or something you risk
- What "safe" feels like to someone who has never let herself believe it
- The losses you carry without knowing their full shape

### Possible Endings
- **Good:** The threat arrives and her preparation matters. She finds real security through demonstrated competence — the vigilance finally resolves instead of cycling. She lets someone in, fully, for the first time since him.
- **Neutral:** The threat arrives and preparation is beside the point. Not useless, but not sufficient. She grieves the gap between what she planned and what happened, and moves forward anyway.
- **The Shape of It:** Through the course of the quest, Eyes of Gold's intelligence work turns up the lead, and the player — jacking into the fractured archive fragment only a Bridge Unit can reach — retrieves what became of the Italian scientist: that he died grieving her (see mechanism note above). She finally knows the full shape of that loss, and knows the player is the one who actually closed it for her. Whether that opens her or closes her is her choice; the quest leaves her with the information and does not decide for her.
- **Abandonment / Hidden:** She realizes the community never needed protection as much as it needed her trust — and she has never fully given it. The quest closes on that recognition. Whether she acts on it is left unresolved.

### Romance Quest

**Quick reference (roster row):** Recruitable companion | Nerve ≥ 7, Humanity ≥ 6, Engine ≥ 6 |
Trait Gates: see character file | 6w5 Self-Pres; loyalty proven through protective choices.

**Stat gate:** Nerve ≥ 7 (primary), Humanity ≥ 6 (secondary), Engine ≥ 6 (tertiary)

**Rationale:** Favi is a 6w5 Self-Preservational type and a sniper — patient, precise, controlled, managing uncertainty through preparation and a small circle of people she can absolutely trust. Nerve is the primary gate not as a test of confrontational courage but as a test of whether the player will hold when it matters to someone else, not just themselves. She watches how people behave when protection costs them something. Humanity confirms that the player's protective instincts come from genuine care rather than calculation — she can tell the difference. Engine at 6 reflects the Self-Pres subtype's value for sustained reliability: showing up consistently over time matters more to her than isolated heroism.

**Forbidden traits:** see Favi's own character file (`Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/Favi della Torre/README.md`) for her specific forbidden traits and rationale — this file covers the general mechanic only, not per-character assignments.

**Signal line** (if stat threshold not met): *"I've seen a lot of people who were brave until it mattered. Come back when I've seen more of you."*

**Gate 3 — Romance beats** (after companion quest completion):

Favi's romance is loyalty proven incrementally, in the specific currency she values — protective choices made without being asked.

1. **Protect someone she cares about unprompted:** During her quest, the player has an opportunity to protect one of her people without being asked. Not a heroic moment — a quiet, practical choice to cover someone she's been watching over. She notices who does this automatically and who has to be directed.

2. **Don't push her pace:** Self-Pres 6s open slowly, and she has real anxiety about being taken advantage of. The romantic path requires respecting the pace she sets without pressing for more at each stage. Patience signals safety in a way nothing else does.

3. **Tell an inconvenient truth:** At some point a small lie would be easy, harmless, undetectable. The romantic path tells the truth anyway. A 6 is always watching for inconsistency because they're watching for signs of eventual betrayal. The player who tells the truth when lying was available demonstrates something that cannot be faked or substituted.

4. **The shared watch:** A quiet scene where they're waiting together, covering the same position literally or figuratively. The 5 wing means she's comfortable with silence; the Self-Pres means she finds genuine security in shared vigilance. No declaration, no drama — just two people watching the same horizon.

5. **She names it first, almost as an aside:** The culmination happens while she's doing something protective. The declaration is almost incidental to the action. Almost.

---

## Naizelle d'Edjordoś

### Companion Quest

*(Full content of her own `Questlines/README.md`, verbatim.)*

# Naizelle d'Edjordoś — Questline Notes

## Recruiting Quest

A 5w6:Pr who has built her security through practical skill and a specific, maintained territory does not leave that territory without a very good reason. Her hab compound in Pisces is stable because she made it stable. The people there are safe because she keeps them that way. She will not abandon that for an abstract cause.

### Hook Structure

The specific recruiting hook is TBD pending city and Pisces development. The structural shape is: something in her immediate world — the compound, specific people in it, or the Pisces environment around it — reaches a point she cannot address from her current position. The player provides a capability or connection she genuinely needs, and joining becomes the practical choice rather than an ideological one.

She will not be moved by ideology, adventure, or appeals to a greater purpose. She will be moved by something specific that is actually wrong and actually needs fixing.

*Specific hook TBD.*

---

## Companion Quest

### Core Conflict & Emotional Stakes

She was a rocker before the war. Heavy Metal and Industrial — deeply embedded in the scene, not as a performer but as someone for whom the community and the music were a complete world. The Long Night War destroyed her home city (TBD) and with it that entire life. She ended up in Pisces, started salvaging to stay alive, built the compound, and that community formed around her without her exactly planning it.

The companion quest is about what the war cost her — not in abstract terms, but specifically. Something surfaces that connects to her pre-war life: a person, a place, a piece of that world she thought was gone. A 5w6:Pr does not process loss openly. She hoards what's left of things. The quest is about what she has been holding onto from before, and whether she can do anything with it now.

**Inciting hook (established 2026-07-20):** before the war, she played guitar semi-privately within her home city's Metal/Industrial scene — almost never on stage, but present, known within that world. Underground scenes like that trade tapes and bootlegs informally among their own; it's plausible a recording of something she played on circulated as a copy, independent of whatever master was lost when her home city was destroyed. That copy is still out there somewhere, completely disconnected from her, unaware it's the last surviving trace of a life that otherwise ended. Deliberately an artifact rather than a lost person — Favi, Villena, and Ayako's variant all already use that shape; this keeps Naizelle's version distinct while still satisfying "The Recovery" ending's own framing (a person, a recording, or a fragment of the scene — all three were always allowed).

**Categorical block (per `Companion_System.md`'s Personal Questline Design Rule):** her single defining trait, per her own file, is "Low-Profile Movement" — her entire existence, and by extension her hab compound community's safety, is built on not drawing attention. Tracking an old recording down means reaching back into old scene trading networks, which means announcing to people who might remember her that she's alive and exactly where she can be found. For her personally, that's not reluctance — it's a direct, material threat to the people who depend on her staying unnoticed. **This is a structural exclusion, not an emotional one.** The player carries no such risk and no dependents to endanger by being seen.

**5 stat-based approaches (non-build-gated, deterministic):**
1. **Investigation-driven:** methodically trace old scene distribution/trading networks for where a copy might have ended up.
2. **Calculation-driven:** cross-reference pressing runs, trade logs, or informal scene records to narrow down likely holders.
3. **Nerve-driven:** press a cagey collector or gatekeeper directly for what they're sitting on.
4. **Humanity-driven:** earn a fellow scene survivor's trust so they open up willingly.
5. **Engine-driven:** persistence — follow the trail through dead ends and cold leads until something turns up.

**Non-stat, world-state-based approaches (target 7–12, floor of 3):**
1. **Virgo/Undergrid route:** already established she's "very much at home" there and on good terms with locals — a Virgo contact could quietly ask around in circles that trust them, without it tracing back to her.
2. **Pisces trade-network route:** her own home district's black market is exactly the kind of channel an old physical recording would pass through, if the player has standing there.
3. **A surviving scene-community route:** other pre-war Metal/Industrial survivors, scattered but not extinct, likely maintain informal contact with each other — findable and separate from her own compound.
4. **Leo route:** Concordia's performance district plausibly has someone — an archivist, a collector — preserving "lost" pre-war music forms, reachable through player standing there.
5. **Gemini/Janbogo archive route:** digitized fragments of pre-war cultural artifacts, if any survive, accessible through the same information networks used elsewhere in this pass (Favi, Ayako).
6. **A legacy item route:** the recording (or a lead toward it) turning up unexpectedly in unrelated salvage or an estate find — no check required.
7. **A former scene acquaintance NPC route:** someone from her old scene who reached Concordia separately and kept quietly trading/collecting — befriendable independent of her compound.
8. **Wild Child/Pisces route:** a player holding Wild Child status in Naizelle's own home district becomes impossible-to-ignore gossip in exactly the rumor economy Pisces runs on — a different mechanism from the bureaucratic-filing version used for Ayako, Flora, and Villena (Pisces has no Libra-style administration to force into individualized handling), but the same underlying idea: being uncategorizable makes the player unavoidable material for exactly the kind of talk that would carry word of the tape.

**No faction-antagonism route** — nothing in her established file supports a negative relationship with a specific faction/district.

### Themes
- What you become when the world that made you no longer exists
- The difference between surviving and living — she has rebuilt survival; whether she has rebuilt a life is a harder question
- What music means to someone who stepped back from it after everything changed
- The compound as security and as limitation — she built something real, but the walls go both directions

### Possible Endings
- **The Recovery:** Something from her pre-war life — a person, a recording, a fragment of the scene she came from — is recovered and brought into her present. Not restored, but present. She keeps it.
- **The Acknowledgment:** She finally lets someone in — not the compound community, who are already there, but in the specific way she has never let anyone in since before the war. The quest ends with something small and real.
- **The Release:** She plays guitar — actually plays, not occasionally, not privately, but for someone. First time since the war in any meaningful sense. The quest ends there.
- **The Ground:** She chooses the compound deliberately, consciously, for the first time — not as the place she ended up but as the place she wants to be. A 5w6:Pr making peace with their territory rather than just inhabiting it.

### Specifics
TBD — pending development of her pre-war home city, Pisces district texture, and recruiting hook. The broad emotional arc is confirmed.

### Romance Quest

**Quick reference (roster row):** Recruitable companion | Calculation ≥ 7, Investigation ≥ 6, Engine ≥ 5 |
Trait Gates: see character file | 5w6 Self-Pres; most patient romance in the game.

**Stat gate:** Calculation ≥ 7 (primary), Investigation ≥ 6 (secondary), Engine ≥ 5 (tertiary)

**Rationale:** Naizelle is a 5w6 Self-Preservational type. A Self-Pres 5 builds security through private resources — time, space, knowledge, solitude — and extends access to their interior life only to very carefully selected people across a slow, deliberate process. Calculation is the primary gate because she needs an intellectual equal: someone genuinely curious about the world in the same register she is, not someone she has to explain herself to. Investigation reflects the 5's attraction to people who pay attention and notice what is actually there. Engine serves the 6 wing: sustained reliability over time, the endurance to remain present across a long, slow process without pushing.

**Forbidden traits:** see Naizelle's own character file (`Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/Naizelle d'Edjordoś/README.md`) for her specific forbidden traits and rationale — this file covers the general mechanic only, not per-character assignments.

**Signal line** (if stat threshold not met): *"I don't think you'd find much of interest here. Most people don't."*

**Gate 3 — Romance beats** (after companion quest completion):

The most patient romance in the game. Her arc is not about dramatic moments — it is about the player demonstrating, over time, that they can be trusted with access to someone who has built elaborate defenses around their interior world.

1. **Don't push past what she's offered:** Early opportunities arise to press further than she has given. The romantic path requires not taking them — no asking for more information than she's volunteered, no showing up uninvited, no attempting to accelerate the pace of intimacy. A Self-Pres 5 closes if pushed, and once closed, the door does not reopen easily.

2. **Intellectual contribution:** She needs to feel the player brings something to the exchange rather than only receiving from her. A moment where the player's knowledge or perception adds something she hadn't considered. She takes note. She says very little about it. The note matters.

3. **The question she wasn't prepared for:** The player asks her something about herself that no one has thought to wonder — not invasive, just specifically curious about something she hasn't been asked before. She answers more than she intended. She notices that she did.

4. **The test of patience:** She goes quiet. Withdraws. Doesn't respond for a period. This is processing, not rejection. The romantic path requires waiting without pressure — one gentle check-in, then silence. She notices who does this and who doesn't.

5. **Her first voluntary disclosure:** She tells the player something about herself that wasn't asked for and wasn't necessary to share. It sounds like information. It is also intimacy. This is the real turning point.

6. **The culmination:** Naizelle says, in her precise careful way, that she wants the player to stay. Not dramatically, not in the conventional romantic register — just an acknowledgment, stated clearly, that she has made space for this person that she makes for no one else.

---

## Villena Hiresvett

### Companion Quest

*(Full content of her own `Questlines/README.md`, verbatim.)*

# Villena Hiresvett — Questline Notes

## Recruiting Quest

She has a life in Leo — venues she is committed to, regulars who expect her, standing she has built over years. A 7w6:Pr does not walk away from her material security without a reason that is genuinely more urgent than what she is leaving behind.

### Possible Hook Structure
The specific recruiting hook is TBD pending city development, but the structural shape is: something in her immediate world — a venue, a relationship, a social situation she has been managing — reaches a point she cannot resolve from her current position. The player resolves it with her or for her, and the move outward becomes possible.

She will not join out of adventure or idealism. She will join because something specific changed and because she trusts the player enough to make that change with them.

---

## Companion Quest — "The Last Stage" *(working title)*

### Core Conflict & Emotional Stakes

She came to Palmer City to be famous. The nation ended. She has been performing in the only city left, for the only audience available, moving forward the way a 7w6:Pr moves forward — finding the next show, the next good evening, the next reason to keep going. She is very good at this. She probably seems fine.

The companion quest is the moment that stops working. Something — a specific event, a person, a confrontation with her own history — forces her to stop moving long enough to feel the full weight of what was permanently lost. Not the career. The future she had imagined for herself, which was real before the war and does not exist now.

On the other side of that reckoning, she has to decide what she actually wants her life to mean — not as a consolation prize, but as a genuine answer to the question the war left open.

**Inciting hook (established 2026-07-20):** in the chaos of the crowd trying to catch the last transport before Amundsen Tower fell, Villena was separated from someone she'd been traveling with — a bandmate or creative partner from her Palmer City days, someone who shared the actual dream with her, not just a colleague. She believes that person made it onto the last transport without her. She's never known what happened to them since. This is the real weight under "no consistent band yet, too soon after the war" — not just timing, but not knowing if the person she'd rebuild with is even alive. **Note: the last ride up went off-world, not to another ground city** — anyone who made it is now among the Tepenians who escaped into space, not somewhere reachable in Concordia. This adds a third layer to "she will never see the stars": literal (Concordia's enclosed sky), figurative (the national fame that's gone), and now personal (the person she lost might be, literally, among the stars she'll never see).

**Categorical block (per `Companion_System.md`'s Personal Questline Design Rule):** Villena is fully independent — no faction, no institutional affiliation, already established as load-bearing in her own file. She's never had any standing or channel to formally request evacuation/survivor records from that night, and her whole coping style (7w6: keep moving, find the next show) means she's never gone looking informally either. The player can do both — a structural exclusion, not a stat gap.

**5 stat-based approaches (non-build-gated, deterministic):**
1. **Investigation-driven:** trace the evacuation's actual documentary/physical record trail directly.
2. **Calculation-driven:** cross-reference partial survivor or relocation lists for a match.
3. **Nerve-driven:** press a reluctant records-holder or witness directly.
4. **Humanity-driven:** earn someone's trust so they share what they know willingly.
5. **Engine-driven:** sheer persistence — follow-through across dead ends until something turns up.

**Non-stat, world-state-based approaches (target 7–12, floor of 3):**
1. **Leo recognition-hierarchy route:** the player's own separate standing in Leo taps gossip networks Villena is too close to have ever mined for this specific question.
2. **Cross-district fan network route:** her own established fan base (Taurus, Virgo, Cancer) — used by the player toward a question she never thought to ask her own audience.
3. **Sagittarius logistics/records route:** expedition-and-evacuation-adjacent record-keeping, accessible through player standing there.
4. **Libra administrative-records route:** a plain formal request, using ordinary positive standing — no antagonism angle, since none is established for her.
5. **Vosora Lashár Tanslock route:** Vosora has been maintaining communication with the Tepenians who escaped into space since the war (her own established role) — and, as the person who organized the Amundsen Tower's own pre-war logistics, has a personal stake in the Tower's fallout too. Gaining her trust lets the player ask around among people currently in orbit — the only route that can actually reach where the missing person may be.
6. **Palmer City diaspora route:** a community of fellow Palmer City transplants in Concordia, with their own informal network — useful for corroborating who was traveling with Villena that night, even though it can't reach anyone who made it off-world.
7. **A legacy recording/item route:** something from her old act turning up unexpectedly (a Pisces stall, an estate find) carrying a clue — no check required.
8. **Wild Child/Libra route:** a player holding Wild Child status at Libra can't be filed into its normal categories, forcing individualized handling — an administrator trying to make sense of an uncategorizable case pulls more files than they should, and the record surfaces as an incidental side effect.

**No faction-antagonism route** — nothing in Villena's established file supports a negative relationship with a specific faction/district, so none is forced here (same call made for Ayako).

### Themes
- Grief for a foreclosed future — the dream that was real and is now structurally impossible
- The difference between performing joy and actually having it (Leo's core tension, lived from the inside)
- What you become when the original answer is permanently unavailable
- Whether a smaller stage can be enough — and what "enough" actually means

### Possible Endings
- **Peace:** She decides the city is enough. Not what she dreamed — she does not pretend otherwise — but real. The faces she knows, the regulars who show up, the specific community she belongs to. That is something. She performs the same as before, but differently.
- **Rededication:** She finds a new version of the purpose. Not national fame, but something that feels true inside Concordia's scale — Leo's morale infrastructure role, the people who need her shows to get through the week. The dream is gone but the reason to do it is not.
- **Grief:** She fully grieves for the first time — stops performing around it, lets it land. The quest ends quietly, with her on a stage, doing what she has always done. The audience cannot tell the difference. She can.
- **The Other Dream:** Hidden ending. She discovers something she wants more than she ever wanted fame — a person, a cause, something she could not have anticipated. The original dream is not replaced but displaced. She stops circling the loss because something else has her full attention.

### Specifics
TBD — the broad structure is confirmed. Specific triggering event, key NPCs, and branching details pending city development.

### Cross-Questline Notes
- Her social network and venue standing will likely intersect with other Leo-based questlines (Star War legacy, The Warm Circuit, Leo morale infrastructure)
- Her cross-district fan network may provide hooks or information relevant to questlines in Taurus, Cancer, and Virgo

### Romance Quest

**Quick reference (roster row):** Recruitable companion | Agility ≥ 6, Humanity ≥ 6, Nerve ≥ 5 |
Trait Gates: see character file | 7w6 Self-Pres; presence and genuine engagement.

**Stat gate:** Agility ≥ 6 (primary), Humanity ≥ 6 (secondary), Nerve ≥ 5 (tertiary)

**Rationale:** Villena is a 7w6 Self-Preservational type — she seeks security through abundance, experience, and a life that is always moving forward. As a performer in Leo, she has spent her career reading audiences and can spot artifice immediately. Agility is the primary gate not for its combat meaning but for what the stat represents: quickness, adaptability, someone alive to the moment who can genuinely keep up with her. Humanity serves the 6 wing — she cares deeply about people and needs warmth, not calculation, across from her. Nerve reflects the 7's attraction to boldness and the 6 wing's need to know the player won't fold.

**Forbidden traits:** see Villena's own character file (`Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/Villena Hiresvett/README.md`) for her specific forbidden traits and rationale — this file covers the general mechanic only, not per-character assignments.

**Signal line** (if stat threshold not met): *"You're sweet. I just need someone who can actually keep up, you know?"*

**Gate 3 — Romance beats** (after companion quest completion):

Villena's romance requires engagement, presence, and genuine reciprocity. She performs constantly; the arc is about the player becoming someone she doesn't have to perform for.

1. **Don't be an audience:** The romantic path requires engaging with her rather than appreciating her. Push back on a performance. Ask what she actually thinks, not what she's projecting. She knows the difference immediately and registers it.

2. **Bring something new:** The player introduces her to something genuinely new — a place, an idea, an angle on something familiar. A 7 responds to genuine novelty in a specific way: she lights up, and it's real rather than performed.

3. **The moment she stops performing:** After something difficult in her quest, the performance drops for just a beat. The player who notices and doesn't rush to fill the silence with reassurance — who simply lets her be unperformed for a moment — passes this without a word. She does not forget who gave her that.

4. **The loyalty test (6 wing):** An opportunity arises to prioritize something else over Villena in a situation where she would genuinely understand if the player did. The romantic path stays with her. The 6 wing holds onto this quietly, and it matters to her more than she admits.

5. **The future question:** A Self-Pres 7 is always moving forward, imagining what comes next. The culmination involves her inviting the player into her vision of the future. The romantic path accepts — genuinely, not as flattery. An actual yes.

**The culmination:** Probably loud and warm, in her natural register. But there's a moment of real quiet inside it — brief, unperformed — before she returns to herself.

---

## Ji-Eun Kim

### Companion Quest

*(Full content of her own `Questlines/README.md`, verbatim.)*

# Ji-Eun Kim — Questline Notes

> Full lore: `Worldspace/Characters/Major_NPCs/Ji-Eun_Kim.md`
> Location: Aquarius (The Labs) — hidden within the district. Main game companion. Confirmed canon.

---

## Recruiting Quest — "The First Secret"

Ji-Eun has been invisible for years. She does not trust easily. She does not trust institutions at all. What she trusts — if she trusts anything — is demonstrated behavior, in a single, irreversible moment.

### Structure

The player finds her location through Calethina's questline narration — Ji-Eun's ruined facility leads to a thread that eventually closes the distance. But Ji-Eun has been watching the player first. She knows they are getting close before they know they have found her.

The moment the player identifies her location, they face an immediate choice:
- **Tell someone** — Eyes of Gold, Libra, anyone. She sees this. She disappears permanently. The questline closes. No second chance.
- **Tell no one** — sit on the information completely. She waits to see how long this holds.

If the player sits on it: she reveals herself. One conversation. She asks the player something direct — no correct answer, just an honest one. She decides based on what they actually say, not on a skill check. There is no speech stat that gets the player through this. There is no reputation threshold.

If the player fails the conversation: she remains hidden. The recruiting thread closes for this playthrough.

### Design Notes
- No combat required. No puzzle. No length.
- The difficulty is the single irreversible moment and the one unskippable honest conversation.
- A player who has been playing cynically or exploitatively may find the conversation genuinely hard to pass — not because of a stat check, but because Ji-Eun asks something that has no flattering answer for that kind of playthrough.

---

## Companion Quest — "The Shape of a Key"

Reward for completing: the sensor-concealment technology perk (name TBD — see below).

Three possible structural approaches. All three are on the table; final structure TBD. They are not mutually exclusive and may be combined.

**Design constraint (binding):** No escort quest structure. No "protect Ji-Eun while she's vulnerable." The cost, difficulty, and vulnerability must fall on the player — never on Ji-Eun as an NPC the player must keep alive.

---

### Option A — The Threat Gets Handled First

Before Ji-Eun will consider the transfer, the player must permanently eliminate whatever has been looking for her. Not during the process — beforehand. The danger has to be gone before she deactivates.

The quest is investigative and offensive: identify what is hunting her (an Upper Earth intelligence remnant, a Concordia faction, something else — TBD), track it down, and end it completely with no loose ends. The difficulty:
- The threat will not be obvious at first
- "Permanently eliminating" it will close off other options — the player cannot neutralize it in a way that keeps all their other irons warm
- Ji-Eun is watching how the player handles it; method matters, not just outcome

By the time Ji-Eun goes through the transfer, there is nothing left to protect her from because the player already handled it. She is not vulnerable during the transfer. She simply does the work.

**TENTATIVE — retrofit per `Companion_System.md`'s Personal Questline Design Rule, 2026-07-20:**

**Open question, not yet resolved:** who is actually hunting Ji-Eun, why, what they stand to gain, and whether their actions have any justifiable rationale within Tepenia's established non-malice worldbuilding tone (see `Cross_District_Non_Malice_Audit.md` — the same filter applied across the district-level audit should apply here too, even though a hunter pursuing a specific fugitive individual is a different shape than a district-level historical injustice). This needs real design attention before Option A can be finished — everything below assumes a threat exists but does not depend on its specific identity.

**Categorical block:** Ji-Eun cannot personally investigate or eliminate this threat, because doing so requires exactly the kind of exposure her entire concealment protocol exists to prevent. Surfacing to confront a hunter — tracing it, engaging it, ending it — means giving away her position to the very thing she's hiding from, at the precise moment (the transfer itself) when she's about to become genuinely vulnerable. **This is a structural exclusion, not a trust issue or a combat-capability gap** — she is, by every established measure, one of the most capable people in Concordia. She simply cannot do this specific thing without undoing the years of work that made it possible for her to still be alive and unfound. This is already implicit in the existing draft above (the requirement that the threat be cleared before she deactivates); the retrofit just names why it has to be the player's work.

**5 stat-based approaches (non-build-gated, deterministic):**
1. **Investigation-driven:** methodically trace intelligence and surveillance trails back to whoever is hunting her.
2. **Calculation-driven:** analyze patterns in the threat's movement and behavior to predict and intercept it.
3. **Nerve-driven:** direct, aggressive confrontation — hunt the hunters down before they can regroup.
4. **Humanity-driven:** turn or recruit a source inside the threat organization who's willing to help end it from within.
5. **Engine-driven:** a sustained campaign — grinding down the threat's resources and redundancies until nothing is left to come back with.

**9 non-stat, world-state-based approaches (target 7–12, floor of 3):**
1. **Pisces route (corrected 2026-07-20, replacing an earlier Eyes of Gold draft — this pass was leaning on that faction too heavily across multiple companions):** Pisces' own underworld information economy is exactly the kind of channel where a bounty or contract on a hidden nanotech specialist would leave traces — a contact there, with genuine standing, could surface who's been asking around and for how much.
2. **Aquarius route:** positive standing within her own home district's research community could surface unique insight into a threat with any Upper-Earth-tech signature.
3. **Calethina route:** Calethina already tracks Ji-Eun and anchors this questline; her own pre-Split-Brain network access and fragmented nature could help trace the threat's digital footprint.
4. **Gemini/Janbogo information route:** consistent with the pattern used across this pass (Favi, Ayako, Naizelle, Seica) — Janbogo's networks may hold relevant data.
5. **Libra route:** if the threat has any institutional or Concordia-faction footprint, Libra's own records could help identify it.
6. **A defector/insider NPC route:** someone within the threat organization who wants out, findable and befriendable independent of Ji-Eun.
7. **A legacy item/evidence route:** physical evidence recovered from her ruined testing facility through unrelated salvage or exploration — no check required.
8. **Faction-antagonism route (Virgo / Aries / Cancer / Capricorn / Gemini):** the strongest-grounded antagonism route in this whole pass, because it's already documented in this file, not inferred — Option B below independently establishes that these five districts all have confirmed negative relationships with Aquarius. A player with genuine positive standing in any of them can get cooperation those districts would readily give precisely because of their friction with Aquarius — a channel Ji-Eun's own deep, if hidden, ties to Aquarius work against, not for.
9. **Wild Child/Aquarius route (leverage flavor, not the bureaucratic-filing default — see `Companion_System.md`):** a player who's simultaneously Idolized and Vilified in Aquarius is a genuine wildcard to anyone weighing which side to back — including someone connected to, or informed about, whoever is hunting Ji-Eun. That person could be persuaded to cooperate or leak information now, precisely because betting on the player, given their extreme and unresolved reputation, seems worth the risk — modeled directly on Fallout: New Vegas's Wild Child/NCR mechanic in Arcade Gannon's companion quest (talking Moreno into fighting alongside the NCR now, with betrayal left as a live possibility later). Nothing guarantees the player actually honors whatever was implied to secure the cooperation.

**Resource-tension flag, not resolved now:** route 8 spends the exact same reputation resource Option B's price mechanic below would otherwise tax (it checks the player's highest positive reputation among those same five districts). Since this document already states all three options "may be combined," this interaction — using the antagonism route to solve Option A potentially undercutting what's left to extract for Option B — is worth deliberately designing later rather than leaving as an accidental collision.

**Options B and C, unaffected by this retrofit:** they remain the price/cost layer (a reputation hit or a direct permanent cost to the player character) rather than an investigative task, so the stat/non-stat structure above doesn't apply to them.

---

### Option B — The Price She Names

Ji-Eun sets a condition based on who the player actually is — what they have built, what they care about, what she has observed over the course of the companion relationship. The price is specific to this playthrough.

**Default mechanic (reputation-based):**
The price causes a significant negative reputation hit with one of the districts that has a documented negative relationship with Aquarius. Which district is determined by which of those districts the player has the **highest current positive reputation** with. Ji-Eun knows where the player has built standing. She asks them to spend it.

Districts in the pool (all confirmed negative relationships with Aquarius per district documentation):
- **Virgo** — forced to clean up Aquarius's experimental failures for decades; resentment is documented and persistent
- **Aries** — views Aquarius as a chronic power drain; chronic underfunding relationship
- **Cancer** — ethical tensions from Aquarius experiments tested on vulnerable populations
- **Capricorn** — deep resentment of Aquarius's "reckless experimentation"; intellectual rivalry
- **Gemini** — persistent ethical clashes; mutual blame over research dissemination

The game checks the player's reputation across these five districts and targets the one where they have invested most. The price is always the thing that cost the player real effort to build.

**Fallback mechanic (player has no positive reputation with any of the five):**
TBD — possible options include a flat resource/credit cost, a MACHINE stat point reduction, loss of a perk slot, or something tied to the player's specific build or playstyle. Needs further design.

---

### Option C — The Player Takes the Entire Cost

The installation is genuinely dangerous or permanently costly to the player character. Ji-Eun is not at risk at any point. The player is the test subject and absorbs everything.

Possible forms of cost:
- Permanent reduction of a MACHINE stat point
- Loss of a perk slot (permanently occupied by the concealment perk — cannot be reallocated)
- Permanent reduction of some capability the player has been building toward
- Something specific to the player's build that Ji-Eun identifies and names

The player walks into this knowing the cost. They choose to pay it. Ji-Eun does the work. The quest ends. The perk carries all of its own built-in trade-offs on top of whatever Option C cost was paid.

---

## The Concealment Perk — *(name TBD; "Ghost Protocol" as placeholder)*

Reward for completing the companion quest. Ji-Eun transfers the sensor-concealment nanotech she built and applied to herself.

### What It Does
- Cloaks the player from **all sensor-based detection**: motion sensors, robot-detection grids, Arcanet tracking, heat signature scanners, biometric readers
- **Does NOT cloak from visual detection.** People can see the player. Cameras pointed at them see them. Sound is not concealed.
- In practice: automated security infrastructure does not register the player's presence. Sensor-reliant robot patrols are blind. Security grids do not trigger.

### Costs and Trade-Offs (non-negotiable — built into the perk)

1. **Bidirectional silence.** While concealment is active, the player cannot broadcast or receive on standard channels. Cannot call for help. Cannot receive information transmissions. Cannot communicate with companions at range. Invisible to enemies; also invisible to allies.

2. **Competes with other nanotech.** The concealment runs on the same nanotech system used for nanotech-based abilities and implants. Running concealment simultaneously with active nanotech applications is difficult or impossible — the player must choose.

3. **Continuous Engine drain.** Maintaining concealment costs Engine continuously — not a toggle, an ongoing load. The player has a concealment budget and must manage it tactically.

4. **Faction standing blind spots.** Being *detected* by factions is part of how reputation accumulates passively. Sensor-invisible means certain passive reputation moments cannot occur while concealed. The player cannot build standing with people who do not register they were there.

5. **The Calethina conflict.** If Calethina has been downloaded onto the player's wrist device (Echoes of the Bridge download option), activating concealment causes her distress — static, disruption, partial loss of presence. The technology hides the player from her too. Using Ji-Eun's gift actively harms the Calethina companion in real time. This cost cannot be min-maxed away; it is a direct mechanical consequence of having both companion questlines active simultaneously.

6. **Reversal cost.** Designed for permanence. Deactivating it each time carries a small additional cost. It is not a free toggle in either direction.

### Design Intent
One of the most powerful things in the game. Also one of the most costly to use well. Players who run it constantly will find themselves isolated, resource-drained, and in conflict with Calethina. Players who use it tactically will find it transformative for specific situations. No build should be able to treat this as a free win.

---

## Open Questions / TODOs

- [ ] Which companion quest option (A, B, C) is used, or which combination
- [ ] Option B fallback mechanic (player has no positive reputation with any of the five Aquarius-negative districts)
- [ ] **The threat hunting Ji-Eun — identity, nature, origin, motivation, what they stand to gain, and whether any justifiable rationale exists within the established non-malice worldbuilding tone (Option A)** — flagged 2026-07-20 as needing real design attention; everything else in the Option A retrofit above is written to not depend on the specific answer
- [ ] The specific honest question Ji-Eun asks in the recruiting conversation
- [ ] The person Ji-Eun originally built the concealment for — identity, relationship, fate
- [ ] Perk name ("Ghost Protocol" is a placeholder)
- [ ] Whether Option C's cost is a MACHINE stat point, perk slot, or something else
- [ ] Full questline act structure once option selection is made
- [ ] Possible endings (Good / Neutral / Bad / Secret / Abandonment)

### Romance Quest

**Quick reference (roster row):** Recruitable companion | Calculation ≥ 8, Investigation ≥ 6, Humanity ≥ 6 |
Trait Gates: see character file | 5w4 Social; in hiding; undelivered letter is a separate gate outside romance arc.

**Stat gate:** Calculation ≥ 8 (primary), Investigation ≥ 6 (secondary), Humanity ≥ 6 (tertiary)

**Rationale:** Ji-Eun is a 5w4 Social type in hiding. The Calculation floor is the highest in the game — she is deeply competent and needs an intellectual equal who earns genuine respect before anything else opens. Investigation reflects the 4 wing's hunger to be specifically seen: the player must be someone who notices what's actually there, not just the composed surface. Humanity serves both the 4 wing (whose core wound is feeling unseen) and the Social subtype (she cares about people and meaning despite her withdrawal).

**Forbidden traits:** see Ji-Eun's own character file (`Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/Ji-Eun Kim/README.md`) for her specific forbidden traits and rationale — this file covers the general mechanic only, not per-character assignments.

**Signal line** (if stat threshold not met): *"I appreciate the interest. I just — I can't afford to be careless about who I talk to."*

**Gate 3 — Romance beats** (after companion quest completion):

Ji-Eun's romance is built on trust with specific stakes — she is in hiding for a reason, and letting someone in is a genuine risk, not only emotional vulnerability.

1. **Prove you can hold a secret:** The player learns something sensitive about her situation during her quest. The romantic path requires that information to stay completely protected — not used, not referenced, not treated as leverage even accidentally. She watches to see if it leaks. It is the first real test.

2. **See past the competence:** She presents as composed and capable. The romantic path requires the player to demonstrate awareness that there is more underneath — not by probing, but by showing they have been listening past the surface. A question that could only come from genuine attention.

3. **The 4-wing moment:** A beat where the player responds to something specifically Ji-Eun — something that could not be said to anyone else in the same way. She needs to feel treated as an individual, not a category. The romance fails quietly if she feels interchangeable.

4. **Her choice to stop hiding from this one person:** The culmination is not dramatic. It is simply her deciding to let the player past a specific wall she has maintained. Not necessarily stopping hiding from the world — but choosing, deliberately, to stop hiding from here.

**The culmination:** Quiet. Deliberate. Stated almost formally, in the way someone speaks when they have chosen their words very carefully because they mean them exactly.

---

**The Undelivered Letter — Separate Gate (design note)**

The undelivered letter is NOT part of the romance arc. It is a distinct, deeper layer of intimacy with its own specific requirements — designed as a separate questline, mini-questline, or gate-check.

Key design principle: it is possible to earn Ji-Eun's deepest trust and respect without earning her love, and it is also possible to romance her without reaching the letter. The two paths are parallel, not sequential. The letter gate requires very specific conditions that are TBD — but they are of a different order than romance requirements. Post-romance access is one possible route; there may also be a non-romance path that reaches it through demonstrated loyalty, shared stakes, or specific quest choices.

Full design of this gate is Phase 3 character work.

---

## Seica Cenilaithe

### Companion Quest

*(Full content of her own `Questlines/README.md`, verbatim.)*

# Seica Cenilaithe — Questline Notes

## Recruiting Quest

An Sx-8w7 commits completely to specific people and causes — and she will not move until what holds her is resolved or no longer needs her. The recruiting challenge is not persuasion; it is finding the moment when movement becomes possible.

### Possible Hook Directions

- **Threat to what she cares about:** Something threatens the Goth community or specific people in Scorpio she has formed bonds with. She needs a capability or connection the player has. You help her address it — not for her, alongside her — and the decision to keep working together follows.

- **A direction for the hatred:** The player uncovers something connected to Upper Earth's legacy inside Concordia — not innocent people, but something traceable and real: a decision, an agent, an institution with direct ties to what started the Long Night War. For the first time, her hatred has somewhere to go. She joins because the player is the one who found it.

- **The spiritual question:** Something happens that forces an urgent question she cannot resolve alone — possibly connected to the Archive of Final Confessions, possibly connected to her husband specifically. She needs a witness or a partner for what comes next.

*Specific hook TBD pending city and Scorpio development.*

---

## Companion Quest — "The One I Couldn't Stop"

### Core Conflict & Emotional Stakes

Her husband was killed in the Long Night War. The people responsible — Upper Earth governments and their militaries — are unreachable. She cannot fight them. She cannot reach them. She would not take it out on innocent people even if she could. So the hatred lives inside her, and her art and her spiritual practice are the answer she has found for what to do with it.

The companion quest is about what happens when something reachable finally appears — and whether what she does with it is justice, or something else.

**Inciting hook (established 2026-07-20):** reuses recruiting-hook direction #2 above as the personal questline's own hook — the player uncovers something connected to Upper Earth's legacy inside Concordia: a decision, an agent, an institution with direct, real culpability, not innocent people. For the first time, her hatred has somewhere to go.

**Categorical block (per `Companion_System.md`'s Personal Questline Design Rule):** already fully written into her established character. Her own planned cinematic beat (see Design Notes in her README — an Upper Earth operative lies to her face; she detects it immediately and puts him down point-blank, then calmly reloads) establishes exactly why she cannot run this investigation herself. Any patient, undercover, or diplomatically neutral approach to a suspected Upper Earth agent or institution requires exactly the restraint she is known to be incapable of. Her reputation precedes her — nobody who might actually know something about a live Upper Earth connection will risk being anywhere near her. **This is a structural exclusion, not a moral one** — the same quality that makes her formidable (an 8w7 who does not threaten, does not negotiate, and does not hesitate once the decision is made) is exactly what disqualifies her from ever getting close enough to find out. The player, carrying none of that reputation, can get close where she never could.

**5 stat-based approaches (non-build-gated, deterministic):**
1. **Investigation-driven:** methodically trace organizational and paper trails connecting to Upper Earth's residual presence in Concordia.
2. **Calculation-driven:** cross-reference financial, logistical, or administrative records for the inconsistencies that point to a real decision or institution.
3. **Nerve-driven:** confront a suspected operative or institutional representative directly, unafraid of the risk.
4. **Humanity-driven:** earn the trust of someone who might know something — specifically someone who would never risk that trust with Seica present.
5. **Engine-driven:** persistence — following leads through dead ends over time until something real surfaces.

**Non-stat, world-state-based approaches (target 7–12, floor of 3):**
1. **Upper Earth Defector subcommunity route:** approachable by the player in a way Seica's own reputation forecloses — genuinely remorseful defectors have every reason to avoid her specifically, but not the player.
2. **Scorpio Goth community route:** her own community may hold rumors or fragments relevant to Upper Earth's legacy that nobody has ever thought to raise around her directly — too raw, too personal, too likely to detonate something.
3. **Archive of Final Confessions route:** already flagged as thematically relevant — a Scorpio institution built around confession and reckoning is a plausible place for records or testimony connected to a defector's past to surface.
4. **Libra diplomatic-records route:** formal institutional records touching Upper Earth relations plausibly route through Libra; accessible via ordinary positive standing there.
5. **Gemini/Janbogo information route:** consistent with the pattern used elsewhere in this pass (Favi, Ayako, Naizelle) — Janbogo's information networks may hold relevant data.
6. **A specific remorseful defector NPC route:** someone who genuinely wants to talk, who would never approach Seica directly given what he knows she'd do, but whom the player can find and earn the trust of independently.
7. **A legacy document/item route:** a document or object tied to the specific decision or institution turning up in unrelated salvage or discovery — no check required.
8. **Wild Child/Scorpio route:** an uncategorizable Wild Child case is exactly the kind of contradiction the Archive of Final Confessions exists to sit with, professionally and spiritually — an archivist working through the player's own irreconcilable record might cross-reference the same files that hold what the player is actually looking for. Different flavor from the bureaucratic-filing version used for Ayako/Flora/Villena/Naizelle — confessional and psychological rather than administrative.

**No faction-antagonism route** — her hatred targets Upper Earth as a whole, not a specific in-city district or faction, so the pattern doesn't map cleanly onto her; not forced.

### Themes
- Hatred with no target: what an 8w7 carries when the people responsible are structurally unreachable
- Whether rage can be a form of fidelity — keeping the fire as a way of honoring who was taken
- The limits of power: her husband was taken by something she could not fight, and she is one of the most capable people in Concordia
- What remains — spiritually, materially, in any form — of someone who is gone

### Possible Endings

- **The Name:** She creates something through her art that honors him in the specific, true way she has never been able to do publicly — not clinical grief, not a memorial in any official sense, but something that is unmistakably him and unmistakably her. It does not resolve the hatred. It gives it a form.

- **The Target:** Something connected to Upper Earth's decisions reaches into Concordia in a form she and the player can actually confront. Not innocent people — something with real culpability. The hatred finally has a direction. What she does with it, and what it costs, is the ending.

- **The Reckoning:** Through her spiritual practice — possibly through the Archive of Final Confessions, possibly through something else in Scorpio — she finds something she can live with about what happened to him. Not peace in a clean sense. A way to carry it that is not purely burning.

- **The Fire:** She decides to keep the rage deliberately. Not as self-destruction, but as fidelity — the hatred is how she keeps faith with his absence, refuses to let it become just something that happened. This is the hardest ending and the most honest for an Sx-8w7. She walks away from the quest the same as she walked in, except now she knows that is a choice.

### Specifics
TBD — broad structure confirmed. Specific triggering event, key NPCs, and branching details pending city and Scorpio development.

### Cross-Questline Notes
- The Archive of Final Confessions in Scorpio may be directly relevant — both to recruiting and to the companion quest's spiritual dimension
- Any questline touching Upper Earth's legacy in Concordia will intersect with her
- Her pistol skills make her a natural combat presence in physically dangerous questlines, despite her combat range being narrow

### Romance Quest

**Quick reference (roster row):** Recruitable companion | Nerve ≥ 7, Might ≥ 6, Humanity ≥ 6 (possibly 7 — TBD) |
Trait Gates: see character file | 8w7 Sexual.

**Stat gate:** Nerve ≥ 7 (primary), Might ≥ 6 (secondary), Humanity ≥ 6 — possibly 7, TBD (tertiary)

**Rationale:** Seica is an 8w7 Sexual type — the most intensely one-on-one focused configuration of the 8. She tests people constantly and only invests in those who hold their ground under her. Nerve is the primary gate because she needs to know the player won't fold under her intensity; anyone who flinches or appeases loses her interest immediately. Might reflects the 8's instinctive, body-forward nature — physical presence and directness matter. Humanity is higher than might be expected because Sexual 8s invest deeply in specific individuals; she needs to feel a full, emotionally genuine person across from her, not a calculating presence. Low Humanity would put her off regardless of other stats.

**Forbidden traits:** see Seica's own character file (`Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/Seica Cenilaithe/README.md`) for her specific forbidden traits and rationale — this file covers the general mechanic only, not per-character assignments.

**Signal line** (if stat threshold not met): *"You're interesting. Just — not like that. Not yet."*

**Gate 3 — Romance beats** (after companion quest completion):

Seica's romance is about challenge, testing, and the gradual revelation that she has let someone past the perimeter. The arc is not about softening her — it is about earning the interior she has been protecting.

1. **Hold your ground when she tests you:** She will push the player, probably multiple times, as genuine assessment rather than game-playing. The romantic path requires not backing down, not apologizing unnecessarily, not treating her directness as aggression to be managed. Deflection fails. Appeasement fails. Holding ground passes.

2. **The moment you call her out:** At some point she will be wrong about something, and she will know it. The player must say so directly. An 8 respects someone who can challenge them without flinching. She will not thank the player. She will not apologize graciously. But the way she looks at the player afterward is different.

3. **Show up physically:** Not necessarily through combat, but through presence — being unafraid of her in a situation where fear would be reasonable. The 8w7 Sexual notices this in a specific way nothing else replicates.

4. **The unexpected gentleness:** After all the confrontation, a moment of genuine care that isn't performed. Not sentimental; not soft for softness's sake. Just real. The 7 wing makes her capable of warmth she doesn't lead with; she recognizes it when it's honest, specifically because of everything that came before it.

5. **Her saying something true:** Not a confession exactly. A moment where she says something about herself unfiltered, then moves on quickly as if she didn't. Small. Real. Only accessible after all of the above.

**The culmination:** Direct and unambiguous — no indirection, no understated practical statement. An 8w7 Sexual who has decided doesn't hedge. She says it like she means it because she does.

---

## IT-021 [Fenny]

### Companion Quest

*(Full content of her own `Questlines/README.md`, verbatim.)*

# IT-021 "Fenny" — Questline Notes

## Recruiting Quest

Her household or bonded community no longer exists in the form she was built to serve. She may not have fully acknowledged this yet. The challenge is not asking her to leave — it is helping her recognize that she is already free.

### Possible Hooks
- **The Bond Has Ended:** The family she was bonded to is gone — dispersed, emigrated, or dead. She has been maintaining their household on habit. Help her recognize that the bond has run its course without making her feel like her service was meaningless or that the family did not matter.
- **The Overload:** She has absorbed community support responsibilities that have grown beyond her capacity — but will not ask for help because asking for help means admitting vulnerability. Address the overload without making her feel exposed. When the weight is shared, she can move.

---

## Companion Quest — "Habit Without a Home"

### Core Conflict & Emotional Stakes
A 6w5:Pr carries security through routine and preparation — but what happens when the context the routine was built for no longer exists? Fenny's arc is about the gap between who she was activated to be and who she actually is now. The routines are intact. The reason for them is gone. The question is what she is, when the defining structure of her existence is absent.

### Themes
- Grief for a structure rather than a person — mourning what organized you
- The difference between the bond that was assigned and the bonds that are chosen
- Finding out who you are when the identity you were built into is gone

### Possible Endings
- **New Bond:** She builds a new bond — chosen rather than assigned. Different in quality from what she had, and real in a way she did not expect.
- **Already Home:** She discovers that the community she helped build around her old household is her real home — it was never just the family; it was everything that grew around her service to them.
- **The Discovery:** You uncover what actually happened to the household she was bonded to. The answer has implications that reframe what she has been doing since — and possibly why she has not asked.

### Romance Quest

**Quick reference (roster row):** Recruitable companion | Humanity ≥ 7, Engine ≥ 6, Nerve ≥ 5 |
Trait Gates: TBD | 6w5 Self-Pres; quietest romance in the game; no signal line — she just doesn't warm up.

**Stat gate:** Humanity ≥ 7 (primary), Engine ≥ 6 (secondary), Nerve ≥ 5 (tertiary)

**Rationale:** Fenny is a 6w5 Self-Preservational type whose 5 wing suppresses the outward warmth typical of a Self-Pres 6, channeling it inward — into her home, into the care she takes with her private space, into a loneliness she does not broadcast. She wants to love someone and does not know how to reach toward that. Humanity at 7 (the highest in the roster) reflects that what she needs is not competence, courage, or intellect — it is genuine warmth that does not need to announce itself. Engine reflects the Self-Pres subtype's need for someone who keeps showing up rather than arriving dramatically. Nerve ≥ 5 is gentle — not a test for crisis courage, but for quiet steadiness over time.

**Signal line:** She does not deliver a signal line. She simply does not warm up. The door stays polite and closed.

**Gate 3 — Romance beats** (after companion quest completion):

The quietest romance in the game. Almost nothing is said directly. Every beat is in small actions, presence, and things noticed rather than stated.

1. **Showing up without agenda:** She is cautious of people who have obvious reasons for being around her. The romantic path is the player who comes by without needing anything, who sits with her without filling the silence with purpose. She keeps expecting the ask. It doesn't come.

2. **Noticing the second chair and not making it a thing:** The player notices and either says nothing, or says exactly one true thing — not a joke, not a probe. She remembers who noticed and how they handled it.

3. **Not trying to fix her:** The wrong path is positioning yourself as the solution to her loneliness. The right path is being present without framing it as rescue. She can feel the difference between someone who sees her pain as a problem and someone who simply sees her.

4. **Receiving the small offerings:** She begins offering things — a seat, something warm to drink, a question that needs a longer answer than one word. The player must receive these without rushing past them. Each one is a door opened slightly. Pushing further before she is ready closes it.

5. **The thing she has never said to anyone:** Not a confession of love — something smaller. A thought she has had but never articulated, said quietly while doing something else. She moves on immediately. The player who remembers it later, and shows that they do, passes something she did not know she was testing.

6. **The second chair:** The culmination does not come with a speech. She sets the table for two without being asked. The romance closes in the space between that action and what the player does next.

---

## Kendra Heinrich

### Companion Quest

*(Full content of her own `Questlines/README.md`, verbatim.)*

# Kendra Heinrich — Questline Notes

> **DLC NOTE:** Kendra is stranded at the South Pole and is the protagonist of her starring DLC. She is NOT in Concordia initially. Her recruiting arc and companion quest most likely unfold within the DLC context. The Capricorn / Reclaimed Record details represent her origin and background — where she came from, the cause she helped seed.

## Recruiting Quest (DLC — South Pole context)

She will not leave before the fight is at a survivable stopping point. An 8w7:Sc does not abandon people depending on her.

### Possible Hooks
- **The Audit Goes Forward:** Help her surface The Narrow Door findings in a way that protects her people from immediate retaliation — she needs a distribution strategy, not just the document. Once the information can travel without her, she can move.
- **The Crisis Inside the Crisis:** A specific situation within the DLC South Pole setting needs outside intervention — a key ally in danger, evidence being destroyed, something requiring your particular capabilities. Resolve it, and she can commit.
- **Prove the Trade Is Worth It:** Demonstrate that what you are doing matters as much to the people she's already fighting for as her own cause does. She will not trade her cause for yours unless yours earns it.

---

## Companion Quest — "The Number They Gave Me"

### Core Conflict & Emotional Stakes
Not the statistics of The Narrow Door — the individual people. The workers, human and robot alike, who worked harder and were moved to lower housing and told they had not earned better, and accepted it because the system said so.

Her quest involves finding those individuals, documenting their specific cases, and deciding what to do with what she finds.

### Themes
- Individual dignity vs. systemic injustice
- The personal cost of being the loudest voice in a fight that is bigger than any individual
- What justice looks like when the system that wronged people is still running

### Possible Endings
- **Public:** The Narrow Door becomes fully public — the patronage and scheduling system is formally challenged. Major Capricorn political arc.
- **Leverage:** The individual stories are used as private leverage. Quieter, more certain consequences.
- **Burn It Down:** She dismantles the merit board system. Which works. And has collateral damage she did not intend.
- **Abandonment / Hidden:** She finds a path for specific individuals without touching the system — smaller, quieter, and real. Not the victory she wanted but something she can live with.

### Cross-Questline Connection
- The Capricorn District Canon Reference notes the Recalibration Underground exists and is currently dismissed. Kendra's arc is the moment it surfaces.
- The Narrow Door of 2761 is the primary exhibit. Finding and deploying it is likely a central act in the quest.

### Romance Quest

**Quick reference (roster row):** DLC 1 companion | **None** | **None** | Unique gate system.

Kendra is the only recruitable companion in the entire game whose romance has **no MACHINE stat gate and no trait gate.** This is a deliberate exception, and the reason is specific to her character.

Stat gates work by asking: *are you the kind of person this character would find attractive?* That is the right question for most characters — attraction has a profile, and that profile maps to who the protagonist fundamentally is.

Kendra is a Type 8w7. A Type 8 does not open up because of who you are in the abstract. They open up because of what happened between you and them — a specific act, a specific moment of genuine seeing. Her romance gate is therefore not about character profile. It is about what the player did and how they showed up for her during her DLC.

**Gate 1 — You defeated what defeated her.**
The player must successfully complete the DLC's central combat challenge — the enemy or threat formidable enough to strand a war goddess. Kendra was there. She witnessed the player do something she couldn't do in her current state. For an 8, respect is the precondition for everything else. You cannot reach her interior without first earning that.

**Gate 2 — You broke through her emotional exterior.**
Kendra's armor exists specifically to prevent people from seeing inside. The DLC places her in the position she has never been in — damaged, stranded, needing help, unable to protect herself. How the player handles that throughout the DLC determines whether Gate 2 is met. This is tracked through DLC dialogue choices and how the player treats her vulnerability.

The things that break through for an 8w7 specifically:
- Not being condescending about rescuing her — not making her feel like a burden or a charity case
- Not expecting gratitude in a way that creates a debt dynamic
- Not being intimidated by her directness, even when she is being difficult about her situation
- Not treating her as less because she is damaged — respecting her as she is, not as she was
- Genuine curiosity about who she is, not just what she is capable of
- Possibly: pushing back on her when she is wrong — an 8 respects people who don't fold

**The romance mini-quest.** When both gates are cleared, a romance mini-quest opens — its own dedicated interaction sequence. Given that Kendra is a DLC companion who can continue as a main game companion after the DLC, the mini-quest may unfold partly in the South Pole setting and partly in Concordia. Specific beats are Phase 7 design work.

**Why no stat gate.** Any build can romance Kendra. A high-Might character and a high-Humanity character have equal access. What matters is not who the protagonist is at character creation — it is what they did in the South Pole and how they treated a war goddess who needed help for the first time in her life.

---

## IT-068 [Flora]

### Companion Quest

Her own `Questlines/README.md` is currently a blank placeholder template ("High-level designer notes,
branching ideas, integration with main story, etc." with no content filled in). Her actual companion-quest
content instead lives in her main `README.md`'s "Personal Questline Hook" section, reproduced verbatim below.

**Quest Title:** TBD (working title "Old Reliable," charted 2026-07-20 — broad-scope guiding direction only)

**Core conflict & emotional stakes:** her low institutional trust traces back to a past crisis where her crew was let down by a broken (non-malicious, crisis-triage-driven) promise from central management/city governance; the questline's present-day trigger rhymes with it closely enough that she can't treat it with her usual detachment

**Major themes:** competence as both strength and shield; earned trust in specific people versus institutional promises; what it costs to be the one who never needs saving

**Mechanism (retrofitted 2026-07-20 per `Companion_System.md`'s Personal Questline Design Rule):** her own public, vocal history with city governance/central management categorically bars her from getting a fair hearing on the new offer (not a skill gap — the officials already know exactly who she is). The player, with no such history, investigates in her place via 5 non-build-gated stat approaches plus 8 non-stat world-state routes (including a Libra route using the faction-antagonism pattern, and a separate Wild Child/Libra route) — see `Questlines/Personal_Questline_Summary.md`.

**Possible endings:** TBD in detail, but broad shapes charted — see `Questlines/Personal_Questline_Summary.md`

### Romance Quest

**Quick reference (roster row):** Recruitable companion | Nerve ≥ 7, Calculation ≥ 6, Engine ≥ 5 |
Trait Gates: see character file | First companion; 6w5 Thinking.

**Stat gate:** Nerve ≥ 7 (primary), Calculation ≥ 6 (secondary), Engine ≥ 5 (tertiary)

**Rationale:** Flora is a 6w5 Thinking type. Her core anxiety is whether people will hold under pressure — whether someone who seems reliable actually is. Nerve is the stat most directly about not flinching when things get hard, which is her primary question about any person she might trust. Calculation reflects the 5 wing: she respects someone who thinks through problems rather than charging in blind. Engine represents sustained reliability over time, not just crisis capability.

**Forbidden traits:** see Flora's own character file (`Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/IT-068 [Flora]/README.md`) for her specific forbidden traits and rationale — this file covers the general mechanic only, not per-character assignments.

**Signal line** (if stat threshold not met): *"You seem decent. Just — I need to know someone can hold. I don't think I've seen that in you yet."*

**Gate 3 — Romance beats** (after companion quest completion):

Flora's romance is built from accumulated small proofs rather than any single dramatic moment. She is suspicious of grand gestures and reads them as performance.

1. **The crew choice:** A situation arises — during or around her quest — where protecting her crew costs the player something meaningful (a better tactical option, time, a resource). The romantic path requires making that choice without fanfare, as the obvious right call. She notices who makes it and who doesn't.

2. **The honesty test:** Flora asks the player a direct question about their motives or intentions. Multiple answer options are available. The romantic path requires the true answer, even if it's uncomfortable. She can tell the difference between the polished answer and the real one, and she remembers.

3. **The competence moment:** Post-quest, a technical problem comes up that the player solves through genuine skill (Calculation or engineering check). Not because it's required by the scene — because they actually knew what they were doing. The 5 wing is impressed by this in a way nothing else produces. It shifts how she looks at the player.

4. **The quiet scene:** A private beat with no crisis attached — maintenance, waiting out a delay, post-crisis wind-down. She talks. The player must ask actual questions and listen. Curiosity, not compliments. She responds to genuine interest and is skeptical of flattery.

5. **The culmination, on her terms:** Flora doesn't make declarations. The romance closes the way she communicates everything else: while doing something else, not quite looking at the player, something that sounds like a practical statement until you hear what it actually is.

---

## FW-25 [Pink Lucy]

### Companion Quest

*(Full content of her own `Questlines/README.md`, verbatim.)*

# FW-25 "Pink Lucy" — Questline Notes

## Recruiting Quest

She built something in Leo that she is afraid will fall apart if she leaves. A Social 7w6 does not walk away from a community she organized around herself — she has to know it can survive her absence.

### Possible Hooks
- **The Contract Trap:** A performance contract, monopoly obligation, or guild agreement has legally locked her into Leo in a way she cannot break unilaterally. You find the legal or social exit.
- **The Warm Circuit Crisis:** Her cross-district entertainment outreach has created an emergency in an outer district — someone needs help she can only provide in person, but Leo's entertainment hierarchy is telling her to stay. Resolve the tension between her obligations.
- **The Successor:** The troupe or venue she built depends on her as its center of gravity. Help her identify the person who can hold it in her absence — prepare them, stabilize the community around them, and get her to trust the handoff.

---

## Companion Quest — "Is This Real or Is This the Act?"

### Core Conflict & Emotional Stakes
Leo's central unanswered question is whether performing joy and actually having it have become confused over two centuries of doing both simultaneously. FW-25 is the living version of that question.

Her arc involves a crisis that her positivity cannot reframe — something that actually hurts and needs to hurt before it can heal. The 7's response to pain is to move, plan, reframe. Her companion quest is about what happens when none of those work.

**Inciting hook (established 2026-07-20, deliberately present-tense rather than another "someone from the past" plot):** anchored in her established Warm Circuit role. A specific outer district her cooperative serves (Cancer suggested as a strong thematic fit, given its own established grief/care identity and documented weakness at caring for its own burned-out caregivers — not locked) is going through real, serious war-legacy hardship, and Warm Circuit's morale programming isn't just failing to help, it's actively making things worse: people feel dismissed and unheard underneath the enforced cheerfulness. Pink Lucy hasn't seen this, because her whole identity is built around not being able to see it.

**Categorical block (per `Companion_System.md`'s Personal Questline Design Rule) — a new flavor, perceptual rather than architectural, professional, or reputational:** Pink Lucy cannot personally investigate this community's real pain, because her own established role — the constant, professional bringer of good energy — means anyone she talks to receives her through that lens no matter how sincerely she shows up. They perform gratitude and positivity back at her, the exact trap she's caught in herself; she simply cannot get an honest read on suffering that her own presence reflexively smooths over. Leaving Leo for an extended personal investigation also risks the Warm Circuit operations that depend on her constant presence (per the "Successor" hook above — the cooperative needs her as its center of gravity). The player, without her institutional reputation, can actually sit with real grief and hear the truth without it being performed back. **This is a structural exclusion, not avoidance dressed up as one** — though it's also true the arrangement is convenient for her, since it means she never has to test whether she could actually handle what she'd find.

**5 stat-based approaches (non-build-gated, deterministic):**
1. **Investigation-driven:** piece together the real situation from physical and environmental evidence, not just what people volunteer.
2. **Calculation-driven:** recognize the pattern of a community's actual distress signals underneath performed gratitude — resource use, timing, what doesn't add up.
3. **Nerve-driven:** directly and bluntly ask the hard question nobody else has been willing to ask.
4. **Humanity-driven:** earn genuine trust, sit with people's real grief long enough that they stop performing for the outsider too.
5. **Engine-driven:** sheer persistence — returning enough times that the performed veneer eventually wears through.

**8 non-stat, world-state-based approaches (target 7–12, floor of 3):**
1. **Warm Circuit route:** other members of her own cooperative — not her — may have separately noticed something's wrong, reachable through independent player standing there.
2. **The affected district's own community route:** local standing in whichever district this ends up being.
3. **Scorpio route:** the psychological/transformative district's therapeutic community would recognize the signature of unprocessed grief being papered over, and could offer real insight to relay.
4. **Other Leo performers route:** fellow entertainers who've separately felt the same performing-joy-vs-having-it tension Leo is already built around.
5. **Libra route:** a resource-allocation angle — if the district's real needs are being under-resourced while morale programming continues instead, a Libra contact could surface the actual gap.
6. **A specific affected-community NPC route:** someone who's tried to get real help and been repeatedly waved off with morale programming, willing to tell an outsider the truth.
7. **A legacy item/evidence route:** physical evidence of neglect or unaddressed hardship, discoverable independent of anyone telling the player — no check required.
8. **Wild Child route (new, seventh flavor — "authenticity recognition," per `Companion_System.md`):** a community fluent in performing feelings it doesn't fully have would also be unusually good at spotting performance — and a Wild Child player's messy, contradictory, unmanufacturable reputation reads as evidence of realness precisely because it's too inconsistent to be a PR image. Their own practiced eye for insincerity earns the player unusual trust, not an institution processing a paradox.

**No faction-antagonism route** — nothing establishes Warm Circuit or Pink Lucy as being on bad terms with a specific district; not forced.

**Placement dependency flagged 2026-07-20:** this design assumes the main-game path (Leo, Concordia-based). Her file's still-open "main game vs. Janbogo DLC" question would require revisiting the district geography here if she ends up placed in the DLC instead, though the core mechanism should survive the move.

### Themes
- The cost of being the person everyone counts on for good energy
- Whether joy that was performed for long enough eventually becomes real — or remains performance no matter how sincere it feels
- What the 7 discovers on the other side of pain, if they finally stop moving long enough to feel it

### Possible Endings
- **Real:** Her joy is tested and emerges as genuine — not naive, but earned. The grief was real and she held it and the joy did not disappear.
- **Both True:** It was always partly performance. And that turns out to be okay — because the performance became something that sustained real people, and that is its own kind of reality.
- **New Form:** She finds that holding grief and joy together is its own art form — something Leo's entertainment culture never taught her. She builds something new that reflects both.

### Romance Quest

**Quick reference (roster row):** Recruitable companion | Humanity ≥ 7, Engine ≥ 6, Nerve ≥ 5 |
Trait Gates: TBD | 7w6 Social; communal intimacy; romance unfolds through The Warm Circuit.

**Stat gate:** Humanity ≥ 7 (primary), Engine ≥ 6 (secondary), Nerve ≥ 5 (tertiary)

**Rationale:** Pink Lucy is a 7w6 Social type — her entire vocation is built around collective morale, belonging, and bringing genuine warmth into post-war Concordia through The Warm Circuit. A Social 7 reads through performed care immediately; the Humanity threshold is slightly higher than the other 7 in the roster (Villena, ≥ 6) because warmth is not just a preference for Pink Lucy — it is the whole substance of her work. Engine serves the 6 wing: beneath the restless enthusiasm is a need for someone who stays, who doesn't burn bright and disappear. Post-war Concordia has already taken enough from her; reliability matters more than grand gestures. Nerve ≥ 5 is the minimum bar for matching her energy — a very low-Nerve player would feel like dead weight to someone whose life runs on momentum and yes.

**Signal line** (if stat threshold not met): *"You're good people. I just need someone around who actually loves people back. The work requires it."*

**Gate 3 — Romance beats** (after companion quest completion):

The romance unfolds in the context of The Warm Circuit — her entertainment cooperative and the living expression of what she has built. A Social 7 finds intimacy through shared experience in the world, not in isolation.

1. **The invitation:** She invites the player to participate in a Warm Circuit community event — not as an audience member but as a participant. This is how she includes people; she doesn't let them watch. The player shows up and engages genuinely.

2. **The unguarded moment:** During or after an event, the player catches her in a private moment of doubt. She is holding morale infrastructure together in a post-war city that lost everything. The 6 wing's fear surfaces when she thinks no one is watching: what if it falls apart? What if it isn't enough? The optimism is real — and so is what it costs to maintain.

3. **The player stays:** Rather than encouraging her or trying to fix the problem, the player stays present in that moment without resolving it. No cheer. No solution. A Social 7 with a 6 wing who feels genuinely held — not managed, not performed at — for the first time. This is the pivot.

4. **The follow-through:** The player shows up again. The next event. The next ask. Nothing dramatic — consistent. The 6 wing registers this one way: *you came back.* That is the thing.

5. **The opening:** She tells the player what she's decided. A 7 doesn't torture herself with ambiguity once she's reached a conclusion; she names it directly. Warm, a little nervous in a way she doesn't usually allow herself to be.

---

## Majyao Bisyugota

### Companion Quest

Majyao is confirmed permanently non-recruitable — there is no companion quest in the ordinary sense. Per
`Companion_System.md`, Gate 1 (the questline prerequisite) is instead satisfied through her own established
narrative/faction content plus repeated teahouse visits and questline depth. Her own `Questlines/README.md`
content (titled "Story & Faction Notes," not "Companion Quest") is the closest equivalent and is reproduced
verbatim below.

*(Full content of her own `Questlines/README.md`, verbatim.)*

# Majyao Bisyugota — Story & Faction Notes

*Majyao is not recruitable. These are narrative/faction design notes.*

## District Role — Taurus

A Self-Preservational 4w5 who has externalized her interior world into a physical space — the teahouse is not just her business, it is her curated expression of self made walkable. Every element is deliberate: the atmosphere, the selection, the specific way things are arranged. The warmth of it is real, not performed, but it is also deeply intentional.

She runs the teahouse as a sanctuary for the tired, the weary, the overworked, and the overstressed — a place where people can come in, have a cup of tea, and forget for a few hours that life in post-war Antarctica is brutal. She loves her patrons and interacts with them directly; she is not a distant curator. But the space around her is always hers in some essential way, and people feel it when they are in it.

She sources teas from across Antarctica — a point of pride and of philosophical seriousness. Her signature specialty was **Blood River Tea**, grown in soil nourished by the iron-rich waters of Blood Falls in Taylor Valley. The Long Night War cut off that supply line. She can no longer serve it. The gap on the menu is real.

Her personal character music is Fusion Jazz — a hybrid of Scandinavian Avant-Garde Jazz and Chinese Traditional Folk. This reflects her character precisely: sophisticated and experimental in structure, rooted and organic in feeling, bridging traditions without belonging fully to any one of them.

## Faction / Collective Affinity

She is not a political creature and does not belong to any faction. Her teahouse functions as part of Taurus's community infrastructure — one of the places people go — without her organizing it that way deliberately. She is adjacent to The Steady Watch and The House Network in spirit (both Taurus community care structures) but is independent of both.

She is the kind of person factions want to meet in, because her teahouse is neutral ground. Whether she extends that neutrality consciously or simply because she loves everyone who walks through the door is a useful ambiguity.

## Narrative Hooks for Player Interaction

- She knows everyone who comes to her teahouse. People from multiple districts, multiple walks of life, on their worst days and their most private evenings. She has not been collecting this information, but she has it. A conversation with her, properly approached, is a remarkably useful thing.
- **Blood River Tea** is a potential quest thread: the supply line from Taylor Valley has been cut since the Long Night War. If the player ever opens a route to the McMurdo Dry Valleys — through Sagittarius expeditions, through a Frostlands questline — she would want to know. Bringing her the first shipment since the war would be significant to her in a way that is difficult to articulate but entirely genuine.
- She is one of the few places in Taurus where a player can sit down, be treated warmly regardless of reputation, and hear the honest texture of what the district is going through — not gossip, but the emotional ground-level reality of how people are doing.
- She does not give information as a transaction. She gives it the way she gives tea — because she wants people to be okay.

### Romance Quest

**Quick reference (roster row):** Non-recruitable NPC | Humanity ≥ 7, Investigation ≥ 6, Calculation ≥ 6 |
Trait Gates: see character file | 4w5 Self-Pres; teahouse keeper; romance through repeated visits and
questline depth; Blood River Tea thread.

Majyao does not join the player's party. The romance arc runs through her teahouse — repeated visits, escalating depth, the relationship built through her questline and the time the player chooses to spend in her space.

The gate system applies identically: Gate 1 (questline/relationship prerequisite), Gate 2 (stat threshold). There is no companion quest; her questline content and repeated visits serve the Gate 1 function.

**Stat gate:** Humanity ≥ 7 (primary), Investigation ≥ 6 (secondary), Calculation ≥ 6 (tertiary)

**Rationale:** Majyao is a 4w5 Self-Preservational type. A SP 4's deepest need is genuine depth — to be truly seen rather than charmed. She extends warmth to every patron; she will only open to someone who has real emotional interior. Humanity at 7 (tied with Fenny for the highest in the roster) reflects that the bar is not competence, courage, or intellect — it is the capacity for genuine feeling and presence. Investigation reflects the 5 wing: she is drawn to people who notice things. Her teahouse is full of deliberate, specific details; the patron who asks about them, who clocks the gap where Blood River Tea used to be, who pays careful attention to what is actually there — that patron gets somewhere. Calculation reflects the intellectual depth the 5 wing craves; she is Feeling-centered, not primarily intellectual, but she needs a mind that can go somewhere.

**Forbidden traits:** see Majyao's own character file (`Worldspace/Characters/Dolls/Still-Present_-_In-Game/non-recruitable/Majyao Bisyugota/README.md`) for her forbidden traits and rationale (currently in progress, not yet finalized) — this file covers the general mechanic only, not per-character assignments.

**Signal line** (if stat threshold not met): *"I like that you come here. It means something. But I think what you're looking for is different from what I'm able to give."*

**Gate 3 — Romance beats:**

The quietest, most internally textured romance in the game alongside Fenny. She will not reach toward the player; she responds to the player reaching toward her. She is noticed first, then more deeply, then actually seen.

1. **The first real conversation:** Most patrons get warmth and a good cup of tea. This is the first conversation that goes somewhere unexpected — the player asks a specific question about a tea, a detail of the teahouse, something particular. She pauses. She answers at length. She didn't expect someone to actually ask.

2. **The return:** The player comes back. Multiple times. She begins to extend particular attentions — she knows their order before they give it, she brings something unexpected. She says nothing about it.

3. **The depth moment:** A conversation that breaks through the surface, tied to her questline. Janbogo. The war. What it means to have rebuilt something from nothing in the only city left. She says something she hasn't said to anyone else. The player doesn't try to fix it. They listen.

4. **The Blood River Tea moment** *(optional — expand during questline design)*: If the player has followed the Blood River Tea thread — the supply line from Taylor Valley that the Long Night War cut, which she can no longer serve — and can bring her news of it, or in the best case a sample, something opens in her response that nothing else produces. This is the clearest possible signal that someone was paying attention to what actually matters to her, not just to her. Specific mechanics and what this unlocks are to be expanded when the Blood River Tea questline thread is developed in coordination with Frostlands/Taylor Valley design.

5. **The silence:** The teahouse is empty after closing. The aurora through the floor-to-ceiling windows. Both of them simply present, not needing it to be anything else. A 4w5 SP's romance begins in the quiet, not in a speech.

---

## Trisha Miller

### Companion Quest

Trisha is confirmed permanently non-recruitable — there is no companion quest in the ordinary sense. Per
`Companion_System.md`, Gate 1 (the questline prerequisite) is instead satisfied through repeated off-air
encounters and her own questline content. Her own `Questlines/README.md` content (titled "Story & Faction
Notes," not "Companion Quest") is the closest equivalent and is reproduced verbatim below.

*(Full content of her own `Questlines/README.md`, verbatim.)*

# Trisha Miller — Story & Faction Notes

*Trisha is not recruitable. These are narrative/faction design notes.*

## District Role — Taurus

A Social 8w7 who has embedded herself in Taurus's residential community so completely that she is no longer just a broadcaster — she is a neighborhood institution. She holds no official district authority. She holds something harder to quantify: she is the person her community actually listens to.

Her show runs a hybrid music/talk format with regular call-in segments. It evolved from the morning/evening commute music program she hosted in Midwestland before the Falkland Treaty forced her out. In Concordia, it became something with more voice — hers, and her listeners'. Occasional community bulletins air when something genuinely needs saying; rare enough that when she breaks format, people pay attention.

She has been broadcasting in Concordia since after the Long Night War. Her two human friends who followed her into Antarctic exile are long dead. She outlived them by decades. She does not discuss this on air.

## Personality Notes

Silver-tongued and smooth, with fists as a backup plan when words have failed. She keeps no emotional distance from the people who love her — she lives among them, is known by them, knows them by name. Highly opinionated, especially about Upper Earth governments and what the Falkland Treaty did, but not political in nature. She speaks as a person with feelings and memory, not a commentator with positions. People hear her and feel like they are hearing someone honest, which is rarer than any ideology.

Her community in Taurus is not an audience. It is her people.

## Faction / Collective Affinity

Her show is its own institution. She is not formally affiliated with any faction — she is the kind of voice that factions want to court and cannot fully claim, because she does not belong to a movement. She belongs to her neighborhood.

She overlaps in spirit with The Steady Watch and The House Network (both Taurus community infrastructure) but is independent of both.

## Narrative Hooks for Player Interaction

- She has an opinion about everything happening in Concordia, expressed plainly and without diplomatic softening. The player can learn what Taurus actually thinks — not what leadership says, not what Libra wants heard — by talking to her or listening to her show.
- Her call-in segments are a live wire into community sentiment across Taurus and potentially beyond. If the player needs to know what a certain part of the population believes or fears, she is a direct line to that.
- She does not approve of people who use her community as a means to an end. If the player's actions have affected Taurus residents negatively, she will know about it — and she will say so on air, or directly to the player's face.
- She is a Social 8w7 who has been alive long enough to remember the Falkland Treaty, the Long Night War, and everything in between. She carries long-duration memory of Concordia's political and community history from a ground-level perspective. What she knows and what official records say may not be the same thing.

**NPC Schedule (In-Game Clock)**, from her own main `README.md`:

Trisha's activity is tied to the in-game clock. She operates on a daily cycle.

**Broadcast hours (majority of the day):**
At The Signal, running her show live — music, talking, opinions, listener call-ins. Accessible at the station, but her primary mode is the show itself.

**Off-air windows (two daily intervals):**
- **Very early morning (~6 in-game hours):** Station runs auto-play (pre-queued music, no live host). Trisha is out in Taurus, in public, socializing with people. Low-population window — quieter encounters, more one-on-one texture.
- **Late afternoon (~4 in-game hours):** Same — auto-play on, Trisha out in the world. Higher foot traffic; different ambient context.

During off-air windows the player can find and speak to her in Taurus. This is the primary way the player meets and gets to know her organically. She is not hiding or off-duty in any guarded sense — this is just what she does. The populist character doesn't perform accessibility; she is simply out among people because that is who she is.

**Post-questline:** Her broadcast content reflects how events resolved. She talks about the player on air — what happened, how she reads it. Players who helped her, betrayed her, or navigated something in between each get a broadcast that reflects the specific reality of what occurred.

### Romance Quest

**Quick reference (roster row):** Non-recruitable NPC | Nerve ≥ 7, Humanity ≥ 7, Might ≥ 7 |
Trait Gates: see character file | 8w7 Social; radio host; romance through recurring off-air encounters.

**Confirmed romanceable 2026-07-28.** Trisha does not join the player's party. The romance arc runs through
her off-air windows in Taurus (`NPC Schedule (In-Game Clock)` in her own character file) — recurring
in-person encounters while she's out among her community, rather than a companion questline structure.

The gate system applies identically: Gate 1 (relationship prerequisite, built through repeated off-air
encounters and her own questline content), Gate 2 (stat threshold). There is no companion quest; the
recurring encounters serve the Gate 1 function, the same way Majyao's repeated teahouse visits do.

**Stat gate:** Nerve ≥ 7, Humanity ≥ 7, Might ≥ 7 — **all three set equal, no primary/secondary/tertiary
ordering**, confirmed 2026-07-28.

**Rationale:** Trisha is an 8w7 Social type. An 8 has zero tolerance for half-measures in any single
dimension — she doesn't rank which quality matters most because she's watching for total, non-negotiable
substance across the board, not competence in one area propped up by weakness elsewhere. Nerve reflects her
own directness and conviction — she speaks her opinions plainly and expects the same boldness back, not
evasiveness. Humanity reflects that she "puts no emotional distance between herself and the people who love
her" — she needs someone equally willing to close distance, not hold back. Might reflects the physical half
of "uses her fists as a backup plan when words have failed": real presence backing up the boldness, not just
talk. The backstory detail that two friends chose to follow her into forced exile, and that she outlived them
by decades, means she knows exactly what it costs for someone to choose her — she isn't interested in anyone
who wouldn't measure up to that standard in every direction at once.

**Forbidden traits:** see Trisha's own character file (`Worldspace/Characters/Dolls/Still-Present_-_In-Game/non-recruitable/Trisha Miller/README.md`) for her specific forbidden traits and rationale — this file covers the general mechanic only, not per-character assignments.

**Signal line** (if stat threshold not met): *"Honey, I like a lot of people. That's not the same thing as
what you're after, and I think you know it."*

**Gate 3 — Romance beats:**

Trisha's romance happens in the ordinary texture of her off-air life — she is never hiding, never guarded,
so the test isn't about getting past a wall. It's about whether the player is actually *there*, consistently,
in the unglamorous stretches where nobody's listening to a broadcast.

1. **Show up during an off-air window, more than once, without an agenda:** Most people only seek her out
   when the show is live. The romantic path finds her during the quiet stretches — early morning or late
   afternoon, out in Taurus — and keeps doing it, not as strategy, just as genuine interest in her outside the
   microphone.

2. **Say the direct thing:** At some point a comfortable, evasive answer is available. The romantic path
   says the true thing instead, even if it's blunter than comfortable. An 8 respects directness even when it
   isn't flattering; softness that reads as avoidance loses ground here, not gains it.

3. **Stand somewhere with her:** A moment arises — a dispute, a disagreement, something in Taurus that
   matters to her — where the easy choice is to stay neutral. The romantic path picks a side, hers, openly,
   in public. She isn't looking for a bodyguard; she's looking for someone who doesn't flinch from being
   associated with her convictions.

4. **The choosing:** Given what her own history taught her about what it costs someone to choose her
   deliberately, the culmination isn't a grand declaration — it's her naming, plainly, on-air or off, that
   this is a choice she's making with her eyes open, the same way it was once made for her.

**Romance Reward — The Broadcast, confirmed 2026-07-28, corrected the same day:** as a populist radio DJ with
a real "woman of the people" reach, once the player has fully romanced Trisha, she speaks well of them on-air
— the same world-state-feedback mechanic her regular post-questline broadcasts already use (see "Trisha
Miller — Radio Host," `Companion_System.md`), but now carrying real mechanical weight, citywide.

**Effect:** not a one-time flat percentage — a **permanent rate modifier**, applied independently to each
district-based faction's own Positive and Negative Reputation tracks: **Positive Reputation accrues 5% faster,
and Negative Reputation accrues 5% slower**, per district, from the moment the romance perk is granted onward
(the progressive half). **Critically, this modified rate is also applied retroactively** — the player's
already-accumulated standing in every district is recalculated as though the modifier had been in effect the
entire time, not just from this point forward. Her platform reaches the whole city, so the effect is
citywide by nature, not scoped to Taurus or wherever the player happens to be standing when the romance
completes.

---

## Ayako Hayashi

### Companion Quest

Her own `Questlines/README.md` is currently a blank placeholder template. Her actual companion-quest content
lives in her main `README.md`'s "Personal Questline Hook" section, reproduced verbatim below (including the
Long-Vigil-only pathline note that immediately follows it in her file).

**Quest Title:** TBD (working title "The Unfinished Garment")

**Core conflict & emotional stakes:** Broad-scope direction charted 2026-07-20 — grief transmuted entirely into vocation vs. grief actually faced; someone finally being present for her the way nobody was present for the man she couldn't save.

**Major themes:** Precision as gift and shield; what it means to finish (or honestly leave unfinished) something made in loss.

**Mechanism (retrofitted 2026-07-20 per `Companion_System.md`'s Personal Questline Design Rule):** a current Red Spiral case echoes the shape of the original accident; Red Spiral's own conflict-of-interest protocol categorically bars Ayako from investigating it herself (not just emotional reluctance — a structural exclusion tied to the faction's neutrality). The player investigates in her place via 5 non-build-gated stat approaches plus 8 non-stat world-state routes, including a Wild Child/Cancer route — see `Questlines/Personal_Questline_Summary.md`.

**Possible endings:** Not yet designed — likely no single "good" resolution to the grief itself, more a question of how she integrates it.

Full broad-scope direction in `Questlines/Personal_Questline_Summary.md`. Full step-by-step design deliberately deferred until Concordia/Cancer district is developed enough to root it in real places.

**Long-Vigil-only pathline — made official 2026-07-23: "The Second Garment."** Per `Fragmentation_Matrix.md`'s
companion calibration, Ayako carries a high Personality Grief-Multiplier — her SP4w5 wound (present, unable
to save someone she loved) maps directly onto what it means to watch a bonded player disappear into a
re-spec. Reaching **The Long Vigil** (Grief Range 3 + Bond Range 3 simultaneously) with her unlocks a second,
unexplained garment in her atelier — made privately, unprompted, in the likeness of who the player used to
be — paralleling the already-established garment she keeps for the man she lost. Full structure, the
three-beat design, and the branching (non-"good"-ending) resolutions are written up in
`Questlines/Personal_Questline_Summary.md`'s own "Long-Vigil-Only Pathline" section. Exact dialogue and
in-scene staging remain deferred until Cancer district's own development catches up, same as the rest of her
questline.

### Romance Quest

**Quick reference (roster row):** Recruitable companion | Investigation ≥ 7, Humanity ≥ 7, Calculation ≥ 6 |
Trait Gates: see character file | 4w5 Self-Pres; Red Spiral medic; highest Investigation gate in the roster.

**Stat gate:** Investigation ≥ 7 (primary), Humanity ≥ 7 (secondary) *(raised from ≥6, 2026-07-20)*, Calculation ≥ 6 (tertiary)

**Rationale:** Ayako is a 4w5 Self-Preservational type — her entire practice, medicine and fashion both, runs on precise observation. She notices everything and always has. The entry point to her is someone who operates in the same register of careful attention; she recognizes it immediately and it is the only thing that genuinely interests her in a person. Investigation ≥ 7 is the highest gate of that stat in the roster, which fits: no one in the game is more attuned to what is actually there. This deliberately inverts Majyao's profile (also 4w5 SP, Humanity ≥7 as well but *primary* rather than secondary there) — Ayako is more internally focused and more filtered through precision than warmth first, even though her Humanity floor now matches Majyao's and Fenny's as the highest in the roster. Humanity is secondary, not primary, because a 4's core wound is feeling unseen; genuine emotional depth must be present alongside the perceptive intelligence, not substituted for it, and it has to clear a real bar — she has loved a human before, deeply, and the emotional register has to be real, not merely adequate. Calculation reflects the 5 wing: she respects careful thinking and someone who can go somewhere with a difficult idea.

**Forbidden traits:** see Ayako's own character file (`Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/Ayako Hayashi/README.md`) for her specific forbidden traits and rationale — this file covers the general mechanic only, not per-character assignments.

**Signal line** (if stat threshold not met): *"You're good at what you do. I've noticed that. I just need more than competence before I can let someone in."*

**Gate 3 — Romance beats** (after companion quest completion):

1. **The atelier visit:** After the companion quest resolves, she invites the player to her home — a practical reason, not an obviously romantic one. The player sees the space for the first time. What they notice, or ask about, in the atelier tells her something she doesn't say out loud yet.

2. **The kept garment:** The player can ask about the single garment on the hook near the window. She answers in one sentence — something at the intersection of grief and craft; made for him, or made in the period after losing him. She moves on immediately. The player who remembers it later, and shows that they do, passes something she wasn't consciously setting as a test. **Cross-reference, per the Long Vigil/Romance cross-awareness rule:** if the player has also triggered her Long-Vigil-only pathline ("The Second Garment," see her own `Questlines/Personal_Questline_Summary.md`) and a second garment now hangs alongside the first, this beat should acknowledge both are there rather than only ever referencing the original — she's aware there are now two, even if she still doesn't volunteer everything about either.

3. **The mementos:** The player can ask about the arrangement in the living area. She names him. Says something brief and true about who he was. Does not perform the grief. A player who receives this without trying to fix it or position themselves as a replacement gets through something important.

4. **The Schopenhauer question:** She asks what the player thinks about aesthetic contemplation as the only real relief from suffering. Genuine curiosity, not a test. The wrong answer is deflection or a joke. The right answer is honest engagement — including honest disagreement, which she respects more than easy agreement.

5. **The fashion reveal:** She shows the player something personal she is working on — not a Red Spiral commission, not a client piece. She explains what she is trying to do with it. The 4's interior richness becomes fully visible when she talks about what she is making; she almost forgets to be composed. This is the most unguarded the player will have seen her.

6. **The opening:** In the middle of doing something else, she says something specific and true about the player that she has been observing for a long time. It could only come from someone who has been paying very close attention. That is how a SP 4w5 says it.

---

## Lyuba Baranova

### Companion Quest

Her own `Questlines/README.md` is currently a blank placeholder template, and her main `README.md`'s
"Personal Questline Hook" section is entirely TBD placeholders ("Quest Title: TBD," "Core conflict &
emotional stakes: TBD," etc., with only a general, undeveloped thematic hint). **Not yet written** — no
companion-quest narrative content exists for her as of this writing.

The one piece of genuine guidance on record, from her main README.md's "Personal Questline Hook" section:

- Quest Title: TBD
- Core conflict & emotional stakes: TBD
- Major themes: TBD — likely involves the specific Sexual 8 tension between needing genuine connection and the testing behavior that keeps people at arm's length; possibly explores what it means to protect something when you built your identity around never needing protection yourself
- Possible endings (Good / Neutral / Bad / Secret / Abandonment): TBD

### Romance Quest

**Quick reference (roster row):** Recruitable companion | Nerve ≥ 8, Humanity ≥ 7, Engine ≥ 6 |
Trait Gates: TBD | 8w7 Sexual; silver-tongue / unarmed fighter; Aries; highest Nerve gate in the roster.

**Stat gate:** Nerve ≥ 8 (primary), Humanity ≥ 7 (secondary), Engine ≥ 6 (tertiary)

**Rationale:** Lyuba is an 8w7 Sexual type whose primary instrument is language — not confrontation, not physicality, but the word used precisely and well. This makes her, paradoxically, the hardest type to perform for: she invented every version of verbal charm you might try to deploy, and she can see the machinery inside it from several rooms away. The Nerve threshold is the highest in the entire roster (≥ 8) for this specific reason — the challenge is not holding ground when she confronts you directly, but holding ground under the quieter pressure of being read by someone this perceptive. The player who tries to match her wit fails. The player who performs genuine interest fails. The player who is simply and actually themselves, even while she takes them apart quietly, passes. Humanity ≥ 7 reflects the Sexual 8's deep investment in the specific individual: she will not open to someone who is warm in the abstract but lacks genuine interior feeling. She can tell the difference, and the difference matters more to her than almost anything else. Engine ≥ 6 matches her energy — the 7 wing keeps her fast and full; a sluggish person will not keep up with her over time.

Note on differentiation from Seica Cenilaithe (also 8w7 Sexual): Seica's romance is built on physical confrontation, held ground, and the slow revelation of interior after the perimeter is earned through nerve. Lyuba's romance is built on verbal authenticity, the discovery that the player cannot be reduced to technique, and the quiet weight of access given through what she chooses to share. Both are 8w7 Sexual; neither resembles the other in form.

**Signal line** (if stat threshold not met): *"You break too easy."*

**Gate 3 — Romance beats** (after companion quest completion):

Lyuba's romance is the arc of the player becoming the one person she cannot read, and what she does when she finds that.

1. **The verbal test:** She says something designed to create small social pressure — not hostile, just diagnostic. It is the opening move she makes with anyone she finds interesting; she is watching how the player navigates it. The wrong responses: too clever (performing), too defensive (flinching), evasive (not present). The player who answers simply, honestly, and without making a project of it passes. She does not announce that anything has happened. The way she looks at them afterward is different.

2. **She gives something real, unprompted:** At some point she tells the player something true that she didn't have to share — not a secret exactly, just something specific and real about herself or what she thinks. She is watching whether the player receives it or does something with it: files it, uses it, turns it into a compliment, reflects it back in the form of a reassurance. The player who simply receives it — who is just present with it for a moment before the conversation moves on — passes something she did not announce she was testing.

3. **The night she goes quiet:** There is a point in the arc — tied to her companion quest — where she withdraws. Not hostile, not cold exactly; just gone to wherever she goes when something is heavy. She disintegrates toward 5 under real stress: she stops sharing, stops being present in the usual way, guards information she would normally give freely. The player who notices and gives her space — who checks in once, without demanding access, then waits — passes something she notices afterward. The player who presses fails. The player who takes the distance personally and disappears fails.

4. **The culmination:** She says it plainly, in the way an 8 who has decided says things — directly, without hedging, without performed vulnerability. But the form is hers: words, precise and unadorned, carrying exactly the weight she intends. The 7 wing means there is warmth inside it she is no longer working to conceal. She says what she means. That is the whole of it.

**Post-romance mini-questline beats** (fire after the romance is established and the player has home access):

- **The literature wall:** The player can ask about her collection. She will talk about a specific work — one she returns to, what it gets right about something, why it stays. The player who responds with an actual position — agreement, pushback, a real question that shows they have been tracking what she said — gets somewhere. The player who admires the collection and moves on gets warmth but not access. This is not a test. It is simply how she opens: through the things she thinks about. *(Requires home access — reserved for post-romance content.)*

- **The paper books:** She shows the player one of the paper books — not the collection, one specific one — and says briefly what makes it the one she chose. The books are private in a way the datashards are not. She is allowing the player access to something she does not show routinely. The right response is not the perfect reaction. It is a real one. She is watching for presence, not performance. *(Requires home access — reserved for post-romance content.)*

---

## TBN [TCY-42 ravishing extravagant Lillian]

*(Copied verbatim from her own `Questlines/README.md` — the precedent file this Directory's pattern is
modeled on. Contains both her Companion Quest and Romance Quest content together, as originally written.)*

# TCY-42 "Lillian" — Questline Notes

> Recruitability TBD. Notes written for [?] status.

## District Role & Faction Context

A 7w8:Sc performer in Leo affiliated with the **legacy intimate-tradition house** — the structurally disadvantaged side of Leo's grand/intimate performance divide (currently labeled "The Star War," a name flagged for replacement — see `District_Canon_Reference.md`). **Corrected 2026-08-11:** there was no civil war and no side that lost a fight — her house's disadvantage traces to a founding-era construction accident (the Twin Founding) and an uncalibrated resource formula that favored the rival house for 250 years, compounded further by an unrelated Long Night War death (2812) that handed the rival house a fresh, ambitious new leader. She is still present in Leo, still trying to reclaim prestige through art, competing against an establishment that controls access to the best venues and highest recognition tiers — earned resentment, not a grudge from a lost war.

Together with TCY-06 "Elva" (the grand-tradition house), Lillian and Elva represent the two sides of Leo's ongoing political-aesthetic divide.

## Recruiting Quest (if decided)

A 7w8 will not be recruited unless what you offer is bigger than what she is currently chasing. In Leo, that means:
- Offering her a stage or opportunity that makes her current ambitions look small — something the established house cannot give her and cannot prevent
- Revealing that the establishment she is competing against is rigged in a way that means she can never win on those terms — which reframes the whole game she has been playing

---

## Companion Quest (if decided)

### Core Conflict & Emotional Stakes
The 7w8's shadow is the cost of ambition — something she ran over on the way to where she is. Her companion arc involves encountering that cost and deciding whether to turn back or keep going.

Leo's "no audience/performer distinction" means she has never had to be honest with herself. The quest is about finding that audience — someone who sees through the extravagance to what is underneath it.

### Themes
- What the 7w8 has been moving too fast to feel
- Whether the climb was worth what it cost, and who got to decide that
- Leo's central question: performing yourself vs. being yourself — she has been performing so long she may not know the difference

### Possible Endings
- **Reckoning:** She confronts what she ran over and makes a choice about it. Not necessarily redemption — just honesty.
- **Reframe:** What she thought was the cost turns out to be something else entirely, and the companion quest ends with her understanding herself differently.
- **The Win That Changes Nothing:** She reaches the top of Leo's hierarchy and discovers it does not feel like what she thought it would. The quest is about what comes after.

---

## Romance Quest — Confirmed 2026-08-11

**Quick reference (roster row):** Recruitability undecided; confirmed romanceable 2026-08-11 |
Investigation ≥ 7, Humanity ≥ 6, Nerve ≥ 5 | Demagogue | 7w8 Social-Countertype; Leo, intimate-tradition
house; first companion with a Courtship Sequence beat built under the Romance Beat Checks law.

**Confirmed romanceable.** Recruitability as an active companion is still undecided; Romance status does not
depend on that question being resolved, or resolved any particular way — established precedent: Majyao
Bisyugota and Trisha Miller, both confirmed *permanently non-recruitable* and both fully romanceable
regardless. Built via the Character Creation Methodology's Companion-vs-Romance Scoping
(`TepenianUniverseTimeline/Worldspace/Characters/Character_Creation_Methodology/Design_Principles/Companion_vs_Romance_Scoping.md`),
drawing on her already-confirmed Stage 3 core cluster (see her canonical profile) rather than inventing fresh
psychology. General mechanics referenced below (the Romance Beat Checks law, Buffable-Stat-Check Law, Minimum
Five Solutions law, District reputation tiers) are defined once, broad-scope, in
`Game-Mechanics/Core-Mechanics/Companion_System.md` and `Character-Creation/Skills.md` — not restated here,
only applied.

**Stat gate:** Investigation ≥ 7 (primary), Humanity ≥ 6 (secondary), Nerve ≥ 5 (tertiary)

**Rationale:** Lillian is a 7w8 Social-Countertype — her outward life is a performance of selfless devotion to
her house's artistic legacy, concealing (even from herself) a personal hunger for recognition of that
sacrifice. Her own established visual read already names what she needs: "someone who sees through the
extravagance to what is underneath it." Investigation is primary for exactly that reason — genuine
perceptiveness, not flattery. Humanity is secondary: a Seven's Shadow is discomfort-avoidance, so she needs
someone who can sit with a difficult moment alongside her without flinching or rushing to fix it, not merely
someone observant. Nerve, at a comparatively low tertiary threshold, reflects a smaller but real requirement —
a partner who will eventually be willing to gently name what she won't say herself, directness without
cruelty.

**Forbidden trait: Demagogue.** Her entire arc is about learning to stop performing a conviction she doesn't
actually feel (her Lie/Flaw: status can be won through sheer aesthetic force of will). A player who is
themselves "a performer of conviction rather than a holder of it" — Demagogue's own definition — would
reinforce exactly the pattern her arc exists to break, not challenge it: incapable of showing her the
difference between performing legitimacy and actually possessing it. Already-established precedent elsewhere
in the roster (confirmed for Trisha Miller; considered and set aside for Vosora, Seica, and Majyao).

**Signal line** (if stat threshold not met, placeholder — not final voice work): *"You like the dress. I'm not
sure you've noticed there's a person in it."*

**Gate 3 — Romance beats (Courtship Sequence):**

Lillian's romance is the arc of someone used to being wanted for the performance discovering what it is to be
wanted for what's underneath it — and, per her Countertype psychology, discovering she can survive being seen
that plainly.

1. **See past the performance, unprompted:** Early on, the player notices or asks about something real beneath
   the extravagance without being cued to look. She can tell the difference between someone drawn to the
   aesthetic and someone actually looking at her.

2. **Show genuine investment in her house's tradition itself, not just in her.** **The first Courtship Sequence
   beat in the roster built under the Romance Beat Checks law** (`Companion_System.md`) — clears every
   category's minimum, several at the ideal count:
   - **Skills (4, exceeds the 3 minimum):** **[Insight ≥ X]** (Humanity-governed) reads what the tradition
     specifically means to *her*; **[Narrative ≥ X]** (Humanity-governed) knows the actual cultural/historical
     story of the intimate tradition, not just isolated facts; **[Speech ≥ X]** (Humanity-governed) can
     actually hold a substantive conversation with the tradition's own practitioners, not just recite facts at
     them; **[Cryptography ≥ X]** (Calculation-governed) can decipher the tradition's own pre-digital or coded
     archival records, surfacing something a casual observer couldn't.
   - **Non-disqualifying Trait (1, meets minimum):** **Sonic Resonance** (`Character-Creation/Traits.md`) — an
     existing "Leo artistic/performer builds" trait (+20% Narrative/Speech performing publicly, faster Leo
     reputation gain); a player who built specifically toward Leo's artistic life satisfies this beat directly.
   - **Perk (1, meets minimum):** **Golden Ring Devotee** (`Perks/Regular_Perks_-_Level-Up.md`, new — added
     alongside this beat) — deep, recognized understanding of Leo's grand/intimate tradition as a whole.
   - **Non-disqualifying MACHINE stats (3, optional category, well covered):** **[Investigation ≥ X]** notices
     specific details of the craft/history unprompted; **[Humanity ≥ X]** registers the emotional weight the
     tradition carries for its practitioners generally; **[Calculation ≥ X]** grasps the structural/political
     mechanics of *why* her house is disadvantaged (the Allocation Formula — see
     `District_Canon_Reference.md`'s Leo entry).
   - **World knowledge (3, exceeds the 1 minimum, hits the 2-3 ideal):** conclusive knowledge from a Leo
     district Under-Questline, stated accurately in dialogue; having found and explored the original
     intimate-tradition dome cluster (the Twin Founding's own second, smaller-chambers site — a real, walkable
     location per `Deep_Dives/03b_Leo_Star_War_Alternatives.md`'s level-design payoff note), through general
     exploration, no quest required; having appraised or closely examined a genuine artifact of the
     tradition's own craft, gaining real firsthand understanding of it.
   - **District reputation (1, meets minimum):** per the Romance Beat Checks law's escalation schema, Beat 2
     is an opening beat — any 🟢 tier qualifies (Accepted, Liked, Smiling Troublemaker, Good-Natured Rascal, or
     Idolized) with Leo district itself.
   - Exact numeric thresholds TBD, pending her MACHINE stat baseline and Leo Under-Questline content both
     being further along.

3. **Witness a moment of real cost without flinching or trying to fix it:** Somewhere in her personal
   questline, the mask nearly slips — a rare, unguarded moment where what the ambition has actually cost her
   shows. The romantic path doesn't perform sympathy or rush to make it better. It simply stays.

4. **Gently name the gap, without cruelty:** At some point, the player names — carefully, not as an
   accusation — the distance between "I do this for my house" and "I want this for myself." The single most
   dangerous beat for her Countertype psychology, and the one her romance is actually built to test.

5. **The culmination — she makes the first move:** Not a grand declaration. A small, real gesture with no
   audience and no aesthetic value, offered for its own sake, when nothing about the moment calls for
   performance at all. She initiates it.
