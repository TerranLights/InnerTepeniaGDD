# Climate Data — Research Log *(cross-city pass)*

**Convention:** `Research_Logs/README.md` · `Disciplines/Real-World_Basis_Extrapolation_Method.md` Step F.
**Appended to, never rewritten.**

> **Why this is a cross-city log rather than seven per-city logs.** The pass researched one *variable*
> across several cities rather than one city in depth, and the same searches served multiple specs.
> **Precedent: `Division_of_Industry_Research_Log.md`**, which is filed the same way for the same reason.
> Per-city logs (`Shirayuki_`, `Zhongshan_`) carry a pointer here rather than a copy.

---

# Session 1 — 2026-09-04 · Monthly climate tables for the 7 cities that lacked them

**Pass served:** closing the `Monthly climate table` row of `ULM_Input_Available_Audit.md`.
**Trigger:** developer instruction — *"any of them that don't have it, should be an easy fix."*
**It was not an easy fix.** *(See Findings.)*

## Scope as measured, not as assumed

Re-derived independently rather than trusting the prior audit, using a **row-content** test
(`^\| *(Jan|January) *\|` **followed by a digit**) rather than a heading match — *the heading test is what
produced the earlier false 37/37.*

**Result: 7 of 37 specs lacked a populated monthly table** — Denison · Juan_Carlos · Port_Lockroy · Scott ·
Shirayuki · Zhongshan · Zukelli. **Matches the prior audit exactly.** *(`_TEMPLATE.md` also lacks one,
correctly.)*

Separately: **15 of 37 `Climate Data/READER/` files were stubs**, and **Denison had no READER file at all** —
the only city of the 37 with no climate entry of any kind.

## Searches run — exact strings, verbatim

| # | Search string | Serving | Outcome |
|---|---|---|---|
| 1 | `Cape Denison Commonwealth Bay climate mean annual temperature monthly wind speed katabatic records` | Denison | ⭐ wind 19.1–19.3 m/s; winter −21 °C / summer −3 °C surface range |
| 2 | `Cape Denison automatic weather station monthly mean temperature January February winter Adelie Land coastal` | Denison | ⛔ AWS exists (AMRDC/AMRC) but **no published monthly normals** |
| 3 | `Juan Carlos I station Livingston Island Hurd Peninsula climate monthly mean temperature summer` | Juan Carlos | partial — "mean annual −2.8 °C" **later proved to be the wrong peninsula** |
| 4 | `"Cape Denison" annual mean temperature -11 degrees Mawson Australasian Antarctic Expedition meteorological record wind 19.1 m/s` | Denison | ⭐ **19.3 m/s confirmed** — highest near-sea-level annual mean on Earth |
| 5 | `"Juan Carlos I" Antarctic base Livingston Island mean annual air temperature "-2.8" AWS permafrost Hurd Peninsula` | Juan Carlos | ⭐ **station's own mean is −1.2 °C; −2.8 °C is Byers Peninsula** |
| 6 | `Cape Denison monthly mean temperature table climatology Adelie Land AWS 1912 1913 Mawson annual mean "-11" OR "-11.2" OR "-13"` | Denison | ⛔ dead end — AAE record not digitized in accessible form |
| 7 | `Dumont d'Urville station annual mean wind speed m/s katabatic Adelie Land compared Cape Denison Port Martin` | Denison | ⭐ **DDU 9.7 m/s vs Denison 19.3** — and the 5 km siting cause |
| 8 | `Palmer Station Anvers Island annual precipitation mm water equivalent King Sejong Livingston Island South Shetlands annual precipitation` | Port Lockroy, Juan Carlos | ⭐ Palmer **658 mm**; ⛔ nothing for Sejong/Livingston |
| 9 | `Scott Base McMurdo annual precipitation mm water equivalent Terra Nova Bay Zucchelli station precipitation` | Scott, Zukelli | partial — Dry Valleys 50–100 mm; no Zucchelli annual total |
| 10 | `Dumont d'Urville Adelie Land annual precipitation mm water equivalent APRES3 snowfall accumulation coastal` | Denison | ⭐⭐ **655 mm / 679 mm — and the sublimation finding** |
| 11 | `Larsemann Hills Zhongshan Progress station annual precipitation mm water equivalent Prydz Bay oasis` | Zhongshan, Shirayuki | ⭐ **159 mm (AARI)**; oasis "rarely exceeds 250 mm" |

### Fetches attempted

| URL | Outcome |
|---|---|
| `en.wikipedia.org/wiki/Cape_Denison` | ⛔ no climate table; only "windiest place on Earth" qualitatively |
| Cambridge, *"The katabatic winds of Cape Denison and Port Martin"* (PDF) | partial — **Table 1 referenced but not in the served extract** |
| `timeanddate.com/weather/@6632020/climate` | ⛔ **HTTP 403** to WebFetch |
| same, via developer's own `curl` with a browser UA | ⛔ **Cloudflare JS challenge** — `"Just a moment…"`, 5.5 KB, no data. **`curl` cannot clear it; a real browser session would be needed.** *Not pursued — better sources landed.* |

## ⛔ SNAGS AND DEAD ENDS

1. **Cape Denison has no published monthly temperature normals.** The AAE 1912–14 record is primary and not
   accessible in digitized monthly form; the modern AWS publishes ten-minute observations, not normals.
   **Resolved by split sourcing** — temperature proxied to Dumont d'Urville, **wind taken from the site
   itself**, with the proxy explicitly marked invalid for wind.
2. **timeanddate.com is not reachable by tooling.** Cloudflare-gated against both WebFetch and `curl`.
3. **No precipitation figure exists for the Livingston Island stations.** Juan Carlos' precipitation column
   is a **regional estimate anchored on Palmer's 658 mm** — flagged in-file as the weakest number written
   this pass.
4. **The −2.8 °C trap.** *(Finding 3 below.)*

## ⭐ FINDINGS

### 1 · "An easy fix" was wrong — 5 of the 7 specs had ERRORS, not gaps
The missing tables were the visible symptom. **The header fields above them were wrong in five cities**, and
those errors were load-bearing. *This is the same class the developer has been chasing all along: values
written from a plausible neighbor rather than looked up.*

