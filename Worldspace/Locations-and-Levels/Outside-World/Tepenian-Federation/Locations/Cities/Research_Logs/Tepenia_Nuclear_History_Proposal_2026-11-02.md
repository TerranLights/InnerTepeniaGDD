# Tepenia's nuclear history: the developer's idea, tested against canon and the research (2026-11-02)

**Status: PROPOSAL AND ANALYSIS. Nothing here is ruled or canon.** Written at the developer's request so the discussion can be referred back to. Related files: `Locations/Infrastructure/Amundsen_Power_Supply.md` (the national grid draft), `Locations/Infrastructure/Geothermal_Heating.md` (the Concordia flag at its end), `Research_Logs/Tepenia_Nuclear_Power_Logistics_Research_2026-11-02.md` (the sourced research), `Research_Logs/Relung_Panen_Round2_Findings_and_Amendments_For_Approval_2026-11-02.md` (Relung's power).

---

## 1 · The developer's idea (2026-11-02)

Relung Panen's energy requirement turns out to be much lower than first calculated, while the national requirement turns out higher. That could be an in-world detail:
- In the beginning the Tepenians **honored the treaty** (no nuclear energy).
- As time went on they found they **absolutely needed nuclear energy to survive** and began establishing nuclear energy grids for themselves.
- That **resolved their energy problems (and so their food problems) in the short term.**
- Later it **caused a chain reaction of conflicts with Upper Earth** in the long term, worsening their political friction with their enemies.

*Question asked:* what would be the logistics, and would it actually work?

## 2 · Verdict

**It works, and the arithmetic supports the "absolutely needed" half.** Its weak points are a canon contradiction (Concordia), the source of the fuel, and what exactly alarms Upper Earth. Details follow.

---

## 3 · Why "they absolutely needed nuclear" holds up

| Quantity | Value | Basis |
|---|---|---|
| National electricity in the food/power model | **about 101.7 GW** | `Division_of_Industry/13`, EDEN-ISS section |
| Indoor staple growing at a "mature" 10 kWh/kg | **about 11.8 GW (11.6% of the above)** | same |
| Amundsen Tower's draw | **about 324 GW net, continuously** (about 2.16 TW gross, 85% regenerative recovery) | `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md` |
| Diesel for one gigawatt-year of electricity | **about 2.07 million tons** | research file, derived there from sourced figures |
| **Diesel for 101.7 GW** | **about 210 million tons a year** | **my multiplication** of the line above |
| Enriched uranium for one gigawatt-year (large light-water reactor) | **about 25 tons** | research file |
| **Uranium for 101.7 GW** | **about 2,500 tons a year** | **my multiplication** |

