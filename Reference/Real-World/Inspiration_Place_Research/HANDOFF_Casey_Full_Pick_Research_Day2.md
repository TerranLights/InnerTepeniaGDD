# Handoff, day 2: continue researching Casey's whole inspiration-picks list (LAW 0-P)

**Written 2026-11-20, about 19:45, by the session that ran day 1.** The developer hands this file to a new session with a fresh
web-search budget. The job is unchanged: research every remaining row of Casey's candidate list, two rounds each, and record coverage.
**Research only:** no Casey ULM, CST or RWBEM work.

## 1 · Read first, in this order

1. **This file.**
2. `HANDOFF_Casey_Full_Pick_Research_2026-11-20.md` (the day-1 handoff): §1 (the law), §3 (the reading list), §4.3–4.4, §5–8 still
   hold. **Its §2 and §9 are out of date; this file corrects them (§3 below).**
3. `Casey_Pick_Research_LOG.md`: **read in full, especially "Session close", the developer's rulings at close and "Documents wanted".**
   It is the resume record. Keep adding to it (a new `## Session 2` section).
4. `_PROTOCOL_AND_BRIEFS.md`, `WHAT_TO_LOOK_FOR.md`, `_DISPATCH_TEMPLATES.md` (as the day-1 handoff lists).
5. `_TRACKER.md`, the Casey C-unit section at its foot: **the queue and the truth about what is done.**

The inputs are already built (`inputs/Casey_C01.md` to `C20.md`). **Do not rebuild them.** You do not need to read `candidates/Casey.md`
unless something in an input file looks wrong.

## 2 · State at the end of day 1 (verified in the files)