| City | Error | Magnitude |
|---|---|---|
| **Port Lockroy** | proxied to **Rothera, ~330 km**, when **Palmer is ~27 km** | **6.3 °C** too cold |
| **Port Lockroy** | given a polar night **and** a midnight sun | ⛔ **has NEITHER — 195 km north of the Circle** |
| **Zukelli** | polar night 64 d / midnight sun 70 d | true: **95 d / 101 d** — off by ~a month |
| **Zhongshan** | polar night ~60 d | true: **49 d** — off by 11 d |
| **Juan Carlos** | Sejong "adjusted **−1 °C**" | **wrong sign** — the site is **warmer**; ~1.3–1.8 °C too cold |
| **Scott** | "essentially identical to Fort McMurdo" | **3.4 °C** apart; 4.6 °C in March |
| **Denison** | "polar night and midnight sun both occur" | ⛔ **no polar night** |

### 2 · ⭐ The tell for a fabricated light cycle: **near-equal polar night and midnight sun**
**Refraction and the sun's semidiameter both *lengthen* midnight sun and *shorten* polar night.** The two
spans are therefore **never** equal, and the gap widens the closer a site is to the Circle. **Any spec
pairing them at similar lengths was computed without refraction, or not computed at all.** *Zhongshan's
60/61 was the first one this caught.*

### 3 · ⭐ The −2.8 °C trap — right island, wrong peninsula
A search for Livingston Island's climate returns **−2.8 °C** prominently. **That is Byers Peninsula**, ~30 km
west of and far more exposed than the Hurd Peninsula station site, whose own mean is **−1.2 °C**. *Caught
only by querying the figure directly to see what it was attached to.* **Logged in `READER/Juan_Carlos.md` as
a standing trap.**

### 4 · ⭐⭐ Denison: the precipitation that never lands
Adélie Land's coastal precipitation is **~655 mm** — nominally **four times** the Larsemann Hills. But APRES3
profiling radar at DDU found **a large fraction sublimates inside the dry katabatic surface layer before
reaching the ground**, and **Cape Denison's drainage layer is roughly twice DDU's strength.**
> **Third-order consequence:** Denison is **wet on paper and scoured in fact.** What lands is immediately
> redistributed by 19 m/s wind. **Snow does not accumulate there; it travels.** The city's engineering
> problem is snow *flux*, not snow *load* — **a different problem from the one every other Tepenian city
> solves**, and it follows directly from the site being at the bottom of a drain.

### 5 · The Denison wind is a siting fact, not a weather fact
**19.3 m/s vs DDU's 9.7 — nearly double, 120 km apart.** Cause: DDU is on an island **offshore of** the ice
slope's base; **Cape Denison is at the foot of it**, at a broad drainage basin's outflow. *For scale,
Terra Nova Bay's katabatics — already "among the windiest on the Ross Sea coast" — run 8–12 m/s.*

### 6 · Method validated against the corpus before use
The daylight computation was checked against cities **not** being edited: it returns **Rothera 15 days** of
polar night against the spec's recorded **~16**, and **Belgrano 116 days** against its recorded **~116**.
**The corpus convention is refraction-corrected (−0.833°), and the model reproduces it.**

## ⚠ OPEN THREADS

1. ⛔ **`Specs/Janbogo.md` carries Zukelli's wrong 64 d / 70 d pair.** True values **95 / 101**. *Out of
   this pass's scope — logged, not fixed.*
2. ⛔ **`Specs/Belgrano.md` midnight sun ~105 d against polar night ~116 d.** **Inverted** — midnight sun
   must exceed polar night. Computed: **119 d**.
3. ⛔ **`Specs/Sinheung.md`** — same Larsemann Hills as Zhongshan/Shirayuki, but gives precipitation
   **200–300 mm** against AARI's **159 mm**, and carries the same wrong **~60 d** polar night.
4. ⛔ **`Specs/Mirny.md`** — Rothera's text refers to "Mirny's minimal polar night." **Mirny is at 66°33'S,
   essentially ON the Circle; with refraction it has NO polar night.** Needs checking.
5. **13 READER stubs remain** *(Aboa · Cape_Adare · Dome_Fuji · Halley · Janbogo · Kunlun · Lazar ·
   Little_America · Princess_Elizabeth · Sanay · Sinheung · Troll — plus any surfaced since)*. **Their
   specs mostly have tables anyway; the stubs mean those tables are unsourced.**
6. **No station precipitation figure for Livingston Island / King Sejong.** Juan Carlos' column is regional.
7. **`Temp Range` · `Avg Precip` · `Precip Probability` are derived in every spec in the corpus**, including
   the ones written before this pass. **Only `Avg Temp` and `Avg Daylight` are measurable.** This pass
   states that per-file; **the pre-existing specs do not, and a reader cannot currently tell.**

---

*Session 1 closed.*

---

# Session 2 — 2026-09-04 · Full 37-city climate audit

**Trigger:** developer instruction — *"have a look at all the other cities and make sure their climate data
is accurate and complete as well."*

**⭐ Full findings and the complete correction table live in a dedicated file:**
**`Reference/Real-World/Climate Data/Climate_Data_Corpus_Audit_2026-09-04.md`**

