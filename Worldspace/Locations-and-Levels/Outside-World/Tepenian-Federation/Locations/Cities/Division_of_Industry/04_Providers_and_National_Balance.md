# Provider Cities & the National Balance — 2026-09-01

**Second Interwar Period throughout.** Instance data (LAW C). Method: `05_Bulk_Mode` LAW D — resolve at the
national level before the per-city level.

**Approach, per developer instruction:** identify cities that are *massively* disproportionate producers, mark
them with their industries, **set them aside without subdividing them**, then compute the needs of everyone
else and see how the two stack up.

---

# 1. ⚠ The correction that reframes everything: robots are workforce, not dependents

**The pilot run silently assumed ~50% workforce participation across the whole population.** That is wrong in a
way that matters enormously here.

> **Robots work. Robots do not eat, attend school, get sick, age, or require obstetric care.**
> **Workforce = 100% of robots + ~50% of humans.**

**Consequence:** a robot-heavy city has a **large workforce relative to its dependent population**, so it can
meet a given absolute need at a *smaller percentage of its economy*. **This is the single biggest factor in
whether the extreme cities are viable, and the pilot missed it.**

| City | Humans | Robots | **Workforce** | Workforce ÷ humans |
|---|--:|--:|--:|--:|
| Vostok | 129,617 | 259,644 | **324,453** | **2.50** |
| Casey | 733,795 | 761,936 | 1,128,834 | 1.54 |
| Neumayer | 613,735 | 638,345 | 945,213 | 1.54 |
| Kunlun | **0** | 123,449 | 123,449 | **∞** |

**Vostok has 2.5 workers for every human needing care, food and schooling — against a national norm of ~1.54.**

---

# 2. The outsourceable / non-outsourceable split

**This is the distinction that makes "relief" coherent.** A provider city can only relieve the right-hand
column.

| ⛔ NON-OUTSOURCEABLE — every city carries its own, always | ✅ OUTSOURCEABLE — relief possible |
|---|---|
| **Water & sanitation** *(shipping water always loses to melting local ice — established this session)* | **Food** — the Davis mechanism |
| **Sewage & waste treatment** *(cannot be landfilled in permafrost, cannot be shipped)* | **Manufactured goods & robot parts** |
| **Enclosure & atmosphere integrity** | **Materials recovery output** |
| **Construction & structural maintenance** *(buildings do not move)* | **Power generation** *(the Tower ran a continent-wide regulated grid)* |
| **Emergency services** *(fire, SAR — response time is the service)* | **Specialist & complex healthcare** *(patients CAN move between Tepenian cities)* |
| **Thermal distribution** *(generation networks; delivery does not)* | **Higher education & specialist training** |
| **Primary healthcare, obstetrics, childcare** | **Arts, entertainment, hospitality** *(the audience travels)* |
| **Mortuary & decommissioning** | **Administration** *(partially — a subnet hub can administer its region)* |

---

# 3. Provider cities — marked, and SET ASIDE (not subdivided)

**Criterion: the sector is far larger than the city's own consumption requires, making it a net national
supplier.** Multiple industries per city where warranted.

