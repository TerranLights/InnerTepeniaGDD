# Deferred research: continue later

**Created 2026-10-11 at the developer's direction.** This is the running list of things researched, not found, and parked
**on purpose** to be continued in a later session. It is separate from `SHOPPING_LIST.md`. That file lists sources the
developer might obtain. This one lists searches **an agent should run again** and what to try. Each batch notes which
research file it came from. **Do not delete an item until it is resolved, and say where in the resolving file.**

**On resume:** work these only after the orchestrator review of the completed research files, unless a class needs one
sooner. Use the "search next" leads as written. A route that failed once may still work through a different mirror,
the author's page, an agency NTRS record, or arXiv. Log each route (`_BRIEF.md`).

**Still to add when each agent finishes:** the open threads of `gap_retry_mars_venus_jupiter.md`, `robot_body_in_space.md`,
`life_support_lowg_power_structures.md` and `moon_lagrange_and_comparables.md`.

---

## Batch 1: from `gap_retry_leo_human_machines_power.md` (418 lines; ~45 searches; ~95 documents opened; ~14 dead routes)

### Routes that failed (the pages exist; the tool could not read them)

| Source | Failure | Try next |
|---|---|---|
| **SpaceX pages** and the **Falcon user's guide** | return a JavaScript shell or a 404 | the PDF user's guide from a mirror; an independent analyst such as a government or university study |
| **Springer ISS-RAD papers** (Life Sciences in Space Research, 2023, Parts 1–3) | paywalled; three routes tried (publisher, Europe PMC, PubMed); abstracts only | author preprint copies; the NASA SRAG WRMISS 2025 slides (read; few numbers) |
| **Cucinotta 2008** (BioOne) | Incapsula wall; NTRS 20080026203 has a different abstract and no PDF | author copies; NASA-hosted version |
| **ORNL Pu-238 page** | 403 | NASA RPS program documents; National Academies radioisotope reviews |
| **MDPI paper** (4058) | blocked | a repository copy |
| **ResearchGate** "Impact of Solar Activity Cycles on ISS Orbital Decay: A Two-Decade TLE-Based Analysis (2005-2025)" | not opened; the arXiv route failed | the arXiv listing again; Space-Track TLE history for catalog number 25544 |

### Facts still not found

| # | Item | Search next |
|--:|---|---|
| 1 | **ISS reboost propellant per year** from a NASA or ESA primary (only a 1995 plan of 8–11 t/yr for the Russian segment, and per-burn data) | NASA ISS Program Office "Trajectory Operations" papers; Progress M propellant manifest tables; *Orbital Debris Quarterly News* altitude histories |
| 2 | **ISS monthly altitude decay** from a NASA primary (tool summaries gave 100 m/day and 2–4 km/month; not used) | Space-Track TLE history; JSC or ESA conference papers on ISS drag |
| 3 | **ISS eclipses per year**; longest sunlit periods (only "no eclipse above about 70° beta, one week twice a year", and 30–35 min eclipse per 90–92 min orbit) | NTRS 20250002029 (found, not opened); JSC "ISS beta angle" thermal documents |
| 4 | **Current ISS altitude** (2026) | NASA mission pages |
| 5 | **TDRS Ku-band ISS round-trip latency** (SNUG and test data used instead) | NASA SCaN documents |
| 6 | **Dose at 600 km vs 400 km** | ESA SPENVIS / ECSS-E-ST-10-04C tables; NASA/TP-2009-215779; Wu et al. 2011 (NTRS 20110015964, abstract only); STS-31 and STS-61 dose reports; Badhwar 2002 |
| 7 | **Solar Cycle 25 effect on crew dose**, quantified | beyond the ISS-RAD slides: none found |
| 8 | **The "80 / 160 mSv" claim.** Not traced to a NASA document. NASA's own figures found: **40–90 mSv** and **72 mSv** per six months. | settle against NASA primaries before any class cites a crew dose |
| 9 | **ORDEM 3.0 numeric fluxes** by size and altitude (numbers live in software and figures) | NASA/TP-20220002309 (ORDEM 3.1 verification; found, not opened); ODQN issues; Hypervelocity Impact Symposium flux tables |
| 10 | **ISS shield ballistic-limit equations and critical diameters** (only a 1 cm statement) | Christiansen (NASA JSC), "Design and performance equations for advanced meteoroid and debris shields" (NTRS); ISS document SSP 30425 |
| 11 | **Atomic oxygen at 600 km**, its solar-cycle swing, ISS ram fluence per year | a NASA primary |
| 12 | **Orbital lifetime of very large structures** (ISS ballistic coefficient was not derived because drag area and drag coefficient were not sourced) | NASA debris-office lifetime tools |
| 13 | **Modern commercial-part TID values** (only 1996 JSC classes) | NASA Goddard RADHOME / NEPP compendia (NTRS 20220010348; found, not opened); NESC COTS assessment (Majewicz, Chen); ISO 21980:2020 |
| 14 | **Typical single-event rates** beyond the 1996 per-class numbers | as above |
| 15 | **ESTL actuator data** beyond the SOT paper and the Harmonic Drive paper | ESTL's own site; NTRS 19750006982 (sputtered MoS₂ bearing endurance; seen in a summary, not opened) |
| 16 | **NASA HRP evidence reports** (cardiovascular, vestibular, SANS, immune) as primaries. The two NTRS numbers given (20150006969, 20160001745) are a panel report and a process deck. | NTRS: the "Evidence Report: Risk of Cardiovascular Adaptations Contributing to Adverse Mission Performance", and the SANS and immune reports. The plasma-volume 10–15% figure is secondary. |
| 17 | **Launch cost per kg, 2024–2026** for Falcon Heavy, Starship, Neutron, New Glenn; any government analysis | not found; SpaceX pages unreadable |
| 18 | **ISS array wing dimensions** from NASA (Lockheed numbers seen only in a summary); a 2026 power-degradation figure (only 2003 P6 data) | NASA ISS pages |
| 19 | **Propulsion and nuclear:** X3 Hall thruster (NTRS 20190001137; PEPL X3 pages); NTRS 20190029289; NTRS 20040161476 (a bibliography; the 2004 papers behind it were not opened); NASA TA-3 space power roadmap radiator numbers; Pu-238 supply and production, 2024–2026 | NASA RPS program; National Academies reviews |
| 20 | **Mars round trip:** the "Folta 2012" item resolved to a two-page abstract plus a 2005 paper. A separate 2012 full paper was not found. Bailey et al. 2013 table columns could not be aligned by year in the extracted text. | the AIAA copy, doi `10.2514/6.2013-5507` |

### Found and not opened (listed for a follow-up)

arXiv 2609.24534 (FACSAT-2 re-entry, solar cycle 25) · Frontiers `fspas.2026.1797886` · the JAXA Kibo shield page
(`iss.jaxa.jp/iss/kibo/develop_status_09_e.html`) · NASA OIG IG-22-003 PDF · GAO-17-673.

---

## Batch 2 onward

*(appended as each remaining agent reports)*
