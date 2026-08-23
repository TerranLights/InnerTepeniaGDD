# graphify build plan — Inner Tepenia GDD knowledge graph

**Resumable by design.** Semantic extraction is the expensive part and it is chunked so that a 5-hour token
window running out costs at most one in-flight checkpoint, never the whole run. Everything already extracted
is written to graphify's per-file semantic cache and is replayed for free on the next attempt.

**Scope:** repo root, filtered by `.graphifyignore` — game content, lore, in-world history, and the Tepenian
universe. Real-world source media (`Reference/Materials/` 44 GB, `to-be-integrated/books/`,
`to-be-integrated/treaties/` — 95 PDFs + 19 EPUBs) is excluded; the hand-extracted residue in
`Reference/Real-World/` is kept, since that is the actual data.

**Corpus after filtering:** 62,339 files → **2,763** (2,664 documents · 93 images · 6 papers) · ~3.3M words ·
**137 extraction chunks**.

**Extraction backend: host subagents. This is settled — do not re-raise it.** The developer has no way to set
`GEMINI_API_KEY`/`GOOGLE_API_KEY`, so the Gemini path is unavailable, not merely unconfigured. The host agent
is the LLM, dispatching `general-purpose` subagents per chunk, exactly as the skill's no-key path specifies.
Future sessions should not suggest the key again or treat its absence as a blocker.

---

## How to resume after a window reset

Do exactly this, from the repo root. It is safe to run at any time, including mid-build.

```bash
cd "/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD"
PY=$(cat graphify-out/.graphify_python)
SPEC="/home/kuroskalacs/.claude/skills/graphify/references/extraction-spec.md"

# Re-resolve the interpreter if graphify-out/ was wiped
[ -f graphify-out/.graphify_python ] || { P=$(head -1 "$(which graphify)" | tr -d '#!'); mkdir -p graphify-out; "$P" -c "import sys;open('graphify-out/.graphify_python','w').write(sys.executable)"; PY=$(cat graphify-out/.graphify_python); }

# Ask the cache what is actually left — this is the source of truth, not this file
$PY -c "
import json
from graphify.cache import check_semantic_cache
from pathlib import Path
d = json.loads(Path('graphify-out/.graphify_detect.json').read_text(encoding='utf-8'))
all_files = [f for cat in ('document','paper','image') for f in d['files'].get(cat, [])]
cn, ce, ch, unc = check_semantic_cache(all_files, root='.', prompt_file='$SPEC')
if cn or ce or ch:
    Path('graphify-out/.graphify_cached.json').write_text(json.dumps({'nodes':cn,'edges':ce,'hyperedges':ch}, ensure_ascii=False), encoding='utf-8')
else:
    Path('graphify-out/.graphify_cached.json').unlink(missing_ok=True)
Path('graphify-out/.graphify_uncached.txt').write_text('\n'.join(unc), encoding='utf-8')
print(f'{len(all_files)-len(unc)} cached / {len(unc)} remaining')
"
```

Then pick up at the first unchecked checkpoint below. **The cache is authoritative** — if it disagrees with
the checkboxes in this file, believe the cache and correct the file.

**Do not** run a bare `/graphify` rebuild to resume. That re-runs detect and restarts the pipeline. Resume
means: re-run the cache check above, dispatch the remaining chunks, then continue at the stretch goals.

---

## Phase A — setup ✅ COMPLETE

- [x] Interpreter resolved → `graphify-out/.graphify_python` (pipx venv)
- [x] `.graphifyignore` written and verified (1,117 paths ignored, 3 noise dirs pruned)
- [x] `detect` run → `graphify-out/.graphify_detect.json` (2,763 files, ~5.15M words reported)
- [x] AST pass (Part A) → 0 nodes; this corpus is prose, not code. Expected.
- [x] Cache checked → 0 hits, 2,763 to extract
- [x] Batch plan generated → `graphify-out/.graphify_batchplan.json`

---

## Phase B — semantic extraction (the expensive part)

**14 checkpoints, 137 chunks, ~22 files per chunk.** Each checkpoint = dispatch up to 10 subagents in one
message, then merge and **write the cache**. The cache write is what makes the checkpoint durable — do not
skip it, and do not batch several checkpoints before caching.

> ### ⚠ "Failed: session limit" does NOT mean the agent is dead
> Learned 2026-08-16. When the session limit hits, subagents report `status: failed` — but they are
> **suspended, not terminated**, and several resumed on their own once the window reset and wrote correct
> output hours later. Two chunks completed this way after being written off as lost.
>
> **Before re-dispatching anything after a window reset: run `ListAgents` and check the chunk files on disk.**
> Re-dispatching a chunk whose original is still alive wastes a full agent's budget (~100k tokens) producing a
> byte-identical result. Writes are idempotent so nothing breaks — the cost is pure waste. Check first.

