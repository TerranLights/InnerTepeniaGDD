<!-- ⚠ PARTLY SUPERSEDED (2026-10-04): the agent later found that every VOACAP per-band table in this report was shifted by one column. See Section 0 of Research_Logs/Radio_Physics_Followup2_Trunk_Peninsula_to_Casey_2026-10-04.md for the corrected tables. P.533, MUF, ground-wave, geomagnetic, terrain and noise results here are unaffected; any-band hour counts changed little. Do not quote the per-band VOACAP hour counts from this file. -->

<!-- Log written 2026-10-04: the research agent's follow-up report, extracted verbatim from its transcript (not re-typed). Parts: (1) Pergamino to Signy, 807 km; (2) a relay on Elephant or Clarence Island; (3) long legs to Santa Luce. Companion to Radio_Physics_Peninsula_2026-10-04.md. (calc) = the agent's own calculation (VOACAP, ITU-R P.533-14, NTIA LFMF, GEBCO, AACGM-v2/IGRF-14); VOACAP and P.533 share the same foF2 maps and disagree on absorption/noise: P.533 is the conservative bound on some paths and VOACAP on others. UNVERIFIED = seen only in a search summary. The later trunk-chain request (Peninsula to Utstein to Mawson to Casey) is NOT covered in this report. -->

# Follow-up report: Pergamino–Signy, Elephant/Clarence relay, Santa Luce legs

