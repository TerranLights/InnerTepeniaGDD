# DLC Main Questline Design Method — Input Synthesis & But/Therefore Construction

**What this is:** the method for constructing each DLC's main questline (one DLC per subnet). Not a
worked example against any specific subnet yet — a reusable specification to run against each subnet
when its turn comes. Companion document to `But_Therefore_Quest_Design_Method.md` and
`But_Therefore_Lore_Design_Method.md`; this file governs *which inputs feed the chain* for a DLC main
questline specifically, where those two govern the chain-construction grammar itself.

**Weighting note (revised):** input source 6, below, draws on the city-level "lore history" files (the
`z-template_-_city_histories_conflict_variant.md` / `z-template_-_city_histories.md` translations of
each city's `_Course_of_Events_Suggestions.md`). That material is newer and less developed than the
other seven inputs, several of which represent multiple completed audit/synthesis passes. For now, this
method should lean on inputs 1–5, 7, and 8 as the strong, well-developed evidentiary base, and treat
input 6 as a lighter supplement rather than a co-equal, load-bearing source — available where it exists
and adds something real, but not a blocker. This method can be run against a subnet whether or not that
subnet's lore-history translation pass is finished.

---

## Step 1: Gather Inputs

For the specific subnet/DLC under construction, pull **only** the following from each of its
established documents — not the full documents wholesale:

1. **City-level Cross-Reference Synthesis sheets** (`[City]_Cross_Reference_Synthesis.md`, one per city
   in the subnet) — **only** each Finding's bolded **4th-order effect:** line, plus the full
   **Synthesis: The Pattern Across All Findings** section. Skip Findings 1–3(or however many) text
   itself except where needed to understand what the 4th-order line is referring back to.

2. **Subnet-level Cross-Reference Synthesis sheet** (`[Subnet]_Subnet_Cross_Reference_Synthesis.md`) —
   same rule: only the 4th-order effect lines and the Synthesis section.

3. **Throughways, both levels** — every city-level Throughways content folded into the subnet's own
   Cross-Reference work, and (**paying special, particular attention here**) the subnet-level
   `[Subnet]_Cross_City_Throughways.md` file in full. Throughways are causal chains by construction, so
   take the full resultant finding of each one, not just a single line.

4. **City-level Full Extrapolation sheets** (`[City]_Full_Extrapolation.md`, one per city) — every
   numbered Section, **except**: (a) whichever section resolves the city's own Demonym, and (b) whichever
   section covers Notable Figures (proposed or confirmed). Every other section is in scope, since these
   are each city's own best-current proposed answers to their open questions — exactly the material a
   main questline should be built out of, not invented fresh.

5. **Subnet-level Full Extrapolation sheet** (`[Subnet]_Subnet_Full_Extrapolation.md`) — **Section I
   only**: the section defining each city's role within the subnet's own collective identity/theme.

6. **City-level "lore history" files** (the Course-of-Events template translations, per city) —
   **lightweight supplement, currently de-emphasized** relative to inputs 1–5, 7, and 8 (see the
   Weighting note above). Where these exist, pull only the very last State of Affairs [N+1] in the last
   cycle of each translated suggestion — everything upstream of that final setting-condition is
   past-tense causal history, not a condition still actively in effect at game-time. Where they don't
   yet exist for a given subnet, skip this input entirely rather than waiting on it.

7. **Local Cultures city sheets** (`Local_Cultures/[Subnet]/[City].md`, one per city) — exactly three
   sections: **Part II §6 (Social Contract & Unwritten Rules)**, **Part III §15 (Division of
   Industry)**, and **Part IV §23 (Relationship to Other Cities)**.

8. **Super-Ultra-Megasheet** — all analysis findings (Mega-Init, Full Extrapolation, Cross-Reference
   Synthesis, Cross-Regional Patterns, Cross-Regional Throughways) that touch the subnet or any of its
   member cities.

---

## Step 2: Construct Candidate Chains

Using everything gathered in Step 1 as the complete evidentiary base, construct **at least 10** distinct
candidate But/Therefore chains for the DLC's main questline (per the grammar in
`But_Therefore_Quest_Design_Method.md`). Each candidate chain must satisfy all three of the following:

- **Non-conflicting.** Doesn't contradict anything gathered in Step 1 — not just avoiding direct
  contradiction, but not requiring any Step 1 fact to be quietly ignored for the chain to work.
- **Characteristically consistent.** Reads as something that could only happen in *this* subnet
  specifically — grounded in the subnet's own collective identity/theme (input 5) and its cities' own
  established social contracts, industry, and inter-city relationships (input 7), not a
  generic conflict that could be relocated to any other subnet without losing anything.
- **Actually emergent, not invented.** Should read as a plausible consequence of the gathered inputs,
  not a new idea dropped on top of them. The more a candidate chain visibly traces back to a specific
  4th-order effect, Throughway finding, Full Extrapolation section, or final lore-history setting-condition
  — the stronger it is. **But don't force this.** If a candidate chain only connects to the source
  material loosely, either strengthen the connection or drop the candidate. A small, solid questline
  beats a long, complex, incoherent one every time.

