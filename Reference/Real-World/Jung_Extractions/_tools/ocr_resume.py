#!/usr/bin/env python3
"""ocr_resume.py -- OCR a page range of an image-based PDF, resuming where an existing output file stopped.

Usage:
  python3 ocr_resume.py <pdf> <out.txt> <first_page> <last_page> [--workers N] [--dpi D] [--psm P]

If <out.txt> already holds `=== PDF PAGE n (OCR) ===` markers, work resumes at (highest n) + 1 and APPENDS. Pages are written in
order, so a killed run leaves a contiguous file. Used for the Red Book (pages 1-404, dpi 150) and Man and His Symbols (156-319,
dpi 200, psm 1). The scratch output directory is the session scratchpad `text/` folder (see EXTRACTION_PLAN_2026-10-04.md).
"""
import argparse
import re
import subprocess
import tempfile
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path


def ocr(args):
    pdf, p, dpi, psm = args
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["pdftoppm", "-f", str(p), "-l", str(p), "-r", str(dpi), "-png", "-singlefile", pdf, f"{td}/x"], capture_output=True)
        cmd = ["tesseract", f"{td}/x.png", "-", "-l", "eng"] + (["--psm", str(psm)] if psm else [])
        t = subprocess.run(cmd, capture_output=True, text=True).stdout
    return p, t


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("out")
    ap.add_argument("first", type=int)
    ap.add_argument("last", type=int)
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--dpi", type=int, default=150)
    ap.add_argument("--psm", type=int, default=0)
    a = ap.parse_args()
    out = Path(a.out)
    start = a.first
    if out.exists():
        done = [int(m.group(1)) for m in re.finditer(r"=== PDF PAGE (\d+) \(OCR\) ===", out.read_text(encoding="utf-8", errors="ignore"))]
        if done:
            start = max(done) + 1
    if start > a.last:
        print("nothing to do: already complete through page", a.last)
        return
    print(f"OCR pages {start}-{a.last} of {a.pdf}", flush=True)
    jobs = [(a.pdf, p, a.dpi, a.psm) for p in range(start, a.last + 1)]
    with ProcessPoolExecutor(max_workers=a.workers) as ex, open(out, "a", encoding="utf-8") as f:
        for p, t in ex.map(ocr, jobs):
            f.write(f"\n=== PDF PAGE {p} (OCR) ===\n{t}")
            f.flush()
    print("done", flush=True)


if __name__ == "__main__":
    main()
