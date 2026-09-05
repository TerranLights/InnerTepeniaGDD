# National-Origin Composition — CORPUS AUDIT, 2026-09-05

**Triggered by the developer:** *"it seems that we need to double-check the national-origin population
compositions for all of the cities (except for Palmer City, because that one has representation from all of the
countries by design)."*

**Origin:** the Davis/Zhongshan Russia inconsistency, found the same day while computing
{{Bunger Hills City}}. ⭐ ***Davis turned out to be one instance of thirty-three.***

> ## ⛔ NOTHING HAS BEEN FIXED. **This file is the finding, not the repair.**
> *The repair cascades into de-stacked per-nation tables and then into the census's National Origin table,
> which its own notes say must be **rebuilt as a direct sum of the Specs files**, never patched.*

---

# 1 · METHOD OF THE AUDIT

**Mechanical, not impressionistic.** *A checker recomputed what
`Upper_Earth_Immigration_Composition.md`'s own stated method produces for each city, and diffed it against what
the `Specs/` files actually carry.*

| Input | Source |
|---|---|
| Gini-adjusted effective pools *(43 nations)* | parsed from `Upper_Earth_Immigration_Composition.md` |
| City longitude → **solar UTC = round(lon ÷ 15)** | parsed from each `Specs/*.md` **Based on:** line |
| Tier membership | parsed from each `Specs/*.md` tier table |
| **±3 solar-UTC window** | the method's own gate *(Mirny: "Belarus (UTC+3, distance=3) just qualifies; Romania/Ukraine outside ±3 window")* |
| **UTC footprint, not scalar** | the rule added 2026-09-05 — *distance = minimum over zones holding a meaningful share of the pool* |

### ⚠ TWO BUGS IN THE CHECKER ITSELF, FOUND AND FIXED MID-AUDIT — recorded per the standing rule
1. ⛔ **Time-zone distance did not wrap.** *Antarctica is circumpolar; all meridians converge.* **Chile (−4) to
   a Ross Sea city (+11) is 9 zones the short way, not 15.** *Fixed to `min(|a−b|, 24−|a−b|)`.*
2. ⛔ **Gateway nations were not exempted.** *The file's own gateway table names **Argentina · Chile · South
   Africa · New Zealand · Australia**; they reach cities their own meridian does not.* **Before the fix the
   checker flagged South Africa at Halley — which is Cape Town, the gateway that serves it.**

### Scope
⛔ **Palmer City excluded** — *developer: all nations by design.*
⛔ **Ten interior cities excluded from the coverage check** — **Byrd · Concordia · Vostok · Kunlun · Dome Fuji ·
Amundsen · Troll · Princess Elisabeth · Abowasa · Sanay.** ***Solar UTC is meaningless for a site nobody sails
to*** — *they are reached through another city's port, so they inherit a gateway's position, not their own
meridian's.* ⭐ **That exclusion is itself a finding: the ±3 window only applies to cities with their own
coastal access, and the method never says so.**
✅ **26 coastal cities audited.**

---

# 2 · ⭐⭐⭐ THE HEADLINE — **23% of qualified entries are missing**

**Across the 26 coastal cities: 112 pool-qualified, in-window nations are listed. 33 are ABSENT.**

✅ **Seven cities are clean:** **Casey · Fort McMurdo · Marambio · Mirny · Rothera · Sinheung · Zhongshan.**

## Raw checker output — coverage