---

## No Good Endings — Ending Distribution and Cost Calibration (DLC/Subnet Scale)

**What this is:** the project's standing "No Good Endings" design law, applied at DLC/subnet scale. This
section is written to stand on its own — the fuller companion-scale version of the same law is authoritatively
defined in `Game-Mechanics/Core-Mechanics/Companion_System.md` under its own "No Good Endings" section, and the
district/faction-scale version lives in `Storyline/Side-Content/District_Under_Questline_Design_Method.md`.
This is the same law again, at the scale of an entire subnet's DLC main questline.

**What the law actually says.** "No Good Endings" does not mean no positive endings. It means no *costless*
positive endings. A DLC's main questline is allowed — expected — to resolve well for the subnet, its cities,
and the factions/figures caught up in it. What it is never allowed to do is resolve well for free.

**The required distribution.** Because a DLC has only *one* main questline (Step 2 above narrows candidates
down to a single chosen chain, unlike a district's under-questlines, which keep every qualifying candidate),
this law applies slightly differently than at district scale: rather than governing the distribution across
many parallel candidates for the same subnet, it governs the distribution across the DLC's own set of possible
*resolution branches* for that one main questline (the different ways the questline's climactic choice can
resolve). Within that set:

- **A purely negative resolution — the subnet or its cities left worse off with nothing gained — should be a
  minority** among the questline's possible resolution branches. A real, available branch, not the default and
  not the majority of the outcome space.
- **Bittersweet or mixed resolutions should be the largest category of the available branches, by a real
  margin.**
- **A genuinely positive resolution for the subnet must be real and achievable** — never a trap, never a
  hollow win. But, exactly as at every other scale, never free.

**The core mechanic: the subnet pays a real, named price for its own genuinely positive outcome.** For a DLC
main questline's best-case resolution branch to actually qualify as positive under this law, the subnet or its
constituent cities — not just an individual Notable Figure or faction leader involved — must give up something
they genuinely value, specifically in order to secure whatever the positive resolution actually delivers. This
is the subnet-scale version of a companion sacrificing something dear specifically to gain the player: the
subnet's own equivalent of "the Want" (its own collective identity/theme per input 5 above, a piece of
inter-city autonomy, a resource, a trade relationship, standing relative to another subnet or to Concordia
itself, or a comfortable collective self-image the questline's own escalating pressure exposes) has to be put
in genuine, structural conflict with whatever the positive resolution delivers, and the subnet has to lose the
former to secure the latter for real — not a sacrifice that turns out to be trivial or reversible once the
"real" prize is revealed.

**Why this matters specifically for a DLC main questline.** Because Step 2 above already applies a strict
"characteristically consistent, actually emergent, non-conflicting" filter and narrows many candidates down to
one, there's a real risk that the single chosen chain gets selected primarily for how well it satisfies those
three tests, without anyone separately checking whether its resolution branches actually satisfy this ending-
distribution law. The two checks are independent and both required: a candidate can be perfectly emergent,
consistent, and non-conflicting while still resolving toward an all-branches-positive or all-branches-costless
outcome space. Apply this section as its own explicit pass over the finally-chosen chain's resolution branches,
not as something the Step 2 tests already guarantee.

**How to apply this once a DLC main questline chain is chosen:**

1. **Name the specific real thing the subnet/cities give up**, for whichever resolution branch is meant to
   read as the best/most positive outcome, before treating that branch as finished. If nothing comes to mind,
   it isn't ready — rework it or explicitly reclassify it as bittersweet.
2. **Scale the cost to what the subnet actually has and values**, per its own established collective identity
   (input 5) and its cities' established social contracts and inter-city relationships (input 7) — not to a
   universal standard.
3. **Make sure the full set of resolution branches for the questline's climactic choice actually spans the
   required distribution** — at least one real negative branch (even if narrow), a larger bittersweet middle,
   and a positive branch with its price named — rather than defaulting to a simple binary of "the correct good
   ending" versus "the ending you get for failing."

---

## Worth Your Attention

Input 6 is the newest and least-precedented of the eight, and — per the Weighting note above — the one
currently carrying the least weight. The other seven inputs represent multiple completed audit and
synthesis passes (the country-wide culture re-check, the Megasheet/Ultra-Megasheet layer, the
Super-Ultra-Megasheet); the lore-history translations are a single, not-yet-fully-built layer on top of
that. A strong candidate chain should be able to stand entirely on inputs 1–5, 7, and 8; if a chain only
holds together *because* of a lore-history connection, treat that as a sign to strengthen its grounding
in the stronger inputs rather than leaning harder on input 6. If input 6 is used at all, remember only
the *final* setting-condition of a translated suggestion is live at game-time — everything upstream of
it is already-resolved backstory, not something still in motion. **Also worth testing deliberately once this
method is actually run against a real subnet:** how the ending-distribution and cost-calibration section above
holds up in practice — whether a single chosen main-questline chain can comfortably support a full spread of
negative/bittersweet/positive resolution branches, or whether some subnet concepts naturally resist a genuine
negative branch (or a genuine positive one) and need a different approach.