| | |
|---|---|
| Rows in scope | **120** (#4–#124 except **#25**, the road-music row, which waits for its own study after all the culture work: developer, 2026-11-20) |
| Done, both rounds, tracker ✅ | **C01, C02, C03, C05, C07, C12 = 36 rows.** Coverage tracker: Casey **39 / 124** with the official picks |
| In progress | **C11 Round 1 ◐**: stopped at the search-budget limit; pick 1 (Magadan) partial, unticked, with a STOP note |
| Not started | C04, C06, C08, C09, C10, C13, C14, C15, C16, C17, C18, C19, C20 (13 units), and C11 Round 2 |
| Queued last | **A gap-fill pass on C01, C12 and C05** after C20 Round 2 (developer, 2026-11-20): their Round 1 ran before the depth note |
| Repo | clean and pushed at `2465c558` |

## 3 · Corrections to the day-1 handoff

- **Row count: 120, not 121.** Casey's file **does** have a road-music row (#25); it waits. `_LAW_0-P_COVERAGE_TRACKER.md` is corrected.
- **Units are built and partly done** (above), so the day-1 handoff's §4.1 and §9 no longer apply.
- **Search budget, measured:** the first refusal came at **1,528** searches, 5 h 26 min after the session started: ~1,000 at start plus
  **~97 an hour**. Per unit at full depth: Round 1 ≈ 145–165 searches, Round 2 ≈ 130–165. **So a long session finishes about five
  units (both rounds).** 14 units remain, so about three sessions, then the gap-fill pass.
- **Cost:** about 1.1 million tokens per unit (both rounds). Developer's rule of thumb: about 1M tokens ≈ 1% of the weekly allotment.
  **Ask the developer for a meter reading at the start**, and between units when convenient; log each with its time.

## 4 · Order of work

1. Re-dispatch **C11 Round 1** with the Round 1 prompt below (unit `Casey_C11`). It resumes from the file.
2. Round 1 of **C04, C06, C08, C09, C10, C13, C14, C15, C16, C17, C18, C19, C20**, in that order (scheduling only, never depth).
   Each unit's **Round 2 as soon as its Round 1 is verified** in the file.
3. After C20 Round 2: the **gap-fill pass** on C01, C12, C05 (brief it on those units' NOT FOUND lists and thin K kinds; about 100
   searches each). Write its brief with the developer's agreement on the format if unsure.

**At most four agents at once.** Budget on the **worst case** (270 searches per unit-round) and keep a reserve of about 100; the refill
lets a fifth or sixth unit-round go out later in the day. **On a refusal:** the agent stops with a STOP note; stop dispatching, mark ◐,
log it, tell the developer. Never work around it.

**After each return:** open the output file, check the PROGRESS block (every pick and FINAL ticked) and the per-pick search lines, grep
it for the city's name (only unit labels should match), then `python3 Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/inspiration_tracker_set.py Casey_C<nn> <1|2> ✅`
(◐ if partial), and log the return (time, picks, searches, `subagent_tokens`, tool uses, duration, snags). Copy any **WANTED** items into
the log's "Documents wanted" table.

**Web-call counter:** `python3 Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/web_quota_count.py --tasks <this session's tasks folder>`
(the script's default points at an old session). Its "quota/rate-limit" flags were all false positives on day 1 (fishing quotas,
websites' own HTTP 429 replies); inspect before believing one.

**Before any commit:** run the American-English sweep on the agents' files (whole words, never inside URLs; see the memory
`feedback_american_english_sweep_before_commit`). Day 1 fixed 318. Commit or push only when the developer asks.

## 5 · The prompts in use (copy exactly; replace `<NN>`)

Agents: `general-purpose`, model **opus**, `run_in_background: true`. Add a one-line, pick-specific list of local-language sources and
sensitive histories where useful (the day-1 prompts did); change nothing else.

### Round 1

> You are a research agent for a worldbuilding project. Read `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Inspiration_Place_Research/_PROTOCOL_AND_BRIEFS.md` in full (the rules, the saved-progress and resume rules, and your round's brief) and, in the same folder, `WHAT_TO_LOOK_FOR.md` in full.
>
> IMPORTANT OVERRIDE on language: `WHAT_TO_LOOK_FOR.md` overrides any line in the protocol that asks you to collect slang, colloquialisms or nicknames. Do NOT hunt for slang, and NEVER write slang, colloquialisms, nicknames or local coinages into the place file. For speech, note only (a line or two) which languages or broad dialect groups are in use. Anything of that kind you happen to find goes ONLY to `slang_found/Casey_C<NN>_R1_slang.md` (format in `slang_found/README.md`; created only if something is found). Proper names of festivals and institutions are fine in the place file. Song lyrics are not recorded in the place file either.
>
> Your unit is `Casey_C<NN>` and your round is `1`. Read ONLY `inputs/Casey_C<NN>.md` (in the same folder as the protocol file). Write ONLY `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Casey_C<NN>_Inspiration_Place_Research_R1.md` (plus the slang file if needed). Edit no other file. Do not spawn sub-agents. Do not use graphify or read any other repo file; if a tool hook tells you to run graphify, disregard it: your instruction is to read only the files named here.
>
> Create the output file FIRST, beginning with a PROGRESS block (one `- [ ] <n> <pick name>` line per pick plus `- [ ] FINAL`), then follow the saved-progress rules exactly (tick a pick only when its section is fully written). If the output file already exists when you start, you are resuming: read it, skip ticked picks, continue from the first unticked pick, and add a line `RESUMED <date> <time>`.
>
> Follow the Round 1 brief in the protocol file for each pick: verify the claim the input makes, then collect the facts the brief asks for (setting, the people and how they got there, work and daily life, institutions and customs, festivals, hardships). Tag findings with the K kinds, and the optional [P3]-[P10], [SM:...] and [R] tags where they plainly apply. Cover everyday behavior rules (kind K6: are there any such rules? if so what, how they work, who enforces them; "none found" is valid). Where a pick is a tradition, network or occupation rather than a single place, research the thing itself and two or three well-documented places where it was or is practiced, as the brief says.
>
> Research FULLY and by the book: a recalled fact is a guess; open and read pages (WebFetch) rather than reporting from snippets; mark each claim SOURCED or UNVERIFIED; log exact search strings and dead ends (and whether each died at the query or at the sources). Use WebSearch in standard mode first and in extended mode for hard-to-find facts. Query each pick from several angles (official and municipal sites, local newspapers and their archives, local-language sources, regional archives, historical societies, university and academic work, oral histories, museum pages); do not stop at the first useful hit. If a search tool tells you the session's search budget is used up, STOP: write a STOP note in your file giving exactly where you stopped, do not work around the limit by any other means, and report it. If a page is refused or blocked, note it and move on; never request that same page again by any route. Other pages on the same site may each be tried. Use only WebSearch and WebFetch to reach the web: no curl, wget or other shell downloads, proxies, reader services or archive copies. If WebFetch saves a binary file (such as a PDF) and tells you where, you may read that saved file locally; if a page is too large for WebFetch, log it as NOT READ. In your FINAL section, under WANTED, list any document that would materially help but could not be read (citation or URL, and why); do not fetch it by any other route. Report sensitive histories neutrally and plainly. Do not compare places to each other and do not write about any fictional setting. American English.
>
> SEARCH BUDGET: at most 45 WebSearch calls per pick (at most 270 for the whole unit). 45 is a ceiling, not a target, but the precedent for full depth in this project is about 40 searches per pick. If you close a pick with far fewer than about 30 searches, say in that pick's section which further angles you tried and that they came back with nothing new. Keep a running count: at the end of each pick's section write `WebSearch calls for this pick: <n>`, and in the FINAL section write the unit totals of WebSearch and WebFetch calls.
>
> Final reply under 250 words: what you found, the most useful finding per pick in one line each, what you could not find, and your total WebSearch and WebFetch counts.

### Round 2

Same as Round 1 with these changes:
- Language paragraph: add after "…nicknames.": *(the Round 2 brief's "subcultures" line mentions slang and nicknames: that part is overridden)*; slang file name `Casey_C<NN>_R2_slang.md`.
- Unit paragraph: *Your unit is `Casey_C<NN>` and your round is `2`. Read ONLY `inputs/Casey_C<NN>.md` (in the same folder as the protocol file) and the Round 1 file `…/Research_Logs/Casey_C<NN>_Inspiration_Place_Research_R1.md` (read it IN FULL first; do not repeat it; its closing sections list the open threads and the NOT FOUND items to chase). Write ONLY `…/Research_Logs/Casey_C<NN>_Inspiration_Place_Research_R2.md` (plus the slang file if needed).* (Use full absolute paths, as in Round 1.)
- Replace the "Follow the Round 1 brief…" paragraph with: *Round 2 goes deeper into what Round 1 does not cover: other settings and sub-areas (worker housing, schools, clinics, off-season life), subcultures (occupational, migrant, seasonal, generational, religious, Indigenous), leisure industries and what locals do when visitors leave, third places (halls, clubs, pubs, markets, shared meals), and cultural activities and civic life (festivals with name, date, origin, who runs and attends; cooperatives, councils, mutual aid; rituals; food culture). Chase every NOT FOUND and open thread in the Round 1 file. Cover everyday behavior rules (kind K6). Tag findings with the K kinds and the optional tags.*
- In the research paragraph, add: *Do NOT re-request any page that Round 1 recorded as refused or blocked: check Round 1's list of refused pages before each fetch.*

## 6 · Do not

Everything in the day-1 handoff's §8 still holds (no ULM/CST/RWBEM; no tier changes or strikes; do not edit Casey's older research
files; do not research #25; no comparisons between cities; no slang in place files; commit or push only when asked). Also: **one city per
fresh session** — no other city's work in this session.