> ### ⚠ Dispatch in waves of 5, not 10
> Learned 2026-08-16, the hard way: a first attempt at B1 dispatched all 10 chunks at once and **all ten died
> on the session limit before a single one wrote its output** — 220 files read, zero yield. Each agent reads
> ~22 lore files (~27k words) before it writes anything, so a wide fan-out spends a lot of budget with nothing
> durable to show for it.
>
> **Dispatch 5 chunks per wave, and write the cache after every wave.** A 10-chunk checkpoint is therefore two
> waves. This halves in-flight exposure and doubles the number of durable save points. The failure itself was
> clean — no partial files, no poisoned cache — which is the design working, but the wasted spend is avoidable.

**Per-checkpoint procedure**
1. Dispatch that checkpoint's chunks **in waves of 5** — each wave's Agent calls in a **single message**,
   `subagent_type="general-purpose"`, each writing an absolute `graphify-out/.graphify_chunk_NN.json`.
   Cache after each wave (step 3) before starting the next.
2. Merge chunk files → `.graphify_semantic_new.json`.
3. `save_semantic_cache(..., allowed_source_files=<this checkpoint's files>, prompt_file=SPEC)`.
4. Tick the box below, note the date.
5. Delete that checkpoint's `.graphify_chunk_*.json` so the next merge does not double-count.

