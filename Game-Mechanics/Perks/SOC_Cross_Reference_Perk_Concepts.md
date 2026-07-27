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

**Status: this is the concept being developed next, archetype by archetype.** See the working notes below as
they're produced.

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


