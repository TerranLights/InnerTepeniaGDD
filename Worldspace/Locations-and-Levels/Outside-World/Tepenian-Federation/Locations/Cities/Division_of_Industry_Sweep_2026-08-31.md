# Division of Industry — corpus-wide sweep, 2026-08-31

> ## ⚠ FINDINGS ONLY. NOTHING HAS BEEN CHANGED IN ANY CITY FILE.
>
> **Developer instruction:** *"for the current time being, don't actually change anything in the official city
> files. Just make a file for keeping records of your findings… and we'll figure out how to approach the
> issue."* **This file records; it does not fix.** The one exception predates the instruction: **Cape Adare's
> own §15 was corrected earlier the same day**, which is what prompted this sweep.

**Scope:** all 36 `Local_Cultures` files carrying a §15 Division of Industry — 35 cities plus Amundsen Station.
*(The two Tri-Cities files are regional overviews and correctly have no §15.)*

**What this sweep hunts:** the failure class established at Cape Adare and now written into
`00b_General_Population_Discipline.md` — **a narrow object, site, or person standing in for a whole sector.**
*(Cape Adare had assigned 35% of a 1,050,051-person economy — ~367,500 people — to work pointed at a single
1899 hut.)* Secondary targets: single-sector over-dominance, systematic omissions, and arithmetic errors.

---

# 1. ✅ Arithmetic — clean, all 36

**Every city's percentages sum to exactly 100%.** No exceptions.

> **Instrument note, per standing discipline:** the first automated pass flagged **Mawson (90%)** and **Mirny
> (120%)**. **Both were false positives of my own regex** — Mawson's hospitality entry is formatted
> `**vision session, 2026-07-06:** 10%` and was missed; Mirny's extra 20% was a *prose back-reference* to a
> sector already counted in its list. **Hand-checked both against the source; both sum to 100.** Reported
> because an unverified scan is not evidence.

---

# 2. ⚠ OBJECT/PERSON-COLONIZATION — the target pattern. Two confirmed instances.

## 2.1 Scott — **confirmed, same shape as Cape Adare's**

> `Education: 15% — historical/commemorative knowledge-keeping tied to St. Robert`

**An entire education sector assigned to commemorating one person.** Scott's population is substantial; 15% of
it is a great many people, and a city of that size needs *schools* — ordinary childhood education, trade
training, maritime instruction. **Commemoration of St. Robert is plausibly a respected specialization inside
the education sector; it cannot be the sector.**

**Aggravating detail:** Scott's own culture file describes it as *"overwhelmingly residential… a genuinely
decent, quiet place to raise a family."* **A city explicitly characterized by family life has no general
schooling in its economy** — the colonized annotation displaced exactly the sector its own civic identity
most needs.

**Suggested direction (not applied):** widen to ordinary education for a residential city, with St. Robert
commemoration and related knowledge-keeping named as a scoped specialization within it. Mirrors the Cape Adare
correction exactly.

## 2.2 Port Lockroy — **the corpus's highest heritage concentration, and it was not on the radar**

> `Heritage / cultural preservation: 25% — a genuine civic function inherited from the museum era`
> `Technical / maintenance: 15% — preserving the layered historical infrastructure`

**40% of the economy is heritage-themed** — higher than Cape Adare's original 35%, and this one had never been
flagged.

**⚠ But it needs a genuinely different judgment than Cape Adare's, and this is the interesting part.** Port
Lockroy's real-world basis *was literally a museum* — the actual site is a historic base operated as a museum
and post office. **So a heritage-heavy economy here is far better motivated than at Cape Adare**, and the
second entry ("preserving the layered historical infrastructure") is already **broad** rather than
object-pointed — it describes a city's whole building stock, not one hut.

**The open question is scale, not legitimacy:** is 40% plausible, or is this the same colonization with a
better excuse? **Flagged for a judgment call, explicitly not diagnosed as a bug.**

## 2.3 Checked and cleared — instances that look like the pattern but are not

- **Janbogo — `Hospitality / communal services: ~15%`.** ⭐ **This is the *correct* version of the pattern and
  should be the model for fixes.** The developer's own "Janbogo cannot be an entire city of teahouses" concern
  is already answered in the file: it names a **broad sector** (hospitality/communal services) and cites
  teahouses as *what drives it* — *"reflecting the centrality of teahouses… to the local economy, not just the
  culture."* **Sector named broadly; signature instance named as its driver. Exactly right.**
- **Mawson — `Hospitality / honeymoon tourism: 10%`.** Specific but *sector-shaped*, and sized modestly.
- **Amundsen Station — Arcanet 60% / Tower ops 30%.** **Self-caveated in the file itself:** *"Division of
  Industry as a category assumes a civic economy; Amundsen Station had no economy in the conventional sense."*
  Correctly handled.

---

# 3. Single-sector dominance — six cities above 40%

**Not automatically a defect** — a genuinely specialized settlement can be dominated by one sector. Listed for
review, with the distinction that matters: **is the dominant sector a *productive activity* or a *theme*?**

