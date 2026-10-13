# Per-Subnet Overview — Reference Data (classification pass)

**Created 2026-10-05.** Companion to `Per-Subnet_Metacategories.md` (the developer's skeleton, **not edited**). This file is **classification, not worldbuilding** (developer, 2026-10-05): it only collects and organizes what existing canon already states about each subnet, so the skeleton's empty slots can be filled from sources.

**Frame:** Second Interwar, pre-war; Census I governs (`DR-4`); post-war statuses are excluded. City names are the current names (`City_Renames_Alias_Table_2026-10-03.md`). **Every row names its source.** A cell reading **"not collected"** means this pass did not read it, not that nothing exists. Nothing here is ranked or scored.

## 1 · The seven units at a glance

| Unit | DLC | Hub (official name) | Colloquial nickname | Region (Census heading) | Cities | Census I combined | Robot share |
|---|:-:|---|---|---|--:|--:|--:|
| **South Pole** (Amundsen) | 1 | Amundsen Station — **inter-subnet relay, not a subnet member** | none | South Pole | 1 | 6,857 | 83.65 % |
| **Byrd** | 2 | Byrd | "Pacific" | Marie Byrd Land / Ross Ice Shelf | 1 | 376,890 | 50.58 % |
| **Palmer** | 3 | Palmer City | "American" | Antarctic Peninsula | 8 | 4,319,961 | 50.03 % |
| **Mawson** | 4 | Mawson | *(none, by design)* | East Antarctic Indian Ocean coast | 3 | 1,727,181 | 53.50 % |
| **Halley** | 5 | Halley | "Atlantic" | Queen Maud Land / Weddell Sea | 8 | 9,724,879 | 50.86 % |
| **Janbogo** | 6 | Janbogo | *(none, by design)* | Ross Sea | 8 | 7,230,307 | 50.45 % |
| **Mirny** | 7 | Mirny | "Australian" (`DR-47`) | Wilkes Land / Prydz Bay coast and plateau | 9 | 8,640,525 | 52.40 % |

*Sources:* DLC numbers — memory `project_subnet_dlc_companion_reservation` and `project_inner_tepenia` (7 DLCs: one per subnet plus the Pole as DLC 1); hubs and nicknames — `City_Relationship_Database.md` §2 and `project_subnet_nicknames` (colloquial names are informal; official names are the hub city's); regions — `Official_Population_Census.md` Section A headings. **Census I figures are recomputed from the city rows** (`Official_Population_Census.md` Section B, with renamed cities mapped); the census's own "Subnet Totals" table is **stale** (it predates the 2026-09-05 changes and the 38th city; it reads Mirny 8,045,281 and Halley 9,986,911), so its figures are **not used** (docketed as Q-32). The seven rows sum to the census total, 32,026,600 (15,623,523 humans + 16,403,077 robots). Seven subnets, counting Amundsen separately (`DR-17`).
⚠ **Doc inconsistency, recorded:** `City_Relationship_Database.md` §2 still says "six subnets"; the census and `DR-17` say seven.

## 2 · The developer's "Broad-scale culture" labels, set beside the founders on record

The labels are the developer's and are kept exactly as written. The right-hand column is only what `Cities/Founding_Register.md` (all ✅ rows) says about founding nations in that subnet, so the labels can be read against it. **Under the culture law, a founding nation names the starting stock, never the culture** (`No_National_Stereotypes`); read each label as shorthand for a stock mix.

| Subnet | Developer's label | Founders on record (Founding Register) |
|---|---|---|
| Palmer | Latin-American | Palmer City: three groups united by relationship to robots, not nationality · Rothera: North American and Argentine industrial workers · Esperanza, Marambio: Argentina · Pergamino: Uruguay first, then Anglo and Latin additions · Puerto Abrigo: Chile · Contrapunto: Chile first, then English-speaking arrivals, then Palmer City invitees, later Korean translators · Signy: South Africa and Brazil |
| Halley | European | Halley: the UK · Neumayer: the Netherlands and Austro-Bavaria · Troll: Norway · Santa Luce: Italy and the CIN · Sanay: South Africa · Utstein: the Scandinavian Trade Union nations · Lazar: Russia (core) and the CIN · Belgrano: Argentina |
| Mawson | Altaic | Mawson: Kazakhstan, Russia and Australia (`DR-53`) · Temirötkel: the CIN or Kazakhstan first, then Kazakh industrialists · Dome Fuji: devout disciples, no country |
| Mirny | Sino-Australian | Mirny: Idelsk-Uralia, with Russia, Australia and the Sinian Federation as exile groups · Casey, Davis: Australia · Zhongshan: Chinese (the Sinian Federation) · Shirayuki: Japan · Sinheung: Korea · Ariun Nuur: Künnarantaiga and Mongolia · Kunlun: Ariun Nuur's stock plus the Sinian Federation (robots only) · Relung Panen: Indonesia and Malaysia |
| Janbogo | East Sinitic | Janbogo: Korea · Zukelli, Denison: Australia · Scott: New Zealand · Dumont d'Urville: Japan · Fort McMurdo: miners then administrators from all over Tepenia · Cape Adare: mixed, an empty slot by ruling · Concordia: no founding nation |
| Byrd | Anglo-American | Byrd: a joint team of first-wave Tepenians from the Peninsula and the Halley coast; **not** founded by any Upper Earth country |
| South Pole | Unification/Scientific | Amundsen Station: multi-subnet technical crews on rotation; no founding nation, neutral by design |

**Read-across notes for the developer (neither is a correction; the labels are yours):**
- **Janbogo** — the Register's founders are Korea ×1, Australia ×2, Japan ×1, New Zealand ×1, plus three cities with no single nation. "East Sinitic" fits Korea and Japan; I did not find where it comes from for the others. Worth confirming the label's scope.
- **Byrd** — the Register's founders are Tepenian first-wave settlers, not an Upper Earth nation, so "Anglo-American" reads as a composition label (the census composition) rather than a founding fact.
- **Mirny** — the subnet's stocks span China, Japan, Korea, Mongolia, Indonesia/Malaysia and Australia; "Sino-Australian" names the two largest founding presences, not the whole range.

## 3 · Per-subnet fact sheets

*Source key:* **REG** `Cities/Founding_Register.md` · **CEN** `Official_Population_Census.md` · **CRD** `Cities/City_Relationship_Database.md` · **HWY** `Infrastructure/Highways.md` · **AIR** `Infrastructure/Airports.md` · **PRT** `Infrastructure/Ports.md` · **UEIC** `Cities/Upper_Earth_Immigration_Composition.md` · **GEO** `Infrastructure/Geothermal_Heating.md` · **DR-n** `DEVELOPER_RULINGS_LOG.md`.

### Palmer — DLC 3 — "American"
| Field | Value | Source |
|---|---|---|
| Members (8) | Palmer City (hub) · Rothera · Esperanza · Marambio · Pergamino · Puerto Abrigo · Contrapunto · Signy | CRD §2 |
| Census I | 2,158,475 humans / 2,161,486 robots / **4,319,961** (robots 50.03 %); largest city Esperanza 1,878,287; smallest Puerto Abrigo 929 | CEN §B |
| Setting | The Antarctic Peninsula; mostly island and coastal sites; **Signy** is on the South Orkney Islands, reachable by sea alone (peripheral, intermittent Arcanet link) | CEN §A; CRD §2; AIR/PRT |
| Highways | **Hwy 1** (Esperanza → Marambio → ramps to Puerto Abrigo, Rothera → Byrd); Palmer City is reached by boat from its ramp. The **only land route** between the Peninsula and the rest of Tepenia; one overland thread shared with Byrd and the Mirny subnet | HWY; CRD §1; Cross-Subnet Part 1 |
| Airports | Rothera · Marambio (domestic) · Machu Picchu (the only international airport; near Contrapunto, connects to Ushuaia); Palmer City is air-disconnected by design | AIR |
| Geothermal heat | Pergamino and Contrapunto (with Scott/Fort McMurdo and Janbogo/Zukelli: the six volcanic cities) | GEO |
| Upper Earth gateway | South America → Marambio's port; **Ushuaia** is the primary port for Pergamino, Puerto Abrigo, Contrapunto and Signy (`DR-48`); Ushuaia is the port of transfer for people bound for the Peninsula (`DR-50`) | PRT §3, §3b–3d |
| Arcanet | Hub Palmer City; Amundsen Station was the inter-subnet relay pre-war | CRD §2 |

### Halley — DLC 5 — "Atlantic"
| Field | Value | Source |
|---|---|---|
| Members (8) | Halley (hub) · Belgrano · Neumayer · Sanay · Troll · Santa Luce · Lazar · Utstein | CRD §2 |
| Census I | 4,779,014 / 4,945,865 / **9,724,879** (robots 50.86 %); the largest subnet by population; Lazar 2,358,287 is the largest single city | CEN §B |
| Setting | Queen Maud Land and the Weddell Sea. **Halley** sits on a moving ice shelf and has **no docks or airstrip of its own** (its architecture exists because the ice moves); Belgrano and Sanay are the subnet's receiving ports | CEN §A; PRT §5.2; TWR |
| Highways | **Hwy 7** (Belgrano → near Halley by connecting road → Santa Luce → Neumayer ramp → Sanay → Troll → Lazar), **Hwy 7-ext** (Lazar → Utstein → the Temirötkel Junction; built 2611–2614, the only dated highway), **Hwy 59** (connector to Hwy 22; carries the Arcanet cable) | HWY |
| Airports | Troll · Belgrano (2) | AIR |
| Upper Earth gateway | South Africa → Sanay and Belgrano, interchangeably by season (Cape Town; ~100 days a year) | PRT §3; TWR |
| Arcanet | Hub Halley | CRD §2 |

### Byrd — DLC 2 — "Pacific"
| Field | Value | Source |
|---|---|---|
| Members (1) | Byrd (hub and only city) | CRD §2 |
| Census I | 186,268 / 190,622 / **376,890** (robots 50.58 %) | CEN §B |
| Setting | Marie Byrd Land / the Ross Ice Shelf side; deep West Antarctica | CEN §A |
| Highways | Western end of **Hwy 1** and western end of **Hwy 22** meet here; the only overland link to the rest of the country runs through the Palmer subnet | HWY; CCSR Part 1 |
| Airports | Byrd (domestic) | AIR |
| Founding | A joint team of first-wave Tepenians from the Peninsula and the Halley coast; no Upper Earth nation | REG |
| Arcanet | Hub Byrd | CRD §2 |
| Other | One of only two active chamber manufacturers, with Sinheung (Cradle network) | CRD; AIR |

### Janbogo — DLC 6 — no nickname
| Field | Value | Source |
|---|---|---|
| Members (8) | Janbogo (hub) · Zukelli · Cape Adare · Fort McMurdo · Scott · Dumont d'Urville · Denison · Concordia | CRD §2 |
| Census I | 3,582,621 / 3,647,686 / **7,230,307** (robots 50.45 %) | CEN §B |
| Setting | The Ross Sea coast, plus Dumont d'Urville and Denison on the Adélie and George V coast, and **Concordia inland on the plateau (Dome C)**. Janbogo and Zukelli share a **year-round, wind-held port** (the polynya), an airport, and geothermal heat; Fort McMurdo and Scott share an ice pier; Fort McMurdo is the **de facto national capital** (relation only) | CRD; PRT §4, §5.3; REG; `DR-21` |
| Highways | **Hwy 183** (Concordia → Janbogo/Zukelli/Cape Adare by connecting roads → Denison → Dumont d'Urville), **Hwy 175** (to the Pole), **Hwy 2** (junction with Hwy 110 → Casey → Dumont d'Urville) | HWY |
| Airports | Zukelli/Janbogo (shared) (1) | AIR |
| Geothermal heat | Janbogo, Zukelli, Scott, Fort McMurdo (two of the three volcanic pairs) | GEO |
| Upper Earth gateway | New Zealand → the Ross region (Christchurch/Lyttelton; the Ross node is "under-specified", `PRT` §6); **Hobart** is the primary port for Dumont d'Urville and Denison (`DR-48`) | PRT |
| Arcanet | Hub Janbogo | CRD §2 |
| Other | **Concordia is the main game's setting** (Capricorn and Sagittarius districts); the main game is set in the Janbogo subnet's plateau city, while the subnet's own DLC (6) covers the Ross Sea coast | memory `project_inner_tepenia`; CRD |

### Mawson — DLC 4 — no nickname
| Field | Value | Source |
|---|---|---|
| Members (3) | Mawson (hub) · Temirötkel · Dome Fuji | CRD §2 |
| Census I | 803,085 / 924,096 / **1,727,181** (robots 53.50 %); Dome Fuji is entirely robot (55,072) | CEN §B |
| Setting | The East Antarctic Indian Ocean coast plus the high plateau. **Mawson has the only natural rock harbor** (geological port); Temirötkel's bay freezes in (needs an icebreaker); Dome Fuji is a plateau city at ~3,810 m | PRT §5.3; CRD |
| Highways | **Hwy 4** (the Temirötkel Junction → Mawson → Sinheung → Shirayuki), **Hwy 37** (the Temirötkel Junction → Dome Fuji → Kunlun → Ariun Nuur → Concordia), the **Temirötkel Spur**; the junction is the three-way crossing of Hwy 4, 7-ext and 37 | HWY |
| Airports | **None — the only subnet with zero air access**; every pilgrim to Dome Fuji arrives overland | AIR |
| Upper Earth gateway | Australia → Mawson (three-node with Dumont d'Urville and Mirny); the neutral-transshipment hubs serve Temirötkel and Mawson | PRT §3; Neutral Transshipment |
| Arcanet | Hub Mawson | CRD §2 |
| Founding | Kazakhstan, Russia and Australia (Mawson, `DR-53`); the CIN or Kazakhstan first, then Kazakh industrialists (Temirötkel); devout disciples (Dome Fuji) | REG |

### Mirny — DLC 7 — "Australian"
| Field | Value | Source |
|---|---|---|
| Members (9) | Mirny (hub) · Ariun Nuur · Kunlun · Casey · Zhongshan · Davis · Sinheung · Shirayuki · Relung Panen | CEN §A; Mirny pass `FRM` R-3 |
| Census I | 4,112,939 / 4,527,586 / **8,640,525** (robots 52.40 %); Kunlun is entirely robot (123,449) and Ariun Nuur is robot-heavy | CEN §B |
| Setting | The Prydz Bay, Davis Coast and Wilkes Land coast, with the high plateau (Kunlun, Ariun Nuur). **Davis is the principal Indian-Ocean-sector import port** (`PRT`); the Tri-Cities (Zhongshan, Sinheung, Shirayuki) share one port, one airport and one oasis | PRT §5.6c; UEIC; AIR |
| Highways | **Hwy 110** (Zhongshan → Davis → Mirny → Casey → Concordia), the Zhongshan/Sinheung/Shirayuki tri-junction (Hwy 4, 22, 110 meet), **Hwy 37**'s Kunlun and Ariun Nuur stretch | HWY |
| Airports | Mirny · Tri-Cities (shared) (2), plus the Mountain Pass outpost airstrip on Hwy 37 | AIR |
| Upper Earth gateway | Australia → Mirny, Mawson, Dumont d'Urville; **Hobart** is the primary port for Relung Panen (`DR-48`) and Hobart/Fremantle the people port of transfer for the Asian span (`DR-50`) | PRT §3, §3d |
| Arcanet | Hub Mirny; **nine members routed through its relay** | CEN; Mirny pass |
| Other | Sinheung is one of only two chamber manufacturers; Mirny supplies its raw material | CRD; AIR; Mirny pass |

### South Pole (Amundsen) — DLC 1
| Field | Value | Source |
|---|---|---|
| Members (1) | Amundsen Station (6,857 people; 1,121 humans, 5,736 robots, ~84 % robot) | CEN §B |
| Role | **The inter-subnet relay, neutral ground, not a member of any subnet**; all cross-subnet Arcanet traffic routed through it pre-war | CRD §2 |
| Highways | **Hwy 22** passes directly through it; **Hwy 59** and **Hwy 175** ramp onto Hwy 22 near it | HWY |
| Founding | Multi-subnet technical crews on rotation; no founding nation | REG |

## 4 · Cross-subnet connections already in canon *(relation only; no comparison)*
Collected from `City_Cross_Subnet_Relationships.md` Parts 1–2 and `Highways.md`. Any tie that rests on a station, an operator, a namesake or "heritage" is **not** carried (`DR-19`).
- **Peninsula ↔ Byrd ↔ Mirny subnet:** one overland corridor (Hwy 1 → Hwy 22), shared by three subnets.
- **Mirny subnet ↔ Janbogo:** Hwy 2 (Casey ↔ Dumont d'Urville) and Hwy 110 (the Mirny coast ↔ Concordia).
- **Halley ↔ Mawson ↔ Mirny subnet ↔ Concordia:** the Temirötkel Junction (Hwy 4, 7-ext, 37); every Halley city is one junction from Mawson, the Mirny subnet and Concordia.
- **Hwy 59:** the Halley subnet's inland link to Hwy 22, carrying the Arcanet cable.
- **Mawson ↔ Mirny subnet:** Hwy 4 (Mawson → Sinheung → Shirayuki) and Hwy 37 (Dome Fuji ↔ Kunlun ↔ Ariun Nuur).
- **Pole:** all inter-subnet signal; the end of Hwy 175 and Hwy 59's Hwy 22 ramps.

## 5 · What this pass did not collect (candidate fields for the empty slots)
Not collected: climate and ice behavior per subnet (specs and the Climate READER), per-subnet industry/economy (`Division_of_Industry/`), per-subnet DLC quest plans (the DLC design files), per-subnet flora/fauna and visual palette, and the Concordia-relative position of each subnet. These are sources, not decisions.

## 6 · Proposed category set for the skeleton's empty bullets *(proposal only; the developer chooses)*
The skeleton gives **7 or 8 unlabeled bullets** per subnet (Palmer, Halley, Mawson, Mirny and the Pole have 7 blank bullets plus a trailing one; Janbogo has 6; Byrd has 8). If one set of labels is wanted for all seven, this fits the data above:
1. **Founding stock** (the Register row; composition, not culture)
2. **Physical setting and access** (coast / plateau / shelf / island; how it is reached)
3. **Network role** (Arcanet hub; the relay; cross-subnet ties)
4. **Upper Earth gateway and supply** (partner nation; primary ports)
5. **Infrastructure** (highways, airports, ports, shared facilities)
6. **Scale** (cities; Census I; robot share)
7. **Economic function** (needs `Division_of_Industry/`; not yet collected)
8. **DLC identity** (DLC number; companion slot; what the subnet's DLC is structurally)

Each is a **classification axis**, not a verdict. Differentiating the DLCs from each other is then a matter of how the filled values differ, decided by the developer.
