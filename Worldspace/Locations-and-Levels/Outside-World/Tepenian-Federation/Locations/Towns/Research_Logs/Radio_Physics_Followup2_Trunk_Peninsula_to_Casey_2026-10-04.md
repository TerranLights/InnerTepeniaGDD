<!-- Log written 2026-10-04: the research agent's second follow-up report, copied verbatim from the saved tool-result file (not re-typed). It re-runs the Pergamino-Signy, Elephant/Clarence and Santa Luce legs and adds the Peninsula-Utstein-Mawson-Casey trunk. **SECTION 0 IS AN ERRATUM: every VOACAP per-band table in the first two radio reports was shifted by one column (values listed for a band were the next-lower band's); the tables in THIS report supersede them. P.533, MUF, ground-wave (LFMF), geomagnetic, terrain and noise results were not affected; any-band hour counts changed little.** (calc) = the agent's calculation; (inf) = inference; UNVERIFIED = search summary only. Polar-cap/auroral availability percentages are the agent's estimates, not measurements. -->

# Follow-up report: Pergamino–Signy, Elephant/Clarence relays, Santa Luce, and the Peninsula–Casey trunk

Same tools and conventions as the first report. All access dates are 2026-10-04. (calc) marks my own calculation, (inf) marks inference, and UNVERIFIED marks facts seen only in a search-engine summary. Nothing was written to the project; all work is in the session scratchpad.

---

## 0. ERRATUM — read this first

**Every VOACAP per-band table in my first report was shifted by one column, and it is superseded by the tables here.**
- VOACAP prints an extra leading "MUF column" before the first requested frequency. My parser read that column as the first frequency, so values for each listed band were really the next-lower band's values (the lowest band got the MUF-column value).
- **P.533-14, MUF values, ground-wave (LFMF), geomagnetic, terrain and noise results were NOT affected.** The "hours with any usable band" counts changed little.
- I found it when VOACAP showed a physically impossible 2.5 MHz SNR of about 59 dB-Hz at midday while 3.5 MHz showed about −3 dB-Hz.
- I verified the fix against VOACAP's own sample output (Tangier–Belgrade), then re-ran all 57 earlier legs, the new legs and the Palmer-based links.
- The first report also used SSN 5/50/100/160; the corrected tables here use SSN 5/60/160, and SSN 100 values lie between 60 and 160.
- Corrected statements that replace first-report text, VOACAP 100 W 0 dBi voice quiet-rural (calc):
  - **Palmer–Rothera, 361 km.** January SSN 5: 2.5, 3.5, 5 MHz usable 24, 24, 23 h. January SSN 160: 3.5, 5, 7.1 MHz usable 16, 24, 24 h (10 MHz not usable). July SSN 5: 2.5 MHz 24 h, 3.5 MHz 8 h, 5 MHz 0 h. July SSN 160: 24, 12, 9, 4 h on 2.5, 3.5, 5, 7.1 MHz.
  - **Palmer–Signy, 1,037 km.** January SSN 60: 7, 11, 14, 18, 17 h on 2.5, 3.5, 5, 7.1, 10.1 MHz (14.2 MHz 0 h). July SSN 5: 24 h on 2.5 and 3.5 MHz, 12 h on 5 MHz, 6 h on 7.1 MHz.
  - **Power/antenna sensitivity, VOACAP, rural noise, voice, SSN 60 (any-band hours/24; columns 10 W 0 dBi / 100 W 0 dBi / 1 kW 0 dBi / 100 W +6 dBi / 1 kW +6 dBi):**

| Link, month | 10 W | 100 W | 1 kW | 100 W +6 | 1 kW +6 |
|---|---|---|---|---|---|
| Palmer–Signy Jan | 0 | 14 | 24 | 24 | 24 |
| Palmer–Signy Jul | 0 | 24 | 24 | 24 | 24 |
| Rothera–Signy Jan | 0 | 2 | 24 | 24 | 24 |
| Rothera–Signy Jul | 0 | 22 | 24 | 24 | 24 |
| Palmer–Ushuaia Jan | 0 | 8 | 24 | 24 | 24 |
| Palmer–Ushuaia Jul | 0 | 24 | 24 | 24 | 24 |
| Palmer–Punta Arenas Jan | 0 | 1 | 24 | 24 | 24 |
| Palmer–Punta Arenas Jul | 0 | 16 | 24 | 24 | 24 |
| Palmer–Buenos Aires Jan | 0 | 0 | 20 | 24 | 24 |
| Palmer–Buenos Aires Jul | 0 | 0 | 0 | 7 | 24 |
| Palmer–McMurdo Jan | 0 | 0 | 0 | 0 | 24 |
| Palmer–McMurdo Jul | 0 | 0 | 0 | 1 | 17 |

  - **The qualitative conclusions of the first report stand:** 10 W is not enough for any link beyond about 400 km, 1 kW or +6 dBi is the transition for 1,000–1,400 km, and 3,400 km and beyond needs both.
  - **Corrected Livingston–Spain validation (SAS→Ebre, 12,710 km, Jan SSN 10, 250 W isotropic).** VOACAP median MUF is 13.8–14.1 MHz at 21–03 UTC, 8.1–8.6 MHz at 05–06 UTC and 19.6–23.3 MHz at 10–19 UTC. The measured availability above 95% on 8–10 MHz at 21–04 UTC [S20] is consistent with MUFday ≥ 0.9 there. The measurement showed under 20% availability at 10–19 UTC because the sounding band stopped at 16.5 MHz, below the MUF. VOACAP's SNR-based REL is pessimistic (0.0–0.4 at the 30 dB-Hz measured threshold), so VOACAP under-predicts the achieved SNR on this path, probably by antenna and receiver gain (inf).

**Model note.** VOACAP and P.533 both include only crude high-latitude absorption. Neither models polar-cap absorption events or auroral substorms. Those are treated separately in Section 4.

---

## 1. Pergamino–Signy (807 km), exact link

