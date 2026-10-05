<!-- Verbatim agent report, 2026-10-04 (corrected VOACAP parser plus ITU-R P.533). Model output: spot-check before relying on it. Corrects the Follow-up 4 statement that the 1913 relay used Wireless Hill (Perth): Wireless Hill is on Macquarie Island. -->

# Macquarie Island relay: Hobart to Dumont d'Urville, Ross Sea side, and the real Macquarie station

All access dates are 2026-10-04. (calc) marks my own calculation, (inf) marks inference, UNVERIFIED marks facts seen only in a search-engine summary. Source numbers [S#] continue the earlier tables. Nothing was written to the project; all work is in the session scratchpad.

**Method.** Same tools and thresholds as the previous legs: VOACAP (voacapl 16.1207W, corrected parser) and ITU-R P.533-14 (ITURHFProp with the P.372 noise library).
- Matrix: Jan and Jul, SSN 5/60/160, 100 W / 1 kW / 5 kW, 0 and +6 dBi at both ends, quiet-rural and rural noise at the receiving end, voice and weak-signal digital (FT8-class).
- The sender is the first-named station and the receiver (with the noise) is the second-named. In a chain, the first leg's noise is applied at Macquarie. How noisy Macquarie's receive site really is has not been measured (see Section 5).
- A chain is scored by "hours with all legs usable in the same hour", which assumes no store-and-forward. Store-and-forward would do better (inf).
- Usable means REL ≥ 0.8 with f ≤ median MUF (VOACAP), or BCR ≥ 80% (P.533). All times are UTC.
- Station positions used: Macquarie −54.50, 158.94; Cape Adare −71.30, 170.15; Jang Bogo −74.6247, 164.2278 (my stand-in for "Zukelli/Janbogo"); McMurdo −77.85, 166.67; Byrd −80.0167, −119.5167; Cape Denison −67.009, 142.664.

---

## 1. Distances, sea fraction, geometry (calc)

My distances match yours within 1 km: Hobart–Macquarie 1,543, Macquarie–DDU 1,688, Macquarie–Denison 1,637, Macquarie–Casey 2,868, Macquarie–Cape Adare 1,945, Macquarie–Jang Bogo 2,250, Macquarie–McMurdo 2,614, Macquarie–Byrd 3,920, Hobart–Cape Adare 3,398, Hobart–Jang Bogo 3,630, Hobart–McMurdo 3,984, Hobart–Byrd 5,388. Perth–Macquarie is 4,197 km (not 4,500).

**Sea fraction (GEBCO-2020, 150–220 samples):**

| Leg | Sea | Land along the path |
|---|---|---|
| Hobart–Macquarie | 99% | Tasmania coast; Macquarie end |
| Macquarie–DDU | 99% | DDU island only |
| Macquarie–Denison | 98% | Denison coast (211 m) |
| Macquarie–Cape Adare | 99% | coast |
| Macquarie–Casey | 94% | last 157 km, ice sheet to 912 m |
| Macquarie–Jang Bogo | 77% | last 483 km over Victoria Land (up to 2,668 m) |
| Macquarie–McMurdo | 79% | 477 km over the Transantarctic Mountains (to 2,852 m) |
| Macquarie–Byrd | 78% | last 841 km over West Antarctica (1,513 m) |
| Hobart–Cape Adare | 100% | none |
| Hobart–Jang Bogo / McMurdo / Byrd | 81% / 79% / 81% | 700–800 km of continent at the far end |
| Perth–Macquarie | 90% | 383 km of SW Australia |

**Hop geometry (F2 at 300 km, spherical earth; one-hop limit 3,836 km):**

| Leg | 1 hop | 2 hops |
|---|---|---|
| Hobart–Macquarie 1,543 | 17.3°, sec 2.43 | 772 km, 35.5°, sec 1.59 |
| Macquarie–DDU 1,688 | 15.3°, sec 2.57 | 844 km, 32.9° |
| Macquarie–Cape Adare 1,945 | 12.4°, sec 2.78 | 972 km, 28.9° |
| Macquarie–Jang Bogo 2,250 | 9.5°, sec 2.98 | 1,125 km, 25.0° |
| Macquarie–McMurdo 2,614 | 6.7°, sec 3.16 | 1,307 km, 21.2° |
| Macquarie–Casey 2,868 | 5.1°, sec 3.24 | 1,434 km, 19.0° |
| Macquarie–Byrd 3,920 | impossible (over the limit) | 1,960 km, 12.2°, sec 2.79 |
| Hobart–DDU 2,681 | 6.3°, sec 3.18 | 1,340 km, 20.6° |
| Hobart–Cape Adare 3,398 | 2.1° (marginal) | 1,699 km, 15.2° |
| Hobart–Jang Bogo 3,630 | 1.0° (marginal) | 1,815 km, 13.8° |
| Hobart–McMurdo 3,984 | impossible | 1,992 km, 11.9° |
| Hobart–Byrd 5,388 | impossible | 2,694 km, 6.2°, sec 3.19 |
| Perth–Macquarie 4,197 | impossible | 2,098 km, 10.9° |

A relay therefore converts a near-grazing or two-hop low-angle path into legs with steeper takeoff angles (12–35° against 2–6°). Low takeoff angles are what simple antennas and the D layer penalize most (inf).

---

## 2. Geomagnetic exposure and daylight (calc; AACGM-v2 at 110 km, 2025.5 / IGRF-14 dipole)

| Node | AACGM | Dipole |
|---|---|---|
| Hobart | −53.7° | −49.6° |
| **Macquarie** | **−64.1°** | **−59.5°** |
| DDU | −80.0° | −73.7° |
| Cape Denison | −79.9° | −73.7° |
| Casey | −80.5° | −75.5° |
| Cape Adare | −76.6° | −73.4° |
| Jang Bogo | −79.8° | −77.1° |
| McMurdo | −80.0° | −79.2° |
| Byrd | −68.7° | −72.4° |
| Perth | −43.6° | −41.0° |

Your dipole value for Macquarie (about −59) reproduces. Under the corrected AACGM frame Macquarie is at −64°, which is the equatorward edge of the auroral band (the oval is usually placed at about 65–75° [S38]). "Sub-auroral" is right for the dipole frame and only just right for AACGM. Exposure to storm-time auroral absorption is therefore higher than Hobart's and much lower than the Antarctic ends' (inf).

**Midpoint and last-hop positions (AACGM; midpoint / three-quarter point / poleward-most):**

| Leg | Midpoint | 3/4 point | Poleward-most |
|---|---|---|---|
| Hobart–Macquarie | −59.3° | −61.8° | −64.1° |
| Macquarie–DDU | −72.1° | −76.1° | −80.0° |
| Hobart–DDU | −66.9° | −73.5° | −80.0° |
| Macquarie–Cape Adare | −71.6° | −74.6° | −76.6° |
| Macquarie–Jang Bogo | −73.6° | −77.5° | −79.8° |
| Macquarie–McMurdo | −75.0° | −78.9° | −80.1° |
| Macquarie–Casey | −75.9° | −80.0° | −80.9° |
| Macquarie–Byrd | −75.0° | −73.9° | −75.2° |
| Hobart–Cape Adare | −68.1° | −73.8° | −76.6° |
| Hobart–McMurdo | −71.7° | −78.8° | −80.6° |
| Hobart–Byrd | −74.8° | −76.2° | −77.0° |
| Perth–Macquarie | −57.7° | −62.3° | −64.1° |

**Sunrise and sunset (calc, geometric, 15 Jan / 15 Jul):**
- Hobart: 15.0 h (18:49 to 09:49 UTC) / 9.3 h (21:38 to 06:55).
- Macquarie: 16.7 h (17:13 to 09:53) / 7.7 h (21:38 to 05:22).
- DDU: 21.4 h / 3.8 h.
- Cape Adare, Jang Bogo, McMurdo and Byrd: midnight sun in January and polar night in July.

**Polar-cap and auroral exposure estimates (inf; method as in the earlier reports):**
- **Antarctic ends at −77° to −80°** (DDU, Denison, Casey, Cape Adare, Jang Bogo, McMurdo): full PCA exposure, 0.7–2.5% of time (UNVERIFIED event statistics), plus 5–15% of hours of auroral or storm degradation.
- **Byrd (−68.7° AACGM)**: PCA 0.7–2.5%, auroral band 10–20% of hours.
- **Macquarie**: PCA 0.1–0.5% (only the larger events reach −64°), auroral degradation 3–10% of hours. BoM lists Macquarie Island among its wide-beam 30 MHz riometer sites (UNVERIFIED, search summary of a BoM page), so the station could monitor absorption itself.
- **Hobart and Perth**: not exposed except at G3 or stronger (about 50° geomagnetic [S15]).
- **A relay does not cure a correlated polar-cap blackout** at the Antarctic end. The relay's value is on the sub-auroral first leg only (inf; BoM advice is that PCA is relieved only by paths that avoid the polar region [S14]).

---

## 3. HF model results

### 3.1 Single legs (any-band hours per 24 h, V = VOACAP, P = P.533; minimum to maximum over SSN 5/60/160; Jan | Jul)

**1 kW, 0 dBi, voice, quiet-rural noise:**

| Leg | Jan | Jul |
|---|---|---|
| Hobart–Macquarie (1,543) | V 24, P 24 | V 24, P 24 |
| Macquarie–DDU | V 20–24, P 24 | V 22–24, P 23–24 |
| Macquarie–Denison | V 21–24, P 24 | V 22–24, P 23–24 |
| Macquarie–Casey | V 13–23, P 24 | V 24, P 23–24 |
| Macquarie–Cape Adare | V 17–22, P 24 | V 22–23, P 22 |
| Macquarie–Jang Bogo | V 18–21, P 24 | V 21–22, P 22 |
| Macquarie–McMurdo | V 16–21, P 24 | V 24, P 23–24 |
| Macquarie–Byrd | V 3–13, P 21–24 | V 12–19, P 11–18 |
| Hobart–Cape Adare | V 12–15, P 20–24 | V 19–23, P 12–19 |
| Hobart–Jang Bogo | V 11–12, P 16–24 | V 19–21, P 13–19 |
| Hobart–McMurdo | V 7–12, P 20–21 | V 14–17, P 13–18 |
| Hobart–Byrd | V 0–1, P 10–15 | V 6–14, P 2–10 |
| Perth–Macquarie | V 1–11, P 11–13 | V 10–22, P 11–18 |

**100 W, 0 dBi, voice, quiet noise:**
- Hobart–Macquarie: V 6–10, P 19–23 (Jan) | V 22–24, P 18–24 (Jul).
- Macquarie–DDU: V 6–7, P 24 | V 12–15, P 12–17.
- Macquarie–McMurdo: V 2–3, P 18–21 | V 11–14, P 10–17.
- Macquarie–Casey: V 1–2, P 8–15 | V 6–7, P 1–8.
- Macquarie–Byrd: 0 in both months.

**Rural noise, 100 W, 0 dBi, voice:** 0 h on every Antarctic leg and on the Perth leg; Hobart–Macquarie is V 2–5, P 1 (Jan) and V 14–18, P 0–5 (Jul). **5 kW, +6 dBi, rural noise** makes every Macquarie and Hobart leg 21–24 h on both models (the weakest being Hobart–Byrd V 10–12, P 24 in January).

**Weak-signal digital at 100 W, 0 dBi:** every leg is V 16–24, P 21–24 or better in quiet noise, and 19–24 in rural noise, except Hobart–Byrd (V 12–13 in January, rural). Weak-signal digital does not need a relay for any Hobart–Antarctic leg except Byrd.

**MUF ranges (1 kW +6 dBi, V | P, MHz):**
- Hobart–Macquarie: Jan SSN 5 7.0–15.2 | 6.4–16.0; Jul SSN 5 5.4–12.8 | 4.6–12.6.
- Macquarie–DDU: Jan SSN 5 8.1–14.6 | 7.4–15.6; Jul SSN 5 5.3–11.7 | 4.3–11.4.
- Macquarie–McMurdo: Jan SSN 5 10.6–16.1 | 9.2–14.7; Jul SSN 5 7.1–14.0 | 5.4–12.3.
- Macquarie–Byrd: Jan SSN 5 12.5–18.9 | 8.6–12.9; Jul SSN 5 8.0–14.5 | 4.8–9.8.
- Hobart–McMurdo: Jan SSN 5 12.0–20.0 | 8.0–14.1; Jul SSN 5 7.8–16.8 | 4.6–12.4.

**Per-band structure, Hobart–Macquarie (1 kW, 0 dBi, voice, quiet; V/P hours; 2.5, 3.5, 5, 7.1, 10.1, 14.2 MHz):**
- Jan SSN 60: 9/10, 11/13, 13/19, 15/24, 19/20, 6/12.
- Jul SSN 60: 15/15, 18/15, 22/16, 15/14, 10/11, 6/7.
- Jul SSN 5: 17/15, 19/17, 24/19, 12/11, 8/8, 0/0.

**Best UTC windows (1 kW, 0 dBi, voice, quiet, SSN 60; V | P):**

| Leg, month | 2.5 MHz | 3.5 | 5 | 7.1 | 10.1 |
|---|---|---|---|---|---|
| Hobart–Macquarie Jan | 10–18 \| 11–20 | 09–19 \| 10–22 | 08–20 \| 09–02 | 07–21 \| all | 20–14 \| 19–14 |
| Hobart–Macquarie Jul | 07–21 \| 08–22 | 05–22 \| 08–22 | 03–24 \| 07–18, 20–23 | 21–11 \| 21–10 | 22–07 \| 22–08 |
| Macquarie–DDU Jan | 12–17 \| 11–21 | 11–18 \| all | 08–19 \| all | 07–20 \| all | 18–13 (P) |
| Macquarie–DDU Jul | 06–21 \| 08–22 | 04–21 \| 08–22 | 24–22 \| 06–18, 21–22 | 24–11 \| 01–10, 22–23 | 24–07 \| 01–07 |
| Hobart–DDU direct Jan | 15–17 \| 17 | 11–17 \| 13–18 | 10–18 \| 13–20 | 08–18 \| 10–22 | 08–19 \| 09–07 |
| Hobart–DDU direct Jul | 08–21 \| 09–19 | 07–21 \| 09–21 | 05–22 \| 09–22 | 03–22 \| 08–17, 22 | 03–10, 22–01 \| 07–09, 22–24 |

The low bands (2.5–5 MHz) work in the daylight and evening hours of Tasmania and Macquarie (about 07–22 UTC in July, about 09–20 UTC in January); 7–14 MHz opens near local night in January and local morning in July (inf from the windows).

### 3.2 (1) Hobart to Dumont d'Urville: direct versus via Macquarie
Hours per 24 h with all legs usable in the same hour (V/P; min to max over SSN 5/60/160; Jan | Jul).

| Case | Direct (2,681 km) | Chain Hobart–Macquarie–DDU (3,232 km) |
|---|---|---|
| 100 W, 0 dBi, voice, quiet | V 3, P 9–11 \| V 11–19, P 2–13 | V 4–7, **P 19–23** \| V 12–15, P 12–17 |
| 100 W, +6 dBi, voice, quiet | V 18–22, P 24 \| V 24, P 22–24 | V 23–24, P 24 \| V 23–24, P 24 |
| 1 kW, 0 dBi, voice, quiet | V 14–21, P 24 \| V 24, P 22–24 | V 20–24, P 24 \| V 22–24, P 23–24 |
| 1 kW, +6 dBi, voice, quiet | V 23–24, P 24 \| V 24, P 23–24 | V 24, P 24 \| V 24, P 24 |
| 5 kW, 0 dBi, voice, quiet | V 22–24, P 24 \| V 24, P 23–24 | V 24, P 24 \| V 24, P 24 |
| 1 kW, 0 dBi, voice, **rural** | V 3–4, P 13–16 \| V 18–19, P 11–21 | V 5–8, P 24 \| V 13–16, P 18 |
| 5 kW, +6 dBi, voice, rural | V 22–24, P 24 \| V 24, P 24 | V 24, P 24 \| V 24, P 24 |
| 100 W, 0 dBi, digital, quiet | 24 / 24 | 24 / 24 |
| 100 W, 0 dBi, digital, rural | V 23–24, P 24 \| 24 | 24 / 24 |

- **What the relay changes (calc).** The chain gives about 10 extra hours a day (P.533) for a 100 W 0 dBi voice station in January, and 3–5 extra V hours. At 1 kW 0 dBi voice it gives 3–6 extra V hours in January and none in July. At +6 dBi, 5 kW or digital modes it gives nothing, because the direct path is already 22–24 h.
- **What it costs.** The path length increases by 20% (3,232 against 2,681 km), the relay must be built and kept alive on a windswept island, and the two legs must be open together. VOACAP and P.533 disagree sharply for the direct 100 W 0 dBi January case (V 3 against P 9–11), so the benefit is model-dependent there.

### 3.3 (2) Ross Sea side: direct from Hobart versus via Macquarie (hours with all legs usable)

**1 kW, 0 dBi, voice, quiet noise:**

| Destination | Direct Hobart–X | Chain Hobart–Macquarie–X |
|---|---|---|
| Cape Adare | V 12–15, P 20–24 \| V 19–23, P 12–19 | V 17–22, P 24 \| V 22–23, P 22 |
| Jang Bogo | V 11–12, P 16–24 \| V 19–21, P 13–19 | V 18–21, P 24 \| V 21–22, P 22 |
| McMurdo | V 7–12, P 20–21 \| V 14–17, P 13–18 | V 16–21, P 24 \| **V 24, P 23–24** |
| Byrd | V 0–1, P 10–15 \| V 6–14, P 2–10 | V 3–13, P 21–24 \| V 12–19, P 11–18 |

**100 W, 0 dBi, voice, quiet noise:**

| Destination | Direct | Chain |
|---|---|---|
| Cape Adare | V 0, P 0–7 \| V 4–12, P 0–10 | V 0–5, P 17–22 \| V 11–12, P 11–17 |
| Jang Bogo | V 0, P 0–7 \| V 1–8, P 0–4 | V 0, P 16–17 \| V 6–8, P 9–16 |
| McMurdo | V 0, P 0–1 \| V 0–1, P 0 | V 2–3, P 15–17 \| V 11–14, P 10–17 |
| Byrd | 0 \| 0 | V 0, P 0 \| V 0–1, P 0–1 |

**100 W, +6 dBi, voice, quiet:**
- Cape Adare: direct V 12–19, P 24 \| V 24, P 13–21; chain V 19–22, P 24 \| V 23–24, P 22–23.
- McMurdo: direct V 12–16, P 24 \| V 18–21, P 15–20; chain V 22–24, P 24 \| V 24, P 24.
- Byrd: direct V 0–2, P 14–22 \| V 8–16, P 9–16; chain V 11–17, P 24 \| V 16–19, P 13–21.

**1 kW, +6 dBi:** direct Cape Adare and Jang Bogo are already V 23–24, P 23–24 in both months; direct McMurdo is V 19–23 (Jan) and V 24 (Jul); via Macquarie 24 h. Direct Byrd is V 12–15 (Jan), V 21–22 (Jul); via Macquarie V 23–24 (Jan), P 21–22 (Jul).

**Rural noise at the Antarctic end, 1 kW, 0 dBi, voice:** direct Hobart–McMurdo is 0–2 h (both models) and via Macquarie V 3–5 / P 23–24 (Jan) and V 15 / P 15–21 (Jul). **5 kW +6 dBi, rural:** every route is V 19–24 / P 23–24, so power and gain solve it without a relay.

**Weak-signal digital at 100 W, 0 dBi:** direct and chain are both 24 h to Cape Adare, Jang Bogo and McMurdo; Byrd direct is V 16–24 / P 21–24, chain 23–24.

**Perth–Macquarie (4,197 km).** Not sensible: two hops at 11° takeoff, and with a 1 kW 0 dBi station it gives V 1–11, P 11–13 (Jan) and V 10–22, P 11–18 (Jul). Perth–Macquarie–DDU at 100 W 0 dBi is 0 h; Perth–Casey direct at 3,834 km (previous report) is better.

### 3.4 (3) Macquarie to Casey and to Byrd
- **Macquarie–Casey (2,868 km, 5° one-hop takeoff, 19° with two hops).** 1 kW 0 dBi quiet voice: V 13–23, P 24 (Jan) | V 24, P 23–24 (Jul). At 100 W 0 dBi it is V 1–2, P 8–15 | V 6–7, P 1–8; at +6 dBi 16–24 h. MUF (1 kW +6): Jan SSN 5 V 11.8–17.7 | P 10.0–16.2; Jul SSN 5 V 7.5–15.3 | P 5.4–13.8. Its poleward end is at −80.5° AACGM with a three-quarter point at −80°, so it carries full PCA exposure.
- **Macquarie–Byrd (3,920 km, over the one-hop limit).** Needs two hops at 12°. 1 kW +6 dBi: V 23–24, P 24 (Jan), V 24, P 21–22 (Jul). At 1 kW 0 dBi V 3–13, P 21–24 | V 12–19, P 11–18; 100 W 0 dBi 0 h. P.533 MUF is only 4.8–9.8 MHz in July at SSN 5 (V 8.0–14.5). Midpoint at −75.0° AACGM. This is a polar-cap-boundary path that needs a directional 1 kW station.

---

## 4. Relay-bottom-line questions answered from the model results

**Does a Macquarie relay buy anything for Hobart–DDU?**
- Only for a simple station (100 W, 0 dBi, voice) or in rural-noise January at 1 kW, where it adds about 10 hours (P.533) or a few V hours. It buys nothing at +6 dBi, 5 kW or with weak-signal digital (24 h direct), and it adds a failure point (inf). A single directional antenna at each end is cheaper and more reliable than a relay station (calc comparison of the matrix rows above).

**Does it make the Ross Sea cities reachable from Tasmania with modest stations?**
- At **1 kW, 0 dBi, voice, quiet noise** it moves McMurdo from V 7–12 / P 20–21 (Jan), V 14–17 / P 13–18 (Jul) to V 16–21 / P 24 (Jan), V 24 / P 23–24 (Jul). It lifts Cape Adare and Jang Bogo by 3–10 h as well. This is the clearest benefit.
- At **100 W, 0 dBi, voice** the chain helps only on P.533 (15–22 h) and not on VOACAP (0–5 h in January), so even the relay does not make a 100 W station reliable on voice; July V 11–14 h to McMurdo.
- **With weak-signal digital**, the Ross Sea cities are already reachable 24 h direct from Hobart with a 100 W 0 dBi station. Byrd is the exception (direct V 16–24 / P 21–24; chain 23–24).
- With rural noise and no gain, even the chain fails (Hobart–Macquarie–McMurdo 1 kW 0 dBi V 3–5 January).
- The Ross Sea legs end at −77° to −80° AACGM and inherit the full polar-cap risk; the relay cannot reduce it (inf).

---

## 5. Documented Macquarie Island practice (the relay site)

- **Station.**
  - Macquarie Island Station was established by the first ANARE in 1948 and is "the longest continuously operating Australian station in the sub-Antarctic or Antarctica". It sits on "a narrow, windswept isthmus near Wireless Hill" and has "more than 30 separate buildings". The number of expeditioners "varies from 14 to 40" [S63, AAD "Living on Macquarie Island"].
  - Other AAD wording gives about 40 in summer and about 16 in winter (UNVERIFIED, search summary).
  - Most buildings pre-date 1978 and are "deteriorating due to the extreme weather and approaching the end of their useful life", with ocean-inundation risk. A 2016 modernization stalled; $163.3 million was allocated in the 2024–25 Budget and a further $207.8 million from July 2028 [S64].
- **Radio practice.**
  - HF is the main mode between the station and field huts, with a daily schedule on 3023 kHz [S27, S28].
  - The island has four VHF repeaters, which "enable communications over the rugged landscape" (UNVERIFIED, search summary; the AAD statement that VHF is the main short-range medium with mountain-top repeaters is [S27]).
  - Each field hut has a remote-area power supply (wind generators and solar panels charging 12 V batteries) for lights and radios, with a small petrol generator as backup (UNVERIFIED, search summary of an AAD page).
  - Historically, communications with Australia used an Intelsat earth station (ANARESAT), and VHF and HF for the huts, ships and aircraft [S27].
  - The AAD HF list includes aircraft frequencies 5726, 9032 and 11256 kHz [S28].
- **Climate and the antenna problem.** Mean wind is about 25 km/h "throughout the year" and "almost constant"; low-pressure systems gust to over 170 km/h; annual rainfall is about 900 mm; "only a few days each year with no precipitation"; winters are generally cloudy; temperatures range from −9 to +13 °C [S65]. These values together mean heavy rime and wind loading on antennas and masts (inf; AWS lessons: "rime and hoar accumulation can interrupt and bias measurements", "mast stability/leaning" [S52]). Ground conductivity at a coastal site on an island is high (sea within metres), which helps HF antennas compared with ice (inf from the first-report conductivity discussion).
- **Resupply.** Macquarie is "only accessible by ship, with one annual resupply voyage carrying personnel and cargo" (UNVERIFIED, search summary); RSV Nuyina can carry 1,200 tonnes in up to 96 20-foot containers, has two barges of over 45 tonnes and two 55-tonne cranes, and up to four helicopters that can sling 1,200 kg [S66]. The Nuyina page gives no Macquarie-specific schedule.
- **1911–13 Macquarie relay (Mawson's expedition).**
  - The AAE station on Wireless Hill (Macquarie) used a Telefunken 1.5 kW spark-gap transmitter, a water-cooled De Dion-Bouton engine for power, and operators Charles Sandell and Arthur Sawyer. It signalled the SS Ulimaroa on 13 February 1912 (first outside radio contact), received ships up to Cape Horn by 14 February, and on 10 March 1912 communicated with Suva, 2,400 miles away [S67, S59].
  - It was "the first radio link between Australia and Antarctica": a relay between Mawson's Commonwealth Bay base and Australia [S67]. Commonwealth Bay established communication in 1913 (February per AAD [S59]; April per Maritime Radio [S67], a contradiction between the two).
  - Operator Jeffryes at Commonwealth Bay "sometimes spent entire evenings trying to transmit or receive a single message" because of static and auroral interference [S59].
  - The Cape Denison to Macquarie to Hobart chain is the same geometry as the chain modeled here (Denison–Macquarie 1,637 km, Macquarie–Hobart 1,543 km).
  - **Correction to my previous report:** I wrote that the relay "used Wireless Hill (Perth)". Wireless Hill in these AAD and Maritime Radio sources is the hill at Macquarie Island Station, not a Perth station; the Macquarie station itself was the relay.
- **ANARE history.** First stations in 1948 used 500 W Morse transmitters (UNVERIFIED, search summary). Macquarie's local amateur activity is by station communications technicians, e.g. VK0AI with over 1,500 contacts in more than 50 countries (UNVERIFIED, search summary). The 2018 VI70MI special-event callsign was operated from mainland Australia, not Macquarie [S68 WIA]; a search summary that suggested otherwise was wrong.
- **Dead ends.** The station's present transmitter powers, antenna types, HF frequency plan beyond 3023 kHz, and the noise level at the receive site were not found. No published failure rate for an unattended or lightly attended Macquarie antenna site was found.

**What an HF relay on Macquarie would need and what constrains it (inf from the sources).**
- Power: the station has generators (the main-station figures were not found); a relay-only load of about 1 kW transmit is small compared to a 14–40 person station but still needs a continuous supply and fuel by ship.
- Siting: a rocky coastal site on the isthmus is easily accessible; the problem is wind and rime loading, the 170 km/h gusts, and the station's aging infrastructure and modernization.
- Staffing: a station of 14–40 people already has communications technicians and daily HF routine, which makes it a much better relay host than any unattended island (compare the Elephant/Clarence discussion in the earlier report).

---

## 6. Bottom line (evidence-only; inferences flagged)

1. **Hobart–DDU:** A Macquarie relay is not needed if the stations have +6 dBi antennas, 5 kW or digital modes (direct is already 22–24 h on both models). It helps only a simple 100 W 0 dBi voice station in January (about 10 more hours on P.533) and costs a longer path and a second site. Prefer a directional antenna at each end.
2. **Ross Sea cities from Tasmania:** A Macquarie relay is useful for **1 kW, 0 dBi voice**: it takes McMurdo from 13–21 h to 23–24 h on P.533, and from 7–17 h to 16–24 h on VOACAP, and brings Cape Adare and Jang Bogo to 17–24 h. At 100 W 0 dBi voice it still fails on VOACAP, and in rural noise at 1 kW 0 dBi it fails everywhere. Weak-signal digital needs no relay except for Byrd.
3. **Macquarie as a destination:** Hobart–Macquarie (1,543 km) is 24 h for a 1 kW 0 dBi station, and Macquarie–Casey (2,868 km) is V 13–24 / P 23–24. Macquarie–Byrd (3,920 km) is feasible only at 1 kW with +6 dBi.
4. **Macquarie hosts a staffed relay** (about 14–40 people, 3023 kHz HF routine, four VHF repeaters) far more credibly than an unattended island, but the station is aging and reached by one annual ship voyage.
5. **Polar-cap blackouts:** Macquarie's −64° AACGM is out of reach of most PCA events, but the Antarctic legs end at −77° to −80°, so a PCA event closes every Ross Sea leg regardless of the relay.

---

## 7. Contradictions, unverified items and log

- **VOACAP versus P.533 disagree** on simple stations in January: Hobart–DDU 100 W 0 dBi voice V 3 against P 9–11; the chain V 4–7 against P 19–23. The benefit of the relay in January is therefore model-dependent.
- **Commonwealth Bay first contact:** February 1913 (AAD [S59]) against April 1913 ([S67]).
- **Macquarie population:** 14–40 [S63], about 40 summer / 16 winter (search summary), "up to 40" [S64].
- **UNVERIFIED:** four VHF repeaters, hut power systems, one annual resupply voyage, VK0AI contacts, BoM riometer at Macquarie, PCA event statistics.
- **Searches this session** (exact strings abbreviated): "Macquarie Island station Australian Antarctic Division population expeditioners power generators resupply ship Nuyina HF radio VHF repeater communications wind tussock", "Macquarie Island 1911 1913 wireless station Mawson Australasian Antarctic Expedition Wireless Hill Hobart relay Sawyer Sandell…", "Macquarie Island climate mean wind speed km/h gales days per year…", "Macquarie Island amateur radio VI70MI OR VK0 Macquarie HF contacts Europe North America Japan…".
- **Process notes:** the P.533 and VOACAP runs for all 13 legs completed with no empty cases. The Hobart–DDU rows reuse the previous report's runs, which used the same 100 W / 1 kW / 5 kW matrix.

### New sources (accessed 2026-10-04)
- [S63] AAD, Living on Macquarie Island: https://www.antarctica.gov.au/antarctic-operations/stations-and-field-locations/macquarie-island/living/
- [S64] AAD, Macquarie Island Station Project Background: https://www.antarctica.gov.au/antarctic-operations/stations-and-field-locations/macquarie-island/station-project/project-background/
- [S65] AAD, Climate, weather and tides at Macquarie Island: https://www.antarctica.gov.au/antarctic-operations/stations/macquarie-island/location/climate-weather-tides/
- [S66] AAD, Resupplying our stations (RSV Nuyina): https://www.antarctica.gov.au/nuyina/about/resupply/
- [S67] Maritime Radio, Macquarie Island wireless station: https://maritimeradio.org/other-stations/macquarie-island/
- [S68] WIA, Activation of VI70MI: https://www.wia.org.au/newsevents/news/2018/20180622-2/index.php
- Earlier sources [S14, S15, S27, S28, S38, S52, S59] as in the previous reports.