No freighter fleet carries 210 million tons of diesel a year to Antarctica, while 2,500 tons of uranium fuel is a manageable shipping load. So a nation that needs about 100 GW cannot exist on imported fuel. It needs a non-fuel source (nuclear, or the Tower's inferred fusion array), and geothermal is local to a handful of cities.

**Relung Panen fits.** Under the canon food model's own "mature" assumption (about 0.66 t of food per human per year at 10 kWh/kg), Relung's export food needs roughly **0.5 GW average**. Higher national total, modest city share: consistent with the developer's observation.

---

## 4 · How the story fits the treaty

- The **draft Article V.1** bans "any nuclear explosive device" and the "disposal of radioactive waste" in Tepenian territory, "without exception and without term". **It does not ban reactors.** (The draft is marked "not locked canon".)
- The **treaty scaffold's gloss** says the article "retroactively explains why Tepenia's civilization runs on the Amundsen Tower's grid-regulation model instead of nuclear power".
- **Proposal:** make the gloss an **in-world belief or official interpretation**. Tepenians read V.1 as a ban on nuclear energy and honored that for generations. The first political act was the *discovery* that the text only forbids explosives and waste disposal, so reactors are legal if the waste leaves. That reinterpretation is itself a source of friction.

---

## 5 · The logistics

**Fuel.** Tiny in tonnage (about 2,500 t a year at full national scale), but it **must come from outside**: nothing in canon mines uranium in Antarctica. That is a dependency on Upper Earth from the first day.

**Waste.** The heavy part. In the research: the McMurdo reactor (1.75 MW, 1962–1972) shipped out **12,000–14,000 t of soil plus the dismantled plant over six years** (sources disagree on tonnage and destination); Bilibino's spent-fuel removal was costed at **40–70 billion roubles**, with shipping possible only four months a year. At national scale, **waste export is a permanent, costly flow that Upper Earth controls** (ports, ships, disposal sites). If it refuses, Tepenia must **store** waste on site, and the line between storage and "disposal" (which V.1 forbids) is a political one.

**Scale (my arithmetic from the research file's unit sizes):**
- About **10 floating RITM-200S-class units (106 MW each) per gigawatt**, so roughly **a thousand** for 101.7 GW; or roughly 100 large units if each is 1 GW (that unit size is my assumption, not in the research file); or about 200 five-megawatt microreactors per gigawatt.
- These sit on **rock by the sea**. The research found **no nuclear plant ever sited on an Antarctic ice shelf or sea-ice coast** (McMurdo's was on rock), so ice-shelf cities need floating units, transmission, or another source.
- **Transmission:** high-voltage DC loses about 3.5% per 1,000 km (AC about 6.7%); sourced isolated-grid lines run about 490–500 km (110 kV); the longest clearly sourced nuclear district-heat pipe is 23 km. So plants serve **clusters** of cities within a few hundred kilometers (the cluster table in the grid file).
- **Geothermal pairs** (Janbogo+Zukelli, Scott+Fort McMurdo, Pergamino+Contrapunto) already have heat and would not need a plant for it.

**Time.** The Tower was completed about 2688 (the Second Interwar Midpoint, plus or minus a couple of decades); the Long Night War's inciting incident is about 2762. The nuclear build-out has to land before or during the Tower's construction (the Tower's 324 GW draw is the largest single demand) and long before the war.

---

## 6 · A plausible chain reaction with Upper Earth *(all proposals, none canon)*

1. **Fuel leverage.** Upper Earth supplies the fuel and takes the waste, so it can squeeze Tepenia whenever it likes.
2. **Enrichment and reprocessing.** To escape that dependence Tepenia is tempted to enrich fuel or reprocess spent fuel itself, which is exactly what alarms a world that remembers the nuclear war of 2083.
3. **Waste.** Storage that quietly becomes disposal is a treaty violation Upper Earth can cite.
4. **The Tower.** A reactor or fusion array at the South Pole powering a mass driver that moves about 270 tons a second looks like a weapon to any observer.
5. **Tinder and spark.** The nuclear friction is the **tinder**; the Palmer City incident of about 2762 (the confirmed inciting incident) is the **spark**. Nothing in the war's canon has to change.

---

## 7 · What would have to change in canon, and the weak joints

**Canon that conflicts or would change**
- **Concordia's Power Core is already geothermal and nuclear from the late 2560s** (`District_Canon_Reference.md`, `City_Logistics.md`, `Energy_Grid_Failure_Rationale.md` §1). That contradicts "honored the treaty at first". Ways to reconcile:
  - (a) Make Concordia's early core geothermal only, with the nuclear part added in the later crisis.
  - (b) Keep it as a small authorized exception (waste shipped out), with the national build-out a later, larger step.
- **The scaffold's gloss** (Timeline repo, `Reference/Falkland_Treaty/Scaffold.md`): becomes an in-world belief. That file is in the perfect-canon Timeline repo, so any edit there is the developer's.
- **`Geothermal_Heating.md`'s "only six cities" line**: already flagged (options A, B, C there).
- **The Tower design file's inferred reactor array**: consistent with this story, not yet a ruling.

**Weak joints (decisions)**
1. **Where does the uranium come from?** (Imports from Upper Earth is the simplest; it is also the leverage.)
2. **Is the alarm mainly the fuel cycle (enrichment, reprocessing) or the Tower's mass driver?**
3. **How long did the "honoring" last?** (decades, a century?)
4. **Does the nuclear build-out belong to the Tower's construction (to power it) or does it precede it?**
5. **Does Concordia's early core stay or change?** (options a, b above)
6. **What happens to the waste** (shipped out, stored, reused)? See the follow-up question below.

---

## 8 · Follow-up question raised the same day

*Can nuclear waste actually be used for anything?* Research started 2026-11-02 (unit R7); results will be added to `Research_Logs/Tepenia_Nuclear_Waste_Reuse_Research_2026-11-02.md`. Why it matters here: reuse (reprocessing, fast reactors, isotopes) could shrink the waste that must leave Tepenia, but reprocessing creates plutonium, which is exactly the alarm in §6 item 2.

---

## 9 · Direction chosen for the initial stages (2026-11-03, at the developer's direction; NOT yet a numbered ruling)

**What the developer said (2026-11-02 evening / 2026-11-03):** after the fusion, helium-3 and waste-heat research, the power situation would "start out" as **fission power in the beginning, against the wishes of Upper Earth, and then figure out something else, some other solution later on, possibly.** The developer wants the initial stages settled now ("for now, I think we can settle the initial stages power issue"), with further research on later possibilities continuing as work goes. This matches the proposal in §1 and §6 and Story option 2 in `Tepenia_Fusion_and_Uranium_Discussion_2026-11-02.md` §3.

**Taken as the working direction:**
1. **Initial stages are fission-powered.** Reactors are built in defiance of Upper Earth's wishes. The chain of friction in §6 (fuel leverage, enrichment or reprocessing alarm, waste, the Tower looking like a weapon, the Palmer City spark of about 2762) is the long-term consequence.
2. **Heat is used where plants sit near people.** Plant heat is reused for housing and for food production around coastal and rock-founded cities by cogeneration (research: `Heat_P2_…`, `Heat_P3_…`); the sourced limits are hot-water lines of about 26 to 75 km, an electricity cost of about 0.12 to 0.2 MWe per MWth of heat extracted, and housing demand of about 0.5 to 1.5 kW per person (derived from Fairbanks and Sisimiut; colder Antarctic cities may be higher).
3. **What replaces fission later is left open.** Candidates the research can support are in the discussion file §3 and §7 (fusion, which has no net-electricity device yet; helium-3 fusion, with no sourced supply; coastal generation with long-distance transmission, unresearched at this scale). The grid's canon instability from the Tower's fall onward means the replacement may simply be unfinished in the player's era.

**Still open (not decided by this direction):**
- The six weak joints in §7 above (uranium source; what exactly alarms Upper Earth; how long the "honoring" lasted; Tower versus build-out order; Concordia's early nuclear core; waste).
- **The Tower:** where its 324 GW is generated and where its heat goes. The ice at the Pole cannot take 600 GWth by melting or conduction (`Heat_P1_…`), so a Pole-sited array needs air or radiative rejection over thousands of square kilometers, or generation on the coast with long-distance transmission, or a different load. The Tower's own losses are also heat; no file says where they go.
- **Interior and shelf cities:** the deep-interior ice-sheet cities (Amundsen, Byrd, Concordia, Dome Fuji, Ariun Nuur, Kunlun) have small heat flows (about 1 GWth or less each) that the ice can take at that scale; the inland rock cities (Sanay, Santa Luce, Troll, Utstein, Lazar) have no sea sink; the three ice-shelf cities (Belgrano, Halley, Neumayer) risk melting the shelf they stand on. None is researched beyond the figures in `Heat_P1_…` and `Heat_P4_…`.
- **Plant sites and sizes** for every city except Concordia's Power Core and the Tower complex are NOT in the files.

**Status:** direction, not canon. No ruling number has been assigned and the rulings log has not been touched; the developer decides whether and when to record it as the next `DR-` entry.