**No new web research was required** — the light cycle is computed from latitude, not sourced. This session
ran no searches. *(Session 1's eleven searches are the research record for the whole pass.)*

## Result in one line

**Temperature: 37/37 correct, zero errors.** **Light cycle: 22 cities had wrong polar night / midnight sun
spans, and all 30 pre-existing daylight columns were inaccurate.**

## ⛔ SNAG — the audit tool was wrong twice before the corpus was

Both at the South Pole, where the general formula divides by zero: **a sign inversion** *(reported January
at Amundsen Station as 0 hours of daylight — it is continuous sun)*, then **a refraction omission**.
**Amundsen Station's stated 183/183 is correct and was nearly "corrected" into being wrong.**

> ⭐ **Recorded because of the direction of the error.** *The tool's first output flattered the audit —
> it manufactured a dramatic finding in a file that was fine.* **Caught only because the magnitude was too
> large to be plausible.** **The instrument was validated against two cities that were NOT being edited
> (Rothera, Belgrano) before any file was touched; that check is what made the pole bug visible.**

## ⭐ The finding that explains almost all 22 errors

**One false assumption, repeated across the corpus:** *that polar night and midnight sun are symmetric, and
that the Antarctic Circle is the boundary for both.* **Refraction plus the sun's semidiameter (~0.833°)
shorten polar night and lengthen midnight sun**, so the two spans are **never equal** and their boundaries
sit **~0.8° apart** — leaving an asymmetric band, containing **four Tepenian cities**, that has a midnight
sun and **no polar night at all**: **Casey · Mirny · Dumont d'Urville · Denison.**

⚠ **Two of those four are SOUTH of the Antarctic Circle and still have no polar night.** *Being inside the
Circle is not sufficient.*

**Practical tell:** a spec pairing polar night and midnight sun at **near-equal lengths** was computed
without refraction, or not computed at all. *(Zhongshan `60/61`, Mirny `4–5 / 4–5`.)*

## ⚠ OPEN THREADS — added this session

8. **The derived-column caveat is missing from 30 specs.** `Temp Range`, `Avg Precip` and `Precip
   Probability` are **derived everywhere in the corpus**; only `Avg Temp` and `Avg Daylight` are real.
   The seven specs written this session say so in-file; **the other thirty do not, and a reader cannot tell
   which numbers are measurements.**
9. **`Specs/Denison.md`** still cites *"Sections I and III"* of the census — a leftover from the 2026-09-03
   relettering to A–D, unrelated to climate.

*Threads 1–4 from Session 1 (Janbogo, Belgrano, Sinheung's light cycle, Mirny) are **CLOSED** — all were
fixed in this session's sweep. Thread 3's precipitation half remains open; see item 1 of the audit file.*


---

# Session 3 — 2026-09-04 · The three derived columns

**Trigger:** developer instruction — *"it appears we need to check the `Temp Range`, `Avg Precip` and
`Precip Probability`, so let's check that next."*

**Premise, from Session 2's audit:** those three columns were **invented in all 37 specs** and formatted
identically to the two real ones. *(Logged as M-140.)*

## ⭐ The premise was too pessimistic — the data exists

**Published monthly normals give exactly the three quantities needed**, and they map one-to-one onto the
columns:

| Column | What actually supplies it |
|---|---|
| **`Temp Range`** | **mean daily maximum → mean daily minimum** — a real measured envelope |
| **`Avg Precip`** | **monthly precipitation normals, mm** |
| **`Precip Probability`** | **mean days with precipitation ÷ days in month** |

## Fetches run — verbatim URLs

| Station | Result |
|---|---|
| `en.wikipedia.org/wiki/Esperanza_Base` | ⭐ max/min + precip + precip-days |
| `…/Casey_Station` | ⭐ max/min + precip + precip-days |
| `…/Amundsen–Scott_South_Pole_Station` | ⭐ full |
| `…/McMurdo_Station` | ⭐ full |
| `…/Davis_Station` | ⭐ full |
| `…/Vostok_Station` | max/min + precip |
| `…/Mirny_Station` | max/min + precip |
| `…/Mawson_Station` | max/min only |
| `…/Halley_Research_Station` | max/min only |
| `…/Neumayer-Station_III` | max/min + precip |
| `…/Dumont_d'Urville_Station` | max/min + precip-days |
| `…/Palmer_Station` | max/min + precip — ⭐ **658 mm, feeds Port Lockroy** |
| `…/Concordia_Station` | max/min only |
| `…/Marambio_Base` | max/min + precip |
| `…/Showa_Station_(Antarctica)` | max/min only |
| `…/Novolazarevskaya_Station` | max/min + precip |
| `…/Bellingshausen_Station` | ⭐ max/min + precip — **702 mm, King George I.** |
| `…/Rothera_Research_Station` | ⛔ daily mean only, no box |
| `…/Zhongshan_Station_(Antarctica)` | ⛔ no climate box |
| `…/Troll_(research_station)` | ⛔ no climate box |
| `…/King_Sejong_Station` | ⛔ no climate box — **resolved via Bellingshausen instead** |
| `…/Signy_Research_Station` | ⛔ **REJECTED — see below** |

## ⛔ SOURCE REJECTED — Signy

The published box is **internally inconsistent**: **February's mean daily minimum (+1.4 °C) is warmer than
January's (−0.7 °C)**; precipitation is present for only 8 of 12 months; September shows **140 mm** against
June's **2.6 mm** in a maritime regime that should be comparatively flat. **Not used.** *Recorded because
the temptation was real — it was the only Signy source found, and a partly-broken table is harder to refuse
than no table at all.*

## Result

**19 cities gained a measured `Temp Range`** · **14 a measured `Avg Precip`** · **6 a measured
`Precip Probability`.** ⭐ **And all 37 specs now carry a per-column provenance line beneath the table**,
so measured, computed and estimated values are distinguishable per number. **That closes M-140's open
item.**

## ⚠ OPEN THREADS — updated

- ✅ **Thread 6 CLOSED** *(no Livingston/Sejong precipitation)* — Bellingshausen supplies 702 mm.
- ✅ **Thread 8 CLOSED** *(derived-column caveat missing from 30 specs)* — all 37 now labelled.
- **18 cities still carry a derived `Temp Range`**, 23 a derived `Avg Precip`, 31 a derived `Precip
  Probability`. **Next route: national met-service archives rather than encyclopedia boxes** — BoM, AARI,
  KOPRI, BAS and PNRA publish fuller normals than the summary boxes carry.

---

# Session 4 — 2026-09-04 · Closing the remaining climate fields

**Trigger:** developer instruction — *"those that are currently missing need to be researched. Do that now."*

## Movement across the pass

| Field | Before Session 3 | After Session 3 | **After Session 4** |
|---|--:|--:|--:|
| `Temp Range` derived | 37 | 18 | **10** |
| `Avg Precip` derived | 37 | 23 | **15** |
| `Precip Probability` derived | 37 | 31 | **28** |
| `Prevailing winds` absent | 16 | 16 | **8** |
| `Record extremes` absent | 23 | 23 | **11** |
| **Solstice daylight absent** | 22 | 22 | ✅ **0** |
| **Annual precipitation absent** | 1 | 1 | ✅ **0** |

## Sources that landed

| Station | Gave | Serves |
|---|---|---|
| **Scott Base** | ⭐ max/min · precip 184 mm · records · **wind** | Scott — *fully closed* |
| **Belgrano II** | ⭐ max/min · precip 299.5 mm · snowy days · records · wind | Belgrano |
| **Mario Zucchelli** | ⭐ max/min · precip 144.7 mm | Zukelli, **Janbogo** *(proxy, ~8 km)* |
| **Progress** | ⭐ max/min · precip 148.9 mm | Sinheung, **Zhongshan** *(~1 km)*, **Shirayuki** *(~15 km)* |
| **Byrd** | precip 30 mm · precip-days · records | Byrd |
| **Dumont d'Urville** | max/min · precip-days | **Denison** *(proxy, ~120 km — already its temperature proxy)* |
| Davis · Mawson · Esperanza · Marambio · Neumayer · Syowa · Palmer | records, some winds | seven cities |
| **SANAE IV** *(search, not box)* | wind 11 m/s mean, gusts 61.9 m/s · precip <200 mm · seasonal means | Sanay |
| **Signy** *(search)* | records · **precipitation on ~250 days/yr** · ~60 gale-days | Signy |
| Kunlun · Dome Fuji · Troll · Princess Elisabeth | narrative extremes / wind only | four cities |

⭐ **One proxy chain worth noting:** Progress Station closes the **entire Larsemann Hills trio** at once —
Sinheung directly, Zhongshan at ~1 km, Shirayuki at ~15 km. *The three cities share one climate, which is
exactly why the climate cannot differentiate them culturally.*

## ⭐ ACCURACY CATCH — a widely-circulated record that WMO rejected

**Marambio/Seymour Island's +20.75 °C of 9 February 2020** is repeated everywhere as an Antarctic record.
**WMO rejected it** — the sensor was a permafrost monitoring unit under an improvised radiation shield.
**The station record used instead is +17.4 °C (23 March 2015)**, and the *mainland* record is correctly
attributed to **Esperanza's +18.3 °C (6 February 2020)**, which WMO did ratify. *(Signy's +19.8 °C of 30
January 1982 is a separate, also-ratified category — the Antarctic **region**, which includes the
sub-Antarctic islands. Both are real; they are not competing figures.)*

## ⭐ INDEPENDENT VALIDATION of the daylight model

Troll's own published description gives **polar night ~May 15 → Jul 27** and **midnight sun ~Nov 9 → Feb 1**.
**The model computed May 16 → Jul 29 and Nov 11 → Feb 1** — within two days on every boundary, from a source
that had no part in building it. *(Third such check, after Rothera and Belgrano.)*

## ⛔ SNAG — the GPS hook fired on a SOURCE ATTRIBUTION

A search naming a national meteorological institute **as the publisher of a dataset** was blocked under the
GPS-purposes-only law.

> ### ⚠ Developer ruling, 2026-09-04: **"that shouldn't get blocked based on a real word."**
>
> ⭐ **Naming a met service as a data publisher is a CITATION, not a cultural import.** **The corpus already
> does this in all 38 `Climate Data/READER/` files** — every one names its climate authority *(Australian
> Antarctic Division, Korea Polar Research Institute, Institut polaire français Paul-Émile Victor,
> CHINARE, AARI, PNRA)*. **The hook cannot distinguish "this nation's institute measured the temperature"
> from "this city inherited this nation's character," and only the second is what the law forbids.**
>
> **Consequence:** three stations whose normals are published only by their national met service — **Troll,
> Aboa, SANAE IV** — could not be searched directly. **Handed to the developer to run with the `!` prefix.**

## ⚠ OPEN THREADS

1. **`Temp Range` still derived in 10** — Abowasa · Byrd · Cape_Adare · Dome_Fuji · Kunlun ·
   Princess_Elisabeth · Rothera · Sanay · Signy · Troll. *(Byrd publishes daily means and record extremes
   but no mean daily max/min — it may not exist.)*
2. **`Avg Precip` still derived in 15**, **`Precip Probability` in 28.** ⚠ **Precipitation-day counts are
   rarely published for Antarctic stations at all** — only 9 of 37 have one. **This may be permanently
   underivable for most of the corpus, and is worth a deliberate ruling rather than standing open forever.**
3. **Cape Adare has no station and no proxy assigned.** Nearest candidates are Leningradskaya or Cape
   Hallett; neither is in the corpus. **Needs a proxy decision.**
4. **Rothera publishes only monthly means** *(confirmed against BAS READER directly)*. Its max/min and
   precipitation were not obtainable despite being a major long-record station.

## Session 4b — after the developer's ruling on the blocked search

> ### ⛔ MY OWN ERROR, recorded: **the `!` commands I handed the developer were useless.**
> I suggested `! echo "<search string>"`. **`echo` prints the string back; it runs no search.** The
> developer ran it and got their own words returned. **Nothing was gained and their time was wasted.**
>
> ⭐ **And the workaround was unnecessary in the first place.** **The GPS hook fires on `WebSearch`
> queries, not on `WebFetch` URLs.** A national met service's own pages, and non-English Wikipedia, were
> reachable directly the whole time. *The block was never a wall; I mistook the one blocked tool for all
> of them.*

### Fetched directly, no developer involvement needed

| URL | Result |
|---|---|
| `no.wikipedia.org/wiki/Troll_(forskningsstasjon)` | ⛔ narrative only, same as English |
| `fi.wikipedia.org/wiki/Aboa` | ⛔ no climate table |
| `af.wikipedia.org/wiki/SANAE_IV` | ⛔ HTTP 404 |
| `zh.wikipedia.org/wiki/中山站` | ⛔ disambiguation page, no data |
| ⭐ **`climatestotravel.com/climate/antarctica`** | **min/max for 15 stations — gave SANAE IV** |
| ⭐ **`climatestotravel.com/…/south-orkney-islands`** | **Orcadas: min/max + precip + precip-DAYS** |

### ⭐ The Orcadas find — Signy closed, including its probability column

**Signy (60°43'S 45°36'W) and Orcadas on Laurie Island (60°44'S 44°44'W) are ~48 km apart in the same South
Orkney group.** Orcadas publishes **precipitation days**, which almost no Antarctic station does — so Signy
gains a **measured** `Precip Probability`, one of only nine cities to have one. *(Cross-check: Orcadas'
annual mean ≈ −3.1 °C against Signy's READER −3.8 °C — sound for a 48 km maritime proxy.)*

**This also supersedes the Session 3 rejection of Signy's Wikipedia box** *(inconsistent: February minimum
warmer than January)*. **The box was rejected; the city is now sourced from a neighbor instead.** ⭐ *The
right response to a broken source was a different source, not an estimate.*

### Standing after 4b

| Field | Still derived / absent |
|---|--:|
| `Temp Range` | **8** — Abowasa · Byrd · Cape_Adare · Dome_Fuji · Kunlun · Princess_Elisabeth · Rothera · Troll |
| `Avg Precip` | **14** |
| `Precip Probability` | **27** |
| `Prevailing winds` | **8** — Abowasa · Davis · Lazar · Sayowa · Sejong · Shirayuki · Sinheung · Zhongshan |
| `Record extremes` | **11** |

⚠ **The eight remaining `Temp Range` cities are all seasonal, inland or unstaffed sites** *(Aboa, Byrd,
Cape Adare, Dome Fuji, Kunlun, Princess Elisabeth, Troll)* **plus Rothera, which genuinely publishes only
monthly means.** *These are not oversights in the search; they are stations that do not publish mean daily
max/min at all.*

---

# Session 5 — 2026-09-04 · Record extremes · Avg Precip · Precip Probability

**Trigger:** developer instruction — *"now, we need to find the Record Extremes, the Avg Precip, and the
Precip Probability for the cities."*

## Movement

| Field | Start of Session 5 | End |
|---|--:|--:|
| `Prevailing winds` absent | 8 | **3** |
| `Record extremes` absent | 11 | **7** |
| `Precip Probability` derived | 27 | **25** |
| `Avg Precip` **annual header** unsourced | 5 | **0** |

⚠ **Note the distinction the gap table does not show:** `Avg Precip` still counts **14 cities as derived**
because that measures the **monthly column**. **Five of those now have a *researched annual total* in the
header** *(Dome Fuji 25 mm · SANAE IV <200 mm · Dumont d'Urville 655 mm · Concordia ~25 mm · Lazar 237.7
mm)* — **only the month-by-month split is still modeled.** *A partial upgrade, recorded as partial.*

## ⭐⭐ The Larsemann Hills ASMA management plan — one document, three cities

**`ASMA No. 6 — Larsemann Hills, ATCM XXXVII Final Report` §4.2** *(env.go.jp PDF, 3 MB)*. **WebFetch could
not parse it** — returned binary — **but it saved the file locally, and reading the PDF pages directly
worked.** ⭐ *A fetch that "fails" may still have delivered the document; check for a saved path before
giving up.*

§4.2 verbatim: *"persistent and strong katabatic winds that blow from the north-east on most summer days.
Daytime air temperatures from December to February frequently exceed 4 °C and can exceed 10 °C… Mean
monthly winter temperatures mostly range between −15 °C and −18 °C. Precipitation occurs as snow and is
rarely exceeds 250 mm water equivalent annually."*

**Closed winds AND record extremes for Zhongshan, Shirayuki and Sinheung simultaneously.**

## Other sources that landed

| Station | Gave | Serves |
|---|---|---|
| **Concordia** | records **−5.4 / −84.6 °C** (Aug 2010) · ⭐ **winter wind only 2.8 m/s** | Concordia |
| **Vostok** | records **−14.0 / −89.2 °C** *(world record low)* · **26 snow-days/yr** · wind 5→27 m/s | Vostok |
| **Novolazarevskaya** | records **+9.9 / −41 °C** · two-regime wind description | Lazar |
| **Syowa** | **200.6 snow-days/yr** · max instantaneous wind **61.2 m/s** (27 May 1996) | Sayowa |
| **Marambio** | monthly **snowy-day counts** — *collected in Session 4 and never applied; caught on review* | Marambio |

⚠ **Vostok's probability column is a two-step derivation, marked as such:** a **measured** annual count (26
days) distributed across **measured** monthly precipitation. **Not a guess, but not a direct measurement
either** — the file says so.