| City | Top sector | Assessment |
|---|---|---|
| **Vostok** | **Science 65%** | ⚠ Highest in corpus. Plus 25% self-sufficiency = **90% in two sectors.** Extreme-outpost profile; plausible, but leaves almost nothing for ordinary life |
| **Kunlun** | **Astronomy 60%** | ⚠ Plus ice core 15% + religious 15% + facility 10% = 100% with **no commercial, education, food, or manufacturing at all.** Mitigating: 0 humans / 123,449 robots — a robot-only population's needs differ |
| **Dome Fuji** | Ice core 40% + religious 35% | ⚠ **75% in two sectors**, only 20% facility upkeep + 5% other. The file itself flags the ice-core share as TBD |
| **Sinheung** | Industrial fabrication 45% | ✅ A productive activity, nationally significant (chamber manufacture). Fine |
| **Rothera** | Industrial 40% | ✅ Productive. Fine |
| **Palmer City / Davis / Fort McMurdo** | 35% each | ✅ All productive (hospitality, agriculture, industry). Palmer City self-caveats as "a working estimate, not confirmed canon" |

**The pattern worth noting:** every city where the dominant share is a **productive activity** reads fine.
Discomfort clusters exactly where the dominant share is a **purpose or identity** (science, astronomy,
devotion, commemoration) rather than an output.

---

# 4. ⭐ THE BIGGEST FINDING — systematic sector omissions, corpus-wide

**This was not what the sweep was looking for, and it is larger than what it was.**

## 4.1 Healthcare is absent from **35 of 36** city economies

**No city lists medicine, healthcare, or public health as an economic sector.** The single partial exception is
**Kunlun's** *"altitude-legacy medical infrastructure / facility maintenance: 10%"* — and even that is framed as
legacy infrastructure rather than as caring for a population.

**These are cities of hundreds of thousands to millions of people, in the most hostile inhabited environment
on the planet.** Hospitals, clinics, trauma care, cold-injury treatment, and — given the human/robot split —
**robot maintenance and repair as a civic service** are all missing from every economy in the corpus.

**This is almost certainly the single largest expansion opportunity the sweep found.**

## 4.2 Food production appears in only **2 of 36**

Only **Davis** (agriculture 35%, the established Breadbasket) and **Esperanza** (15%). **Every other city's
food supply is implicit.** For a continent-scale closed economy this is a real, load-bearing question:
Davis alone feeding ~30 cities is a supply chain with enormous narrative and logistical implications — and if
that *is* the intent, it is a significant, currently-unstated national dependency.

## 4.3 Education is absent from roughly a third

Missing entirely from **Byrd, Belgrano, Sanay, Dome Fuji, Kunlun, Vostok, Marambio, Palmer City, Port Lockroy,
Rothera, Signy, Juan Carlos, Casey, Mirny** *(some fold it into "Other")*. **Cities with families and children
need schools.**

## 4.4 ⭐ The full matrix — measured, all 36 cities × six necessary industries

**Developer instruction, 2026-08-31: this is now HIGH PRIORITY.** *"I live in a city where there's constantly
construction happening everywhere, [and] I thought to myself, 'What about construction?' So I'm glad you caught
that."* — independent convergence: the same gap noticed from walking around a real city and from scanning the
corpus.

`Y` = the sector is named or clearly described · `.` = absent

| City | Health | Constr | Food | Educ | Admin | Utils | missing |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Amundsen Station | . | . | . | . | . | . | **6/6** |
| Byrd | . | . | . | . | . | . | **6/6** |
| Abowasa | . | . | . | Y | . | . | 5/6 |
| Belgrano | . | . | . | . | . | . | **6/6** |
| Halley | . | . | . | . | . | . | **6/6** |
| Lazar | . | Y | . | Y | . | . | 4/6 |
| Neumayer | . | . | . | Y | . | . | 5/6 |
| Princess Elisabeth | . | . | . | Y | . | . | 5/6 |
| Sanay | . | Y | . | Y | Y | . | 3/6 |
| Troll | . | . | . | Y | . | . | 5/6 |
| **Cape Adare** | Y | Y | . | Y | Y | . | **2/6** *(post-correction)* |
| Denison | . | . | . | Y | . | . | 5/6 |
| Dumont d'Urville | . | . | . | Y | . | . | 5/6 |
| Fort McMurdo | . | . | . | Y | . | . | 5/6 |
| Janbogo | Y | . | . | Y | . | . | 4/6 |
| Scott | . | . | . | Y | . | . | 5/6 |
| Zukelli | Y | . | Y | Y | . | . | 3/6 |
| Dome Fuji | . | . | . | . | . | . | **6/6** |
| Mawson | Y | . | . | . | . | . | 5/6 |
| Sayowa | . | . | . | . | . | . | **6/6** |
| Casey | . | . | . | . | . | . | **6/6** |
| Davis | . | . | Y | . | . | . | 5/6 |
| Kunlun | Y | . | . | . | . | . | 5/6 |
| Mirny | . | Y | . | . | . | . | 5/6 |
| Shirayuki | . | . | . | Y | . | . | 5/6 |
| Sinheung | . | . | . | Y | . | . | 5/6 |
| Vostok | . | . | . | . | . | . | **6/6** |
| Zhongshan | . | . | . | Y | . | . | 5/6 |
| **Esperanza** | Y | . | Y | Y | Y | . | **2/6** |
| Juan Carlos | . | . | . | . | . | . | **6/6** |
| Marambio | . | . | . | . | . | . | **6/6** |
| Palmer City | Y | . | . | . | . | . | 5/6 |
| Port Lockroy | . | . | . | . | . | . | **6/6** |
| Rothera | . | . | . | . | . | . | **6/6** |
| Sejong | . | . | . | Y | . | . | 5/6 |
| Signy | . | . | . | . | . | . | **6/6** |
| **MISSING FROM** | **29** | **32** | **33** | **18** | **33** | **36** |