```
City                  UTC  T2flr  listed  qualif  MISSING   the missing, largest first
----------------------------------------------------------------------------------------------------
Belgrano               -2  17.0M      15       8        4   France(35), Italy(27), Canada(20), Spain(20)
Cape_Adare            +11  13.0M      12       7        1   Russia(25)
Casey                  +7  13.0M      13       6        0
Davis                  +5  13.0M      20       4        1   Russia(25)
Denison               +10  13.0M      11       6        1   Russia(25)
Dumont_dUrville        +9  13.0M      12       6        1   Russia(25)
Esperanza              -4   6.0M       7       6        2   Canada(20), Australia(13)
Fort_McMurdo          +11  27.0M      15       3        0
Halley                 -2  17.0M      17       8        2   Italy(27), Spain(20)
Janbogo               +11  13.0M      13       7        1   Russia(25)
Juan_Carlos            -4  20.0M      10       2        1   Canada(20)
Lazar                  +1  17.0M      25       7        2   Italy(27), Spain(20)
Marambio               -4  17.0M      10       4        0
Mawson                 +4  13.0M      26       7        3   Italy(27), Russia(25), Spain(20)
Mirny                  +6  13.0M      14       6        0
Neumayer               -1  17.0M      26       8        4   Italy(27), Russia(25), Canada(20), Spain(20)
Port_Lockroy           -4  17.0M       8       4        1   Canada(20)
Rothera                -5  17.0M       9       4        0
Sayowa                 +3  13.0M      25       7        3   Italy(27), Russia(25), Spain(20)
Scott                 +11  13.0M      12       7        1   Russia(25)
Sejong                 -4  17.0M      12       4        1   Canada(20)
Shirayuki              +5  13.0M      17       4        1   Indonesia(16)
Signy                  -3  17.0M       9       5        2   Canada(20), Mexico(18)
Sinheung               +5  13.0M      17       4        0
Zhongshan              +5  13.0M      18       4        0
Zukelli               +11  13.0M      12       7        1   Russia(25)
----------------------------------------------------------------------------------------------------
ACROSS 26 COASTAL CITIES:  112 qualified listed, 33 MISSING -> 23% absent
```

---

# 3 · ⭐⭐⭐ THE GAPS FALL IN SUBNET BLOCKS, NOT AT RANDOM

**Four mid-size nations account for 29 of the 33 gaps — and each is missing from a CONTIGUOUS BLOCK:**

| Nation | Pool | Missing at | The block |
|---|--:|--:|---|
| **Russia** | 25M | **10** — Cape Adare · Davis · Denison · Dumont d'Urville · Janbogo · Mawson · Neumayer · Sayowa · Scott · Zukelli | ⭐ **Janbogo / Mirny / Mawson — the Pacific and East Antarctic side** |
| **Canada** | 20M | **7** — Belgrano · Esperanza · Juan Carlos · Neumayer · Port Lockroy · Sejong · Signy | ⭐ **Palmer subnet, plus Neumayer** |
| **Italy** | 27M | **6** — Belgrano · Halley · Lazar · Mawson · Neumayer · Sayowa | ⭐⭐ **Halley + Mawson** |
| **Spain** | 20M | **6** — *the **same six** as Italy* | ⭐⭐ **identical footprint to Italy** |
| *France · Australia · Mexico · Indonesia* | | 1 each | |

> ## ⭐⭐ **ITALY AND SPAIN ARE MISSING FROM EXACTLY THE SAME SIX CITIES.**
> ***Two unrelated nations with different pools, corridors and gateways cannot coincide by chance across six
> sites.*** **They were not evaluated and rejected — they were never in the working set when those subnets were
> written.**
>
> ### ⭐ THE DIAGNOSIS: **the per-city nation SETS were assembled subnet-by-subnet, by hand, at different
> times — and a nation absent from one pass's working set never got added.**
> ***This is authoring drift, not a rule.*** **It is not a GPS violation, and it is not a judgment anyone made.
> Nobody decided Spain does not reach Halley. Spain simply was not on the desk that day.**

---

# 4 · ⚠ A SECOND, DIFFERENT PROBLEM — **RUSSIA'S PRESENT-SIDE IS STATION-DERIVED**

**Where Russia IS listed, it tracks real-world operator identity almost perfectly.** *Of its **9 coastal/nunatak
appearances**, **8 have a Russian-operated facility at or adjacent to the site**:*

| City | The facility |
|---|---|
| **Lazar** | Novolazarevskaya — *the file says so outright: "co-located at this exact site, giving Russia infrastructure advantage"* |
| **Mirny** | Mirny Station — *`Specs/Mirny.md` still tags it **`Russia (founding operator heritage)`*** |
| **Sinheung** | Progress Station |
| **Zhongshan** | *adjacent to* Progress |
| **Shirayuki** | *adjacent to* Progress |
| **Sejong** | Bellingshausen, King George Island |
| **Troll** · **Abowasa** | **Novo airfield — the gateway table names it *"(Russia-operated)"*** |
| ⚠ **Casey** | ***unexplained*** — the one appearance with no Russian facility |

⛔ **That is the GPS-purposes-only violation, and it has been caught before and not swept.** *`Zhongshan`'s own
2026-07-13 note says Russia was there for "operator heritage," that the claim was **also factually wrong** (the
Russian station is at Sinheung's site, not Zhongshan's) — **and then rewrote the justification while leaving
the row standing.*** **The reason was deleted; the effect was not.**