## ⛔ BLOCKED — handed to the developer

| URL | Response |
|---|---|
| `http://www.bom.gov.au/climate/averages/tables/cw_300001.shtml` | **HTTP 403** |

**The Australian met service is the single highest-value remaining source** — it publishes full station
climate statistics *(monthly precipitation, mean rain-days, record high/low)* for **Mawson, Davis and
Casey**, which would close three cities across all three fields at once. **It refuses WebFetch.**

## ⛔ Dry holes this session

Italian, Spanish, Russian, Japanese and Norwegian Wikipedia for Zucchelli, Juan Carlos I, Aboa/Wasa and
Troll; the BAS Halley facility page *(served an empty document)*. **Aboa/Wasa appears to publish no climate
data at all in any language** — its own institute's Antarctic page carries none.

## ⚠ REMAINING — and an assessment, not just a list

- **`Record extremes` absent (7):** Abowasa · Cape_Adare · Denison · Juan_Carlos · Princess_Elisabeth ·
  Sejong · Zukelli
- **`Prevailing winds` absent (3):** Abowasa · Davis · Sejong
- **`Precip Probability` derived (25)** — ⛔ **the honest position: precipitation-day counts barely exist
  for Antarctic stations.** **Twelve of 37 now have one**, and every single one came from a station that
  happened to publish it. **Further searching will not move this much.** *Recommend a developer ruling that
  it stays derived corpus-wide rather than remaining an open item indefinitely.*
