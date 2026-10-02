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
| Palmer City | Palmer | −4 | 🟡 | Three groups united by relationship to robots: exiled robots, human partners, human ideological supporters — **not by nationality** | Founding of the Federation itself; settled 2564-06-21 (`DR-16`) | `Specs/Palmer subnet/Palmer_City.md` L218 | — |
| Rothera | Palmer | −5 | ⛔ | *"primarily, most notably established by industrial workers from North America and Argentina, though with other nations being represented"* | Geography/access | `DR-20` | British |
| Esperanza | Palmer | −4 | ✅ | Argentina | *"almost immediately accessible"* from Argentina | `DR-19`, `DR-22` | — |
| Marambio | Palmer | −4 | ✅ | Argentina | *"almost immediately accessible"* from Argentina | `DR-19`, `DR-22` | — |
| Juan Carlos | Palmer | −4 | ⛔ | *"essentially the same situation as Sejong"*: a primarily Anglo-Latin society of immigrants from the Americas; first founders open (`DR-20a`) | Geography/access | `DR-20` | Spanish |
| Port Lockroy | Palmer | −4 | ⏸️ | Not yet ruled (spec: British exiles; UK ≈ 4 zones) | — | `Specs/Palmer subnet/Port_Lockroy.md` L191; see tracker R-4 | — |
| Sejong | Palmer | −4 | ⛔ | *"a primarily Anglo-Latin society by immigrants from North, Central, and South America"*; first founders open (`DR-20a`). **How it became multinational (developer direction, 2026-10-01):** the inherited station records were in Korean and the newcomers spoke Spanish; translators were invited, who invited others from other countries, *"roughly, approximately akin to the Dutch foundings of New Amsterdam eventually producing New York City (although on a much… smaller scale)"* | Geography/access | `DR-20` | South Korean |
| Signy | Palmer | −3 | ✅ (partial) | South Africa, **partially**; at least one other co-founder, open | Developer ruling (South Africa ≈ 5 zones; the composition file cites the Cape Town–South Orkneys crossing) | `DR-22` | — |
| Halley | Halley | −2 | ✅ (partial) | The UK, in a central role | Two to three time zones | `DR-22` | — |
| Neumayer | Halley | −1 | ⏸️ | Not yet ruled (Germany ≈ 2 zones, within reach; spec names no founder) | — | tracker R-7 | — |
| Troll | Halley | 0 | ✅ | Norway | Near-perfect time-zone alignment | `DR-22` | — |
| `{{ Abowasa }}` | Halley | −1 | ⛔ | Italy and the Confederacy of Intermarium Nations (CIN), jointly | Time-zone proximity | `DR-22` | Finnish, Swedish |
| Sanay | Halley | 0 | ✅ | South Africa | Developer ruling (the one African founder besides part of Signy) | `DR-22` | — |
| `{{ Princess Elisabeth }}` | Halley | +2 | ⛔ | The Scandinavian Trade Union nations, jointly | Time-zone proximity; Belgium did not exist in 2564 | `DR-22` | Belgian |
| Lazar | Halley | +1 | ⏸️ | Not yet ruled (spec: Russian exiles; the two-settlement story rests on real-site history) | — | tracker R-19 | — |
| Belgrano | Halley | −2 | ✅ | Argentina | Accessible from Argentina | `DR-19`, `DR-22` | — |
| Mawson | Mawson | +4 | ✅ | Australia | *"extremely close… comparatively easy access"* | `DR-19` | — |
| Sayowa | Mawson | +3 | ✅ | **First established by the CIN or by Kazakhstan** (which of the two: open); then **industrialized primarily by Kazakh industrialists**, who made it the heavy-industry and shipping city it is in the Second Interwar Period | Time-zone proximity: *"near-perfect alignment"* (the CIN ≈ +1…+2, Kazakhstan ≈ +3…+6) | `DR-30` | Japanese |
| Dome Fuji | Mawson | +3 | ⛔ | *"devout religious disciples, and not associated with any particular country"* (the Ice Cold Buddhism pilgrims) | Developer ruling | `DR-20` | Japanese |
| Mirny | Mirny | +6 | ✅ | Exiles from Russia, China and Australia | Developer ruling | `DR-9` | — |
| Casey | Mirny | +7 | ✅ | Australia | *"extremely close… comparatively easy access"* | `DR-19` | — |
| Davis | Mirny | +5 | ✅ | Australia | *"extremely close… comparatively easy access"* | `DR-19` | — |
| Zhongshan | Mirny | +5 | ✅ | Chinese (state at the Treaty: the Sinian Federation; the people are Chinese) | The Sinian Federation's (i.e. China's) immediate geographic and time-zone access to the site: *"perfectly reasonable that in the 2500s, it would still be the Chinese who would have control over Zhongshan Station"* | `DR-21` | — |
| Shirayuki | Mirny | +5 | 🟡 | Japan, by the Jeju-do court's diplomatic allocation | Allocation, not geography | `Specs/Mirny subnet/Shirayuki.md` L175 | — |
| Sinheung | Mirny | +5 | 🟡 | Korea, by the Jeju-do court's diplomatic allocation | Allocation, not geography | `Specs/Mirny subnet/Sinheung.md` L189 | — |
| Vostok | Mirny | +7 | ⏸️ | Not yet ruled (spec: Russian exiles; Russia's Siberian zones are within reach) | — | `Specs/Mirny subnet/Vostok.md` L128 | — |
| Kunlun | Mirny | +5 | ⏸️ | Not yet ruled (spec: Chinese, "re-resolved" to a curated multinational population) | — | `Specs/Mirny subnet/Kunlun.md` L168 | — |
| {{Bunger Hills City}} | Mirny | +7 | ⏸️ | Not yet ruled (spec: "NOT YET RULED — developer decision") | — | `Specs/Mirny subnet/Bunger_Hills_City.md` L197 | — |
| Janbogo | Janbogo | +11 | ✅ | Korea | Two to three time zones | `DR-22` | — |
| Zukelli | Janbogo | +11 | ⛔ | Open. Developer's shortlist: Hawaii, Mongolia, Taiwan, Indonesia, Australia | — | `DR-20`, tracker R-18 | Italian |
| Cape Adare | Janbogo | +11 | 🟡 | Mixed; no single dominant national community (spec: "TBD") | — | `Specs/Janbogo subnet/Cape_Adare.md` L213 | — |
| Fort McMurdo | Janbogo | +11 | ⛔ | Miners from all over Tepenia (Mt. Erebus raw materials), then clerics, bureaucrats and logistics coordinators from all over Tepenia; became the de facto capital | Developer ruling | `DR-20`, `DR-21` | American |
| Scott | Janbogo | +11 | ⏸️ | Not yet ruled (spec: New Zealand exiles; NZ ≈ 1 zone) | — | `Specs/Janbogo subnet/Scott.md` L145 | — |
| Dumont d'Urville | Janbogo | +9 | ⛔ | Open: *"would not have been established by France. The time zones are much too far away"* | — | `DR-20` | French |
| Denison | Janbogo | +10 | ⏸️ | Not yet ruled. *Proposed*: Australia (and New Zealand), per the composition file's geography-based founding wave | — | `Specs/Janbogo subnet/Denison.md` L279 | — |
| Concordia | Janbogo | +8 | 🟡 | A mix of robots and human partners directed or choosing inland, then successive waves of coastal refugees | — | `Specs/Janbogo subnet/Concordia.md` L179; French/Italian question → tracker R-1 | — |
| Byrd | Byrd | −8 | ⏸️ | Not yet ruled (spec: American exiles; post-war the USA is gone, so this is a CST question) | — | `Specs/Byrd subnet/Byrd.md` L225 | — |
| Amundsen Station | Amundsen | — | 🟡 | Multi-subnet technical crews, no dominant national community | — | `Specs/Amundsen-Scott subnet/Amundsen_Station.md` L152 | — |

## Change log

| Date | Change |
|---|---|
| 2026-10-01 | Register created and populated from `DR-9` and `DR-19`…`DR-24`, plus existing spec canon for the 🟡 rows. No row was invented: anything not ruled is ⏸️. |