| City | Pop | Provider industries | Evidence |
|---|--:|---|---|
| **Davis** | 1,158,314 | **FOOD** | agriculture 35% — "the breadbasket," explicitly national |
| **{{Bunger Hills City}}** | *(TBD)* | **FOOD** | ⭐ **Added 2026-09-01.** Second agricultural region: largest ice-free area in East Antarctica (450–942 km²) + **Lake Figurnoye, Antarctica's largest freshwater lake.** Population, subdivision and all internal detail **deliberately blank** — see `../Bunger_Hills_City_-_Development_Brief.md` |
| **Esperanza** | 1,878,287 | **FOOD · EDUCATION/CHILDCARE · ⭐ MEDICINE** | agri 15% + educ/childcare 25%, rank 2 population, founding charter. **Medicine added 2026-09-01: the Esperanza Institute of Medicine — settled medicine, flagship Dept. of Pediatrics** |
| **Signy** | 188,694 | **FOOD (fish)** | fishing 30% of a small city working "the Scotia Sea's genuine productivity" |
| **Juan Carlos** | 386,692 | **FOOD (fish)** | maritime/fishing 30% |
| **Janbogo** | 1,310,511 | **FOOD (fish) · LOGISTICS** | marine 20% w/ **year-round polynya access**; commercial/logistics 30% |
| **Zukelli** | 1,258,651 | **FOOD (prepared)** | commercial 25% = "food and hospitality industries, **the city's signature export**" |
| **Sinheung** | 1,069,350 | **FABRICATION · ⭐ MEDICINE (robotic)** | industrial fabrication **45%** — highest in corpus; builds Cradle chambers shipped nationwide. **Medicine added 2026-09-01: the Sinheung Institute of Cybernetics and Robotic Care — physical AND emotional care of and for robots; the mental-health system of the ~51% robot majority** |
| **Rothera** | 317,449 | **FABRICATION** | industrial 40% |
| **Fort McMurdo** | 445,310 | **FABRICATION · EXTRACTION** | industrial 35% + marine extraction 25% |
| **Byrd** | 376,890 | **FABRICATION · DISPATCH** | mechanized fabrication 30% ("huge underground plants") + dispatch 25% |
| **Sayowa** | 225,376 | **FABRICATION · TRUCKING** | industrial fab 30% ("things genuinely get *made* here") + trucking 25% |
| **Marambio** | 570,269 | **LOGISTICS (air+sea)** | aviation 30% + maritime 30% = **60%** |
| **Sanay** | 463,669 | **LOGISTICS (port)** | port/shipyard 30% + trucking 20% = **50%** |
| **Casey** | 1,495,731 | **LOGISTICS** | transit/logistics 30%, Hwy 110 × Hwy 2 junction |
| **Belgrano** | 1,071,890 | **LOGISTICS (air) · ⭐ MEDICINE** | aviation/logistics 35% + maritime 20%. **Medicine added 2026-09-01: the Belgrano Institute of Medicine — field medicine, flagship Dept. of Emergency and Trauma Response; medevac is an aviation function** |
| **Troll** | 954,450 | **LOGISTICS (air)** | commercial/logistics 30%, airfield |
| **Mawson** | 1,446,733 | **LOGISTICS (subnet hub)** | subnet-hub logistics/Arcanet 25% |
| **Mirny** | 1,351,430 | **ARCANET** | communications/Arcanet 20% — "unusually large… unique subnet-hub" |
| **Amundsen Station** | 6,857 | **ARCANET · TOWER** | relay ops 60% + Tower ops 30% *(not a city; special case)* |
| **Shirayuki** | 1,178,313 | **ARTS · EDUCATION** | arts/music/fashion 25% (only city with arts as a major economic sector) + educ 20% |
| **Palmer City** | 332,808 | **HOSPITALITY** | entertainment/hospitality 35% |
| **Princess Elisabeth** | 1,137,917 | **ENERGY ENGINEERING** | "renewable energy systems, zero-emissions design expertise" |

**22 providers set aside. 15 cities remain to be needs-assessed.**

### ⭐ The gap this exercise found — and the developer's reframe of it

**Not one of the 37 cities has healthcare as a named sector at any scale.** Every other necessity has a
national specialist. **A nation of 15.6 million, which cannot evacuate a patient off-continent, has no medical
provider at all.**

> **Developer response, 2026-09-01 — and it is a better formulation than the gap as I stated it:**
> *"There can realistically be a city that's 'known for producing medical staff' — a city that's generally
> either home, or at least a training grounds for, doctors, nurses, first-aid attendants, field medics, air
> medics… This definitely deserves to be explored further."*

**⚠ The distinction is structural, not cosmetic. A treatment center would not solve this problem.**

| | |
|---|---|
| **Care DELIVERY** | **NON-outsourceable.** Cities sit 1,000+ km apart; nobody treats a Vostok patient from Concordia. **Every city staffs its own clinicians regardless of who else exists.** |
| **Care TRAINING** | **OUTSOURCEABLE — and it is the only part that concentrates.** A handful of schools supplying a continent is exactly how real nations work. |

**So the provider role is not *"we treat your sick."* It is *"we make your doctors."*** And it compounds with
a constraint already established this session: **Tepenia cannot evacuate off-continent, therefore it cannot
import foreign-trained clinicians either. Every medic in the nation was made in Tepenia.** That makes the
training cities load-bearing national infrastructure in a way no other provider role is.

### Two pipelines, not one — the seam the setting already has

**Splitting them prevents one city becoming the answer to everything, which the differentiation guard would
flag on sight.**