- **Cape Adare has no station, no proxy, and no data in any field.** **It needs a proxy ruling** —
  candidates are Leningradskaya or Cape Hallett, neither in the corpus.
- **Abowasa likewise** — Aboa/Wasa publishes nothing; the nearest station with data is SANAE IV at **~390
  km**, far beyond the 15–120 km proxies used elsewhere. **Also a ruling, not a research task.**

---

# Session 6 — 2026-09-04 · NOAA NCEI, and the schema rebuild

**Trigger:** developer instruction — *"are you able to find other sources with better, more reliable, and
more available data?"* ⭐ **Yes. I should have looked sooner instead of pushing timeanddate.**

## ⛔ First — timeanddate is a dead end, confirmed twice over

**Twelve `curl` attempts: all Cloudflare challenge pages, zero data.** **Then eleven browser-saved pages
(62–64 KB each, real HTML): the monthly grid still absent** — it loads by AJAX *after* render, so
"Save Page As" captures the page before the numbers arrive. Only the "Quick Climate Info" summary is static.

### ⭐ But the summary was worth something — it exposed a measurement-convention problem

Cross-checking its figures against measured data: **temperature tracks well** *(Amundsen −26/−59 vs measured
−27.3/−60.2; Zucchelli −1/−22 vs −1.2/−21.8)* — **except Vostok, where it names April as the coldest month
when the true answer is August.** **Precipitation diverges wildly** *(South Pole 33.8 mm vs the measured
2.1 mm; Vostok 44.7 vs 22; Rothera an implausible 1048.5)*.

