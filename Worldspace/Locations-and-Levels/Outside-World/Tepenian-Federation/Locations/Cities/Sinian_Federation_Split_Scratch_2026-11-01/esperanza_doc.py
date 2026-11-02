import json
from pathlib import Path
P=json.load(open('esperanza_plan.json',encoding='utf-8')); M=json.load(open('esperanza_map.json',encoding='utf-8'))
f=lambda n:f"{n:,}"
rows=[]
for c,v in M.items():
    if c=='Esperanza': continue
    o,n=v['old'],v['new']
    ci_o=o[0]+(o[1] or 0); ci_n=n[0]+(n[1] or 0)
    cii=f"{f(o[2]+(o[3] or 0))} → {f(n[2]+(n[3] or 0))}" if len(o)>3 and o[2] is not None else "—"
    add=f"+{f(n[1]-o[1])} H / +{f(n[0]-o[0])} R" if o[1] else f"+{f(n[0]-o[0])} R"
    rows.append(f"| {c} | {f(ci_o)} → {f(ci_n)} | {add} | {cii} |")
E=P['esperanza_old'];N=P['esperanza_new'];R=P['removed']
txt=f"""# Population scenario: Esperanza's relocation to 1,200,000 (2026-11-02)

> **ADOPTED AND APPLIED 2026-11-02 (`DR-90`).** Developer: *"go with 1,200,000 for Esperanza"* (Option D of 2026-11-01: a smaller Esperanza on Hope Bay, Tabarin Peninsula and ice, with some population relocated). **Arithmetic on the census rows, NOT a migration** (the held-overflow rule applies: no one moved, and no city gains a community or an origin story from it). Method: the Santa Luce scenario's (`DR-68`, `DR-69`).

## How it was built
1. **Esperanza keeps 1,200,000 of its 1,902,205 in Census I** (63.08%). Census II is scaled by the same factor ({P['factor']:.5f}): {f(E[2]+E[3])} → {f(N[2]+N[3])}. Humans and robots are scaled in proportion (Census I {f(E[1])} H / {f(E[0])} R → {f(N[1])} / {f(N[0])}; Census II {f(E[3])} H / {f(E[2])} R → {f(N[3])} / {f(N[2])}). **Removed: Census I {f(R[1])} H + {f(R[0])} R = {f(R[0]+R[1])}; Census II {f(R[3])} H + {f(R[2])} R = {f(R[2]+R[3])}.**
2. **The removed people are divided evenly across the 26 other non-island cities** (the 38 minus the 11 island-labeled cities minus Esperanza). Census I: about {f(R[1]//26)} H and {f(R[0]//26)} R each (integer remainders given one person at a time in census order).
3. **Kunlun and Dome Fuji are robot-only:** their human shares are divided across the 23 other continental cities. **Census II:** four of the 26 have no Census II row by design (Ariun Nuur, Byrd, Kunlun, Dome Fuji), so it is divided across the 22 that do.
4. **Amundsen Station's share is not added to the city.** Census I: all of it goes to the maritime fleet. Census II: it splits 50-50 on average between the space workforce and the maritime fleet.
5. **Each recipient's per-nation table keeps every share; each column is redistributed over its old counts** (largest remainder) so it sums exactly to the new total. National totals are unchanged (Census I 15,623,523 H / 16,403,077 R / 32,026,600; Census II surface 10,486,701 / 11,434,935 / 21,921,636).

## Results (combined)
| City | Census I | Added (Census I) | Census II |
|---|---|---|---|
{chr(10).join(rows)}
| **Esperanza** | {f(E[0]+E[1])} → {f(N[0]+N[1])} | −{f(R[1])} H / −{f(R[0])} R | {f(E[2]+E[3])} → {f(N[2]+N[3])} |
| *Maritime fleet* | 22,982 → 49,991 | +{f(P['groups']['maritime'][1])} H / +{f(P['groups']['maritime'][0])} R | 7,922 → 17,938 |
| *Space workforce* | — | — | 7,923 → 17,941 |

## Esperanza's site (for the extent work, not decided)
At 7,000–10,000 people per km² the 1,200,000 need **120–171 km²** (Census II: 75–108 km²). Hope Bay's own ice-free ground is about 4 km² (Poeiras et al. 2026), so the city is mostly Tabarin Peninsula and ice; ice speed near Hope Bay/Tabarin was NOT FOUND (`Research_Logs/Esperanza_Site_Size_and_Education_Figures_2026-11-01.md`). The Ulu Peninsula (about 250 km², 62–92 km away) is a second site whose role is open.

## Applied the same day
Specs of all 26 cities (headers, per-nation tables, exact sums checked); `Official_Population_Census.md` (city rows, subnet totals, the two group rows, row notes, the national-origin table); the datasheets and Pre-Trips of the changed cities (census rows, the retention rows recomputed, Division of Industry quotes); Division of Industry `09` (Humans, Residents, Workforce columns) and `16` (Half B workforce column; Esperanza's §11 counts refreshed, shares and rulings held); `National_Medical_and_Care_Institutes.md` L173–L177 (3% of a 1.2 M city; 134,897 workers; about 1.6 million students), Division of Industry README L189 (about seven times its own need), the Esperanza `Phase_4` row, Marambio's spec and the extent file (Esperanza's row and callout); Santa Luce's robot-culture sheet.

## NOT done (named)
- **The national food balance** (`04`, `13`, `17`): Esperanza was the country's breadbasket (about 5.1 million people from one city); its farm workforce falls from about 126,700 to about 80,900 while the recipients' baselines grow. The balance must be re-run.
- The per-city determinations in `16` for the 25 recipients (counts still on their old workforces); the `09` Required and % WF columns (superseded model, as before); `08` section 5.2; the Extent table's other cities.
- Culture files, megasheets and other prose that quote the changed cities' old populations (not edited).
"""
out=Path('../../../../../Universal_Location_Methodology/Population_Scenario_Esperanza_Relocation_2026-11-02.md')
out.write_text(txt,encoding='utf-8'); print('ok',out.resolve().name)
