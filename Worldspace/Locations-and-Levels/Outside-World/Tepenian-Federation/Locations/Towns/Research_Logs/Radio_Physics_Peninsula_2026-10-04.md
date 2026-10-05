<!-- ⚠ PARTLY SUPERSEDED (2026-10-04): the agent later found that every VOACAP per-band table in this report was shifted by one column. See Section 0 of Research_Logs/Radio_Physics_Followup2_Trunk_Peninsula_to_Casey_2026-10-04.md for the corrected tables. P.533, MUF, ground-wave, geomagnetic, terrain and noise results here are unaffected; any-band hour counts changed little. Do not quote the per-band VOACAP hour counts from this file. -->

<!-- Log written 2026-10-04: the research agent's full report, copied verbatim from the saved tool-result file (not re-typed). Topic: radio propagation physics, standard frequencies and range envelopes for a Peninsula-built comms network (Open_Research_Topics.md section 2). (calc) = the agent's own calculation (VOACAP, ITU-R P.533-14, NTIA LFMF/P.368, GEBCO terrain, AACGM-v2/IGRF-14); (inf) = inference; UNVERIFIED = seen only in a search summary. Many figures come from the agent's models: VOACAP and P.533 disagree in winter (treat P.533 as the conservative bound). Spot-check specific claims before relying on them. -->

# Peninsula Radio Research Report: propagation physics, "standard" frequencies, and range envelopes