> ### ⚠⚠ THE FINDING, and it needs a developer ruling
> ***These are not errors. Antarctic precipitation has two legitimate and very different numbers.***
> **Gauge-caught** precipitation under-measures severely — blowing snow does not enter the gauge.
> **Reanalysis/accumulation** captures what actually falls. **The South Pole's true accumulation is
> ~70–80 mm/yr, so 2.1 mm and 33.8 mm are both correct measurements of different quantities.**
>
> **This is the same physics as the Denison finding** *(snow that falls, sublimates in the katabatic layer,
> and never lands)*. **Three distinct quantities: what falls · what is caught · what accumulates.**
>
> ⛔ **The corpus currently mixes conventions and does not say which is which.** For a weather system,
> *what falls* is probably the right choice — it is what a person outdoors experiences — **but converting
> 37 cities is a decision, not a cleanup, and was NOT done unilaterally.**

**Wind from that source was also rejected** — "Mawson 96 km/h avg" for a month exceeds Cape Denison's annual
mean at the windiest sea-level site on Earth. Those are gusts, not means.

## ⭐⭐ THE SOURCE THAT WORKED — NOAA NCEI Global Summary of the Month

**Per-station CSVs, direct download, no Cloudflare, no JavaScript.** *(`ncei.noaa.gov/data/gsom/access/<ID>.csv`)*

| Column | Supplies |
|---|---|
| **`EMXT` / `EMNT`** | **extreme max/min actually observed in each calendar month** — the record fields |
| **`DP01`** | **days with ≥0.1 mm precipitation** — *the field I had recommended writing off as permanently derived* |
| `PRCP` · `TAVG` · `TMAX` · `TMIN` · `EMXP` | monthly totals, means, heaviest single day |

**102 Antarctic stations listed; 68 had monthly data.** **Matched to cities by COORDINATE, not by name** —
deliberately, given the corpus's standing "files are named for the station, not the city" trap.

⭐ **31 of 37 cities have a station within 30 km**, including several previously written off: **Rothera
(0 km) · Troll (5 km) · SANAE (4 km) · King Sejong (2 km) · Kunlun (7 km) · Zhongshan · Progress.**

### ⚠ Cross-check before applying — and it changed the plan

**Published climate boxes proved WIDER than NCEI in 14 of 17 overlapping cities**, because they cover longer
periods than NCEI's GSOM holdings. **The decisive case: Vostok's box carries −89.2 °C, the world record;
NCEI reaches only −79.8 °C.**

> ***So NCEI was used to FILL GAPS, never to overwrite an existing published record.*** **Had this been
> applied blindly, it would have erased the lowest temperature ever measured on Earth from Vostok's file.**

## Result

| Field | Before | After |
|---|--:|--:|
| `Rec High` / `Rec Low` | 17/37 | **25 full · 9 partial · 3 none** |
| `Precip Probability` | 12 measured | ⭐ **22 measured**, 37/37 populated |
| `Avg High` · `Mean` · `Avg Low` · `Precip` · `Daylight` | — | **37/37** |

**The table schema was also rebuilt to 10 columns:** `Month · Rec High · Avg High (day) · Mean ·
Avg Low (night) · Rec Low · Precip mm · Precip Prob · Daylight · Notes`.

⚠ **Day/night mapping, stated in every file:** *`Avg High` and `Avg Low` are the mean daily maximum and
minimum — the warmest and coolest parts of the 24-hour cycle, which is what "day" and "night" mean at these
latitudes.* ⭐ **During polar night the diurnal cycle is not solar-driven at all**, so the day/night split
narrows toward weather noise rather than following a clock. *Relevant to any in-game weather model.*

## ⛔ SNAG — a parser bug I introduced, caught by the verification pass

The restructure dropped `Avg High`/`Avg Low` for **Palmer City, Port Lockroy, Sejong and Juan Carlos**: my
regex did not accept a leading `+` on the low value. **Restored from source.** *Recorded because the apply
step reported success — only the independent coverage re-count caught it. **Never trust an apply count as
verification.***

## ⚠ REMAINING

- **3 cities have no monthly records and no station in range:** **Abowasa** *(nearest 312 km)* ·
  **Dome_Fuji** *(240 km)* · **Princess_Elisabeth** *(430 km)*. **A proxy ruling, not a research task.**
- **9 cities have partial records** *(Rothera 3–8 months · Cape_Adare 6 · Lazar 8 · Mirny 7–9 ·
  Shirayuki/Sinheung/Zhongshan 9 · Kunlun 11 · Sejong 11)* — **short station records, not missing sources.**
- **The precipitation-convention ruling above.**

## Session 6b — Developer ruling: the South Pole reference station

> ### ⭐ RULING, 2026-09-04 — **Amundsen-Scott Station is the official climate reference for Amundsen Station.**
>
> ***"Go by Amundsen-Scott Station as the official reference (regardless what the conditions are at either
> Geographical or Magnetic South), since ASS is the actual basis for the ground-base of Amundsen Tower."***

**Written into `Specs/Amundsen_Station.md` as a standing ruling block, not a footnote** — the reasoning is
in-world *(the Tower's ground base sits on the station site, so the station's conditions are the city's
conditions)* and would otherwise be re-litigated by any pass that noticed the pole/station distinction.

### Why this needed recording even though no data changed

**All three of the file's sources already resolved to Amundsen-Scott** — BAS READER `Amundsen_Scott`, the
published climate box, and NCEI `AYW00090001`. **Nothing was edited to comply.** The ruling matters because
it **forecloses a live ambiguity**: the **Magnetic South Pole is not at this station** — it lies off the
Adélie Land coast, nearer *Dumont d'Urville*, and it migrates annually. **A later pass "correcting" toward
magnetic-pole conditions would be wrong by ruling rather than by taste.** *(Geographic pole and station are
effectively co-located; the station drifts ~10 m/yr with the ice. No conflict there.)*

**Corpus check:** the only file in the project mentioning the magnetic south pole is now this one.