### 1.1 Distance, sea fraction, terrain, horizon
- **Great-circle distance 806.8 km** (calc, haversine R = 6371 km).
- **GEBCO-2020, 251 samples at 3.2 km** (OpenTopoData [S39]): 96% sea (241/251).
  - Land is only 5–27 km from Pergamino (Livingston Island's own interior, highest GEBCO cell 485 m on the path) and one sample at 801 km (Laurie Island, 18 m).
  - Deepest water is −3,161 m. About 65% of the path is deeper than 1,000 m.
  - The path lies about 3–4° away from Elephant Island; no land appears between 27 and 801 km.
- **Earth bulge** at the midpoint is d²/(8kR) with k = 4/3: 806.8²/(8 × 1.3333 × 6371) = **9.6 km** (calc). Equal masts of about 9.6 km each would be needed, so VHF/UHF line of sight is impossible.
- **Summit-to-summit** with Livingston about 1,700 m (UNVERIFIED) and Signy 414 m (GEBCO cell): 4.12(√1700 + √414) = **253 km**, far short of 807 km (calc).
- **Geomagnetic latitude (calc, AACGM-v2 at 110 km, 2025.5):** Pergamino −49.7°, Signy −49.7°, midpoint −49.8°. IGRF-14 dipole: −53.6° and −52.3°.

### 1.2 MF ground wave (NTIA LFMF = ITU-R P.368-10; sea σ = 5 S/m, εr = 70, heights 10 m / 2 m, radiated power into a short monopole) (calc)

| Case | Field at 806.8 km, sea-only (dBµV/m) | Distance to 54 dBµV/m | to 40 | to 20 |
|---|---|---|---|---|
| 0.9 MHz, 1 kW | **31.6** | 319 km | 614 km | 1,080 km |
| 0.9 MHz, 10 kW | **41.6** | 526 | 843 | 1,321 |
| 0.9 MHz, 50 kW | **48.6** | 682 | 1,008 | 1,492 |
| 1.0 MHz, 1 / 10 / 50 kW | 30.7 / 40.7 / 47.7 | 314 / 515 / 665 | 600 / 822 / 981 | 1,050 / 1,284 / 1,450 |
| 3.5 MHz, 100 W | **5.5** | 129 | 298 | 585 |

- Over sea at 3.5 MHz, 100 W reaches +10 dBµV/m at 735 km and 0 dBµV/m at 891 km (calc).
- **Mixed-path correction (Millington, calc).** If the transmitter sits where the path crosses about 22 km of Livingston land first, the field at 807 km (0.9 MHz, 1/10/50 kW) falls from 32/42/49 to 20/30/37 (rock land, σ = 2 mS/m) or 11/21/28 (ice land, σ = 0.3 mS/m). At 3.5 MHz 100 W it falls from 5 to −17 (rock) or −23 (ice) dBµV/m. A transmitter on the shore with a short land run keeps nearly the sea-only values (inf).
- **Receive noise at Signy (P.372 library, ITURHFProp noise sources, SSN 60) [S8, S39].**
  - At 1.0 MHz, atmospheric noise Fa is 9.5–48.5 dB through the day in January and 41–61 dB in July (highest at night). Man-made noise is 53.6 dB (quiet rural) or 67.2 dB (rural). Total Fam is 53.6–56.5 dB quiet and 67 dB rural in January, 55–62 dB quiet and 65–69 dB rural in July.
  - Converting with En = Fa + 20 log f + B − 95.5 [S8 eq. 7]: for AM (B = 9 kHz) the noise-limited field is **−2.4 to +0.5 dBµV/m (January) and −0.5 to +5.7 (July) quiet-rural**, and +9 to +12.7 dBµV/m rural.
  - At 3.5 MHz (3 kHz): En is −10.7 to −5.5 (Jan) and −8.9 to +1.1 (Jul) quiet, +1.8 to +5.3 rural.
  - The P.372 library accepts 1.0 MHz at minimum, so 0.9 MHz uses the 1.0 MHz value as proxy (error about 1 dB).
- So a 1 kW daytime AM ground wave at 31.6 dBµV/m gives about 34 dB S/N over quiet-rural noise and about 20 dB over rural noise in summer. In July the night atmospheric noise cuts that to about 26 dB (quiet) or 19 dB (rural). The ITU planning sensitivity for MF is 60 dBµV/m (54 and 40 also supported) [S12]; 31.6 dBµV/m is far below broadcast-quality, so 807 km is a fringe-listening distance, not coverage, at 1 kW. 10 kW lifts it to 41.6, just over the 40 dBµV/m level.

### 1.3 HF skywave, VOACAP and P.533 (V = VOACAP, P = P.533-14; REL ≥ 0.8 and f ≤ median MUF for VOACAP; BCR ≥ 80% for P.533; UTC)
Assumptions as before. Voice needs 45 dB-Hz (VOACAP) or 10 dB S/N in 3 kHz (P.533). Weak-signal digital needs 15 dB-Hz or −20 dB in 3 kHz (FT8-class). Quiet-rural noise is −164 dBW/Hz at 3 MHz; rural is −150.

**Baseline 100 W, 0 dBi, voice, quiet-rural (hours/24 per band V/P, columns 2.5, 3.5, 5, 7.1, 10.1, 14.2 MHz; any band V/P):**

| Month, SSN | Per band | Any band |
|---|---|---|
| Jan 5 | 12/16 15/24 24/24 24/24 0/4 0/0 | 24/24 |
| Jan 60 | 10/13 13/21 16/24 24/24 0/12 0/0 | 24/24 |
| Jan 160 | 8/11 11/14 16/24 20/24 18/24 0/0 | 20/24 |
| Jul 5 | 24/16 24/17 9/5 4/4 0/0 0/0 | 24/21 |
| Jul 60 | 22/15 24/17 10/4 7/7 0/0 0/0 | 24/23 |
| Jul 160 | 18/7 17/9 12/5 9/6 6/6 0/0 | 24/18 |

**Same, rural noise:** January 7–24 h (V 13–24, P 24); **July P.533 only 3–4 h per day** (V still 24). That is the main V/P disagreement: in July with rural noise at 100 W, 0 dBi, P.533 says voice mostly fails and VOACAP says it holds on 2.5–3.5 MHz.

**Digital, rural noise, 100 W 0 dBi:** any band 24/24 h in all 6 cases for both models. Per-band January: 2.5 MHz 10–16 h (V) up to 24 (P), 3.5 MHz 12–20 (V) / 24 (P), 5 and 7.1 MHz 16–24.

**Best UTC windows, voice, 100 W 0 dBi, quiet-rural (V | P):**

| Case | 2.5 | 3.5 | 5 | 7.1 | 10.1 |
|---|---|---|---|---|---|
| Jan SSN 60 | 23–08 \| 23–11 | 22–10 \| 19–15 | 20–11 \| all | all \| all | − \| 01–03, 12–20 |
| Jul SSN 60 | 17–14 \| 22–12 | all \| 21–13 | 12–21 \| 12–14, 21 | 13–19 \| 13–19 | − |
| Jan SSN 5 (about 2030) | 22–09 \| 22–13 | 21–11 \| all | all \| all | all \| all | − \| 15–18 |
| Jul SSN 5 (about 2030) | all \| 21–12 | all \| 21–13 | 12–20 \| 12–16 | 14–17 \| 14–17 | − |
| Jul SSN 160 | 19–12 \| scattered | 02–06, 09–13, 18–24 \| 01–02, 09–12, 21–23 | 11–22 \| 11–13, 21–22 | 12–20 \| 12–16 | 14–19 \| 14–19 |

**Median MUF (hourly range, V | P):** January 7.4–9.2 | 7.8–10.3 MHz at SSN 5, up to 10.1–11.5 | 11.1–12.6 at SSN 160. July 3.9 at 07 UTC rising to 7.8 at 15–17 UTC at SSN 5, and 3.3 up to 12.5–13.3 MHz at SSN 160 (calc).

**Power and antenna sensitivity, any-band hours/24 (V/P), voice, quiet-rural noise:**

| Month, SSN | 10 W 0 dBi | 10 W +6 | 100 W 0 | 100 W +6 | 1 kW 0 | 1 kW +6 |
|---|---|---|---|---|---|---|
| Jan 5 | 24/21 | 24/24 | 24/24 | 24/24 | 24/24 | 24/24 |
| Jan 160 | 11/16 | 20/24 | 20/24 | 24/24 | 23/24 | 24/24 |
| Jul 5 | 24/1 | 24/22 | 24/21 | 24/24 | 24/24 | 24/24 |
| Jul 160 | 22/1 | 24/24 | 24/18 | 24/24 | 24/24 | 24/24 |

Rural noise, voice: 10 W 0 dBi gives 0–5 h in both models; 10 W +6 dBi gives V 14–24 h but P 8–24 h in July (poor); 100 W +6 dBi and above give 24 h on both. Weak-signal digital at 10 W, 0 dBi is 21–24 h on VOACAP and 24 h on P.533 for all months and SSNs.

### 1.4 NVIS versus low-angle F2 at 807 km
Spherical-earth one-hop geometry (calc, layer 300 km): take-off elevation **34.2°**, incidence angle at the layer 52.2°, secant factor 1.63. For a 250 km F2: 29.5°, 56.9°, 1.83. For an E layer at 110 km: 13.3°, 73.1°, 3.43. Maximum one-hop F2 range at 0° elevation is 3,836 km (calc; the IPS value is "4000 km" [S14]).
- At 807 km a signal at frequency f ≤ MUF ≈ 1.63 foF2 is reflected by F2 at 34° elevation. There is no skip-zone problem at this distance for the working band, because the skip zone (typically 80–113 km inside the ground wave [S13]) is far shorter than 807 km.
- **NVIS antennas are the wrong choice here.** An NVIS dipole (maximum radiation 70–90° elevation [S13, S21]) has little gain at 34°, so a low-angle antenna is needed. The pure NVIS band (below foF2, up to about 250 km coverage [S21 design claim]) does not reach 807 km at useful signal. Frequencies below 3.5 MHz are the best winter bands, because they work through the long polar night with low absorption, but the antenna must radiate at about 35°, not vertically.
- **Best band by season (P.533 and VOACAP agree):**
  - January (polar-summer sunlit): 5–7 MHz (24 h); 3.5 MHz at night (22–10 UTC); 10 MHz only at SSN 60–160 and mostly 12–20 UTC.
  - July (3–6 h daylight at both ends): 2.5–3.5 MHz overnight and morning (21–13 UTC); 5–7 MHz only in the sunlit window 12–21 UTC and rarely at solar minimum.
- Sunrise/sunset (calc, geometric): 15 Jan Pergamino 06:43/01:38 UTC, Signy 06:05/00:17 UTC (day length 18.9 h / 18.2 h); 15 Jul Pergamino 13:16/18:58 UTC, Signy 11:58/18:18 UTC (5.7 h / 6.3 h).
  - The July sunlit window (12–19 UTC) is where 7 MHz appears and where D-layer absorption is highest on 2.5–3.5 MHz (the 2.5 and 3.5 MHz windows in July run 17–14 / 21–13 UTC, i.e. they close in the sunlit hours; this is the D-layer LUF effect [S14]).

### 1.5 Day/night, polar-cap and auroral risk for this path
- Both ends are at −50° AACGM, midpoint −50°. This is the sub-auroral mid-latitude zone, not the polar cap. The NOAA geomagnetic storm scale places aurora "as low as" about 50° geomagnetic latitude at G3 (200 events per cycle, 130 days per cycle) [S15], so the oval reaches this path at G3 or stronger, about 3.2% of days at the cycle average (calc: 130/4018 days). At G1–G2 the effect is "HF radio propagation can fade at higher latitudes" [S15].
- PCA exposure is small: it needs S4–S5 radiation storms (3 per cycle and under 1 per cycle) [S15] (inf).
- The Weddell Sea Anomaly (WSA) shifts the summer electron-density peak to night over this longitude (WSA region 55–75°S, 80–30°W) [S22], favoring higher frequencies after dusk in summer (inf).

### 1.6 Bottom line, Pergamino–Signy (inf from the calculations above)
- **A settled community can hold this link with 100 W and a simple antenna, but only on the right band and with a low-angle antenna.** In January use 5–7 MHz (24 h) with 3.5 MHz at night. In July use 2.5–3.5 MHz overnight to morning (about 21–13 UTC) and 5–7 MHz only in the short sunlit window 12–21 UTC. Plan for four frequencies and automatic link establishment (a time-of-day/season schedule).
- **At 100 W, 0 dBi, voice is marginal in rural-noise winter** (P.533 only 3–4 h/day). A quiet site or +6 dBi antenna restores 24 h. **Weak-signal digital at 10 W works 24 h in every case modeled.** **At 10 W voice it fails** (0–5 h on both models). **At 1 kW, 0 dBi, voice holds 24 h** on both models (except January SSN 160 at 23/24 h V).
- **MF AM reception at Signy from a Pergamino transmitter:** 1 kW at 0.9 MHz gives 31.6 dBµV/m by sea ground wave at 807 km (about 34 dB S/N in quiet summer, about 20 dB in rural noise). That is fringe/DX reception and with a land segment at the transmitter it falls to 11–20 dBµV/m. **10 kW gives 41.6 dBµV/m (just over the 40 dBµV/m planning level), 50 kW gives 48.6.** Night skywave (E-layer) adds range and fading but its field was not computed (the P.1147/Rec. 435 method was not obtained; NTIA states MF sky wave is practical only at night and about 30 dB lower by day [S24]). Daytime AM broadcast coverage of Signy from Pergamino therefore needs 10 kW or more at a shore site.

---

## 2. Elephant and Clarence Island relays; Esperanza as the Signy trunk

### 2.1 What is on the islands (checked)
- **Elephant Island:** ice-covered, mountainous, uninhabited; highest point Mount Pendragon about 975 m, Pardo Ridge about 853 m (Wikipedia/UK-APC, UNVERIFIED primary). **Point Wild** (61°05′53″S 54°51′39″W) holds Historic Site HSM 53 (bust of Captain Pardo, monolith, plaques) [S49 ATS guideline]; landing there is "often prohibited... opportunistic only, typically one small boat" (ATS guideline, via fetch summary) and tour sources say it is landed on perhaps once every five years (UNVERIFIED, tour-operator wording). **Cape Lookout** is on the south-west coast at 61°16′45.9″S 55°12′53.7″W (IAATO landing) [S50]; swell/surge from W and SW, shallow rocks, one rough path, icefall risk, a small beach often blocked by wildlife [S50]. My earlier "Cape Lookout −61.08, −55.37" coordinate you supplied does not match IAATO's −61.28, −55.21; my "ECL" legs use −61.1333, −55.35, which is the Brazilian **Goeldi refuge** position in the COMNAP dataset (seasonal, established 1988, operator Brazil; no power/elevation fields recorded) [S51]. HSM 74 (a wreck at Hampson Cove) also exists (Wikipedia, UNVERIFIED).
- **Clarence Island** (about 61.2°S 54.0°W, Mount Irving 1,950 m, older 2,300 m, "recent research" 1,772 m; Wikipedia, UNVERIFIED): Cape Bowles is an Important Bird Area with over 100,000 chinstrap pairs (UNVERIFIED, search summary). I found no station, refuge, visitor-site guideline or protected-area entry (COMNAP facilities dataset has none within the region except Goeldi, Signy/Orcadas and the KGI stations [S51]). Treat Clarence as unlandable by default (dead end: no landing-condition source found).
- **GEBCO cannot be used for summits here:** within 6 km of Pendragon the highest GEBCO cell is 678 m, of Mount Irving 188 m, of Machu Picchu 569 m (calc). I used literature summit heights, not GEBCO, for the relay-site calculations.
- **Machu Picchu Station** (Peru): COMNAP lists −62.0916, −58.4706, seasonal, peak population 30, fossil-fuel power [S51].

### 2.2 Geometry, horizon and VHF/UHF line of sight (calc; 4/3 earth; antenna 10 m at the far end; relay at the literature summit +10 m)

| Leg | km | Sea % | Horizon sum (relay to 10 m) | Terrain-checked clearance relay-to-10 m / relay-to-far-peak (m) |
|---|---|---|---|---|
| Elephant PW (853 m)–Pergamino | 337 | 60 | 134 km | −1,540 / −1,154 |
| Elephant PW–Contrapunto | 242 | 66 | 134 | −673 / −196 |
| Elephant PW–Machu Picchu | 221 | 71 | 134 | −783 / −263 |
| Elephant PW–Esperanza | 279 | 96 | 134 | −745 / −424 |
| Elephant PW–Signy | 501 | 99 | 134 | −3,276 / −3,060 |
| Clarence (1,950 m)–Pergamino | 371 | 89 | 195 | −1,155 / −787 |
| Clarence–Contrapunto | 276 | 85 | 195 | −482 / **+26** |
| Clarence–Machu Picchu | 256 | 80 | 195 | −560 / −14 |
| Clarence–Esperanza | 289 | 88 | 195 | −607 / −131 |
| Clarence–Signy | 456 | 99 | 195 | −2,156 / −1,920 |
| Goeldi-site (975 m)–Machu Picchu | 196 | 83 | 142 | −717 / −209 |
| Goeldi-site–Signy | 528 | 93 | 142 | −3,625 / −3,409 |

- Clarence's summit (4.12 √1950 ≈ 182 km horizon) is the only candidate with a clear VHF/UHF path to the KGI highlands (to Contrapunto at +26 m clearance if the far end is on a 569 m ridge; Machu Picchu −14 m, essentially grazing). Elephant's summit (about 133 km) is blocked by 200–420 m to every KGI/Esperanza point and by 3 km to Signy. **No island summit gives line of sight to Signy.** 156.8 MHz free-space loss is 123–130 dB for these legs; knife-edge diffraction over the bulge adds at least 17–32 dB (optimistic lower bound).
- The GEBCO terrain test is coarse (about 450 m grid, 150-point profiles).

### 2.3 MF ground wave on these legs (LFMF; field in dBµV/m at the leg distance, sea-only vs Millington with rock land; 0.9 MHz 10 kW | 3.5 MHz 100 W) (calc)

| Leg | km | 0.9 MHz 10 kW sea-only / rock | 3.5 MHz 100 W sea-only / rock |
|---|---|---|---|
| Elephant PW–Machu Picchu | 221 | 69 / 49 | 46 / 18 |
| Elephant PW–Esperanza | 279 | 66 / 63 | 41 / 35 |
| Elephant PW–Pergamino | 337 | 63 / 38 | 37 / −4 |
| Elephant PW–Signy | 501 | 55 / 53 | 26 / 14 |
| Clarence–Contrapunto | 276 | 66 / 54 | 42 / 23 |
| Clarence–Pergamino | 371 | 61 / 48 | 35 / 8 |
| Clarence–Signy | 456 | 57 / 53 | 29 / 14 |
| Goeldi-site–Signy | 528 | 54 / 39 | 24 / −11 |

- The legs to Signy are 93–99% sea, so MF/HF ground wave is the strong mode for the relay-to-Signy legs; the KGI/Livingston-end legs lose 15–40 dB where the path runs across island interiors.

### 2.4 HF skywave on these legs
- **Any-band usable hours/24 at 100 W, 0 dBi (V/P; min to max over SSN 5/60/160):** January quiet 24/24 on every relay and trunk leg; July quiet 24/24 (P.533 23–24 for the Signy legs); **rural-noise July voice P.533 only 10–21 h** on relay legs and 3–11 h on the long legs (Perg–Signy 3–4 h, Esperanza–Signy 5–11 h). Weak-signal digital: 24 h on all legs. With +6 dBi at 100 W: 24 h on every leg, voice, even rural.
- **Chain versus direct Pergamino–Signy, hours with all legs usable (V/P; SSN 5/60/160; Jan || Jul):** direct 24/24 for 100 W +6 dBi voice (quiet or rural) and for 1 kW 0 dBi; at 100 W 0 dBi rural voice the direct link is 24/24 24/24 13/24 || 24/3 24/4 24/3 (V/P) while via Elephant PW it is 24/24 24/24 22/24 || 24/17 24/13 24/10 and via Esperanza 24/24 24/24 16/24 || 24/11 24/5 24/8. So a relay roughly triples the July rural-noise voice hours on P.533 (3–4 h to 10–17 h) but does not reach 24 h; +6 dBi does (voice 24 h on every route at 100 W).
- **P.533 median best-band S/N (3 kHz, 100 W 0 dBi, SSN 60, quiet-rural):** direct Pergamino–Signy 32 dB (Jan) / 22 dB (Jul); Elephant PW–Signy 34/25; Elephant PW–Pergamino 33/26 (calc). A relay buys only +1 to +4 dB per leg on HF, because both legs still need a single-hop F2 at 30–50° elevation and see the same absorption.

### 2.5 (a) What a relay buys physically versus the direct 807 km link (evidence-only)
- **Power, antenna, band:** essentially nothing on HF (+1 to +4 dB, same bands). A +6 dBi antenna at each end of the direct link gives more than a relay does at 100 W (voice 24 h in all cases vs 10–17 h through a relay in July rural noise).
- **Noise and reliability:** the relay does not cure absorption; both legs see the same July low-band limit (3 kHz S/N 22–26 dB). It adds a second path to fail.
- **MF/AM and VHF are where it matters.** A 10 kW 0.9 MHz transmitter on Elephant or Clarence gives about 55–57 dBµV/m (sea-only) at Signy 456–501 km, versus about 42 at 807 km from Pergamino, so a relay moves Signy from the fringe to inside 54 dBµV/m coverage. Clarence is also the only site with possible VHF/UHF line of sight to KGI (Contrapunto, Machu Picchu), which would give a high-capacity VHF trunk across the Bransfield Strait to the highlands.
- **Store-and-forward:** at a relay, weak-signal digital messages can be queued until a band opens (July low bands close in the sunlit hours). That is a software benefit; it needs power and a modem, not a mountain.

### 2.6 (b) Build, access and keep-running (precedents and what I could verify)
- **Access.** Elephant Point Wild is rarely landable (swell, reefs, grounded icebergs) and Cape Lookout needs west/southwest-swell-free conditions and a small boat [S49, S50]. No landing information for Clarence was found. All access is by small boat from a ship or by helicopter (inf; no air facility on either island in COMNAP).
- **Wind and rime.** Elephant Island gusts of 160 km/h (100 mph) are cited (UNVERIFIED, search summary of Wikipedia). AWS programs report that "Rime and hoar accumulation can interrupt and bias measurements" and "mast stability/leaning and instrument failure due to extreme weather" [S52, Box et al.]; "1 cm of rime will obviously affect" anemometers [S52]. Power: solar cells "useless during Antarctic winter" and wind generators unable to provide adequate winter power at some sites (UNVERIFIED, search summary of Antarctic geophysical observatory reviews); the polar night at 61°S is about 5 h of daylight at midwinter, so a low-power design (a few watts, digital-only) is the realistic one (inf).
- **Precedents for unattended polar relays/repeaters.** AAD "solar and wind-powered VHF repeaters located on mountain tops" [S27]; McMurdo repeaters at Mounts Taylor, Wright, Terror, Aurora and Brooke (the Brooke site "location varies") [S2]; a Casey repeater on channel 21 "at the highest vantage point" (UNVERIFIED). AWS planning: "MTBF of more than five times the mean time between visits is a reasonable planning strategy. For many stations this demands MTBF > 5 years" [S52]; one AWS has run since October 1984 with no maintenance access (UNVERIFIED). Quantitative failure rates: **not found** (dead end at the sources; no published per-site failure rate for polar repeaters was located).
- **Sustainability.** The nearest staffed neighbors are Goeldi refuge (seasonal only, Brazil, since 1988 [S51]) and KGI. A relay on Elephant/Clarence would depend on annual boat visits that Point Wild's landing record suggests cannot be guaranteed (inf). Elephant has two protected historic sites (HSM 53 at Point Wild, HSM 74 at Hampson Cove); any new structure there needs ATS approval and avoidance of those sites (inf).

### 2.7 (c) Does Esperanza as the Signy trunk make an island relay unnecessary?
- **Yes, for HF.** Esperanza–Signy is 663 km, 92% sea, 100 W 0 dBi voice quiet: 24 h any-band on both models (rural July P.533 5–11 h, same limit as direct). A staffed city has power, antennas, maintenance and no landing problem. The Esperanza–Pergamino (191 km) and Esperanza–Contrapunto (160 km) legs are 24 h on HF at 100 W (rural-July P.533 12–21 h) and VHF/UHF line of sight needs 610–1,560 m masts at both ends, so HF NVIS or a shore-sited MF ground wave is the intra-Peninsula link, not a relay.
- **No, for MF and VHF coverage.** Esperanza to Signy over sea at 0.9 MHz 10 kW gives 48 dBµV/m (sea-only; 39 with rock land), so a 10–50 kW MF station at Esperanza reaches Signy; the VHF/UHF coverage a Clarence summit could give to KGI is not replaceable by Esperanza. (inf: if the goal is only a Signy trunk, Esperanza makes the island relay unnecessary.)

---

## 3. Santa Luce legs and the Weddell sector

### 3.1 Geometry and geomagnetic exposure (calc; AACGM-v2 at 110 km, IGRF-14 dipole)
Distances: Signy–Santa Luce 1,918 km, Esperanza–Santa Luce 2,025, Marambio–Santa Luce 1,943, Santa Luce–Halley 484, –Troll 543, –Neumayer 319, –SANAE ("Sanay") 388 (calc). Sea fraction 90–93% for the three Peninsula-side legs (land only at the Santa Luce end, 123–187 km, max 332 m), and **0–2% sea for the four inland legs** (Halley 2%, others 0%), terrain 642–2,313 m.
Santa Luce AACGM −62.2° (dipole −67.0°), Halley −62.9°/−68.2°, Troll −63.3°/−67.9°, Neumayer −61.1°/−65.3°, SANAE −62.4°/−66.9°, Belgrano −64.2°/−69.8°, Utstein −66.0°/−70.7°, Signy −49.7°/−52.3°. Midpoints: Signy–Santa Luce −56.3°, Esperanza–Santa Luce −57.1°, Marambio–Santa Luce −57.5°, Santa Luce–Halley −62.6° (AACGM). At Santa Luce and Halley the sun is up all day for about 90–106 days (midnight sun) and down for 83–101 days (polar night) (calc).

### 3.2 HF results (1 kW, quiet-rural; V/P any-band hours/24, SSN 5/60/160)
- **Signy–Santa Luce (1,918 km), 100 W, voice, quiet-rural, 0 dBi:** January V 6–7 h but P 24; July V 20–24 / P 10–13. Rural noise: **0 h on both models**. **With +6 dBi at 100 W: 24/24 h** (January and July, all SSN). Weak-signal digital 100 W 0 dBi rural: 24/24 h.
  - Per band, 100 W +6 dBi, quiet voice (V/P): January SSN 60 5/12 7/12 12/24 14/24 24/24 20/24 on 2.5–14.2 MHz; July SSN 60 17/14 23/16 24/15 12/10 8/6 1/0.
  - MUF (V|P): January 12.9–14.7 | 12.3–14.7 MHz (SSN 5) up to 14.8–18.5 | 14.2–16.6 (SSN 160); July 5.5–11.4 | 4.4–10.6 (SSN 5), 4.8–19.1 | 4.5–19.3 (SSN 160). Geometry: one hop 12.7° take-off, secant 2.76 (calc); two hops 29.3° and 1.81; three hops 41.1° and 1.44.
- **Esperanza–Santa Luce (2,025 km direct):** same pattern (100 W voice quiet January V 2–5 / P 23–24, July V 19–24 / P 9–11; +6 dBi 24/24).
- **Chain versus direct (hours all legs usable, V/P):** 1 kW 0 dBi quiet voice, Esperanza–Santa Luce direct 24/24 22/24 24/24 || 24/22 24/24 24/24 and via Signy 24/24 23/24 24/24 || 24/23 24/24 24/24 (about equal). At 100 W 0 dBi quiet voice: direct 4/24 2/24 5/23 || 24/11 23/9 19/9 versus via Signy 7/24 6/24 7/24 || 24/12 24/13 20/10 (the chain is slightly better, but both are poor on V in January). At 100 W +6 dBi both 24/24 everywhere. So Signy as an intermediate gives about the same or slightly more hours than the 2,025 km direct hop (the chain length 2,581 km vs 2,025 km) but adds an extra station (inf).
- **Regional NVIS at the Santa Luce end (100 W, 0 dBi, quiet voice, any band V/P):** SL–Halley January 24/24, July V 16–24 / P 11–21; SL–Neumayer July V 16–24 / P 13–21; SL–SANAE V 17–24 / P 9–21; SL–Troll V 19–24 / P 12–21. **Rural noise July: V 6–15 / P 0–4 h**, which is the key weakness (winter MUFs 1.8–3.7 MHz at Halley, polar night). Weak-signal digital 24 h (P.533 July 21–24 h). SL–Halley MUF: January 5.9–7.0 (V) | 6.2–7.3 (P) MHz (SSN 5); July 1.9–3.6 | 1.8–3.7 MHz (SSN 5), up to 3.3–8.2 | 3.4–8.9 (SSN 160) (calc). The inland legs are 0–2% sea with 640–2,300 m terrain (**MF/HF ground wave is not viable**: 3.5 MHz 100 W field −34 to +27 dBµV/m, rock land) and VHF line of sight needs masts of 1.9 km (Santa Luce–Neumayer).
- **Documented performance on Weddell-sector paths:** the Neumayer III WSPR beacon DP0GVN (5 W, 5 m vertical, multiband receiver 160–6 m, running since January 2018) received "several thousand beacon spots" within days, with "the majority of reported WSPR spots originat[ing] from stations in the Northern Hemisphere" [S53 ARRL; second statement UNVERIFIED, search summary of the MDPI paper]; WSPR from DP0GVN reached ZL (New Zealand) over more than 7,500 km, and some paths succeeded from Australia, EA8 and South America (HamSCI 2021 poster) [S54]. These show 5 W weak-signal links in the Weddell sector working over long paths; they do not give availability statistics for Halley, SANAE or Belgrano. BAS/AWI/SANAE HF-propagation papers for the Weddell sector: **not found** (dead end at the sources; an MDPI polar-day balloon paper and a Frontiers/Ukrainian Vernadsky storm paper are known only from search summaries).
- **Polar-cap evidence on a comparable path:** McMurdo–South Pole oblique sounding (1,300 km) between 28 February and 13 March used 12 frequencies from 2.6 to 7.2 MHz; "No signals were received below 4.1 MHz, due to absorption and reduced transmitter efficiency", and GPS-TEC predicted 7.2 MHz propagation only 40% true-positive / 73% true-negative [S55, Atmos. Meas. Tech. 2020]. Polar-cap links therefore have a higher MUF floor and a lower predictability than model tables suggest.
- **Weddell Sea Anomaly.** The WSA region (55–75°S, 80–30°W) covers Signy, the Peninsula and the Belgrano/Halley sector; in summer electron density peaks at night [S22], first seen at Halley in 1958 [S22]. It raises the night MUF in summer on the Peninsula–Weddell hops (inf from [S22]; not in the CCIR maps used by the models, so the models likely under-predict summer-night MUF there).

### 3.3 Bottom line, Signy–Santa Luce and the chain
- **A settled community can hold Signy–Santa Luce HF with 100 W and +6 dBi antennas, or 1 kW with 0 dBi** (24 h both models, quiet-rural noise). At 100 W 0 dBi voice the models disagree (V 6–7 h January, P 24) and rural noise gives 0 h on both, so it is not reliable. Weak-signal digital works at 100 W 0 dBi.
- **Chain via Signy versus the direct 2,025 km Esperanza hop:** about the same hours (see 3.2); Signy is a manned seasonal station (UK, COMNAP [S51]) and not needed; the direct hop is shorter in total path (2,025 vs 2,581 km) and has one fewer failure point.
- **Interruption frequency:** see Section 4.4 (Santa Luce at −62° AACGM is exposed to auroral absorption and to larger PCA events; Signy at −50° is not).

---

## 4. Peninsula–Casey trunk (meta-nodes at 1 kW, +6 to +10 dBi)

### 4.1 Hop geometry and exposure (calc)
Nodes (AACGM at 110 km / dipole): Peninsula −50.9/−55.0, Halley −62.9/−68.2, Belgrano −64.2/−69.8, Santa Luce −62.2/−67.0, Utstein −66.0/−70.7, Mawson −70.9/−73.0, Davis −75.1/−75.9, Mirny −77.4/−75.3, Casey −80.5/−75.5. Hop midpoints and most-poleward point (AACGM): Pen–Utstein −60.9/−66.0; Pen–Halley −57.3/−62.9; Halley–Utstein −65.2/−66.0; Pen–Belgrano −57.8/−64.2; Belgrano–Utstein −66.1/−66.3; Utstein–Mawson −69.0/−70.9; Mawson–Casey −77.5/−80.6; Mawson–Mirny −74.7/−77.4; Mirny–Casey −79.4/−80.5; Mawson–Davis −73.0/−75.1; Davis–Casey −79.1/−80.6; Pen–Casey (5,508 km) −73.2/−85.3. Distances (calc): Peninsula–Utstein 3,288, –Halley 1,777, –Belgrano 1,766, –Santa Luce 2,079, –Neumayer 2,264, –Mawson 4,702, –Casey 5,508; Halley–Utstein 1,551; Belgrano–Utstein 1,713; Belgrano–Neumayer 1,108; Neumayer–Utstein 1,122; Halley–Neumayer 797; Belgrano–Halley 327; Utstein–Mawson 1,561; Utstein–Casey 3,198; Mawson–Casey 2,029; Mawson–Mirny 1,297; Mirny–Casey 777; Mawson–Davis 634; Davis–Casey 1,395; Mawson–Zhongshan 583; Zhongshan–Davis 109; Zhongshan–Mirny 758; Davis–Mirny 675; Zhongshan–Casey 1,453.

### 4.2 HF model results (1 kW, quiet-rural; hours/24 with at least one tested band usable, V/P; SSN 5|60|160; Jan || Jul)

**Single hops, +6 dBi each end, voice:**

| Hop | km | Jan | Jul |
|---|---|---|---|
| Peninsula–Utstein | 3,288 | 23/24 23/24 23/24 | 24/18 24/24 24/24 |
| Peninsula–Halley | 1,777 | 24/24 ×3 | 24/24 ×3 |
| Halley–Utstein | 1,551 | 24/24 ×3 | 24/24 ×3 |
| Peninsula–Belgrano | 1,766 | 24/24 ×3 | 24/24 ×3 |
| Belgrano–Utstein | 1,713 | 24/24 ×3 | 24/24 ×3 |
| Peninsula–Neumayer | 2,264 | 23/24 24/24 24/24 | 24/24 ×3 |
| Belgrano–Neumayer | 1,108 | 24/24 ×3 | 24/24 ×3 |
| Neumayer–Utstein | 1,122 | 24/24 ×3 | 24/24 ×3 |
| Belgrano–Halley | 327 | 24/24 ×3 | 14/19 19/24 24/24 |
| Utstein–Mawson | 1,561 | 24/24 ×3 | 24/24 ×3 |
| Utstein–Casey | 3,198 | 24/24 24/24 22/24 | 24/22 24/24 24/24 |
| Mawson–Casey | 2,029 | 24/24 ×3 | 24/24 ×3 |
| Mawson–Mirny | 1,297 | 24/24 ×3 | 24/24 ×3 |
| Mirny–Casey | 777 | 24/24 ×3 | 24/24 ×3 |
| Mawson–Zhongshan | 583 | 24/24 ×3 | 22/24 24/24 24/24 |
| Zhongshan–Davis | 109 | 24/24 ×3 | 15/24 24/24 24/24 |
| Zhongshan–Mirny | 758 | 24/24 ×3 | 24/24 ×3 |
| Davis–Mirny | 675 | 24/24 ×3 | 24/24 ×3 |
| Davis–Casey | 1,395 | 24/24 ×3 | 24/24 ×3 |
| Zhongshan–Casey | 1,453 | 24/24 ×3 | 24/24 ×3 |
| Peninsula–Mawson | 4,702 | V 13/13/24 P 24 | V 12/22/24 / P 11/13/18 |
| **Peninsula–Casey direct** | 5,508 | **V 11/14/1 / P 24** | **V 11/19/24 / P 0/0/7** |

- **At 0 dBi (1 kW voice quiet):** Peninsula–Utstein single hop falls to V 13–16 h January / V 21 h, P 3–17 h July; Peninsula–Casey direct 0 h (P 18–24 January, 0 in July); Peninsula–Mawson 0 h (P.533 21–24 January, 0–1 July). The split chains all reach 18–24 h.
- **Weak-signal digital at 1 kW, +6 dBi:** every hop 24/24 except Peninsula–Casey July P.533 18–24 h, and Peninsula–Mawson 24/24. At 0 dBi digital: Peninsula–Casey July P.533 11–15 h (V 24).
- **Per-band structure (1 kW, +6 dBi, voice, quiet, V|P):**
  - **Peninsula–Utstein:** January daytime needs 10–18 MHz (14.2 MHz: V 17–20 h, P 16–24 h at SSN 5–60; 18.1 MHz V 17–23 h at SSN 60–160, 3.5–5 MHz V 0–10 h because of polar-day absorption but P 19–24 h); July 3.5–7 MHz (V 15–24 h on 2.5–7.1 MHz, P 8–15 h).
  - **Mawson–Casey:** January 7.1 and 10.1 MHz 24 h, 5 MHz 13–19 h, 14.2 MHz 4–11 h; July 2.5–5 MHz 16–24 h, 7.1 MHz 13–24 h.
  - **Peninsula–Casey direct:** VOACAP January 10.1–14.2 MHz only 4–9 h at SSN 5–60; P.533 24 h on 3.5–10 MHz; July VOACAP 5–7.1 MHz 1–24 h, P.533 zero.
- **Chains (all legs usable in the same hour), 1 kW +6 dBi quiet voice (V/P, SSN 5|60|160, Jan || Jul):**
  - Peninsula–Belgrano–Utstein, Peninsula–Halley–Utstein, Peninsula–Belgrano–Neumayer–Utstein: 24/24 on all.
  - Peninsula–Neumayer–Utstein: 23/24 24/24 24/24 || 24/24 ×3.
  - **Peninsula–Utstein direct: 23/24 23/24 23/24 || 24/18 24/24 24/24** (one or two hours short, a model-ionosphere artifact in polar day).
  - Mawson–Casey direct, via Mirny, via Davis–Mirny, via Zhongshan–Mirny: 24/24 on all (Zhongshan chains 22/24 in July SSN 5).
  - **At 0 dBi voice the split is clearly better:** Peninsula–Utstein direct V 13–21 / P 3–24, Peninsula–Halley–Utstein V 18–24 / P 23–24, Peninsula–Belgrano–Utstein V 21–24 / P 18–24, Peninsula–Belgrano–Neumayer–Utstein V 23–24 / P 23–24.
- **Utstein–Casey is 3,198 km** (calc), about the same as Peninsula–Utstein, and works 22–24 h at +6 dBi; so Mawson is not needed for HF reach alone (inf).

### 4.3 Is each node worth it? (physics, evidence-only; node value for reliability versus adding a failure point)
- **Required.** One Weddell-sector node between the Peninsula and Utstein is required for **voice with simple antennas**; with +6 dBi and 1 kW the 3,288 km single hop already gives 23–24 h on both models, so a node is "helpful", not "required", only if the stations are strong. Without directional gain (0 dBi) the single hop is 3–21 h/day on voice.
- **Halley versus Belgrano versus Neumayer versus Santa Luce:** all give 24/24 for +6 dBi (and 18–24 at 0 dBi). Halley (−62.9°) and Santa Luce (−62.2°) have more exposure than Belgrano (−64.2°) to auroral absorption only marginally (all three are within 2°); Belgrano–Halley (327 km) adds nothing. **Belgrano–Neumayer–Utstein (3 hops) adds a node and does not improve on Peninsula–Belgrano–Utstein (24/24 at both)**, so Neumayer merely adds a failure point for HF. Neumayer's value is as a staffed German station with 5 W WSPR experience [S53] and an inland-coast anchor, not for propagation (inf).
- **Peninsula–Neumayer (2,264 km skip-ahead):** works (+6: 23–24 h) and removes Belgrano/Halley from the chain; Neumayer–Utstein 1,122 km also 24 h. This skip-ahead is the shortest two-hop chain with a fully staffed station at the middle (inf).
- **Mawson–Casey direct versus via Mirny, Davis or Zhongshan:** the direct 2,029 km hop is already 24/24 at +6 and at 0 dBi, voice and digital. Mirny, Davis and Zhongshan therefore do **not** make the Mawson–Casey link more reliable on the HF models; they only shorten hops. They add failure points and none sits equatorward of the polar cap (Mirny −77.4, Davis −75.1, Casey −80.5), so they share Casey's exposure (see 4.4). Their value would be as local Indian-Ocean-sector sites (inf).
- **Davis–Zhongshan (109 km, 97% sea per GEBCO, max 6 m terrain) (calc).** HF NVIS works at 100 W, 0 dBi, quiet or rural: January 24 h on 2.5–5 MHz (up to 7.1 at SSN 160), July 12–24 h (V) / 7–24 h (P); at 10 W quiet: January 22–24 h, July 10–24 h. Ground wave over sea at 3.5 MHz 100 W gives 56 dBµV/m (sea-only), 1 dBµV/m (rock), −10 dBµV/m (ice) at 108 km; at 1 MHz 1 kW 68 / 32 / 16 dBµV/m. VHF line of sight needs about 180 m masts at both ends (earth bulge 173 m at the midpoint, calc). **A shared HF site is simpler.** Two separate sites 109 km apart add no HF reach (inf).
- **Polar-cap blackouts hit these nodes together.** Mawson (−70.9° AACGM) through Casey (−80.5°) and Mirny, Davis and Zhongshan (all poleward of −75°) lie within the same polar cap; a PCA event raises absorption at all of them at once, and extra nodes cannot cure a correlated blackout. Rerouting around the cap is the only mitigation named by BoM ("relaying messages on paths which avoid the polar regions") [S14]. The Peninsula and Signy are the only nodes equatorward of −55° and are the "outside" relay points (inf).

### 4.4 Interruptions: polar-cap absorption (PCA), auroral absorption (AA) and storms
Method and sources.
- **NOAA scales [S15], cycle average (1 cycle = 11 years = 4,018 days) (calc):**

| Event | Frequency | Days/cycle | Fraction of days |
|---|---|---|---|
| G1+ (Kp ≥ 5) | 1,700 events | 900 days | 22% |
| G2+ | 600 events | 360 days | 9.0% |
| G3+ | 200 events | 130 days | 3.2% |
| G4+ | 100 events | 60 days | 1.5% |
| G5 | 4 events | 4 days | 0.1% |
| S1 radiation storm (>10 MeV, ≥ 10 pfu) | 50 per cycle | | |
| S2 | 25 per cycle | | |
| S3 | 10 per cycle | | |
| S4 | 3 per cycle | | |
| S5 | fewer than 1 per cycle | | |

  The scale effects: S1 "minor impacts on HF radio in the polar regions", S2 "small effects", S3 "degraded HF radio propagation through the polar regions", S4 "blackout", S5 "complete blackout possible" [S15]. G-scale aurora lower latitudes (geomagnetic): G2 55°, G3 50°, G4 45°, G5 40° [S15].
- **PCA absorption scaling [S16 D-RAP]:** A(f) = A(f0)(f0/f)^1.5 dB; daytime Ad = 0.115 [J(>5.2 MeV)]^½ dB and nighttime An = 0.020 [J(>2.2 MeV)]^½ dB (the polar-night PCA absorption is about 17% of the daytime value for equal flux, calc). A 1 dB event at 30 MHz therefore gives about 5.2 dB at 10 MHz, 14.7 dB at 5 MHz, 25 dB at 3.5 MHz and 42 dB at 2.5 MHz one-way (calc; round trip roughly doubles). So **the low bands used in winter (2.5–5 MHz) are the first to black out, and bands above about 10 MHz survive moderate events** (inf).
- **PCA duration and occurrence.** BoM: PCAs "can last several days" [S14, S41]. Published statistics (UNVERIFIED, search summaries): 218 riometer events of at least 1 dB between 1955 and 1986 (about 7 per year); 24 moderate and 13 severe HF-relevant PCA events per solar cycle, with mean durations of about 8 h (moderate) and 1.6 days (severe); in cycles 22 and 23 moderate-or-severe space-weather impacts on HF "a maximum of 163 and 78 days per year" (Space Weather Space Clim. 2022; full text not retrievable, 403). Using these with the NOAA counts, my bracket for the fraction of time with PCA degradation at polar-cap latitudes is **0.7% (24 × 8 h + 13 × 1.6 d ≈ 29 days per cycle) to 2.5% (50 S1+ events × about 2 days)** (calc, assumptions flagged; events cluster near maximum and in the declining phase, so near 2030 solar minimum the rate is lower).
- **Auroral absorption.** Peaks at 64–68° magnetic latitude in the pre-noon and pre-midnight sectors, 30 MHz peaks up to about 6 dB, near zero in quiet times (UNVERIFIED, search summary of the literature); weak fluctuating absorptions below 1 dB 30 MHz were recorded at Casey over a study period (UNVERIFIED). A Murmansk-region HF experiment found that "a significant level of auroral absorption decreases the reliability of the HF communication inside the auroral zone" and that the main ionospheric trough and the poleward trough edge control winter evening/night propagation (ΦL 60–70°) [S56 URSI]. **No quantitative Antarctic occurrence percentage for auroral absorption (Casey, Mawson, Davis, Halley, SANAE) was found** (dead end at the sources; the BoM/AAD riometer data exist at Casey, Davis, Mawson and Macquarie [S41] but statistics were not retrieved).

**My explicit estimates (inf; derived from the NOAA counts above and the flagged assumptions; not measurements):**

| Hop group | PCA, share of time | Auroral absorption / storm degradation, share of hours | Basis |
|---|---|---|---|
| Peninsula–Signy–Pergamino-type (−50°) | 0.1–0.4% (only S4–S5, 3 per cycle × 1.6–4 days) | 3% of days at G3+ (oval at about 50°); about 1–3% of hours | NOAA G3 aurora at 50° geomagnetic |
| Peninsula–Halley/Belgrano/Santa Luce/Neumayer, Peninsula–Utstein (midpoints −57 to −61°, far end −62 to −66°) | 0.3–1% (S3+, 10 per cycle × 1.6–4 days) | storm days G1+ 22% × assumed 25–50% of the day degraded ≈ 5–11% of hours at the far end (oval-latitude end), 2–5% at midpoint | AA peaks at 64–68° (UNVERIFIED) |
| Weddell hops among Halley/Belgrano/Santa Luce/Neumayer/Utstein (−61 to −66°) | 0.3–1% | 5–11% of hours (both ends in the AA band) | same |
| Utstein–Mawson (−69 to −71°) | 1–2.5% | 5–15% of hours (poleward edge of the oval) | assumption |
| Mawson–Casey, Mirny, Davis, Zhongshan (−73 to −80°) | **0.7–2.5% (full S1+ exposure)** | storm-time oval excursions plus polar-cap patches; no occurrence data | polar-cap evidence McMurdo–South Pole (4.1 MHz floor, 40% predictability) [S55] |
| Peninsula–Casey direct (midpoint −73°, extreme −85°) | 0.7–2.5% plus polar-cap sounding unpredictability | as above | |

- **What that means for availability (inf).** For the Weddell-sector and Indian-Ocean hops, the clean-model availability (24 h with at least one band) minus PCA (0.7–2.5%) minus oval/storm degradation (5–15% of hours) gives a **realistic year-round availability for a single hop of about 85–95% for voice and about 90–98% for weak-signal digital with automatic band selection** (the missing hours concentrate on the winter low bands, where storm-time absorption is worst). A multi-hop chain multiplies the per-hop availabilities, and because PCA is correlated across all nodes poleward of −60°, the correlated loss (0.7–2.5% + major storms) does **not** multiply independently: the chain's loss is the union of the correlated polar-cap blackout and the independent per-hop auroral degradations (inf). A 4-hop chain at about 90% per hop has about 66% product availability if the auroral degradations were independent; they are correlated in time (storm days), so the true figure lies between 66% and 90% (calc).
- **Solar minimum (about 2030, SSN 5, NOAA predicted 9.3 for October 2030 [S17]):** models give the lowest MUFs, so the working bands drop by 2–4 MHz (for example, Peninsula–Utstein January: 7–14 MHz still usable, July 2.5–5 MHz), and the low bands (2.5–5 MHz) become the winter workhorses on exactly the bands most sensitive to PCA and AA (A ∝ f^−1.5). PCA counts are smaller near minimum than at maximum (S1+ 50 per cycle cluster in the active years) (inf, no source found for minimum-phase counts). So **expect fewer but harder interruptions at 2030: lower rates of PCA, but each affects the very bands in use** (inf).
- **Required versus merely helpful for a Peninsula–Casey chain (evidence-only):**
  1. **Required:** a Peninsula station and a Casey station; at least one intermediate in the Weddell sector (Halley, Belgrano or Neumayer) **if** the stations use 0 dBi antennas or 100 W (voice hop 3,288 km fails 3–21 h/day); with 1 kW and +6 dBi the single Peninsula–Utstein hop is 23–24 h on both models. Utstein is required as a bridging point between the Weddell sector and Indian-Ocean sector (Peninsula–Mawson at 4,702 km and Peninsula–Casey at 5,508 km are unreliable on voice), but Utstein–Casey at 3,198 km works 22–24 h at +6 dBi, so **Mawson is helpful, not required** on HF reach grounds (inf).
  2. **Merely helpful or adds a failure point:** Belgrano–Halley (327 km), Neumayer (when Belgrano or Halley is already in), Santa Luce (about equal to Halley), Mirny, Davis, Zhongshan (Mawson–Casey direct is already 24/24).
  3. **Cannot be cured by extra nodes:** a polar-cap blackout, because all of Mawson, Davis, Zhongshan, Mirny and Casey lie in the same cap. The mitigations that exist are a lower-latitude relay path (Peninsula, Signy, South America) and weak-signal digital modes with scheduled retries (inf).

---

## 5. Contradictions, unverified items, and problems found
1. **VOACAP column shift** (Section 0): corrected here. P.533 results and all non-VOACAP numbers are unaffected.
2. **VOACAP versus P.533:** Pergamino–Signy July rural voice 24 h (V) vs 3–4 h (P); Signy–Santa Luce January 100 W 0 dBi quiet voice V 6–7 h vs P 24 h; Peninsula–Casey July P.533 0 h vs V 1–24 h. P.533 is the conservative bound, VOACAP the optimistic one except in the polar-day January cases noted.
3. **Cape Lookout coordinates:** the coordinates supplied (−61.08, −55.37) differ from IAATO's landing (−61.28, −55.21); my "ECL" legs use the Goeldi refuge position (−61.133, −55.35).
4. **Summit heights:** Mount Irving 1,950 m / 2,300 m (older) / 1,772 m ("recent research"); Pardo Ridge 852–853 m; GEBCO cells far lower (188 m near Mount Irving, 678 m near Pendragon).
5. **PCA duration:** BoM "several days" versus the UNVERIFIED published 8 h (moderate) to 1.6 days (severe) means; my 0.7–2.5% bracket uses both.
6. **Unverified items used:** NOAA S/G counts are verified [S15]; the 218-event riometer list, the 24 moderate + 13 severe events and 163/78 days per year, the auroral-absorption latitude statements, Elephant Island 160 km/h winds, Point Wild "once every five years", Mount Irving/Pardo heights, AWS GC41, Clarence IBA status, and the DP0GVN "majority from Northern Hemisphere" statement are all UNVERIFIED search-summary items.

### Search log (new this session) and dead ends
Queries (exact strings abbreviated): "Pardo Ridge Elephant Island height…", "Mount Irving Clarence Island height…", "Elephant Island Point Wild Historic Site… landing conditions", "Clarence Island… landing difficult… ASPA", "Elephant Island Antarctica wind speed… Goeldi refuge…", "unattended automatic weather station Antarctica failure rate…", "remote Antarctic automatic geophysical observatory OR radio repeater site unattended…", "Halley Antarctica HF radio communication auroral absorption riometer…", "Neumayer Station HF radio link… SANAE Weddell Sea sector HF…", "solar proton events per solar cycle… PCA events per year…", "statistics of auroral absorption riometer 30 MHz…", "Davis OR Mawson OR Casey… HF blackout days per year…", "WSPR Antarctica Neumayer DP0GVN propagation analysis…", "SANAE IV OR Halley OR Neumayer OR Belgrano HF… Weddell Sea sector…", "Weddell Sea Anomaly effect on HF radio propagation…", "auroral absorption occurrence Mawson OR Davis OR Casey riometer percentage…".
Dead ends:
- **Quantitative auroral-absorption occurrence for Casey/Mawson/Davis/Halley/SANAE:** died at the sources (BoM/AAD riometer data exist but no statistics retrieved).
- **PCA frequency statistics beyond NOAA counts:** the Space Weather Space Climate 2022 paper returned 403; used only its search summary (UNVERIFIED).
- **Polar relay/repeater failure rates:** died at the sources (no quantitative figures; only AWS planning guidance).
- **Clarence Island landing conditions or protected-area status:** not found.
- **BAS/AWI/SANAE Weddell-sector HF propagation papers:** not found; MDPI (polar-day balloons), Wiley (McMurdo–South Pole) and BAMS (AWS program) PDFs returned 403, only the AMT McMurdo–South Pole paper and the Box et al. AWS lessons paper (fetched with relaxed TLS) were read in full.
- **MF night sky-wave field (ITU-R P.1147/Rec. 435):** not computed; PDFs not retrieved.
- **Self-correction log:** the VOACAP parser offset (Section 0); GRWAVE rejected in favor of NTIA LFMF (first report); gap in MUFday filtering retained as MUFday ≥ 0.5, now valid after the fix.

### New sources
- [S49] ATS Visitor Site Guideline, Site 38 Point Wild — https://www.ats.aq/devAS/Ats/Guideline/3bc3c80e-15ca-494d-a178-66b972951d93
- [S50] IAATO Cape Lookout visitor site guide — https://documents.ats.aq/ATCM46/att/ATCM46_att123_e.pdf
- [S51] COMNAP Antarctic Facilities Master (CSV) — https://github.com/PolarGeospatialCenter/comnap-antarctic-facilities
- [S52] Box, Anderson, van den Broeke, Automatic Weather Stations on Glaciers: Lessons — https://polarmet.osu.edu/jbox/pubs/AWS_on_glaciers_-_Lessons_Box_Anderson_Broeke.pdf
- [S53] ARRL, Permanent WSPR beacon in Antarctica — https://www.arrl.org/news/permanent-wspr-beacon-in-antarctica-now-on-the-air
- [S54] HamSCI 2021 poster, R. Westphal DJ4FF — https://hamsci.org/sites/default/files/publications/2021_HamSCI/20210320_1700z-Robert_Westphal_DJ4FF.pdf
- [S55] AMT 13, 3023 (2020), McMurdo–South Pole oblique HF channel — https://amt.copernicus.org/articles/13/3023/2020/
- [S56] Blagoveshchensky & Sergeeva, Impact of the auroral ionosphere on HF radio propagation (URSI GA 2011) — https://www.ursi.org/proceedings/procGA11/ursi/GP2-5.pdf
- [S57] NOAA D-RAP documentation — https://www.spaceweather.gov/content/global-d-region-absorption-prediction-documentation
- Earlier sources S1–S48 are as in the first report (S8 P.372, S12 BS.703, S13 FM 24-18, S14 BoM HF propagation, S15 NOAA scales, S16 D-RAP, S17 NOAA solar cycle JSON, S22 Weddell Sea Anomaly, S24 NTIA 99-368, S27 AAD telecommunications, S38 auroral ovals, S39 tools, S41 BoM PCA).