| # | Checkpoint | Landmark(s) | Chunks | Files | Done |
|---|---|---|---|---|---|
| B1 | Locations 1/4 | `Worldspace/Locations-and-Levels` | 10 | ~220 | [x] |
| B2 | Locations 2/4 | `Worldspace/Locations-and-Levels` | 10 | ~220 | [x] |
| B3 | Locations 3/4 | `Worldspace/Locations-and-Levels` | 10 | ~220 | [x] |
| B4 | Locations 4/4 | `Worldspace/Locations-and-Levels` | 6 | ~115 | [x] |
| B5 | Characters 1/4 | `Worldspace/Characters` | 10 | ~220 | [x] |
| B6 | Characters 2/4 | `Worldspace/Characters` | 10 | ~220 | [x] |
| B7 | Characters 3/4 | `Worldspace/Characters` | 10 | ~220 | [ ] |
| B8 | Characters 4/4 | `Worldspace/Characters` | 4 | ~69 | [ ] |
| B9 | Background-Lore 1/2 | `Background-Lore` | 11 | ~242 | [ ] |
| B10 | Background-Lore 2/2 | `Background-Lore` | 11 | ~228 | [ ] |
| B11 | Storyline 1/2 | `Storyline` | 8 | ~176 | [ ] |
| B12 | Storyline 2/2 | `Storyline` | 7 | ~148 | [ ] |
| B13 | Systems & world rules | `Game-Mechanics`, `Worldspace/Factions`, `Worldspace/Enneagram`, `Worldspace/Robot_Biology_and_Culture`, `Worldspace` (loose) | 10 | ~173 | [ ] |
| B14 | Research, drafts & meta | `Reference/Real-World`, `Reference/Images`, `Reference` (loose), `to-be-integrated`, `Neo-Races-and-Cultures`, `Dev-Road-Map`, `Code-Architecture`, `General-Overview-Notes`, `Theoretical-Calculations`, `testing`, root files | 20 | ~292 | [ ] |
| B15 | **Gap-fill pass — mandatory, see warning above** | full-corpus cache check against all 2,763 detected files; dispatch whatever is still uncached (expect a handful of real strays like B2's 20, plus legitimate empty stubs) | — | — | [ ] |

> ### ⚠ A "success" chunk can still silently drop specific files — verify per-checkpoint, don't trust the count
> Learned 2026-08-17 on B2: after caching, 22 of B2's 220 files were still uncached. 2 were the expected
> empty-stub case (harmless, matches B1's pattern). The other **20 were real files** — 9 concept-art `.jpg`s
> (chunk B2_04) and 11 Janbogo-subnet Megasheet files (chunk B2_10) — whose subagents both reported clean
> success with real node/edge counts, yet specific files from their own assigned list never produced a cached
> entry. Most likely cause: a `source_file` value that didn't match `detect`'s path exactly (encoding, an
> apostrophe in "Dumont d'Urville", etc.) — not investigated further because the chunk JSONs were already
> deleted post-merge by the time this was caught.
>
> **Consequence:** a nonzero node/edge count is not proof a chunk's *entire* file list actually got cached.
> **Do not chase individual stragglers mid-run** — it fragments effort. Instead: **after every checkpoint,
> run the cache check scoped to that checkpoint's own file list (not just the merge step) and note the gap
> count** in the log below, then keep moving. **B15 (below, after B14) is a mandatory full-corpus gap-fill
> pass** that catches everything any checkpoint missed, in one pass, before Phase C builds the graph. Do not
> skip B15 even if every checkpoint above looks clean.

**Landmarks** (a whole content area finished — good natural stopping points):
- [x] 🏁 **Locations complete** — after B4. Every district, city, and level in the graph.
- [ ] 🏁 **Characters complete** — after B8. All dolls, NPCs, companions.
- [ ] 🏁 **Historical corpus complete** — after B10. Per-city vignettes and courses of events.
- [ ] 🏁 **Narrative complete** — after B12. Quests, endings, DLC.
- [ ] 🏁 **Extraction complete** — after B14. Ready for the stretch goals.

**Ordering rationale.** Locations and Characters go first because that is where the current district-culture
work lives, so a half-built graph is already useful for it. B13/B14 are the long tail.

---

## Phase C — stretch goals (cheap, but gated on Phase B)

These are near-free compared to extraction, but each needs the one before it.

- [ ] **C1 — Merge semantic + AST** → `.graphify_extract.json` (Step 3 Part C)
- [ ] **C2 — Build, cluster, analyze** → `graph.json`, `GRAPH_REPORT.md` (Step 4)
      Note the `#479` shrink-guard: `to_json` refuses to write a graph smaller than the existing one. If it
      refuses, **do not force past it** — surface the message.
- [ ] **C3 — Graph health check** (Step 4.5, read-only integrity gate)
- [ ] **C4 — Label communities** and regenerate questions with real labels, then re-export (Step 5)
- [ ] **C5 — HTML visualization** (Step 6). ⚠ Honesty rule: warn before running viz on >5,000 nodes.
- [ ] **C6 — Save manifest, cost tracker, final report** (Step 9)

**Optional extras, only on request:** `--obsidian` vault · `--wiki` · `--svg` · `--graphml` · `--neo4j` ·
`--falkordb` · `--mcp`.

---

## Honesty rules in force (from the skill)

- Never invent an edge — unsure means `AMBIGUOUS`.
- Never skip the corpus-size warning. *(Surfaced: 2,763 files / ~5.15M words, flagged expensive. User
  reviewed the cost breakdown and chose full scope.)*
- Always show token cost in the report.
- Never hide cohesion scores behind symbols — show the raw number.
- Never run HTML viz above 5,000 nodes without warning.

---

## Log

| Date | Event |
|---|---|
| 2026-08-16 | Phase A complete. Scope agreed at full (2,763 files) after cost review. Extraction not yet started. |
| 2026-08-17 | B1 (Locations 1/4) complete and cached: 214/214 real files (6 legitimately-empty stub files correctly left unstamped). 1,463 nodes, 3,099 edges, 30 hyperedges. First dispatch (10 at once) died to session limits with zero yield — no damage, but wasteful; switched to waves of 5. Learned mid-checkpoint that "failed: session limit" agents are suspended, not dead, and can resume on their own — check `ListAgents` + disk before ever re-dispatching. Real per-chunk runtime once actually executing is ~5-10 min, not hours. |
| 2026-08-17 | B2 (Locations 2/4) complete and cached: 198/220 files cached, 22 uncached (2 legitimate empty stubs + **20 real files from chunks B2_04 and B2_10 that reported success but never cached** — see warning above). 511 nodes, 834 edges, 30 hyperedges. Added the mandatory B15 gap-fill checkpoint as a direct result. Waves of 5 ran clean this time with zero wasted re-dispatch, after checking `ListAgents` + disk first per the B1 lesson. |
| 2026-08-17 | B3 (Locations 3/4) complete and cached: 220/220 files cached, 0 gaps. 435 nodes, 541 edges, 30 hyperedges. Both waves reported false "failed: session limit" (chunks 2, 4, 5 in wave 1) but all had actually written valid output to disk before the notification fired — confirmed via direct file check, no re-dispatch needed, zero wasted spend. |
| 2026-08-17 | B4 (Locations 4/4) complete and cached: 115/115 files cached, 0 gaps. 201 nodes, 349 edges, 18 hyperedges. Again, 2 of 6 chunks reported false "failed: session limit" but had written valid output; confirmed via disk check, no re-dispatch. **Locations landmark complete** — all districts, cities, and levels are in the graph. |
| 2026-08-17 | B5 (Characters 1/4) complete and cached: 220/220 files cached, 0 gaps. 369 nodes, 349 edges, 23 hyperedges. All 5 wave-2 chunks (6-10) reported false "failed: session limit" but had all written valid output; confirmed via disk check, no re-dispatch, zero wasted spend. |
| 2026-08-22 | Resumed after a rate-limit checkpoint from 2026-08-17. Verified B5 was genuinely cached (967/2763 = exactly B1-B5 combined) before trusting the file's checkboxes, per "cache is authoritative." B6 (Characters 2/4) complete: wave 1 (chunks 1-5, 110 files) was already sitting on disk from before the interruption — verified valid, merged, and cached (110/110, 0 gaps). Wave 2 (chunks 6-10, 110 files) dispatched fresh: 127/220 files cached total for the checkpoint, 93 uncached. Unlike B2's silent-drop bug, every subagent in wave 2 explicitly reported the uncached files as unfilled template placeholders (most of the SHD-02/STP-06/STP-09/STP-10/TCY-02/SE-157/SE-164/IT-021/HKD-172 folders are dev stubs with no real content) — a legitimately high stub rate for this character batch, not a hidden extraction failure. Left for B15 gap-fill to double-check. 132 nodes, 175 edges, 8 hyperedges total for B6. |