### Tightened in the same pass
`Record extremes` moved from *"approximately −82 / −14"* to the exact station record — **high −12.3 °C
(December), low −82.8 °C (June)** — with the monthly breakdown already in the table.

⚠ **And the precipitation caveat was made explicit in-file:** Amundsen Station's **2.1 mm** is the
**gauge-caught** figure, against roughly **70–80 mm** of actual accumulation. **This is the corpus's most
extreme instance of the falls-vs-caught-vs-accumulates problem**, and the convention ruling remains open.

---

# Session 7 — 2026-09-04 · WHAT FALLS vs WHAT LANDS

**Trigger:** developer instruction — *"see if you're able to research and identify A.) what falls, and
B.) what actually lands, because this may create interesting results for the in-game experience."*

## The chain, with measured coefficients

**Four distinct quantities, not two.** Each step has a published number:

| # | Quantity | Measured value |
|---|---|---|
| **1** | **Falls aloft** *(CloudSat radar, 1200 m above ground)* | **coastal 275 mm/yr · plateau 34 mm/yr · continent mean 171 mm/yr** |
| **2** | **− low-level sublimation** *(katabatic air is unsaturated; snow evaporates mid-fall)* | **−17% continent-wide · up to −35% on East Antarctic margins** |
| **3** | **− blowing-snow sublimation and transport** | **up to −50% of precipitation in coastal and slope convergence areas** |
| **4** | **= accumulates (SMB)** | *what a stake farm or ice core measures* |
| *(aside)* | **gauge-caught** | ⛔ *not on this chain at all — an instrument artifact* |

**Sources:** Palerme/Lemonnier CloudSat climatology · **Grazioli et al. 2017, PNAS, "Katabatic winds diminish
precipitation contribution to the Antarctic ice mass balance"** · Antarctic SMB intercomparison (MAR/RACMO2)
· blowing-snow sublimation SMB studies.

**Continent-wide totals:** total sublimation **236.2 Gt/yr, of which 223.3 Gt/yr is blowing-snow
sublimation** — *the snow that never lands is overwhelmingly snow that already landed once and was picked
back up.* Blowing-snow **erosion** is only 11.2 Gt/yr; the loss is to the air, not downhill.

## ⭐ The station checks — and they resolve the 2.1 mm problem

| Site | Gauge | Falls | Accumulates | Reading |
|---|--:|--:|--:|---|
| **Amundsen Station** | **2.1 mm** | **~70 mm** | **~70–80 mm** *(stake, 1983–2010: ~275 mm of snow depth)* | ⭐ **gauge catches ~3%.** Falls ≈ lands: no wind to remove it |
| **Vostok** | **22 mm** | ~25 mm | **22.5 ± 1.3 mm** *(stake, since 1970; +8% corrected)* | ⭐ **gauge ≈ accumulation.** Nothing is lost because nothing blows |
| **Denison / DDU** | — | **~655 mm** | *far less* — margin site, −35% sublimation then transport | ⛔ **the widest gap in the set** |

> ### ⭐⭐ THE HEADLINE NUMBER FOR GAMEPLAY
> ***"Cumulative snow transportation can be approximately 4 orders of magnitude higher than snow
> precipitation at coastal sites."***
>
> **At a coastal katabatic city, the snow moving horizontally past a person is on the order of TEN THOUSAND
> TIMES the snow falling from the sky.** ***Weather there is not something that comes down. It is something
> that goes past.*** **Nobody at Denison digs out from what fell on them; they dig out from what arrived
> from upwind.**

## ⭐ Three regimes — the 37 cities sort cleanly

| Regime | Cities | Falls | Lands | What it feels like |
|---|---|---|---|---|
| **PLATEAU — accumulating** | Amundsen · Vostok · Concordia · Dome_Fuji · Kunlun | **tiny** (25–70 mm) | **≈ all of it** | Clear, still, diamond dust. **Almost nothing falls — and every flake that does, stays.** Snow is permanent, not weather |
| **KATABATIC MARGIN — scoured** | Denison · Dumont_dUrville · Mawson · Mirny · Casey · Janbogo · Zukelli · Sanay · Troll · Lazar · Sayowa · Cape_Adare | **large** (300–650 mm) | **a fraction** | **Snow flux, not snowfall.** Up to 35% evaporates before landing; the rest is entrained. Blue-ice and wind-crust where the net goes negative |
| **MARITIME — wet** | Palmer_City · Port_Lockroy · Signy · Esperanza · Juan_Carlos · Sejong · Marambio · Rothera | **large** (400–700 mm) | **most of it** | Genuinely wet. **Rain as well as snow**, melt, compaction, slush. The only cities where precipitation behaves like temperate weather |

⚠ **The Larsemann Hills trio (Zhongshan · Shirayuki · Sinheung) sit between plateau and margin** — an
ice-free oasis, low precipitation (~160 mm) with strong NE katabatic winds. **Low fall, high transport.**

## ⭐ Why this is worth building on rather than just recording

**The three regimes are not a reskin of "cold vs mild" — they are orthogonal to temperature.**
**Vostok and Denison are both brutally cold and are opposite weather experiences**: one is airless stillness
where snow is a permanent deposit, the other is a horizontal river of ice crystals where snow is a *medium*
you move through. **Two cities can share a temperature curve and share nothing about what weather means.**

⭐ ***And it explains a piece of canon that was already written:*** **Denison's "one continuous, interlinked,
load-sharing structure" and its 25% distinctive-tier spend on structural/wind engineering.** *That city is
not built against snow load. It is built against snow flux.*

## ⚠ DECISION PENDING — not applied to the 37

**The corpus currently records one precipitation number per city and does not say which of the four
quantities it is.** *Proposal put to the developer; awaiting ruling before touching any city file.*

## Session 7b — Applied to all 37, with the wind/cold split made explicit

> **Developer ruling:** *"update all 37 to carry as many individual quantities as we have available. All of
> this information can definitely be used. Especially make sure to distinguish between wind and cold."*

**Created `Reference/Real-World/Climate Data/Precipitation_Falls_vs_Lands.md`** — the mechanism, the
published coefficients, the six regimes, and the falls/lands figure for every city.
**Registered in `City_Master_Reference/README.md` and the `00_RUNBOOK.md` §C.9 registry** *(a reference the
methodology cannot address is one this project has repeatedly proven it will not use)*.