| Tradition | Grows out of | Candidate | Causal chain from existing canon |
|---|---|---|---|
| **Settled medicine** — obstetrics, pediatrics, chronic and geriatric care | family life | **Esperanza** | educ/childcare 25% + the birth registry + rank-2 population → **a city built around birth becomes a city built around medicine** → obstetrics → pediatrics → general practice. *(Real-world: the first child born in Antarctica, civilian families, an actual school.)* |
| **Field medicine** — trauma, cold injury, rescue, air medevac, industrial accident | danger | **Belgrano** *(aviation 35%, the Halley subnet's primary airbase)* or **Marambio** *(aviation 30% + maritime 30%, the national air hub)* | **medevac is an aviation function** → whoever pulls casualties off the highways and the plateau treats them first → trauma tradition. **Dark horse: Fort McMurdo** (industrial 35% + extraction 25%) — a city that generates its own trauma and learns to treat it. |
| **⭐ Robot maintenance training** *(the unassigned counterpart)* | manufacture | **Sinheung** | builds the Cradle chambers shipped nationwide → **the city that builds the chambers robots are made in trains the technicians who service them.** Currently unassigned; three steps from canon. |

### Three consequences worth keeping

1. **A national social network the setting otherwise lacks.** Every city holds people who trained at Esperanza
   or Belgrano. **An NPC anywhere can be "Esperanza-trained," and it means something** — a shared institutional
   identity crossing subnet lines.
2. **A quiet civic sorrow.** A training city exports its brightest young people permanently, by design.
   **Esperanza raises them and loses them, continuously.**
3. **⚠ A strategic vulnerability with a decade-long fuse.** If every medic comes from two or three cities, then
   cutting those cities off kills nobody immediately — **it kills people six to ten years later, when the
   graduates who would have replaced the dead never arrive.** Worth having on the table well before the Long
   Night War.

> ## ✅ SETTLED — 2026-09-01, developer ruling. All three institutes codified to canon.
>
> `[CGRM 2026-09-01 · Path 6 · developer ruling]`
>
> - **The Esperanza Institute of Medicine** — with a substantial **Department of Pediatrics**
> - **The Belgrano Institute of Medicine** — with a substantial **Department of Emergency and Trauma Response**
> - **The Sinheung Institute of Cybernetics and Robotic Care** — with a strong, pronounced focus on the
>   **physical and emotional care of and for robots**
>
> **Deposited to:** `../National_Medical_and_Care_Institutes.md` *(full canon entry)* and each city's own
> `Specs/` **Notable Locations** section. **The gap this section opened is closed.**

---

# 4. The national food balance — the headline result

**Demand: 15,623,523 humans.** *(Kunlun and Dome Fuji contribute zero — 0 humans, and robots do not eat.
~178,000 residents removed from the national ledger by not eating.)*

**Supply, counting only the provider cities' food sectors** *(workforce = robots + 50% humans; marine sectors
discounted where they include port operations and non-food extraction)*:

| Provider | Workforce | Food sector | **Food producers** |
|---|--:|--:|--:|
| Davis | 876,515 | agriculture 35% | **306,780** |
| Esperanza | 1,400,619 | agriculture 15% | **210,093** |
| Janbogo | 987,241 | marine 20%, ~⅓ food | **65,816** |
| Juan Carlos | 291,821 | fishing 30% | **87,546** |
| Signy | 142,127 | fishing 30% | **42,638** |
| Cape Adare | 1,126,671 | marine 25%, ~⅓ food | **93,889** |
| Dumont d'Urville | 341,560 | marine 25%, ~⅓ food | **28,463** |
| | | **TOTAL** | **≈ 835,000** |

> ## **835,000 producers ÷ 15,623,523 humans = 1 food producer per ~19 people.**

**That closes.** One producer per 19 is entirely plausible for energy-intensive controlled-environment
agriculture plus commercial fishing — it sits between pre-industrial farming and modern greenhouse yields,
which is exactly where polar food production belongs.

### ⭐ But it only closes as a COALITION, and that is the real finding

**Davis alone: 306,780 producers ÷ 15,623,523 = 1 per 51.** Achieved in the Vestfold Hills — an ice-free polar
oasis of rock and hypersaline lakes, under 66 days of polar night. **Not credible.**

> **"The breadbasket of Tepenia" is a title, not a supply chain.** Davis is the largest single producer and
> the only one whose identity is *agricultural*, but it supplies roughly **37% of national food labor**. The
> other ~63% comes from Esperanza's farms and, above all, **from the sea** — Janbogo's year-round polynya,
> the Scotia Sea at Signy, Livingston Island at Juan Carlos, the Ross Sea at Cape Adare.
>
> **Tepenia is fed by fishing fleets at least as much as by farms**, and no city's §15 currently says so.

