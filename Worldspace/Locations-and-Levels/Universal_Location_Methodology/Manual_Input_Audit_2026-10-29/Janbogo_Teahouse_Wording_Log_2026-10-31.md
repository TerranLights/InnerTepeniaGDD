# Janbogo — teahouse wording: change log (2026-10-31)

**Rule:** `/home/kuroskalacs/Documents/Doll-Fi/media/y-files/session-instructions/Janbogo - not a city of teahouses.md` (author, binding). **Plan and inventory:** `Janbogo_Teahouse_Wording_Plan_2026-10-30.md`.

**How this session works (developer's request, 2026-10-30): the fixes are done together, with the developer awake, 05:00–14:59.**
For each file, in the order below:
1. I print the exact current lines and my drafted replacement.
2. The developer approves or changes the wording.
3. I apply it with the file's line count preserved and the edited file read back.
4. I record here the verbatim before and after, the time, and the approval. Nothing is logged as done before it is applied and read back.
5. The edited files carry no "[removed]", "formerly" or changelog text; this log is the only record.

At the end: the author's grep (`grep -rniE "teahouse city|city of teahouses|teahouse culture|teahouse tradition" --include=*.md .`), the sheet verifier, and a list of which files changed. Commit only when the developer says.

## Open questions to confirm before editing (from the plan, section C)
| # | Question | Default if not changed | Answer |
|---|---|---|---|
| 1 | Hours | Apply in the 05:00–14:59 window, together | yes (07:17, in the window; together) |
| 2 | The developer's own concern quoted in `Phase_7` L21, the sweep, `OBSERVATIONS` L1426 and `00b` L97 ("Janbogo [cannot be] an entire city of teahouses") | Remove that example from each list; keep the Zhongshan and Cape Adare examples | developer: the Zhongshan lake stays (a physical geological feature that exists whoever lives there) and the Cape Adare hut stays; only the Janbogo example is removed (confirm when we reach each file) |
| 3 | `Inspirational-Influences.md` PRIMARY pick "Central Asian chaykhana (teahouse) tradition" (copied into the pass's `Step_3`) | Leave | leave |
| 4 | Files outside the Janbogo run (vision notes, neo-race catalogs, Zukelli's culture files, Casey catalog, Concordia refugee-diaspora composition file, DLC questline candidates) | Handle later; megasheets, Background-Lore and the Run 9 archive are never edited | later |

## Order of work
| # | File | Lines | Status | Approved | Applied | Read back |
|---|---|---|---|---|---|---|
| 1 | `Local_Cultures/Janbogo_Subnet/Janbogo.md` (read last at Step 5; the author's "main one"; 30 tea-related lines) | batches 1–3 done (29 lines changed across 3 batches); the author's grep finds nothing left in this file | ✅ done | batches 1–3 | batch 3 at 07:41 | yes |
| 2 | `Local_Robot_Culture/Janbogo_Subnet/Janbogo.md` (13 tea-related lines) | L38, L57, L72, L100, L101, L103, L107, L184, L230, L234, L244, L273 (L162, L176, L207, L40 left: tea paired with coffee, Majyao's music, the chaykhana source) | ✅ done | yes | 07:44 | yes |
| 3 | Spec `Specs/Janbogo subnet/Janbogo.md` (stays 219 lines) | L123, L149, L151, L153, L167, L175, L178, L214 (07:57); L205, and Aquarius→Taurus at L175 and L191 (08:01) | ✅ done | yes | 08:01 | yes |
| 4 | `Division_of_Industry/16_Per_City_Three_Tier_Run.md` §28 | L2882, L2885, L2890 (the last also Aquarius→Taurus) | ✅ done | yes | 08:02 | yes |
| 5 | `Division_of_Industry_Sweep_2026-08-31.md` | L72–75 | ✅ done | yes | 08:06 | yes |
| 6 | `Universal_Location_Methodology/Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` | L1426, L1703–1704 | ✅ done | yes | 08:08 | yes |
| 7 | `Concordia-City/Districts/Phase_Instructions/00b_General_Population_Discipline.md` | L97 | ✅ done | yes | 08:08 | yes |
| 8 | Pass `Datasheets/Phase_7.md` | L20 edited, L21 row removed | ✅ done | yes | 08:12 | yes |
| 9 | Pass `Datasheets/Phase_8.md` | L12 (re-counted against the edited spec) | ✅ done | yes | 08:12 | yes |
| 10 | Pass `Datasheets/Step_3.md` | L11 | ✅ no change (question 3: leave) | yes | — | — |
| 11 | Re-run the grep and the verifier; report which files changed | — | ⏳ | | | |

Already done: Pass `00.0_Pre-Trip_Inspection.md` L27 — "Majyao's teahouse" → "the teahouse Majyao ran (it has no name yet)" (2026-10-30, ~18:00).

## Change record
*(Filled in during the session: file · line · verbatim before · verbatim after · time · approval.)*

### File 1 · `Local_Cultures/Janbogo_Subnet/Janbogo.md` · Batch 1 (Part I and §5) · applied 07:32, approved by the developer ("this series of edits works much better, yes") · file still 330 lines (`wc -l`) · read back OK

**L26 — before**
```text
*Janbogo is Tepenia's clearest case of a founding-era civic template surviving its own demographic minority status. Unified Korea founded the city, gave it its name, and set its earliest civic institutions in place — teahouses, communal warmth, the instinct to make daily life worth living under difficult conditions, all worked out independently by the founding population out of the city's own circumstances. But over roughly two and a half centuries, the sheer scale of Chinese and American emigration potential outweighed Korea's smaller founding population, and China and USA became the numerically dominant lineages. The culture did not follow the numbers. It stayed exactly as it was built. People whose ancestry is Chinese, American, Japanese, German — the demographic majority of the city — grew up inside a civic identity that was never theirs by blood and is now inarguably theirs by practice.*
```
**L26 — after**
```text
*Janbogo is Tepenia's clearest case of a founding-era civic template surviving its own demographic minority status. Unified Korea founded the city, gave it its name, and set its earliest civic institutions in place — tea, hospitality, communal warmth, the instinct to make daily life worth living under difficult conditions, all worked out independently by the founding population out of the city's own circumstances. But over roughly two and a half centuries, the sheer scale of Chinese and American emigration potential outweighed Korea's smaller founding population, and China and USA became the numerically dominant lineages. The culture did not follow the numbers. It stayed exactly as it was built. People whose ancestry is Chinese, American, Japanese, German — the demographic majority of the city — grew up inside a civic identity that was never theirs by blood and is now inarguably theirs by practice.*
```

**L36 — before**
```text
The founding population built the teahouse tradition almost immediately, developing it independently out of the environment's own harsh demands: a reason to gather, warmth that had to be built rather than assumed, care expressed through the ritual of hosting rather than through words. *(The form happens to echo real-world Korean tea-house tradition — a coincidence of convergent development given the founding population's own background, not a direct transplant.)* This was the template. Every later arrival — Chinese, American, Japanese, German, Italian, Southeast Asian — arrived into a city where the answer to "how do we survive this place together" had already been worked out, and it looked like a teahouse.
```
**L36 — after**
```text
The founding population built its tradition of tea, hospitality and togetherness almost immediately, developing it independently out of the environment's own harsh demands: a reason to gather, warmth that had to be built rather than assumed, care expressed through the ritual of hosting rather than through words. *(The form happens to echo real-world Korean tea and hosting traditions — a coincidence of convergent development given the founding population's own background, not a direct transplant.)* This was the template. Every later arrival — Chinese, American, Japanese, German, Italian, Southeast Asian — arrived into a city where the answer to "how do we survive this place together" had already been worked out, and it looked like hosting.
```

**L46 — before**
```text
This produces a specific psychology: the sharp, immediate line between exterior danger and interior sanctuary. Unlike Concordia, where cold is a constant, ambient pressure, Janbogo's threat is episodic and violent — a katabatic event can turn a manageable walk into an emergency in minutes. The result is a culture that takes shelter seriously not as comfort but as the precondition for being alive at all. The teahouse tradition is, at its root, a response to this: if the outside world is going to try to kill you without warning, the inside world had better be worth surviving for.
```
**L46 — after**
```text
This produces a specific psychology: the sharp, immediate line between exterior danger and interior sanctuary. Unlike Concordia, where cold is a constant, ambient pressure, Janbogo's threat is episodic and violent — a katabatic event can turn a manageable walk into an emergency in minutes. The result is a culture that takes shelter seriously not as comfort but as the precondition for being alive at all. The culture of hospitality and togetherness is, at its root, a response to this: if the outside world is going to try to kill you without warning, the inside world had better be worth surviving for.
```

**L54 — before**
```text
Polar night runs roughly May 20 to July 23 — about 64 days, shorter than Concordia's 82, but coinciding with the year's most intense katabatic season. This is Janbogo's hardest stretch: total darkness layered on top of the worst wind of the year. The teahouses fill. Outdoor life effectively stops except for what the supply route to Concordia demands, and even that runs on tight, wind-monitored windows.
```
**L54 — after**
```text
Polar night runs roughly May 20 to July 23 — about 64 days, shorter than Concordia's 82, but coinciding with the year's most intense katabatic season. This is Janbogo's hardest stretch: total darkness layered on top of the worst wind of the year. The shared interior spaces fill. Outdoor life effectively stops except for what the supply route to Concordia demands, and even that runs on tight, wind-monitored windows.
```

**L68 — before**
```text
**Name/concept:** *Inherited Warmth, Owned Completely* — colloquially, *the Teahouse City*
```
**L68 — after**
```text
**Name/concept:** *Inherited Warmth, Owned Completely*
```

**L70 — before**
```text
Janbogo's culture is built on an inversion most cities never have to reckon with: the people who founded it are no longer most of the people who live there, and the culture never noticed the difference. The teahouse as social infrastructure, hospitality as the highest form of care, the instinct to make ordinary life worth living under hard conditions — the founding population's own institution was so completely internalized by every wave of arrivals that it was never anyone's borrowed tradition to begin with. It simply became "Janbogo." A fourth-generation Chinese-descended Janbogo resident does not feel like a guest in someone else's tradition. They feel like they're home, because they are.
```
**L70 — after**
```text
Janbogo's culture is built on an inversion most cities never have to reckon with: the people who founded it are no longer most of the people who live there, and the culture never noticed the difference. Tea and hosting as social infrastructure, hospitality as the highest form of care, the instinct to make ordinary life worth living under hard conditions — the founding population's own tradition was so completely internalized by every wave of arrivals that it was never anyone's borrowed tradition to begin with. It simply became "Janbogo." A fourth-generation Chinese-descended Janbogo resident does not feel like a guest in someone else's tradition. They feel like they're home, because they are.
```

**L74 — before**
```text
- **a. Founding tension** — Korean identity is Janbogo's origin and template, but not its numbers. The tension isn't Koreans defending their culture from dilution — it's the reverse: descendants of the Korean founding population are keenly aware that the institution they originated is now carried forward mostly by people who aren't Korean at all, and there's a quiet, rarely-voiced question running underneath the city's warmth: *does it still count as ours if almost none of us are left to keep it?* The teahouse tradition answers this by simply continuing, unbothered by the question — which some Korean-descended residents find comforting and others find a little bit like grief.
```
**L74 — after**
```text
- **a. Founding tension** — Korean identity is Janbogo's origin and template, but not its numbers. The tension isn't Koreans defending their culture from dilution — it's the reverse: descendants of the Korean founding population are keenly aware that the institution they originated is now carried forward mostly by people who aren't Korean at all, and there's a quiet, rarely-voiced question running underneath the city's warmth: *does it still count as ours if almost none of us are left to keep it?* The tradition answers this by simply continuing, unbothered by the question — which some Korean-descended residents find comforting and others find a little bit like grief.
```

**L77 — before**
```text
  - The most visible fault line is invisible to outsiders: within Janbogo, there's a quiet, informal distinction between "old teahouse families" (regardless of ethnicity, families whose hosting lineage goes back to the founding generation or close to it) and everyone else. It has nothing to do with blood and everything to do with how many generations your family has been *making* the warmth rather than just receiving it.
```
**L77 — after**
```text
  - The most visible fault line is invisible to outsiders: within Janbogo, there's a quiet, informal distinction between "old hosting families" (regardless of ethnicity, families whose hosting lineage goes back to the founding generation or close to it) and everyone else. It has nothing to do with blood and everything to do with how many generations your family has been *making* the warmth rather than just receiving it.
```

### File 1 · `Local_Cultures/Janbogo_Subnet/Janbogo.md` · Batch 2 (§6–§14) · applied 07:39, approved by the developer ("everything else looks fine"; L102's first change dropped at the developer's direction: "Majyao really did run the single most famous teahouse in Tepenia") · file still 330 lines (`wc -l`) · read back OK

*Developer's design note, same session: in the eventual future design, make sure to include teaware in the setting (L152 keeps "ceramics (particularly teaware)").*

**L90 — before**
```text
- **d. Public/private divide** — Comparatively thin. Janbogo's warmth culture extends deep into what other cities would consider private — neighbors check on neighbors, teahouse keepers know regulars' troubles, community involvement in individual hardship is expected rather than intrusive. This is not gossip culture; it's care culture, and the city genuinely does not experience the two as the same thing.
```
**L90 — after**
```text
- **d. Public/private divide** — Comparatively thin. Janbogo's warmth culture extends deep into what other cities would consider private — neighbors check on neighbors, hosts know regulars' troubles, community involvement in individual hardship is expected rather than intrusive. This is not gossip culture; it's care culture, and the city genuinely does not experience the two as the same thing.
```

**L102 — before**
```text
- **Case study — Majyao Bisyugota:** Ran the single most famous teahouse in Tepenia, out of Janbogo, for years before relocating to Concordia. She is Chinese-descended, not Korean — her aesthetic is explicitly Chinese (qipao, Chinese lanterns, a musical sensibility built on Chinese traditional folk fused with Scandinavian avant-garde jazz), and her establishment served coffee alongside tea, not tea alone. She is, in one person, the entire thesis of Janbogo's culture: the demographic majority made itself the custodian of a founding tradition that was never its own by blood, and did it so completely that "Majyao's teahouse" became the nationally recognized symbol of Janbogo's own founding-era warmth tradition. Nobody in Tepenia who knew the teahouse thought to question that its keeper wasn't Korean. That is exactly how thoroughly the culture transcended its founding ethnicity.
```
**L102 — after**
```text
- **Case study — Majyao Bisyugota:** Ran the single most famous teahouse in Tepenia, out of Janbogo, for years before relocating to Concordia. She is Chinese-descended, not Korean — her aesthetic is explicitly Chinese (qipao, Chinese lanterns, a musical sensibility built on Chinese traditional folk fused with Scandinavian avant-garde jazz), and her establishment served coffee alongside tea, not tea alone. She is, in one person, a clear example of how Janbogo's culture works: the demographic majority made itself the custodian of a founding tradition that was never its own by blood, and did it so completely that her teahouse became one of the city's founding-era landmarks. Nobody in Tepenia who knew the teahouse thought to question that its keeper wasn't Korean. That is exactly how thoroughly the culture transcended its founding ethnicity.
```

**L108 — before**
```text
- **a. Primary language(s):** Korean persists as a heritage and ceremonial language, spoken fluently within old teahouse families and used in specific hosting rituals regardless of the host's ancestry. Mandarin and English (American-inflected) are the most widely spoken daily languages, reflecting the long-run demographic majority. Japanese, German, and Indonesian are meaningfully present within their communities.
```
**L108 — after**
```text
- **a. Primary language(s):** Korean persists as a heritage and ceremonial language, spoken fluently within old hosting families and used in specific hosting rituals regardless of the host's ancestry. Mandarin and English (American-inflected) are the most widely spoken daily languages, reflecting the long-run demographic majority. Japanese, German, and Indonesian are meaningfully present within their communities.
```

**L122 — before**
```text
Inside, the character inverts completely. Teahouses and communal interior spaces are where Janbogo's aesthetic investment concentrates: warm lighting, textiles, the deliberate softening of every hard edge the exterior architecture had to accept. Interior design principles established early by the founding population — low seating, warm wood tones where wood can be afforded, an emphasis on threshold spaces that transition gradually from outside to in rather than a single hard door — persist in teahouse design specifically, even in buildings built and run by non-Korean-descended families. *(The approach happens to echo real-world Korean domestic design — a coincidence of convergent development given the founders' own background, not a direct import.)* The threshold matters more in Janbogo than almost anywhere else in Tepenia: the physical and emotional distance between "the wind that wants to kill you" and "the warmth that's waiting" is the entire architectural point.
```
**L122 — after**
```text
Inside, the character inverts completely. Communal interior spaces are where Janbogo's aesthetic investment concentrates: warm lighting, textiles, the deliberate softening of every hard edge the exterior architecture had to accept. Interior design principles established early by the founding population — low seating, warm wood tones where wood can be afforded, an emphasis on threshold spaces that transition gradually from outside to in rather than a single hard door — persist in communal interior design specifically, even in buildings built and run by non-Korean-descended families. *(The approach happens to echo real-world Korean domestic design — a coincidence of convergent development given the founders' own background, not a direct import.)* The threshold matters more in Janbogo than almost anywhere else in Tepenia: the physical and emotional distance between "the wind that wants to kill you" and "the warmth that's waiting" is the entire architectural point.
```

**L128 — before**
```text
- **a. Human cuisine:** The founding population's own foodways form the base layer — communal stews, shared small dishes, and above all tea culture, later joined by coffee culture as the population diversified — developed independently out of the city's own founding-era needs for warmth and gathering. Later arrivals' own culinary traditions, reflecting the long-run demographic majority, sit alongside rather than displacing this — Janbogo's food culture is genuinely layered rather than fused into something new the way Zhongshan's own cuisine became one thing. You can get a meal built around the founding tea-and-stew tradition and one reflecting the city's demographic majority in the same neighborhood, sometimes the same establishment, and nobody considers this unusual. *(The layering happens to echo real-world Korean and Chinese foodways specifically, given the population's own origins — a coincidence of convergent development, not a direct transplant.)*
```
**L128 — after**
```text
- **a. Human cuisine:** The founding population's own foodways form the base layer — communal stews, shared small dishes, and tea culture, later joined by coffee culture as the population diversified — developed independently out of the city's own founding-era needs for warmth and gathering. Later arrivals' own culinary traditions, reflecting the long-run demographic majority, sit alongside rather than displacing this — Janbogo's food culture is genuinely layered rather than fused into something new the way Zhongshan's own cuisine became one thing. You can get a meal built around the founding tea-and-stew tradition and one reflecting the city's demographic majority in the same neighborhood, sometimes the same establishment, and nobody considers this unusual. *(The layering happens to echo real-world Korean and Chinese foodways specifically, given the population's own origins — a coincidence of convergent development, not a direct transplant.)*
```

**L138 — before**
```text
Practical, layered, wind-resistant — Janbogo clothing has to survive katabatic conditions, and the city's fashion sensibility treats function and warmth as inseparable from style rather than opposed to it. Layering principles established early by the founding population (functional under-layers, a more expressive and warmer outer layer meant to be seen once you're inside) persist broadly. *(The approach happens to echo real-world Korean layering traditions — a coincidence of convergent development, not a direct import.)* Interior wear, specifically teahouse and hosting attire, is where aesthetic expression concentrates — soft fabrics, warm colors, garments meant to be comfortable for long unhurried hours indoors. A Janbogo local's "good clothes" are almost always their indoor clothes, not their outdoor ones.
```
**L138 — after**
```text
Practical, layered, wind-resistant — Janbogo clothing has to survive katabatic conditions, and the city's fashion sensibility treats function and warmth as inseparable from style rather than opposed to it. Layering principles established early by the founding population (functional under-layers, a more expressive and warmer outer layer meant to be seen once you're inside) persist broadly. *(The approach happens to echo real-world Korean layering traditions — a coincidence of convergent development, not a direct import.)* Interior wear, specifically hosting attire, is where aesthetic expression concentrates — soft fabrics, warm colors, garments meant to be comfortable for long unhurried hours indoors. A Janbogo local's "good clothes" are almost always their indoor clothes, not their outdoor ones.
```

**L140 — before**
```text
*(Established 2026-07-05, developer vision session — see `City_Vision_Notes/Janbogo.md`.)* This same insulated-but-vivid principle extends across the whole city, not just teahouses: fashionable residents fill Janbogo's huge shielded indoor commercial and social spaces in richly colored, insulated outfits, developed independently out of the city's own indoor-warmth civic instinct rather than imported from anywhere in particular. *(The resulting look happens to echo real-world Chinese and French design sensibilities — a coincidence of convergent development given the population's own composition, not a direct import from either.)*
```
**L140 — after**
```text
*(Established 2026-07-05, developer vision session — see `City_Vision_Notes/Janbogo.md`.)* This same insulated-but-vivid principle extends across the whole city, not just hosting settings: fashionable residents fill Janbogo's huge shielded indoor commercial and social spaces in richly colored, insulated outfits, developed independently out of the city's own indoor-warmth civic instinct rather than imported from anywhere in particular. *(The resulting look happens to echo real-world Chinese and French design sensibilities — a coincidence of convergent development given the population's own composition, not a direct import from either.)*
```

**L146 — before**
```text
Warm, communal, meant to be experienced together rather than performed at a distance — folk traditions across the city's many communities (Korean, Chinese, Japanese, Indonesian, and others) are kept alive specifically as teahouse and hosting music, genres meant to accompany gathering rather than demand attention. Fusion is common and unforced: Majyao Bisyugota's own musical signature — Chinese traditional folk fused with Scandinavian avant-garde jazz — is a genuinely Janbogo phenomenon, sophisticated without losing its rootedness, experimental without abandoning warmth. The city produces music built to be played while people are talking to each other, not instead of it.
```
**L146 — after**
```text
Warm, communal, meant to be experienced together rather than performed at a distance — folk traditions across the city's many communities (Korean, Chinese, Japanese, Indonesian, and others) are kept alive specifically as hosting music, genres meant to accompany gathering rather than demand attention. Fusion is common and unforced: Majyao Bisyugota's own musical signature — Chinese traditional folk fused with Scandinavian avant-garde jazz — is a genuinely Janbogo phenomenon, sophisticated without losing its rootedness, experimental without abandoning warmth. The city produces music built to be played while people are talking to each other, not instead of it.
```

**L152 — before**
```text
- **Visual arts:** Domestic and craft-oriented rather than gallery-oriented — textiles, ceramics (particularly teaware), and interior design are where Janbogo's visual culture concentrates its seriousness, consistent with a city whose aesthetic center of gravity is the inside of a teahouse rather than a museum wall.
```
**L152 — after**
```text
- **Visual arts:** Domestic and craft-oriented rather than gallery-oriented — textiles, ceramics (particularly teaware), and interior design are where Janbogo's visual culture concentrates its seriousness, consistent with a city whose aesthetic center of gravity is the inside of a shared interior rather than a museum wall.
```

**L154 — before**
```text
- **Literature:** A strong oral and anecdotal tradition — stories about specific teahouses, specific hosts, specific acts of unexpected kindness during hard winters — carried forward more through speech and community memory than published work. What written literature exists tends toward the personal and warm rather than the abstract. **Confirmed 2026-07-05:** Janbogo is also one of the Tepenian cities whose libraries openly welcome smuggled Upper Earth books, part of a broader national practice (also confirmed at Zukelli and Esperanza).
```
**L154 — after**
```text
- **Literature:** A strong oral and anecdotal tradition — stories about specific places, specific hosts, specific acts of unexpected kindness during hard winters — carried forward more through speech and community memory than published work. What written literature exists tends toward the personal and warm rather than the abstract. **Confirmed 2026-07-05:** Janbogo is also one of the Tepenian cities whose libraries openly welcome smuggled Upper Earth books, part of a broader national practice (also confirmed at Zukelli and Esperanza).
```

**L164 — before**
```text
- **Smell:** Brewing tea and coffee everywhere, layered with the cold mineral smell of the bay and sea spray; woodsmoke or heating elements in older teahouse buildings; the specific ozone-and-ice smell that follows a katabatic event once it passes.
```
**L164 — after**
```text
- **Smell:** Brewing tea and coffee everywhere, layered with the cold mineral smell of the bay and sea spray; woodsmoke or heating elements in older buildings; the specific ozone-and-ice smell that follows a katabatic event once it passes.
```

### File 1 · `Local_Cultures/Janbogo_Subnet/Janbogo.md` · Batch 3 (§15–§32) · applied 07:41, approved by the developer ("all looks good"; L330 softened to "one of") · file still 330 lines (`wc -l`) · read back OK

**L182 — before**
```text
- Hospitality / communal services: ~15% — an unusually large sector for any Tepenian city, reflecting the centrality of teahouses and hosting institutions to the local economy, not just the culture
```
**L182 — after**
```text
- Hospitality / communal services: ~15% — an unusually large sector for any Tepenian city, reflecting the centrality of hospitality and hosting institutions to the local economy, not just the culture
```

**L198 — before**
```text
Robot residents gravitate toward the hospitality and logistics sectors that define the city's economy — teahouse keeping, coffee service, and the supply/shipping work tied to the polynya and Hwy 183. The warmth-through-action ethos suits robot residents particularly well: care expressed through competent, attentive service rather than through emotionally demonstrative language maps naturally onto how many robots already prefer to express solidarity and affection.
```
**L198 — after**
```text
Robot residents gravitate toward the hospitality and logistics sectors that define the city's economy — tea and coffee service, and the supply/shipping work tied to the polynya and Hwy 183. The warmth-through-action ethos suits robot residents particularly well: care expressed through competent, attentive service rather than through emotionally demonstrative language maps naturally onto how many robots already prefer to express solidarity and affection.
```

**L239 — before**
```text
Complicated by a layered history rather than a single clean grievance. The founding exile population carries the accumulated weight of the anti-robot sentiment that produced the Falkland Treaty exile in the first place. Later Chinese and American-descended residents carry their own, separate relationships to whatever drove their ancestors' emigration. The city's dominant public attitude is less about Upper Earth directly and more about defiant continuation — the teahouse tradition, deliberately kept alive and deliberately shared regardless of ancestry, reads as an implicit answer to exile: *you tried to erase where we came from; we made it something everyone wanted to keep.*
```
**L239 — after**
```text
Complicated by a layered history rather than a single clean grievance. The founding exile population carries the accumulated weight of the anti-robot sentiment that produced the Falkland Treaty exile in the first place. Later Chinese and American-descended residents carry their own, separate relationships to whatever drove their ancestors' emigration. The city's dominant public attitude is less about Upper Earth directly and more about defiant continuation — the tradition of tea, hospitality and togetherness, deliberately kept alive and deliberately shared regardless of ancestry, reads as an implicit answer to exile: *you tried to erase where we came from; we made it something everyone wanted to keep.*
```

**L261 — before**
```text
- Hosting culture itself — Janbogo-trained or Janbogo-influenced teahouse and hospitality keepers are recognizable and respected across Tepenia, Majyao Bisyugota being the most famous example
```
**L261 — after**
```text
- Hosting culture itself — Janbogo-trained or Janbogo-influenced hosts and hospitality keepers are recognizable and respected across Tepenia, Majyao Bisyugota being the most famous example
```

**L297 — before**
```text
- **The site of Majyao's original teahouse** — the establishment famous throughout Tepenia before its keeper relocated to Concordia; current state (preserved, repurposed, damaged) is a DLC 6 open question
```
**L297 — after**
```text
- **The site of the teahouse Majyao ran** — the establishment famous throughout Tepenia before its keeper relocated to Concordia; current state (preserved, repurposed, damaged) is a DLC 6 open question
```

**L300 — before**
```text
- **The great shielded commercial halls** *(established 2026-07-05)* — huge indoor shopping and social districts, brightly lit and constantly active, where most of daily Janbogo life actually happens; the direct architectural fulfillment of the outside-hostile/inside-warm design principle already established in Section 9, at a genuinely large civic scale rather than just individual teahouses
```
**L300 — after**
```text
- **The great shielded commercial halls** *(established 2026-07-05)* — huge indoor shopping and social districts, brightly lit and constantly active, where most of daily Janbogo life actually happens; the direct architectural fulfillment of the outside-hostile/inside-warm design principle already established in Section 9, at a genuinely large civic scale rather than just individual interiors
```

**L308 — before**
```text
- **[Placeholder — the founding teahouse tradition's spread beyond Korean-descended families]** — the period in which the hosting tradition became genuinely city-wide rather than ethnically specific; likely gradual, not a single event, but culturally significant enough to be remembered as an era
```
**L308 — after**
```text
- **[Placeholder — the founding tradition of tea, hospitality and togetherness spreading beyond Korean-descended families]** — the period in which the hosting tradition became genuinely city-wide rather than ethnically specific; likely gradual, not a single event, but culturally significant enough to be remembered as an era
```

**L316 — before**
```text
- **[Placeholder — founding-era Korean community figure]** — the person most associated with establishing the original teahouse tradition that the entire city's culture eventually grew from
```
**L316 — after**
```text
- **[Placeholder — founding-era Korean community figure]** — the person most associated with establishing the founding tradition of tea, hospitality and togetherness that the city's culture eventually grew from
```

**L317 — before**
```text
- **[Placeholder — first non-Korean-descended teahouse keeper of note]** — whoever first proved the tradition could be carried by someone outside its founding ethnicity; likely a culturally significant, semi-legendary figure in Janbogo's own self-understanding
```
**L317 — after**
```text
- **[Placeholder — first non-Korean-descended host of note]** — whoever first proved the tradition could be carried by someone outside its founding ethnicity; likely a culturally significant, semi-legendary figure in Janbogo's own self-understanding
```

**L330 — before**
```text
Majyao Bisyugota's Concordia teahouse is the diaspora's most visible cultural anchor — proof, replicated in the capital, that the tradition travels intact regardless of who's carrying it.
```
**L330 — after**
```text
Majyao Bisyugota's Concordia teahouse is one of the diaspora's most visible cultural anchors — proof, replicated in the capital, that the tradition travels intact regardless of who's carrying it.
```

### File 2 · `Local_Robot_Culture/Janbogo_Subnet/Janbogo.md` · applied 07:44, approved by the developer ("for File 2, yup, all looks good") · file still 290 lines (`wc -l`) · read back OK
*(Process note: the first attempt aborted before writing because the L103 phrase wraps onto the next line; nothing was changed by it. Re-run with the exact text.)*

**L38 — before**
```text
  Mechanisms). Katabatic Warning Towers, the Great Shielded Commercial Halls, Majyao's Original Teahouse, the
```
**L38 — after**
```text
  Mechanisms). Katabatic Warning Towers, the Great Shielded Commercial Halls, the teahouse Majyao ran, the
```

**L57 — before**
```text
  compartmentalization chain, and Wu Lian-Marchetti's teahouse-to-hall scaling decision all fed specific
```
**L57 — after**
```text
  compartmentalization chain, and Wu Lian-Marchetti's interior-to-hall scaling decision all fed specific
```

**L72 — before**
```text
| Kinship, Clan & Mentor/Mentee Institution | **Yes** | Teahouse-keeping apprenticeship is a literal, concrete local instance of the only real robot kinship mechanism — see §1 below. |
```
**L72 — after**
```text
| Kinship, Clan & Mentor/Mentee Institution | **Yes** | Hosting-craft apprenticeship (tea and coffee service) is a literal, concrete local instance of the only real robot kinship mechanism — see §1 below. |
```

**L100 — before**
```text
  regardless of which teahouse trained her or when she arrived. That daily condition of hosting-as-communication
```
**L100 — after**
```text
  regardless of where she trained or when she arrived. That daily condition of hosting-as-communication
```

**L101 — before**
```text
  is Janbogo's real kinship floor; it holds between two robots who never worked the same teahouse, as long as
```
**L101 — after**
```text
  is Janbogo's real kinship floor; it holds between two robots who never trained in the same place, as long as
```

**L103 — before**
```text
- **[Adapted, Deep]** One specific shape that shared life takes: teahouse-keeping and coffee-service craft
```
**L103 — after**
```text
- **[Adapted, Deep]** One specific shape that shared life takes: tea and coffee-service craft
```

**L107 — before**
```text
  already-established "old teahouse families" fault line (§5) is, for robots specifically, quite literally a
```
**L107 — after**
```text
  already-established "old hosting families" fault line (§5) is, for robots specifically, quite literally a
```

**L184 — before**
```text
  The robot-specific angle: teahouse/coffee-service apprentices (per §1's kinship finding) plausibly retain
```
**L184 — after**
```text
  The robot-specific angle: tea/coffee-service apprentices (per §1's kinship finding) plausibly retain
```

**L230 — before**
```text
- **[Adapted, Deep]** — *Input categories combined: A (§5's "old teahouse families" fault line, §8's language
```
**L230 — after**
```text
- **[Adapted, Deep]** — *Input categories combined: A (§5's "old hosting families" fault line, §8's language
```

**L234 — before**
```text
  teahouse-keeping (§1's finding) — meaning the "old teahouse families" fault line isn't really about bloodline
```
**L234 — after**
```text
  tea-and-coffee service craft (§1's finding) — meaning the "old hosting families" fault line isn't really about bloodline
```

**L244 — before**
```text
  after-hours space within the Halls or teahouses, modeled directly on the kahvehane's specific historical
```
**L244 — after**
```text
  after-hours space within the Halls or other shared interior spaces, modeled directly on the kahvehane's specific historical
```

**L273 — before**
```text
  figures (the founding-era Korean community figure, the first non-Korean-descended teahouse keeper, Han
```
**L273 — after**
```text
  figures (the founding-era Korean community figure, the first non-Korean-descended host of note, Han
```

### File 3 · Spec `Specs/Janbogo subnet/Janbogo.md` · applied 07:57 (8 of 9 drafted lines; **L205 held** pending the Taurus-vs-Aquarius question) · approved by the developer ("Everything else looks fine. All of the other points you can write to file.") · file still 219 lines (`wc -l`) · read back OK
*(Process note: the first attempt aborted before writing on a wrong line-count assertion of mine; nothing was changed by it.)*

**L123 — before**
```text
- **The communal warmth design tension:** the violent outdoor environment versus Janbogo's renowned interior culture (teahouses, shared warmth) is the defining design contrast of the setting — sheltered interior spaces are survival, not luxury; transitioning between exterior and interior is a constant mechanical and atmospheric rhythm
```
**L123 — after**
```text
- **The communal warmth design tension:** the violent outdoor environment versus Janbogo's interior culture of tea, hospitality and togetherness is the defining design contrast of the setting — sheltered interior spaces are survival, not luxury; transitioning between exterior and interior is a constant mechanical and atmospheric rhythm
```

**L149 — before**
```text
The teahouse culture was its most nationally visible expression. Janbogo teahouses were not simply places to drink tea; they were social institutions, community anchors, places where the texture of daily life was deliberately made worth living. This tradition was strong enough that at least one Janbogo teahouse was famous throughout Tepenia — known to people who had never been to Janbogo and would never go.
```
**L149 — after**
```text
Tea, hospitality and togetherness are part of its culture. At least one Janbogo teahouse was famous throughout Tepenia — known to people who had never been to Janbogo and would never go.
```

**L151 — before**
```text
**Tepenia's Korean-founded cities:** Janbogo is not the only Korean city in Tepenia. Sinheung, in the Mirny subnet's Larsemann Hills cluster, is singularly Korean-founded via the same Jeju-do diplomatic partition that allocated Zhongshan to China and Shirayuki to Japan, and remains genuinely Korean-**Primary** today at 34.62% — by current population, the most heavily Korean city in Tepenia, more so than Janbogo itself. Janbogo's own claim to being "Korea's primary Tepenian city" rests on a different foundation than raw population share: South Korea is still Janbogo's largest Significant-tier nation (10.23%, ahead of even Australia's 9.99%), and Janbogo's founding-era civic template — the teahouse tradition, communal warmth — was never displaced or diluted even as the population that carries it forward diversified (see `Local_Cultures/Janbogo_Subnet/Janbogo.md` Section 1). Both cities carry genuine Korean cultural identity, by different mechanisms: Sinheung by demographic dominance, Janbogo by cultural/institutional depth despite demographic dilution. Contrapunto, founded by immigrants from the Americas, also has a Korean community at Significant tier (5.79%). Whether the Korean communities of these cities had meaningful contact pre-Split Brain, and what the current relationship between surviving diaspora members might be, is a lore thread running through all three.
```
**L151 — after**
```text
**Tepenia's Korean-founded cities:** Janbogo is not the only Korean city in Tepenia. Sinheung, in the Mirny subnet's Larsemann Hills cluster, is singularly Korean-founded via the same Jeju-do diplomatic partition that allocated Zhongshan to China and Shirayuki to Japan, and remains genuinely Korean-**Primary** today at 34.62% — by current population, the most heavily Korean city in Tepenia, more so than Janbogo itself. Janbogo's own claim to being "Korea's primary Tepenian city" rests on a different foundation than raw population share: South Korea is still Janbogo's largest Significant-tier nation (10.23%, ahead of even Australia's 9.99%), and Janbogo's founding-era civic template — tea, hospitality and communal warmth — was never displaced or diluted even as the population that carries it forward diversified (see `Local_Cultures/Janbogo_Subnet/Janbogo.md` Section 1). Both cities carry genuine Korean cultural identity, by different mechanisms: Sinheung by demographic dominance, Janbogo by cultural/institutional depth despite demographic dilution. Contrapunto, founded by immigrants from the Americas, also has a Korean community at Significant tier (5.79%). Whether the Korean communities of these cities had meaningful contact pre-Split Brain, and what the current relationship between surviving diaspora members might be, is a lore thread running through all three.
```

**L153 — before**
```text
**Nationally known for:** Its teahouse culture and the quality of warmth and communal hospitality its people carried with them; being the last active coastal link to Concordia.
```
**L153 — after**
```text
**Nationally known for:** The quality of warmth and communal hospitality its people carried with them; being the last active coastal link to Concordia.
```

**L167 — before**
```text
- **Majyao's Teahouse** — the establishment famous throughout Tepenia; Majyao has since relocated to Concordia; what remains of the teahouse in Janbogo's current damaged state is TBD
```
**L167 — after**
```text
- **The teahouse Majyao ran** *(no name yet)* — one of the city's founding-era landmarks, famous throughout Tepenia; Majyao has since relocated to Concordia; what remains of the teahouse in Janbogo's current damaged state is TBD
```

**L175 — before**
```text
- **Majyao Bisyugota** — Robot — Teahouse keeper whose establishment was famous throughout Tepenia; relocated to Concordia (Aquarius district) before or during the Long Night War; her teahouse was a defining landmark of Janbogo's cultural identity and the most nationally recognized symbol of the city's character
```
**L175 — after**
```text
- **Majyao Bisyugota** — Robot — Teahouse keeper whose establishment was famous throughout Tepenia; relocated to Concordia (Aquarius district) before or during the Long Night War; her teahouse was one of the city's founding-era landmarks
```

**L178 — before**
```text
- **Architect Wu Lian-Marchetti** *(placeholder, added 2026-07-17, same section)* — credited with designing the great shielded commercial halls, translating the teahouse-scale interior-warmth principle into large-scale civic architecture.
```
**L178 — after**
```text
- **Architect Wu Lian-Marchetti** *(placeholder, added 2026-07-17, same section)* — credited with designing the great shielded commercial halls, translating the interior-warmth principle into large-scale civic architecture.
```

**L214 — before**
```text
- What does Majyao's original teahouse in Janbogo look like now — preserved, looted, repurposed, partially destroyed?
```
**L214 — after**
```text
- What does the teahouse Majyao ran in Janbogo look like now — preserved, looted, repurposed, partially destroyed?
```

### Correction · Majyao's teahouse is in the **Taurus** district of Concordia (not Aquarius) · applied 08:01 · developer: "Specifically in the city of Concordia. Her teahouse is in the Taurus district, yes. Also, Aquarius is a zodiac district placeholder, not its actual proper name. We can refer to things using placeholders."
*Evidence: her own character README, questline README, `Player_Homes.md`, `Romance_Unlocked_Homes.md`, `District_Source_Index.md`, `DONE.md` (all Taurus). The Aquarius value sat only in the Janbogo city-level files. Still to fix: `16` L2890 (with the `16` step), and the reference copies `City_Master_Reference/Janbogo_Subnet_Reference.md` L304 and `Split_Extracts/Janbogo_Subnet_Reference_EXTRACT.md` L423 (outside the Janbogo run; developer's call).*

#### Spec `Specs/Janbogo subnet/Janbogo.md` (L175, L191, L205) · file still 219 lines (`wc -l`) · read back OK

**L175 — before**
```text
- **Majyao Bisyugota** — Robot — Teahouse keeper whose establishment was famous throughout Tepenia; relocated to Concordia (Aquarius district) before or during the Long Night War; her teahouse was one of the city's founding-era landmarks
```
**L175 — after**
```text
- **Majyao Bisyugota** — Robot — Teahouse keeper whose establishment was famous throughout Tepenia; relocated to Concordia (Taurus district) before or during the Long Night War; her teahouse was one of the city's founding-era landmarks
```

**L191 — before**
```text
- **Majyao Bisyugota** — Aquarius district; runs a teahouse; relocated from Janbogo
```
**L191 — after**
```text
- **Majyao Bisyugota** — Taurus district; runs a teahouse; relocated from Janbogo
```

**L205 — before**
```text
In Concordia, Janbogo's legacy is not historical — it is present-tense. The Gemini district enclave is a living piece of Janbogo culture, maintained by the diaspora community. The teahouse tradition survives through Majyao's establishment in Aquarius. The supply relationship is ongoing.
```
**L205 — after**
```text
In Concordia, Janbogo's legacy is not historical — it is present-tense. The Gemini district enclave is a living piece of Janbogo culture, maintained by the diaspora community. Majyao's teahouse continues in Taurus. The supply relationship is ongoing.
```

#### Culture file `Local_Cultures/Janbogo_Subnet/Janbogo.md` (L315) · file still 330 lines (`wc -l`) · read back OK

**L315 — before**
```text
- **Majyao Bisyugota** — Robot; kept the most nationally famous teahouse in Tepenia in Janbogo before relocating to Concordia's Aquarius district; Chinese-descended, embodying the city's central cultural inversion; her Concordia establishment carries the tradition forward in diaspora
```
**L315 — after**
```text
- **Majyao Bisyugota** — Robot; kept the most nationally famous teahouse in Tepenia in Janbogo before relocating to Concordia's Taurus district; Chinese-descended, embodying the city's central cultural inversion; her Concordia establishment carries the tradition forward in diaspora
```

### File 4 · `Division_of_Industry/16_Per_City_Three_Tier_Run.md` §28 · applied 08:02, approved by the developer ("all correct") · file still 3,578 lines (`wc -l`) · read back OK

**L2882 — before**
```text
reflecting the centrality of teahouses and hosting institutions **to the local economy, not just the
```
**L2882 — after**
```text
reflecting the centrality of hospitality and hosting institutions **to the local economy, not just the
```

**L2885 — before**
```text
> **But ECONOMIC is not the test. NATIONAL is.** The teahouse tradition is *"nationally famous"* — **the same
```
**L2885 — after**
```text
> **But ECONOMIC is not the test. NATIONAL is.** Janbogo's warmth and hospitality are *"nationally known"* — **the same
```

**L2890 — before**
```text
*(Majyao's Teahouse has since relocated to Concordia/Aquarius — **the export was the institution itself, not
```
**L2890 — after**
```text
*(The teahouse Majyao ran has since relocated to Concordia/Taurus — **the export was the institution itself, not
```

### File 5 · `Division_of_Industry_Sweep_2026-08-31.md` L72–75 · applied 08:06, approved by the developer ("yup, that looks right") · file still 250 lines (`wc -l`) · read back OK · also removes the quoted "Janbogo cannot be an entire city of teahouses" concern from this file (question 2)

**L72 — before**
```text
  should be the model for fixes.** The developer's own "Janbogo cannot be an entire city of teahouses" concern
```
**L72 — after**
```text
  should be the model for fixes.** It names a **broad sector** (hospitality/communal services) and cites
```

**L73 — before**
```text
  is already answered in the file: it names a **broad sector** (hospitality/communal services) and cites
```
**L73 — after**
```text
  hosting institutions as *what drives it* — *"reflecting the centrality of hospitality and hosting
```

**L74 — before**
```text
  teahouses as *what drives it* — *"reflecting the centrality of teahouses… to the local economy, not just the
```
**L74 — after**
```text
  institutions to the local economy, not just the
```

**L75 — before**
```text
  culture."* **Sector named broadly; signature instance named as its driver. Exactly right.**
```
**L75 — after**
```text
  culture."* **Sector named broadly, with what drives it named beside it. Exactly right.**
```

### File 6 · `Universal_Location_Methodology/Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` · L1426, L1703, L1704 · applied 08:08, approved by the developer ("yup, that looks right") · file still 8,586 lines (`wc -l`) · read back OK · removes the quoted Janbogo example (question 2)

**L1426 — before**
```text
entirely based around managing the lake"* and *"Janbogo an entire city of teahouses."*
```
**L1426 — after**
```text
entirely based around managing the lake."*
```

**L1703 — before**
```text
communal culture, the teahouse tradition as "the district's most nationally visible expression" of that
```
**L1703 — after**
```text
communal culture, and a national reputation for that temperament — and it **directly cites
```

**L1704 — before**
```text
temperament — and it **directly cites `Local_Cultures/Janbogo_Subnet/Janbogo.md` Section 1 by name** as the
```
**L1704 — after**
```text
`Local_Cultures/Janbogo_Subnet/Janbogo.md` Section 1 by name** as the
```


### File 7 · `Concordia-City/Districts/Phase_Instructions/00b_General_Population_Discipline.md` · L97 · applied 08:08, approved by the developer ("yup, that looks right") · file still 157 lines (`wc -l`) · read back OK · removes the quoted Janbogo example (question 2)

**L97 — before**
```text
entirely based around managing the lake"* or *"Janbogo an entire city of teahouses."*
```
**L97 — after**
```text
entirely based around managing the lake."*
```

### File 8 · pass `Datasheets/Phase_7.md` L20 (edited) and L21 (row removed) · applied 08:12, approved by the developer ("yup, that looks right") · file now 30 lines (was 31; one row removed on purpose) · read back OK

**L20 — before**
```text
| `Division_of_Industry_Sweep_2026-08-31.md` *(the four hits below, L71, L72, L157 and L223, each name the city)* | - **Janbogo — `Hospitality / communal services: ~15%`.** ⭐ **This is the *correct* version of the pattern and | `Division_of_Industry_Sweep_2026-08-31.md` L71 |
```
**L20 — after**
```text
| `Division_of_Industry_Sweep_2026-08-31.md` *(the three hits below, L71, L157 and L223, each name the city)* | - **Janbogo — `Hospitality / communal services: ~15%`.** ⭐ **This is the *correct* version of the pattern and | `Division_of_Industry_Sweep_2026-08-31.md` L71 |
```

**L21 — before (row removed)**
```text
| ↳ `Division_of_Industry_Sweep_2026-08-31.md` | should be the model for fixes.** The developer's own "Janbogo cannot be an entire city of teahouses" concern | `Division_of_Industry_Sweep_2026-08-31.md` L72 |
```


### File 9 · pass `Datasheets/Phase_8.md` L12 · applied 08:12, approved by the developer ("yup, that looks right") · file still 16 lines · read back OK

**L12 — before**
```text
| The city's own spec — term check for cuisine / dress / music / craft | Counted by pattern against the full 219-line file: cuisine / food / dish / drink — 1 hit(s) (L149, "places to drink tea", in the teahouse paragraph at L147–L149; the teahouse is also named at `## Notable Locations` L167) · dress / clothing / attire — 0 hit(s) · music — 0 hit(s) · craft — 0 hit(s) | Counted 2026-10-21; the food / drink count re-run by hand 2026-10-30: `Specs/Janbogo.md` L166–L149, L167 |
```
**L12 — after**
```text
| The city's own spec — term check for cuisine / dress / music / craft | Counted by pattern against the full 219-line file: cuisine / food / dish / drink — 0 hit(s) (the teahouse Majyao ran is named at `## Notable Locations` L167) · dress / clothing / attire — 0 hit(s) · music — 0 hit(s) · craft — 0 hit(s) | Counted 2026-10-21; the food / drink count re-run by hand 2026-10-31 after the spec's L149 was reworded: `Specs/Janbogo.md` L166–L149, L167 |
```


### File 10 · pass `Datasheets/Step_3.md` L11 · **no change** (developer, question 3: leave the chaykhana pick; the sheet copies `Inspirational-Influences.md` L47 as it stands)

*(Bookkeeping correction 08:12: line counts in this log are `wc -l` counts. Earlier headers had used the split count — 220 for the spec, 331 for the culture file, 291 for the robot file — which are one too many; the files' lengths were unchanged by every edit.)*

### File 11 · `City_Master_Reference/Janbogo_Subnet_Reference.md` · L304, L311 · applied 08:15, approved by the developer ("yup, fix them now") · file still 383 lines (`wc -l`) · read back OK · same wording as the spec/culture/`16` edits (Aquarius → Taurus; teahouse label and driver replaced)

**L304 — before**
```text
- Teahouse culture nationally famous (Majyao's Teahouse, since relocated to Concordia/Aquarius).
```
**L304 — after**
```text
- Nationally known for its warmth and communal hospitality; the teahouse Majyao ran, famous throughout Tepenia, has since relocated to Concordia/Taurus.
```

**L311 — before**
```text
~15% (unusually large — teahouses/hosting institutions) · technical/scientific ~10% · education ~5% · other ~5%.
```
**L311 — after**
```text
~15% (unusually large — hospitality/hosting institutions) · technical/scientific ~10% · education ~5% · other ~5%.
```


### File 12 · `City_Master_Reference/Split_Extracts/Janbogo_Subnet_Reference_EXTRACT.md` · L423, L430 · applied 08:15, approved by the developer ("yup, fix them now") · file still 529 lines (`wc -l`) · read back OK · same wording as the spec/culture/`16` edits (Aquarius → Taurus; teahouse label and driver replaced)

**L423 — before**
```text
- Teahouse culture nationally famous (Majyao's Teahouse, since relocated to Concordia/Aquarius).
```
**L423 — after**
```text
- Nationally known for its warmth and communal hospitality; the teahouse Majyao ran, famous throughout Tepenia, has since relocated to Concordia/Taurus.
```

**L430 — before**
```text
~15% (unusually large — teahouses/hosting institutions) · technical/scientific ~10% · education ~5% · other ~5%.
```
**L430 — after**
```text
~15% (unusually large — hospitality/hosting institutions) · technical/scientific ~10% · education ~5% · other ~5%.
```

