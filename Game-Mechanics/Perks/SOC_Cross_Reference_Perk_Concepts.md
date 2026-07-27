# SOC Cross-Reference Perk Concepts

**What this is:** five perk concepts that emerged specifically from *cross-referencing* the 14 archetypes
against Concordia's 13 districts (`SOC_Cross_Category_District_Matching.md`) — patterns visible only once the
archetype list and the district list are read against each other, not from either list in isolation. Marked
for design & development, 2026-07-26. Companion to `SOC_Archetype_Perk_Brainstorm.md` (one concept per
archetype in isolation); this file is the next layer up. **None of these are locked design** — concepts and
directions only, flagged here so they aren't lost before real development time is available.

---

## 1. District-Flavored Variants of the Same Archetype

**The insight:** a single archetype (e.g., Licensed/Credentialed Professional) doesn't mean the same thing
everywhere it appears. The district it was practiced in should color *how* the game and its NPCs react to it
— not just whether the archetype applies at all.

**The concept:** rather than one flat "you have a credential" perk, split by district-flavor:
- **Cancer-flavored:** warm, community-embedded — NPCs read the credential as trustworthiness and care,
  extend informal access the way Cancer's own "doors are always unlocked" culture works.
- **Libra-flavored:** formal, procedural — NPCs read the credential as institutional legitimacy, opens doors
  gated by rank/protocol rather than by warmth.
- **Scorpio-flavored:** intense, confrontational — NPCs read the credential as evidence of having survived or
  administered something difficult; opens doors gated by demonstrated toughness, not paperwork.

**Design note:** this could generalize beyond just Licensed Professional — any archetype that hits Strong or
Moderate in more than one district (nearly all of them) could get this same district-flavor treatment. Worth
deciding whether to build this as 2-3 explicit named variant-perks per archetype, or as a single perk whose
flavor text/dialogue dynamically reflects whichever district the player's chosen background points to.

---

## 2. The Taurus "Quiet Professional"

**The insight:** Taurus is the one district where no archetype hits Strong — confirmed as correctly
reflecting the district's own residential, non-institutional identity, not a gap to fix. But that absence is
itself interesting: it means a character whose profession *doesn't* register strongly anywhere is, in a real
sense, a Taurus-flavored identity by default.

**The concept:** a perk built around professional anonymity rather than professional recognition — "nobody
ever needed to know what you did before the war." Mechanically, this could grant the *opposite* benefit of
every other archetype perk on this list: instead of NPCs recognizing and reacting to your background, you
blend in, avoid unwanted attention, and move through Taurus specifically (and possibly the wider city) without
your professional history ever becoming a plot hook, a target, or a lever anyone can pull on you.

**Design note:** this reframes "underrepresented" as a genuine roleplay choice rather than a deficiency —
a player picking an obscure, unremarkable real-world job for their character concept gets something real out
of it (safety/anonymity) rather than just missing out on the recognition perks everyone else gets.

---

## 3. Aquarius's Credentialed-but-Anti-Institutional Tension

**The insight:** Aquarius is Moderate (not Strong) for Licensed/Credentialed Professional specifically because
its own culture actively undervalues formal credentialing as a value, even though the University of Concordia
sits right there and plenty of Aquarius researchers hold real credentials. That's a genuine internal
contradiction worth building a perk around, not smoothing over.

**The concept:** a perk for a character who has real, earned credentials and treats the institutions that
granted them with open contempt or indifference. Bonus standing specifically in Aquarius (where this attitude
is *the norm*, not a liability), real friction in Cancer or Libra (institutions that expect deference the
character refuses to give, even though the character's credentials are completely genuine there too).

**Design note:** distinct from a simple "high skill, low reputation" build — the friction here is
specifically about *attitude toward institutions*, not competence. A character could be extremely good at
their job and still generate this friction, which is the point.

---

## 4. "Portable Expertise" (Multi-District Archetype Overlap)

**The insight:** several archetypes hit Strong or Moderate in *multiple* districts at once (Skilled Manual
Trade: Capricorn, Virgo, and Aries all want it; Clerical/Office-Based: Libra, Gemini, Capricorn, Virgo, and Hub
all want it). A trade or skill that's valuable in more than one place isn't really a single-district
specialty — it's genuinely portable.

**The concept:** rather than tying recognition to one specific district, a perk built around this overlap
travels with the player — the same baseline recognition and access wherever the archetype has real
institutional pull, rather than requiring the player to "pick" one district's version of their old job. The
flavor is explicitly "your trade/skill is useful everywhere that needs it," distinct from concept 1 above
(which is about the *same* archetype reading differently per district) — this one is about *not* needing a
district-specific flavor at all, because the expertise itself is what travels, not a district-flavored
performance of it.

**Status: fully developed, 2026-07-26.** See "Working Notes — Concept 4, Archetype by Archetype" below for all
14 archetypes (13 with a concept, 1 explicitly given no entry).

---

## 5. The "Generalist" (8-Archetype Districts)

**The insight:** Sagittarius and Gemini each pull in 8 of the 14 archetypes — more than any other district, by
a real margin. That's not a coincidence of the matching exercise; it reflects something true about both
districts' own established identity (frontier life demands versatility; the information economy rewards
being able to do a bit of everything).