**Recommended structure — two-tier, and it is already half-canon:**

1. **Every city grows what it can locally.** The `City_Logistics.md` Concordia precedent — *"everything consumed
   in the city must be produced in the city or brought in at significant cost and risk"* — as baseline
   hydroponics covering a substantial fraction of local need.
2. **Providers cover the national deficit, the variety, and FULL supply to the cities that structurally
   cannot grow** — the plateau: Vostok, and formerly the Mountain Pass corridor.

---

# 5. Floor check — does anybody actually die?

**Floors computed as absolute headcount ÷ workforce.** *(⚠ Rates below are ASSUMED, not canon — see §6.)*

**Assumed rates:** primary healthcare 1 per 40 humans · water & sanitation 1 per 150 residents · construction
1 per 100 residents · thermal distribution 1 per 200 · emergency 1 per 300 · enclosure 1 per 500 · childcare
1 per 60 humans · mortuary 1 per 3,000 humans.

| City | Workforce | Non-outsourceable floor | Healthcare floor | Pilot's healthcare | Verdict |
|---|--:|--:|--:|--:|---|
| **Vostok** | 324,453 | **~5.0%** | **1.00%** | 1.6% | ✅ **PASSES** |
| **Casey** | 1,128,834 | ~6.4% | **1.63%** | 1.6% | ⚠ **MARGINAL** |
| **Cape Adare** | 1,126,671 | ~6.4% | 1.66% | 1.8% | ✅ passes |
| **{{Abowasa}}** | 782,123 | ~6.4% | 1.61% | 1.8% | ✅ passes |
| **Kunlun** | 123,449 | ~3.1% | **0%** | — | ✅ n/a — no humans |

> ## ⭐ **Vostok does not die — and the reason is its robots.**
>
> **At 67% robot against a ~51% national average, Vostok has 2.50 workers per dependent human** where the
> national norm is 1.54. **Its enormous machine workforce carries a small human population**, so the absolute
> need is met at a low percentage of the economy. **The pilot's alarming 1.6% healthcare and 2.0% food are
> survivable precisely because two-thirds of Vostok's workforce never needs a doctor, a school, or a meal.**

**This is a genuine characterization, not a reprieve on a technicality:** Vostok is a city where machines keep
a small, precious human population alive at the coldest inhabited place on Earth. **The demographic skew that
looked like a curiosity in the census is the thing that makes the city possible.**

### The real constraint at Vostok is energy, not headcount

Vostok's ~6,500 growers work out to **1 per 20 humans — better than the national average of 1 per 19.** But at
−54.8 °C, 3,488 m, under 121 days of polar night, **each grower's yield is a fraction of Davis's.** So Vostok
is labor-sufficient and **energy-insufficient**, which is the correct shape for it: not "too few farmers" but
"food here costs power the city does not have." **It remains a net importer — and its lifeline is Hwy 37.**

---

# 6. ⭐ THE GEOGRAPHIC LAYER — real-world geology and marine biology, per developer instruction

> *"Make sure to take real-world geography/geology/climate into account. That's part of the reason we have the
> GPS locations for all these cities… Situations like this are why I made sure to ground those locations in
> actual real-world geography."* — 2026-09-01

**§4 above used climate and ignored geology and marine biology. For a food question that is the half that
matters most, and correcting it moves the answer's center of gravity.**

## 6.1 Krill — and Tepenia's food problem is not what §4 said it was

**Signy is the South Orkney Islands. Juan Carlos is Livingston Island, South Shetlands. Both sit directly on
the largest concentrated protein resource on Earth.**

| Real-world figure | Value |
|---|--:|
| Circumpolar Antarctic krill biomass *(best estimate)* | **379,000,000 tonnes** |
| Krill biomass, South Orkney survey area alone (60,000 km²), 2011–2020 | **1.4 – 7.8 million tonnes** |
| CCAMLR reference exploitation rate | **9.3%** |
| Real-world commercial landings, recent | >450,000 t/yr *(trigger limit 620,000 t)* |

**The fishery is concentrated in exactly four places: the South Shetlands, Bransfield Strait, the South
Orkneys, and South Georgia** — i.e. the Palmer subnet's own waters.

