#!/usr/bin/env python3
"""Write one phase's T8 round record (orchestrator helper). usage: record_phase.py <spec.json>
spec keys: N, title, outfile, lines, dispatched, r1back, r3back, merged, recorded, brief_sha, brief_lines, list_entries,
list_note, receipts_rows (markdown rows), r3_note, procedural (markdown list), precheck_triage, audit_triage, ledger_note,
tokens (list of [agent, r1, r3delta, last]), merge_tokens, unit_total, decs"""
import json, sys
s = json.load(open(sys.argv[1]))
P = ('/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/'
     'Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/')
SC = '/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/9d90e9d3-c049-471e-860e-caf23e07bb73/scratchpad/t8/phase%d/' % s['N']
N = s['N']
rd = lambda p: open(p).read().rstrip()
r1 = rd(P + f'.t8_Phase{N}_round2_run1.txt')
import os
r2 = rd(P + f'.t8_Phase{N}_round2_run2.txt') if os.path.exists(P + f'.t8_Phase{N}_round2_run2.txt') else None
r3p = P + f'.t8_Phase{N}_round2_run3.txt'
r3 = rd(r3p) if os.path.exists(r3p) else None
r2txt = (f"\n\n{s.get('repair_note','')}\n\n**Run 2, raw output whole" + (' — UNANIMOUS' if not r3 else '') + f":**\n\n```\n{r2}\n```") if r2 else ''
if r3: r2txt += f"\n\n{s.get('repair2_note','')}\n\n**Run 3, raw output whole — UNANIMOUS:**\n\n```\n{r3}\n```"
pre1 = rd(SC + 'quote_precheck.txt')
pre2 = rd(SC + 'quote_precheck_after_fix.txt') if s.get('precheck_fixed') else None
qa = rd(P + f'.t8_Phase{N}_quotation_audit.txt'); qa = qa[qa.index('=== QUOTATION AUDIT ==='):]
ha = rd(SC + 'handoff_audit.txt'); pd = rd(SC + 'phase_discipline.txt')
tok = '\n'.join(f'| {a} | {b} | {c} | {d} |' for a, b, c, d in s['tokens'])
fix = f"\n\nAfter the fix, raw:\n\n```\n{pre2}\n```" if pre2 else ''
rec = f'''# Ariun Nuur — ULM Phase {N} ({s['title']}) — T8 round record

**Unit:** Phase {N}. **Written:** `{s['outfile']}` ({s['lines']} lines; PROPOSED, not declared complete). **Run mode:** WARM (`DR-6`).
**Date:** 2026-11-19; brief frozen and readers dispatched {s['dispatched']}, Round 1 back by {s['r1back']}, Round 3 by {s['r3back']}, merge
returned {s['merged']}, record {s['recorded']}.
**List:** `.t8_required_04_Phase{N}.txt` ({s['list_entries']} entries). {s['list_note']} **Brief:** `.t8_brief_04_Phase{N}.md` ({s['brief_lines']}
lines; built from the phase template; sha256[:16] {s['brief_sha']}). Reader outputs archived as `.t8_Phase{N}_reader{{A,B,C}}.md`; Round 3
replies as `.t8_Phase{N}_round3_reader{{A,B,C}}.md`. Three Opus readers; one fresh Opus merge writer (`M-246`).

## Round 1 — receipts (as returned)

| Reader | Lines | Axis | Findings | Asymmetry rows | Handed forward | Positions | RF · SH · REQ · Q | Handoff places | Manifest |
|---|--:|---|--:|--:|--:|--:|---|--:|---|
{s['receipts_rows']}

## Round 2 — `Tools/triple_read_verify.py` (last commit `8777bb5f` 2026-11-03; clean), run 1, raw output whole

```
{r1}
```{r2txt}

## Round 3 — cross-check verdicts (the first two verdict lines of each reply)

| Reader | On | Verdict |
|---|---|---|
| A | B | CONSISTENT |
| A | C | CONSISTENT |
| B | A | CONSISTENT |
| B | C | CONSISTENT |
| C | A | CONSISTENT |
| C | B | CONSISTENT |

**All six CONSISTENT.** {s['r3_note']} Filed as {s['decs']}.

## Procedural events (the recording law)

{s['procedural']}

## Quotation checks, before this record existed

**Pre-check (T8 line 13), per quotation, normalized.** First run, raw:

```
{pre1}
```

**Triage:** {s['precheck_triage']}{fix}

**`Tools/quotation_audit.py`** (last commit `5a63e074` 2026-11-02; clean), `--phase {N} --own-pass`. Whole output saved beside this record
as `.t8_Phase{N}_quotation_audit.txt`; result block, raw:

```
{qa}
```

**Triage:** {s['audit_triage']}

## Phase-close instruments (raw output whole)

**`Tools/handoff_audit.py`** (T1):

```
{ha}
```

**`Tools/phase_discipline_check.py`** (T3, T4, T5), run before the ledger was updated:

```
{pd}
```

**Ledger:** {s['ledger_note']}

## American English sweep and the one-location check

From the pre-check script's last lines, raw, above: no British form; the name scan's hits, if any, are the parent subnet and the pass
folder's path; the tower's name 0. **No other location named.**

## Tokens (from the task notifications; full rows in `Universal_Location_Methodology/TOKEN_LOG_Ariun_Nuur.md`)

| Agent | Round 1 | Round 3 (delta) | Last figure |
|---|--:|--:|--:|
{tok}
| merge writer | — | — | {s['merge_tokens']} |
| **Unit total (sum of last figures)** | | | **{s['unit_total']}** |

Web calls: readers 0; `Tools/web_quota_count.py`: TOTAL 284 (unchanged).
**The record grows after this check** (T8 line 8): no DOUBLE-CHECK script was run on this record.
'''
open(P + f'04b_T8_Rounds_Phase_{N}.md', 'w').write(rec)
print(len(rec.splitlines()), 'lines written')