> ## ⭐⭐⭐ SO RUSSIA IS WRONG IN BOTH DIRECTIONS AT ONCE
> **Where a Soviet station exists, heritage put Russia in — the right answer for the wrong reason.**
> **Where none exists, its absence left Russia out — the wrong answer, ten times.**
> ***Davis is not an anomaly. Davis is the visible corner of a pattern that covers a third of the coast.***

⚠ **Same class, already logged three times for Italy at Janbogo** *(`Specs/Janbogo.md`: "Same Janbogo/Zukelli
bleed-over pattern previously found (and fixed) twice… this is its third occurrence")*. **The corpus keeps
catching this one city at a time. This audit is the first time it has been counted.**

---

# 5 · ⛔ WHAT IS **NOT** A BUG — do not "fix" these

**A second check looked for pool inversions** *(a nation tiered below one with a smaller pool)* **and returned 7
cities. Nearly all are DELIBERATE developer hand-tiering, and correcting them would destroy canon:**

| City | The inversion | Why it stands |
|---|---|---|
| **Shirayuki** | China 210M in Significant, **Japan 65M Primary** | *"founding population — Jeju-do diplomatic allocation; re-tiered 2026-07-06"* |
| **Sinheung** | China/Japan/Germany above **South Korea 26M Primary** | *"re-tiered 2026-07-06, strengthened same day"* — **and the 2026-07-13 founding correction** |
| **Zhongshan** | Indonesia 16M in Notable, Australia 13M in Significant | *Indonesia **"(demoted 2026-07-06)"*** |
| **Kunlun** | Japan/Germany/France above **Russia 25M Primary** | *curated 19-nation space/astronomy population* |
| **Concordia** | USA 155M in Significant, **Australia 13M Primary** | *hand-built; the census uses its "precise, already-computed per-nation figures directly"* |
| **Byrd · Dome Fuji** | many | *"everyone" cities — Byrd carries **36** Notable nations* |

⭐ **The lesson: the method produces a BASELINE, and the developer has overridden it deliberately at specific
cities. A checker cannot tell an override from an error — only the change-log can.** ⛔ **Never auto-apply.**

---

# 6 · ⚠ LIMITS OF THIS AUDIT — stated so the numbers are not over-read

1. ⚠ **The "qualified" test uses each city's OWN current Significant-tier floor**, which is mildly circular — *a
   city with a wrong list has a wrong floor.* ✅ *It errs conservative: too high a floor **understates** the
   missing count. **33 is a lower bound.***
2. ⚠ **Applying the ±3 window to large pools is an extension.** *The file documents it gating the **Notable**
   tier only.* **Whether a 27M pool at distance 3 belongs in Significant is a judgment the method does not
   make** — *this is why Belgrano's France/Italy/Spain flags are softer than the Russia ones.*
3. ⚠ **UTC footprints were supplied by the auditor**, not parsed from canon. *Russia +2…+12, Indonesia +7…+9,
   Australia +8…+10, USA −10…−5, Canada −8…−4, Brazil −5…−2, Mexico −8…−6; all others single-zone.*
4. ⚠ **Interior cities were not coverage-checked at all** *(10 of 36)*. **They need a gateway-relative rule that
   does not yet exist.**
5. ✅ **{{Bunger Hills City}} was built from the method the same day and is not evidence** — *it would pass its
   own test by construction.*

---

# 7 · 📋 PROPOSED ORDER OF REPAIR — **not started, awaiting a ruling**

1. **Rule on the window's scope first** — *does ±3 gate every tier, or only Notable?* ⛔ **Everything downstream
   depends on this and it is currently undefined.**
2. **Close the 33 coverage gaps**, cheapest-first: *the four block-missing nations account for 29 of them.*
3. **Re-derive Russia everywhere** — *strip the operator-heritage justifications at **Lazar** and **Mirny**
   (the last two live ones), and add Russia to the ten cities where it qualifies.* ⭐ **Its rows are mostly
   right; its reasons are wrong and its absences are wrong.**
4. **Re-de-stack** every touched city's per-nation table.
5. ⛔ **LAST — rebuild the census's National Origin table as a direct sum of the Specs files.** *Its own notes
   forbid patching it, and it has drifted twice before.*

📎 `Upper_Earth_Immigration_Composition.md` *(method + per-city raw layer)* · `Specs/*.md` *(authoritative)* ·
`Official_Population_Census.md` *(National Origin table, downstream of everything above)*
