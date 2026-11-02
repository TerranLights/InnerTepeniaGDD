import json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
M = json.loads((HERE / "esperanza_map.json").read_text(encoding="utf-8"))
D09 = {"Byrd":1.43,"Belgrano":1.43,"Halley":2.50,"Lazar":1.25,"Neumayer":2.50,"Sanay":1.43,"Santa Luce":1.54,"Troll":1.43,"Utstein":1.43,"Cape Adare":1.25,"Concordia":1.67,"Denison":2.00,"Janbogo":1.25,"Zukelli":1.25,"Mawson":1.25,"Ariun Nuur":2.50,"Casey":1.11,"Davis":1.25,"Mirny":1.25,"Relung Panen":1.43,"Shirayuki":1.25,"Sinheung":1.25,"Zhongshan":1.25,"Esperanza":1.11}
def f(n): return f"{n:,}"
def wf(R, H): return int(R + 0.5 * H + 0.5)
def req(H, Res, D): return H * (53 * D + 85.6) / 1000 + Res * (64 * D + 113.2) / 1000
def tokens():
    tok = {}
    conflicts = []
    def add(old, new, who):
        if old == new: return
        if old in tok and tok[old] != new: conflicts.append((old, who)); return
        tok[old] = new
    for c, v in M.items():
        o, n = v["old"], v["new"]
        # [CI R, CI H, CII R, CII H]
        names = ["CI robots", "CI humans", "CII robots", "CII humans"]
        for k in range(len(o)):
            if o[k] is not None and o[k] != n[k]: add(f(o[k]), f(n[k]), c + " " + names[k])
        if len(o) >= 2:
            add(f(o[0] + (o[1] or 0)), f(n[0] + (n[1] or 0)), c + " CI combined")
        if len(o) >= 4 and o[2] is not None:
            add(f(o[2] + (o[3] or 0)), f(n[2] + (n[3] or 0)), c + " CII combined")
    return tok, conflicts
def d09(c):
    v = M[c]; o, n = v["old"], v["new"]; D = D09.get(c)
    if D is None: return None
    o1, n1 = (o[1] or 0), (n[1] or 0)
    ow, nw = wf(o[0], o1), wf(n[0], n1)
    oreq, nreq = round(req(o1, o[0] + o1, D)), round(req(n1, n[0] + n1, D))
    return dict(D=D, old=(o1, o[0] + o1, oreq, ow, round(100 * oreq / ow, 1)), new=(n1, n[0] + n1, nreq, nw, round(100 * nreq / nw, 1)))
if __name__ == "__main__":
    tok, conf = tokens()
    print(len(tok), "tokens; conflicts:", conf)
    for c in M:
        r = d09(c)
        if r: print(f"{c:14s} 09 old {r['old']} -> new {r['new']}")