### What the totals say

- **Utilities / water / sanitation / waste: absent from 36 of 36.** **Not one Tepenian city has any of it in
  its economy** — in the coldest environment on Earth, where water is frozen, waste cannot simply be buried,
  and a utility failure is lethal rather than inconvenient.
- **Food 33/36 · Administration 33/36 · Construction 32/36 · Healthcare 29/36 · Education 18/36.**
- **Thirteen cities are missing all six**: Amundsen Station, Byrd, Belgrano, Halley, Dome Fuji, Sayowa, Casey,
  Vostok, Juan Carlos, Marambio, Port Lockroy, Rothera, Signy.
- **Best-covered: Cape Adare and Esperanza, at 2/6 missing** — and Cape Adare only because it was corrected
  earlier today, which is itself the point.

> **⚠ Instrument caveat: these are FLOOR estimates, and the real gaps are worse.** The matcher was deliberately
> generous — Health matched any occurrence of `care`, so Esperanza's *childcare* and similar incidental words
> counted as hits. **A stricter reading would push healthcare's 29 closer to 35.** Reported as a floor rather
> than tuned, since the direction of the error is knowable and conservative.

### Why this matters more than the colonization bug that started the sweep

**The colonization bug makes a sector describe the wrong thing. This makes whole sectors not exist.** And it is
systematic rather than scattered — **a corpus-wide blind spot in how these economies were originally
composed**, not a set of individual oversights. Every one of these industries is *load-bearing* in an Antarctic
city specifically:

- **Construction** — every structure is built and maintained against conditions that destroy buildings;
  Denison's whole identity is wind-engineering, and it still has no construction sector.
- **Utilities** — water is ice, waste cannot be landfilled, and heat is survival infrastructure. Concordia's
  own canon establishes dome-and-corridor heating as *"the survival precondition"* — nobody's economy runs it.
- **Healthcare** — including the robot-population equivalent: maintenance, repair, and coolant/siligel supply
  as civic services rather than personal habits.
- **Food** — see §4.2; ~30 cities have no stated source.

---

# 5. Good models, for whenever fixes are approached

**Cities naming sectors by genuine economic function, with no colonization** — the pattern to copy:

**Davis** (agriculture 35%) · **Casey** (transit/logistics 30%) · **Zukelli** (hospitality 25%) · **Sanay**
(port/shipyard 30%) · **Byrd** (mechanized fabrication 30%) · **Sayowa** (industrial fabrication 30%) ·
**Mirny** (communications 20%, with genuinely specific industrial detail) · **Marambio** (aviation 30% /
maritime 30%) · **Signy** (biological research 30% / fishing 30%)

**And the single best model in the corpus: Janbogo's hospitality entry** (§2.3) — broad sector, signature
instance named as its driver.

---

# 6. Expansion opportunities noticed in passing

- **"Other" buckets run 3–15%** across the corpus and are almost entirely undifferentiated. Naming what's in
  them is cheap, high-yield work.
- **Cape Adare's guano extraction** is the kind of ordinary, unglamorous, specific industry most cities lack —
  a useful template for giving economies non-thematic texture.
- **Shirayuki** is the only city with arts/culture as a major *economic* sector (25%), despite several cities
  having strong established arts identities.
- **Two cities name "Diplomatic / inter-community coordination"** as a sector (Sejong 15%, Sinheung 10%) — an
  unusual and rather good idea that could apply more widely.

---

# 7. Suggested approach — for discussion, not action

1. **Fix the two confirmed colonizations** (Scott; Cape Adare already done) using the `00b` rule: widen the
   definition, keep the percentage, name the signature instance as a scoped specialization.
2. **Make a judgment call on Port Lockroy** — legitimacy is genuine, scale is the question.
3. **Decide whether the missing-sector finding (§4) is a corpus-wide pass of its own.** It is much larger than
   this sweep's original target and probably deserves its own treatment — healthcare especially, which is
   absent everywhere and needed everywhere.
4. **Review the four purpose-dominant cities** (Vostok, Kunlun, Dome Fuji, and Scott once fixed) against the
   question *"could a person live an entire life here?"* — the standing closing test.
