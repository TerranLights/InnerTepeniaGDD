# Mirny — Step 3 · `T8` Rounds

**Read set:** `.t8_required_03_Step3.txt` — runbook Step 3 (L2567–2661), `02_Spine.md`, `Research_Logs/README.md`. Readers did the web research themselves.

## Round 1 — three research readers (12:02 → 13:14 / 13:21 / 13:43)

- `.t8_Step3_readerA.md` (60 searches) · `.t8_Step3_readerB.md` (70) · `.t8_Step3_readerC.md` (70)
- ⚠ **Session web-search cap reached (200 of 200, shared across all three).** Later picks went fetch-only. Collides with LAW 0-R "no search budget" — a tool limit, not exhausted research. Each reader logged its NOT-SPENT picks.
- ⚠ **Shared scratch folder:** reader B's day-length script was overwritten by a sibling's and B saw its output once (B's own figures predate that). Day-length agreement between readers is therefore not fully blind.
- ⚠ Two readers caught the web-fetch summarizer inventing quote-marked text; both re-verified by direct text search.

## Round 2 — raw output

```
required files: 3
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2567-2661] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/02_Spine.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/README.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

## Round 3 — `SendMessage` to the same three readers (13:45)

| From → about | Verdict |
|---|---|
| A → B, A → C | **CONSISTENT**, **CONSISTENT** |
| B → A, B → C | **CONSISTENT**, **CONSISTENT** |
| C → A, C → B | **CONSISTENT**, **CONSISTENT** |

**Gate: Round 2 UNANIMOUS + Round 3 6/6 CONSISTENT → cleared; `03_Research.md` written.** Settled by concession:
the sea-ice window (ASPA 127 governs; A withdrew "about a month"), drift fills windward first (A conceded), the
upwind warning line has no demonstrated lead time (A withdrew its per-km figure), USNO's solstice figure governs, the
winter daily cycle is unknown (B and C withdrew "no winter lull"), the clear sky is an honest, misread cue (all
three). Research-log corrections appended to `Mirny_Research_Log.md`.

**Later (not asked):** search-cap vs LAW 0-R; per-reader scratch folders for future T8 dispatches; American-English law vs verbatim search strings (readers flagged); WebFetch summaries can fabricate quotes.
