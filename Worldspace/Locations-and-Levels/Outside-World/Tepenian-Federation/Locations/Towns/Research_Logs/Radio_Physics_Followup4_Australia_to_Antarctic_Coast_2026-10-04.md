<!-- ERRATUM (2026-10-04, from Follow-up 5): the statement below that the 1913 Mawson link used 'Wireless Hill, Perth' is wrong. Wireless Hill in the AAD and Maritime Radio sources is the hill at Macquarie Island Station; Macquarie was the relay (Commonwealth Bay to Macquarie to Hobart). See Radio_Physics_Followup5_Macquarie_2026-10-04.md section 5. -->
<!-- Log written 2026-10-04: the research agent's fourth follow-up report (Perth to Casey, Hobart to Dumont d'Urville and context legs), extracted verbatim from its transcript (not re-typed). Uses the CORRECTED VOACAP parser. VOACAP and P.533 disagree on the MUF peak for Perth-Casey; polar-cap and auroral availability percentages are the agent's estimates, not measurements; the 1978 telex circuit and Casey relay hub statements are UNVERIFIED (search summaries). -->

# Australia to the Antarctic coast: HF models, geometry, polar exposure and documented performance

All access dates are 2026-10-04. (calc) marks my own calculation, (inf) marks inference, UNVERIFIED marks facts seen only in a search-engine summary. Source numbers [S#] continue the earlier source tables. Nothing was written to the project; all work is in the session scratchpad.

**Method.**
- Same tools as before: voacapl 16.1207W with the corrected parser, and ITURHFProp (ITU-R P.533-14 with the P.372 noise library).
- The sender is in Australia and the receiver is at the Antarctic end, so quiet-rural (−164 dBW/Hz at 3 MHz) or rural (−150) noise applies at the Antarctic end.
- Matrix: Jan and Jul, SSN 5/60/160, 100 W / 1 kW / 5 kW, 0 / +6 dBi at both ends, voice (45 dB-Hz VOACAP; 10 dB S/N in 3 kHz P.533) and weak-signal digital (15 dB-Hz; −20 dB).
- Usable means REL ≥ 0.8 with f ≤ median MUF (VOACAP) or BCR ≥ 80% (P.533). All hours are UTC.
- 10 W was not run (the request listed 100 W, 1 kW and 5 kW).
- Cape Denison position used: −67.009, 142.664 (my assumption for "Denison").
- Neither model includes polar-cap absorption (PCA) or auroral substorms; those are treated in Section 4.

---

## 1. Distance, sea fraction, terrain, geomagnetic latitude (calc)

| Leg | Distance | Sea (GEBCO, 160 samples) | Land segments along the path |
|---|---|---|---|
| Perth–Casey | **3,834 km** | 92% | 0–265 km (SW Australia), 1 sample at Casey |
| Hobart–Dumont d'Urville (DDU) | **2,681 km** | 98% | 0–17 km (Tasmania), small island at 51 km |
| Hobart–Denison | **2,698 km** | 97% | 0–17 km, 51–68 km (234 m), Denison end |
| Perth–Mawson | **5,209 km** | 99% | Perth coast only |
| Perth–Davis | **4,727 km** | 97% | small islands at 208–238 km, Davis coast (424 m) |

The distance to Casey is 3,834 km (calc). A DX-World article gives "about 3,880 kilometres due south of Perth" (UNVERIFIED, 1.2% higher; Casey is 5.3° of longitude east of south) [S58].

**Geomagnetic latitude (AACGM-v2 at 110 km, 2025.5 / IGRF-14 dipole):**

| Node | AACGM | Dipole |
|---|---|---|
| Perth | −43.6° | −41.0° |
| Hobart | −53.7° | −49.6° |
| Casey | **−80.5°** | −75.5° |
| DDU | **−80.0°** | −73.7° |
| Cape Denison | **−79.9°** | −73.7° |
| Mawson | −70.9° | −73.0° |
| Davis | −75.1° | −75.9° |

**Hop midpoints and last-hop positions (AACGM):**

| Leg | Midpoint | One-quarter point | Three-quarter point | Poleward-most | Dipole mid |
|---|---|---|---|---|---|
| Perth–Casey | −62.7° | −53.2° | −72.0° | −80.5° | −58.3° |
| Hobart–DDU | −66.9° | −60.3° | −73.5° | −80.0° | −61.6° |
| Hobart–Denison | −66.9° | −60.3° | −73.4° | −79.9° | −61.7° |
| Perth–Mawson | −65.6° | −55.3° | −71.7° | −72.2° | −61.5° |
| Perth–Davis | −65.0° | −54.7° | −72.9° | −75.3° | −60.8° |

Casey, DDU and Denison lie at −80° AACGM, which is at or poleward of the usual auroral-oval band (about 65–75° [S38]). They are inside the polar cap, and Casey is the station BoM uses as its PCA riometer reference [S41].

**Day and night (calc, geometric, 15 January / 15 July):**

| Station | 15 Jan | 15 Jul |
|---|---|---|
| Casey | 21.0 h (sunrise about 18:16, sunset about 15:17 UTC) | 4.0 h |
| DDU | 21.4 h | 3.8 h |
| Davis | midnight sun | 1.9 h |
| Mawson | 22.7 h | 3.0 h |
| Perth | 14.0 h | 10.2 h |
| Hobart | 15.0 h | 9.3 h |

---

## 2. One-hop versus multi-hop geometry (calc; spherical earth, layer heights 300 km F2 and 110 km E; IPS gives a maximum one-hop F2 distance of about 4,000 km [S14], 3,836 km at 0° elevation in my calculation)

| Leg | 1 hop | 2 hops | 3 hops |
|---|---|---|---|
| Hobart–Denison (2,698 km) | 6.1° takeoff, sec 3.19 | 1,349 km hops, 20.4°, sec 2.24 | 899 km, 31.1°, 1.74 |
| Hobart–DDU (2,681 km) | 6.3°, sec 3.18 | 1,340 km, 20.6°, 2.23 | 894 km, 31.2°, 1.73 |
| Perth–Casey (3,834 km) | **0.0° (exactly the one-hop limit; not usable)** | 1,917 km, 12.7°, sec 2.76 | 1,278 km, 21.7°, 2.17 |
| Perth–Davis (4,727 km) | exceeds the 3,836 km limit | 2,364 km, 8.6°, sec 3.04 | 1,576 km, 16.8°, 2.47 |
| Perth–Mawson (5,209 km) | exceeds the limit | 2,604 km, 6.8°, sec 3.15 | 1,736 km, 14.7°, 2.61 |

- Perth–Casey must be a two-hop (or three-hop) path with a middle refraction near −55° to −62° (Southern Ocean). The Casey-side hop lands at about −72° AACGM (3/4 point).
- Hobart–DDU can be one low-angle hop (6°, hard for real antennas) or two hops at about 20°, which is the natural mode. Its second refraction is at about −73° AACGM.
- The MUF is the layer critical frequency times the secant: sec 3.2 for one hop at 2,700 km, 2.2 for two hops (calc).

---

## 3. HF model results

### 3.1 Any-band usable hours per 24 h (V = VOACAP, P = P.533; minimum to maximum across SSN 5/60/160; each cell shows Jan | Jul)

**Voice, quiet-rural noise at the Antarctic end:**

| Power, antenna | Perth–Casey | Hobart–DDU | Hobart–Denison | Perth–Mawson | Perth–Davis |
|---|---|---|---|---|---|
| 100 W, 0 dBi | V 0–2, P 0–2 \| V 0–7, P 0 | V 3, P 9–11 \| V 11–19, P 2–13 | V 3, P 9–11 \| V 11–19, P 2–14 | 0 \| 0 | 0 \| 0 |
| 100 W, +6 dBi | V 16–19, P 16–19 \| V 17–24, P 14–22 | V 18–22, P 24 \| V 24, P 22–24 | V 17–22, P 24 \| V 24, P 23–24 | V 4–6, P 11–12 \| V 6–20, P 6–14 | V 7–9, P 12 \| V 14–21, P 11–19 |
| 1 kW, 0 dBi | V 11–16, P 15 \| V 16–23, P 14–20 | V 14–21, P 24 \| V 24, P 22–24 | V 14–20, P 24 \| V 24, P 23–24 | V 3, P 10–12 \| V 4–18, P 0–7 | V 5–7, P 9–11 \| V 7–21, P 7–14 |
| 1 kW, +6 dBi | V 22–24, P 24 \| V 24, P 21–24 | V 23–24, P 24 \| V 24, P 23–24 | V 22–24, P 24 \| V 24, P 23–24 | V 12–16, P 24 \| V 23–24, P 16–22 | V 13–16, P 20–24 \| V 23–24, P 16–22 |
| 5 kW, 0 dBi | V 17–24, P 17–24 \| V 24, P 16–24 | V 22–24, P 24 \| V 24, P 23–24 | V 22–24, P 24 \| V 24, P 23–24 | V 9–10, P 16–24 \| V 15–23, P 13–20 | V 10–11, P 17–24 \| V 19–24, P 15–21 |
| 5 kW, +6 dBi | V 23–24, P 24 \| V 24, P 24 | V 24, P 24 \| V 24, P 24 | V 23–24, P 24 \| V 24, P 24 | V 16–22, P 24 \| V 24, P 23–24 | V 19–23, P 24 \| V 24, P 20–24 |

**Voice, rural noise at the Antarctic end:**

| Power, antenna | Perth–Casey | Hobart–DDU | Hobart–Denison | Perth–Mawson | Perth–Davis |
|---|---|---|---|---|---|
| 100 W, 0 dBi | **0 \| 0** | **0 \| 0** | **0 \| 0** | 0 \| 0 | 0 \| 0 |
| 100 W, +6 dBi | V 0–7, P 4–7 \| V 0–18, P 1–5 | V 6–9, P 15–22 \| V 20–23, P 19–23 | V 6–9, P 18–22 \| V 20–22, P 20–23 | 0 \| V 0–6, P 0 | 0 \| V 0–11, P 0–2 |
| 1 kW, 0 dBi | V 0–3, P 0–2 \| V 0–11, P 0–1 | V 3–4, P 13–16 \| V 18–19, P 11–21 | V 3–4, P 13–16 \| V 18–19, P 11–22 | 0 \| V 0–3, P 0 | 0 \| V 0–5, P 0 |
| 1 kW, +6 dBi | V 16–19, P 16–23 \| V 21–24, P 15–24 | V 18–24, P 24 \| V 24, P 23–24 | V 18–24, P 24 \| V 24, P 23–24 | V 6–8, P 13–14 \| V 14–21, P 13–20 | V 9–10, P 13–17 \| V 17–22, P 14–20 |
| 5 kW, 0 dBi | V 9–12, P 14 \| V 17–22, P 13–20 | V 13–17, P 24 \| V 24, P 22–24 | V 13–17, P 24 \| V 24, P 23–24 | V 3, P 8–11 \| V 3–18, P 1–9 | V 2–3, P 8–10 \| V 10–18, P 2–11 |
| 5 kW, +6 dBi | V 17–24, P 21–24 \| V 24, P 22–24 | V 22–24, P 24 \| V 24, P 24 | V 22–24, P 24 \| V 24, P 24 | V 12–15, P 22–24 \| V 22–24, P 16–22 | V 13–14, P 18–24 \| V 23–24, P 16–22 |

**Weak-signal digital (FT8-class), any-band hours:**

| Case | Perth–Casey | Hobart–DDU | Hobart–Denison | Perth–Mawson | Perth–Davis |
|---|---|---|---|---|---|
| 100 W, 0 dBi, quiet | V 24, P 24 (both months) | 24 / 24 | 24 / 24 | V 17–24, P 24 \| 24 | V 20–24, P 22–24 |
| 100 W, 0 dBi, rural | V 18–24, P 24 \| V 24, P 22–24 | V 23–24, P 24 \| 24 / 24 | V 22–24, P 24 \| 24 / 24 | V 12–16, P 24 \| V 23–24, P 18–23 | V 13–14, P 19–24 \| V 24, P 17–22 |
| 100 W, +6 dBi, rural | 24 / 24 | 24 / 24 | 24 / 24 | V 19–24, P 24 \| 24 | V 22–24, P 24 \| 24 |

The Hobart–DDU and Hobart–Denison rows differ by at most 1 h everywhere (calc), because the two Antarctic ends are 54 km apart (calc).

### 3.2 Per band, MUF and best windows

**MUF ranges (hourly range over the day, V | P, MHz):**
- Perth–Casey, January: V 12.4–19.6 | P 8.1–14.2 (SSN 5), V 13.7–20.9 | P 9.6–17.4 (SSN 160).
- Perth–Casey, July: V 8.3–19.7 | P 5.0–13.8 (SSN 5), V 8.9–32.8 | P 5.6–24.5 (SSN 160). The models differ by up to about 6 MHz at the daytime peak.
- Hobart–DDU: January V 10.5–17.7 | P 8.8–16.4 (SSN 5); July V 7.1–16.5 | P 5.2–15.2 (SSN 5), up to about 27 MHz at SSN 160.
- Perth–Mawson: January V 10.5–15.7 | P 8.7–14.4 (SSN 5); July V 6.6–15.6 | P 4.6–14.1. Perth–Davis is similar.

**Hours per day per band, 1 kW, +6 dBi, voice, quiet-rural (V/P; columns 2.5, 3.5, 5, 7.1, 10.1, 14.2 MHz):**

| Leg, month, SSN | 2.5 | 3.5 | 5 | 7.1 | 10.1 | 14.2 |
|---|---|---|---|---|---|---|
| Perth–Casey Jan 5 | 6/6 | 9/9 | 13/12 | 15/18 | 12/21 | 2/8 |
| Perth–Casey Jan 160 | 6/5 | 8/7 | 10/10 | 13/13 | 15/24 | 13/13 |
| Perth–Casey Jul 5 | 13/14 | 15/14 | 17/14 | 12/5 | 10/5 | 2/0 |
| Perth–Casey Jul 160 | 11/12 | 14/13 | 16/14 | 17/12 | 16/8 | 13/12 |
| Hobart–DDU Jan 5 | 8/10 | 11/13 | 13/24 | 15/24 | 22/24 | 15/19 |
| Hobart–DDU Jul 5 | 16/14 | 19/15 | 24/17 | 23/14 | 11/10 | 6/6 |
| Hobart–DDU Jul 160 | 14/14 | 16/14 | 18/14 | 22/16 | 20/18 | 12/13 |
| Perth–Mawson Jan 5 | 0/10 | 5/13 | 8/17 | 10/24 | 13/22 | 5/4 |
| Perth–Mawson Jul 5 | 4/12 | 13/14 | 15/11 | 14/3 | 7/1 | 0/0 |

**Best UTC windows (1 kW +6 dBi quiet voice, SSN 60, V | P):**

| Leg, month | 2.5 MHz | 3.5 | 5 | 7.1 | 10.1 | 14.2 |
|---|---|---|---|---|---|---|
| Perth–Casey Jan | 14–19 \| 15–19 | 12–20 \| 14–21 | 11–21 \| 13–22 | 10–22 \| 11–24 | 09–16, 22–24 \| 19–17 | 10, 16, 21–22 \| 11–12, 24–09 |
| Perth–Casey Jul | 11–22 \| 11–23 | 09–23 \| 11–24 | 08–24 \| 11–24 | 07–13, 16–19, 23–02 \| 10–13, 16–19, 23–01 | 01–11, 13, 16–19 \| 08–11, 24–02 | 03–09, 11, 24 \| 03–09 |
| Hobart–DDU Jan | 11–17 \| 12–19 | 10–18 \| 11–21 | 08–20 \| 09–22 | 07–20 \| all | 05–20, 22, 24–02 \| all | 03–13, 20–24 \| 18–16 |
| Hobart–DDU Jul | 07–21 \| 09–22 | 06–22 \| 09–22 | 04–24 \| 08–22 | all \| 06–18, 21–23 | 22–10 \| 02–11, 22–24 | 23–07 \| 23–09 |

- In local terms (Perth about UTC+8, Casey about UTC+7.4 solar), the low bands 2.5–5 MHz are usable from about 11–22 UTC, which is local evening to early morning (inf from the windows).
- The July 14.2 MHz window (03–09 UTC) is the local daytime peak at both ends.
- At solar minimum (SSN 5, about 2030) the high end shrinks: Perth–Casey 14.2 MHz is usable only 2 h in July (VOACAP) and 18.1 MHz is gone in July. The link then depends on 2.5–7.1 MHz.

---

## 4. Polar-cap and auroral exposure of the Antarctic end (inf; derived from NOAA counts and flagged assumptions)

**Documented behavior (sources as in the earlier reports):**
- BoM [S14, S41]: PCA gives HF blackout on trans-polar circuits that can last several days, and BoM advises relaying around the polar region.
- NOAA [S15]: S1–S5 radiation storms occur 50, 25, 10, 3 and under 1 times per cycle. Geomagnetic storm days per cycle: G1 or stronger 900, G3 or stronger 130.
- D-RAP [S57]: absorption scales as A(f) = A(f0)(f0/f)^1.5, so 2.5–5 MHz is hit hardest.
- McMurdo–South Pole sounding [S55]: nothing received below 4.1 MHz in a polar-summer test.

**Exposure of each station:**

| Station | AACGM | Exposure |
|---|---|---|
| Casey, DDU, Denison | −80° | Polar cap, full PCA exposure; cusp-latitude events near local magnetic noon (inf) |
| Davis | −75° | Poleward edge of the oval to the polar cap |
| Mawson | −71° | In the night-side auroral band |
| Hobart (sender end) | −54° | Sub-auroral; the NOAA G3 oval (about 50° geomagnetic) can reach it |
| Perth (sender end) | −44° | Mid-latitude, not exposed |

**Where the exposure bites on the path.** The last refraction point (3/4 along the path) sits at −72° (Perth–Casey), −73.5° (Hobart–DDU), −72° (Perth–Mawson) and −73° (Perth–Davis). The signal enters the polar D region near the Antarctic end on the last hop, which is where PCA acts. The Australian ends are not exposed (inf).

**My estimates:**
- **PCA:** 0.7–2.5% of time on any link ending at Casey, DDU, Denison, Davis or Mawson (calc: about 29 days per cycle from 24 moderate events of about 8 h and 13 severe events of 1.6 days, up to 50 S1 events at about 2 days each; the event statistics are UNVERIFIED).
- **Auroral absorption and storm degradation:** 5–15% of hours at the −80° ends and 10–20% at Mawson (inf). I found no published occurrence percentage for Casey, Davis or Mawson; the BoM/AAD riometer data exist, but statistics were not retrieved.
- **Net per-link voice availability (inf):** about 80–95% for Hobart–DDU/Denison and Perth–Casey at 1 kW with +6 dBi, about 70–90% for Perth–Mawson, and about 88–98% for weak-signal digital with automatic band selection.
- **Solar minimum (about 2030, SSN 5; NOAA predicts 9.3 for October 2030 [S17]):** the high bands close and the link depends on 2.5–7.1 MHz, the bands PCA absorbs most (inf).
- **Historical corroboration:** at Commonwealth Bay the 1913 operator Jeffryes "sometimes spent entire evenings trying to transmit or receive a single message" because of atmospheric static and auroral interference [S59].

---

## 5. Documented real performance

- **Mawson's 1912–13 expedition.** A relay station at Macquarie Island used Wireless Hill (Perth); the main Antarctic base achieved communication with Australia via Wireless Hill in February 1913. The Wireless Hill transmitter was a Telefunken 1.5 kW spark set on long wave and Morse [S59].
- **AAD post-war HF.**
  - Stations used 500 W Morse transmitters from 1948 (UNVERIFIED, search summary).
  - The "radphone" gave voice from Australia to Antarctica via Sydney Radio. Weather changes could cause "frustrating black-outs, noise interference, and regular fade-outs" [S60].
  - In 1978 Australia opened a leased 50-band telex circuit between Casey and Sydney, and Casey acted as relay for Mawson and Davis (UNVERIFIED: this appeared in search summaries but not in any fetched page text; the same sources say data tapes were relayed to Australia via Casey in the early 1980s).
  - Inmarsat from the mid-1980s "signalled the end of High Frequency (HF) radio as the primary mode of communication with Australia" [S60].
- **AAD practice today** (2001 feature, [S27]): VHF is the main short-range medium with mountain-top solar/wind repeaters; "HF radio is still used for field parties, ships and aircraft out of VHF range with the addition of a SELCALL emergency calling system". Further statements seen only in search summaries (UNVERIFIED): HF links stations to field parties without satellite terminals, HF is used for aircraft between stations, and HF "will be used" for aircraft flying between Hobart and Casey.
- **AAD frequency list [S28, 2012, hobbyist compilation]:** 2.720, 3.023, 3.175, 3.418, 4.040, 4.540, 4.678 and 5.400 MHz (primary), with aircraft on 5726, 9032 and 11256 kHz USB. A daily schedule on 3023 kHz serves Macquarie Island field huts. The list is dominated by 2.7–5.4 MHz, matching the low-band model results (inf).
- **VK0 amateur contacts.**
  - VK0TBC (Casey) operates SSB and FT8, and VK0DS (Davis) uses an end-fed antenna on a 22 m tower with a V-beam array planned. Both operators say propagation, work commitments, weather and station life prevent a regular schedule [S58].
  - Historical VK0 contacts on 20 m succeeded, and attempts on 40 m failed for noise and insufficient signal (UNVERIFIED, search summary).
  - The sources did not give the amateurs' power or contact distances.
- **Local broadcasting (hobbyist compilation, AOTR):** Casey's first station was 5 W on 1573 kHz AM (1961), now "Radio COLD" on 102.5 FM, with coverage that "reached 250km for expeditions". Mawson's first was 5 W on 1570 kHz (1955), now 16 W FM [S61]. This is consistent with the ice ground-wave calculations of the first report (inf).
- **Dumont d'Urville.**
  - The station (Île des Pétrels, Terre Adélie, 20–30 winterers) hosts TAAF radio and postal services, and L'Astrolabe sails between Hobart and DDU [S62].
  - FT4YM amateur operation from Concordia and DDU (UNVERIFIED).
  - **No IPEV or Australian HF-link performance data for Hobart–DDU were found** (dead end at the sources).
- **Perth-based and Hobart-based Antarctic radio stations.** Hobart-based: AAD headquarters at Kingston, Hobart [S27]. Perth-based: only the historical Wireless Hill station. A present-day dedicated Perth- or Hobart-based Antarctic HF station was not found.

---

## 6. Bottom line (evidence-only; inferences flagged)

**Hobart–DDU / Hobart–Denison is the easier link; Perth–Casey is harder; Perth–Mawson and Perth–Davis are the hardest.**

**Hobart–DDU / Denison (2,681–2,698 km).**
- It is easier mainly because it is shorter, so it can use the natural two-hop geometry at about 20° takeoff, and because the Hobart end is at −54° AACGM, well below the main auroral oval.
- With 1 kW and +6 dBi at both ends it gives 22–24 h any-band on both models, in both months, at all solar levels, in quiet or rural noise. With 5 kW and +6 dBi it gives 22–24 h in every case, and 24 h in nearly all.
- A 100 W station with +6 dBi gives 17–24 h in quiet noise and 6–23 h in rural noise. A simple 100 W 0 dBi station fails: V 3 h in January, P.533 9–11 h in January and 2–13 h in July in quiet noise, and 0 h in rural noise.
- Weak-signal digital at 100 W 0 dBi is 22–24 h in every case.
- Bands to plan: 5–10 MHz in January days (7.1 and 10.1 MHz 14–24 h), 3.5–7.1 MHz in July (14–24 h each), 14 MHz and above only near solar maximum.
- Reliability estimate (inf): about 85–95% voice and about 92–98% weak-signal digital per year for a staffed 1 kW +6 dBi installation, falling in polar night and at solar minimum.

**Perth–Casey (3,834 km).**
- It sits at the one-hop limit, so two hops are required. 1 kW and +6 dBi gives 21–24 h on both models.
- At 1 kW and 0 dBi it is only 11–23 h; at 100 W and +6 dBi 14–24 h; at 100 W and 0 dBi 0–7 h.
- A 5 kW broadcast-class sender at 0 dBi gives 16–24 h in quiet noise and 9–22 h in rural noise. 5 kW with +6 dBi gives 17–24 h in rural noise.
- Weak-signal digital at 100 W 0 dBi works 18–24 h even in rural noise, so a digital link is practical for a simple station.
- Reliability estimate (inf): about 75–90% voice and about 88–96% digital with automatic band selection.

**Perth–Mawson (5,209 km) and Perth–Davis (4,727 km).**
- These need two or three hops at 7–9° takeoff. At 1 kW and +6 dBi voice gives only 12–24 h (Mawson January V 12–16, P 24; July V 23–24, P 16–22). A 5 kW +6 dBi sender is needed for most cases to reach 20 h or more.
- Mawson is in the night-side auroral band at −71° and has only about 3 h of daylight in July.
- Both are poor choices for a settled voice link; digital is workable (24 h at 100 W +6 dBi in most cases).

**Power, antenna and noise lessons (calc).**
- Antenna gain is worth more than power: +6 dBi at 100 W beats 1 kW at 0 dBi on the Hobart legs and roughly matches it on Perth–Casey.
- Quiet-site noise discipline matters: rural noise removes the 100 W 0 dBi voice link everywhere.
- Weak-signal digital modes turn a 0–10 h voice link into a 22–24 h link for a simple 100 W station, at the cost of text-speed data (the required S/N is lowered from 45 to 15 dB-Hz, a 30 dB difference, calc).

**Correlated blackout.** All the Antarctic-end links share the same polar-cap exposure at the Antarctic end. A PCA event interrupts every Casey, DDU and Denison link at once, and no choice of Australian sender cures it. The only mitigation documented by BoM is a path that avoids the polar region [S14] (inf).

---

## 7. Contradictions, unverified items and log

- **VOACAP versus P.533** disagree on the MUF peak for Perth–Casey (V up to 20 MHz, P up to 14 MHz in January SSN 5) and on rural-noise voice (Perth–Casey, 100 W +6 dBi, January: V 0–7, P 4–7 h). On the Hobart legs they agree within about 2 h except for the 1 kW 0 dBi January case (V 14–21, P 24).
- **Distance to Casey:** my calculation 3,834 km against "about 3,880 km due south of Perth" [S58].
- **1978 telex circuit and Casey relay hub:** appeared in search summaries of AAD pages, but the fetched page text did not contain it. I treat it as UNVERIFIED.
- **UNVERIFIED items:** the AAD 500 W 1948 transmitters, planned Hobart–Casey aircraft HF use, VK0 20 m and 40 m historical contacts, FT4YM at DDU, and all PCA event-duration statistics.
- **Dead ends:** documented Hobart–DDU HF performance (IPEV or AAD); a present-day Perth- or Hobart-based Antarctic radio station; published auroral-absorption statistics for Casey, Davis and Mawson; the VK0 amateurs' power levels and contact distances.
- **Searches this session** (exact strings abbreviated): "ANARE Casey Davis Mawson HF radio communications Australia history Casey relay hub 1978…", "Dumont d'Urville station radio communications HF Hobart Australian Antarctic Division IPEV…", "\"ANARE communications\" 1947 1985 antarctica.gov.au history communications HF radio Mawson radphone Casey Sydney telex 50 band", "VK0 amateur radio Casey OR Davis OR Mawson Antarctica contacts Perth Western Australia 20 metres OR 40 metres…", "Australian Antarctic Division HF radio network Hobart Kingston radio room field party HF schedule…", "Dumont d'Urville Hobart radio amateur FT0 OR FT8 OR \"Terre Adélie\" HF contacts Australia Hobart…".
- **Process note:** the first model pass produced empty VOACAP results (the absolute-path call failed). I re-ran VOACAP with the working relative-path script and verified that no empty cases remain.

### New sources (all accessed 2026-10-04)
- [S58] DX-World, Two VK0 stations on air from Australian Antarctica: https://www.dx-world.net/two-vk0-stations-on-air-from-australian-antarctica/
- [S59] AAD, The wireless of Wireless Hill: https://www.antarctica.gov.au/about-antarctica/history/communications/the-wireless-of-wireless-hill/
- [S60] AAD, ANARE communications 1947–1985: https://www.antarctica.gov.au/about-antarctica/history/communications/telecommunications/ and Satellite communications: https://www.antarctica.gov.au/about-antarctica/history/communications/satellite-communications/
- [S61] Australian Antarctic Broadcasting Stations (AOTR, hobbyist): https://www.australianotr.com.au/australian-antarctic-broadcasting-stations.html
- [S62] IPEV, Dumont d'Urville Station: https://institut-polaire.fr/en/antarctica/the-dumont-durville-ddu-station/
- Earlier sources [S14, S15, S17, S27, S28, S38, S41, S55, S57] as in the previous reports.
