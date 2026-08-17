# graphify build plan — Inner Tepenia GDD knowledge graph

**Resumable by design.** Semantic extraction is the expensive part and it is chunked so that a 5-hour token
window running out costs at most one in-flight checkpoint, never the whole run. Everything already extracted
is written to graphify's per-file semantic cache and is replayed for free on the next attempt.

**Scope:** repo root, filtered by `.graphifyignore` — game content, lore, in-world history, and the Tepenian
universe. Real-world source media (`Reference/Materials/` 44 GB, `to-be-integrated/books/`,
`to-be-integrated/treaties/` — 95 PDFs + 19 EPUBs) is excluded; the hand-extracted residue in
`Reference/Real-World/` is kept, since that is the actual data.

**Corpus after filtering:** 62,339 files → **2,763** (2,664 documents · 93 images · 6 papers) · ~3.3M words ·
**137 extraction chunks**. Semantic extraction runs through host subagents (no `GEMINI_API_KEY` set).

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

**Per-checkpoint procedure**
1. Dispatch that checkpoint's chunks — all Agent calls in a **single message**, `subagent_type="general-purpose"`,
   each writing an absolute `graphify-out/.graphify_chunk_NN.json`.
2. Merge chunk files → `.graphify_semantic_new.json`.
3. `save_semantic_cache(..., allowed_source_files=<this checkpoint's files>, prompt_file=SPEC)`.
4. Tick the box below, note the date.
5. Delete that checkpoint's `.graphify_chunk_*.json` so the next merge does not double-count.

| # | Checkpoint | Landmark(s) | Chunks | Files | Done |
|---|---|---|---|---|---|
| B1 | Locations 1/4 | `Worldspace/Locations-and-Levels` | 10 | ~220 | [ ] |
| B2 | Locations 2/4 | `Worldspace/Locations-and-Levels` | 10 | ~220 | [ ] |
| B3 | Locations 3/4 | `Worldspace/Locations-and-Levels` | 10 | ~220 | [ ] |
| B4 | Locations 4/4 | `Worldspace/Locations-and-Levels` | 6 | ~115 | [ ] |
| B5 | Characters 1/4 | `Worldspace/Characters` | 10 | ~220 | [ ] |
| B6 | Characters 2/4 | `Worldspace/Characters` | 10 | ~220 | [ ] |
| B7 | Characters 3/4 | `Worldspace/Characters` | 10 | ~220 | [ ] |
| B8 | Characters 4/4 | `Worldspace/Characters` | 4 | ~69 | [ ] |
| B9 | Background-Lore 1/2 | `Background-Lore` | 11 | ~242 | [ ] |
| B10 | Background-Lore 2/2 | `Background-Lore` | 11 | ~228 | [ ] |
| B11 | Storyline 1/2 | `Storyline` | 8 | ~176 | [ ] |
| B12 | Storyline 2/2 | `Storyline` | 7 | ~148 | [ ] |
| B13 | Systems & world rules | `Game-Mechanics`, `Worldspace/Factions`, `Worldspace/Enneagram`, `Worldspace/Robot_Biology_and_Culture`, `Worldspace` (loose) | 10 | ~173 | [ ] |
| B14 | Research, drafts & meta | `Reference/Real-World`, `Reference/Images`, `Reference` (loose), `to-be-integrated`, `Neo-Races-and-Cultures`, `Dev-Road-Map`, `Code-Architecture`, `General-Overview-Notes`, `Theoretical-Calculations`, `testing`, root files | 20 | ~292 | [ ] |

**Landmarks** (a whole content area finished — good natural stopping points):
- [ ] 🏁 **Locations complete** — after B4. Every district, city, and level in the graph.
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
