# Handoff: research Casey's whole inspiration-picks list (LAW 0-P)

**Written 2026-11-20, about 13:40, by the session that ran the Ariun Nuur ULM run.** The developer will hand this file to a new session that
has a fresh web-search budget. Their request, verbatim: *"In that session, I'll need you to fully research the inspirational pics for
Casey."*

**The job, in one line:** research every row of Casey's candidate list that has not been researched yet, **rows #4 to #124 (121 rows),
two rounds each**, by the standing inspiration-place research protocol in this folder, and record the coverage.

This is **research only**. It is not a Casey ULM, CST or RWBEM run. Nothing in it is a conclusion about the fictional city.

---

## 1 · Why (the law)

**LAW 0-P** (project `CLAUDE.md`; filed as `DR-144` in `Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md`, 2026-11-20): every item
on a location's inspiration-picks list is researched and incorporated, **not only the top tiers**. "The list" is the official picks plus
**every row of the candidate list**, whatever its tier. **The tiers decide only how prominently a pick figures in the place, never how thoroughly it is researched** (amended 2026-11-20, `DR-145`): every row gets the same full depth. Developer:
*"That's the whole reason why those items are on the list. I wouldn't have made that list if the results didn't matter."*

The Mirny subnet's passes were researched on the official picks only, so the subnet is to be re-run (developer, 2026-11-19). Casey is the
first city of that catch-up. **The other seven Mirny cities wait until the developer brings them up.**

**LAW 0-R** applies to every agent: research fully; a pick is not used up because it has been searched once; query from several angles;
log dead ends.

## 2 · Where Casey stands (verified 2026-11-20 from the files named)

