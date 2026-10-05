# Founding Register

**The single home for every Tepenian city's founders.** Created 2026-10-01 at the developer's direction, as the
root-level fix for the station-heritage mistake (`Station_Heritage_Removal_Tracker.md`, "READ THIS FIRST").

## ⛔ The rules this file enforces

1. **Founders are decided here and nowhere else.** No spec, culture sheet, megasheet, catalog, census tag, robot-culture
   sheet, datasheet or ULM pass may originate or restate a founding claim that this file doesn't hold. They **point to
   this file**.
2. **A founding nation stands on geography and access, never on the real station** (`DEVELOPER_RULINGS_LOG.md`
   `DR-19`). A real station, the nation or program that ran it, and its start year are facts about **infrastructure**
   only (`DR-24`). They are never a reason for who founded the city.
3. **State each founding on the city's own geography and access. Never justify it by comparison to another city** (developer, 2026-10-01).
4. **Only the developer changes a row's status.** A session may *propose* (in the Notes column, marked "proposed").
   It may never mark a row ✅.
5. **Post-war framing comes later.** Rows name founders in pre-war terms for now. Recasting them in post-war nations
   (`Post-War_Nations_Founder_Reference.md`) is a CST task (`DR-23`).
6. **Checked by reading, not searching.** `Universal_Location_Methodology/Tools/check_founders_against_register.py`
   lists every place a city's files disagree with this register. That list says where to **read**; the reading is the
   check.

**Status key:**
- ✅ **ruled** by the developer.
- 🟡 **canon, not re-ruled since `DR-19`**: established in earlier canon; not yet checked against the geography rule.
- ⏸️ **open**: no ruling yet; nothing may be written as fact.
- ⛔ **overturned**: the spec's current founders are wrong; the city awaits its revisit.

**Solar UTC** = round(longitude ÷ 15), the measure `DR-19`/`DR-22` use for time-zone proximity.

## The register

The **Not founders** column lists nations the developer has ruled out for that city. The check script flags any of
the city's files that still name them as founders.