**Against national demand:** 15,623,523 humans at ~365 kg food/person/year ≈ **5.7 million tonnes per year.**

> ## **The circumpolar krill resource exceeds national food demand by roughly two orders of magnitude.**
> **At CCAMLR's own 9.3% reference rate the sustainable circumpolar harvest is ~35 Mt/yr against a 5.7 Mt/yr
> national requirement.** Even a conservative fraction of that closes the books on its own.

**⭐ So the constraint was never the resource. It is harvesting fleet, processing capacity, and haulage.** And
krill has a real, specific, unglamorous processing problem worth having: **the exoskeleton carries fluoride
that must be removed, and the catch degrades enzymatically within hours of coming aboard** — so processing is
time-critical and happens at or near the water. **That is a genuine industry, sited by biology.**

### What this does to §4's conclusion

**§4 said Tepenia is fed by a coalition in which Davis is the largest single member. The geography says
something stronger and stranger:**

> **Tepenia is fed by the Scotia Sea. Davis is the nation's *farm*, but the Palmer subnet is its *larder*** —
> and Signy, at 188,694 people the fourth-smallest city in the country, sits on top of the single most
> important food resource the Federation has. **Its size is not a limitation; krill fishing is capital-
> intensive, not labor-intensive.** A fleet does not need a million people.

**And it recasts the Peninsula.** Esperanza, Juan Carlos, Palmer City, Rothera, Signy, Port Lockroy, Sejong
and Marambio are not merely the mild, pleasant cities — **they are where the food is.** That is a strategic
fact with obvious consequences the moment anyone contests it.

## 6.2 Ice-free ground — <1% of the continent, and it decides who can build

**Ice-free "oases" are the only places in Antarctica with actual rock underfoot. Real areas:**

| Oasis | Area | Tepenian city |
|---|--:|---|
| **Bunger Hills** | **450 – 942 km²** | ⚠ **NONE — unclaimed** |
| **Vestfold Hills** | **~410 km²** | **Davis** |
| Larsemann Hills | **~40 km²** | **Zhongshan · Sinheung · Shirayuki** *(all three)* |
| Schirmacher Oasis | **~35 km²** | **Lazar** |

### Three findings, in ascending order of importance

1. **Davis's breadbasket designation is geologically correct.** It holds the second-largest ice-free area on
   the continent — ~410 km² of rock, meltwater lakes and Prydz Bay access, at −10 °C. **Canon picked the right
   city, and this is real-world grounding validating a call already made.**

2. **⚠ Lazar is Tepenia's LARGEST city (2,620,319) on one of its SMALLEST oases (~35 km²).** That is ~74,900
   residents per km² of ice-free ground. **Lazar must be extraordinarily vertical and dense, must extend well
   out onto the ice beyond the rock, and cannot be an agricultural provider despite sitting on an oasis.** The
   same applies, harder, to the **Larsemann Hills cluster: three cities totaling 3,527,096 people sharing
   ~40 km².** **The Tri-Cities are not three cities near each other — they are three cities on one small
   rock**, which is a far better explanation of their cluster economy than proximity alone.

3. **⚠ The largest ice-free area in East Antarctica has no city on it.** Bunger Hills — 450 to 942 km², bigger
   than Vestfold — sits on the Knox Coast between Mirny and Casey, **unclaimed in canon.** **See §6.4 — the
   developer has since taken this up as a candidate city site, and the geology is stronger than this entry
   assumed.**

## 6.4 ⭐ THE BUNGER HILLS CITY — candidate site, developer-initiated 2026-09-01

> *"There could easily be a city built at Bunger Hills (no idea yet what it could be called)."*

**Real-world basis** *(66°15'S, 100°45'E, Knox Coast, Wilkes Land — "Bunger Oasis")*:

| Fact | Consequence for a city here |
|---|---|
| **⭐ Lake Figurnoye — the LARGEST FRESHWATER LAKE IN ALL OF ANTARCTICA**, in a lake system reaching ~140 m deep, most lakes not ice-covered year-round | **The cheapest water in Tepenia by an enormous margin** |
| **Ice-free year-round; 450–942 km²** — largest in East Antarctica | Rock foundations, no ice engineering; room to expand |
| Position between Mirny (93°E) and Casey (110°E) | Sits naturally on **Hwy 110 (the Coastal Cut Highway)**, filling a real gap in that chain |

### ⭐ Why the water fact is the whole city