**The concept:** a perk for a character whose job history doesn't fit neatly into a single archetype at all —
someone who's genuinely worn a lot of hats. Rather than picking one specific background, this is its own
distinct identity option: "jack of all trades" as a real roleplay choice, flavored specifically toward
Sagittarius (frontier generalism — the caravan trader who's also scout, mechanic, and storyteller) or Gemini
(information-economy generalism — the operator who's also broker, technician, and analyst), rather than a
vague catch-all.

**Design note:** distinct from simply not having a background at all — this is a genuine, specific identity
("I did a little bit of everything, out on the frontier / in the info trade"), not a null option.

---

## Working Notes — Concept 4, Archetype by Archetype

### Archetype 1 — Supervisor / Foreman

**Multi-district reach:** Strong = Capricorn, Aries, Virgo. Moderate = Leo, Sagittarius, Libra, Pisces, Gemini,
Hub. **9 of 13 districts** — the single broadest reach of any archetype, consistent with "Supervisors of X"
being the most-repeated pattern in the SOC structure itself.

**Concept name:** *Any Crew, Any Yard*

**Idea:** rather than a district-specific "you were a foreman here" perk, this leans into crew leadership
itself being the portable thing — workers and crews across any of the 9 reachable districts recognize a
former boss's bearing regardless of what industry they actually supervised. A unique dialogue option to
direct or rally a crew/group of NPCs becomes available broadly, not gated to one location.

**Resolved 2026-07-26 — requirement:** Positive (in-the-green Reputation Matrix standing, not necessarily
Idolized) in **any 6 of the 9** reachable districts (Capricorn, Aries, Virgo, Leo, Sagittarius, Libra, Pisces,
Gemini, Hub), **plus completion of one Under-Questline in each of those same 6+ districts that's thematically
relevant to crew leadership/supervision.** The "any 6 of 9" framing means the player doesn't need every
district's own Under-Questline to exist for the perk to be reachable — just enough of the 9 for a real player
to plausibly hit 6 — though ideally all 9 eventually get one, for maximum build flexibility.

**Real production dependency, flagged the same way as Reclaimer's Hands/Derelict's Eye earlier this project:**
this perk is currently decorative, not functional — it depends on at least 6 (ideally all 9) genuinely
Supervisor/Foreman-flavored Under-Questlines actually existing across Capricorn, Aries, Virgo, Leo,
Sagittarius, Libra, Pisces, Gemini, and Hub, none of which have been written yet. Per the standing rule
established this session (`feedback_soc_tier_marking_additive_only` memory), those Under-Questlines still need
to go through the actual `District_Under_Questline_Design_Method.md` process when the time comes — this perk
concept is only the reference input pointing at where that content should eventually live, not a shortcut
around building it.

### Archetype 2 — Licensed / Credentialed Professional

**Multi-district reach:** Strong = Cancer, Libra, Scorpio, Capricorn. Moderate = Aquarius, Gemini, Aries. **7 of
13 districts.**

**Concept name:** *Recognized Practice*

**Idea:** the credential itself carries weight regardless of which district originally granted or recognized
it — institutional NPCs across these 7 districts extend a baseline trust/access without the player needing to
re-earn it from scratch in each new place, the same portable-expertise logic as Archetype 1.

**Resolved 2026-07-26 — requirement:** Positive Reputation Matrix standing in **5 of the 7** reachable
districts, plus completion of one relevant Under-Questline in each of those 5 — **with the explicit condition
that at least one of the 5 must be one of the four Strong-tier districts (Cancer, Libra, Scorpio, Capricorn)**,
not an entirely open "any 5 of 7." This keeps the requirement anchored to where the archetype is genuinely
strongest, rather than letting a player satisfy it purely through the three Moderate-tier districts
(Aquarius, Gemini, Aries) alone.

**Real production dependency, same caveat as Archetype 1:** decorative until at least 5 (ideally all 7)
genuinely Licensed/Credentialed-Professional-flavored Under-Questlines exist across Cancer, Libra, Scorpio,
Capricorn, Aquarius, Gemini, and Aries — none written yet, and each still needs to go through the actual
`District_Under_Questline_Design_Method.md` process, not skip it.

### Archetype 3 — Skilled Manual Trade

**Multi-district reach:** Strong = Capricorn, Virgo, Aries. Moderate = Taurus, Sagittarius. **5 of 13
districts.**

**Concept name:** *Hands That Know the Work*

**Idea:** the same portable-expertise logic — a trained eye for diagnosing and fixing a physical problem
reads as legitimate expertise regardless of which district's specific trade tradition it was learned in. A
Capricorn foundry worker, a Virgo tunnel crew member, an Aries engineer, a Taurus household-insulation
specialist, and a Sagittarius jury-rigger all read as "one of us" to each other, despite very different
specific work.

**Resolved 2026-07-26 — requirement:** Positive Reputation Matrix standing in **3 of the 5** reachable
districts, plus completion of one relevant Under-Questline in each of those 3 — **with the explicit condition
that at least one of the 3 must be one of the three Strong-tier districts (Capricorn, Virgo, Aries)**, not an
entirely open "any 3 of 5." Matches the same anchoring logic as Archetype 2 — Taurus and Sagittarius alone
(both Moderate-tier) can't satisfy the requirement on their own.

**Real production dependency, same caveat as Archetypes 1-2:** decorative until at least 3 (ideally all 5)
genuinely Skilled-Manual-Trade-flavored Under-Questlines exist across Capricorn, Virgo, Aries, Taurus, and
Sagittarius — none written yet, and each still needs to go through the actual
`District_Under_Questline_Design_Method.md` process, not skip it.

### Archetype 4 — Uniformed / Disciplined Service

**Multi-district reach:** Strong = Aries. Moderate = Libra, Sagittarius, Capricorn, Virgo. **5 of 13
districts.**

**Concept name:** *Standing Orders*

**Idea:** the same portable-expertise logic — chain-of-command discipline and high-stakes operational
readiness reads the same way regardless of which specific institution instilled it. An Aries shift crew, a
Libra security detail, a Sagittarius expedition team, a Capricorn guild apprenticeship, and a Virgo
crisis-response unit all recognize the same underlying bearing in each other.

**Resolved 2026-07-26 — requirement:** Positive Reputation Matrix standing in **3 of the 5** reachable
districts, plus completion of one relevant Under-Questline in each of those 3 — **with Aries required as one
of the 3, since it's the archetype's only Strong-tier district** (a tighter constraint than Archetypes 2-3,
which each had multiple Strong-tier options to choose from). The other 2 of the 3 can be any combination of
Libra, Sagittarius, Capricorn, and Virgo.

**Real production dependency, same caveat as Archetypes 1-3:** decorative until at least 3 (ideally all 5)
genuinely Uniformed/Disciplined-Service-flavored Under-Questlines exist across Aries, Libra, Sagittarius,
Capricorn, and Virgo — none written yet, and each still needs to go through the actual
`District_Under_Questline_Design_Method.md` process, not skip it.

### Archetype 5 — Direct Public-Facing / Customer Service

**Multi-district reach:** Strong = Leo, Hub. Moderate = Pisces, Gemini, Sagittarius. **5 of 13 districts.**

**Concept name:** *Never Off the Clock*

**Idea:** the same portable-expertise logic — trained composure under constant, repetitive public contact
reads the same regardless of what specific counter, stage, or transit desk it was learned behind. A Leo
performer, a Hub transit coordinator, a Pisces dream-den attendant, a Gemini information broker, and a
Sagittarius trader all share the same "never let them see you rattled" instinct.

**Resolved 2026-07-26 — requirement:** Positive Reputation Matrix standing in **3 of the 5** reachable
districts, plus completion of one relevant Under-Questline in each of those 3 — **with at least one of Leo or
Hub required as one of the 3**, since those are the archetype's only Strong-tier districts. The other 2 of the
3 can be any combination of Pisces, Gemini, and Sagittarius.

**Real production dependency, same caveat as Archetypes 1-4:** decorative until at least 3 (ideally all 5)
genuinely Direct-Public-Facing-Service-flavored Under-Questlines exist across Leo, Hub, Pisces, Gemini, and
Sagittarius — none written yet, and each still needs to go through the actual
`District_Under_Questline_Design_Method.md` process, not skip it.

### Archetype 6 — Scientific / Research / Analytical

**Multi-district reach:** Strong = Aquarius, Gemini. Moderate = Libra, Capricorn, Scorpio, Sagittarius. **6 of
13 districts.**

**Concept name:** *Method, Not Location*

**Idea:** the same portable-expertise logic — methodical, hypothesis-driven thinking reads as legitimate
regardless of which specific discipline or district it was trained in. An Aquarius researcher, a Gemini data
archaeologist, a Libra policy analyst, a Capricorn quality-control auditor, a Scorpio rebirth-technique
developer, and a Sagittarius philosophical debate-hall veteran all recognize the same underlying rigor in each
other.

**Resolved 2026-07-26 — requirement:** Positive Reputation Matrix standing in **4 of the 6** reachable
districts, plus completion of one relevant Under-Questline in each of those 4 — **with at least one of
Aquarius or Gemini required as one of the 4**, since those are the archetype's only Strong-tier districts. The
other 3 of the 4 can be any combination of Libra, Capricorn, Scorpio, and Sagittarius.

**Real production dependency, same caveat as Archetypes 1-5:** decorative until at least 4 (ideally all 6)
genuinely Scientific/Research/Analytical-flavored Under-Questlines exist across Aquarius, Gemini, Libra,
Capricorn, Scorpio, and Sagittarius — none written yet, and each still needs to go through the actual
`District_Under_Questline_Design_Method.md` process, not skip it.

### Archetype 7 — Caregiving / Vulnerable-Population Work

**Multi-district reach:** Strong = Cancer, Scorpio. Moderate = Taurus, Pisces. **4 of 13 districts** — the
smallest reachable pool of any archetype covered so far.

**Concept name:** *A Steady Hand*

**Idea:** the same portable-expertise logic — sustained emotional labor and trust-building with vulnerable
people reads the same regardless of which specific district's caregiving tradition it came from. A Cancer
nurse, a Scorpio trauma therapist, a Taurus family caregiver, and a Pisces community carer for burnouts/addicts
all recognize the same underlying steadiness in each other.

**Resolved 2026-07-26 — requirement:** Positive Reputation Matrix standing in **3 of the 4** reachable
districts, plus completion of one relevant Under-Questline in each of those 3 — **with at least one of Cancer
or Scorpio required as one of the 3**, since those are the archetype's only Strong-tier districts. Kept at the
same proportional strictness as the other archetypes (~60-67%) by explicit developer confirmation, even though
this produces the tightest bar of any archetype so far (only 1 of the 4 districts is ever optional).

**Real production dependency, same caveat as Archetypes 1-6:** decorative until at least 3 (ideally all 4)
genuinely Caregiving/Vulnerable-Population-Work-flavored Under-Questlines exist across Cancer, Scorpio,
Taurus, and Pisces — none written yet, and each still needs to go through the actual
`District_Under_Questline_Design_Method.md` process, not skip it.

### Archetype 8 — Working With Animals — No Entry

**No "Portable Expertise" concept for this archetype.** Per `SOC_Cross_Category_District_Matching.md`,
Working With Animals has **zero Strong or Moderate matches** anywhere — only Present-but-minor (Sagittarius,
Cancer, Taurus), reflecting the already-flagged fact that Inner Tepenia's Antarctic setting doesn't establish
meaningful animal populations anywhere in current canon. "Portable Expertise" specifically depends on having
real Strong/Moderate institutional pull in multiple districts for the expertise to travel *between* — with
none of that here, there's nothing for this concept to build on. Same gap already noted in
`SOC_Archetype_Perk_Brainstorm.md`'s own Archetype 8 entry. Not resolved by inventing a concept anyway; held
open pending either richer animal-population lore or a deliberate decision to leave this archetype without
any perk at all.

### Archetype 9 — Outdoor / Elements-Exposed Work

**Multi-district reach:** Strong = Sagittarius, Capricorn. Moderate = Aries. **3 of 13 districts.**

**Concept name:** *No Stranger to the Cold*

**Idea:** the same portable-expertise logic — sustained tolerance for weather/terrain exposure as a working
condition reads the same regardless of which district it was earned in. A Sagittarius frontier scout, a
Capricorn Yards worker exposed in the partially-exterior fabrication grounds, and an Aries technician built
for extreme heat/cold tolerance all share the same hardened relationship to the elements. Deliberately kept
identity/recognition-flavored rather than a fresh numeric bonus, since Frontier Survival and Cold Adaptation
already cover the mechanical side of cold tolerance.

**Resolved 2026-07-26 — requirement:** Positive Reputation Matrix standing in **specifically both Sagittarius
and Capricorn** (not an "any 2 of 3" pick), plus completion of one relevant Under-Questline in each of those
two — **Aries is not required and does not substitute for either.** A tighter, more specific bar than the
"any N of M with at least one Strong-tier" pattern used for the other archetypes, since both of this
archetype's Strong-tier districts are being required outright rather than treated as interchangeable options.

**Real production dependency, same caveat as Archetypes 1-7:** decorative until genuinely
Outdoor/Elements-Exposed-Work-flavored Under-Questlines exist in both Sagittarius and Capricorn — neither
written yet, and each still needs to go through the actual `District_Under_Questline_Design_Method.md`
process, not skip it.

### Archetype 10 — Vehicle / Heavy Equipment Operator (reframed as repair, not operation)

**Multi-district reach:** Strong = Sagittarius. Moderate = Capricorn, Aries, Hub. **4 of 13 districts.**

**Reframing, 2026-07-26:** the archetype's original "operator" framing runs into the same standing
turn-based-format caveat as the Piloting skill — Inner Tepenia has no in-context moment where the player
actually drives a vehicle. Per the developer's direct correction, this concept is reframed around **fixing
and repairing** vehicles and heavy equipment instead of operating them — a real mechanical context via the
Repair skill and existing maintenance systems, rather than flavor-only until Outer Tepenia.

**Concept name:** *One Set of Hands, Any Rig*

**Idea:** the trained eye for diagnosing and fixing vehicles and heavy equipment specifically — Rastras,
industrial machinery, transit systems — reads the same regardless of which district's fleet it was learned
on. A Sagittarius caravan mechanic, a Capricorn industrial-equipment technician, an Aries heavy-equipment
maintainer, and a Hub transit-system repair worker all share the same specific hands-on competence.

**Differentiation from Archetype 3 (Skilled Manual Trade):** that archetype covers general hands-on trade
work — construction, metalwork, industrial engineering broadly. This one is deliberately narrower and
specifically vehicle/heavy-equipment-flavored, the same way Precision Technical Support (Archetype 14) carves
its own niche out of Clerical (Archetype 12) rather than duplicating it.

**Resolved 2026-07-26 — requirement:** Positive Reputation Matrix standing in **3 of the 4** reachable
districts, plus completion of one relevant Under-Questline in each of those 3 — **with Sagittarius required as
one of the 3**, since it's the archetype's only Strong-tier district. The other 2 of the 3 can be any
combination of Capricorn, Aries, and Hub.

**Real production dependency, same caveat as Archetypes 1-7 and 9:** decorative until at least 3 (ideally all
4) genuinely Vehicle/Heavy-Equipment-Repair-flavored Under-Questlines exist across Sagittarius, Capricorn,
Aries, and Hub — none written yet, and each still needs to go through the actual
`District_Under_Questline_Design_Method.md` process, not skip it.

### Archetype 11 — Creative / Expressive Occupations

**Multi-district reach:** Strong = Leo, Pisces. Moderate = Sagittarius, Gemini. **4 of 13 districts** — same
size pool as Archetype 7 (Caregiving), which also landed on 3 of 4.

**Concept name:** *An Audience Anywhere*

**Idea:** the same portable-expertise logic — the instinct for public creation and audience/craft-oriented
identity reads the same regardless of which district's creative tradition it came from. A Leo performer, a
Pisces illusion-artist/dream-weaver, a Sagittarius storyteller, and a Gemini writer/journalist all recognize
the same underlying creative instinct in each other.

**Resolved 2026-07-26 — requirement:** Positive Reputation Matrix standing in **3 of the 4** reachable
districts, plus completion of one relevant Under-Questline in each of those 3 — **with at least one of Leo or
Pisces required as one of the 3**, since those are the archetype's only Strong-tier districts. The other 2 of
the 3 can be any combination of Sagittarius and Gemini.

**Real production dependency, same caveat as Archetypes 1-7, 9, and 10:** decorative until at least 3
(ideally all 4) genuinely Creative/Expressive-flavored Under-Questlines exist across Leo, Pisces, Sagittarius,
and Gemini — none written yet, and each still needs to go through the actual
`District_Under_Questline_Design_Method.md` process, not skip it.

### Archetype 12 — Clerical / Information-Processing / Office-Based

**Multi-district reach:** Strong = Libra, Gemini. Moderate = Capricorn, Virgo, Hub. **5 of 13 districts** —
same size pool as Archetypes 3, 4, and 5, which all landed on 3 of 5.

**Concept name:** *Every Ledger Reads the Same*

**Idea:** the same portable-expertise logic — precision, recordkeeping, and systems-literacy read as
legitimate expertise regardless of which district's paperwork it was trained on. A Libra bureaucratic
administrator, a Gemini Arcanet/information clerk, a Capricorn production-records auditor, a Virgo
documentation specialist, and a Hub transit-records coordinator all recognize the same underlying rigor in
each other's work.

**Resolved 2026-07-26 — requirement:** Positive Reputation Matrix standing in **3 of the 5** reachable
districts, plus completion of one relevant Under-Questline in each of those 3 — **with at least one of Libra
or Gemini required as one of the 3**, since those are the archetype's only Strong-tier districts. The other 2
of the 3 can be any combination of Capricorn, Virgo, and Hub.

**Real production dependency, same caveat as Archetypes 1-7 and 9-11:** decorative until at least 3 (ideally
all 5) genuinely Clerical/Information-Processing-flavored Under-Questlines exist across Libra, Gemini,
Capricorn, Virgo, and Hub — none written yet, and each still needs to go through the actual
`District_Under_Questline_Design_Method.md` process, not skip it.

### Archetype 13 — Sales / Persuasion-Based

**Multi-district reach:** Strong = Pisces, Sagittarius. Moderate = Leo, Gemini, Hub. **5 of 13 districts** —
same pool size as Archetypes 3, 4, 5, and 12, which all landed on 3 of 5.

**Concept name:** *A Deal's a Deal, Anywhere*

**Idea:** the same portable-expertise logic — negotiation instinct and rapport-building read the same
regardless of which district's market it was learned in. A Pisces black-market dealer, a Sagittarius caravan
trader, a Leo arena promoter, a Gemini information broker, and a Hub merchant all recognize the same closer's
instinct in each other.

**Resolved 2026-07-26 — requirement:** Positive Reputation Matrix standing in **3 of the 5** reachable
districts, plus completion of one relevant Under-Questline in each of those 3 — **with at least one of Pisces
or Sagittarius required as one of the 3**, since those are the archetype's only Strong-tier districts. The
other 2 of the 3 can be any combination of Leo, Gemini, and Hub.

**Real production dependency, same caveat as Archetypes 1-7 and 9-12:** decorative until at least 3 (ideally
all 5) genuinely Sales/Persuasion-flavored Under-Questlines exist across Pisces, Sagittarius, Leo, Gemini, and
Hub — none written yet, and each still needs to go through the actual
`District_Under_Questline_Design_Method.md` process, not skip it.

### Archetype 14 — Precision Technical Support

**Multi-district reach:** Strong = Aquarius. Moderate = Cancer, Scorpio, Capricorn, Virgo. **5 of 13
districts** — same pool size as Archetypes 3, 4, 5, 12, and 13, which all landed on 3 of 5.

**Concept name:** *The Steady Second*

**Idea:** the same portable-expertise logic — deep domain literacy and exacting precision in service of
someone else's licensed judgment call reads the same regardless of which district's senior professionals it
was practiced under. An Aquarius lab assistant, a Cancer nursing assistant, a Scorpio confession-recording
archivist, a Capricorn quality-control auditor, and a Virgo systems analyst all share the same "I make the
expert's work possible" identity.

**Resolved 2026-07-26 — requirement:** Positive Reputation Matrix standing in **3 of the 5** reachable
districts, plus completion of one relevant Under-Questline in each of those 3 — **with Aquarius required as
one of the 3**, since it's the archetype's only Strong-tier district (same situation as Archetype 4's Aries).
The other 2 of the 3 can be any combination of Cancer, Scorpio, Capricorn, and Virgo.

**Real production dependency, same caveat as Archetypes 1-7 and 9-13:** decorative until at least 3 (ideally
all 5) genuinely Precision-Technical-Support-flavored Under-Questlines exist across Aquarius, Cancer, Scorpio,
Capricorn, and Virgo — none written yet, and each still needs to go through the actual
`District_Under_Questline_Design_Method.md` process, not skip it.

---

**Concept 4 development complete, 2026-07-26.** All 14 archetypes have now been worked through: 13 with a
full Portable Expertise concept and requirement, and Archetype 8 (Working With Animals) explicitly given no
entry due to lacking any Strong/Moderate district match to build portability from. Every concept above remains
unbuilt — each depends on Under-Questlines that don't exist yet, and every one of those still has to go
through the real `District_Under_Questline_Design_Method.md` process when the time comes, per the standing
`feedback_soc_tier_marking_additive_only` rule. Concepts 1, 2, 3, and 5 (the other cross-reference ideas above)
remain undeveloped past their initial sketch.

---

## Working Notes — Concept 1, Archetype by Archetype

**Scope, confirmed 2026-07-26:** unlike Concept 4 (which used an archetype's full Strong+Moderate reach),
Concept 1 focuses **exclusively on Strong-tier districts** for each archetype — the districts where that
archetype is genuinely, unambiguously part of the district's own identity, not just present. Archetypes whose
Strong tier has zero or one district get correspondingly thin (or no) entries here; this is expected, not a
gap to force-fill.

### Archetype 1 — Supervisor / Foreman

**Strong-tier districts:** Capricorn, Aries, Virgo (3).

- **Capricorn-flavored:** guild-formal, merit-earned rank — a foreman here embodies the spire-system
  meritocracy itself; recognition is tied to demonstrated output and earned rank, read through the same
  "status lighting" logic the district applies to everything else. NPCs expect the player to *prove* the old
  authority still holds, not just claim it.
- **Aries-flavored:** barracks/crew-loyalty — a foreman here embodies "running hot" and crew-first loyalty
  superseding everything else; recognition comes from having led people through danger, not from a title.
  NPCs respond to demonstrated toughness/decisiveness rather than rank.
- **Virgo-flavored:** quiet, uncelebrated competence — a foreman here embodies the district's own "we keep
  you alive and get no thanks for it" culture; recognition is subdued, almost reluctant, extended by other
  Virgo workers who recognize the same exhausted reliability in a newcomer rather than by any formal signal.

### Archetype 2 — Licensed / Credentialed Professional

**Strong-tier districts:** Cancer, Libra, Scorpio, Capricorn (4). This is the same archetype used as the
original illustrative example when Concept 1 was first floated — that early sketch covered three of the four;
Capricorn completes the set here.

- **Cancer-flavored** *(from the original sketch)*: warm, community-embedded — NPCs read the credential as
  trustworthiness and care, extending informal access the way Cancer's own "doors are always unlocked" culture
  works.
- **Libra-flavored** *(from the original sketch)*: formal, procedural — NPCs read the credential as
  institutional legitimacy, opening doors gated by rank/protocol rather than by warmth.
- **Scorpio-flavored** *(from the original sketch)*: intense, confrontational — NPCs read the credential as
  evidence of having survived or administered something difficult; doors open through demonstrated toughness,
  not paperwork.
- **Capricorn-flavored** *(new)*: guild-rank as credential — a master engineer's apprenticeship-earned status
  reads the same way Capricorn reads any other earned rank; recognition comes from demonstrated technical
  mastery within the guild system, distinct from Archetype 1's Capricorn flavor (that one is about crew
  leadership; this one is about engineering/technical expertise specifically).

### Archetype 3 — Skilled Manual Trade

**Strong-tier districts:** Capricorn, Virgo, Aries (3) — the same three as Archetype 1, but this is about
hands-on trade competence itself, not leadership, so the flavors read differently.

- **Capricorn-flavored:** guild-craft mastery — recognition tied to the actual demonstrated trade skill itself
  (welding, machining, assembly), the concrete hands-on output that earns spire advancement in the first
  place, distinct from Archetype 1's Capricorn flavor (crew leadership) and Archetype 2's (credentialed
  engineering rank).
- **Aries-flavored:** hands-on survival-engineering — recognition tied to keeping equipment running under
  extreme, dangerous conditions; the "push it until it breaks, then fix it" culture applied to the trade
  itself rather than to crew command.
- **Virgo-flavored:** invisible-infrastructure mastery — recognition tied to knowing every pipe, junction, and
  system by feel; the deep tactile expertise that comes from years of working in low light, navigating by
  touch as much as sight.

### Archetype 4 — Uniformed / Disciplined Service

**Strong-tier districts:** Aries only (1) — a single-district case, no cross-district variation to work
against; confirmed as-is rather than force-fitting additional flavor comparisons that wouldn't mean anything.

- **Aries-flavored:** barracks/shift-crew discipline — the "warrior-engineer" identity forged in wartime;
  recognition tied to having endured and served within the district's own quasi-military chain-of-command
  structure specifically, distinct from Archetype 1's Aries flavor (leadership through demonstrated toughness)
  and Archetype 3's (hands-on survival-engineering) — this one is about institutional discipline and
  obedience to structure itself, not leadership or trade skill.

### Archetype 5 — Direct Public-Facing / Customer Service

**Strong-tier districts:** Leo, Hub (2)

- **Leo-flavored:** performance-as-service — the district's own "no audience/performer distinction" applied
  directly to customer interaction; NPCs read the player as putting on a show for them, not merely serving
  them — service itself becomes a kind of performance.
- **Hub-flavored:** professional neutrality — the Hub-born "adaptability"/professional-detachment culture
  applied to customer service; NPCs read the player as someone who serves everyone equally well without
  favoring any single district's own cultural norms, the trained even-handedness of someone who's dealt with
  every kind of person passing through.

### Archetype 6 — Scientific / Research / Analytical

**Strong-tier districts:** Aquarius, Gemini (2)

- **Aquarius-flavored:** visionary/experimental — the district's own "certain, not malicious" idealism applied
  to analytical thinking; recognition tied to genuine intellectual ambition and a willingness to pursue a
  breakthrough idea regardless of where it leads, the "trying to save the world" instinct read as a research
  posture.
- **Gemini-flavored:** speed-over-rigor — the district's own "faster is better" information culture applied to
  analysis; recognition tied to being able to synthesize and triangulate information quickly under a flood of
  competing, contradictory data — a genuinely different analytical instinct from Aquarius's slower,
  idealism-driven research approach.

### Archetype 7 — Caregiving / Vulnerable-Population Work

**Strong-tier districts:** Cancer, Scorpio (2)

- **Cancer-flavored:** nurturing/maintaining — the district's own "the dead are maintained, not just
  remembered" caregiving philosophy; recognition tied to sustained, gentle presence — the kind of care that
  shows up every day without being asked, never dramatic, always there.
- **Scorpio-flavored:** confrontational/transformative — the district's own "the only way through is through"
  caregiving philosophy; recognition tied to a willingness to sit with someone through genuine darkness or
  crisis rather than softening it — care expressed through honest confrontation rather than gentleness, the
  opposite instinct from Cancer's own approach.

**Archetype 8 (Working With Animals) — skipped, per its established no-entry status** (no Strong-tier
districts at all; see Concept 4's own Archetype 8 note above for the full explanation).

### Archetype 9 — Outdoor / Elements-Exposed Work

**Strong-tier districts:** Sagittarius, Capricorn (2)

- **Sagittarius-flavored:** existential/mortality-aware — the district's own "the cold is never abstract, it's
  lethal" identity; recognition tied to a hardened, matter-of-fact relationship with mortality itself, a
  philosophical weight to the exposure that goes beyond mere tolerance.
- **Capricorn-flavored:** industrial-exposure/output-driven — the district's own partially-exterior
  fabrication-yard identity; recognition tied to enduring exposure specifically in service of production
  output, a more utilitarian relationship to the cold than Sagittarius's existential one — you endure it
  because the work demands it, not because survival itself is the philosophy.

### Archetype 10 — Vehicle / Heavy Equipment Operator (repair-reframed)

**Strong-tier districts:** Sagittarius only (1) — another single-district case, no cross-district variation
to work against; confirmed as-is rather than force-fitting additional flavor comparisons that wouldn't mean
anything.

- **Sagittarius-flavored:** caravan/expedition-fleet repair — recognition tied specifically to keeping
  frontier vehicles and equipment running far from any proper depot, resourceful improvised fixes made under
  real logistical pressure and distance from support. Distinct from Archetype 9's Sagittarius flavor (the
  philosophical/existential relationship to cold exposure broadly) — this one is narrowly about keeping the
  caravan's actual machinery moving.

### Archetype 11 — Creative / Expressive Occupations

**Strong-tier districts:** Leo, Pisces (2)

- **Leo-flavored:** grand/spectacle performance — the district's own "grand vs. intimate" tradition (rooted in
  the historical Star War between rival performance houses); recognition tied to large-scale, audience-facing
  showmanship, holding a crowd's attention as a demonstrated craft.
- **Pisces-flavored:** illusion/dissolution-as-art — the district's own syncretic dream-tech aesthetic, where
  art blurs the boundary between self and other, real and unreal, rather than performing for a crowd in any
  traditional sense; a far more intimate, disorienting creative mode than Leo's showmanship.

### Archetype 12 — Clerical / Information-Processing / Office-Based

**Strong-tier districts:** Libra, Gemini (2)

- **Libra-flavored:** procedural/formal recordkeeping — the district's own institutional bureaucracy;
  recognition tied to precision within a formal review/approval process, patience with slow, layered systems
  built specifically to prevent hasty mistakes.
- **Gemini-flavored:** rapid-verification/triangulation — the district's own "every story has two versions"
  information culture; recognition tied to quickly sorting signal from noise across competing, contradictory
  data streams — a genuinely different clerical skill from Libra's slow procedural rigor, speed over
  ceremony.

### Archetype 13 — Sales / Persuasion-Based

**Strong-tier districts:** Pisces, Sagittarius (2)

- **Pisces-flavored:** information-and-secrets economy — the district's own "every transaction of consequence
  requires sharing something true about yourself" trade philosophy; recognition tied to negotiating in a
  currency of secrets and vulnerability, not just goods or credits.
- **Sagittarius-flavored:** frontier trade/storytelling-as-pitch — the district's own storytelling-as-social-
  currency tradition; recognition tied to using narrative and reputation ("a story doesn't need to be
  literally true to be valuable about something") as the actual instrument of a sale, distinct from Pisces's
  secrets-based negotiation.

### Archetype 14 — Precision Technical Support

**Strong-tier districts:** Aquarius only (1) — another single-district case, same as Archetypes 4 and 10.

- **Aquarius-flavored:** experimental-support/lab-assistant — recognition tied to supporting genuinely
  cutting-edge, sometimes unstable research work; distinct from Archetype 6's Aquarius flavor (that one is
  about *being* the visionary researcher) — this one is about being the steady hands that make someone else's
  visionary, occasionally reckless research actually survivable.

---

**Concept 1 development complete, 2026-07-26.** All 14 archetypes worked through, Strong-tier districts only:
Archetype 8 (Working With Animals) skipped per its established no-entry status, Archetypes 4, 10, and 14
given single-district entries (no cross-district comparison possible, confirmed as fine rather than
force-fitting), and the remaining 10 archetypes each given 2-4 district-flavored variants. Every variant above
is a concept sketch, not locked design — none of it has been built, and the same standing rule applies as
everywhere else in this file: any of this feeding into a real Under-Questline, Sidequest, or perk still goes
through the actual established design methods, not this document. Concepts 2, 3, and 5 remain at their
original sketch stage, undeveloped further.