Accessed 2026-10-04. Source numbers [S#] refer to the table at the end. (calc) marks my own calculation. UNVERIFIED marks facts seen only in a search summary or a Wikipedia-derived lead.

**Methods, same as the first report.**
- **Geometry and ground wave:** haversine with R = 6371 km; GEBCO-2020 profiles of 150 samples (250 for paths over 1,000 km); NTIA LFMF (P.368-10) with Millington mixed-path correction.
- **HF models:** VOACAP (voacapl 16.1207W, CCIR coefficients) and ITURHFProp (P.533-14 with the P.372 noise library). 26 legs, each run for 144 scenarios per model:
  - months: Jan and Jul;
  - SSN: 5, 60 and 160;
  - power: 10 W, 100 W and 1 kW;
  - antennas: 0 and +6 dBi at both ends (isotropic plus gain);
  - noise: quiet-rural and rural;
  - traffic: voice and weak-signal digital.
- **Voice vs. digital:** voice is 45 dB-Hz in VOACAP and 10 dB S/N in 3 kHz in P.533. Digital is 15 dB-Hz, which is −20 dB in 3 kHz in P.533 and about FT8/WSPR class.
- **Noise:** quiet-rural is −164 dBW/Hz at 3 MHz; rural is −150 (P.372-13 constants, calc).
- **"Usable":**
  - VOACAP: REL ≥ 0.8 and MUFday ≥ 0.5.
  - P.533: BCR ≥ 80%.
  - Cells below read "V/P" (VOACAP/P.533) in usable hours per 24 h. All hours are UTC; local solar time at about 55°W is UTC − 3.7 h.

**Caveats on the models.**
- **The two models are not independent on the ionosphere.** Their MUFs agree to within 1 MHz (for example, Pergamino–Signy July SSN 60: 3.7–9.4 MHz in VOACAP and 3.7–9.5 in P.533) because both use the same CCIR/URSI foF2 maps, which are sparsely constrained in Antarctica. They differ in absorption, noise and mode handling. I treat P.533 as the conservative bound and VOACAP as the optimistic one, and I quote both.
- **Neither model includes auroral or polar-cap absorption events or the Weddell Sea Anomaly explicitly.** Those are treated separately in Section 1.5 and Part 3.
- **VOACAP at 2.5 MHz in daytime is non-physical.**
  - It shows 59 dB-Hz at 2.5 MHz while 3.5 MHz collapses to about 0 dB-Hz. At night VOACAP and P.533 agree closely (61–69 dB-Hz).
  - The MUFday ≥ 0.5 filter removes the artifact hours, so VOACAP 2.5 MHz daytime hours should be trusted less than the P.533 ones.
  - Correction to my first report: its low-band counts used that same filter and are conservative for VOACAP 2.5 MHz in daytime.
- **The digital results are mode-existence limited.** The −20 dB threshold is so low that availability is set by the MUF, not by SNR.
- **GEBCO-2020 fails over Elephant and Clarence Islands.**
  - Cells at Pardo Ridge and the Point Wild area read about 1 m. The Mount Pendragon cell reads 678 m (the literature gives about 975 m), and the Mount Irving cell reads 188 m (literature 1,950 m).
  - I therefore use literature summit heights (Section 2.2). Those are Wikipedia/UK-APC values (UNVERIFIED), because the SCAR gazetteer is a JavaScript app I could not query.

---

## PART 1. Pergamino → Signy, 807 km

### 1.1 Geometry, sea fraction, terrain, horizon (calc; GEBCO-2020, 251 samples at 3.2 km)
- **Distance:** 806.8 km.
- **Sea fraction:** 96.0% (241 of 251 samples).
- **Land segments:**
  - km 5–27: Livingston Island at the transmitting end, up to 485 m along the path.
  - km 801: Laurie Island (Signy) at the receiving end, 18 m at the sample.
- **Water depth:** minimum −3,161 m; 65% of the path is deeper than 1,000 m (open Scotia/Weddell water).
- **Distance and radio horizon:** the path is about 20 times the 10 m/10 m radio horizon of 26 km (4.12(√10 + √10), k = 4/3 [S11]).
- **Earth bulge:** the earth bulge at mid-path is d²/(8kR) = 9.6 km (calc), so line of sight would need about 9.6 km masts at both ends (calc). Line of sight is impossible, even from the 2,382 m Anvers summit class of site.

### 1.2 MF ground wave (NTIA LFMF; sea σ = 5 S/m, εr = 70; heights 10 m / 2 m; short vertical monopole radiating the stated power)

Field strength at 806.8 km, and range to thresholds over a homogeneous sea path (calc):

| Case | E at 807 km, all-sea | Range to 54 / 40 / 20 dBµV/m, all-sea | Millington, Livingston land as polar ice (3e-4) | Millington, Livingston land as rock (2e-3) |
|---|---|---|---|---|
| 0.9 MHz, 1 kW | 31.6 dBµV/m | 319 / 614 / 1,080 km | 11 | 20 |
| 0.9 MHz, 10 kW | 41.6 | 526 / 843 / 1,321 km | 21 | 30 |
| 0.9 MHz, 50 kW | 48.6 | 682 / 1,008 / 1,492 km | 28 | 37 |
| 1.0 MHz, 1 kW | 30.7 | 314 / 600 / 1,050 km | n/a | n/a |
| 1.0 MHz, 10 kW | 40.7 | 515 / 822 / 1,284 km | n/a | n/a |
| 1.0 MHz, 50 kW | 47.7 | 665 / 981 / 1,450 km | n/a | n/a |
| 3.5 MHz, 100 W | 5.5 dBµV/m | 129 / 298 / 585 km (735 km to 10 dBµV/m, 891 km to 0) | −23 | −17 |

- **Mixed-path correction:** the 26 km of Livingston land at the transmit end costs 10 to 20 dB at 0.9 MHz. A 50 kW transmitter on the shoreline therefore delivers 28 to 37 dBµV/m in the mixed-path case, not 48.6.
- **Millington method:** the multi-section form uses the forward and reverse averages from the same LFMF tables (calc).
- **Antenna efficiency:** LFMF assumes the stated power is radiated. An antenna on ice or rock without a counterpoise radiates less, so subtract the efficiency loss from every row (inf).

**Planning thresholds:** ITU-R BS.703 gives MF reference-receiver sensitivity of 60 dBµV/m, with 54 and 40 also supported [S12]. The all-sea 10 kW case (41.6) meets only the lenient 40 value. The 54 and 60 values need more than 50 kW even over all-sea.

**Expected receive noise at Signy (P.372 library, receiver at −60.72, −45.60, SSN 60):**
- **At 1.0 MHz (proxy for 0.9, which the library rejects):**
  - atmospheric noise FaA: 9.5–48.5 dB (Jan), 41–61 dB (Jul);
  - man-made noise FaM: 53.6 dB quiet-rural, 67.2 dB rural;
  - total FamT: quiet-rural 53.6–56.5 (Jan) and 55.4–61.6 (Jul); rural 67.3–67.4 (Jan) and 64.9–68.7 (Jul).
- **Equivalent field in a 9 kHz AM channel** (En = Fa + 20 log f + B − 95.5 [S8]):
  - quiet-rural −2.4 to +0.5 dBµV/m (Jan) and −0.5 to +5.7 (Jul);
  - rural +9.0 to +12.7 dBµV/m.
- **At 3.5 MHz, 3 kHz bandwidth:**
  - quiet-rural: −10.7 to −5.5 dBµV/m (Jan), −8.9 to +1.1 (Jul);
  - rural: +1.8 to +5.3.
  - Total FamT is 39–44 dB (Jan) and 41–51 dB (Jul) quiet-rural, or 52–55 dB rural.
- **Reading:** July atmospheric noise is higher than January at both frequencies, because the model's lightning sources are mostly in the northern summer hemisphere.
- **Consequence for 100 W at 3.5 MHz over water:** the all-sea 5.5 dBµV/m gives an S/N of about 11 to 17 dB (quiet-rural) or about 0 to 4 dB (rural) in 3 kHz (calc). In practice the mixed-path loss of −17 to −23 dBµV/m puts the signal 20 to 25 dB below the noise, so ground wave does not carry 100 W voice at 3.5 MHz over this path.

### 1.3 HF skywave, Pergamino–Signy, both models

**MUF ranges (both models):**

| Month, SSN | Basic MUF (VOACAP / P.533) |
|---|---|
| Jan, SSN 5 | 7.4–9.2 / 7.8–10.3 MHz |
| Jan, SSN 60 | 8.5–10.0 / 9.2–11.2 MHz |
| Jan, SSN 160 | 10.1–11.5 / 11.1–12.6 MHz |
| Jul, SSN 5 | 3.9–7.8 / 3.9–7.8 MHz |
| Jul, SSN 60 | 3.7–9.4 / 3.7–9.5 MHz |
| Jul, SSN 160 | 3.3–12.5 / 3.3–13.3 MHz |

- The January daily maximum falls at 15–17 UTC and the minimum at 6–10 UTC.
- The July minimum is at 07 UTC, just before sunrise (13:20 UTC, below).

**Usable hours per 24 h, 100 W, 0 dBi, V/P, bands 2.5 / 3.5 / 5.0 / 7.1 / 10.1 / 14.2 MHz:**

Voice, quiet-rural noise:

| Case | Per-band V/P | Any band V/P |
|---|---|---|
| Jan SSN 5 | 17/16, 12/24, 15/24, 24/24, 24/4, 0/0 | 24/24 |
| Jan SSN 60 | 15/13, 10/21, 13/24, 16/24, 24/12, 0/0 | 24/24 |
| Jan SSN 160 | 5/11, 8/14, 11/24, 16/24, 20/24, 18/0 | 20/24 |
| Jul SSN 5 | 24/16, 24/17, 24/5, 9/4, 4/0, 0/0 | 24/21 |
| Jul SSN 60 | 24/15, 22/17, 24/4, 10/7, 7/0, 0/0 | 24/23 |
| Jul SSN 160 | 20/7, 18/9, 17/5, 12/6, 9/6, 6/0 | 24/18 |

Voice, rural noise:

| Case | Per-band V/P | Any band V/P |
|---|---|---|
| Jan SSN 5 | 9/7, 8/10, 12/17, 17/24, 24/4, 0/0 | 24/24 |
| Jan SSN 60 | 7/6, 7/9, 10/14, 14/24, 24/5, 0/0 | 24/24 |
| Jan SSN 160 | 0/4, 3/7, 6/11, 9/22, 13/24, 4/0 | 13/24 |
| Jul SSN 5 | 6/0, 19/2, 24/1, 9/1, 4/0, 0/0 | 24/3 |
| Jul SSN 60 | 16/0, 17/3, 20/1, 10/0, 7/0, 0/0 | 24/4 |
| Jul SSN 160 | 6/0, 16/0, 14/1, 8/2, 9/1, 6/0 | 24/3 |

Digital, rural noise:

| Case | Per-band V/P | Any band |
|---|---|---|
| Jan SSN 5 | 17/24, 16/24, 20/24, 24/24, 24/24, 0/24 | 24/24 |
| Jan SSN 60 | 16/24, 14/24, 16/24, 24/24, 24/24, 0/24 | 24/24 |
| Jan SSN 160 | 16/19, 10/24, 12/24, 16/24, 24/24, 19/24 | 24/24 |
| Jul SSN 5 | 24/20, 24/24, 24/24, 9/12, 4/5, 0/0 | 24/24 |
| Jul SSN 60 | 24/18, 24/20, 24/24, 10/13, 7/8, 0/5 | 24/24 |
| Jul SSN 160 | 24/16, 20/18, 21/22, 12/13, 9/10, 6/8 | 24/24 |

- Digital with quiet-rural noise gives 24 h on at least one band in every case in both models.

**Any-band voice hours across the power/gain matrix, rural noise, V/P:**

| Month, SSN | 10 W, 0 dBi | 10 W, +6 | 100 W, 0 | 100 W, +6 | 1 kW, 0 | 1 kW, +6 |
|---|---|---|---|---|---|---|
| Jan SSN 5 | 2/0 | 24/24 | 24/24 | 24/24 | 24/24 | 24/24 |
| Jan SSN 60 | 2/0 | 24/24 | 24/24 | 24/24 | 24/24 | 24/24 |
| Jan SSN 160 | 0/0 | 14/24 | 13/24 | 20/24 | 20/24 | 23/24 |
| Jul SSN 5 | 5/0 | 24/19 | 24/3 | 24/24 | 24/24 | 24/24 |
| Jul SSN 60 | 3/0 | 24/8 | 24/4 | 24/24 | 24/24 | 24/24 |
| Jul SSN 160 | 1/0 | 24/11 | 24/3 | 24/24 | 24/24 | 24/24 |

- With quiet-rural noise, 10 W at 0 dBi gives 24/20 (Jan SSN 5), 24/1 (Jul) and 11/16 (Jan SSN 160) V/P hours. +6 dBi each end lifts nearly all cells to 24/24.
- Digital at 10 W and 0 dBi rural gives 24 h in both models in every scenario except Jan SSN 160 in VOACAP (21 h).

**Best time windows (UTC), SSN 60, 100 W, 0 dBi (VOACAP | P.533; wrapped windows, for example 22–11 = 22 to 11 next day):**

Voice, quiet-rural:
- January:
  - 5.0 MHz: 22–10 | all hours.
  - 7.1 MHz: 20–11 | all hours.
  - 10.1 MHz: all hours | 01–03 and 12–20.
- July:
  - 2.5 MHz: all hours | 22–12.
  - 3.5 MHz: 17–14 | 21–13.
  - 7.1 MHz: 12–21 | 13–19.
  - 10.1 MHz: 13–19 | none.

Voice, rural:
- January:
  - 3.5 MHz: 01–07 | 01–09.
  - 5.0 MHz: 23–08 | 23–12.
  - 7.1 MHz: 21–10 | all hours.
  - 10.1 MHz: all hours | 13–16.
- July:
  - 3.5 MHz: 19–11 | 10–11 and 22.
  - 5.0 MHz: 18–13 | 12 only.
  - 7.1 MHz: 12–21 | none.
  - With +6 dBi, July rural windows widen to 2.5 MHz 21–12, 3.5 MHz 21–13, 7.1 MHz 13–19 and 10.1 MHz 13–19 (P.533).

Digital, rural, July:
- 2.5 MHz: all | 20–13.
- 3.5 MHz: all | 19–14.
- 5.0 MHz: all | all.
- 7.1 MHz: 12–21 | 10–22.
- 10.1 MHz: 13–19 | 13–20.
- 14.2 MHz: none | 14–18.

**Pattern.**
- **Winter (July):** low bands (2.5–5 MHz) at night and mornings, 7–10 MHz only roughly 12–21 UTC (the daytime; the model sunrise is 13:10 UTC at Pergamino, so this is about 4 h of day plus the pre-dawn).
- **Summer (January):** 5–10 MHz carries all 24 h, with 7.1 MHz as the workhorse.

### 1.4 NVIS vs low-angle F2 at 807 km (calc geometry; models agree)

| Layer height | Take-off elevation | Incidence angle | MUF ≈ f₀ × sec i |
|---|---|---|---|
| F2, 300 km | 34.2° | 52.2° | 1.63 × foF2 |
| F2, 250 km | 29.5° | 56.9° | 1.83 × foF2 |
| E, 110 km | 13.3° | 73.1° | 3.43 × foE |

- The one-hop F2 maximum at 0° elevation is 3,836 km; one hop is geometrically fine.
- **There is no skip-zone problem for frequencies at or below the path MUF.** The skip zone only matters above foF2: a signal at f > foF2 has a skip distance with sec i = f/foF2. For example foF2 = 3 MHz and f = 5 MHz gives sec i = 1.67, skip about 830 km, which would blind exactly this link (inf).
- **Antenna:** a 807 km path wants energy at about 30–35° elevation. A high-angle NVIS antenna (very low dipole or inverted-V, maximum above 70° [S13]) has less gain at that angle than a dipole at 0.25–0.5 λ height. NVIS-optimized antennas are the right tool for 0–about 450 km (elevation above about 50° needs d below about 450 km) (calc).
- **Best band by season (models):**
  - Summer: 5–10 MHz all day, with 7.1 MHz the anchor; 3.5 MHz only at night.
  - Winter: 2.5–3.5 MHz at night and morning (MUF 3.3–3.9 MHz before dawn), 5–7 MHz in the 12–21 UTC window.
- **The anchor frequencies must change with the day.** Use the 0.85 × MUF working-frequency rule [S21] (for the 3.7 MHz pre-dawn July MUF this is about 3.1 MHz, so 3.5 MHz is above MUF at that hour).

### 1.5 Day/night, geomagnetic latitude, auroral and polar-cap exposure

| Site | AACGM-v2 (110 km, 2025.5) | Dipole (IGRF-14 2025.0) |
|---|---|---|
| Pergamino | −49.7° | −53.6° |
| Signy | −49.7° | −52.3° |
| Path midpoint | −49.8° | −53.1° |

All figures are (calc).
- **Position:** the whole path is sub-auroral and mid-latitude. NOAA's storm table has aurora overhead at about 50° geomagnetic latitude at G3 (Kp 7), about 200 events or 130 days per 11-year cycle [S15] (about 12 days/yr, calc).
- **Polar cap:** not exposed. Polar-cap absorption (PCA) acts at polar-cap latitudes [S14, S41]; the Peninsula is on the fringe only for the biggest events (inf).
- **Day/night at the ends (calc, geometric, refraction included):**
  - 15 Jan: Pergamino sunrise 06:43, sunset 01:38 (next day) UTC, day 18.9 h; Signy sunrise 06:05, sunset 00:17, day 18.2 h.
  - 15 Jul: Pergamino sunrise 13:16, sunset 18:58, day 5.7 h; Signy sunrise 11:58, sunset 18:18, day 6.3 h.
  - There is no polar day or night on this path.
- **Weddell Sea Anomaly:** both Signy (45.6°W) and the path lie inside the WSA region (55–75°S, 80–30°W) [S22]. In summer the anomaly puts the F2 peak at night, so night-time MUF is higher than the maps give and higher bands stay open longer after dusk (inf; the CCIR maps likely understate it). At solar minimum the effect is weakest.
- **Measured foF2 near the path:** at Vernadsky in June 2019 (solar minimum, F10.7 about 70) NmF2 stayed under 2×10⁵ cm⁻³, giving foF2 ≤ about 4.0 MHz (calc from f = 8.98√N), roughly consistent with the July model MUF of about 3.3–3.9 MHz before dawn [S23].

### 1.6 Bottom line, Pergamino → Signy
**Could a settled community with 100 W and a simple antenna hold a reliable link?**
- **Yes, with scheduling and a frequency plan, for data and for voice in most conditions.** The honest numbers:
  - **Quiet-rural noise:** both models give some band for 24 h at 100 W isotropic in January, and 18–24 h in July (P.533 18–23 h).
  - **Rural noise:** January still gives 24 h; July is the weak case, with P.533 giving only 3–4 h of voice per day at 100 W and 0 dBi. VOACAP gives 24 h. The models bracket it.
  - **Weak-signal digital:** 24 h in both models even at 10 W.
- **Frequencies and times:**
  - **Summer (Jan):** 7 MHz around the clock, 10 MHz as the daytime fallback (about 12–20 UTC), 5 MHz and 3.5 MHz at night (about 22–09 UTC).
  - **Winter (Jul):** 2.5–3.5 MHz overnight (about 20–12 UTC), 5 MHz near 12–14 UTC and 21 UTC, and 7–10 MHz between about 12 and 21 UTC. On the winter day the anchor is 7.1 MHz.
  - **Solar-cycle effect:** at SSN 160 in January, 14 MHz opens (18 h in VOACAP) and 2.5–3.5 MHz is only 5–11 h.
- **At 10 W:** voice fails except with +6 dBi at both ends in quiet-rural noise (and even then P.533 gives 1–22 h across seasons); rural-noise voice is 0–5 h at 0 dBi. Weak-signal digital and a store-and-forward text link still work all 24 h.
- **At 1 kW (or 100 W with +6 dBi each end):** voice is 24 h in both models on both noise levels, except January SSN 160 rural 0 dBi (20–23 h).
- **Rule of thumb:** a directive antenna at each end is worth about 10 times the power (calc, from the +6 dBi columns).

**AM (MF) reception at Signy from a transmitter at Pergamino.**
- **Ground wave, 0.9 MHz.** All-sea field strength at 807 km: 1 kW 31.6, 10 kW 41.6, 50 kW 48.6 dBµV/m. With the Livingston land section the values fall to 11 to 37 dBµV/m (Section 1.2).
- **Against the noise:** quiet-rural total noise in a 9 kHz channel is −2 to +6 dBµV/m (Jan/Jul) and rural +9 to +13. A 10 kW all-sea signal is therefore 36 to 44 dB above quiet noise, but only 21 to 30 dBµV/m with the land penalty, which is about 15 to 30 dB above noise.
- **Against broadcast planning values (60/54/40 dBµV/m [S12]):** 10 kW does not meet 54 or 60 at all. It meets the lenient 40 only if the whole path is sea. 50 kW with a shoreline antenna gives 49 over water or 28 to 37 with Livingston land.
- **Result:** daytime AM ground-wave reception at Signy is possible only as DX-grade reception with a good receiver on a quiet site, not as a consumer broadcast. Site the transmitter at the water's edge with a sea-facing counterpoise, and use at least 10 kW. 1 kW is not viable (11 to 32 dBµV/m).
- **Night:** MF sky wave adds a strong, fading contribution at night (day sky wave is about 30 dB lower, practical MF sky wave is a night effect [S24]). I did not compute the sky-wave field; I could not retrieve the Rec. 435/P.1147 formula, so night coverage is unquantified (UNVERIFIED).

---

## PART 2. Relay on Elephant or Clarence Island

### 2.1 Site facts (verified where marked)
- **Point Wild:** 61°06'S 54°52'W; HSM 53 (bust of Capt. Pardo, monolith, plaques) [S49]. Landings are "opportunistic only, typically one small boat", often prohibited by conditions; the beach is reefy with swell; calving hazard from the adjacent Furness Glacier [S49]. A statement that it is landed on "perhaps once every five years" is UNVERIFIED (operator summary).
- **Pardo Ridge:** 61.125°S 54.883°W, 853 m (Wikipedia; UNVERIFIED), about 3 km behind Point Wild. **Mount Pendragon:** 61.25°S 55.233°W, about 975 m (UNVERIFIED; GEBCO 678 m). **Mount Irving (Clarence):** 61.264°S 54.142°W, 1,950 m (UNVERIFIED; "recent research" suggests 1,772 m).
- **Cape Lookout:** the IAATO primary landing is 61°16'45.9"S 55°12'53.7"W, a small rocky beach exposed to west/southwest swell, with surge through the Rowett Island channel and glacier-snout collapse risk, better suited to small-boat cruising [S50]. **Your Cape Lookout coordinates (−61.08, −55.37) match the Brazilian Goeldi refuge, not the landing.** COMNAP lists "Emílio Goeldi", Brazil, a seasonal refuge, open, established 1988, at −61.133, −55.35 [S51]. A seasonal facility for up to six researchers is UNVERIFIED (Wikipedia). The Point Wild you gave (−61.10, −54.85) matches the HSM 53 site to about 1 km.
- **Hampson Cove HSM 74** (wreck), southwest Elephant Island (Wikipedia; UNVERIFIED).
- **Clarence Island:** no COMNAP facility and no ATS visitor site found. Cape Bowles supports over 100,000 pairs of chinstrap penguins (an Important Bird Area; UNVERIFIED) [Key Biodiversity Areas result].
- **Weather:** Elephant Island winds frequently exceed 50 kn with peaks near 100 kn in storms (UNVERIFIED, meteoblue/Wikipedia-level).

### 2.2 Legs: distance, sea fraction, horizon (calc; GEBCO for profiles, literature summits for heights)

Your distances all check: Elephant (Point Wild) to Pergamino 337 km, Machu Picchu 221, Signy 501, Esperanza 279; Clarence to Pergamino 371, Machu Picchu 256, Signy 456.

| Leg | km | Sea % | Max land along path (m) | Relay summit (m) | LOS horizon: summit to 10 m dest / to dest on local peak | Terrain-checked clearance, summit to 10 m dest |
|---|---|---|---|---|---|---|
| Elephant PW → Pergamino | 337 | 60 | 496 | 853 | 134 / 224 km | −1,540 m |
| → Contrapunto | 242 | 66 | 535 | 853 | 134 / 220 | −673 |
| → Machu Picchu | 221 | 71 | 647 | 853 | 134 / 220 | −783 |
| → Esperanza | 279 | 96 | 79 | 853 | 134 / 220 | −745 |
| → Signy | 501 | 99 | 1 | 853 | 134 / 206 | −3,276 |
| Clarence → Pergamino | 371 | 89 | 639 | 1,950 | 195 / 285 | −1,155 |
| → Contrapunto | 276 | 85 | 295 | 1,950 | 195 / 282 | −482 (+26 m with dest on peak) |
| → Machu Picchu | 256 | 80 | 499 | 1,950 | 195 / 282 | −560 (−14 m with dest on peak) |
| → Esperanza | 289 | 88 | 257 | 1,950 | 195 / 282 | −607 (−131 m with dest on peak) |
| → Signy | 456 | 99 | 34 | 1,950 | 195 / 267 | −2,156 |
| Cape Lookout (Goeldi) → Pergamino | 313 | 69 | 614 | 975 (Pendragon, about 17 km away) | 142 / 232 | −1,596 |
| → Machu Picchu | 196 | 83 | 652 | 975 | 142 / 228 | −717 |
| → Signy | 528 | 93 | 1 | 975 | 142 / 214 | −3,625 |
| Esperanza → Signy | 663 | 92 | 549 | n/a | LOS impossible | n/a |
| Marambio → Signy | 687 | 99 | 88 | n/a | impossible | n/a |
| Esperanza → Pergamino | 191 | 68 | 1,206 | n/a | equal masts of 1,310 m needed | n/a |
| Esperanza → Contrapunto | 160 | 84 | 547 | n/a | equal masts of 670 m needed | n/a |
| Machu Picchu → Signy | 701 | 97 | 153 | n/a | impossible | n/a |

- **Summit-to-summit** on the two islands: Pardo Ridge (853 m) to Mount Irving (1,950 m) = 302 km line of sight (calc).
- **Destination peaks used:** the highest GEBCO cell within 30 km (Pergamino 612 m, Contrapunto 569 m, Esperanza 572 m, Signy 414 m, Machu Picchu 569 m). These are grid-smoothed values (calc).
- **What this means.** A relay on Pardo Ridge reaches the sea-level KGI/Livingston stations only to about 134 km, so the 221–337 km legs fail by line of sight; it works to KGI only if the destination is also on a peak (221 km needs 220 km: borderline, and over a rim of Livingston terrain). Mount Irving is the only candidate with line of sight to the KGI summits (256–276 km: +26 m and −14 m clearance, with a 1,950 m glaciated peak as the site). For Signy (456–528 km) there is no VHF/UHF line of sight from any summit, and over-horizon diffraction loss at 156.8 MHz is at least 29 to 32 dB over free space (knife-edge lower bound, calc; the actual smooth-earth loss is larger).
- **MF ground wave** (0.9 MHz, sea-only | Millington with rock land), dBµV/m:

| Leg | 1 kW | 10 kW | 50 kW | 3.5 MHz 100 W (sea-only / with ice land) |
|---|---|---|---|---|
| EPW–Pergamino | 53 | 63 | 70 | 37 / −10 |
| EPW–Machu Picchu | 59 | 69 | 76 | 46 / 18 |
| EPW–Esperanza | 56 | 66 | 73 | 41 / 35 |
| EPW–Signy | 45 | 55 | 62 | 26 / 8 |
| CLA–Signy | 47 | 57 | 64 | 29 / 9 |
| ECL–Signy | 44 | 54 | 61 | 24 / −23 |
| Esper–Signy | 38 | 48 | 55 | 15 / −10 |
| Maram–Signy | 37 | 47 | 54 | 13 / −6 |
| Esper–Pergamino | 61 | 71 | 78 | 48 / −2 |
| Esper–Contrapunto | 63 | 73 | 80 | 51 / 14 |

  - Sea-only values; ice-land Millington values are lower (full table in the computation log). So an island AM relay delivers about 45 to 47 dBµV/m (1 kW) at Signy from Elephant or Clarence, against 32 from Pergamino direct, a gain of about 14 dB (calc). A 10 kW relay gives 55 to 57 dBµV/m, meeting the 54 criterion at Signy.
- **HF over the relay legs (any-band hours, voice, 100 W 0 dBi, SSN 60, V/P):**
  - quiet-rural: 24/24 on all legs in January; in July 24/24 on most (100 W) with P.533 24 on the shortest;
  - rural: January 24/24; July 24 (VOACAP) and 15 to 24 (P.533) hours.
  - The NVIS legs of 160–337 km have best bands of 2.5–7 MHz; the 456–528 km legs to Signy are the 5–10 MHz class.
- **Median best-band S/N (100 W, 0 dBi, quiet-rural, SSN 60, P.533 | VOACAP, 3 kHz):**

| Leg | Jan P / V | Jul P / V |
|---|---|---|
| Pergamino–Signy 807 km | 32 / 34 | 22 / 35 |
| EPW–Signy 501 km | 34 / 41 | 25 / 37 |
| EPW–Pergamino 337 km | 33 / 43 | 26 / 38 |
| Esper–Signy 663 km | 33 / 39 | 23 / 36 |
| Esper–Perg 191 km | 33 / 44 | 27 / 39 |

  - **A relay barely changes the S/N** (1 to 8 dB, calc). HF at 300 to 800 km is a single-hop F2/E path whose loss grows slowly with distance.

**Chain vs direct (voice, both legs required in the same hour = an in-band repeater), any-band hours V/P, SSN 5/60/160, 100 W 0 dBi, rural noise:**

| Route | Jan SSN 5 / 60 / 160 | Jul SSN 5 / 60 / 160 |
|---|---|---|
| Pergamino–Signy direct | 24/24, 24/24, 13/24 | 24/3, 24/4, 24/3 |
| via Esperanza (Esper–Perg + Esper–Signy) | 24/24, 24/24, 16/24 | 24/11, 24/5, 24/8 |
| via Elephant PW | 24/24, 24/24, 22/24 | 24/17, 24/13, 24/10 |
| via Clarence | 24/24, 22/24, 22/24 | 24/18, 24/12, 24/10 |

(With +6 dBi at each end, or with 1 kW, all four routes give 24/24 in all cases except direct Jan SSN 160 at 20 h.)

### 2.3 Answers

**(a) What a relay on Elephant or Clarence buys physically versus the direct 807 km link.**
- **Power, antenna and noise:** little on HF (1 to 8 dB median S/N, calc). The main HF gain is in the hardest case: rural noise in July, where voice hours at 100 W and 0 dBi rise from 3–4 (P.533) to 10–18 via the island (calc).
- **Band choice:** shorter legs allow lower bands (2.5–5 MHz at night) with a lower MUF requirement, so the relay's HF legs need a less demanding frequency plan than the 807 km direct hop.
- **MF:** an island AM relay at 10 kW reaches Signy at 55 to 57 dBµV/m (sea paths), about 14 dB above the Pergamino direct transmitter, which is the one clear physical gain (calc). VHF/UHF line of sight reaches Signy from nowhere, but Mount Irving to the KGI summits works marginally.
- **Reliability:** HF is ionosphere-dependent, and neither model includes absorption events (Section 1.5). A relay does not remove that. The relay adds a new single point of failure on an exposed island.
- **Store-and-forward:** weak-signal digital already runs 24 h even at 10 W on the direct 807 km path (Section 1.3), so store-and-forward on an island relay buys nothing for text. A relay only helps voice at low power or in rural-noise July.

**(b) What it would take to build and keep a relay running.**
- **Access:** Point Wild landings are opportunistic, swell-limited and rare [S49]. Cape Lookout is swell-exposed and wildlife-limited [S50]. Clarence has no documented landing site. Heavy gear for a ridge or peak site would need a helicopter or a favorable-weather boat transfer (inf; I found no source on helicopter access).
- **Existing foothold:** the only facility is the seasonal Brazilian Goeldi refuge at −61.133, −55.35 [S51], which could hold a battery or a hand-serviced radio but not an installation without its operator.
- **Protected-site constraint:** Point Wild is HSM 53. A relay on Pardo Ridge would sit about 3 km behind it, and any installation would need environmental assessment under the Environmental Protocol (general knowledge, UNVERIFIED in this session).
- **Wind and rime:** peaks near 100 kn (UNVERIFIED). Rime accumulation and mast leaning are documented failure modes of unattended polar stations [S53]; an iced whip or thin leading edge fails first (UNVERIFIED, generic).
- **Power budget (calc, my assumptions):** a 10 W average load (HF receive with periodic transmit, plus controller) is 240 Wh/day, about 88 kWh/yr. A 14-day no-sun storm reserve is about 3.4 kWh, roughly 280 Ah at 12 V, before cold derating. The Spanish Livingston station's own numbers show the scale: a transmitter drew 96 W, sleep 7.2 W, and a 110 Ah battery gave about two weeks of hourly transmissions [S21]. Winter daylight at this latitude is about 6 h with a low sun (calc, Section 1.5), and the Spanish station notes winter power is "restricted… served only by batteries charged by wind and solar" [S20].
- **Precedents and failure rates.**
  - The Antarctic automatic weather station lessons paper gives the planning rule that "mean time between failures of more than five times the mean time between visits is a reasonable planning strategy… for many stations this demands MTBF > 5 years" and lists rime, mast leaning and instrument failure [S53].
  - AAD mountain-top solar/wind VHF repeaters are routine [S27]. McMurdo runs five hilltop repeaters (Taylor, Wright, Terror, Aurora, Brooke) [S2].
  - AWS GC41 has run since October 1984 without maintenance access; a remote geophysical observatory review says "in typical years, failure occurs in two or three system subassemblies" with single points of failure (both UNVERIFIED search summaries). Instrument failures include sensor freezing and frost-covered screens [S58].
  - **I found no quantified annual failure rate for unattended Antarctic relay or repeater sites.** That is a documented dead end (Section 4).

**(c) Does a manned Esperanza trunk make an island relay unnecessary?**
- **For HF, yes.** Esperanza (manned, with existing power and antennas, 191 km from Pergamino and 663 km from Signy) chains to the same effect as an Elephant relay. For the hardest case (rural noise, July, 100 W, 0 dBi) the Esperanza chain gives 5–11 h versus direct 3–4 h and an island chain 10–18 h (P.533/VOACAP mix, above); with +6 dBi or 1 kW all routes give 24 h. Esperanza–Signy alone (663 km) gives any-band voice hours of 24/22 (quiet, July, 100 W 0 dBi) and 24/5 (rural, July), and 24/24 with +6 dBi (V/P). Weak-signal digital runs 24 h at 10 W.
- **For non-ionospheric trunks (MF broadcast, VHF line of sight) the island still has a unique role,** but only Mount Irving (1,950 m) gives any line of sight to the KGI peaks, at marginal clearance. Esperanza gives none to Signy and only 190 and 160 km to Pergamino and Contrapunto, where a mountain-top or high-mast repeater is required (equal masts of 1,310 m and 670 m).
- **Conclusion (inf):** a settled community that can afford power at Esperanza gets a more reliable and maintainable trunk from Esperanza than from an unattended island, unless it needs MF broadcast coverage of Signy from an exposed coast or a Mount Irving VHF/UHF link.

---

## PART 3. Legs to Santa Luce (−73.05, −13.4167)

### 3.1 Geometry (calc)
- **Distances:** Signy–Santa Luce 1,918 km, Esperanza–Santa Luce 2,025 km, Marambio–Santa Luce 1,943 km, Santa Luce–Halley 484 km, Santa Luce–Troll 543 km, Santa Luce–Neumayer 319 km, Santa Luce–Sanay (SANAE IV, −71.667, −2.833) 388 km. Esperanza–Signy–Santa Luce chain 663 + 1,918 = 2,581 km (+27% against the direct hop).
- **Sea fraction (GEBCO):** Signy–SL 93% (Weddell Sea, with 123 km of ice sheet at the Santa Luce end, max 332 m); Esperanza–SL 90%; Marambio–SL 90%; Santa Luce to Halley 2% (all ice sheet, max 981 m); to Troll 0% (max 2,313 m); to Neumayer 0% (max 642 m); to Sanay 0% (max 1,558 m).
- **Ground wave:** useless. Over 1,900 km the field is below 0 dBµV/m even at 50 kW (−14 to +3 dBµV/m all-sea) and the Millington mixed values are −35 to −138; over the ice-sheet regional legs the Millington values are −32 to +17 dBµV/m (50 kW at 0.9 MHz, rock land: 3 to 24; ice land: −15 to +7).
- **Take-off geometry (calc):**

| Distance | 1 hop F2 300 km: elevation / sec | 2 hops: hop length, elevation / sec |
|---|---|---|
| 1,918 km | 12.7° / 2.76 | 959 km, 29.3° / 1.81 |
| 2,025 km | 11.6° / 2.83 | 1,012 km, 27.8° / 1.87 |
| 2,581 km | 7.0° / 3.14 | 1,290 km, 21.5° / 2.18 |

- **Basic MUF over the long legs:** Jan SSN 60 about 14–16 MHz around the clock (Signy–SL VOACAP 14.1–16.1, P.533 13.4–15.7 MHz); Jul SSN 60: 5.4 at 23 UTC to 14.3 at 15 UTC (VOACAP) and 4.6–13.8 (P.533). At SSN 5 in July the MUF is only 4.4–5.5 MHz at night.

### 3.2 Geomagnetic position and the polar exposure at the Santa Luce end (calc, AACGM-v2; dipole from IGRF-14 2025.0)

| Site | AACGM | Dipole | Dipole L |
|---|---|---|---|
| Santa Luce | −62.2° | −67.0° | 6.54 |
| Halley | −62.9° | −68.2° | 7.25 |
| Troll | −63.3° | −67.9° | 7.04 |
| Neumayer | −61.1° | −65.3° | 5.73 |
| Sanay (SANAE IV) | −62.4° | −66.9° | 6.49 |
| Belgrano II | −64.2° | −69.8° | 8.41 |
| Signy | −49.7° | −52.3° | 2.68 |
| Esperanza | −50.6° | −54.5° | 2.96 |
| Marambio | −51.4° | −55.3° | 3.09 |
| Midpoint Signy–Santa Luce | −56.3° | −60.0° | n/a |
| Midpoint Esperanza–Santa Luce | −57.1° | −61.4° | n/a |
| Midpoint Santa Luce–Halley | −62.6° | −67.7° | n/a |

- Your dipole −67 at Santa Luce is confirmed and equals Halley's −68.2 within 1.2°. The literature L for Halley is about 4.5–4.6 (UNVERIFIED search snippets) against my dipole L of 7.25, because dipole L overstates it; the AACGM value of −62.9° corresponds to L ≈ 4.5 (calc: L = 1/cos²(62.9°) is 4.8), so use AACGM for the physical exposure.
- **Exposure frequency (NOAA, per 11-year cycle [S15], converted to per-year averages, calc):**

| Event | Per cycle | Per year (avg.) |
|---|---|---|
| Kp 5 (G1) | 900 days | 82 days |
| Kp 6 (G2) | 360 days | 33 days |
| Kp 7 (G3) | 130 days | 12 days |
| Kp 8–9− (G4) | 60 days | 5.5 days |
| Kp 9 (G5) | 4 days | 0.4 days |
| S1 radiation storm (≥ 10 pfu) | 50 events | 4.5 events |
| S2 | 25 | 2.3 |
| S3 | 10 | 0.9 |
| S4 | 3 | 0.27 |
| S5 | under 1 | under 0.1 |

  Cycle averages concentrate in the declining phase and near maximum, so the next two to three years (declining toward the 2030 minimum, NOAA predicts SSN 9.3 for October 2030 [S17]) are above average (inf).
- **Auroral oval:** the oval's equatorward edge descends to about 65–75° geomagnetic latitude depending on activity [S38]. Santa Luce at −62° AACGM sits just equatorward of the quiet-time oval and inside it on disturbed nights; Signy and the Peninsula (−50°) are outside except at about G3 and above (NOAA: aurora at about 50° geomagnetic at G3 [S15]). The midpoint (−56) is the region the sky-wave control points fall in; storms at G2+ (aurora at about 55°) reach it (inf).
- **Trough and absorption physics (Northern Hemisphere analog, auroral zone paths at about 64–66° invariant, URSI GA 2011 [S54]):** in winter at night under quiet conditions (Kp 0–1) the main ionospheric trough spreads over the auroral zone, creating "the most difficult conditions" for HF; auroral absorption "significantly impacts the quality of the information transmission" and cuts HF communication probability. Frequencies selected correctly can improve quality. This is the physical context for a −62° AACGM end (inf).
- **Absorption scaling (UNVERIFIED, standard riometer scaling, f⁻²):** 1 dB at 30 MHz is about 36 dB at 5 MHz and about 9 dB at 10 MHz, vertical incidence (calc); oblique paths are worse. When the oval is active the lower bands at the Santa Luce end close first and the 10–14 MHz bands remain longest. On summer days (midnight sun for 90 days at −73°, calc) daytime D-layer absorption adds a second high-latitude loss at the low bands.
- **Polar cap absorption at −62°:** PCA acts at polar-cap latitudes, with a dayside cutoff near 66.8° and nightside near 70.8° magnetic latitude in one riometer analysis, and extends equatorward in larger events (UNVERIFIED search snippets). Santa Luce at −62° is equatorward of the typical cutoff, so it feels only the larger (S2+, about 2.3 per year) events (inf). A PCA "causes a HF radio blackout for trans polar circuits and can last several days" [S41]; the NOAA scale puts polar-region HF effects at "degraded" for S3 and "blackout" for S4 [S15].
- **Weddell Sea Anomaly:** Signy end is inside the WSA region; Santa Luce (13.4°W) is outside. In summer nights the anomaly raises the F2 peak at the Signy end, which helps higher bands from the Signy side after dusk (inf; the models use the global maps).

### 3.3 HF models, long legs (V/P usable hours per 24 h, 100 W, 0 dBi)

**Signy–Santa Luce (1,918 km), per band 2.5 / 3.5 / 5 / 7.1 / 10.1 / 14.2:**

Voice, quiet-rural:

| Case | Per-band V/P | Any band V/P/both |
|---|---|---|
| Jan SSN 5 | 0/0, 0/5, 0/11, 7/21, 4/24, 0/5 | 7/24/7 |
| Jan SSN 60 | 0/0, 0/1, 0/9, 5/16, 4/23, 3/19 | 6/24/6 |
| Jan SSN 160 | 0/0, 0/0, 0/5, 3/11, 7/23, 3/23 | 7/24/7 |
| Jul SSN 5 | 0/7, 14/11, 20/10, 20/0, 7/0, 0/0 | 24/12/12 |
| Jul SSN 60 | 1/0, 13/12, 16/9, 20/1, 9/0, 1/0 | 24/13/13 |
| Jul SSN 160 | 2/0, 12/2, 14/3, 11/5, 7/2, 3/2 | 20/10/7 |

Voice, rural: 0 h in both models in every case.

Digital, quiet-rural and rural: 24 h in both models on at least one band in all cases. Per band in January SSN 60 (rural): 2.5 MHz 16/11, 3.5 MHz 5/24, 5 MHz 8/24, 7.1 MHz 13/24, 10.1 MHz 22/24, 14.2 MHz 24/24.

Esperanza–Santa Luce (2,025 km) and Marambio–Santa Luce (1,943 km) behave the same within 1 to 3 hours.

**Voice, 100 W any-band, quiet-rural, power/gain matrix (Signy–SL), V/P:**

| Month, SSN | 10 W, 0 dBi | 10 W, +6 | 100 W, 0 | 100 W, +6 | 1 kW, 0 | 1 kW, +6 |
|---|---|---|---|---|---|---|
| Jan SSN 5 | 0/0 | 10/24 | 7/24 | 24/24 | 24/24 | 24/24 |
| Jan SSN 60 | 0/0 | 8/24 | 6/24 | 24/24 | 23/24 | 24/24 |
| Jul SSN 5 | 0/0 | 24/15 | 24/12 | 24/24 | 24/23 | 24/24 |
| Jul SSN 60 | 0/0 | 24/17 | 24/13 | 24/24 | 24/24 | 24/24 |

- **Rural noise:** voice needs 1 kW or +6 dBi at each end: 100 W with +6 dBi gives 11–13 V / 24 P hours in January and 24/19–24 in July; 1 kW at 0 dBi gives 6–7/24 January, 23–24/18–21 July.
- **Digital:** 24 h at 10 W and 0 dBi, both models.
- **Model disagreement:** P.533 is the optimistic one on this long path in January (24 h of voice at 100 W where VOACAP gives 6–7), and VOACAP is optimistic in July (20–24 h against 10–13). The "both agree" count (last column) is 6–7 h in January and 7–13 h in July at 100 W, 0 dBi, quiet-rural noise. The MUFs agree (Section 0); the disagreement is absorption and noise treatment.
- **Best windows (SSN 60, 100 W, +6 dBi, quiet voice, UTC, VOACAP | P.533):**
  - January: 10.1 MHz 20–09 | all; 14.2 MHz all | all; 7.1 MHz 21–08 | all.
  - July: 3.5 MHz 18–10 | 20–11; 5.0 MHz 15–13 | 01–11 and 19–22; 7.1 MHz all | 09–14 and 17–20; 10.1 MHz 09–20 | 13–18; 14.2 MHz 12–19 | none.
- **Median best-band S/N (100 W, 0 dBi, quiet-rural, SSN 60, 3 kHz), P.533 | VOACAP:** Signy–SL Jan 24 | 20, Jul 18 | 25 (against 32–34 and 22–35 for Pergamino–Signy), so the Santa Luce hop is 8 to 14 dB weaker than the 807 km hop (calc).

**Regional NVIS and short legs from Santa Luce (V/P any-band hours, 100 W, 0 dBi):**

| Leg | km | Voice quiet Jan / Jul | Voice rural Jan / Jul | Digital rural |
|---|---|---|---|---|
| SL–Halley | 484 | 24/24 · 21–24/11–21 | 1–8/12–18 · 6–15/0–1 | 24/24 |
| SL–Troll | 543 | 24/24 · 22–24/12–21 | 1–6/12–20 · 7–13/0–1 | 24/24 |
| SL–Neumayer | 319 | 24/24 · 24/13–21 | 2–7/10–20 · 6–15/0–4 | 24/24 |
| SL–Sanay | 388 | 24/24 · 23–24/9–21 | 1–6/9–18 · 6–15/0–3 | 24/24 (23 in Jul P.533) |

- **Basic MUF on the regional legs:** Jan SSN 60 about 6–8 MHz; Jul SSN 5 only 1.8–3.7 MHz (SL–Halley, 1.9 MHz at 21–22 UTC), SSN 60 2.4–5.6 MHz, SSN 160 3.3–8.9 MHz. In July at solar minimum the usable band is at the bottom of the HF range (1.8–3.5 MHz), so antenna size and the 160/80 m bands matter.
- **Rural noise in winter kills voice** on these legs (0–1 h in P.533), and 100 W with +6 dBi or 1 kW recovers 17–24 h.
- **Ground wave and ice:** none; all four regional legs are over the ice sheet, so NVIS is the only voice mode (inf).

### 3.4 Chain via Signy vs direct Esperanza → Santa Luce (calc, voice, both legs required in the same hour; V/P any-band hours)

| Case (SSN 5; 60; 160) | Direct Esperanza–SL, Jan | Chain via Signy, Jan | Direct Esperanza–SL, Jul | Chain via Signy, Jul |
|---|---|---|---|---|
| 100 W 0 dBi quiet | 4/24; 2/24; 5/23 | 7/24; 6/24; 7/24 | 24/11; 23/9; 19/9 | 24/12; 24/13; 20/10 |
| 100 W +6 dBi quiet | 24/24 all | 24/24 all | 24/24 all | 24/24 all |
| 1 kW 0 dBi quiet | 24/24; 22/24; 24/24 | 24/24; 23/24; 24/24 | 24/22; 24/24; 24/24 | 24/23; 24/24; 24/24 |
| 100 W +6 dBi rural | 11/24; 11/24; 8/24 | 13/24; 11/24; 11/24 | 24/18; 24/24; 23/24 | 24/19; 24/23; 24/24 |
| 1 kW 0 dBi rural | 0/24; 2/24; 2/24 | 6/24; 6/24; 7/24 | 24/12; 23/20; 22/20 | 24/18; 23/21; 22/19 |
| 100 W 0 dBi digital rural | 24/24 | 24/24 | 24/24 | 24/24 |

- **Result:** the chain via Signy is never worse than the direct 2,025 km hop in the models and sometimes gains up to 6 hours per day (VOACAP, 1 kW rural, January); P.533 shows no difference. The Signy relay's leg Esperanza–Signy is a low-risk 663 km hop (any-band 24 h at 100 W, quiet-rural; July P.533 rural 5 h at 100 W 0 dBi, 20 h with +6 dBi). The longer total path (2,581 km vs 2,025 km) costs nothing in HF terms because each leg is shorter than the single-hop limit and neither leg needs more than one hop (calc), while Signy is itself a seasonal station (COMNAP lists it seasonal [S51]) and sits at −50°, outside the auroral oval, so a Signy relay keeps the sub-auroral half of the chain out of the oval.
- **Chain with a store-and-forward node at Signy** relaxes the same-hour requirement entirely, so for digital traffic it is only as limited as each leg (24 h each) (inf).

### 3.5 Documented HF performance in the Weddell sector (what exists)
- **Neumayer III permanent WSPR beacon DP0GVN** (TU Munich/Univ. Bremen/DARC, from January 2018): 5 W into a 5 m vertical, multiband receiver monitoring up to eight bands from 160 to 6 m, several hundred reports per hour into WSPRnet [S56]. A 2021 DARC presentation reports WSPR detection from DP0GVN to a New Zealand receiver over more than 7,500 km, and some paths from Australia, the Canary Islands (EA8) and South America [S57]. "Initial findings… indicate that the majority of reported spots originate from stations in the Northern Hemisphere" (UNVERIFIED search summary of the project text).
- **McMurdo–South Pole oblique HF** (a high-latitude analog, not the Weddell sector): no signals below 4.1 MHz "due to absorption and reduced transmitter efficiency", stable E layer, spread F, 12 frequencies between 2.6 and 7.2 MHz [S55].
- **Not found:** published HF performance for Halley, SANAE or Belgrano; a BAS or AWI paper on Weddell-sector HF links (the AWI Neumayer WSPR paper "Investigation of 10 MHz propagation from DP0GVN to GM0HCQ/MM" was not retrievable); a polar-day balloon WSPR paper (MDPI Atmosphere 2023, 14, 1118) was blocked (403) and is UNVERIFIED. Signy-specific HF measurements: not found.

### 3.6 Bottom line, Santa Luce
**Could a settled community hold a Signy–Santa Luce HF link?**
- **Data and weak-signal digital (WSPR/FT8 class): yes, all 24 h at 10 W** in both models in all seasons and solar-cycle states, with the caveat that the models contain no auroral or PCA events.
- **Voice at 100 W with simple antennas:** marginal. Quiet-rural noise gives only 6–7 h/day in January and 10–13 h in July by the "both models agree" count (24 h in P.533 January, 24 h in VOACAP July). With rural noise voice is 0 h. Voice becomes reliable at 100 W with +6 dBi at both ends in quiet noise (24/24) or at 1 kW in quiet noise. With rural noise it needs both 1 kW and gain antennas.
- **Frequencies and times:** January 10–14 MHz (the MUF is 13–19 MHz around the clock), with 7 MHz at night; July 3.5–5 MHz overnight (about 18–11 UTC), 7 MHz midday (about 09–20 UTC), 10 MHz about 09–20 UTC, 14 MHz about 12–19 UTC, and in SSN 5 July nights only 2.5–5 MHz.
- **Interruptions.** Using the NOAA frequencies converted to per-year averages (Section 3.2): about 82 disturbed days per year at Kp ≥ 5, 33 at Kp ≥ 6 and 12 at Kp ≥ 7, with the oval overhead at Santa Luce for most nights at Kp ≥ 4 to 5 (inf, from −62° against an equatorward edge of about 65° at quiet times falling to about 55° by G2 [S15, S38]). Polar-cap events large enough to affect −62° occur at the S2 and above rate, about 2.3 per year, lasting from hours to days (NOAA S1–S5 per cycle [S15]; "can last several days" [S41]).
  - On those days expect the 3.5–7 MHz bands to degrade or fail at the Santa Luce end first (f⁻² scaling), leaving 10–14 MHz, then nothing during a major PCA.
  - A realistic planning statement is: a few percent of days see a severe interruption, tens of days see partial degradation (inf; derived from the NOAA counts, not from a measured Santa Luce record).
- **Chain vs direct:** use the chain Esperanza → Signy → Santa Luce rather than the direct 2,025 km hop for voice. The models show it is equal or better (up to +6 h/day), the first leg is a safe 663 km hop, and Signy is outside the oval. The second leg still carries the full auroral exposure, so the chain does not remove the interruptions. It adds a relay and a failure point at Signy. For digital traffic the direct hop already works 24 h at 10 W, so the chain is only worth it for voice or when an operator is on hand at Signy.
- **Regional NVIS (Halley, Neumayer, Troll, Sanay):** reliable for quiet-rural noise and 100 W in January (24/24 h); fragile in winter at solar minimum (1.8–3.7 MHz MUF) and impossible for voice in rural noise in July without 1 kW or gain antennas. All regional legs are over ice, so there is no ground wave.

---

## 4. Contradictions, assumptions, computation and search log

**Contradictions and corrections.**
1. VOACAP vs P.533 disagree in opposite directions on different paths: P.533 is lower for 807 km rural July (3–4 h vs 24 h), higher for the 1,918–2,025 km January legs (24 h vs 4–7 h), and lower for July Santa Luce (9–13 h vs 19–24 h).
2. The two models share foF2 maps, so agreement on MUF is not independent confirmation.
3. VOACAP daytime 2.5 MHz anomaly (above); first-report low-band counts are conservative.
4. Your Cape Lookout coordinates are the Goeldi refuge, not the landing site (Section 2.1).
5. GEBCO heights at Elephant and Clarence contradict the literature summits (Section 0).
6. Mount Irving is 1,950 m in the main entry and 1,772 m in "recent research"; older sources say 2,300 m (UNVERIFIED).
7. The AWS lessons paper says MTBF should exceed five times the visit interval; AAD routinely uses unattended repeaters. These are consistent only if the repeater is visited annually.

**Assumptions.**
- Isotropic ±6 dBi antennas; 100 W means transmitter power, not radiated; LFMF assumes full radiation of the stated power; sea σ = 5 S/m, εr = 70; polar-ice land σ = 3×10⁻⁴, rock 2×10⁻³; terrain sampling 3.2 km (≤ 150 m on short legs) so narrow ridges can be missed; Elephant and Clarence summit heights are Wikipedia/UK-APC values; the Goeldi relay is assumed to use Mount Pendragon (about 17 km away) as its summit; AM at 0.9 MHz uses 1.0 MHz noise as a proxy because the P.372 library rejects 0.9; 24 h any-band counts mean at least one tested band is usable each hour, which in practice requires frequency changes.

**Computation log (all in the session scratchpad).** `legworker.py`/`legvoa.py`/`legsum.py` (HF matrices, 26 legs); `legprof.py` (GEBCO profiles); `leglos.py` (horizons, clearance, knife-edge bounds); `legmf.py` (LFMF with Millington); AACGM and dipole scripts; sunrise/sunset script; the P.372-library noise runs.
- **Snag, VOACAP:** the first batch run produced all-zero VOACAP results because I passed an absolute run path; voacapl has a fixed-length path buffer. I re-ran all legs with relative paths and got 144 valid scenarios per leg.
- **Snag, P.372 library:** it rejects 0.9 MHz (minimum 1.0 for noise) and 1.6 for the HF engine.

**Searches run this round (exact strings, abbreviated for the long ones).**
- Pardo Ridge height / Mount Irving height / Point Wild HSM landing / Clarence Island landing and protected status / Elephant Island wind and Goeldi refuge.
- unattended AWS failure rate / remote Antarctic observatory and repeater reliability.
- Halley HF and riometer; Neumayer HF and WSPR (DP0GVN) and paper searches; SANAE/Halley/Neumayer/Belgrano HF absorption; WSA effect on HF; PCA and solar proton statistics; auroral-oval latitude.

**Dead ends.**
1. SCAR gazetteer (JavaScript app): summit heights unverified at the primary.
2. Quantified failure rates for unattended polar relay or repeater sites: not found (died at the sources; only MTBF planning guidance and qualitative failure lists).
3. BAMS 2012 (AWS 30 years), the Rec. 435/P.1147 MF sky-wave formula, the D-RAP documentation PDF, the swsc-journal 2022 occurrence-rate paper, the MDPI polar-day balloon paper and the Liu 2024 McMurdo–South Pole paper: blocked or 404, so quantitative PCA-per-year statistics and the night MF sky-wave field were not obtained.
4. Published HF performance for Halley, SANAE, Belgrano and Signy; BAS or AWI Weddell-sector HF papers (died at the query and the sources).
5. Clarence Island landing and facilities: nothing found.
6. A documented Santa Luce auroral-absorption record: none exists (the station is a project coordinate).

**Source table for this round (accessed 2026-10-04; S1–S48 are as in the first report).**

| # | Source | URL |
|---|---|---|
| S49 | ATS visitor site guideline, Point Wild (Site 38), HSM 53 | https://www.ats.aq/devAS/Ats/Guideline/3bc3c80e-15ca-494d-a178-66b972951d93 |
| S50 | IAATO visitor site guide, Cape Lookout, Elephant Island (ATCM 46) | https://documents.ats.aq/ATCM46/att/ATCM46_att123_e.pdf |
| S51 | COMNAP Antarctic Facilities master list (Goeldi refuge, Machu Picchu, Signy) | https://github.com/PolarGeospatialCenter/comnap-antarctic-facilities |
| S52 | Wikipedia leads (UNVERIFIED): Pardo Ridge, Mount Irving, Mount Pendragon, Elephant Island, Clarence Island, Point Wild, Refuge Emílio Goeldi | https://en.wikipedia.org/wiki/Pardo_Ridge ; https://en.wikipedia.org/wiki/Mount_Irving ; https://en.wikipedia.org/wiki/Elephant_Island |
| S53 | Box et al., Automatic Weather Stations on Glaciers: Lessons | https://polarmet.osu.edu/jbox/pubs/AWS_on_glaciers_-_Lessons_Box_Anderson_Broeke.pdf |
| S54 | Blagoveshchensky & Sergeeva, Impact of the auroral ionosphere on HF radio propagation, URSI GA 2011 | https://www.ursi.org/proceedings/procGA11/ursi/GP2-5.pdf |
| S55 | First observations of the McMurdo–South Pole oblique ionospheric HF channel, Atmos. Meas. Tech. 13, 3023 (2020) | https://amt.copernicus.org/articles/13/3023/2020/ |
| S56 | ARRL, Permanent WSPR beacon in Antarctica now on the air | https://www.arrl.org/news/permanent-wspr-beacon-in-antarctica-now-on-the-air |
| S57 | Westphal DJ4FF, HamSCI 2021 poster ("Geocaching in the Ionosphere") | https://hamsci.org/sites/default/files/publications/2021_HamSCI/20210320_1700z-Robert_Westphal_DJ4FF.pdf |
| S58 | Zhang et al., AntAWS dataset, ESSD 15, 411 (2023) | https://essd.copernicus.org/articles/15/411/2023/ |
| S59 | NOAA SWPC Space Weather Scales (G, S, R tables) | https://www.spaceweather.gov/noaa-scales-explanation |
| — | Not fetched, cited from search summaries (UNVERIFIED): swsc-journal 2022 occurrence-rate paper (https://www.swsc-journal.org/articles/swsc/pdf/2022/01/swsc220003.pdf); MDPI Atmosphere 2023, 14, 1118 (https://www.mdpi.com/2073-4433/14/7/1118); Liu 2024 McMurdo–South Pole (https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2022RS007632); Key Biodiversity Areas Cape Bowles factsheet (https://www.keybiodiversityareas.org/site/factsheet/29448) | as listed |

No project files were edited. Scratch products, including the leg JSON files, are in the session scratchpad (`legs/*.json`, `legprof.json`, `legmf.json`, `leglos.json`).