All access dates are 2026-10-04. Source numbers [S#] point to the source table at the end.
(calc) marks my own calculation. (inf) marks inference. UNVERIFIED marks facts seen only in a search-engine summary.

Local tools I built or ran, all in the session scratchpad. Nothing was written to the project.
- **VOACAP.** voacapl 16.1207W, compiled from source. CCIR coefficients. [S39]
- **ITU-R P.533-14.** ITURHFProp v14.2 with the P.372-14.3 noise library, compiled from the ITU-R SG3 repository. [S39]
- **Ground wave.** NTIA LFMF, the reference implementation of ITU-R P.368-10, compiled. [S39]
- **Terrain.** GEBCO-2020 elevation profiles via OpenTopoData. The grid is about 450 m, so peaks are smoothed and underestimated. [S39]
- **Geomagnetic coordinates.** AACGM-v2 (aacgmv2 2.7.1) and IGRF-14 (2025.0) dipole coefficients. [S39]

---

## 0. Geometry used for everything below (calculation)

Method: haversine great-circle distance with R = 6371 km, applied to the project coordinates you supplied.

| km | Palmer | P.Abrigo | Rothera | Esperanza | Marambio | Contrapunto | Pergamino | Signy |
|---|---|---|---|---|---|---|---|---|
| **Palmer** | 0 | 27 | 361 | 375 | 361 | 385 | 297 | 1037 |
| **Puerto Abrigo** | 27 | 0 | 370 | 353 | 335 | 371 | 285 | 1013 |
| **Rothera** | 361 | 370 | 0 | 690 | 639 | 739 | 655 | 1319 |
| **Esperanza** | 375 | 353 | 690 | 0 | 94 | 160 | 191 | 663 |
| **Marambio** | 361 | 335 | 639 | 94 | 0 | 249 | 257 | 687 |
| **Contrapunto** | 385 | 371 | 739 | 160 | 249 | 0 | 95 | 718 |
| **Pergamino** | 297 | 285 | 655 | 191 | 257 | 95 | 0 | 807 |
| **Signy** | 1037 | 1013 | 1319 | 663 | 687 | 718 | 807 | 0 |

- **Palmer to Puerto Abrigo is 27.4 km**, not the 30 to 50 km you stated.
- **Distances from the cities to external points:**

| From | To | km |
|---|---|---|
| Palmer | Ushuaia | 1,133 |
| Palmer | Punta Arenas | 1,347 |
| Palmer | Stanley | 1,496 |
| Palmer | Buenos Aires | 3,376 |
| Palmer | McMurdo | 3,798 |
| Palmer | Hobart | 7,737 |
| Contrapunto | Ushuaia | 991 |
| Signy | Ushuaia | 1,488 |
| Signy | Stanley | 1,252 |

- **Terrain and sea fraction per link.** I sampled about 100 points along each great circle from GEBCO-2020. The sea share (elevation ≤ 0, which in winter includes sea ice) runs from 25% to 99%.
  - Marambio to Signy is 99% sea.
  - Palmer to Esperanza is 27% sea, with 41% of samples above 500 m.
  - Rothera to Esperanza is 37% sea, with a 265 km continuous land run.
  - Rothera to Marambio has a 271 km continuous land run.
- **Highest GEBCO cell within 30 km of each city (calc):**

| City | Highest cell (m) |
|---|---|
| Palmer / Puerto Abrigo | 2,382 (Anvers Island massif) |
| Rothera | 1,741 |
| Pergamino | 612 |
| Contrapunto | 569 |
| Esperanza | 572 |
| Signy | 414 |
| Marambio | 233 |

  - The literature gives Mount Français as 2,760 m or 2,825 m (UNVERIFIED, Wikipedia-sourced). GEBCO smooths that to 2,382 m.
- **Daylight at the solstice (calc, geometric, no refraction).** The Antarctic Circle is at 66.56°S.

| Site | Midsummer day length | Midwinter day length |
|---|---|---|
| Palmer | 20.9 h | 3.1 h |
| Esperanza | 20.0 h | 4.0 h |
| Signy | 18.8 h | 5.2 h |
| Contrapunto | 19.4 h | 4.6 h |
| Rothera | 24 h (south of the circle) | 0 h |

  - Palmer, Esperanza, Contrapunto, Pergamino and Signy have no true polar day or night. Only Rothera does.
- **Local time.** Solar time at 64°W is UTC − 4.3 h (calc). All model hours below are UTC.

---

## 1. Propagation physics, band by band

### 1.1 Band-by-band summary

| Band | Mode(s) | What limits range | Realistic ranges (sourced or calc) |
|---|---|---|---|
| **ELF/VLF/LF (<300 kHz)** | Earth–ionosphere waveguide. Ground wave at LF. | Needs huge antennas. Ground conductivity matters at LF. | VLF attenuates about 2–3 dB per Mm, giving global range from megawatt stations [S44, thesis citing Davies 1990]. A claim that attenuation over ice is about 12 dB/Mm higher than over seawater is UNVERIFIED (search snippet). Primary source to read: Barr, Jones & Rodger 2000, and Barr 1987 on the Antarctic icecap [S44 reference list]. Practically a receive-only or time-signal band. A small community cannot field kW-class VLF transmitters (inf). |
| **MF (300 kHz–3 MHz, incl. AM broadcast)** | Ground wave by day. Night E-layer sky wave. | Day: ground conductivity. D-layer absorbs MF sky wave by day, so long-distance MF is practical only at night [S24]. | FM 24-18: ground wave about 24 km at 3 MHz to about 640 km at the bottom of MF; night sky wave up to about 12,870 km [S13]. IPS: HF ground wave about 100 km over land, about 300 km over sea [S14]. My ground-wave computations are in 1.3 (calc). The daytime sky-wave field is about 30 dB lower than at night (Rec. 435 method, NTIA) [S24]. |
| **HF (3–30 MHz)** | Ground wave (short). NVIS. One-hop F2 up to about 4,000 km (3,200 km at 4° takeoff). Multi-hop. E and sporadic-E modes. | D-layer absorption (LUF side). F2 critical frequency (MUF side). Skip zone. Polar-cap absorption, SIDs, storms. | Details in 1.4 to 1.7 and Section 3. |
| **VHF (30–300 MHz)** | Space wave (line of sight). Repeaters. Ducting and sporadic E are rare. | Radio horizon, terrain shadowing. | LOS = 4.12(√h1 + √h2) km with k = 4/3 [S11] (calc). Power is not the limit: 5 W at 156.8 MHz has a free-space range of over 3,000 km to −110 dBm (calc), so geometry dominates. |
| **UHF and above, satellite** | Line of sight. | Horizon. Rain and ice loading at microwave. | See 1.9. |

### 1.2 Ionospheric basics (D, E, F layers, LUF/MUF, skip, absorption)

All of this section is from the BoM Space Weather Services manual [S14].
- **Layer heights.** D 50–90 km, E 90–140 km, F1 140–210 km, F2 over 210 km. At night D, E and F1 become insignificant. F2 persists but decays. F2 is "the most important region for HF sky wave".
- **The D layer absorbs HF as it passes through, and absorption is greater at lower frequencies.** Paths wholly within the night hemisphere "may be able to use the lowest frequencies in the HF band".
- **Maximum hop length at 0° takeoff.** 2,000 km via E and 4,000 km via F, for heights of 100 km and 300 km. At 4° takeoff they fall to 1,800 km (E) and 3,200 km (F).
- **Absorption.** D-region absorption is greatest at solar maximum and near the sub-solar region. It is normally greatest in summer, but can be anomalously high in winter for days.
- **Seasonal anomaly.** At solar maximum, winter F2 frequencies tend to be higher than summer.
- **Mid-latitude trough.** Midnight critical frequencies are lowest around 60° from the geomagnetic equator.
- **Polar ionosphere.** It is "quite variable" because of solar-wind input.
- **Sporadic E.** At high latitudes it tends to form at night and with a disturbed ionosphere.

### 1.3 Ground wave over sea, sea ice, snow, ice sheet and rock

- **Conductivity standards (ITU-R P.832-4 Table 1).** Sea water is 5 S/m (limits 3 to 7). The scale then steps by about half-decades down to 1×10⁻⁵ S/m. The Atlas has MF maps standardized to 1 MHz and no Antarctic map (grep of the text found no Antarctic or polar entry) [S9].
- **Ice and snow.**
  - Evans (J. Glaciol. 1965) gives direct-current conductivities for pure ice and snow from about 10⁻⁹ to 10⁻⁷ S/m for clean cold material. Impure "city snow" is about 3×10⁻⁵ to 3×10⁻⁶ S/m [S25]. The scanned table is partly garbled, so treat the exact values with care.
  - The permafrost value used in the Livingston Island antenna study is σ = 5×10⁻⁵ S/m, εr = 3. It costs up to 5.5 dB of gain against ideal ground [S21].
  - The 4nec2 "polar ice cap" (1×10⁻⁴) and "polar ice" (3×10⁻⁴) values are from a hobbyist tool with no primary citation [S40].
- **Sea ice.** Physics: sea ice is a thin dielectric layer on conductive water, modeled as a two-layer surface impedance (Hill & Wait 1981), and the influence is "significantly less pronounced" at MF [S26]. A figure of 0.017 S/m for the horizontal conductivity of Antarctic sea ice is UNVERIFIED (search snippet).
- **Army arctic guidance.** "The conductivity of frozen ground is often too low to provide good ground wave propagation. To improve ground wave operation, use a counterpoise… install it high enough above the ground so that it will not be covered by snow." [S13]
- **Livingston Island, 7.5 m monopole.** The authors modeled it over permafrost: poor ground raises the maximum-radiation angle to 20–30°, and 32 radials of 15 m give about 2 dB of improvement [S21].

**Ground-wave computation (calc).** I used NTIA LFMF (P.368-10), a short vertical monopole radiating the stated power, antenna heights of 3–10 m, and a homogeneous smooth Earth. Heights are the only terminal parameters in the model, and it ignores terrain.
- **How to read the tables.** The first table gives the field strength at each link distance. The second gives the distance to a threshold.
- **Threshold values.** For AM, the ITU planning sensitivity for MF is 60 dBµV/m, with 54 and 40 also supported [S12]. The FCC protected contour is 0.5 mV/m, which is 54 dBµV/m (UNVERIFIED, search snippet).
- **Homogeneous-ground upper bounds on a mixed sea/ice/rock path (calc).** Real Peninsula paths are mixed, so the true value lies between the sea row and the ice or rock row.

Field strength in dBµV/m at link distance:

| Case | Ground | 27 km | 94 km | 160 km | 297 km | 361 km | 385 km | 690 km | 739 km | 1037 km |
|---|---|---|---|---|---|---|---|---|---|---|
| AM 0.9 MHz, 1 kW | sea | 81 | 69 | 63 | 55 | 52 | 51 | 37 | 35 | 22 |
| | rock 2e-3 | 61 | 37 | 26 | 9 | 3 | 1 | -27 | -32 | -58 |
| | polar ice 3e-4 | 44 | 20 | 9 | -7 | -14 | -16 | -45 | -50 | -77 |
| | cold ice 5e-5 | 40 | 16 | 5 | -11 | -18 | -20 | -49 | -54 | -81 |
| AM 0.9 MHz, 10 kW | sea | 91 | 79 | 73 | 65 | 62 | 61 | 47 | 45 | 32 |
| | polar ice 3e-4 | 54 | 30 | 19 | 3 | -4 | -6 | -35 | -40 | -67 |
| AM 0.9 MHz, 50 kW | sea | 98 | 86 | 80 | 72 | 69 | 68 | 54 | 52 | 39 |
| | polar ice 3e-4 | 61 | 37 | 26 | 10 | 3 | 1 | -28 | -33 | -60 |
| 3.5 MHz, 100 W | sea | 70 | 58 | 51 | 40 | 35 | 34 | 13 | 10 | -9 |
| | rock 2e-3 | 29 | 5 | -9 | -31 | -40 | -44 | -88 | -95 | -137 |
| | polar ice 3e-4 | 18 | -7 | -20 | -43 | -52 | -56 | -100 | -107 | -150 |

Distance to reach a threshold at 1.0 MHz (km):

| Power | Ground | to 60 dBµV/m | to 54 | to 40 | to 20 |
|---|---|---|---|---|---|
| 1 kW | sea | 209 | 314 | 600 | 1050 |
| 1 kW | rock | 25 | 35 | 72 | 185 |
| 1 kW | polar ice | 9 | 13 | 30 | 87 |
| 10 kW | sea | 391 | 515 | 822 | 1284 |
| 10 kW | polar ice | 17 | 24 | 52 | 141 |
| 50 kW | sea | 536 | 665 | 981 | 1450 |
| 50 kW | rock | 62 | 84 | 163 | 335 |
| 50 kW | polar ice | 25 | 35 | 75 | 190 |

- **HF ground wave, 100 W radiated.** Range to 10 dBµV/m (a plausible voice-quality level):

| Frequency | Sea | Rock | Polar ice |
|---|---|---|---|
| 3.5 MHz | 736 km | 71 km | 36 km |
| 7.1 MHz | 546 km (computed at 7.0) | 46 km | 26 km |

- **Noise-limited reference level (calc, P.372 eq. 7).** En = Fa + 20 log f + B − 95.5. For quiet-rural man-made noise combined with galactic noise at 3.5 MHz and B = 3 kHz, En is about −8 dBµV/m. A 10 dB S/N therefore needs about +2 dBµV/m, so field strength is not the limit over water. Ice and rock are.
- **Caveat on the 20 dB mismatch between runs.** The original GRWAVE code in the same repository gave a roughly 20 dB step between its flat-earth and residue regions at 3 m antenna heights. I rejected it in favor of NTIA LFMF. The LFMF value at 105 km, 1 MHz, 1 kW over sea (68 dBµV/m) agrees with a hand estimate of about 300 mV/m·km divided by distance (calc).

### 1.4 NVIS (near-vertical incidence skywave)

- **Principle.** The wave must be radiated at angles above about 75–80° from horizontal, on a frequency low enough to be reflected at zenith. There is then no skip zone. Path loss is "nearly constant at about 110 dB ±10 dB", and terrain shadowing is "greatly reduced". [S13, Appendix M]
- **Military reach.** The AS-2259 NVIS antenna is specified for 0–483 km (0–300 mi). Without NVIS, the standard HF skip zone is at least 80–113 km. [S13]
- **Antenna geometry.** Half-wave dipoles one-quarter to one-tenth wavelength above ground direct energy vertically. [S13]
- **Working frequency.** Use about 0.85 × foF2. [S21]
- **Livingston Island authors.** They say NVIS gives "approximately 200–250 km radius" coverage with tens of watts. That is a design claim. I checked the raw text: their NVIS tests were run in Spain (Barcelona to Cambrils, 96 km, 4.5 MHz), not in Antarctica. [S21]
- **Inverted-V over permafrost.** An inverted-V needs a 13 m mast and gives only 1.3 dBi over permafrost, against 6.8 dBi over ideal ground. [S21]
- **Model output for the Peninsula (calc).** NVIS-length paths of 94 to 385 km with 100 W isotropic antennas, quiet-rural noise and a 10 dB S/N in 3 kHz. P.533-14 results:
  - January, SSN 100 (basic MUF 7.4–8.4 MHz): every hour has all of 1.8 to 7.1 MHz usable.
  - January, SSN 5 (basic MUF 5.5–6.7 MHz): 1.8 to 6 MHz usable.
  - July, SSN 5 (Palmer to Rothera): basic MUF 2.5–3.1 MHz from 01 to 12 UTC and 4.2–4.8 MHz from 14 to 18 UTC. Usable bands are 1.8–2.5 MHz at night and morning, widening to 3–5 MHz in the afternoon.
  - July, SSN 100: MUF 2.7–3.4 MHz overnight, rising to 7.1 MHz at 17–18 UTC. Usable 1.8–2.5 MHz overnight, 4–7.1 MHz at 17–18 UTC.
  - Esperanza to Marambio (94 km) gives nearly identical numbers.
- **VOACAP agrees on the MUF structure.** For Palmer to Rothera in January, MUF was 6.4/5.5/5.9 MHz (04/12/20 UTC) at SSN 5 and 8.7/8.1/8.3 MHz at SSN 160.
- **The measured Vernadsky ionosphere agrees roughly.**
  - Vernadsky is on the Argentine Islands, 54 km from Palmer.
  - Near the winter solstice at solar minimum (28–29 June 2019, F10.7 about 70), peak electron density NmF2 "generally do[es] not exceed 2×10⁵ cm⁻³" and the station is sunlit under 4 h per day [S23].
  - foF2 = 8.98 × √N Hz, so 2×10⁵ cm⁻³ is 2×10¹¹ m⁻³, giving about 4.0 MHz (calc).
  - Night values are lower. A factor-of-about-2 night enhancement is attributed to plasmaspheric flux [S23].
- **Weddell Sea Anomaly.** In summer, electron density at Vernadsky peaks at night rather than by day (WSA region 55–75°S, 80–30°W) [S22]. This favors higher NVIS frequencies after dusk in summer (inf).

### 1.5 Line of sight, repeaters, shadowing

- **Radio horizon.** d = √(2kRh) = 4.12√h km with k = 4/3 [S11] (calc).

| Antenna heights | LOS |
|---|---|
| 10 m / 10 m | 26 km |
| 30 m / 10 m | 36 km |
| 100 m / 10 m | 54 km |
| 300 m / 10 m | 84 km |
| 1,000 m / 10 m | 143 km |
| 1,000 m / 1,000 m | 261 km |
| 2,000 m / 2,000 m | 369 km |
| 2,382 m / 2,382 m | 402 km |

- **Ducting threshold.** ITU-R P.834-9: ducting needs a refractivity gradient below −157 N/km [S11].
- **Link budget (calc).** At 156.8 MHz, free-space loss is 110.3 dB at 50 km, 116.4 dB at 100 km and 122.4 dB at 200 km. A 5 W handheld has 147 dB of allowable loss to a −110 dBm receiver, so it is geometry-limited, not power-limited.
- **Real repeater practice.**
  - The Australian Antarctic Division: "Solar and wind-powered VHF repeaters located on mountain tops, extend the coverage around the main station areas." [S27]
  - McMurdo uses repeaters on Mounts Taylor, Wright, Terror, Aurora and Brooke, all with input 138.600 and output 143.225 MHz [S2].
  - Palmer: "VHF radios require a line of site around the Palmer Station boating area. There are repeaters around station to extend the VHF range." Channel 27 (157.350/161.950 MHz) is the radio watch, and channel 25 (156.250/161.850) is the relay [S3].
  - The Palmer repeater is on the tower behind the station, and the handheld "must be in line of sight with the tower" [S2, 2001–02 edition].
  - UNVERIFIED: a Casey repeater on channel 21 at "the highest vantage point" (search snippet).
  - Not found: any BAS or Frei repeater technical data.
- **My terrain analysis (calc, GEBCO).** With 10 m masts, every one of the 28 pairs is blocked. The smallest equal mast height needed at both ends is shown here, as a small subset.

| Pair | Equal mast AGL needed | Clearance with ends on summits ≤30 km away |
|---|---|---|
| Palmer–Puerto Abrigo | 410 m | clear (+43 m, 10 km peaks) |
| Palmer–Rothera | 1,910 m | clear (+142 m) |
| Palmer–Pergamino | 1,590 m | clear (+62 m) |
| Contrapunto–Pergamino | 580 m | clear (+40 m) |
| Esperanza–Marambio | 660 m | blocked (−207 m) |
| Esperanza–Contrapunto | 610 m | blocked (−92 m) |
| Palmer–Esperanza, Palmer–Marambio, anything with Rothera except Palmer | more than 3,000 m | blocked |
| Anything to Signy | more than 3,000 m | blocked |

  - Summits are the highest GEBCO cell within 30 km, assumed to be on the path axis, which is an inference. The 100-sample spacing (0.3 to 13 km) can miss narrow ridges.
  - So VHF is a local and intra-island tool. Inter-island links need mountain-top repeaters, and Signy at about 660 to 1,320 km is out of reach for any VHF terrestrial link.

### 1.6 HF skywave over long paths; the solar cycle

**Solar cycle numbers (NOAA SWPC JSON, retrieved 2026-10-04) [S17].**
- Cycle 25 maximum smoothed SSN was **160.9 in October 2024**.
- The last minimum was 1.8 (December 2019).
- The all-time smoothed maximum in the data is 285 (March 1958).
- The monthly SSN for September 2026 is 60.3. The last smoothed value in the file is 94.5 for March 2026.
- NOAA predicts 87.9 for October 2026 (band 72.9 to 97.2), then 65.9 (2027), 38.7 (2028), 20.2 (2029) and 9.3 (2030).

**Solar-cycle effect (calc).** I ran VOACAP and P.533 at SSN 5, 100 and 160, for January and July. At 100 W with isotropic antennas, voice needs a 45 dB-Hz S/N in VOACAP (10 dB in 3 kHz); P.533 used 10 dB in 3 kHz.
- **Bands for a 361 km link (Palmer to Rothera).** SSN 5 limits the upper band to about 7 MHz in January and 2.5–5 MHz in July. SSN 160 pushes it to 10 MHz in January.
- **For 1,037 km (Palmer to Signy).** In January, usable bands go up to 14 MHz (all 24 h) in VOACAP. In P.533 at SSN 100 the upper limit is 10 MHz.
- **Frequencies above 14 MHz.** At 100 W isotropic they appear only on paths of 3,000 km or more, and at solar maximum.

**Per-band usable hours per day, VOACAP, 100 W isotropic, voice, REL ≥ 0.8 and frequency at or below the median MUF (calc).** UTC hours; bands are 2.5, 3.5, 5.0, 7.1, 10.1, 14.2 MHz. Quiet-rural noise.

| Link, month, SSN | 2.5 | 3.5 | 5 | 7.1 | 10.1 | 14.2 |
|---|---|---|---|---|---|---|
| Palmer–Rothera Jan 5 | 24 | 24 | 24 | 23 | 0 | 0 |
| Palmer–Rothera Jan 160 | 19 | 13 | 16 | 24 | 24 | 0 |
| Palmer–Rothera Jul 5 | 24 | 24 | 8 | 0 | 0 | 0 |
| Palmer–Rothera Jul 160 | 24 | 24 | 12 | 9 | 4 | 0 |
| Rothera–Esperanza Jan 100 | 14 | 10 | 13 | 16 | 24 | 0 |
| Palmer–Signy Jan 5 | 11 | 9 | 13 | 17 | 24 | 4 |
| Palmer–Signy Jan 100 | 8 | 7 | 10 | 14 | 17 | 24 |
| Palmer–Signy Jul 5 | 12 | 24 | 24 | 12 | 6 | 0 |
| Palmer–Ushuaia Jan 100 | 1 | 3 | 8 | 11 | 12 | 20 |
| Palmer–Ushuaia Jul 5 | 13 | 19 | 24 | 17 | 8 | 0 |

- **Higher noise.** Rural noise, −150 dBW/Hz at 3 MHz, reduces availability and removes the lowest bands:
  - Palmer to Signy in January at SSN 100 drops from 24 h to 12 h.
  - Rothera to Signy in January at SSN 100 drops to 0 h.
  - Palmer to Ushuaia in January at SSN 100 drops to 6 h.
- **Power and antenna sensitivity, VOACAP, rural noise, voice, January, SSN 100 (hours/day with any usable band).**

| Link | 10 W 0 dBi | 100 W 0 dBi | 1 kW 0 dBi | 100 W +6 dBi each end | 1 kW +6 dBi each end |
|---|---|---|---|---|---|
| Palmer–Signy | 0 | 12 | 24 | 24 | 24 |
| Rothera–Signy | 0 | 0 | 24 | 24 | 24 |
| Palmer–Ushuaia | 0 | 6 | 24 | 24 | 24 |
| Palmer–Punta Arenas | 0 | 2 | 21 | 24 | 24 |
| Palmer–Buenos Aires | 0 | 0 | 22 | 24 | 24 |
| Palmer–McMurdo | 0 | 0 | 0 | 0 | 24 |

  - So a 3 to 6 dBi directive antenna is worth roughly an order of magnitude in power, and 10 W isotropic is not enough for any inter-island link beyond about 400 km.
- **A published long-path measurement (not a model).**
  - Spanish station Juan Carlos I, Livingston Island, to Ebro Observatory, Spain (calc distance 12,710 km, minimum 4 hops). 250 W into a 7.5 m monopole.
  - Over the 2006/07 austral summer, availability exceeded 95% at 8–10 MHz between 21 and 04 UTC, exceeded 95% at 11–12 MHz between 07 and 08 UTC, exceeded 95% at 14–15 MHz between 08 and 09 UTC, and scarcely reached 20% at any frequency between 10 and 19 UTC.
  - Typical receiver SNR was −5 dB in 3 kHz. Free-space loss at 10 MHz is 135 dB. [S20]
  - VOACAP reproduces the timing: MUF was 8.1–9.0 MHz at 05–06 UTC and above 20 MHz at 10–19 UTC (SSN 10 and 20, 250 W). Availability was low at 10–19 UTC because that range lies above the 16.5 MHz top of the sounding band (calc).
- **Antarctic-wide HF experience.** USAP: HF best at the sun's greater zenith angle; "begin[s] to deteriorate mid-to-late evening… weakest during early morning hours" at McMurdo. HF "begin[s] to deteriorate" and "less variance in the angle of the sun… nearer the Poles" [S2].

### 1.7 High-latitude effects: auroral oval, polar cap, PCA, SIDs, storms; geomagnetic latitude

**The Peninsula is in the sub-auroral, mid-latitude zone, not the polar cap.**

| Site | AACGM-v2 latitude at 110 km, 2025.5 (calc) | Dipole geomagnetic latitude, IGRF-14 2025.0 (calc) |
|---|---|---|
| Palmer | −51.4° | −55.6° |
| Rothera | −53.8° | −58.4° |
| Esperanza | −50.6° | −54.5° |
| Marambio | −51.4° | n/a |
| Contrapunto | −49.5° | −53.2° |
| Pergamino | −49.7° | n/a |
| Signy | −49.7° | −52.3° |
| Ushuaia | −42.2° | −45.6° |
| McMurdo | −80.0° | −79.2° |
| Casey | −80.5° | −75.5° |
| Davis | −75.1° | −75.9° |
| Mawson | −70.9° | −73.0° |
| Halley | −62.9° | −68.2° |
| South Pole | −74.7° | −80.8° |

- **Why.** The dipole axis comes out at **80.8°N 72.8°W** (north geomagnetic pole) and **80.8°S 107.2°E** (south geomagnetic pole) (calc, IGRF-14 2025.0 g10 = −29350, g11 = −1410.3, h11 = 4545.5). The south geomagnetic pole lies off the Wilkes Land coast, so East Antarctica is at high geomagnetic latitude and the Peninsula, on the opposite side, is about 25° nearer the equator.
- **Auroral oval (reference values).**
  - The oval's equatorward edge descends to about 65–75° geomagnetic latitude depending on activity [S38].
  - NOAA geomagnetic storm scale, with aurora seen "as low as… typically N° geomagnetic lat": G2 about 55° (600 per cycle), G3 about 50° (200 per cycle, 130 days), G4 about 45° (100 per cycle), G5 about 40° (4 per cycle). HF effects are "fade at higher latitudes" (G1–G2), "intermittent" (G3), "sporadic" (G4) and "may be impossible in many areas for one to two days" (G5) [S15].
  - Combining the table with the 50° geomagnetic latitudes above: the oval overhead happens at about G3 (Kp 7) or stronger (inf).
- **Polar cap absorption (PCA).** Protons "ionise the polar D region", producing an HF blackout "for trans polar circuits" that "can last several days" [S14, S41]. Even the winter dark pole is affected. The riometer that BoM uses to gauge PCA severity is at Casey, at about −80° AACGM [S41, calc]. The NOAA scales list S1 to S5 radiation storms: 50, 25, 10, 3 and under 1 per cycle, with polar-region HF effects ranging from "minor" to "complete blackout" [S15]. The PCA cutoff boundary sits equatorward of 60–66° magnetic latitude for typical events (UNVERIFIED, search snippets). So the Peninsula at −50° is on the fringe of all but the biggest events (inf).
- **Solar flares (SID).** NOAA R1 to R5 radio blackouts occur 2000, 350, 175, 8 and under 1 per cycle respectively, on the sunlit side only [S15].
- **WWV broadcasts geophysical alerts** [S18]. A settled community could rely on that for space-weather warnings.
- **April 2023 storm at Vernadsky.** Ukrainian measurements showed HF signals unexpectedly scattered on the polar ovals and returning by long-arc paths (UNVERIFIED, search snippet of Zalizovski et al., Ukr. Antarct. J. 2023) [S47].
- **Antarctic Peninsula ionosondes and published papers.** Vernadsky/Argentine Islands has data from 1960 to 2023 (ANGEO 2025) [S22]. Port Stanley and Halley Bay also carry long records. The first WSA detection was at Halley in 1958 [S22]. I did not find BAS, Argentine or Chilean HF-propagation measurements specific to the Peninsula beyond the Spanish Livingston Island work [S20, S21].

### 1.8 Noise

- **ITU-R P.372-13 equation (13): Fam = c − d log f.** Constants (c, d): city 76.8, 27.7; residential 72.5, 27.7; rural 67.2, 27.7; quiet rural 53.6, 28.6; galactic 52.0, 23.0 [S8]. At 3 MHz these give quiet rural −164 dBW/Hz and rural −150 dBW/Hz (calc: 53.6 − 28.6 log 3 − 204 and 67.2 − 27.7 log 3 − 204).
- **Galactic noise** is not observed below foF2 and is lower than the formula up to about 3 foF2 [S8].
- **Lightning noise.** I looked at the P.372 atmospheric-noise world maps, rendered from the PDF. In the one I viewed (summer, 0000–0400 LT, 1 MHz) the contour labels in the southern polar region read as low as about 25 dB. That is a visual reading, not a number extracted for 64°W, and it is UNVERIFIED for the Peninsula. The principle is documented: lightning occurs far less near the poles, so atmospheric noise there is low, and man-made noise from the settlement's own equipment becomes the limit (inf).
- **My use in the models.** I tested quiet rural (−164) and rural (−150). The difference moves usable hours materially (see 1.6), so noise discipline at the receiver (distance from generators, shielded power) is a primary design lever.

### 1.9 Wind, ice loading, satellite baseline

- **Antennas on ice.** The 1965 CRREL report on icing and snow accretion on wires is the generic reference (UNVERIFIED beyond the title) [S42]. Whips and thin leading edges ice first, and wind often damages iced wires more than the static ice does. No Peninsula-specific antenna-icing data were found.
- **Geostationary visibility (calc).** Best case (sub-satellite point at the station's longitude): Palmer 16.9°, Rothera 14.0°, Esperanza 18.3°, Signy 21.2°, Contrapunto 19.6°. The visibility limit is 81.3°. For a satellite at 75°W, Palmer sees 16.4° and Rothera 13.8°. NASA (1991): "visible to latitudes as high as 81°, they appear on the local horizon and are easily masked" [S34]. INMARSAT at McMurdo was typically under 7° [S34].
- **Iridium and Starlink.** USAP Peninsula camps carry HF plus at least two Iridium phones "that do not depend only on satellite" [S3]. Starlink serves McMurdo since 14 Sept 2022 (UNVERIFIED, search summary), using polar shells at 97.6° inclination (UNVERIFIED). I did not find Peninsula-specific Starlink coverage data.
- **Palmer HF antennas:** a sloping "V" and a conical monopole, 2–30 MHz (UNVERIFIED, search snippet).
- **Meteor burst.** 40–50 MHz, optimum about 1,000 km, maximum 2,000 km, low data rate (UNVERIFIED, search summary, NTIA 89-241). Not Antarctic-specific.

---

## 2. "Standard" frequencies

### 2.1 The real international framework

**Regions.** ITU Region 2 is bounded on the east by Line B (meridian 20°W to the South Pole) and on the west by Line C (120°W to the pole) [S7, Nos. 5.4, 5.8, 5.9]. The whole Peninsula and Signy (45.6°W) are in Region 2.

**Distress and safety (RR 2024 Appendix 15 and footnotes) [S6, S7].**

| Frequency | Use |
|---|---|
| 2 182 kHz | Radiotelephony, "international distress and calling frequency for radiotelephony" (RR 5.108) |
| 4 125, 6 215, 8 291, 12 290, 16 420 kHz | Radiotelephony distress and safety traffic. 4 125 may be used by aircraft with maritime stations. |
| 2 187.5, 4 207.5, 6 312, 8 414.5, 12 577, 16 804.5 kHz | Digital selective calling |
| 3 023, 5 680 kHz | Aeronautical SAR carriers |
| 518 kHz | NAVTEX |
| 490 kHz | MSI |
| **500 kHz** | **Now NAVDAT, no longer distress** (WRC-23) |
| 121.5 MHz | Aeronautical emergency |
| 123.1 MHz | SAR auxiliary |
| 156.8 MHz (ch. 16) | Distress, safety and calling; may be used by aircraft |
| 156.525 MHz (ch. 70) | DSC |
| 156.3 MHz (ch. 06) | Ship–aircraft SAR |
| 161.975 and 162.025 MHz | AIS-SART |
| 406–406.1 MHz | EPIRB |
| **243 MHz** | **Not in Appendix 15.** It appears in RR 5.256: "the frequency in this band for use by survival craft stations" |

**Time and frequency signals (RR Article 5) [S7].** Allocations are 2 495–2 505, 4 995–5 005, 9 995–10 005, 14 990–15 010, 19 990–20 010 and 24 990–25 010 kHz, plus 19.95–20.05 kHz. WWV (Fort Collins) radiates 10 kW on 5, 10 and 15 MHz and 2.5 kW on 2.5 and 20 MHz, with a 2.5 kW experimental 25 MHz transmission, and broadcasts "geophysical alerts" [S18]. The USAP manual notes signals are "sometimes weak in the mornings" and lists BBC pips in 9.0–9.8, 11.6–12.1 and 15.0–15.5 MHz [S2, 2001–02 text; NBS-era wording].

**Broadcasting bands in Region 2 (RR 2024 table) [S7].**

| Band | Allocation |
|---|---|
| MF AM | 525–1 705 kHz (525–535 limited to 1 kW day and 250 W night; 1 605–1 705 governed by the Rio 1988 plan) |
| FM | 88–108 MHz in Region 2 (Region 1: 87.5–108) |
| 120 m | 2 300–2 495 kHz (tropical-zone footnotes) |
| 90 m | 3 200–3 400 kHz |
| 60 m | 4 750–4 995 and 5 005–5 060 kHz |
| 49 m | 5 900–6 200 kHz |
| 41 m | 7 300–7 400 kHz in Region 2 (7 200–7 300 is the amateur band in Region 2; 7 200–7 450 is broadcasting in Regions 1 and 3) |
| 31 m | 9 400–9 900 kHz |
| 25 m | 11 600–12 100 kHz |
| 22 m | 13 570–13 870 kHz |
| 19 m | 15 100–15 800 kHz |
| 16 m | 17 480–17 900 kHz |
| 15 m | 18 900–19 020 kHz |
| 13 m | 21 450–21 850 kHz |
| 11 m | 25 670–26 100 kHz |

- Footnote 5.134 restricts the use of 5 900–5 950, 7 300–7 350, 9 400–9 500, 11 600–11 650, 13 570–13 600, 13 800–13 870 and others to digital emissions or conditions.
- The 3 900–4 000 kHz band is broadcasting in Regions 1 and 3 but not in Region 2 [S7].

**Why these bands became de facto standards (physics and history).** This is my synthesis, with the physical parts supported by [S13, S14, S24].
- MF: ground wave by day, night sky wave. Large antennas but cheap. That is why AM broadcasting sits there.
- 2–8 MHz: NVIS and short-range skywave. That is why the outback and distress allocations cluster there (RFDS below).
- 14 MHz and above: day and long-range. That is why amateur DX and long-distance broadcasting sit there.
- VHF marine and aviation: line of sight, small antennas, and good local reuse.
- 121.5 and 243 MHz are legacy VHF/UHF emergency bands.

### 2.2 Frequencies actually used in or near the Peninsula and Antarctica

**US (Palmer).**
- **HF field parties:** 4125 kHz secondary and 11553 kHz primary [S2, 2001–02 edition; also a RadioReference wiki mirror UNVERIFIED]. The primary daily check-in was 4125 kHz [S2]. The 2026 manual says the HF radios (Barrett 2090) use a "Palmer Station individual frequency" and lists no kHz values [S3].
- **VHF at Palmer:** ch. 16 156.8 MHz is the standard hailing channel and is used to hail R/V Laurence M. Gould [S2]. Ch. 27 157.350/161.950 MHz is "Palmer Station Radio Watch". Ch. 25 156.250/161.850 is the "Channel 27 Relay" [S3].
- **The check-in procedure.** Camps check in once per day. If the party misses it, it calls hourly. If six hours pass, the POC notifies Denver. If 20 minutes pass after a boat check-in time, Palmer mobilizes the OSAR team [S3].
- **McMurdo air-ground HF** (an Antarctic-wide reference, not Peninsula): 4770, 5100, 5400, 7995, 9032 and 11553 kHz [S2]. The 2026 Air Operations Manual gives primary HF 9.032 (typo for 9032 kHz), with secondary and tertiary 5726, 13251, 11256 and 6708 kHz [S1]. VHF: Mac Radio 118.5 MHz, Williams Field Tower 126.2, area common 122.8, maintenance 123.45 [S1]. The manual's "kHz" values like "5.371 kHz" are typos for 5371 kHz.
- **123.45 MHz air-to-air** is stated in ICAO Annex 10 (UNVERIFIED, search snippet).

**British (Rothera).**
- Marine VHF handhelds on channel 1, 156.000 MHz, are normal (UNVERIFIED, search snippet).
- Rothera airfield HF: 5080, 7775 and 9106 kHz USB, VHF 118.1 MHz (UNVERIFIED, search summary, no source found despite two additional searches).

**Other national programs.**
- **Australia (AAD, 2012 list [S28]).** Frequencies 2720, 3023, 3175, 3418, 4040, 4540, 4678 and **5400 (primary)** kHz, with aircraft on 5726, 9032 and 11256 kHz USB.
- **Argentina and Chile.** Marambio's internal communications are "mainly through HF, Vox/Data, aeronautic VHF-AM and UHF-FM" (Wikipedia lead only) [S33].
- **The 2001 US inspection report** [S5] describes the Peninsula stations of the time:
  - Juan Carlos I: VHF radiotelephones for short to medium range, HF and radiotelephone for medium to long range, INMARSAT.
  - Frei (the King George Island hub): tower "equipped with HF, VHF, and UHF radios monitored 24 hours a day", with weather updates passed to the area stations by HF teletype several times daily.
  - Artigas monitored VHF channel 16 for emergencies.
  - Vernadsky had two HF transmitters, a VHF radio and INMARSAT.
- **IAATO.** Suggested HF hailing frequencies 4146, 6224 and 8294 kHz, a daily radio schedule at 0730 and ship reports at 1230 and 1930 Ushuaia time (UNVERIFIED, all from one search summary of the IAATO manual; I could not open the primary). The IAATO yacht checklist (verified) requires long-range communications by satellite and/or HF/SSB and a marine VHF radio [S43].
- **COMNAP AFIM.** The public edition I retrieved is the procedures document only (Version 15 July 2021) and contains no frequency tables [S4]. Frequency tables sit in the subscriber editions. This is a documented dead end.

**Broadcasters on the Peninsula (real examples of what a small station achieves).**
- **LRA36 Radio Nacional Arcángel San Gabriel, Esperanza Base.** On the air since 20 October 1979. Shortwave 15 476 kHz (19 m) plus FM 96.7 MHz. Power is disputed (see Section 5). A 1999 Ontario DXer needed numerous attempts to hear a clear ID, and called it "usually not audible at all or too buried under the noise level" (Coe Hill, Ontario, 12,175 km, calc) [S31]. A 2019 listener says it is "incredibly difficult to hear in North America" [S30].
- **Radio Soberanía, Villa Las Estrellas, King George Island.** 90.5 MHz, 100 W, covering "Chilean Antarctic bases and nearby bases in the South Shetland Islands" (UNVERIFIED, Spanish Wikipedia summary) [S32/S33].
- **FM 96.7 MHz at Esperanza** is stated at 500 W [S32].

### 2.3 Why people converge on a frequency (real examples)

- **Channel 16** is codified internationally [S6] and works as a hail-and-switch channel. The IAATO text says "Channel 16 is used for hailing purposes only" (UNVERIFIED, search summary) [S43].
- **CB channel 9** is codified by the FCC: "CBRS Channel 9 may be used only for emergency communications or traveler assistance" [S37]. **Channel 19** is not mentioned in that rule, so its status as the trucker channel is custom, not regulation (inf).
- **Amateur calling and emergency "centers of activity" (IARU Region 2 band plan, 2016 [S19]).**
  - 3750 kHz and 3985 kHz emergency centers of activity.
  - 7060, 7240 and 7275 kHz Region 2 emergency centers.
  - **14 300 kHz global emergency center of activity.**
  - 18 160 and 21 360 kHz global emergency centers.
  - 14 285 kHz AM calling, 29 600 kHz FM calling.
  - 144.200 MHz weak-signal calling, 146.520 MHz FM calling.
- **The 14.300 MHz maritime net.** MMSN started 3 January 1968 on 14.320 MHz, moved to 14.317 and then 14.313, and has settled on 14.300 MHz (UNVERIFIED, from a search summary; mmsn.org returned 403).
- **Royal Flying Doctor Service (RFDS) (2013 list [S29]).**
  - Bases use 2020–8165 kHz, for example Derby 5300 kHz primary, Meekatharra 4010, Port Hedland 4030, Charleville 2020/4980/6845/6965/7465.
  - Shared "VKS-737" channels 3995, 5455, 6796, 8022, 10180, 11612 and 14977 kHz.
  - Users run USB with "outpost bases operate at 1 kW" and a maximum of 100 W for users.
  - Takeaway: a continent-scale community with no common regulator-free alternative used 2–8 MHz as the working band and a handful of shared channels (inf).
- **Antarctic examples.**
  - McMurdo amateurs use mostly FT8 on 14.075 MHz, a tribander for 20/15/10 m and a 40 m dipole planned; the Concordia and Halley operators planned FT8, JT65 and SSB on 40 and 20 m. Operating times were 0000 UTC for about 30 minutes and 0600 UTC [S35].
  - A South Pole operator on 14243 or 7243 kHz is UNVERIFIED (search summary).
- **What makes a natural calling frequency (inf, supported by the physics above).**
  - It must propagate for most hours.
  - Antennas must be buildable.
  - A common band edge (the 2182 kHz and 156.8 MHz style anchors) helps.
  - A network effect needs only that most radios cover it.
  - Quiet noise matters in the Peninsula (1.8–8 MHz for regional, 14 MHz class for long range).

### 2.4 Practical equipment (calc)

- **Dipole lengths.** Half-wave in free space = 149.9/f(MHz) meters; the practical dipole is about 5% shorter (142.4/f). The quarter-wave monopole is half that.

| Frequency | Half-wave dipole | Quarter-wave monopole |
|---|---|---|
| 1.0 MHz | 142 m | 71 m |
| 2.5 MHz | 57 m | 28 m |
| 3.5 MHz | 40.7 m | 20.3 m |
| 5.3 MHz | 26.9 m | 13.4 m |
| 7.1 MHz | 20.1 m | 10.0 m |
| 10.1 MHz | 14.1 m | 7.1 m |
| 14.2 MHz | 10.0 m | 5.0 m |
| 28.5 MHz | 5.0 m | 2.5 m |
| 121.5 MHz | 1.17 m | 0.59 m |
| 156.8 MHz | 0.91 m | 0.45 m |
| 406 MHz | 0.35 m | 0.18 m |

- **Power reference points.**
  - Livingston Island ran 250 W (long range) and under 10 W (NVIS sensors). The NVIS transmitter drew 7.2 W asleep and 96 W transmitting, and a 110 Ah battery supported about two weeks at hourly transmissions [S21].
  - RFDS users run at most 100 W.
  - The Spanish 250 W monopole system reached 12,710 km [S20].
- **Antenna practice on ice.** Elevated counterpoise [S13]. A 7.5 m monopole with radials or a 13 m inverted-V was used at Livingston [S21].
- **Digital modes.** The Livingston system reached 150 bit/s DS-SS with over 90% packet success on the 12,700 km path [S20] and 2.3–4.6 kbit/s on NVIS in the Spanish tests [S21]. Technology assumption: weak-signal digital modes (FT8-class thresholds near 14 dB-Hz in my runs) cut the power or antenna requirement by about 30 dB compared with voice (calc: 45 versus 15 dB-Hz). That is the single biggest technology lever in the model.

---

## 3. How far could a broadcast or link actually go on the Peninsula

### 3.1 Link-feasibility table (calc, 100 W station, simple antenna unless noted)

Key to the HF columns: VOACAP and P.533 at SSN 100 unless stated; hours are per 24 h. "L" means local only (under 100 km), "NVIS" means regional near-vertical skywave.

| Link | km | Sea | MF ground wave (0.9 MHz, 1 kW) | VHF | HF 100 W | Dominant limit |
|---|---|---|---|---|---|---|
| Palmer–Puerto Abrigo | 27 | 37% | Sea 81, ice 44 dBµV/m: easy | LOS needs 410 m masts (island ridge); summits clear | NVIS, all hours 2.5 to 10 MHz | Ridge. Anything works over water. |
| Esperanza–Marambio | 94 | 70% | Sea 69, ice 20 | Needs 660 m masts, summits blocked (−207 m) | NVIS 24 h | Ridge across Trinity Peninsula |
| Contrapunto–Pergamino | 95 | 49% | Sea 69, ice 20 | 580 m masts; summit-to-summit clear (+40 m) | NVIS 24 h | Terrain |
| Esperanza–Contrapunto | 160 | 84% | Sea 63, ice 9 | 610 m masts; summits blocked | NVIS 24 h | Bransfield Strait is mostly sea; MF/HF ground wave plausible |
| Esperanza–Pergamino | 191 | 68% | Sea 63, ice 9 | 1,560 m | NVIS 24 h | Terrain |
| Marambio–Contrapunto | 249 | 84% | Sea 55–63 | 1,390 m | NVIS 24 h | Terrain |
| Palmer–Pergamino | 297 | 78% | Sea 55, ice −7 | 1,590 m; summits clear (+62 m) | NVIS 24 h, 2.5 to 10 MHz | Terrain; a mountain-top repeater works |
| Palmer–Rothera | 361 | 84% | Sea 52, ice −14 | 1,910 m; summits clear (+142 m) | NVIS 24 h, 2.5 to 10 MHz | Mountain-top repeater feasible; HF NVIS easy |
| Palmer–Marambio | 361 | 46% | Mixed, poor | More than 3,000 m | NVIS | Peninsula spine |
| Palmer–Esperanza | 375 | 27% | Mixed, poor | More than 3,000 m | NVIS: 1.8–7 MHz | Peninsula spine, 73% land to 1,790 m |
| Palmer–Contrapunto | 385 | 74% | Sea 51 | 2,590 m; summits blocked | NVIS | Terrain |
| Rothera–Marambio / Esperanza | 639 / 690 | 40% / 37% | Sea 37, ice −45 | More than 3,000 m | NVIS to low-angle F2: 2.5–10 MHz (24 h, Jan SSN100); July: 2.5–7 MHz | Terrain + earth curvature; HF only |
| Rothera–Contrapunto / Pergamino | 739 / 655 | 62% / 64% | Sea 35 | More than 3,000 m | Same as above | HF only |
| Marambio–Signy | 687 | 99% | Sea 37 | LOS impossible | 24 h at 2.5–14 MHz (Jan, SSN 100) | Distance; HF |
| Palmer–Signy | 1,037 | 74% | Sea 22 | Impossible | Voice, quiet noise: 24 h, 2.5–14.2 MHz. Rural noise, Jan SSN 100: 12 h | Noise, power, antenna |
| Rothera–Signy | 1,319 | 73% | Sea under 20 | Impossible | Quiet noise: 18 h, 2.5–14.2 (Jan SSN 100). Rural noise: 0 h at 100 W isotropic | Distance plus noise; needs gain antennas or 1 kW |
| Palmer–Ushuaia | 1,133 | n/a | n/a | Impossible | 21 h at 100 W, quiet noise, Jan SSN 100 | Drake Passage is sea but too far for ground wave |
| Palmer–Punta Arenas | 1,347 | n/a | n/a | Impossible | 12 h at 100 W, 24 h at 1 kW | Same |
| Palmer–Buenos Aires | 3,376 | n/a | n/a | Impossible | 0 h at 100 W isotropic; with 1 kW: 22 h Jan (10–28 MHz), 3 h Jul | Needs 14+ MHz and daylight |
| Palmer–McMurdo | 3,798 | n/a | n/a | Impossible | 0 h at 1 kW isotropic; 24 h only at 1 kW with +6 dBi each end | Auroral and polar-cap paths |

P.533-14 cross-check for the same links (100 W isotropic, 10 dB S/N in 3 kHz, quiet rural, basic circuit reliability at least 80%) is in 1.4 and 1.6 and gives the same pattern with more pessimistic winter results. In July, rural noise, Palmer–Signy and Rothera–Signy come out at 0 h/day in P.533 and Palmer–Ushuaia at 1 h (see Section 5).

### 3.2 Over water: Bransfield Strait and Drake Passage

- **Bransfield Strait (KGI/Livingston to Esperanza/Marambio, 95–260 km).** Mostly sea (68–84%). MF ground wave over sea at 1 kW 0.9 MHz is 55–69 dBµV/m at those distances (calc), so a 1 kW AM or a 100 W 3.5 MHz ground-wave station would cover it if the antenna is at the water's edge. Shadowing by islands is real but ground waves diffract around small islands.
- **Drake Passage legs (990–1,490 km).** Beyond ground wave except at the very bottom of the MF band at high power. HF skywave only.
- **Signy (660–1,320 km).** The Weddell Sea paths are 92–99% sea (Esperanza, Marambio, Contrapunto, Pergamino to Signy). MF ground wave at 10–50 kW can reach (sea, 0.9 MHz, 690 km: 47–54 dBµV/m for 10–50 kW). Over 700 km a daytime MF broadcast would be a real engineering case (inf; it needs a coastal site, a large antenna and a quiet receiver).

### 3.3 Documented achievements on the Peninsula (what I found)

- **Livingston Island (62.7°S) to Spain, 12,710 km, 250 W, 7.5 m monopole:** more than 95% availability on 8–10 MHz from 21 to 04 UTC in the 2006/07 summer; −5 dB typical S/N in 3 kHz [S20]. This is the strongest data point.
- **LRA36 (Esperanza)** heard in Ontario, Canada (12,175 km) on 15 476 kHz, rarely and with difficulty [S30, S31].
- **King George Island and the South Shetlands:** HF teletype weather bulletins from Frei to nearby stations (2001) [S5].
- **Not found:** documented amateur records from the Peninsula, VHF repeater ranges at Rothera or Frei, Palmer-to-Rothera link logs, tropospheric ducting events on the Peninsula. These are dead ends at the sources (Section 6).

### 3.4 Broadcast coverage envelopes (calc, from the tables in 1.3 and 1.5)

- **AM (MF), 1 kW / 10 kW / 50 kW radiated, 1 MHz, to 54 dBµV/m:**

| Ground | 1 kW | 10 kW | 50 kW |
|---|---|---|---|
| Sea | 314 km | 515 km | 665 km |
| Rock | 35 km | 59 km | 84 km |
| Polar ice | 13 km | 24 km | 35 km |

  - Over a sea or sea-ice path, to 40 dBµV/m: 600, 822 and 981 km. To 20 dBµV/m: 1,050, 1,284 and 1,450 km. That is a noise-limited fringe, not broadcast quality.
  - Night adds a sky wave, E-layer reflected, to thousands of kilometers, but it fades and mixes with interference [S13, S24].
  - Radiated power is lower than transmitter power for an antenna on ice without a good ground system (inf).
- **Shortwave, 10 to 100 kW.** In Region 2, 49 m (5.9–6.2 MHz) is a regional-to-national band, 41 m is narrow, and 25/19 m (11.6–12.1, 15.1–15.8 MHz) are used for international broadcasts. LRA36 transmits on 15 476 kHz to reach the rest of the world and is only rarely heard (see above). 10 kW at 15 MHz is a weak-signal DX result in North America. I did not model shortwave broadcast coverage numerically.
- **FM, 100 W to 10 kW with an antenna on a high point.** Coverage is horizon-limited. A 1,000 m antenna reaches 143 km to a 10 m receiver; 2,000 m reaches 197 km (calc). Free-space power is not limiting: for ERP 100 W the free-space distance to 48 dBµV/m is about 280 km (calc: 106.9 + 10 log 0.1 − 20 log d = 48 → d ≈ 279 km). So an FM service on a mountain top covers a ring about 140–200 km in radius over open water (inf, no terrain diffraction beyond the horizon). Radio Soberanía and LRA36's FM show real stations serving local sectors only.

---

## 4. The big-picture answer (evidence only)

**In order of need:**
1. **Local (under about 30 km, within an island group or harbor).** VHF at 156–162 MHz (the marine channel 16 hailing, channel 6/12/27-style working) with repeaters on high points. Calling frequency anchored by ITU channel 16 [S6]. Limit: radio horizon (26–36 km for 10 to 30 m masts; 140–400 km mountain to mountain).
2. **Regional (30–400 km, across the Bransfield Strait and up the Peninsula).** **NVIS HF on 1.8–7 MHz**, 100 W and a low horizontal dipole or inverted-V. Winter nights and mornings: 1.8–3 MHz. Summer and solar maximum: up to 7 MHz, MUF 7–8 MHz in January at SSN 100 for 361 km (VOACAP 7.1–7.8, P.533 7.4–8.4). Daytime and winter afternoons: 3.5–7 MHz. A natural calling band is 80/75 m (3.5–4.0 MHz) and 40 m (7.0–7.3 MHz), with the IARU emergency centers at 3750 and 7060 kHz as precedent. RFDS used 2–8 MHz for this role [S29]. Limit: foF2 (about 2–4 MHz in winter at solar minimum [S23]), not power.
3. **Long-distance (400–1,400 km: Signy, Ushuaia, Punta Arenas).** HF skywave, 2.5–14 MHz. Feasible with 100 W and 0 dBi in quiet noise. Marginal in rural noise. Dependable with 1 kW or with +6 dBi antennas. Frequencies shift with the cycle (SSN 5: up to 10–14 MHz; SSN 160: up to 14–18 MHz).
4. **Continental and ocean-basin distances (3,000+ km: Buenos Aires, McMurdo, Australia).** Needs 14–28 MHz in daylight at SSN of about 100 or above (Buenos Aires, 100 W with 0 dBi: 0 h; with 1 kW: 22 h in January). Palmer to McMurdo needs both 1 kW and directional antennas. Livingston Island reached 12,700 km on 8–10 MHz at night with 250 W and a monopole.
5. **Broadcast.** AM at 525–1705 kHz (Region 2) works best at the water's edge: 1–50 kW covers about 300 to 700 km over sea by ground wave, and only 10–85 km over ice or rock, so the siting matters more than the power. FM covers about 140–200 km from a mountain top.

**Main caveats:**
- **Solar cycle.** MUF changes by 30–50% across the cycle at 361 km. Cycle 25 peaked at 160.9 (October 2024) and NOAA expects about 9 by 2030, so the 2030 minimum is the harder case for upper bands.
- **Polar-cap absorption and storms.** The Peninsula at −50° geomagnetic is on the fringe of PCA, but G3+ storms (about 130 days per cycle) put the oval overhead, and the Weddell Sea Anomaly shifts summer peaks to night.
- **Ground conductivity.** Ice and rock cut ground-wave range by 10–20× compared with sea. Antennas need elevated radials or a counterpoise above snow depth.
- **Noise.** A quiet site is worth about 14 dB. Man-made noise from the settlement, not the atmosphere, is the limit.
- **Technology assumptions.** The numbers use 100 W and isotropic antennas. A directional antenna (+6 dBi each end) is worth roughly an order of magnitude in power. A weak-signal digital mode lowers the S/N requirement from 45 to 15 dB-Hz (30 dB). Both are far-future-neutral physics. Practical power, battery and antenna-size limits are not.
- **Model reliability.** VOACAP and P.533 use global CCIR/URSI foF2 maps that are thinly constrained in the Antarctic. They matched the published Livingston-Spain timing and the Vernadsky foF2 magnitude, but disagree on winter availability (Section 5).

---

## 5. Contradictions between sources

1. **VOACAP versus ITU-R P.533-14 in winter.** For the same 100 W isotropic quiet-rural inputs, VOACAP gives 24 h availability on some band for all NVIS and Signy links in July. P.533 gives 6–21 h for Rothera-to-Esperanza, Rothera-to-Signy, Palmer-to-Ushuaia and Palmer-to-Signy at SSN 5 to 160. With rural noise, P.533 gives 0 h for Palmer-to-Signy in July. I treat P.533 as the conservative bound and VOACAP as the optimistic one.
2. **LRA36 power and history.** Wikipedia: initially 6030 kHz at 1.2 kW, now 15 476 kHz at 10 kW. A search summary: began 20 October 1979 with 2 kW on 15 476 kHz. The 2019 announcement says 10 kW, while a commenter's QSL says 1.5 kW. A 2026 blog says 2 kW originally and 10 kW from 2024. The 1999 announcement said 10 kW. I could not resolve this.
3. **Palmer–Puerto Abrigo distance:** 27.4 km (calc) versus the 30 to 50 km you gave.
4. **Mount Français height:** 2,760 m or 2,825 m in different Wikipedia-derived sources (UNVERIFIED), versus 2,382 m in GEBCO (grid smoothing).
5. **Conductivity of ice.** The 4nec2 values (1×10⁻⁴, 3×10⁻⁴), the permafrost value used at Livingston (5×10⁻⁵), and Evans' pure-ice and snow values (10⁻⁹ to 10⁻⁵) differ by orders of magnitude. The ground-wave answer for ice is insensitive between 5×10⁻⁵ and 1×10⁻⁵ (7–8 km at 60 dBµV/m, 1 kW), so the model choice does not change the conclusion. Whether very-low-σ ice behaves like a lossy dielectric at MF/HF is not established by these sources.
6. **Ground-wave range quoted by the Army and by IPS.** FM 24-18: ideal 80 km, "as little as 3 km" in the field. IPS: 100 km land and 300 km sea. My calculation agrees with IPS for sea and is much shorter over ice and rock. The sources use different frequency ranges and thresholds.
7. **500 kHz.** It appeared in your list as a distress frequency. In RR 2024 it is NAVDAT only (WRC-23) [S6].
8. **243 MHz.** In your list with the distress allocations, it is outside Appendix 15 and is a survival-craft frequency under No. 5.256 [S7].
9. **The IntechOpen summary versus the source.** An automated summary said Livingston NVIS gave 200–250 km. The raw chapter shows that was the design claim and the NVIS trials were in Spain [S21].
10. **A search snippet said** "the installation of a repeater station is not an option in Antarctica." The AAD and USAP sources show mountain-top repeaters are in routine use [S2, S3, S27]. I discarded the snippet.
11. **USAP air manual** prints HF as "5.371 kHz" and "9.032 kHz"; the context shows MHz-style typos for 5371 and 9032 kHz [S1].

---

## 6. Search log and dead ends

**Queries I ran (exact strings, abbreviated where I appended operators).** Each topic was approached from at least two angles.

*AFIM, COMNAP, IAATO and station frequencies*
- "Antarctic Flight Information Manual AFIM COMNAP communications HF frequencies 5440 kHz 6 MHz Antarctic common frequencies" (found the 2021 procedures document, no frequency tables)
- "Antarctic aircraft common HF frequency "Antarctic" air-to-air VHF 123.45 MHz HF 5440 OR 4700 OR 6500 kHz ICAO Annex 10 Antarctic region"
- "IAATO field operations manual radio communications VHF channel 16 channel 12 channel 10 Antarctic Peninsula vessels station contact procedures"
- "Antarctic Peninsula radio "HF net" OR "HF schedule" stations Rothera Palmer Esperanza Marambio Frei calling frequency kHz"
- "Rothera Research Station VHF marine channel 1 156.000 handheld radio Rothera radio communications BAS radio room HF SSB frequencies"
- ""Rothera" "5080" "7775" "9106" HF USB" and "Falkland Islands AIP Rothera aerodrome communications HF 5080 kHz VHF 125.5 …" and "Rothera airfield approach sheet pilots HF contact frequencies USB VHF 118.1 MHz British Antarctic Survey air unit"
- "COMNAP Antarctic telecommunications HF radio schedule national programs "Antarctic" ham radio nets "14.243" OR "14.290" OR "7.090" Antarctic stations net"
- "Antarctic" "air-to-air" common VHF frequency 123.45 OR 126.7 OR 131.55 MHz …
- "USAP Field Manual Palmer Station HF radio field party daily check-in frequency 4125 kHz 11553 kHz VHF channel 27 …" and "Palmer Station Antarctica HF radio antenna VHF repeater Gamage Point OR "Bone Bay" …"
- "British Antarctic Survey Rothera field radio VHF repeater "Fossil Bluff" OR "Adelaide Island" OR "Mount Gaudry" …"
- "Australian Antarctic Division Davis OR Casey VHF repeater hilltop field communications repeater range km …"
- "VHF repeater Antarctic Peninsula Rothera OR "Palmer Station" OR "Vernadsky" OR "Frei" repeater mountain range km coverage"

*Ionosphere and geomagnetic latitude*
- "Antarctic Peninsula HF radio propagation measurements ionosonde Palmer Station Faraday Argentine Islands NVIS"
- "geomagnetic latitude Antarctic Peninsula Palmer Station Vernadsky corrected geomagnetic latitude South Atlantic anomaly ionosphere"
- "Weddell Sea Anomaly Antarctic Peninsula ionosphere nighttime summer electron density higher than daytime Vernadsky ionosonde foF2"
- "Vernadsky Argentine Islands ionosonde foF2 typical values MHz summer winter solar minimum maximum Antarctic Peninsula critical frequency"
- "polar cap absorption solar proton event geomagnetic cutoff latitude riometer equatorward extent PCA HF blackout NOAA SWPC D-RAP"
- "solar proton event polar cap absorption equatorward boundary corrected geomagnetic latitude 60 degrees large events extend to 55 degrees …"
- "auroral oval equatorward boundary geomagnetic latitude quiet Kp 0 magnetic latitude 67 storm Kp 9 reaches 50 degrees Feldstein oval Southern hemisphere"
- "Long-distance HF radio waves propagation during the April 2023 geomagnetic storm measurements Antarctica Europe RV Noosfera Vernadsky Zalizovski"
- "NOAA SWPC solar cycle 25 progression smoothed sunspot number latest observed predicted 2026"
- "NVIS near vertical incidence skywave Antarctica measurements critical frequency polar winter low foF2 below 3 MHz communication field parties"
- "Army FM 24-18 OR "TC 6-02" NVIS near vertical incidence skywave 0 to 500 km …"

*Ground conductivity, ground wave, noise, ITU documents*
- "ITU-R P.372 radio noise recommendation man-made noise quiet rural Fam equation …"
- "ground conductivity ice snow permafrost glacier S/m MF HF ground wave Antarctica ITU-R P.832 conductivity sea water 5 S/m"
- "ground-wave propagation over sea ice and snow ice sheet conductivity measurement MF HF Arctic Antarctic …"
- "electrical conductivity of polar ice sheet at radio frequency MHz firn snow dielectric permittivity …"
- "VLF propagation attenuation rate dB per Mm earth-ionosphere waveguide 20 kHz daytime nighttime Antarctic ice sheet conductivity effect NWC 19.8 kHz Palmer Station received"
- "LF MF ground wave range sea water 1 MHz 100 km 1 kW over land 30 km medium wave propagation ranges …"
- "minimum usable field strength AM medium wave broadcasting 0.5 mV/m rural 2 mV/m urban 54 dBuV/m …"
- "FM broadcast coverage radio horizon antenna height ERP 50 dBuV/m F(50,50) contour distance km …"
- "effective Earth radius factor k = 4/3 radio horizon formula 4.12 sqrt(h) km ITU-R P.834 …"
- "ITU Radio Regulations 2024 edition Volume 2 Appendices PDF Appendix 15 …"
- "Introduction to HF Radio Propagation" Bureau of Meteorology Space Weather Services PDF …"
- "rime ice accretion on antennas wires Antarctica HF antenna icing wind loading guy wires failure …"

*Frequencies in common use, communities, broadcasters, satellite*
- "IARU Region 2 band plan emergency center of activity 3750 7060 7240 14300 21360 calling frequency …"
- "14.300 MHz Intercontinental Maritime Mobile Service Net history …"
- "Royal Flying Doctor Service HF radio network history Traeger pedal radio frequencies base stations outback channels CB channel 9 emergency channel 19 truckers FCC origins"
- "amateur radio Antarctica Peninsula station HF contacts CE9 OR LU OR DP0 OR VP8 OR R1AN operators Vernadsky Palmer KC4 callsign 20 meters propagation experience"
- "LRA36 Radio Nacional Arcangel San Gabriel Esperanza 15476 kHz reception report DX heard 6030 kHz power kW Antarctica shortwave" and "swling.com Antarctica LRA36 …"
- "Radio Soberanía Villa Las Estrellas 90.5 FM 100 watts Frei Base Chile …"
- "Starlink coverage Antarctica stations …" and "geostationary satellite visibility Antarctic Peninsula Palmer Station low elevation …"
- "meteor burst communications 40 50 MHz range 1000 to 2000 km data rate SNOTEL …"
- "sporadic E OR "auroral" VHF propagation Antarctic Peninsula 50 MHz OR 144 MHz amateur radio beacon …"
- "tropospheric ducting VHF Antarctica Antarctic Peninsula radio refractivity inversion katabatic surface duct events"
- "anomalous propagation Antarctica refractivity profile radiosonde ducting frequency Antarctic coastal inversion trapping layer radar duct study"
- "Mount Français Anvers Island height 2760 metres highest point Palmer Archipelago USGS GNIS OR SCAR gazetteer"

**Dead ends and snags (what died where):**
1. **COMNAP AFIM frequency tables.** Died at the sources: the public AFIM is procedures only [S4]. Frequency tables are in the subscriber release.
2. **Rothera HF frequencies (5080/7775/9106 kHz) and IAATO hailing frequencies (4146/6224/8294).** Died at the sources. Repeated searches returned only the same unsourced snippet, and I could not open the primary documents.
3. **Peninsula-specific VHF ducting, anomalous propagation, sporadic-E or auroral VHF contacts.** Died at the sources (no Antarctica-specific literature surfaced across four searches).
4. **Documented amateur records, Palmer-to-Rothera link logs, Frei/Rothera repeater ranges, BAS and Argentine/Chilean HF net frequencies.** Died at the sources.
5. **BAS or Argentine/Chilean/Ukrainian propagation measurements** beyond the Spanish Livingston Island studies: not found (the Ukrainian Vernadsky papers are about ionospheric physics, with one HF-propagation storm paper known only from a search summary).
6. **Primary ice and snow conductivity at MF/HF in Antarctica.** Died at the sources. Only the DC review (Evans 1965), a simulation value (permafrost) and a hobbyist table exist in what I found.
7. **Sea-ice conductivity at MF.** Only the model concept [S26] and an unverified summary number.
8. **P.372 atmospheric-noise value at 64°W.** Not read numerically from the map images, so left as a qualitative statement.
9. **Pages that returned 403 or other errors:** vlfstanford.ku.edu.tr (Palmer L-shell), academia.edu (Vernadsky WSA paper), mmsn.org, vlf.ece.ufl.edu (certificate error), the ITU P.372-17 and P.368-10 PDFs (404; I used P.372-13 and P.368-9). The Palmer L = 2.4 and "50° geomagnetic latitude" figure from the Stanford page snippet is UNVERIFIED; my AACGM/IGRF computation gives an invariant latitude consistent with it.
10. **Self-corrections.**
    - My first VOACAP matrix ignored the sunspot number because I put the decimal point outside the card's fixed 5-column field (read as SSN/100). All results shown here are from the corrected re-run.
    - My first summaries counted VOACAP's over-the-MUF E-layer scatter mode as "usable"; I re-filtered to median-MUF-supported frequencies.
    - The first ground-wave tool (GRWAVE) showed a 20 dB discontinuity; I replaced it with NTIA LFMF and cross-checked by hand.
    - WebFetch summaries of two sources were wrong or misleading (IntechOpen NVIS claim; ITU RR text). I re-read raw text from downloaded PDFs for every number quoted from them.
11. **Textbooks.** Davies "Ionospheric Radio", Maslin "HF Communications" and the ARRL Handbook were not accessible and were not read. I used primary standards, manuals and papers instead.
12. **IAATO FOM and the 'MMSN' history, Starlink coverage, Mount Français height, and the PCA cutoff-latitude number** are marked UNVERIFIED wherever used.

---

## 7. Source table (all accessed 2026-10-04)

| # | Source | URL |
|---|---|---|
| S1 | USAP Interagency Air Operations Manual, 1 March 2026 | https://www.usap.gov/logistics/documents/Air_Operations_Manual.pdf |
| S2 | USAP Field Manual, 6th ed. (2001–02 season) | https://intranet.ess.uw.edu/intranet/public_files/usap-field-manual.pdf |
| S3 | USAP Peninsula Field Manual 2026, Communications chapter | https://www.usap.gov/usapgov/travelAndDeployment/documents/USAP-Peninsula-Field-Manual-2026-Communications.pdf |
| S4 | COMNAP AFIM Procedures, Version 15 July 2021 | https://www.comnap.aq/s/Antarctic-Flight-Information-Manual-Procedures-15-July-2021.pdf |
| S5 | Report of the US Antarctic Inspection, 2–16 Feb 2001 (ATCM XXIV) | https://documents.ats.aq/ATCM24/att/ATCM24_att002_e.pdf |
| S6 | ITU Radio Regulations 2024, Vol. 2 (Appendices, incl. App. 15) | https://search.itu.int/history/HistoryDigitalCollectionDocLibrary/1.49.48.en.102.pdf |
| S7 | ITU Radio Regulations 2024, Vol. 1 (Articles, Table of Allocations, footnotes) | https://search.itu.int/history/HistoryDigitalCollectionDocLibrary/1.49.48.en.101.pdf |
| S8 | Rec. ITU-R P.372-13 (09/2016) Radio noise | https://www.itu.int/dms_pubrec/itu-r/rec/p/R-REC-P.372-13-201609-S!!PDF-E.pdf |
| S9 | Rec. ITU-R P.832-4 (07/2015) World atlas of ground conductivities | https://www.itu.int/dms_pubrec/itu-r/rec/p/R-REC-P.832-4-201507-I!!PDF-E.pdf |
| S10 | Rec. ITU-R P.368-9 (02/2007) Ground-wave curves; implemented via NTIA LFMF (P.368-10) | https://www.itu.int/dms_pubrec/itu-r/rec/p/R-REC-P.368-9-200702-S!!PDF-E.pdf ; https://github.com/NTIA/LFMF |
| S11 | Rec. ITU-R P.834-9 (12/2017) Effects of tropospheric refraction | https://www.itu.int/dms_pubrec/itu-r/rec/p/R-REC-P.834-9-201712-I!!PDF-E.pdf |
| S12 | Rec. ITU-R BS.703 (1990) Characteristics of AM sound broadcasting reference receivers | https://www.itu.int/dms_pubrec/itu-r/rec/bs/R-REC-BS.703-0-199006-I!!PDF-E.pdf |
| S13 | US Army FM 24-18, Tactical Single-Channel Radio Communications Techniques (1987) | https://www.bits.de/NRANEU/others/amd-us-archive/FM24-18(87).pdf |
| S14 | BoM Space Weather Services, "Introduction to HF Radio Propagation" (2016) | https://www.sws.bom.gov.au/Category/Educational/Other%20Topics/Radio%20Communication/Intro_HF_Radio.pdf |
| S15 | NOAA SWPC, NOAA Space Weather Scales | https://www.spaceweather.gov/noaa-scales-explanation |
| S16 | NOAA SWPC, D-Region Absorption Predictions (D-RAP) | https://www.spaceweather.gov/products/d-region-absorption-predictions-d-rap |
| S17 | NOAA SWPC JSON: observed and predicted solar cycle | https://services.swpc.noaa.gov/json/solar-cycle/observed-solar-cycle-indices.json ; https://services.swpc.noaa.gov/json/solar-cycle/predicted-solar-cycle.json |
| S18 | NIST, Radio Station WWV | https://www.nist.gov/pml/time-and-frequency-division/time-distribution/radio-station-wwv |
| S19 | IARU Region 2 Band Plan (effective 14 Oct 2016) | https://www.iaru.org/wp-content/uploads/2020/01/R2-Band-Plan-2016.pdf |
| S20 | Bergadà et al., Sensors 2009, 9(12):10136, HF Antarctica–Spain link | https://pmc.ncbi.nlm.nih.gov/articles/PMC3267214 |
| S21 | Porté et al. (2018), IntechOpen, "Advanced HF Communications for Remote Sensors in Antarctica" | https://www.intechopen.com/chapters/63904 |
| S22 | Marayén Canales et al. (2025), Ann. Geophys. 43, 383, Weddell Sea Anomaly trends | https://angeo.copernicus.org/articles/43/383/2025/ |
| S23 | Bogomaz et al. (2019), Ukr. Antarct. J. 19, ionosphere over Vernadsky, June 2019 | https://uaj.uac.gov.ua/index.php/uaj/article/download/154/98 |
| S24 | NTIA Report 99-368, Medium Frequency Propagation Prediction Techniques (DeMinco, 1999) | https://its.ntia.gov/publications/download/99-368_ocr.pdf |
| S25 | Evans (1965), Dielectric properties of ice and snow: a review, J. Glaciol. 5(42) | https://users.fuw.edu.pl/~op2ds/wyklad/Evans-igs_journal_vol05_issue042_pg773-792.pdf |
| S26 | Hehenkamp et al. (2025), Modeling ground-wave propagation across sea ice, Adv. Radio Sci. 22 | https://ars.copernicus.org/articles/22/77/2025/ |
| S27 | Australian Antarctic Division magazine, Spring 2001, telecommunications feature | https://www.antarctica.gov.au/magazine/issue-2-spring-2001/feature/australia-continues-as-telecommunications-innovator/ |
| S28 | SWLD, AAD HF frequency list (data 18 Oct 2012; hobbyist compilation) | http://www.swld.com.au/pages/aus_antarctica.htm |
| S29 | SWLD, RFDS HF frequencies (data 13 Sept 2013; hobbyist compilation) | http://www.swld.com.au/pages/aus_rfds.htm |
| S30 | SWLing.com, LRA36 special broadcast, 21 Sept 2019 | https://swling.com/blog/2019/09/special-broadcast-lra36-radio-nacional-arcangel-san-gabriel-antarctica/ |
| S31 | Shortwave Radio Audio Archive, LRA36 recording, Coe Hill ON, 20 Feb 1999 | https://shortwavearchive.com/archive/radio-nacional-arcangel-san-gabriel-lra36-base-esperanza-antarctica-february-20-1999 |
| S32 | Shortwave Central blog, "Radio in Antarctica Part 2" (March 2026; secondary) | https://mt-shortwave.blogspot.com/2026/03/radio-in-antarctica-part-2-antarctic.html |
| S33 | Wikipedia (LEADS ONLY, flagged): Esperanza Base, LRA36, Marambio Base, Radio Soberanía (es), Telecommunications in Antarctica, Rothera pages | https://en.wikipedia.org/wiki/Esperanza_Base ; https://en.wikipedia.org/wiki/LRA36_Radio_Nacional_Arc%C3%A1ngel_San_Gabriel ; https://en.wikipedia.org/wiki/Marambio_Base ; https://es.wikipedia.org/wiki/Radio_Soberan%C3%ADa |
| S34 | NASA NTRS, Polar Communications: Status and Recommendations (1991) | https://ntrs.nasa.gov/api/citations/19910021045/downloads/19910021045.pdf |
| S35 | ARRL News, Amateur Radio News from Antarctica (12 Dec 2019) | https://www.arrl.org/news/amateur-radio-news-from-antarctica |
| S36 | MMSN history (UNVERIFIED; search summary, site returned 403) | https://www.mmsn.org/about-us/about-us.html |
| S37 | 47 CFR 95.931 (CB channel 9) | https://www.law.cornell.edu/cfr/text/47/95.931 |
| S38 | Royal Belgian Institute for Space Aeronomy, auroral ovals at the two geomagnetic poles | https://www.aeronomie.be/en/encyclopedia/auroral-ovals-two-geomagnetic-poles |
| S39 | Tools: voacapl https://github.com/jawatson/voacapl ; ITURHFProp/P.533/P.372 https://github.com/ITU-R-Study-Group-3/ITU-R-HF ; NTIA LFMF https://github.com/NTIA/LFMF ; aacgmv2 (PyPI); IGRF-14 coefficients (ppigrf, PyPI); GEBCO-2020 via https://api.opentopodata.org | as listed |
| S40 | hamwaves.com World Atlas of Ground Conductivity page (4nec2 tables, no primary citation) | https://hamwaves.com/ground/en/ |
| S41 | BoM SWS, Global HF: Polar Cap Absorption | https://www.sws.bom.gov.au/HF_Systems/6/3 |
| S42 | CRREL, Icing and Snow Accretion on Electric Wires (1965) (UNVERIFIED beyond title) | https://erdc-library.erdc.dren.mil/server/api/core/bitstreams/81b728f8-7e71-4ef8-e053-411ac80adeb3/content |
| S43 | IAATO checklist of yacht items for Antarctic voyages (2025) | https://iaato.org/sites/default/files/2025-03/ATCM%20Yacht%20Checklist.en_.pdf |
| S44 | Numerical modelling of VLF propagation (PhD thesis, Univ. Calcutta), arXiv 1503.05789, citing Davies 1990 and Barr 1987/2000 | https://arxiv.org/pdf/1503.05789 |
| S45 | Starlink at McMurdo (news; UNVERIFIED search summaries): SpaceX/Space.com/DCD | https://www.space.com/spacex-starlink-internet-service-antarctica |
| S46 | Zakharenkova et al. (2017) JGR Space Physics 122 (WSA TEC; cited in S22, not read) | n/a |
| S47 | Zalizovski et al., Ukr. Antarct. J. 2023, April 2023 storm HF (UNVERIFIED, search summary) | http://uaj.uac.gov.ua/index.php/uaj/article/view/749 |
| S48 | NTIA Report 89-241, Meteor Burst System Communications Compatibility (UNVERIFIED, search summary) | https://its.ntia.gov/publications/download/89-241_ocr.pdf |
