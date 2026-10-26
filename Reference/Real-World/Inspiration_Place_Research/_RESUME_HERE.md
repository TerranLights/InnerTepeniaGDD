# RESUME HERE: inspiration place research (all cities)

**Written 2026-10-26, at the moment this session's web search budget ran out.** A new session should read this file first, then `_TRACKER.md` (the truth about each unit), then `_PROTOCOL_AND_BRIEFS.md`.

## The web search budget (verified from the tool's own message, 2026-10-26)
> "this session's web search budget is used up (limit: 1000 WebSearch calls shared by every agent in this session; the budget refills at about 100 calls per hour)... do not work around the limit by querying search engines with curl or wget from Bash, or by searching or fetching through a third-party reader, proxy or archive service."

- **A fresh session starts with a clean 1,000 searches; they are shared by every agent in it.** A research unit takes roughly 100 to 150 searches per round (Relung Panen's 26 places took about 1,500 searches per round across four agents). So **one session's budget covers about six to ten unit-rounds.**
- **Never work around the limit.** Do not search through curl, a proxy, a reader or an archive. If a search says the budget is used up, stop and tell the developer.
- The budget message names WebSearch only. WebFetch (opening a known page) did not report a limit, but agents need searches to find pages.
- **Before dispatching, plan the session:** count how many unit-rounds the remaining budget allows, dispatch only that many, and keep a reserve of about 100 searches. Tell agents to record exactly where they stopped if a search is refused (the protocol already says so).

## Where things stand (snapshot; `_TRACKER.md` is authoritative)
- **Relung Panen (separate, 26 candidate places):** both rounds finished 2026-10-26 (eight files in `Cities/Research_Logs/`). Tiers not yet proposed; picks entry not yet written.
- **Mirny subnet, both rounds finished (7 units):** Mirny, Casey, Davis, Ariun Nuur, Kunlun, Zhongshan, Sinheung.
- **Mirny subnet, Shirayuki:** Round 1 finished; **Round 2 was running** (check its file's PROGRESS block).
- **Janbogo subnet:** Concordia Round 1 and Dumont d'Urville Round 1 were running when the budget ran out (check their PROGRESS blocks); **Denison Round 1 stopped at its second search, nothing ticked.**
- **Everything else:** not started (see the tracker, in file order after Janbogo).

## How to continue
1. Open `_TRACKER.md`. For every unit marked ◐, open its file in `Cities/Research_Logs/<unit>_Inspiration_Place_Research_R<n>.md` and read its PROGRESS block and STOPPED note.
2. Resume ◐ units first: dispatch an agent with the standard prompt (section 3 of `_PROTOCOL_AND_BRIEFS.md`); it resumes from its file.
3. Then start the next units in tracker order, at most four agents at a time, Round 1 before Round 2 for each unit.
4. After each agent: check the PROGRESS block (every pick and FINAL ticked), then `Tools/inspiration_tracker_set.py <unit> <1|2> <☐|◐|✅>`.
5. Results go in `Cities/Research_Logs/` beside each city's existing research log; finished pass records are never edited. How to merge is a later decision with the developer.

## Open questions waiting for the developer
- Ariun Nuur's pick "CRISPR": the NSF has no facility by that name; the agent suggested the NSF "CRISP" infrastructure-resilience program as an alternate reading. Keep as written, or change?
- Two of the developer's notes in the picks file do not match sources (Nizhny Tagil has two dominant plants, not one; Wolfsburg's plant was the world's largest factory only until 2022). Logged as facts only; tiers unchanged.

## Exact stop points, 2026-10-26 (all four agents stopped on the search budget; every file has a STOP note)
| Unit and round | Ticked | Stopped at |
|---|---|---|
| Concordia Round 1 | Moscow, Los Angeles | Mexico City, the Iztapalapa Passion Play question (nine open questions listed in the STOP RECORD); Berlin not started |
| Dumont d'Urville Round 1 | none | Singapore, section B, housing (a primary-source search) |
| Denison Round 1 | none | Kowloon Walled City, population and demolition dates (second search) |
| Shirayuki Round 2 | Shibuya | Harajuku, section D (three queries not run); Hongdae and Novosibirsk not started |