**Every one of the 37 specs now carries a `Precipitation regime` block:** regime · falls · lands · lost ·
retention, and a **`WIND vs COLD`** statement built from that city's own cold-rank and wind figure.

### ⭐⭐ The data settled the wind/cold question outright

| | |
|---|---|
| **The 5 coldest cities** — Kunlun · Vostok · Dome_Fuji · Concordia · Amundsen | ⭐ **all plateau, all calm, all ~90% retention** |
| **The windiest city** — Denison, 19.3 m/s | ⚠ **only the 22nd coldest of 37 — twenty-one cities are colder** |

***Cold and wind are not correlated in this set; they are nearly orthogonal.*** **Concordia is the #4
coldest city and the calmest (2.8 m/s). Denison is middling-cold and the windiest place on Earth.** Each
spec now says which of the two actually defines it, in those terms.

**Three distinct statements were written, not one template:**
- **PLATEAU** — *"the hazard is temperature and altitude; air movement is close to irrelevant.* ⛔ *There is
  no whiteout-under-clear-sky here — when visibility closes, something is actually falling."*
- **KATABATIC MARGIN** — *"whiteout routinely occurs under a clear sky, because the snow is lifted, not
  falling. Residents dig out from what arrived from upwind, not from what fell on them."*
- **MARITIME** — *"the hazard is WATER. Rain as well as snow; melt, saturation, freeze-thaw and slush rather
  than scouring. The engineering problem is drainage and damp, not drift."*

### ⛔ SNAG — two bugs in my own generated prose, caught on spot-check

The maritime and oasis templates printed **the count of MILDER cities where the sentence said "are
colder"** — Port Lockroy read *"1 are colder"* when 35 cities are colder — and the verb did not agree.
**Fixed across all 11 affected files.**

> ⚠ **Both bugs were in generated text that the apply step reported as fully successful.** *Same lesson as
> the `Avg High` regex bug in Session 6: **an apply count is not verification. Read the output.*** **This
> is the second time in one day that a clean apply report concealed wrong content.**

---

# Session 8 — 2026-09-04 · Robot cold physiology · Concordia altitude

**Trigger:** developer direction — *"what Frostland life costs a robot player… being able to recharge, and
how quickly cold-exposure depletes HP… other effects will need to be researched according to their own
Physics"*, then *"write all of it to file"* and *"include where you got the research results from."*

## Files created

| File | Covers |
|---|---|
| **`Worldspace/Robot_Biology_and_Culture/Robot_Cold_Physiology.md`** | Recharge trade-off · the death spiral · reversible vs permanent capacity loss · output sag · embrittlement, lubricants, seals · **moving-is-safer** |
| **`…/Concordia-City/Concordia_Altitude_and_Atmosphere.md`** | 3,233 m geographic / **~3,800 m physiological** · **no acclimatization** · heated-not-pressurized · the newcomer tell · robots as mobility |

**Cross-linked from** `Robot_Physiology_and_Cultural_Practices.md`, `Specs/Concordia.md`, and the
Sagittarius megasheet README. **Full source URLs are in each file**, per developer instruction.

## ⭐ The physics that produced usable mechanics

**Charging a cold cell below freezing causes lithium plating — permanent capacity loss.** Safe cold
charging requires **5–10% of normal current (10–20× slower)**. Usable capacity falls **20–30% near
freezing** and to **50–60% at −20 °C**. Below −40 °C lubricants *"exhibit properties similar to a solid."*

> ### ⭐⭐ THE DEATH SPIRAL — the finding the whole design hangs on
> **Warming your own cells costs energy. Below a threshold you cannot afford to warm them enough to charge
> safely.** ***Let charge fall too far in deep cold and you cannot recover unaided.*** **This supplies the
> Frostlanders' warmed charging shelters as infrastructure rather than hospitality, and gives "properly
> equipped" a concrete meaning: never crossing that line.**

> ### ⭐ THE INVERSION — a robot is safer MOVING than resting
> Work generates the heat that keeps cells and lubricants in range. **Stopping is the dangerous act** —
> the exact opposite of human cold survival. *A genuinely robot discipline, not borrowed mountaineering.*

## ⛔⛔ A CORRECTION — I had the acclimatization backwards, and said so to the developer

**I asserted that Concordia's long-term human residents would be fully acclimatized and need no breathing
assistance, reasoning by analogy to Andean highland populations.** ***Research contradicts this outright.***

> **"Lack of acclimatization to chronic hypoxia in humans in the Antarctica"**, *Scientific Reports* 7:18090
> (2017). **Concordia winter-overs of 10–12 months show NO acclimatization.** Residents remain at
> **91–94% arterial oxygen saturation indefinitely.**

⭐ **The corrected fact is better material than the assumption was.** An adapted population is a solved
problem that generates nothing. **A population that never adapts is a permanent, universally shared civic
condition that its robot neighbours are structurally incapable of sharing.**

⚠ **Recorded as a correction, not silently fixed** — the wrong version was stated aloud, and the
reasoning-by-analogy that produced it (*"highland populations adapt, so these will too"*) is exactly the
move that will produce it again.

## ⭐ And the architecture answer fell out of the same source

**Real Concordia Station holds +22 °C interior against −58 °C outside — thoroughly heated, and NOT
pressurized.** Occupants breathe 3,800 m air indoors and out.

> **So pressurization is not merely expensive — it is counterproductive.** Sea-level interiors would leave
> the population unable to function outdoors. ***A pressurized Concordia manufactures humans who cannot
> leave the building*** — in a city whose frontier district is defined by people who go out onto the
> plateau. **The absence of pressurization is a policy with an ongoing human cost.**

## Sources recorded in-file

**Battery:** Battery University BU-410 · RELiON cold-weather guide *(the 5–10% figure)* · capacity-vs-
temperature data · EV cold-weather preconditioning (arXiv 2512.00541).
**Materials:** Nord-Lock extreme-temperature metals · *J. Failure Analysis & Prevention* on DBTT ·
Klüber and FUCHS on low-temperature lubricants · *Lubricants* 10(1):1 on grease glass transition.
**Altitude:** *Sci. Rep.* 7:18090 · *Front. Physiol.* 13:819345 · PMC9078816 · *Pulmonology* 12-month
Concordia study · IPEV and ESA station pages.

⚠ **Every URL is in the two created files**, not only here — *a source recorded only in a session log is
one the next pass will not find.*
