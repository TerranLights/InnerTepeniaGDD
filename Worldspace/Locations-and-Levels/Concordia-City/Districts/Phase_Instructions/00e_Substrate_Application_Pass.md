# Cross-Phase Procedure — Applying the Zodiac Personality Substrate

**Written 2026-08-29**, generalised from Cancer's substrate application pass (`District_Megasheets/01_Cancer/
Cancer_Full_Extrapolation.md`, "Second Pass"). This is the repeatable procedure for using
`../Zodiac_Personality_Substrate/` on **any** district.

Not a phase. The eight phases are *content categories*; this is a layer that cuts across all of them. Sibling to
`00b_General_Population_Discipline.md` and `00d_Shadow_Proportion_Discipline.md`.

---

## 1. Two modes — establish which one you are in before starting

| | **Mode A — Second Pass** | **Mode B — First-Pass Input** |
|---|---|---|
| **Applies to** | Cancer, Taurus, Leo | The other ten districts |
| **Why** | Phases 1-8 were completed before the substrate existed | The substrate exists *before* their phases are written |
| **Shape** | A separate dated section appended after existing findings | Folded into the phases themselves as they are written |
| **Overlap check** | **Mandatory** (§3) | Not applicable |
| **Existing QA record** | Left intact; the new pass gets its own QA block | Single QA at completion, as normal |

**Do not run Mode A on a Mode B district.** Producing a bolted-on "substrate section" for a district whose
phases have not been written yet fragments its file for no reason. In Mode B the substrate is simply one more
input, alongside the district's Deep Dive, Vision Notes, Canon Reference entry, diaspora composition, and
real-world influence picks.

**Taurus and Leo carry a complication:** both are Mode A, but neither has passed the completion QA gate, and
both predate Phase 7, the research-first rule, and the general-population discipline. **QA them first**, or the
substrate pass will be layered on top of material that has not been verified.

---

## 2. Inputs

Per district, before writing:

- `../Zodiac_Personality_Substrate/NN_<Sign>.md` — the district's own sign file
- `F_Rulerships.md` §5–6 — its capability profile. **The highest-yield single input** (see §5)
- `D_Aspect_Geometry.md` §5 — its opposition, two squares, trines, sextiles, quincunxes, in district terms
- `A_Elements.md` and `B_Modalities.md` — its temperament family and its relationship to change
- `G_Correspondences.md` — material texture, already filtered for Antarctic enclosure
- `E_Decans.md` — optional sub-neighbourhood texture; weakly sourced, treat as a menu
- **`NN_<Sign>.md` §15 Source Gaps — read it as an input, not a disclaimer.** *(Added 2026-08-29.)* This section
  looks like a caveats list and is in practice one of the highest-yield generators in the folder. **Two of
  Taurus's strongest structural findings came from it and from nowhere else:** the corpus's admission that it
  says nothing about this temperament *under poverty* is what produced the Coldsiders reading, and its admission
  that it offers *no resolution mechanism* for two of this temperament in conflict is what finally supplied the
  missing machinery behind a 250-year-old unresolved schism. **Where the sources have a hole, ask whether the
  hole is the district's mechanism.** A faculty the corpus cannot describe is often a faculty the district does
  not have — and that absence, made institutional, is a finding no amount of positive material would produce.
- The district's existing `Deep_Dives/`, `District_Vision_Notes/`, and `District_Canon_Reference.md` entry

**The Hub is a genuine exception.** Ophiuchus has no element, no modality, no opposing sign, and no aspects at
all. The layer stack in §4 does not apply to it, and neither does §6. Its substrate file
(`13_Ophiuchus_Hub.md`) treats that absence *as* the content; use it directly and skip the structural steps.

---

## 3. Mode A step zero — the overlap check, before writing anything

**This is what keeps the pass from being a re-labelling exercise**, which is the failure that forced Cancer's
original rewrite.

Take the substrate file's main claims — its capability profile, its central shadow mechanism, its modality
reading, its entry/socialisation mechanic, its conflict geometry, its correspondences — and grep the district's
existing `Full_Extrapolation.md` for each. Something like:

```
for t in "<capability terms>" "<shadow mechanism>" "<modality>" "<entry mechanic>" \
         "<opposition district>" "<stone/metal>" ; do
  printf "%-40s %s\n" "$t" "$(grep -ci "$t" <District>_Full_Extrapolation.md)"
