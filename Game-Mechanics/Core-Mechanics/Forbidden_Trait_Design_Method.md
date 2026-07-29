# Forbidden Trait Design Method

**What this is:** the repeatable process for assigning "forbidden traits" (romance dealbreakers) to
companions, established 2026-07-28 while working through Favi della Torre, Naizelle d'Edjordoś, and Villena
Hiresvett. Use this file each time this work resumes with a new companion, rather than re-deriving the
process from scratch.

**Read `Core-Mechanics/Companion_System.md`'s "Forbidden Traits — A Categorically Different Gate" section
first** — that's the authoritative explanation of the mechanic itself (why it's categorically different from
a stat threshold, the implementation precedence rule, the distinct signal-line register). This file is the
*process* for applying that mechanic character by character; it doesn't restate the mechanic's own design.

---

## Step 1 — Derive candidate forbidden traits from the character's existing profile

Forbidden traits come from the same three inputs already used to derive a companion's MACHINE stat
thresholds — don't invent new criteria:

1. **Enneagram personality** (type, wing, subtype, Hornevian/Harmonic group)
2. **Personal history** (backstory, what she's been through, what it left her needing or unable to tolerate)
3. **Personal sensibilities** (professional skills/instincts, what she's spent her life doing, what she can
   detect or refuses to accept)

Ask: given who this specific character is, is there a trait in the pool (`Character-Creation/Traits.md`)
that represents someone she would recognize — through instinct, professional skill, or lived experience — as
fundamentally wrong for her, permanently? Look for **precise** mechanical fits, not vague thematic ones. The
strongest picks so far have come from a trait's own defining *mechanic* mapping almost literally onto
something the character's romance test is already built around (e.g., Naizelle's whole arc is about never
having what she hasn't offered pried out of her — Narrative Ghost's defining ability is a mechanical
enactment of exactly that violation, not just a loose vibe match).

**Aim for 1 to 3 forbidden traits per character — never pad to hit 3.** Quality over quota, same rule as the
implant-system pass earlier. Two precise, well-justified traits are better than three where the third is a
stretch. It is completely fine for a character to end up with just one.

**The same trait can be forbidden for multiple different companions, for different reasons.** Reuse is not a
problem — Narrative Ghost is forbidden for both Naizelle (privacy violation) and Villena (inauthenticity/
artifice), and the two rationales don't overlap at all despite sharing a trait. Always write out the specific
reason for *this* character, even when reusing a trait already forbidden elsewhere.

**When nothing in the existing pool fits precisely, design a new trait.** This is expected, not a fallback —
the process is also a real trait-design pipeline. When proposing a new trait:
- Ground the mechanic in something concrete and reusable beyond just this one companion (Cut Losses, designed
  for Favi, is a general "self-preservation over loyalty" trait usable as a dealbreaker for any
  protection/loyalty-testing companion later, not a one-off).
- Give it a real bonus and a real penalty, following the same varied-mechanic-shape standard set during the
  Base Traits redesign (conditional effects, stat trades, unique abilities — not just another flat -Humanity).
- Add it to `Character-Creation/Traits.md` in the same pass, in the main Base traits table, noting which
  companion/pass surfaced it.