**Every other Tepenian city pays the full latent heat of fusion to turn ice into water** — A2 is a Tier-A
survival industry everywhere, and the pilot scored it at 3.9–10.2% of municipal economies. **A Bunger Hills
city draws from standing liquid fresh water instead.**

**Its A2 burden would be the lowest in the nation, and that single fact should shape everything about it:**
what it exports, who resents it, and — the interesting question — **what "wasting water" means in the one
place where water is not scarce.** In a nation where meltwater is metered, registered and paid for, a city
with a lake is a moral anomaly as much as an economic one.

**Combined with ice-free rock, it is the obvious second agricultural region** — which resolves the
Davis-alone problem structurally, rather than by inflating Davis's share past credibility.

### Founding story — built, given away, abandoned, and woken up 43 years later

**Corrected and expanded 2026-09-01 after the developer asked whether a real station exists there. It does,
and the actual history is stronger than the first draft of this section.**

| Year | Event |
|---|---|
| **1957** | USSR builds **`Oazis`** station in the Bunger Oasis — two buildings, eight people |
| **Dec 1958 / Jan 1959** | **DONATED TO POLAND**; formally acquired by the Polish Academy of Sciences and renamed **`A. B. Dobrowolski Station`**, on the shore of **Algae Lake**. **Poland's only station on mainland Antarctica** *(Arctowski is offshore, King George Island)* |
| **1979** | **ABANDONED.** Goes dark. |
| **1979 → 2021** | **Dormant for 43 years** |
| **10 Nov 2021** | A team sails from Bremerhaven aboard a Russian icebreaker **to reactivate it** |
| 1986 · 1987 | Australia's **`Edgeworth David Base`** (northern Bunger Hills, summer-only field base); USSR's **`Oazis 2`** |

> ## ⭐ And the reactivation's stated purpose is almost uncomfortably on-theme.
> **The revitalized station is to serve as a base for erecting AUTONOMOUS geophysical stations on the exposed
> rock** — a station brought back from four decades of silence specifically **to host machines that run
> without people.** In this project, that is not a detail to leave on the table.

**What this gives a city that does not exist yet: a founding inheritance unlike any other in Tepenia.**

- **Davis** was continuously operated. **Casey** was kept genuinely functional across the centuries.
  **Abowasa** inherited two live, adjacent national stations.
- **Bunger Hills inherited a place that was built, given away, used, walked away from, and left in the dark
  for two generations before anyone came back** — while sitting on the largest ice-free ground and the largest
  freshwater lake on the continent the entire time.

**Three nations' fingerprints — Soviet, Polish, Australian — and no continuous human presence at any of them.**
**Poland has no other foothold anywhere in the Tepenian city roster.**

### ⚠ Naming — developer's call, per the binding no-invented-names rule

**Candidates from the real site:** `Dobrowolski` · `Oazis` · `Bunger` · `Figurnoye` · `Edgeworth David`.

*Noting only that **"Oazis" literally means oasis**, is the site's original station name, and describes exactly
what the place is — the water-rich, ice-free anomaly on a frozen continent.* **Not selected here.**

## 6.5 The maritime counterpart to "breadbasket" — researched, and there isn't one

> *"While Davis is 'the breadbasket of Tepenia', the maritime of that would be… something like 'the fishbucket
> of Tepenia' (unless there's already a maritime equivalent vocabulary term that I'm not aware of)."*

**Checked. English has no established equivalent of "breadbasket" for fishing regions** — "seafood basket" is
a fried dish. **The real-world convention runs differently: productive fishing grounds are named as `Banks`**
— the Grand Banks, Georges Bank, Dogger Bank. A *bank* is a shallow, productive ground, and that is the actual
working maritime vocabulary.

### ⚠ And a distinction the question surfaces, worth keeping

**"Breadbasket" names a region that PRODUCES. Davis grows the food.** But **Signy does not produce krill — the
Scotia Sea does, and Signy harvests it.** The parallel is therefore not exact, and Tepenia probably wants
**two** terms:

| | Term | Register |
|---|---|---|
| **The grounds** *(the sea itself)* | **"the Banks"**, or a named bank | Real maritime vocabulary; plain and functional, exactly as "breadbasket" is |
| **The port** *(the city or coalition that lands and processes it)* | a colloquial coinage — the developer's **"fishbucket"** sits here | Informal, which is correct: "breadbasket" is itself colloquial |

