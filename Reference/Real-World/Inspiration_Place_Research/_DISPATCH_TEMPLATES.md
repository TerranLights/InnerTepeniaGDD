# Dispatch templates for the inspiration place research (saved 2026-10-29 so a new session can continue without the old conversation)

**How to use:** pick the template, replace `<UNIT>` (for example `Relung_Panen_B08`) and `<N>` (the batch label used in file names, for example `B08`), and send it to a `general-purpose` agent with `model: opus`. If the output file already exists, the agent **resumes** from its PROGRESS block (the template says so). **At most four research agents at once.** The session's web search budget is 1,000 searches shared by every agent, refilling at about 100 an hour; never work around a refusal.

**After each agent finishes:** open its output file and check the PROGRESS block (every pick and FINAL ticked), then mark the tracker:
`python3 Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/inspiration_tracker_set.py <UNIT> <1|2> ✅` (run from the GDD repo root). Never tick a row from the agent's report alone.

**If an agent was cut off (session ended):** its file has unticked PROGRESS boxes. Dispatch the same template again; it reads the file, skips ticked picks and adds a `RESUMED` line.

---

## Round 1 template (first pass on a batch)

> You are a research agent for a worldbuilding project. Read `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Inspiration_Place_Research/_PROTOCOL_AND_BRIEFS.md` in full (the rules, the saved-progress and resume rules, and your round's brief) and, in the same folder, `WHAT_TO_LOOK_FOR.md` in full.
>
> IMPORTANT OVERRIDE on language: `WHAT_TO_LOOK_FOR.md` overrides any line in the protocol that asks you to collect slang, colloquialisms or nicknames. Do NOT hunt for slang, and NEVER write slang, colloquialisms, nicknames or local coinages into the place file. For speech, note only (a line or two) which languages or broad dialect groups are in use. Anything of that kind you happen to find goes ONLY to `slang_found/<UNIT>_R1_slang.md` (format in `slang_found/README.md`; created only if something is found). Proper names of festivals and institutions are fine in the place file.
>
> Your unit is `<UNIT>` and your round is `1`. Read ONLY `inputs/<UNIT>.md` (in the same folder as the protocol file). Write ONLY `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/<UNIT>_Inspiration_Place_Research_R1.md` (plus the slang file if needed). Edit no other file. Do not spawn sub-agents.
>
> Create the output file FIRST, beginning with a PROGRESS block (one `- [ ] <n> <pick name>` line per pick plus `- [ ] FINAL`), then follow the saved-progress rules exactly (tick a pick only when its section is fully written). If the output file already exists when you start, you are resuming: read it, skip ticked picks, continue from the first unticked pick, and add a line `RESUMED <date> <time>`.
>
> Follow the Round 1 brief in the protocol file for each pick: verify the claim the input makes, then collect the facts the brief asks for (setting, the people and how they got there, work and daily life, institutions and customs, festivals, hardships). Tag findings with the K kinds, and the optional [P3]-[P10], [SM:...] and [R] tags where they plainly apply. Cover everyday behavior rules (kind K6: are there any such rules? if so what, how they work, who enforces them; "none found" is valid).
>
> Research FULLY and by the book: a recalled fact is a guess; open and read pages (WebFetch) rather than reporting from snippets; mark each claim SOURCED or UNVERIFIED; log exact search strings and dead ends (and whether each died at the query or at the sources). Use WebSearch in standard mode first and in extended mode for hard-to-find facts. If a search tool tells you the session's search budget is used up, STOP: write a STOP note in your file giving exactly where you stopped, do not work around the limit by any other means, and report it. If a page is refused or blocked, note it and move on; do not retry by another route. Do not compare places to each other and do not write about any fictional setting. American English.
>
> Final reply under 250 words: what you found, the most useful finding per pick in one line each, and what you could not find.

## Round 2 template (deeper pass; needs the Round 1 file to exist)

Same opening paragraph and language override as Round 1 (slang file name `<UNIT>_R2_slang.md`), then:

> Your unit is `<UNIT>` and your round is `2`. Read ONLY `inputs/<UNIT>.md` and the Round 1 file `.../Cities/Research_Logs/<UNIT>_Inspiration_Place_Research_R1.md` (read it IN FULL first; do not repeat it; its closing section lists the open threads and the NOT FOUND items to chase). Write ONLY `.../Cities/Research_Logs/<UNIT>_Inspiration_Place_Research_R2.md` (plus the slang file if needed). Edit no other file. Do not spawn sub-agents.
>
> Create the output file FIRST with a PROGRESS block, then follow the saved-progress rules (resume if the file exists).
>
> Round 2 goes deeper into what Round 1 does not cover: other settings and sub-areas (worker housing, schools, clinics, off-season life), subcultures (occupational, migrant, seasonal, generational, religious, Indigenous), leisure industries and what locals do when visitors leave, third places (halls, clubs, pubs, markets, shared meals), and cultural activities and civic life (festivals with name, date, origin, who runs and attends; cooperatives, councils, mutual aid; rituals; food culture). Chase every NOT FOUND and open thread in the Round 1 file. Cover everyday behavior rules (kind K6). Tag findings with the K kinds and the optional tags.
>
> (Then the same "Research FULLY and by the book" paragraph as Round 1, plus: Do NOT retry any page that Round 1 recorded as blocked or refused by another route.)

---

## Status at the time of writing (2026-10-29, about 10:30)
- **Relung Panen second list (71 candidates, #27 to #97), units B01 to B12.** Round 1: **all twelve done and tracker-ticked.** Round 2: **B01 to B05 done and ticked; B06 and B07 were running; B08 to B12 not started.** Check `_TRACKER.md` (the section at the foot) for the truth.
- Tiers for the 71 are NOT set; the developer sets them after the research. Slang found by chance goes only to `slang_found/`.
- The agent files are in `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Relung_Panen_B<nn>_Inspiration_Place_Research_R<1|2>.md`.
