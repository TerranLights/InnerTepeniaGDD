<!-- Log written 2026-10-04: the research agent's third follow-up report (Byrd legs), extracted verbatim from its transcript (not re-typed). Uses the CORRECTED VOACAP parser. VOACAP and P.533 disagree sharply on polar paths (VOACAP pessimistic in January polar day, P.533 pessimistic in July polar night): treat the lower as the planning value; neither includes polar-cap absorption or auroral substorms. Availability percentages are the agent's estimates from NOAA counts, not measurements. UNVERIFIED = search summary only. -->

# Byrd legs: HF models, polar-cap exposure and satellite baseline

All access dates are 2026-10-04. (calc) marks my own calculation, (inf) marks inference, UNVERIFIED marks facts seen only in a search-engine summary. Source numbers [S#] refer to the earlier reports' source tables. Nothing was written to the project; all work is in the session scratchpad.

**Method.**
- This run uses the corrected VOACAP parser (voacapl 16.1207W, CCIR coefficients) and ITURHFProp (ITU-R P.533-14 with the P.372-14.3 noise library), exactly as in the previous report.
- Each leg was modeled for the full matrix: Jan and Jul, SSN 5/60/160, 10 W / 100 W / 1 kW, 0 / +6 dBi at both ends, quiet-rural (−164 dBW/Hz at 3 MHz) and rural (−150) noise, voice and weak-signal digital.
- Voice thresholds: 45 dB-Hz (VOACAP), 10 dB S/N in 3 kHz (P.533). Digital thresholds: 15 dB-Hz and −20 dB (FT8-class).
- Usable means REL ≥ 0.8 with f ≤ median MUF (VOACAP) or BCR ≥ 80% (P.533). Hours are UTC.
- Neither model includes polar-cap absorption (PCA) events or auroral substorms. Those are treated separately in Section 3.

**Coordinates.**
- Pole = −89.99, 0. McMurdo = −77.85, 166.67. Belgrano = −77.874, −34.627. Halley = −75.5833, −26.5667. Palmer City = −64.7667, −64.05. Rothera = −67.5667, −68.1167.
- "Zukelli/Janbogo": I used the real Jang Bogo station position, −74.6247, 164.2278. This is an assumption; it reproduces your 1,795 km.
- Additional stepping-stone legs I ran so the Pole and Ross Sea options can be judged: Pole–Belgrano, Pole–Rothera, Pole–Halley, McMurdo–Pole, McMurdo–Rothera.

---

## 1. Geometry and geomagnetic exposure (calc; AACGM-v2 at 110 km, 2025.5; IGRF-14 dipole)

**Distances.** Your distances reproduce (calc, R = 6371 km):

| Leg | km | Leg | km |
|---|---|---|---|
| Byrd–Rothera | 1,990 | Byrd–Pole | 1,111 |
| Byrd–Belgrano | 1,663 | Byrd–McMurdo | 1,485 |
| Byrd–Halley | 1,990 | Byrd–Jang Bogo | 1,796 |
| Byrd–Palmer | 2,349 | Pole–Belgrano | 1,347 |
| Pole–Rothera | 2,494 | Pole–Halley | 1,602 |
| McMurdo–Pole | 1,352 | McMurdo–Rothera | 3,445 |

**Node latitudes (AACGM / dipole).**

| Node | AACGM | Dipole |
|---|---|---|
| Byrd | −68.7° | −72.4° |
| Rothera | −53.8° | −58.4° |
| Palmer | −51.4° | −55.6° |
| Belgrano | −64.2° | −69.8° |
| Halley | −62.9° | −68.2° |
| Pole | −74.7° | −80.8° |
| McMurdo | −80.0° | −79.2° |
| Jang Bogo | −79.8° | −77.1° |

**Hop midpoints and extremes (AACGM; dipole midpoint in the last column).**

| Hop | Midpoint | Poleward-most | Equatorward-most | Dipole mid |
|---|---|---|---|---|
| Byrd–Rothera | −61.3° | −68.7° | −53.8° | −66.0° |
| Byrd–Belgrano | −67.1° | −68.7° | −64.2° | −72.6° |
| Byrd–Halley | −66.6° | −68.7° | −62.9° | −72.2° |
| Byrd–Palmer | −60.0° | −68.7° | −51.4° | −64.8° |
| Byrd–Pole | −72.1° | −74.7° | −68.7° | −76.9° |
| Byrd–McMurdo | −74.7° | −80.0° | −68.7° | −77.0° |
| Pole–Belgrano | −69.3° | −74.7° | −64.2° | −75.5° |
| Pole–Rothera | −64.3° | −74.7° | −53.8° | −69.6° |
| McMurdo–Rothera | −67.6° | −80.0° | −53.8° | −72.1° |

**Your two framing statements check out against the dipole values but need a qualifier under AACGM.**
- Byrd–Rothera "one quieter end at −58" matches the Rothera dipole latitude of −58.4°.
- The Byrd–Belgrano midpoint is −72.6° in the dipole frame, "deep in the polar cap". In the corrected (AACGM) frame it is −67.1°, and Byrd itself is −68.7°. That is the auroral-oval latitude band, not the polar-cap interior. NOAA and the literature put the quiet auroral oval at roughly 65–75° geomagnetic latitude [S38]. Both frames agree that the path is poleward of any mid-latitude sub-auroral protection. The practical consequence: Byrd–Belgrano is exposed to **both** daily auroral absorption and PCA, not PCA alone (inf).
- The Pole sits at −74.7° AACGM, which is inside the polar cap proper. A Pole stepping stone therefore does not avoid the cap.

**Day and night at Byrd (calc, geometric).** 131 days of midnight sun and 129 days of polar night. The Pole has 183 and 182 days. Belgrano has 119 and 116. Rothera has 44 and 15.

---

## 2. HF model results

### 2.1 Any-band usable hours per 24 h (V = VOACAP, P = P.533; minimum to maximum across SSN 5/60/160; Jan | Jul)

**1 kW, +6 dBi each end, quiet-rural noise, voice:**

| Link | Jan | Jul |
|---|---|---|
| Byrd–Rothera (1,990 km) | V 24, P 24 | V 24, P 23–24 |
| Byrd–Belgrano (1,663) | V 24, P 24 | V 24, **P 14–24** |
| Byrd–Halley (1,990) | V 24, P 24 | V 24, **P 11–24** |
| Byrd–Palmer (2,349) | V 24, P 24 | V 24, P 23–24 |
| Byrd–Pole (1,111) | 24 / 24 | V 24, P 24 |
| Byrd–McMurdo (1,485) | 24 / 24 | 24 / 24 |
| Byrd–Jang Bogo (1,796) | 24 / 24 | 24 / 24 |
| Pole–Belgrano (1,347) | 24 / 24 | V 24, P 23–24 |
| Pole–Rothera (2,494) | 24 / 24 | V 24, **P 6–20** |
| Pole–Halley (1,602) | 24 / 24 | V 24, P 17–24 |
| McMurdo–Pole (1,352) | 24 / 24 | 24 / 24 |
| McMurdo–Rothera (3,445) | V 21–24, P 24 | V 24, **P 5–21** |

**1 kW, 0 dBi, quiet-rural, voice:**

| Link | Jan | Jul |
|---|---|---|
| Byrd–Rothera | **V 10–14**, P 24 | V 19, **P 10–20** |
| Byrd–Belgrano | 24 / 24 | V 24, **P 5–18** |
| Byrd–Halley | V 20–24, P 24 | V 22–24, **P 3–17** |
| Byrd–Palmer | **V 9–15**, P 24 | V 9–13, P 10–18 |
| Byrd–Pole | 24 / 24 | V 24, P 14–23 |
| Pole–Rothera | V 9–17, P 24 | V 10–15, **P 0–4** |

**100 W, +6 dBi, quiet-rural, voice:**

| Link | Jan | Jul |
|---|---|---|
| Byrd–Rothera | V 17–20, P 24 | V 22–23, P 15–20 |
| Byrd–Belgrano | 24 / 24 | V 24, **P 5–18** |
| Byrd–Halley | 24 / 24 | V 24, **P 5–18** |
| Byrd–Palmer | V 11–19, P 24 | V 14–16, P 16–20 |
| Byrd–Pole | 24 / 24 | V 24, P 15–23 |
| Byrd–McMurdo | 24 / 24 | V 24, P 20–24 |
| Byrd–Jang Bogo | 24 / 24 | V 24, P 23–24 |
| Pole–Rothera | V 17–21, P 24 | V 14–15, **P 0–5** |

**100 W, 0 dBi, quiet-rural, voice (the "simple station"):**

| Link | Jan | Jul |
|---|---|---|
| Byrd–Rothera | **V 0**, P 17–19 | V 3–6, **P 0** |
| Byrd–Belgrano | **V 0**, P 24 | V 14–15, **P 0–1** |
| Byrd–Halley | V 0, P 24 | V 7–12, P 0 |
| Byrd–Palmer | V 0, P 16–18 | V 0–2, P 0 |
| Byrd–Pole | V 24, P 24 | V 24, P 3–12 |
| Byrd–McMurdo | V 19–22, P 24 | V 24, P 6–15 |
| Byrd–Jang Bogo | V 6–18, P 24 | V 19–20, P 0–13 |
| Pole–Belgrano | V 21–24, P 24 | V 24, P 0–2 |

**Rural noise, +6 dBi, 100 W, voice:**

| Link | Jan | Jul |
|---|---|---|
| Byrd–Rothera | **V 0**, P 24 | V 10–14, P 4–16 |
| Byrd–Belgrano | V 5–8, P 24 | V 15–18, **P 0–8** |
| Byrd–Palmer | V 0, P 24 | V 5–8, P 4–8 |
| Byrd–Pole | 24 / 24 | V 24, P 8–18 |

**1 kW, +6 dBi, rural noise, voice:**

| Link | Jan | Jul |
|---|---|---|
| Byrd–Rothera | V 18–24, P 24 | V 23, P 16–22 |
| Byrd–Belgrano | 24 / 24 | V 24, **P 5–19** |
| Byrd–Halley | 24 / 24 | V 24, **P 5–19** |
| Byrd–Palmer | V 21–24, P 24 | V 19–21, P 21–24 |

**Weak-signal digital:**

| Case | Jan | Jul |
|---|---|---|
| 10 W, +6 dBi, rural noise, Byrd–Rothera / Byrd–Palmer | 24 / 24 | V 24, P 23–24 / V 24, P 24 |
| 10 W, +6 dBi, rural noise, Byrd–Belgrano / Byrd–Halley | 24 / 24 | V 24, **P 11–24** |
| 10 W, 0 dBi, rural noise, Byrd–Rothera | V 17–21, P 24 | V 22–23, P 14–20 |
| 100 W, 0 dBi, rural noise, all Byrd legs | 24 / 24 | 24 / 24 on both models, except Byrd–Belgrano and Byrd–Halley (P 11–24) |

**Models disagree sharply on polar paths. Read the disagreement as the uncertainty, not as noise.**
- In January (24 h sun at Byrd) VOACAP is pessimistic on 0 dBi voice, because it computes strong polar-day D-layer absorption (V 0–14 h against P 17–24 h).
- In July (polar night at Byrd) P.533 is much more pessimistic (P 0–20 h against V 3–24 h on the 0 dBi cases).
- I treat the lower of the two as the planning value for each season.

### 2.2 Per band, 1 kW, +6 dBi, voice, quiet-rural (hours/24, V/P; columns 2.5, 3.5, 5, 7.1, 10.1, 14.2 MHz)

**Byrd–Rothera.**

| Month, SSN | 2.5 | 3.5 | 5 | 7.1 | 10.1 | 14.2 |
|---|---|---|---|---|---|---|
| Jan 5 | 1/24 | 9/24 | 15/24 | 24/24 | 22/24 | 11/24 |
| Jan 60 | 0/21 | 5/24 | 12/24 | 18/24 | 24/24 | 15/24 |
| Jan 160 | 0/6 | 0/23 | 6/24 | 13/24 | 19/24 | 20/24 |
| Jul 5 | 24/17 | 24/17 | 20/14 | 9/5 | 0/0 | 0/0 |
| Jul 60 | 23/15 | 24/18 | 24/24 | 15/13 | 1/2 | 0/0 |
| Jul 160 | 19/9 | 23/16 | 24/19 | 22/22 | 8/14 | 2/3 |

**Byrd–Belgrano.**

| Month, SSN | 2.5 | 3.5 | 5 | 7.1 | 10.1 | 14.2 |
|---|---|---|---|---|---|---|
| Jan 5 | 2/24 | 14/24 | 24/24 | 24/24 | 24/24 | 0/24 |
| Jan 60 | 0/24 | 5/24 | 18/24 | 24/24 | 24/24 | 0/24 |
| Jan 160 | 0/24 | 0/24 | 5/24 | 20/24 | 24/24 | 9/24 |
| Jul 5 | 24/0 | 23/12 | 14/7 | 3/4 | 0/0 | 0/0 |
| Jul 60 | 24/0 | 24/16 | 24/22 | 7/7 | 0/4 | 0/0 |
| Jul 160 | 24/0 | 24/0 | 24/23 | 24/24 | 3/15 | 0/3 |

**Median MUF ranges (V | P, MHz).**

| Month, SSN | Byrd–Rothera | Byrd–Belgrano |
|---|---|---|
| Jan 5 | 12.6–15.1 \| 12.2–14.9 | 12.0–13.7 \| 11.8–13.6 |
| Jan 160 | 13.4–17.8 \| 13.3–16.1 | 12.3–15.3 \| 12.9–15.9 |
| Jul 5 | **4.1–7.9 \| 2.9–7.1** | **3.5–7.5 \| 2.6–6.8** |
| Jul 160 | 6.6–14.4 \| 6.7–13.6 | 8.1–10.5 \| 8.1–10.9 |

**Best UTC windows, 1 kW +6 dBi quiet voice (V | P).**

| Case | Band | Byrd–Rothera | Byrd–Belgrano |
|---|---|---|---|
| Jan SSN 60 | 5 MHz | 24–11 \| all | 18–11 \| all |
| Jan SSN 60 | 7.1 MHz | 20–13 \| all | all \| all |
| Jan SSN 60 | 10.1 MHz | all \| all | all \| all |
| Jan SSN 60 | 14.2 MHz | 16–18, 20–07 \| all | no \| all |
| Jul SSN 60 | 2.5 MHz | 16–14 \| 23–13 | all \| no |
| Jul SSN 60 | 3.5 MHz | all \| 22–15 | all \| 15, 18–08 |
| Jul SSN 60 | 5 MHz | all \| all | all \| 02–23 |
| Jul SSN 60 | 7.1 MHz | 04–09, 14–22 \| 04–09, 15–21 | 04–10 \| 03–09 |
| Jul SSN 5 | 3.5 MHz | | 01–23 \| 03–08, 12, 15–19 |
| Jul SSN 5 | 5 MHz | | 03–12, 15–18 \| 04–10 |
| Jul SSN 5 | 7.1 MHz | | 06–08 \| 05–08 |

**Solar-minimum polar-night gap on Byrd–Belgrano (P.533, July SSN 5, 1 kW +6 dBi quiet voice, tested 1.8–5 MHz).**
- No frequency meets BCR ≥ 80% at 01, 02, 11, 13, 14 and 20–24 UTC, about 10 hours. Median basic MUF is 2.6–3.4 MHz overnight (calc).
- At SSN 60 the same hours are usable on 3.5 and 5 MHz, so the gap is a solar-minimum feature.
- Byrd–Rothera does not have it: 1.8–2.5 MHz covers the night hours, with the only no-band hour at 21 UTC at SSN 5.

**Other legs (any-band, 1 kW +6 dBi, voice quiet).**
- **Byrd–Pole (1,111 km).** Usable on 2.5–7.1 MHz in January and 2.5–5 MHz in July, 24 h on both models. At 100 W +6 dBi in July P.533 gives 15–23 h.
- **Byrd–McMurdo and Byrd–Jang Bogo.** Both 24 h in all cases at 1 kW. At 100 W 0 dBi in July P.533 gives only 6–15 h and 0–13 h.
- **Pole–Rothera (2,494 km).** July P.533 only 6–20 h at 1 kW +6 dBi and 0–5 h at lower power. This is the weakest stepping-stone leg.

### 2.3 Terrain and MF/HF ground wave
The ice sheet gives no usable ground wave at these ranges. At a 0.3 mS/m or lower surface the 1 MHz 1 kW field is 8 dBµV/m at 8 km and drops below 0 dBµV/m by about 100 km (calc, NTIA LFMF; first-report tables). There is no line of sight: the earth bulge for 1,990 km is about 58 km at the midpoint (calc: 995²/(2 × 1.3333 × 6371) = 58 km).

---

## 3. Polar-cap and auroral exposure (documented behavior, then my estimates)

### 3.1 Documented behavior
- **BoM [S14].** "The effects of PCAs on polar sky wave paths can sometimes be overcome by relaying messages on paths which avoid the polar regions." The same document states that even the winter polar zone, "a region of perpetual darkness", can suffer the effects of PCAs.
- **McMurdo–South Pole oblique sounding (about 1,300 km) [S55, Atmos. Meas. Tech. 2020].**
  - 12 frequencies from 2.6 to 7.2 MHz were operated between 28 February and 13 March. "No signals were received below 4.1 MHz, due to absorption and reduced transmitter efficiency." No signal was received on 4.4 MHz "for unknown reasons".
  - The E layer was consistently visible at 100–120 km on 4.1 and 5.1 MHz. Sporadic F-region enhancements around local noon on the higher frequencies carried virtual-height spread of more than 500 km.
  - GPS TEC predicted 7.2 MHz propagation with only a 40% true-positive and 73% true-negative rate.
  - This was a summer-end (sunlit) test. My models give 2.5–3.5 MHz as the workhorse for Byrd–Rothera/Belgrano in winter, so this is direct evidence that the low-band winter workhorse can fail on the polar-cap path (inf).
- **D-RAP scaling [S57].** Absorption scales as A(f) = A(f0)(f0/f)^1.5, so a 1 dB event at 30 MHz gives about 14.7 dB at 5 MHz and 42 dB at 2.5 MHz one way (calc). Daytime A = 0.115 √J(>5.2 MeV), nighttime A = 0.020 √J(>2.2 MeV) dB, so polar-night PCA is about 17% of the daytime value for equal flux (calc). The low bands go first, and bands at 10 MHz and above survive moderate events (inf).
- **NOAA scales [S15] (cycle averages).**
  - Radiation storms: S1 50 per cycle ("minor impacts on HF radio in the polar regions"), S2 25, S3 10 ("degraded HF radio propagation through the polar regions"), S4 3 ("blackout"), S5 under 1 ("complete blackout possible").
  - Geomagnetic storms: G1 or stronger on 900 days per cycle (22% of days, calc), G2 360 days (9.0%), G3 130 days (3.2%), G4 60 days (1.5%), G5 4 days (0.1%).
- **Aurora and auroral-zone HF [S56, S38].**
  - Auroral absorption peaks around 64–68° magnetic latitude in the pre-noon and pre-midnight sectors, with values up to about 6 dB at 30 MHz (UNVERIFIED, search summary).
  - A high-latitude HF experiment concluded that "a significant level of auroral absorption decreases the reliability of the HF communication inside the auroral zone" and that the main ionospheric trough and its poleward edge control winter evening and night propagation [S56].
- **Antarctic riometer statistics.** BoM and AAD operate 30 MHz riometers at Casey, Davis, Mawson and Macquarie, with data archived at the World Data Centre [S41]. I found no published occurrence percentage for Byrd, Pole, Belgrano or Halley (dead end at the sources).

### 3.2 Explicit estimates (inf; derived from the NOAA counts and flagged assumptions; not measurements)

| Leg group | PCA, share of time | Auroral / storm degradation, share of hours | Notes |
|---|---|---|---|
| Byrd–Rothera, Byrd–Palmer (Byrd end at −68.7° AACGM, other end −51 to −54°) | 0.3–1% (S3 and stronger, 10 per cycle × 1.6–4 days) | 5–15% of hours, concentrated at the Byrd end | Rothera/Palmer end is sub-auroral; Byrd end is in the auroral band |
| Byrd–Belgrano, Byrd–Halley (midpoint −67°, far end −63 to −64°) | 0.7–2.5% (S1 and stronger, 50 per cycle × about 2 days, plus S3 and stronger tail) | 10–20% of hours | Both ends and the midpoint are in or near the auroral band; no quiet end |
| Byrd–Pole, Pole–Belgrano (Pole at −74.7° inside the cap) | 0.7–2.5% | 10–20% | Pole shares the cap |
| Byrd–McMurdo, Byrd–Jang Bogo, McMurdo–Pole (McMurdo −80°, Jang Bogo −79.8°) | 0.7–2.5% | 10–20% | Full polar-cap exposure at one end |

**Lower bound of the PCA bracket (0.7%).** About 29 days per cycle, from 24 moderate events of about 8 h and 13 severe events of 1.6 days (UNVERIFIED search summary of a 2022 Space Weather paper that returned 403). **Upper bound (2.5%).** 50 S1 events times about 2 days per cycle (calc).

**Correlated-blackout caveat.** PCA affects every node poleward of about −60° at once. Extra stepping stones at the Pole, McMurdo or Jang Bogo are poleward of −74° and share the same blackout, so they cannot cure a correlated PCA event (inf, consistent with BoM advice that the only relief is a path that avoids the polar regions [S14]).

**Realistic availability bracket per hop (inf).**
- Take the clean-model availability (24 h with a band for 1 kW +6 dBi quiet voice, or the lower of V and P).
- Subtract the PCA share and the auroral/storm share above.
- This gives about **80–95% for voice and about 88–98% for weak-signal digital with automatic band selection and retries**, year-round, per hop on the Byrd–Rothera, Byrd–Belgrano, Byrd–Halley and Byrd–Palmer legs.
- At solar minimum (about 2030, SSN 5; NOAA predicts 9.3 for October 2030 [S17]) the July voice gap on Byrd–Belgrano and Byrd–Halley widens (P.533 11–14 h at 1 kW +6 dBi), so the voice figure falls toward 60–75% in polar night (inf from Section 2.2). Digital stays 88–95%.
- PCA counts are lower near minimum, but each event removes the very low bands the minimum-phase link depends on (inf).

---

## 4. Non-HF baseline: geostationary visibility at Byrd (calc)

- Geostationary satellites are visible to a geocentric limit of 81.3° latitude (acos(Re/rs) with Re = 6378.137 km, rs = 42,164 km).
- At Byrd (−80.0167°, −119.5167°) the best case, a satellite at the station's own longitude, has a central angle of 80.0° and an elevation of **+1.3°**. At sub-satellite longitude −90° the elevation is −0.0°, at −150° −0.1°, at −60° −3.6°.
- So the geostationary elevation at Byrd is **0 to 1.3°**, effectively masked by any horizon feature. NASA states the same limit: satellites "are visible to latitudes as high as 81°, they appear on the local horizon and are easily masked" [S34]. Palmer (best case 16.9°) and Rothera (14.0°) are marginal but usable; the Pole is beyond the limit.
- Polar-orbiting links are the baseline: USAP deep-field camps carry an HF radio plus at least two Iridium phones because they need two long-range means that "do not depend only on satellite" [S3]. Iridium works at the poles. Starlink service at McMurdo from 14 September 2022 is UNVERIFIED (search summary). I did not verify any satellite link at the real Byrd site.

---

## 5. Bottom line (evidence-only, with inferences flagged)

**Byrd–Rothera (1,990 km).**
- **Feasible with 1 kW and +6 dBi at both ends (24 h on both models).** At 100 W and +6 dBi voice is 15–23 h; at 100 W and 0 dBi voice fails in January on VOACAP (0 h) and is 0–6 h in July.
- Use 5–10 MHz in January (7.1 and 10.1 MHz 18–24 h; 14.2 MHz only at higher SSN). Use 2.5–5 MHz in July (all-hours on 3.5 and 5 MHz in the models), with 7.1 MHz only in the 04–09 and 15–21 UTC windows.
- The quieter −54° AACGM Rothera end shortens the auroral exposure, and P.533 finds 1.8–2.5 MHz usable through most night hours even at SSN 5. This leg has the best winter solar-minimum behavior of the Byrd legs.
- **Weak-signal digital at 10 W with +6 dBi is 24 h on both models** (P 23–24 in July). Realistic reliability (inf): about 80–90% voice, about 90–97% digital.

**Byrd–Belgrano (1,663 km).**
- **Workable in January (24 h at 1 kW +6 dBi on 5–10 MHz), but the hard case is polar night at solar minimum.** P.533 gives only 14 h at 1 kW +6 dBi in July SSN 5 and 5–18 h at 100 W +6 dBi.
- Weak-signal digital is robust: 100 W +6 dBi rural noise gives 24 h on both models except July SSN 5 (P 13–24). 10 W digital +6 dBi is P 13–24 in July.
- The path is entirely at −64° to −69° AACGM (dipole −72.6° at the midpoint), so both daily auroral absorption and PCA affect it. Realistic reliability (inf): 75–90% voice and 85–95% digital year-round, lower in July and at 2030 minimum.
- The Byrd–Halley leg is equivalent or slightly worse (P 11–24 h at 1 kW +6 dBi in July).

**Byrd–Palmer (2,349 km).** 1 kW +6 dBi 23–24 h (July P 23–24); marginal at 100 W. Longer than Byrd–Rothera for no benefit unless Palmer is the hub.

**Stepping stones.**
- **The Pole** does not help. Byrd–Pole is 1,111 km and works 24 h, but Pole–Belgrano is 1,347 km and works 23–24 h in July, Pole–Rothera (2,494 km) only 6–20 h, and the Pole sits at −74.7° AACGM inside the cap. The polar-cap interior is exactly where McMurdo–South Pole sounding found no signal below 4.1 MHz [S55]. The Pole adds a failure point and shares the PCA blackout.
- **McMurdo and Jang Bogo (Ross Sea).** Byrd–McMurdo and Byrd–Jang Bogo work 24 h at 1 kW, but both are at −80° AACGM and McMurdo–Rothera (3,445 km) is only 5–21 h in July. They are useful only as destinations (an Ross Sea station), not as stepping stones to the Peninsula.
- **A lower-latitude relay (the BoM advice).** The only path that avoids the polar cap is one through the Peninsula or Weddell side (Rothera/Palmer at −51 to −54°). The Byrd–Rothera leg is already the one that does this (inf).

**Which is better for a settled community.** Byrd–Rothera (or Byrd–Palmer if Palmer is the hub) is preferable to Byrd–Belgrano: it has one quiet end, a better solar-minimum winter, and the same power and antenna requirement. Both require at least 1 kW with +6 dBi (directional) antennas for reliable voice, or weak-signal digital at 10–100 W with +6 dBi for text and data. A simple 100 W, 0 dBi station cannot hold voice on either leg (VOACAP 0 h in January; P.533 0–1 h in July).

---

## 6. Contradictions, unverified items and log

- **Dipole versus AACGM latitude.** The Byrd–Belgrano midpoint is "deep in the polar cap" at −72.6° dipole but −67.1° AACGM (auroral band). Byrd is −72.4° dipole and −68.7° AACGM. Both frames place it poleward of any quiet-latitude protection; they differ on whether PCA or auroral absorption dominates.
- **VOACAP versus P.533** disagree by up to 20 h on the polar legs (January pessimistic in VOACAP, July pessimistic in P.533). Neither is validated for the Byrd region; no Byrd HF measurements were found.
- **UNVERIFIED.** The 218-event riometer count, 24 moderate and 13 severe PCA events with 8 h and 1.6 day mean durations, auroral-absorption latitude statements, Starlink at McMurdo, and the Jang Bogo identification of "Zukelli/Janbogo".
- **Dead ends.** Quantitative auroral-absorption occurrence at any Antarctic station; documented HF performance of the actual Byrd Station; Iridium or Starlink availability at Byrd; any published Weddell/West-Antarctic polar-cap HF availability statistics. All died at the sources.
- **Search this session:** "South Pole Station HF radio communications McMurdo HF reliability polar cap blackout winter polar night HF South Pole to McMurdo frequencies 7995 kHz field party Byrd Station HF history" (returned the NASA 1991 report, the McMurdo–South Pole papers and RadioReference; nothing on Byrd). Earlier searches in this task cover PCA statistics, riometers and the Weddell sector (previous report).
- **Calculations in this section:** haversine distances; AACGM-v2 and IGRF-14 dipole latitudes; geostationary elevation (cos γ = cos φ cos Δλ, el = atan((cos γ − Re/rs)/sin γ)); polar day/night lengths; earth bulge d²/(8kR) with k = 4/3; PCA frequency scaling (f0/f)^1.5; all HF tables from VOACAP and ITURHFProp as described in the Method note.

## Sources used for this section
- [S3] USAP Peninsula Field Manual 2026, Communications chapter: https://www.usap.gov/usapgov/travelAndDeployment/documents/USAP-Peninsula-Field-Manual-2026-Communications.pdf
- [S14] BoM Space Weather Services, Introduction to HF Radio Propagation (2016): https://www.sws.bom.gov.au/Category/Educational/Other%20Topics/Radio%20Communication/Intro_HF_Radio.pdf
- [S15] NOAA SWPC, NOAA Space Weather Scales: https://www.spaceweather.gov/noaa-scales-explanation
- [S17] NOAA SWPC solar-cycle JSON: https://services.swpc.noaa.gov/json/solar-cycle/predicted-solar-cycle.json
- [S34] NASA NTRS, Polar Communications: Status and Recommendations (1991): https://ntrs.nasa.gov/api/citations/19910021045/downloads/19910021045.pdf
- [S38] Royal Belgian Institute for Space Aeronomy, auroral ovals: https://www.aeronomie.be/en/encyclopedia/auroral-ovals-two-geomagnetic-poles
- [S41] BoM SWS, Global HF: Polar Cap Absorption: https://www.sws.bom.gov.au/HF_Systems/6/3
- [S55] Atmos. Meas. Tech. 13, 3023 (2020), McMurdo–South Pole oblique HF channel: https://amt.copernicus.org/articles/13/3023/2020/
- [S56] Blagoveshchensky & Sergeeva, URSI GA 2011: https://www.ursi.org/proceedings/procGA11/ursi/GP2-5.pdf
- [S57] NOAA D-RAP documentation: https://www.spaceweather.gov/content/global-d-region-absorption-prediction-documentation