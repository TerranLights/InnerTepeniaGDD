# Inspiration place research: protocol and the two briefs

**Written 2026-10-26.** Developer's instruction: for every city's real-world inspiration places, do **two rounds at full depth**, with genuine accuracy and extensive research, accepting the cost and the waiting for window limits. *"Everything else rests on this research."* (It feeds the ULM, then Southern Lights, the Second Interwar timeline, the post-war conditions, the exiles and refugees reaching Concordia, and the orbital and Mars societies.)

**What this is:** real-world facts about real places, institutions and traditions. **It is not synthesis, and nothing here is a conclusion about any fictional city.** A place's tier in the picks file is not changed by this research; tiers are the developer's.

## Where the results go (developer, 2026-10-26)

**Next to each city's existing research files**, in `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/` (`<Research_Logs>` below), named `<unit>_Inspiration_Place_Research_R1.md` and `_R2.md`. This sits beside the city's own `<City>_Research_Log.md` where one exists (Davis, Mirny, Shirayuki, Sinheung, Zhongshan). **Finished pass records are not edited.** Later, the developer and the orchestrator look through the results and decide how to merge them into the existing files. The old `outputs/` folder here is unused.

## The standing list of things to look for (added 2026-10-26)
**Every agent also reads `WHAT_TO_LOOK_FOR.md` in this folder in full**, uses its kinds (K1 to K14) as prompts in both rounds, and **tags each finding with the kind(s)** it fits. Three of its rules override anything below: **K2 is open** (festivals and customs tied to whatever is relevant to that place), **K6 is a question** (are there any such rules? if so what and how they work; "none found" is valid), and **K11 is very loose** (no slang, colloquialisms, nicknames or local coinages are collected; see the language caution). The A to F structure of the two briefs below still applies.

## How a unit is run

- **Queue:** `_TRACKER.md` (one row per work unit; 39 units for 37 cities; Relung Panen is separate). Inputs: `inputs/<unit>.md`, holding only that city's own picks. **An agent assigned to a unit reads only its own input file.** (One-location rule.)
- **Round 1** uses the brief in section 1 and writes `<Research_Logs>/<unit>_Inspiration_Place_Research_R1.md`. **Round 2** uses the brief in section 2, **starts by reading that unit's `_R1.md` in full**, and writes `<Research_Logs>/<unit>_Inspiration_Place_Research_R2.md`. Round 2 never starts before Round 1 for that unit is finished (FINAL ticked).
- **Concurrency:** no more than four agents at a time; the orchestrator dispatches the next unit as one finishes.
- **Orchestrator:** after each agent finishes, check the file's PROGRESS block (every pick ticked, FINAL ticked), then update the unit's row in `_TRACKER.md` (☐, ◐ or ✅). Never mark ✅ from the agent's report alone.

## Saved progress and resume (applies to every agent)

1. Create the output file first, beginning with a PROGRESS block: one `- [ ] <n>` line per pick in the input file, plus `- [ ] FINAL`.
2. After finishing each pick, append its findings and its search-log lines to the file, **then** tick its box.
3. If the output file already exists when you start, you are resuming: read it, skip ticked picks, continue from the first unticked one, finish a half-written pick without duplicating, and add a line `RESUMED <date> <time>`.
4. Do not spawn sub-agents. Do not delete or rewrite earlier sections.
5. **On a session-limit or rate-limit failure:** do not re-dispatch before the reset time shown in the error. At the reset, resume the same agent with a message ("Resume: read your file's PROGRESS block, skip ticked picks, continue"), or dispatch a fresh agent with the same prompt (it resumes from the file).

## Rules that bind every agent