done
```

**Read the result honestly:**

- **Near-zero overlap** — the substrate is genuinely additive. Proceed. *(Cancer scored 0 on nine of ten
  concepts.)*
- **Substantial overlap** — most of what the substrate offers is already present under other names. **Do not
  write a second pass.** Record that the substrate corroborated the existing work and stop. That is a real and
  useful outcome, not a failure.
- **Partial** — write only the genuinely new material. Do not pad it out to look like a full pass.
- **Correction** *(added 2026-08-29 — a fourth outcome, and the most valuable one).* The substrate shows an
  **existing** finding to be half-written rather than wrong. Taurus's Finding II had described a trust mechanism
  in only its favorable direction; the substrate revealed the mechanism is symmetrical, which turned the
  district's warmth and its most characteristic injustice into a single institution seen from two sides. **Write
  this as an explicit correction of the named prior Finding, not as a new independent one**, and say in the text
  that it corrects rather than contradicts — the original finding was true, just incomplete. Expect this outcome
  wherever the original pass wrote about admission, trust, or belonging, because those are the findings a
  well-meaning pass writes only the pleasant half of. See `00c` **Gate 9**.

---

## 4. The layer stack

Four independent readings per district. They should **agree in tone and differ in content**:

1. **Enneagram** — *psychological motive*. Already established in
   `../Regional-Characteristics/district_by_Enneagram_group_series.md`. Why the district wants what it wants.
2. **Element** — *temperament family*. How it processes experience.
3. **Modality** — *relationship to change*. Whether it initiates, holds, or dissolves.
4. **Dignity** — *capability profile*. What it is structurally good at and structurally cannot do.

Where two axes agree, the trait is well grounded and can be built on hard. Where they disagree, that is usually
a finding — see §7.

---

## 5. The primary generator: the capability reading

The highest-yield technique in the folder, and the one to run first.

> A faculty **strong** in this district (domicile/exaltation) = something it does structurally well.
> A faculty **weak** here (detriment/fall) = something that works against the grain, is distrusted, or has no
> institutional home.
> **The district's characteristic failure is what its weak faculty was supposed to prevent.**

It produces flaws that feel *inevitable rather than assigned*, and — critically — flaws that need **no
villain**, which is what makes them compatible with this project's non-malice discipline and with
`00d_Shadow_Proportion_Discipline.md`.

**When a district has fewer than four terms, the absence itself is the finding.** *(Added 2026-08-29 — this
affects six of the thirteen.)* `F_Rulerships.md` §5 notes that Gemini, Leo, Sagittarius and Aquarius have
neither exaltation nor fall, Taurus has no fall, and Scorpio has no exaltation. **Do not treat the thin row as
less material to work with.** Taurus's entire principal finding came out of the empty cell: having no fall means
there is nothing it actively despises, therefore nothing it refuses on principle, therefore — run out to its
institutional consequence — it is the district the rest of the city routes its unwanted asks through, because it
is the one that will not turn a request into a fight. **Ask what it means for a district to lack that faculty
entirely**, rather than reading the row as incomplete.

**Write it as a capability profile, not a diagnosis.** Two strong faculties and two weak ones, each stated as
what the district can and cannot institutionally do — then one consequence that follows. In Cancer's case the
consequence was that a resident with no dependent has no route to be heard. **Every district's consequence will
be different in kind, not just in detail.** If yours reads like a variant of another district's, it is wrong.

---

## 6. Conflict geometry

`D_Aspect_Geometry.md` §5 gives each district its opposition, two squares, and its affinities, already
translated into district names. Three things to do with it:

- **Write the opposition as a mechanism, not a rivalry.** The useful question is *what does each pole refuse to
  develop, and who supplies it instead?* Oppositions here tend to be feedback loops rather than standoffs.
- **Distinguish the two squares from each other.** They are rarely the same kind of friction — typically one is
  loud and one is quiet, and the quiet one is usually nastier and better material.
- **Check against existing canon before writing.** `../District_Natural_Allies.md`, the district's own
  internal/external conflict lists, and the four Enneagram-derived "full overlap" pairs. Where geometry and
  canon agree, the pairing is doubly grounded. Where they disagree, read them **together** before discarding
  either — the disagreement is often more accurate than either axis alone.

**The three-way differentiation set — the most reusable trick the Taurus pass produced.** *(Added 2026-08-29.)*
A district plus its two hardest frictions makes a **natural three-way contrast for any single behavior
category**, because the geometry guarantees they differ on the same axis without overlapping. Taurus's protest
grammar fell out of this immediately: **the Labs organizes, Leo performs, Taurus obstructs** — three answers to
one question, each finding the other two faintly embarrassing, none of them villainous, none of them previously
written down. The technique generalizes to any category where districts must differ but have no reason to
conflict: how each mourns, celebrates, apologizes, courts, settles a dispute, or treats a stranger. **Pick the
category first, then read all three off the geometry** — deriving one district's answer alone tends to produce
something generic, because there is nothing to differentiate it against.

**Standing opportunity:** none of the four canon district pairs is a square or an opposition. All six
oppositions and twelve squares remain unexploited by district canon.

---

## 7. Handling contradictions with existing canon

The substrate *will* contradict established material. That is expected and it is not a problem to be smoothed.

**Rules:**

- **Canon wins.** The substrate is proposed reference; Deep Dives, Vision Notes, and Canon Reference outrank it.
- **State the contradiction in the text**, with the reconciliation. Do not silently pick one.
- **Look for a both-are-true reading first — three for three so far, so treat it as the default expectation
  rather than a hopeful first try.** Cancer's two contradictions resolved that way (unhurried at street level
  *and* institutionally expansionist; entry fast for *structural residency*, sideways-only for *belonging*), and
  so did Taurus's (the most static position in the system *and* a standing migration destination — it absorbs
  people readily and changes practice never).

  **The recurring shape is worth naming, because knowing it makes the reconciliation findable rather than
  lucky:** in every case so far the contradiction turned out to be **one disposition producing two opposite
  effects on two different objects, or at two different scales.** So when the substrate and canon disagree, do
  not ask which is true — ask *what single trait would produce both of these*, and check whether the two claims
  are actually about different objects (people vs. practice, structure vs. belonging, street level vs.
  institution). If they are, both stand, and the pair is more informative than either half.
- **Where it genuinely cannot be reconciled, leave it flagged as open** rather than deciding unilaterally.

---

## 8. Translation discipline

**The zodiac never appears in the district's own claims.** Put substrate reasoning in bracketed citations so it
can be audited, and write the finding itself entirely in district vocabulary:

> ✅ *"The district has no working mechanism for refusing a request, and no grammar for a grievance voiced on
> one's own behalf* **(substrate §10)**.*"*
>
> ❌ *"Because Mars is in fall here, the district cannot self-advocate."*

Nothing from `00_Method_and_Sources.md`'s prohibited list — sign names, element labels, aspect or modality
vocabulary, rulers, decans — may appear outside a bracketed citation, and none of it may reach player-facing
text under any circumstances.

A useful check when finished: **grep the new material for zodiac terms and confirm every hit is inside a
citation or a section header.** Use word boundaries on *every* alternative — a pattern with a bare `mars` will
match inside `grammars` and send you chasing a leak that isn't there:

```
awk 'NR>{last line of the original pass}' <District>_Full_Extrapolation.md > /tmp/new.md
grep -Ein '\b(venus|mars|moon|saturn|mercury|jupiter|pluto|uranus|neptune)\b|\b(domicile|exalted|detriment|decans?)\b|\b(trines?|squares?|sextiles?|quincunx|opposition)\b|\b(cardinal|fixed|mutable)\b|zodiac|astrolog' /tmp/new.md
```

Inspect **every** hit rather than trusting the count. In the Taurus pass this surfaced four genuine leaks in
district-facing prose (`squares`, `trine`) that had to be rewritten into district vocabulary, alongside two
legitimate in-citation uses and one false positive.

---

## 9. Shadow proportion

Read `00d_Shadow_Proportion_Discipline.md` before writing, not after.

The one point specific to this procedure: **the substrate files are deliberately shadow-heavy** because the
extraction brief prioritised capturing failure modes. That weighting is an artifact of extraction. Applying a
sign file proportionally to its own section lengths produces a district that is largely pathology, which is
wrong for every district in Concordia.

Lead with what the district sincerely believes it is doing and largely achieves. The shadow follows from that,
unintended and unnoticed.

---

## 10. QA

`00c_Completion_QA_Checklist.md` still governs. Three notes on how this pass interacts with it:

- **Gate 4 (Swap Test) is the load-bearing one here.** Substrate-derived material is the most likely of any to
  generalise, because it descends from a system of twelve archetypes rather than from this district's own
  history. Swap against the nearest comparable register and require that **nothing survives unchanged**.
- **Gate 3 (contradiction check)** absorbs §7 above.
- **Mode A only:** record the overlap-check result in the new QA block, and leave the original QA block
  untouched — it is the record of a different pass.

---

## 11. Worked example — and the warning that goes with it

Cancer's Second Pass section is the model: `District_Megasheets/01_Cancer/Cancer_Full_Extrapolation.md`.

**Take its procedure. Do not take its content.** Cancer produced a capability profile about refusal and
self-advocacy, a shadow about care that is hard to end, and sideways-only belonging because *that is what
Cancer is*. Another district's capability profile will concern entirely different faculties, and there is no
reason to expect anything resembling a smother-lock, a sideways gate, or a dependent-based standing rule
anywhere else. Inventing one because Cancer has one is exactly the failure `00_Index.md` warns about.

**The proportion note in that section is worth copying structurally** — an explicit statement, before the
findings, of what the district sincerely is and does well.

---

## 12. Known limits

- **Everything at institutional or civic scale is derivation.** The source books describe individual psychology
  and one-to-one compatibility, essentially never populations or institutions. Mark derived material as derived.
- **The substrate cannot tell you a district's history.** It supplies temperament, capability, and relational
  geometry. Founding events, migrations, and specific crises come from `Historical_Pressures.md`, the Deep
  Dives, and `00b_Two_Stage_Methodology.md`.
- **Decans are weakly sourced** (two of eight books). Optional.
- **Some correspondence columns are thin or absent** per district. `G_Correspondences.md` logs exactly which.
  Leave gaps as gaps.