| What | State | Source |
|---|---|---|
| Candidate list | **124 rows** (#1–#124). #1–#3 are the official picks (`[EXISTING]`); #85–#124 were added in the 2026-10-27 top-up | `candidates/Casey.md` §2 (L34–165) |
| Rows researched | **3 of 124**: the official picks (Flagstaff, Memphis, Reno), both rounds | `_TRACKER.md` row `Casey`; `Cities/Research_Logs/Casey_Inspiration_Place_Research_R1.md` and `_R2.md` |
| Rows to research now | **121** (#4–#124) | `_LAW_0-P_COVERAGE_TRACKER.md` L30 and L93 |
| Solo road-travel music (the subnet-wide developer row) | **Not in Casey's file, and not researched now.** It waits for its own study after the CST (developer, 2026-11-19) | `_LAW_0-P_COVERAGE_TRACKER.md` L86–89; `candidates/_DEVELOPER_ADDITIONS.md` |
| Tiers | Each row carries a **suggested** tier only; the developer gave "no strikes or tier changes" at the 2026-10-27 review | `candidates/Casey.md` L36; `candidates/_REVIEW_PROGRESS.md` L5 |
| Open review points | **Rows 76 (Warsaw) and 118 (Shuri Castle)** are marked OPEN (both rebuilt after destruction). **Research them anyway** (LAW 0-P: no row is left out); note the open point in their unit's input file | `candidates/_REVIEW_PROGRESS.md` L5 |
| Doubtful details in the top-up | The care notes on #85, #88, #89, #92, #95–#98, #101, #104, #105, #110, #111, #115, #118, #121 flag uncertain dates, heights and whether events still run; #96 needs a light-band check. Carry each care note into the input file as a thing to verify | `candidates/Casey.md` §4 (L197–203) |

## 3 · Read first (in this order)

1. **This file.**
2. `_PROTOCOL_AND_BRIEFS.md`: the rules, where results go, the two round briefs, the save-and-resume rules, the agent prompt (63 lines).
3. `_DISPATCH_TEMPLATES.md`: the Round 1 and Round 2 prompts as actually used for Relung Panen's 71 candidates, with the language override
   (45 lines). **Use these templates.**
4. `WHAT_TO_LOOK_FOR.md`: kinds K1–K14, the tags, the language caution (44 lines).
5. `_TRACKER.md` (the Relung Panen B-unit section at its foot is the model for Casey's units) and `_LAW_0-P_COVERAGE_TRACKER.md`.
6. `candidates/Casey.md` in full (203 lines): the facets (§1), the 124 rows (§2), the gaps (§3), the top-up note (§4).
7. One finished input file as a format model: `inputs/Relung_Panen_B01.md`.

The orchestrator reads `candidates/Casey.md` to build the units. **A research agent reads only its own unit's input file** (the one-location
rule), never the candidate list, Casey's spec or any other city's file.

## 4 · The plan

### 4.1 Build the units
- **About 20 units of 6 rows** (121 rows: 19 units of 6 and 1 of 7, or 20 of 6 and 1 of 1; choose what groups cleanly). Name them
  **`Casey_C01` … `Casey_C20`** (the name `Casey` is already the official-picks unit).
- **Group rows that share facets**, as Relung Panen's B-units were grouped by theme. Tier does not change depth or scope
  (`DR-145`); taking the higher suggested tiers first is fine for scheduling, never for depth.
- **Each unit's file** `inputs/Casey_C<nn>.md` follows `inputs/Relung_Panen_B01.md`: a header saying it holds only this unit's picks and
  that the agent reads no other file; then one line per row: **the row number, the place, `// claim to test:` the row's "why it
  parallels" text (an unverified drafting guess), `// care:` its care note.** Keep the K tags the row already carries.
  ⚠ Candidate files can name other Tepenian cities (the 2026-10-30 walk-through noted it). A name scan of `candidates/Casey.md` on
  2026-11-20 found one, in its header (L5, a note about the drafting), and **none in the rows**. Copy rows only, never the header; if a
  row does turn out to name another Tepenian city, strip the name (the real-world place names stay).
- **Add the units to `_TRACKER.md`** as a new section at its foot, in the same form as the Relung Panen B-unit section (a dated note, then
  one row per unit: unit, city, subnet, picks, Round 1 ☐, Round 2 ☐, theme and row range). `Tools/inspiration_tracker_set.py` needs the
  rows to exist before it can tick them.

### 4.2 Dispatch
- **Round 1 template** from `_DISPATCH_TEMPLATES.md`, filled with `<UNIT>` = `Casey_C<nn>`. Agents: `general-purpose`, **Opus**.
- **At most four agents at once**; dispatch the next unit as a slot frees. **Round 2 of a unit only after its Round 1 is finished**
  (every pick and FINAL ticked).
- Outputs: `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Casey_C<nn>_Inspiration_Place_Research_R<1|2>.md`;
  stray slang only to `slang_found/Casey_C<nn>_R<n>_slang.md`.
- **Put an explicit search budget in every prompt** (for example "use at most 45 WebSearch calls per pick"). Agents told a number stayed
  at or under it (memory, 2026-11-01).

### 4.3 After each agent
1. Open its output file and check the PROGRESS block yourself (every pick ticked, FINAL ticked). **Never tick from the agent's report.**
2. `python3 Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/inspiration_tracker_set.py Casey_C<nn> <1|2> ✅`
   (from the repo root); ◐ if it stopped part-way.
3. Log the unit (see §6).

### 4.4 When rows are done
Update Casey's row in `_LAW_0-P_COVERAGE_TRACKER.md` (L30, and L93 in the Mirny table): *researched / 124*, the date, and the files that
hold the research. **Never mark LAW 0-P met (✅)**: that also needs each pass (ULM, CST, RWBEM) to have read the whole list, which is the
re-run's business.

## 5 · The web-search budget: this will take several sessions

- **1,000 WebSearch calls per session, shared by every agent** (the developer's setting, `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`; never
  change it). The tool's own refusal message (2026-10-26) said the budget refills at about 100 calls an hour.
- **The precedent:** about 40–45 searches per pick per round (`_RESUME_HERE.md` L50 and L62). **121 rows × 2 rounds × 40–45 ≈ 9,700–10,900
  searches.** At 1,000 at a session's start plus about 100 an hour, one long day gives roughly 2,000. **So expect about five to six days
  of research**, carried across sessions by the save-and-resume rules (each file's PROGRESS block is the state; `_TRACKER.md` is the queue).
- **Plan each session before dispatching:** count the unit-rounds the budget allows, keep a reserve of about 100, launch the
  highest-tier units first.
- **On a refusal:** the agent stops and writes a STOP note in its file. **Never work around it** (no curl, proxy, reader or archive
  search). Stop dispatching, log it, tell the developer.
- `Tools/web_quota_count.py` gives a count of this session's calls, but it **read 0 partway through the Ariun Nuur run after reading 284**.
  Use the agents' own counts as well, and say which you used.
- **Depth is the developer's call.** The protocol's two full rounds are the standing rule (developer, 2026-10-26: *"two rounds at full
  depth for every city"*), and this plan follows it. If the developer wants it faster (for example one round now, the second later), that
  is theirs to say; do not cut depth on your own.

## 6 · Logging (the developer asked for this during the Ariun Nuur run)

Create **`Casey_Pick_Research_LOG.md`** in this folder at the start, and keep it current; resume from it, not from memory.
- **Per dispatch:** time, unit, round, agent ID.
- **Per return:** time, picks ticked, the agent's search count, `subagent_tokens`, tool uses, duration, anything notable (STOP note,
  refusals, blocked pages, a row that turned out not to exist as listed).
- **Allotment-meter readings:** the developer is home and can give the weekly meter reading between units. **Ask at the start, record
  each reading with its time**, and note what ran in between. (The Ariun Nuur run's figure is provisional because its starting reading
  was not clean; get a clean one here.)
- **Per session close:** web calls used (agents' counts and the tool's), units finished and ◐, the next unit to dispatch.
- **Snags and self-corrections** too, not only successes (the recording law, Step 9.5).

## 7 · Hours

`_SESSION_RESUME_2026-10-29.md` L12 records: *"ULM/CST/RWBEM/district/character work only 05:00 to 14:59 (wrap-up 13:59); research agents
and mechanics are any hour."* So this research is **not** bound to the 05:00–14:59 window by that record. Check the clock anyway, and if
the developer says otherwise, their word governs.

## 8 · Do not

- Start a Casey ULM, CST or RWBEM run, or any other city's work (one city per fresh session; the Kunlun ULM run is the week of 2026-11-29).
- Edit `Cities/Inspirational-Influences.md`, set or change tiers, or strike rows (the developer's).
- Edit Casey's existing research files (`Casey_Inspiration_Place_Research_R1/R2.md`, `Casey_Research_Log.md`) or any finished pass
  record. **How the new research is merged into Casey's passes is a later decision with the developer.**
- Research the solo road-travel music row (it waits for its own study after the CST).
- Compare Casey with any other city, or have an agent read another city's files.
- Collect slang, nicknames or local coinages in the place files.
- Commit or push without being asked.

## 9 · State at the time of writing

- The repo is clean at `24d72cec` (the Ariun Nuur run's day 3, pushed 2026-11-20).
- Nothing for this job has been built yet: no `inputs/Casey_C*.md`, no tracker rows, no log file.
- The developer's open questions from the Ariun Nuur run (`DEC-708` to `DEC-1105` in `Cities/Research_Logs/DECISIONS_NEEDED_FROM_DEVELOPER.md`)
  are separate from this job.