Research **fully**. A recalled fact is a guess; a wrong fact is worse than a missing one. Do not stop at the first useful hit; query each place from several angles (official and municipal sites, tourism boards, encyclopedias, news, academic work, local-language sources); **open and read** sources, never report from snippets. Every claim carries a source (URL or citation) and a date and is marked **SOURCED** (read on the page) or **UNVERIFIED** (seen only in a snippet or secondhand). Never fill a gap with a guess: write **NOT FOUND** and where you looked. Keep a search log: exact search strings, whether each found something, every dead end. Report sensitive histories (colonialism, forced labor, displacement, war) neutrally and plainly. Real-world facts only; do not compare places to each other; do not write about any fictional setting. American English.

---

## 1 · BRIEF, ROUND 1 (the basics)

For each pick in your input file (a place, institution or tradition), find out what else exists there and what cultural locations exist there. Record, with sources and dates:

- **A. Snapshot:** location, population, size, what it is, and its defining feature.
- **B. What else exists there:** economy and industries (sizes, employment), institutions (governance, schools, hospitals, research bodies), services, infrastructure, how food and goods arrive and leave, who lives and works there (workforce makeup, housing), daily work and life patterns.
- **C. Cultural locations:** museums, theaters, galleries, music venues, festivals, markets, religious and ceremonial sites, libraries, food and drink places, sports and gathering places, crafts and local traditions. Give **names**, what each is, and a source. Include the small and local, not only the famous.
- **D. How the defining feature shaped those things:** what exists because of it.
- **E. Structural features** that bear on local industry, local economy, arts and music scene, and work and life culture.
- **F. NOT FOUND.**

If a pick is a tradition or an institution rather than a single place (for example a type of teahouse or a style of market), research the tradition itself and two or three well-documented places where it is practiced today.

## 2 · BRIEF, ROUND 2 (deeper)

First read the unit's `<Research_Logs>/<unit>_Inspiration_Place_Research_R1.md` in full. **Do not repeat it.** For each pick, go deeper into what it does not cover:

- **A. Other settings:** the distinct kinds of spaces and sub-areas that make up daily life (neighborhoods, worker housing, workplaces, schools, clinics, sports grounds, outdoor spaces), what each is like to be in, including in the off-season.
- **B. Subcultures:** occupational, migrant, seasonal-worker, generational, religious, Indigenous, hobby, artist and youth groups; how each lives; each group's own spaces, customs, language, slang and nicknames; where groups overlap or stay apart.
- **C. Leisure industries:** how free time is organized and sold: tourism, hospitality, recreation, sport, entertainment, outdoor activity, nightlife, seasonal differences, who the customers are and who works in it, and what locals do for fun when the visitors leave.
- **D. Places of connecting, meeting and communing (third places):** cafes, pubs and bars, community halls, houses of worship, sports clubs, baths and saunas, markets, libraries, shared meal spaces, docks, squares, associations: names, what happens there, who goes.
- **E. Cultural activities and civic life:** festivals (name, date, origin, who runs and attends), parades, markets, concerts, sports leagues, volunteer groups, cooperatives, councils and associations, mutual aid, seasonal cycles, rituals and traditions, food culture, storytelling, school and youth events.
- **F. NOT FOUND.**

Prefer specifics: names, dates, sizes, who organizes. Use local-language sources, municipal and regional event calendars, local newspapers, community pages, festival websites and tourism boards.

## 3 · The prompt to give an agent

> You are a research agent for a worldbuilding project. Read `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Inspiration_Place_Research/_PROTOCOL_AND_BRIEFS.md` in full (the rules, the saved-progress and resume rules, and your round's brief) and, in the same folder, `WHAT_TO_LOOK_FOR.md` in full (the kinds of things to look for, the tags, and the language caution: collect no slang, nicknames or local coinages). Your unit is `<unit>` and your round is `<1 or 2>`. Read ONLY `inputs/<unit>.md` (and, for round 2, `<Research_Logs>/<unit>_Inspiration_Place_Research_R1.md`). Write ONLY `<Research_Logs>/<unit>_Inspiration_Place_Research_R<round>.md`. Edit no other file. Final reply under 250 words: what you found, the most useful finding per pick in one line each, and what you could not find.
