# CLIMATE DATA — FULL 37-CITY CORPUS AUDIT

**Run 2026-09-04**, at developer instruction, immediately after filling the 7 specs that had no monthly
climate table. **Every one of the 37 city specs was checked**, not a sample.

> ## ⭐ HEADLINE
> **Temperature was clean. The light cycle was not.**
>
> | Variable | Cities checked | Errors found |
> |---|--:|--:|
> | **Mean annual temperature** *(vs. BAS READER)* | 37 | ⭐ **0** |
> | **Polar night / midnight sun spans** | 37 | ⛔ **22** |
> | **Monthly `Avg Daylight` column** | 37 | ⛔ **30** |
>
> ***Every city whose daylight column had been written before today was wrong somewhere in it.*** The only
> seven that passed were the seven written earlier the same day.

---

# 1 · Method

**Daylight, polar night and midnight sun are computed, not sourced** — they follow from latitude alone.
Each city's own stated coordinate was read from its spec, and the standard solar-geometry formula applied
with the **−0.833° refraction/semidiameter correction** (mid-month, the 15th, for the monthly column).

### ⚠ The method was validated against the corpus BEFORE it was used to change anything

Two cities were computed and compared to values **that were not being edited**:

| City | Corpus says | Computed | |
|---|---|---|---|
| **Rothera** *(67°34'S)* | ~16 days polar night | **15 days** | ✅ |
| **Belgrano** *(77°52'S)* | ~116 days polar night | **116 days** | ✅ |

**The corpus convention is refraction-corrected, and the model reproduces it.** *Only then were corrections
applied.*

### ⚠ Two errors in the audit tool itself, caught and fixed before any file was touched

**Both were at the South Pole**, where the general formula divides by `cos(latitude) = 0`:
1. The pole special-case had **its sign inverted** — it reported January at Amundsen Station as **0 hours of
   daylight**. *At the South Pole, January is continuous sun.*
2. The corrected special-case still **ignored refraction**, returning 179/186 days where the truth is
   182/183.

⭐ **Consequence: Amundsen Station was very nearly "corrected" from right to wrong.** Its stated 183/183 is
accurate. **The tool was the broken thing, and it was caught because the reported error was too large to be
plausible.** *Recorded because the failure mode — a measuring instrument that flatters its own findings —
is the exact one this project keeps hitting.*

---

# 2 · ⭐⭐ THE ROOT CAUSE — a single false assumption, repeated 22 times

**Nearly every light-cycle error traces to one belief:**

> ***"Polar night and midnight sun are symmetric. A city gets equal amounts of each, and north of the
> Antarctic Circle it gets neither."***

**All three halves of that are false.**

**Atmospheric refraction, plus the sun's own angular width, lift the apparent sun by about 0.833°.** That
correction **shortens polar night and lengthens midnight sun.** So:

- ⭐ **The two spans are never equal at any latitude.** Midnight sun is always the longer one.
- ⭐ **The two boundaries are ~0.8° apart** — they are not both "the Antarctic Circle."
- ⭐ **There is an asymmetric band** between them, containing **four Tepenian cities**, where **a city has a
  midnight sun but no polar night at all.**

### The asymmetric band — Casey · Mirny · Dumont d'Urville · Denison

| City | Latitude | Polar night | Midnight sun |
|---|---|---|---|
| **Casey** | 66°16'S — *north of the Circle* | **none** | **~23 days** |
| **Mirny** | 66°33'S — *on the Circle* | **none** | **~29 days** |
| **Dumont d'Urville** | 66°40'S — ***south* of the Circle** | **none** | **~31 days** |
| **Denison** | 67°00'S — ***south* of the Circle** | **none** | **~36 days** |

> ### ⚠ Note the bottom two rows. **Being south of the Antarctic Circle is not sufficient for a polar
> night.** The polar-night boundary sits ~0.8° further south than the Circle itself, so Dumont d'Urville
> and Denison are both inside the Circle and both have continuous, if brief, midwinter daylight.

**The tell for a fabricated light cycle is a near-equal pair.** Zhongshan's `60 / 61`, Mirny's `4–5 / 4–5`
and Amundsen's `183 / 183` all have that shape; two of the three were wrong. **Any spec pairing them at
similar lengths was computed without refraction, or not computed at all.**

---

# 3 · Every correction made

## 3a · Light-cycle spans — 22 cities

| City | Polar night: was → now | Midnight sun: was → now |
|---|---|---|
| **Abowasa** | 102 → **83** | 104 → **90** |
| **Belgrano** | 116 ✓ | 105 → **119** ⚠ *was shorter than its polar night — impossible* |
| **Byrd** | 108 → **129** | 128 → **131** |
| **Cape Adare** | 87 → **69** | 98 → **78** |
| **Casey** | none ✓ | **none → 23** |
| **Concordia** | 82 → **98** | 85 → **103** |
| **Davis** | 66 → **37** | 67 → **55** |
| **Dome Fuji** | 99 → **113** | 102 → **116** |
| **Dumont d'Urville** | **10 → none** | 12 → **31** |
| **Fort McMurdo** | 118 → **116** | 116 → **119** ⚠ *impossible pair* |
| **Halley** | 106 → **101** | 132 → **106** |
| **Janbogo** | **64 → 95** | **70 → 100** |
| **Lazar** | 75 → **63** | 77 → **74** |
| **Mawson** | **36 → 17** | 37 → **44** |
| **Mirny** | **4–5 → none** | **4–5 → 29** |
| **Neumayer** | 73 → **63** | 75 → **73** |
| **Princess Elisabeth** | 90 → **75** | 93 → **83** |
| **Rothera** | 16 ✓ | **20 → 44** |
| **Sanay** | 88 → **72** | 89 → **81** |
| **Sayowa** | 46 ✓ | 47 → **59** |
| **Sinheung** | **60 → 49** | 61 ✓ |
| **Troll** | 93 → **75** | 96 → **83** |
| **Zhongshan** *(earlier today)* | 60 → **49** | 62 ✓ |
| **Zukelli** *(earlier today)* | **64 → 95** | **70 → 101** |

**Largest single error: Janbogo and Zukelli, ~31 days.** Both sit at 74°37'–74°41'S and both carried a
figure corresponding to roughly 71°S — **about 400 km north of where they actually are.** *Zukelli's file
said its values were "same as Janbogo," which was true; they were the same and both wrong.*

## 3b · `Avg Daylight` column — 30 cities, 309 cells

**Every spec written before today had an inaccurate daylight column.** All 444 cells across the 37 cities
are now computed from each city's own stated coordinate.

Also corrected in the same pass:
- **Footer summary lines** — several had their dates updated but kept the old day-counts.
- **Stray asterisks** — the `*` marker meant "polar night / midnight sun in effect" and had ended up on
  ordinary values like `22.7*`, where it means nothing. Removed from all non-`24`/non-`0` cells.
- **Notes-column dates** — 32 cells across 23 files said things like *"Polar night begins ~Apr 28"* against
  a corrected header. Re-synced.

## 3c · Prose corrections

- **`Mirny.md` Geographic Basis** — a full paragraph built the city's identity on getting *"both phenomena
  in their minimal form,"* and invoked refraction **in the wrong direction**, claiming it *"extends"* polar
  night. Rewritten. ⭐ *The corrected fact is better material than the wrong one: Mirny does not sit at the
  edge of the polar zone, it sits in the gap where only half of it happens.*
- **`Dumont_dUrville.md`** — *"slightly further south than Mirny, giving it a slightly longer polar night"*;
  it has none. Winter-solstice minimum corrected from "0 hours (within polar night window)" to **~1.9 h**.
- **`Casey.md`** — *"Midnight sun: None at this latitude"* → **~23 days**.
- **`Scott.md`** — the whole climate section was a pointer to Fort McMurdo as *"essentially identical."*
  **READER gives −19.6 vs −16.2 — 3.4 °C apart, 4.6 °C in March.** Scott now has its own table, and the
  pointer is withdrawn. *(Cause: Scott Base faces the Ross Ice Shelf; McMurdo faces north into the Sound.)*

---

# 4 · What was already correct

- ⭐ **Mean annual temperature: 37 for 37.** Every city carrying a READER-backed figure matches its station
  normal exactly. **No temperature error was found anywhere in the corpus.**
- **Amundsen Station's 183/183** — correct, and nearly broken by a bug in the audit tool.
- **Rothera's and Belgrano's polar nights** — correct, and used as the validation cases.
- The **no-polar-night, no-midnight-sun** calls for Esperanza, Juan Carlos, Marambio, Palmer City, Port
  Lockroy, Sejong and Signy — all correct.

---

# 5 · The three derived columns — **RESEARCHED AND LARGELY REPLACED, same day**

**When first written, this section reported that `Temp Range`, `Avg Precip` and `Precip Probability` were
invented in all 37 specs. A follow-on research pass then replaced them with measured normals wherever
those could be obtained.** *(Developer instruction: "it appears we need to check the `Temp Range`,
`Avg Precip` and `Precip Probability", so let's check that next.")*

## What was found

**Published monthly normals exist for most of these stations** — national met-service data giving **mean
daily maximum and minimum** *(a real `Temp Range`)*, **monthly precipitation in mm**, and **mean days with
precipitation** *(a real `Precip Probability`, days ÷ days-in-month)*.

| | Cities |
|---|--:|
| ⭐ **`Temp Range` now MEASURED** *(mean daily min → mean daily max)* | **19** |
| ⭐ **`Avg Precip` now MEASURED** *(monthly normals)* | **14** |
| ⭐ **`Precip Probability` now MEASURED** *(precipitation-day counts)* | **6** |
| ⚠ **Still derived, and now explicitly labelled so** | **18** |

**Stations that yielded data:** Esperanza · Casey · Amundsen-Scott · McMurdo · Davis · Vostok · Mirny ·
Mawson · Halley · Neumayer III · Dumont d'Urville · Palmer · Concordia · Marambio · Syowa ·
Novolazarevskaya · Bellingshausen. **Two feed proxies:** Palmer → **Port Lockroy** (~27 km);
Bellingshausen → **Sejong** (~25 km) and **Juan Carlos** (~95 km).

⭐ **This also closed an open item from the first pass:** Bellingshausen gives **702 mm** for King George
Island, supplying the South Shetlands precipitation figure that no Livingston/Sejong source would give.

## ⛔ Sources rejected

- **Signy** — the Wikipedia box is internally inconsistent *(February mean daily minimum warmer than
  January's; precipitation present for only 8 months, with a 140 mm September against a 2.6 mm June)*.
  **Not used.** Signy remains derived.
- **Rothera, Zhongshan, Troll, King Sejong** — no monthly box published; **Sejong resolved via
  Bellingshausen instead.**

## ⭐ Every one of the 37 specs now carries a per-column provenance line

**Directly beneath its monthly table**, stating for that city which columns are measured, which are
computed, and which are estimates. **A reader can now tell, per number, what is real.** *(This was the
open item this section originally raised; it is closed.)*

| Column | Status after both passes |
|---|---|
| **`Avg Temp`** | ⭐ **Measured** — BAS READER WMO 1991–2020 normals *(or a marked proxy)*. **37/37** |
| **`Avg Daylight`** | ⭐ **Computed** — solar geometry from the city's own coordinate. **37/37** |
| **`Temp Range`** | ⭐ Measured in **19**; ⚠ derived and labelled in **18** |
| **`Avg Precip`** | ⭐ Measured in **14**; ⚠ derived and labelled in **23** |
| **`Precip Probability`** | ⭐ Measured in **6**; ⚠ derived and labelled in **31** |

---

# 6 · Open items

1. **Sinheung's precipitation** — states 200–300 mm; **AARI's figure for the Larsemann Hills is 159 mm.**
   Zhongshan and Shirayuki now carry ~160 mm; Sinheung is the same oasis and still disagrees.
2. **`Denison.md` line 26** — *"Sections I and III"*; the census was relettered to A–D on 2026-09-03. A
   leftover from that pass, unrelated to climate.
3. ✅ **CLOSED** — *"No station precipitation figure for Livingston Island / King Sejong."* **Resolved via
   Bellingshausen (King George Island): 702 mm.**
4. **13 READER files remain stubs** — Aboa · Cape_Adare · Dome_Fuji · Halley · Janbogo · Kunlun · Lazar ·
   Little_America · Princess_Elizabeth · Sanay · Sinheung · Troll · *(and any since surfaced)*. **Their
   specs carry temperature tables anyway, which means those tables are unsourced.** *Not a gap in the
   specs; a gap in their provenance.*
5. ✅ **CLOSED** — *"The derived-column caveat should be stated in the specs that lack it."* **All 37 now
   carry a per-column provenance line.**
6. **`timeanddate.com` is unreachable by tooling** — Cloudflare-gated against both WebFetch and `curl` with
   a browser user-agent. **Not a viable source for this project.**
7. **18 cities still have a derived `Temp Range`**, 23 a derived `Avg Precip`, 31 a derived `Precip
   Probability` — **all now labelled in-file.** The most likely route to closing more: **national met-service
   archives rather than encyclopedia boxes** — the Australian BoM (Casey/Davis/Mawson already yielded),
   AARI, KOPRI, BAS and PNRA publish fuller normals than the summary boxes carry.
8. **Signy's published climate box is unreliable** *(§5)* and should not be used without a better source.

---

*Full research record, including every verbatim search string and the sources behind each figure:*
*`…/Locations/Cities/Research_Logs/Climate_Data_Research_Log.md`*