| City | Subnet | Solar UTC | Status | Founders | Basis | Source | Not founders |
|---|---|---|---|---|---|---|---|
| Palmer City | Palmer | −4 | ✅ | Three groups united by relationship to robots: exiled robots, human partners, human ideological supporters — **not by nationality** | Founding of the Federation itself; settled 2564-06-21 (`DR-16`) | `Specs/Palmer subnet/Palmer_City.md` L218; `DR-16`, `DR-44` | — |
| Rothera | Palmer | −5 | ✅ | *"primarily, most notably established by industrial workers from North America and Argentina, though with other nations being represented"* | Geography/access. Argentina stays a founder alongside North America (`DR-44`, closing `FQ-13b`); `DR-22`'s "only Belgrano, Marambio and Esperanza" described the specs as they then stood | `DR-20`, `DR-44` | British |
| Esperanza | Palmer | −4 | ✅ | Argentina | *"almost immediately accessible"* from Argentina | `DR-19`, `DR-22` | — |
| Marambio | Palmer | −4 | ✅ | Argentina | *"almost immediately accessible"* from Argentina | `DR-19`, `DR-22` | — |
| Pergamino | Palmer | −4 | ✅ | A primarily Anglo-Latin society of immigrants from the Americas (`DR-20`); **first founders: Uruguay**, with the later Anglo and Latin additions of that ruling | Geography/access: zone gap 0; the Río de la Plata is the Atlantic-side gateway to the South Shetlands. *(Gateway claim not yet researched.)* | `DR-20`, `DR-34` | Spanish |
| Puerto Abrigo | Palmer | −4 | ✅ | **Chile** | Geography/access: Wiencke Island faces the Drake Passage's Pacific mouth; the nearest populous gateway on the whole continental side is Chile's Magallanes coast; zone gap 0. *(Gateway claim not yet researched.)* | `DR-34` | — |
| Contrapunto | Palmer | −4 | ✅ | **A primarily Anglo-Latin society of immigrants from the Americas (`DR-20`). First founders: Chile; then English-speaking arrivals; then people invited from Palmer City (canon: it has representation from every country), and later from Korea, to translate the inherited station's records, logs and manifests (written in Korean).** Developer: *"roughly, approximately akin to the Dutch foundings of New Amsterdam eventually producing New York City (although on a much… smaller scale)"* | Geography/access: zone gap 0 (Chile); the translators are later waves, not founders. *(Gateway claim not yet researched.)* | `DR-20`, `DR-35` | South Korean (as founders) |
| Signy | Palmer | −3 | ✅ | South Africa and **Brazil**, jointly (South Africa partly, as ruled in `DR-22`) | Developer ruling (South Africa ≈ 5 zones; the composition file cites the Cape Town–South Orkneys crossing). Brazil: zone gap 0; the nearest large populous Atlantic coast on the Scotia Sea. *(Gateway claim not yet researched.)* | `DR-22`, `DR-44` | — |
| Halley | Halley | −2 | ✅ (partial) | The UK, in a central role | Two to three time zones | `DR-22` | — |
| Neumayer | Halley | −1 | ✅ | **The Netherlands and Austro-Bavaria, jointly** | Time-zone proximity: the Netherlands gap 1, Austro-Bavaria gap 2. Developer: they *"would be able to make the quickest re-upstart of the setting"* | `DR-35` | — |
| Troll | Halley | 0 | ✅ | Norway | Near-perfect time-zone alignment | `DR-22` | — |
| Santa Luce | Halley | −1 | ✅ | Italy and the Confederacy of Intermarium Nations (CIN), jointly | Time-zone proximity | `DR-22` | Finnish, Swedish |
| Sanay | Halley | 0 | ✅ | South Africa | Developer ruling (the one African founder besides part of Signy) | `DR-22` | — |
| Utstein | Halley | +2 | ✅ | The Scandinavian Trade Union nations, jointly | Time-zone proximity; Belgium did not exist in 2564 | `DR-22` | Belgian |
| Lazar | Halley | +1 | ✅ | **Russia (the core state) and the CIN, as two communities that coalesced** (the second community replaces the spec's Indian half: no South Asian population ever came to Tepenia, `NNS` L44) | Time-zone proximity: the CIN gap 0, Russia's core (+2…+3) gap 1 | `DR-34` | — |
| Belgrano | Halley | −2 | ✅ | Argentina | Accessible from Argentina | `DR-19`, `DR-22` | — |
| Mawson | Mawson | +4 | ✅ | **Kazakhstan, Russia (the core state) and Australia, jointly.** Australia restored (`DR-53`, reversing `DR-45`) | Kazakhstan: Mawson lies directly south of it (zone gap 0). Russia (core, +2…+3): zone gap 1. **Australia: geography and access (`DR-19`); its nearest zone is +8 against Mawson's +4, a gap of 4, a ruled exception (`DR-33`)** | `DR-19`, `DR-33`, `DR-45` (reversed), `DR-46`, `DR-53` | — |
| Temirötkel | Mawson | +3 | ✅ | **First established by the CIN or by Kazakhstan** (which of the two: open); then **industrialized primarily by Kazakh industrialists**, who made it the heavy-industry and shipping city it is in the Second Interwar Period | Time-zone proximity: *"near-perfect alignment"* (the CIN ≈ +1…+2, Kazakhstan ≈ +3…+6) | `DR-30` | Japanese |
| Dome Fuji | Mawson | +3 | ✅ | *"devout religious disciples, and not associated with any particular country"* (the Ice Cold Buddhism pilgrims) | Developer ruling | `DR-20` | Japanese |
| Mirny | Mirny | +6 | ✅ | **Founded by Idelsk-Uralia** (replacing Russia in the founding-nation role); **exile groups present: Russia, Australia and the Sinian Federation (China)** | Idelsk-Uralia (+2…+5): zone gap 1, against Russia's core (+2…+3) gap 3; developer: it would have *"a reasonably strong-enough economy to support doing so"* | `DR-9`, `DR-46` | — |
| Casey | Mirny | +7 | ✅ | Australia | *"extremely close… comparatively easy access"* | `DR-19` | — |
| Davis | Mirny | +5 | ✅ | Australia | *"extremely close… comparatively easy access"* | `DR-19` | — |
| Zhongshan | Mirny | +5 | ✅ | Chinese (state at the Treaty: the Sinian Federation; the people are Chinese) | The Sinian Federation's (i.e. China's) immediate geographic and time-zone access to the site: *"perfectly reasonable that in the 2500s, it would still be the Chinese who would have control over Zhongshan Station"* | `DR-21` | — |
| Shirayuki | Mirny | +5 | ✅ | Japan, by the Jeju-do court's diplomatic allocation | The Jeju-do court's diplomatic allocation, **and, in addition, geography**: zone gap 3 to the Prydz Bay coast (the edge of the rule). Developer: geography is an *additional* factor, not a replacement. | `Specs/Mirny subnet/Shirayuki.md` L175; `DR-44` | — |
| Sinheung | Mirny | +5 | ✅ | Korea, by the Jeju-do court's diplomatic allocation | The Jeju-do court's diplomatic allocation, **and, in addition, geography**: zone gap 3 to the Prydz Bay coast (the edge of the rule). Developer: geography is an *additional* factor, not a replacement. | `Specs/Mirny subnet/Sinheung.md` L189; `DR-44` | — |
| Ariun Nuur | Mirny | +7 | ✅ | **Künnarantaiga and Mongolia, jointly** (Künnarantaiga is one of the successor states of the old Russia in the developer's maps; **not** Russia itself) | Time-zone proximity: gap 0 each; Ariun Nuur's meridian (106°52′E) runs through Ulaanbaatar and the Baikal region, where Buryat, Irkutsk and Chita are Künnarantaiga subdivisions | `DR-35` | Russia (the core state) |
| Kunlun | Mirny | +5 | ✅ | **Ariun Nuur's founding stock (Künnarantaiga and Mongolia), plus the Sinian Federation (China)**; a robot-only city, so *founding nation* means the robots' learned national origin (`DR-11`) | Relation (launched from Ariun Nuur via Highway 37) and geography (the Prydz Bay coast it faces is the Sinian Federation's nearest; gap 1) | `DR-34`, `DR-35` | — |
| Relung Panen | Mirny | +7 | ✅ | **Indonesia and Malaysia, jointly** | Time-zone proximity: gap 0 each; a Southeast-Asian maritime pair whose open-water run crosses the Indian Ocean on the site's meridians. *(Gateway claim not yet researched.)* | `DR-34` | — |
| Janbogo | Janbogo | +11 | ✅ | Korea | Two to three time zones | `DR-22` | — |
| Zukelli | Janbogo | +11 | ✅ | **Australia** | Geography/access: zone gap 1; the nearest of the developer's shortlist to Terra Nova Bay, a Southern Ocean run from Tasmania. *(Gateway claim not yet researched.)* Developer: Zukelli *may well* be Australian-founded; his thought is that one of the *other* Australian-founded cities could change instead (`FQ-20`). | `DR-20`, `DR-44` | Italian |
| Cape Adare | Janbogo | +11 | ✅ | **Mixed; no single dominant national community.** An empty slot by ruling, not a gap | Empty-slot law: an entry point on the Ross Sea coast; no nation is required. | `DR-44` | — |
| Fort McMurdo | Janbogo | +11 | ✅ | Miners from all over Tepenia (Mt. Erebus raw materials), then clerics, bureaucrats and logistics coordinators from all over Tepenia; became the de facto capital | Developer ruling | `DR-20`, `DR-21` | American |
| Scott | Janbogo | +11 | ✅ | **New Zealand** | Geography/access: zone gap 0; New Zealand's Canterbury coast is the nearest populous gateway to the Ross Sea. *(Gateway claim not yet researched.)* | `DR-34` | — |
| Dumont d'Urville | Janbogo | +9 | ✅ | **Japan** | Geography/access: zone gap 0; Adélie Land (140°01′E) lies on almost the same meridian as Tokyo (139.7°E), a near-due-south run. *(Gateway claim not yet researched.)* | `DR-20`, `DR-44` | French |
| Denison | Janbogo | +10 | ✅ | **Australia** | Geography/access: zone gap 0; Commonwealth Bay lies almost due south of Tasmania. *(Gateway claim not yet researched.)* Developer's thought, not a requirement: Australia is heavily represented, so one of the Australian-founded cities may be re-founded (`FQ-20`). | `DR-44` | — |
| Concordia | Janbogo | +8 | ✅ | **No founding nation.** Robots and human partners who went inland, then successive waves of coastal refugees. The French/Italian station is not a reason (`DR-19`) | Settlement pattern, not nationality. | `DR-44` | — |
| Byrd | Byrd | −8 | ✅ | **A joint team of first-wave Tepenians from the Peninsula (the Palmer subnet) and the Halley coast (the Halley subnet)**; **not** founded by any Upper-Earth country | Developer ruling. The zone test does not apply: the founders are Tepenian, not a foreign nation. The spec's "American exiles" is superseded. | `DR-44` | American |
| Amundsen Station | Amundsen | — | ✅ | Multi-subnet technical crews on rotation; **no founding nation** (neutral by design) | Neutral inter-subnet infrastructure; the station's neutrality was built into its staffing. | `Specs/Amundsen-Scott subnet/Amundsen_Station.md` L152; `DR-44` | — |

## Change log

| Date | Change |
|---|---|
| 2026-10-01 | Register created and populated from `DR-9` and `DR-19`…`DR-24`, plus existing spec canon for the 🟡 rows. No row was invented: anything not ruled is ⏸️. |
| 2026-10-03 | **Mawson** ruled co-founded by Australia and Kazakhstan (`DR-33`). **Signy**'s partial South African founding confirmed as feasible (`DR-33`). Audit and proposals: `Founding_Register_TimeZone_Audit_and_Proposals_2026-10-03.md` (proposals only; no other row changed). |
| 2026-10-03 | **Six rows ruled** (`DR-34`): Puerto Abrigo (Chile), Pergamino (Uruguay first), Lazar (Russia core + CIN), Kunlun (Ariun Nuur's stock + the Sinian Federation), Relung Panen (Indonesia + Malaysia), Scott (New Zealand). Contrapunto, Neumayer and Ariun Nuur carry developer **direction** recorded in the proposals file; not yet ruled. |
| 2026-10-03 | **Contrapunto, Neumayer and Ariun Nuur ruled** (`DR-35`); Kunlun's stock follows Ariun Nuur (Künnarantaiga and Mongolia, plus the Sinian Federation). 38-city status: see the count in `DR-35`. |
| 2026-10-03 | **Four cities renamed** (`DR-36`–`DR-39`): `{{ Abowasa }}` → Santa Luce · Sayowa → Temirötkel · `{{ Princess Elisabeth }}` → Utstein (native Utsteinen) · `{{ Bunger Hills City }}` → Relung Panen. Rows above use the new names; founders unchanged. See `City_Renames_Alias_Table_2026-10-03.md`. |
| 2026-10-03 | **Gateway research run** for the nine rows marked "gateway claim not yet researched" (three logs in `Research_Logs/`); primary ports ruled (`DR-48`): Ushuaia and Hobart. **Basis wording options recorded, not applied:** `Founding_Basis_Wording_Options_2026-10-03.md`; ports: `Gateway_Ports_Peninsula_and_Scotia_Sea_2026-10-03.md`, `Gateway_Ports_Adelie_and_Queen_Mary_Land_2026-10-03.md`. No row changed. |
| 2026-10-03 | **Gateway research RERUN** with web search (three `…2_…RERUN` logs); ports files corrected, Round 2 wording options appended (`Founding_Basis_Wording_Options_2026-10-03.md`). Bunger Hills coast corrected to the Knox Coast (Wilkes Land) in the Relung Panen spec and dossier. No Register row changed; Basis cells still show the old wording pending the developer's choice. |
| 2026-10-03 | **Mawson ruled: Kazakhstan and Russia** (`DR-46`; closes `FQ-21`). **Mirny amended** (`DR-46`): founded by Idelsk-Uralia, with Russia, Australia and the Sinian Federation present as exile groups (amends `DR-9`). ⚠ Mirny's ULM pass is live; see `DR-46`. |
| 2026-10-03 | **Mawson: Australia removed as a founder** (`DR-45`), to ease Australia's share of the founders. Kazakhstan stays, jointly with a co-founder to be chosen (`FQ-21`). |
| 2026-10-03 | **Eleven rows ruled** (`DR-44`): Signy (South Africa + Brazil) · Dumont d'Urville (Japan) · Denison (Australia) · Zukelli (Australia) · Byrd (a joint team of first-wave Tepenians from the Peninsula and the Halley coast) · Cape Adare (mixed; empty slot) · Palmer City, Amundsen Station and Concordia (not nation-based) · Shirayuki and Sinheung (the Jeju-do allocation, plus geography). Rothera's Argentina stays (`FQ-13b` resolved). Open: `FQ-20` (Australia's share). |
| 2026-10-03 | **Rows re-statused ⛔ → ✅ at the developer's direction:** Rothera, Santa Luce, Utstein, Dome Fuji and Fort McMurdo. Developer: *"all of the 'Ruled founders' listings are right"*. The register's founders were never wrong; the **specs** still contradict them and await their revisit (the check script lists where). |
| 2026-10-03 | **Four more cities renamed** (batch 2, `DR-40`–`DR-43`): Port Lockroy → Puerto Abrigo · Juan Carlos → Pergamino · Sejong → Contrapunto · Vostok → Ariun Nuur (the central scientific district keeps "Vostok"). Founders unchanged. See `City_Renames_Alias_Table_2026-10-03.md` §7. |
| 2026-10-04 | **Mawson: Australia RESTORED as a founder** (`DR-53`, reversing `DR-45`); founders are now Kazakhstan, Russia (core) and Australia, jointly. Basis cites geography and access (`DR-19`) only; the developer's other stated reasons (reuse of an older site, the name) are recorded in `DR-53` but are not the Basis. Australia's share is back to six cities (`FQ-20`). `Mawson.md`'s `Founding population:` line needs a spec revisit. |
