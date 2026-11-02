#!/usr/bin/env python3
"""China-decline scenario (developer's idea, 2026-11-01 ~22:15). SCRATCH, read-only on every repo file.

Question: what happens to the city figures if, by the Falkland Treaty, China's population is about
1/2 to 2/3 of today's?

Reads (never writes): each city's per-nation table in Specs/, the effective-pool table in
Upper_Earth_Immigration_Composition.md (L68-L110). Prints markdown tables to stdout.

Three readings are computed:
  1. THE METHOD AS WRITTEN: a city's shares come from tiers (Primary 8 shares, Significant 3, Notable 1),
     and the Primary tier is the nations above the largest ratio gap at the top of the pool ranking
     (Upper_Earth_Immigration_Composition.md L17, L1107-L1109). A smaller China pool changes a city only
     if it changes who is Primary.
  2. DIRECT, CITY SHRINKS: China's head count in the city x f, every other nation unchanged.
  3. DIRECT, CITY KEEPS ITS SIZE: China's share x f, the freed share spread over the other nations in
     proportion to their present shares.
"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
CITIES = HERE.parent
SPECS = CITIES / "Specs"
COMP = CITIES / "Upper_Earth_Immigration_Composition.md"

CITY_FILES = {
    "Zhongshan": "Mirny subnet/Zhongshan.md",
    "Dumont d'Urville": "Janbogo subnet/Dumont_dUrville.md",
    "Mirny": "Mirny subnet/Mirny.md",
    "Zukelli": "Janbogo subnet/Zukelli.md",
    "Relung Panen": "Mirny subnet/Relung_Panen.md",
    "Janbogo": "Janbogo subnet/Janbogo.md",
    "Davis": "Mirny subnet/Davis.md",
    "Temirötkel": "Mawson subnet/Temirotkel.md",
    "Mawson": "Mawson subnet/Mawson.md",
    "Denison": "Janbogo subnet/Denison.md",
    "Cape Adare": "Janbogo subnet/Cape_Adare.md",
    "Scott": "Janbogo subnet/Scott.md",
    "Fort McMurdo": "Janbogo subnet/Fort_McMurdo.md",
    "Amundsen Station": "Amundsen-Scott subnet/Amundsen_Station.md",
    "Casey": "Mirny subnet/Casey.md",
    "Kunlun": "Mirny subnet/Kunlun.md",
    "Dome Fuji": "Mawson subnet/Dome_Fuji.md",
    "Sinheung": "Mirny subnet/Sinheung.md",
    "Concordia": "Janbogo subnet/Concordia.md",
    "Shirayuki": "Mirny subnet/Shirayuki.md",
    "Byrd": "Byrd subnet/Byrd.md",
    "Palmer City": "Palmer subnet/Palmer_City.md",
}
EXEMPT = {"Zhongshan", "Kunlun"}  # developer: set up by the Sinian Federation
# Cities whose tables were built by the standard tier method (no hand re-tiering of the top), China Primary
TIER_METHOD_CITIES = ["Dumont d'Urville", "Mirny", "Zukelli", "Relung Panen", "Janbogo", "Davis",
                      "Temirötkel", "Mawson", "Denison", "Cape Adare", "Scott", "Fort McMurdo",
                      "Amundsen Station", "Casey", "Dome Fuji"]

ROW = re.compile(r"^\|\s*(Primary|Significant|Notable)[^|]*\|\s*([^|]+?)\s*\|\s*([0-9]+\.[0-9]+)\s*%\s*\|(.*)$")


def read_table(path):
    """First contiguous block of tier rows whose shares sum to ~100%. Returns list of
    (tier, nation, share, census_I_humans or None)."""
    lines = path.read_text(encoding="utf-8").splitlines()
    blocks, cur = [], []
    for ln in lines:
        m = ROW.match(ln)
        if m:
            tier, nation, share, rest = m.groups()
            nation = re.sub(r"\*.*?\*|\(.*?\)", "", nation).strip()
            cells = [c.strip().replace(",", "") for c in rest.split("|")]
            nums = [int(c) for c in cells if c.isdigit()]
            humans = nums[1] if len(nums) >= 2 else None  # CI robots, CI humans[, CII robots, CII humans]; Byrd has no CII (fixed 2026-11-01 ~23:50: was >= 4, which dropped Byrd's 5,853)
            cur.append((tier, nation, float(share), humans))
        elif cur:
            blocks.append(cur)
            cur = []
    if cur:
        blocks.append(cur)
    for b in blocks:
        if abs(sum(r[2] for r in b) - 100) < 1.5:
            return b
    raise ValueError(f"no ~100% table in {path}")


def read_pools():
    pools = {}
    for ln in COMP.read_text(encoding="utf-8").splitlines()[66:111]:
        m = re.match(r"^\|\s*([A-Za-z .]+?)\s*\|\s*~([0-9.]+)M\s*\|", ln)
        if m:
            pools[m.group(1)] = float(m.group(2))
    return pools


def primary_set(pool_of, nations, max_pos):
    """Nations above the largest ratio gap among the first max_pos boundaries of the ranking."""
    ranked = sorted(nations, key=lambda n: -pool_of[n])
    best_i, best_r = 1, 0.0
    for i in range(1, min(max_pos, len(ranked) - 1) + 1):
        r = pool_of[ranked[i - 1]] / pool_of[ranked[i]]
        if r > best_r:
            best_i, best_r = i, r
    return set(ranked[:best_i]), ranked


def tier_share(rows, primaries):
    w = {}
    for tier, nation, _, _ in rows:
        if nation in primaries:
            w[nation] = 8
        elif tier == "Primary":
            w[nation] = 3  # dropped out of Primary -> Significant
        else:
            w[nation] = {"Significant": 3, "Notable": 1}[tier]
    tot = sum(w.values())
    return {n: 100 * v / tot for n, v in w.items()}


def main():
    pools = read_pools()
    tables = {c: read_table(SPECS / f) for c, f in CITY_FILES.items()}
    F = [("two-thirds", 2 / 3), ("half", 1 / 2)]

    # ---------- Reading 1: the method as written ----------
    print("## Reading 1: the method as written (tiers)\n")
    print("China's pool: today 210M; two-thirds 140M; half 105M. Primary = nations above the largest ratio gap "
          "among the top two boundaries (\"typically the top 1-2\"); a third boundary is shown where it would "
          "change the answer. Shares are the plain 8/3/1 shares before de-stacking.\n")
    print("| City | Primary today (rule check) | China today | Two-thirds: Primary | China | Half: Primary | China | Half, if a third place may join |")
    print("|---|---|--:|---|--:|---|--:|---|")
    for c in TIER_METHOD_CITIES:
        rows = tables[c]
        nations = [r[1] for r in rows]
        missing = [n for n in nations if n not in pools]
        if missing:
            print(f"| {c} | pools missing for {missing} | | | | | | |")
            continue
        actual_primary = {r[1] for r in rows if r[0] == "Primary"}
        out = [c]
        for label, f in [("today", 1.0)] + F:
            pool_of = dict(pools)
            pool_of["China"] = 210 * f
            prim, ranked = primary_set(pool_of, nations, 2)
            sh = tier_share(rows, prim)
            if f == 1.0:
                ok = "matches" if prim == actual_primary else f"DIFFERS (spec: {', '.join(sorted(actual_primary))})"
                out.append(f"{', '.join(sorted(prim, key=lambda n: -pool_of[n]))} ({ok})")
            else:
                out.append(", ".join(sorted(prim, key=lambda n: -pool_of[n])))
            out.append(f"{sh['China']:.1f}%")
            if f == 0.5:
                prim3, _ = primary_set(pool_of, nations, 3)
                if prim3 != prim:
                    sh3 = tier_share(rows, prim3)
                    out.append(f"{', '.join(sorted(prim3, key=lambda n: -pool_of[n]))}: China {sh3['China']:.1f}%")
                else:
                    out.append("same")
        print("| " + " | ".join(out) + " |")

    # ---------- Readings 2 and 3: direct ----------
    print("\n## Readings 2 and 3: China's people cut directly\n")
    print("| City | China today (spec) | China rank today | Two-thirds, city shrinks | Two-thirds, city keeps size | Half, city shrinks | Half, city keeps size | Largest other nation today | China's rank at half (shrinks / keeps size) |")
    print("|---|--:|--:|--:|--:|--:|--:|---|--:|")
    nat_china_now = 0
    nat_china = {lbl: 0.0 for lbl, _ in F}
    for c, rows in tables.items():
        shares = {r[1]: r[2] for r in rows}
        humans = {r[1]: r[3] for r in rows}
        tot = sum(shares.values())
        s = 100 * shares["China"] / tot
        ranked = sorted(shares, key=lambda n: -shares[n])
        rank = ranked.index("China") + 1
        other = [n for n in ranked if n != "China"][0]
        h = humans.get("China") or 0
        nat_china_now += h
        cells = [c + (" *(exempt)*" if c in EXEMPT else ""), f"{s:.2f}%", f"{rank} of {len(ranked)}"]
        for lbl, f in F:
            ff = 1.0 if c in EXEMPT else f
            shrink = 100 * ff * s / (100 - s + ff * s)
            keep = ff * s
            cells += [f"{shrink:.1f}%", f"{keep:.1f}%"]
            nat_china[lbl] += h * ff
            if lbl == "half":
                # city shrinks: China x f against the others unchanged
                new = dict(shares)
                new["China"] = shares["China"] * ff
                rk_shrink = sorted(new, key=lambda n: -new[n]).index("China") + 1
                # city keeps size: others scaled up in proportion to fill the gap
                scale = (tot - shares["China"] * ff) / (tot - shares["China"])
                new2 = {n: (v * ff if n == "China" else v * scale) for n, v in shares.items()}
                rk_keep = sorted(new2, key=lambda n: -new2[n]).index("China") + 1
        cells += [f"{other} {100 * shares[other] / tot:.2f}%", f"{rk_shrink} / {rk_keep}"]
        print("| " + " | ".join(cells) + " |")

    print("\n## Nationally (Census I humans; Zhongshan and Kunlun left as they are)\n")
    total_now = 15_623_523
    print(f"- China-origin humans summed from these specs: {nat_china_now:,} "
          f"({100 * nat_china_now / total_now:.1f}% of 15,623,523)")
    for lbl, _ in F:
        lost = nat_china_now - nat_china[lbl]
        print(f"- {lbl}: {nat_china[lbl]:,.0f} China-origin humans; if cities shrink, Tepenia has "
              f"{total_now - lost:,.0f} humans (-{lost:,.0f}, -{100 * lost / total_now:.1f}%) and China is "
              f"{100 * nat_china[lbl] / (total_now - lost):.1f}% of them; if cities keep their size, China is "
              f"{100 * nat_china[lbl] / total_now:.1f}%")


if __name__ == "__main__":
    main()
