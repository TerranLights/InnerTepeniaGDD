# Division of Industry `04`, `08`, `13`, `15`, `17`: prose pass after the robot term (2026-11-03)

**Result: no number was rewritten.** All five files are dated records of the 2026-09 and 2026-10 model (flat 25% baseline, two-tier, the first three-tier pass, and the 2026-10-28 refresh). Under the policy (dated records get a pointer, never a rewrite), the work was pointers. Line counts are unchanged in all five (04: 436; 08: 775; 13: 931; 15: 528; 17: 83); every pointer was appended to an existing line.

## Pointers added (this pass)
| File | Line | What | Why |
|---|---|---|---|
| `08` | L1 | Title pointer: dated 2026-09-01 method record; flat 25% baseline and national workforce 24,214,839 are first-pass figures; current figures in `16`, `09`, `18` (national row 24,211,482; 43.1 / 15.3 / 41.5; robot term `DR-97`) and `19` section 5 | The file had no pointer; its L500–L507 table (NATIONAL 24,214,839, 25.2%) is the historical flat-baseline run |
| `15` | L1 | Title pointer: dated 2026-09-02 record; its baselines (two-tier 40.6%, three-tier 42.0% at L291–L293), workforce and slack are 2026-09 figures; current figures as above | The file had no pointer |
| `13` | L931 (end of the file's last section) | Pointer: the section's 7.4% slack on 1,150,116 people is the 2026-09 figure; `19` section 5 gives 7.4% again on current inputs (1,156,729 people) by coincidence; current balance +66% with Relung Panen, slack without Relung Panen 2.8% | Two different calculations produce the same 7.4%, which could be mistaken for "the figure never changed" |

## Already carrying pointers (from earlier passes, verified present)
`04` L1 (to `17` and `19`, section 5 for the robot term), `13` L1 (to `17` and `19`, section 5), `17` L1 (superseded by `19` and its section 5). Left as is.

## Places checked and left unchanged, with the reason
- `04` L151–L160 (supply table, workforce 876,515 / 1,400,619, convention C) and L60 (Davis 1,158,314): 2026-09 originals; title pointer covers them.
- `13` L21, L31 (8.09% and 6.4% of the national workforce), L206 (−141,711, 26.0% shortfall), L276, L358 (national baseline 40.6%), L379 (NATIONAL 24,214,838; 59.4%), L559, L846, L871 (+166,583, +70%): the file's narrated 2026-09/10 derivation; title pointer covers them. Not rewritten (dated record; the reasoning is the ruling's history).
- `15` L94 (18,476 FTE = 0.08% of the national workforce), L291–L293, L346–L347, L467, L523 (7.4% specialization slack): dated 2026-09-02 results; the new title pointer covers them.
- `17` L14, L24, L30–L32, L63–L69, L81–L82 (all three conventions, Relung Panen at 108,149 then 102,758, export supply 468,126, slack 9.9%): a dated refresh record, already superseded in its title; conventions A and C are retained records.

## Recomputation
None needed here: no national figure in these five files is a live present-tense statement. The current figures (export supply 420,833; balance +66%; slack 7.4% / 2.8%) are in `19` section 5 and were not re-derived.

## Tool
`audit_city_inputs.py --scope all`: see the report line below.

Audit result: only the known Amundsen Station (1) and Davis (2) gaps; no run-city gaps.
