#!/usr/bin/env python3
"""Update the 'Per-nation ...' rows of every city's Datasheets/Phase_2.md and Step_1_and_2.md. 2026-11-02.
usage: python3 write_datasheet_rows.py [--apply]
Families: (1) 'Present at Lx-Ly ... not quoted' -> new line range; (2) 'de-stacked, share-weighted model' -> new description
and range; (3) rows that quote figures -> regenerated from final_tables.json in the row's own format."""
import json, re, sys, glob, os
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from apply_final import SPEC_PATH
from write_datasheet_tiers import DIRKEY, PASSES
from write_specs import fmt_share
SPECS = HERE.parent / "Specs"
DESC = ("rebalanced 2026-11-02 (`DR-85`): every country in its latest-period form, the Sinian Federation's decline and refill where it "
        "applies, places never counted before added by time-zone window, tiers relabeled by the largest-ratio-gap rule")


def spec_ranges(city):
    L = (SPECS / SPEC_PATH[city]).read_text(encoding="utf-8").split("\n")
    h = next(i for i, l in enumerate(L) if re.match(r"^\| *Tier *\| *Nation *\|", l))
    ph = max(i for i in range(h) if L[i].startswith("### Per-Nation"))
    j = h + 2
    while L[j].startswith("|"):
        j += 1
    post = next(i for i in range(j, len(L)) if L[i].strip().startswith("*Tier labels follow"))
    return {"ph": ph + 1, "h": h + 1, "last": j, "post": post + 1}


def fig_cell(city, rows, kind):
    out = []
    for x in rows:
        c = x["counts"]
        g = lambda k: f"{c[k]:,}" if len(c) > k and c[k] is not None else "n/a"
        s = fmt_share(x["share"])
        if kind == "casey":
            out.append(f"{x['nation']} {s} (CI: {g(0)}R/{g(1)}H · CII: {g(2)}R/{g(3)}H)")
        elif kind == "ariun":
            out.append(f"{x['nation']} {s} ({g(0)} R / {g(1)} H)")
        elif kind == "denison":
            out.append(f"{x['nation']} {s} — {g(0)} R / {g(1)} H (I); {g(2)} R / {g(3)} H (II).")
        elif kind == "kunlun":
            out.append(f"{x['nation']} {s}/{g(0)}")
        else:
            out.append(f"{x['nation']} {s}")
    return (" " if kind == "denison" else " · ").join(out)


def main():
    apply = "--apply" in sys.argv
    data = json.loads((HERE / "final_tables.json").read_text(encoding="utf-8"))["cities"]
    log = []
    for d in sorted(glob.glob(str(PASSES / "*" / "*" / "Datasheets"))):
        key = DIRKEY.get(os.path.basename(os.path.dirname(d)))
        if key is None or key not in data:
            continue
        R = spec_ranges(key)
        rows = data[key]["rows"]
        for fn in ("Phase_2.md", "Step_1_and_2.md"):
            f = os.path.join(d, fn)
            if not os.path.exists(f):
                continue
            L = open(f, encoding="utf-8").read().split("\n")
            ch = False
            for i, ln in enumerate(L):
                if not ln.startswith("| Per-nation"):
                    continue
                cells = ln.split(" | ")
                # cells[0] = '| label', cells[1] = text, cells[2] = citation + ' |'
                if len(cells) < 3:
                    log.append(("UNPARSED", key, fn, i + 1)); continue
                label, text, cite = cells[0], " | ".join(cells[1:-1]), cells[-1]
                rng_table = f"L{R['h']}–{R['last']}"
                new_text = text
                if "cite by range" in text:
                    new_text = re.sub(r"Present at L\d+–L\d+", f"Present at L{R['ph']}–L{R['post']}", text)
                    cite = re.sub(r"(\.md`?\s+)L\d+(?:[–-]L?\d+)?", lambda m: f"{m.group(1)}L{R['ph']}", cite, count=1)
                elif "share-weighted" in text and "Full " in text:
                    tail = text[text.index("model output, not measured counts") + len("model output, not measured counts"):]
                    new_text = (f"Full {len(rows)}-row table with Census I/II robot and human splits per row exists in the source, {DESC} — "
                                f"**per-nation figures are model output, not measured counts**" + tail)
                    cite = re.sub(r"(\.md`?\s+)L\d+[–-]\d+(?: \(table L\d+[–-]\d+\))?", lambda m: f"{m.group(1)}L{R['ph']}–{R['post']} (table {rng_table})", cite, count=1)
                    label = label.replace("(de-stacked, share-weighted model)", "(rebalanced 2026-11-02)")
                elif key == "Casey" and label.startswith("| Per-nation table, full figures"):
                    new_text = fig_cell(key, rows, "casey")
                    cite = re.sub(r"(\.md`?\s+)L\d+[–-]\d+", lambda m: f"{m.group(1)}{rng_table}", cite, count=1)
                elif key == "Ariun Nuur" and "full table" in label:
                    new_text = fig_cell(key, rows, "ariun")
                    cite = re.sub(r"(\.md`?\s+)L\d+[–-]\d+", lambda m: f"{m.group(1)}{rng_table}", cite, count=1)
                elif key == "Denison" and fn == "Step_1_and_2.md":
                    new_text = fig_cell(key, rows, "denison").rstrip(".")
                    cite = re.sub(r"(\.md`?\s+)L\d+[–-]\d+", lambda m: f"{m.group(1)}{rng_table}", cite, count=1)
                elif key in ("Cape Adare", "Zukelli") and label.startswith("| Per-nation shares"):
                    new_text = fig_cell(key, rows, "shares")
                    cite = re.sub(r"(\.md`?\s+)L\d+[–-]\d+", lambda m: f"{m.group(1)}{rng_table}", cite, count=1)
                    label = re.sub(r"\(model output, de-stacked 2026-07-05\)", "(model output, rebalanced 2026-11-02)", label)
                elif key == "Kunlun":
                    new_text = (f"Full {len(rows)}-row table, Census I robots only (no human population), Option A tiers ({DESC.split(':')[0]}; "
                                f"`DR-85`): Primary — the Sinian Federation alone; the USA and Russia moved to the middle tier; Mongolia and "
                                f"Künnarantaiga added to the middle tier as the founding wave. Share/Census I robots, largest first: "
                                + fig_cell(key, rows, "kunlun") + " *(counts total 135,226, the census figure; the rows after the Option A names "
                                "keep their space-program heritage names, USA, Russia, Canada, UK, Italy, Germany, South Korea and Argentina, until the "
                                "developer rules which successor carries each)*")
                    cite = re.sub(r"(\.md`?\s+)L\d+[–-]\d+", lambda m: f"{m.group(1)}{rng_table}", cite, count=1)
                else:
                    new_text = text
                    cite = re.sub(r"(\.md`?\s+)L\d+[–-]\d+", lambda m: f"{m.group(1)}{rng_table}", cite, count=1)
                new = " | ".join([label, new_text, cite])
                if new != ln:
                    L[i] = new
                    ch = True
                    log.append(("ok", key, fn, i + 1))
            if ch and apply:
                open(f, "w", encoding="utf-8").write("\n".join(L))
    print(("APPLIED" if apply else "dry run"), len([x for x in log if x[0] == "ok"]), "rows;", [x for x in log if x[0] != "ok"])


if __name__ == "__main__":
    main()