**Flag, don't force, near-miss candidates.** If a trait is thematically close but mechanically represents a
*different* violation than the one under discussion (e.g., Information Warfare's Data Leak vs. Narrative
Ghost's rumor-probing — both "extract what wasn't given," just through different mediums), name the overlap
explicitly and let the developer decide whether it's genuine additional coverage or redundant restatement.

---

## Step 2 — Where the confirmed forbidden traits actually get written

**`Core-Mechanics/Companion_System.md` never gets per-character specifics.** It holds the general mechanic
only. Each companion's own "Romance Design" subsection in that file should say only:

> **Forbidden traits:** see [Character]'s own character file (`Worldspace/Characters/Dolls/
> Still-Present_-_In-Game/recruitable/[Character]/README.md`) for her specific forbidden traits and
> rationale — this file covers the general mechanic only, not per-character assignments.

**The "Confirmed Romanceable Characters" summary table's Trait Gates column** reads **"See character file"**
for any character whose forbidden traits are assigned — never list the actual trait names there.

**Each companion's own `README.md` gets the real content**, in a new section titled `## Romance — Forbidden
Traits`, placed logically among the file's other sections (after "Relationships & Hooks," before "Design
Notes & Open Questions" worked well for all three done so far). That section must contain:

1. A one-line pointer back to `Companion_System.md`'s general mechanic explanation.
2. **"[Character]'s forbidden traits: [Trait A], [Trait B]."** followed by the specific rationale for each,
   tied to her own personality/history/sensibilities.
3. A **forbidden-trait rejection line** — distinct in register from her ordinary stat-threshold Signal line.
   Where the Signal line implicitly invites "come back once you've grown," the forbidden-trait line must read
   as a genuinely closed door — something that acknowledges there's no path forward, ever, on this
   playthrough.

**Also update the character's own top-of-file summary line** (the `**Romance Potential:**` line near the top)
to briefly name the forbidden traits inline, matching how it already names the stat thresholds — e.g.,
`forbidden traits (permanent dealbreakers, confirmed [date]): [Trait A], [Trait B]`.

---

## Step 3 — Don't forget the implementation note

Per `Companion_System.md`'s own binding rule: in actual game code, a forbidden-trait check must be evaluated
**before** and **instead of** the standard MACHINE stat-gate dialogue — the two never display simultaneously.
This is already documented centrally and doesn't need repeating per-character, but keep it in mind when
sequencing which companions to prioritize once implementation work begins.

---

## Companions completed so far, 2026-07-28

- **Favi della Torre** — Loose Cannon, Cut Losses (Cut Losses designed during this pass)
- **Naizelle d'Edjordoś** — Narrative Ghost, Loose Cannon
- **Villena Hiresvett** — Narrative Ghost, Cut Losses
- **Ji-Eun Kim** — Narrative Ghost, Information Warfare (a case where reusing Narrative Ghost alongside
  Information Warfare was judged genuinely non-redundant, unlike the Naizelle case — see her own file's
  rationale for why "gathering secrets" vs. "weaponizing exposed secrets" are distinct threats for someone
  hiding from real danger)
- **Michelle Stanton** — Cut Losses (its 3rd distinct use — see her own file for why "commitment to place"
  is a different specific failure than Favi's protection test or Villena's loyalty test). A new trait,
  **Greener Pastures**, was designed specifically as a candidate second forbidden trait for her (a permanent
  reputation ceiling, mirroring her own "passing through" Signal line) but went through several balance
  iterations — see `Traits.md`'s own entry for the full history of why every conditional trigger tested broke
  under scrutiny (exhaustible novelty flags, farmable time-based cooldowns) before landing on a flat,
  unconditional bonus. Once unconditional, it lost the specific "transience" characterization that made it
  Michelle's opposite, so it was added to the general trait pool but **not** applied as her forbidden trait.
- **Trisha Miller** (non-recruitable, romanceable — her full romance design, including stat gate, was also
  created from scratch during this pass, since she had none before) — Narrative Ghost, Cut Losses, Demagogue.
  Two new traits surfaced during her pass: **Fists First** (added to the pool, but NOT applied to her — her
  own philosophy already tolerates physical force as a last resort, so a violence-first personality reads as
  distasteful rather than disqualifying) and **Demagogue** (added to the pool AND applied to her — a
  performer of public conviction rather than a genuine holder of it, directly contradicting what makes her
  own voice credible to her community). Demagogue carries a flagged production dependency — see `Traits.md`'s
  own entry and the matching `TODO.md` item.
- **Seica Cenilaithe** — Cut Losses, Empathic Bridge, Narrative Ghost. Cut Losses' escalating reuse (now 5
  companions) prompted a real balance fix — see `Traits.md`'s own updated entry: the trait now grants zero-AP
  fleeing plus a once-per-combat save-from-death at 50% HP, proportional to how disqualifying it's become.
  Empathic Bridge is a case worth remembering: a "good," kind trait can still be a precise dealbreaker for a
  specific personality without being a bad trait overall (Seica explicitly names appeasement, its defining
  ability, as a failure condition). Demagogue and Fists First were both considered and set aside as
  insufficiently precise fits — see her own file for why.
- **Majyao Bisyugota** (non-recruitable, romanceable — her stat gate already existed; only forbidden traits
  were missing) — **Demagogue confirmed; Narrative Ghost considered but not confirmed** (developer wasn't
  convinced it was precise enough — left off). **A new trait, working title "Broad Strokes," is held/flagged
  in `Traits.md` rather than finalized** — someone constitutionally oblivious to small details, opposing her
  5-wing's need for a patron who notices specifics. Its bonus side is still undecided (Speech vs.
  Survival/Outdoorsman vs. combat-initiative, none chosen) — an earlier "+Barter on fast trades" version was
  rejected since the game has no trade-timer mechanic to hook into. **Revisit Majyao's forbidden-trait list
  once that trait is finalized** to decide whether it gets added to her alongside Demagogue.
- **IT-068 [Flora]** (her own stat gate already existed; only forbidden traits were missing) — Cut Losses,
  Narrative Ghost, Demagogue. Also a 6w5 like Favi, so Cut Losses recurs for the same core reason (a crew/
  companion-protection test). Confirms Demagogue's production dependency (crowd/group-address content) now
  applies beyond just Trisha's case — worth prioritizing that content question given how many companions
  already depend on it.
- **Vosora Lashár Tanslock** — Narrative Ghost only. Loose Cannon was considered (distasteful to her, but not
  a dealbreaker) and set aside. A new trait, **"One-Way Exchange"** (an intellectual free-rider who never
  reciprocates), was designed specifically from her personal specs but flagged for future review rather than
  finalized — it went through two corrections (a percentage-bonus version that doesn't exist in this game's
  flat-threshold system, then a MACHINE-stat-scale number used on what should be a skill-scale bonus) and
  still carries a real, unresolved production dependency (tracking NPC-given vs. self-discovered information,
  tagging specific "informed checks"). See `Traits.md`'s own entry for the full history.

All other confirmed romanceable companions still need this pass.