**Third option worth weighing: "larder."** Genuinely used for food-storing regions, and it carries a
whole-nation connotation that **suits a coalition better than a single city does.**

## ✅ RULED — 2026-09-01: the official word is **FISHBUCKET**

> ## **"the fishbucket of Tepenia"** — the official counterpart to **"the breadbasket of Tepenia."**
> `[CGRM 2026-09-01 · Path 6 · developer ruling]`

**"Banks" was considered and rejected, for a stated reason worth preserving:**

> *"'Banks' can be confusing for people who are not familiar with the fishing and/or maritime industry
> (compared to the word 'breadbasket', which doesn't require any industry-familiarity)."*

**⭐ That is the correct test, and it is the one "breadbasket" itself passes.** "Breadbasket" is legible to
anyone who has ever seen bread; it requires no agricultural knowledge whatsoever. **A counterpart term that
demands maritime literacy is not a counterpart — it is a jargon term wearing the same hat.** "Fishbucket" is
plain, concrete, and immediately understood by someone who has never been on a boat. **It matches the
register of the word it pairs with, which is the whole job.**

**⚠ Still open: WHO holds the title.** §4 established that Tepenia's food supply is a coalition, not one
place — Signy (South Orkneys) and Juan Carlos (South Shetlands) sit on the krill grounds, Janbogo works a
year-round polynya, Cape Adare the Ross Sea. **The developer has floated the Palmer subnet collectively, a
single city, or a formal coalition of cities.** Undecided.

**⚠ Deposit note:** "breadbasket" lives in Davis's `Background-Lore/` vignettes and course-of-events files
rather than in any central glossary. **"Fishbucket" therefore has no permanent home until its holder is
named** — it is recorded here as canon, and must be deposited into the holder's own files once that ruling is
made.

> **⚠ Ice-free does NOT mean arable.** These are polar deserts: no soil, and hypersaline lakes *(Davis's Deep
> Lake stays liquid below −20 °C)*. **Food production is greenhouse and hydroponic regardless of geology.** The
> real advantage of an oasis is different and was missed entirely by the burden model: **rock foundations
> instead of ice engineering, and summer meltwater instead of fuel-fed ice melt.**

## 6.3 Two driver corrections this forces on `01_Burden_Scoring_Model.md`

1. **NEW DRIVER — ice-free ground.** Reduces **A4 construction** *(build on rock; no ice-movement engineering,
   no structural relocation)* and **A2 water** *(summer meltwater lakes vs. melting ice at full latent-heat
   cost)*. **Davis, Lazar and the Tri-Cities should all carry a discount the model currently does not give
   them.** Contrast Halley, whose §15 already names *"ice engineering, structural relocation planning"* —
   a city built on a floating shelf, which should carry the opposite penalty.

2. **⚠ DENISON'S WIND IS BADLY UNDER-SCORED.** Cape Denison, Commonwealth Bay is **the windiest place on Earth
   at sea level** — Mawson's *"Home of the Blizzard,"* mean annual winds around 22 m/s with gusts far beyond.
   The pilot's highest wind multiplier was **Casey at 1.45 for 7–10 m/s.** **Denison should sit at the corpus
   maximum, roughly 2.0**, and its §15's unusual `Structural/wind engineering: ~25%` is not an eccentricity —
   **it is the correct response to a real place, and the model must be able to reproduce it.**

---

# 7. ⚠ What is NOT established here

1. **Every per-capita rate in §5 is assumed.** No canon rate exists for clinicians-per-population,
   growers-per-population, or utility staffing anywhere in the corpus. **The floor mechanism is structurally
   sound; its numbers are placeholders.** These are a developer ruling or a research task, and every verdict
   in §5 moves if they move.
2. **Marine-sector food fractions are estimated at ~⅓** where a §15 entry bundles fishing with port operations
   and non-food extraction. Cape Adare's 25% explicitly includes harbor operations and guano; Janbogo's
   includes bay industry. **Splitting those properly is per-city hand work.**
3. **Workforce participation for humans is assumed at 50%.** Artificial wombs, a male-skewed exile demographic
   and unclear retirement norms could move it materially.
4. **The 15 non-provider cities have not yet been needs-assessed individually** — §5 covers only the pilot
   four plus Kunlun. That is the next step.
5. **No provider city's own §15 has been touched**, per the set-aside instruction. Their internal subdivision
   is deferred, and several will need large upward revisions to their food or fabrication shares once the
   national books are balanced properly.
