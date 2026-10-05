#!/usr/bin/env python3
"""audit.py -- find book files that are present but contain no usable data.

Statuses:
  OK            has a text layer / text
  STUB          file is under 2 KB (placeholder / failed download)
  CORRUPT       will not open (pdfinfo fails, epub is not a zip, 0 pages)
  SCAN_OCR_OK   no text layer, but OCR of sampled pages returns real text (readable, slower)
  EMPTY         no text layer AND OCR of sampled pages returns (almost) nothing  -> shopping-list candidate
  EPUB_EMPTY    epub opens but has (almost) no text
  DJVU_NOTEXT   djvu with no text layer (OCR not tested)
  ENCRYPTED     pdf refuses text extraction
  OTHER         format not audited
"""
import csv
import os
import re
import subprocess
import sys
import tempfile
import zipfile
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

ROOT = Path("/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD")
ROOTS = [ROOT / "Reference/Materials/books", ROOT / "to-be-integrated/books"]
EXTS = {".pdf", ".epub", ".djvu", ".mobi", ".azw3", ".azw", ".zip"}


def run(cmd, timeout=90):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, errors="ignore")
    except Exception as e:  # timeout etc.
        class R:  # noqa
            stdout = ""
            stderr = str(e)
            returncode = 1
        return R()


def pdf_chars(path, page):
    r = run(["pdftotext", "-f", str(page), "-l", str(page), str(path), "-"], 60)
    return len(r.stdout.strip())


def audit(path):
    p = str(path)
    size = os.path.getsize(p)
    ext = Path(p).suffix.lower()
    if size < 2048:
        return (p, size, ext, "STUB", f"{size} bytes")
    if ext == ".pdf":
        info = run(["pdfinfo", p], 60)
        if info.returncode != 0 or "Pages:" not in info.stdout:
            err = (info.stderr or "").strip().splitlines()[:1]
            return (p, size, ext, "CORRUPT", "pdfinfo failed: " + (err[0][:80] if err else ""))
        pages = int(re.search(r"Pages:\s+(\d+)", info.stdout).group(1))
        if pages == 0:
            return (p, size, ext, "CORRUPT", "0 pages")
        fracs = [0.1, 0.25, 0.4, 0.55, 0.7, 0.85]
        pgs = sorted({max(1, min(pages, int(pages * f))) for f in fracs})
        counts = [pdf_chars(p, g) for g in pgs]
        mean = sum(counts) / len(counts)
        if mean >= 60:
            return (p, size, ext, "OK", f"{pages}pp, ~{mean:.0f} chars/page")
        # no text layer: OCR test on 3 pages
        octs = []
        for f in (0.3, 0.5, 0.7):
            g = max(1, min(pages, int(pages * f)))
            with tempfile.TemporaryDirectory() as td:
                run(["pdftoppm", "-f", str(g), "-l", str(g), "-r", "100", "-png", "-singlefile", p, f"{td}/x"], 120)
                if os.path.exists(f"{td}/x.png"):
                    t = run(["tesseract", f"{td}/x.png", "-", "-l", "eng"], 120).stdout
                    octs.append(len(t.strip()))
        om = sum(octs) / len(octs) if octs else 0
        if om >= 300:
            return (p, size, ext, "SCAN_OCR_OK", f"{pages}pp, no text layer, OCR ~{om:.0f} chars/page")
        return (p, size, ext, "EMPTY", f"{pages}pp, no text layer, OCR ~{om:.0f} chars/page ({octs})")
    if ext == ".epub":
        try:
            z = zipfile.ZipFile(p)
        except Exception as e:
            return (p, size, ext, "CORRUPT", "not a zip: " + str(e)[:60])
        tot = 0
        for n in z.namelist():
            ln = n.lower()
            if ln.endswith((".xhtml", ".html", ".htm", ".xml")) and not ln.endswith((".opf", ".ncx")) and "toc" not in ln:
                try:
                    tot += len(re.sub(r"<[^>]+>", "", z.read(n).decode("utf-8", "ignore")).strip())
                except Exception:
                    pass
        if tot < 5000:
            return (p, size, ext, "EPUB_EMPTY", f"~{tot} chars of text")
        return (p, size, ext, "OK", f"~{tot/6000:.0f}k words")
    if ext == ".djvu":
        r = run(["djvutxt", p], 120)
        n = len(r.stdout.strip())
        if r.returncode != 0:
            return (p, size, ext, "CORRUPT", "djvutxt failed")
        if n < 2000:
            return (p, size, ext, "DJVU_NOTEXT", f"{n} chars")
        return (p, size, ext, "OK", f"{n//6000}k words")
    return (p, size, ext, "OTHER", "not audited")


def main():
    out = sys.argv[1]
    files = []
    for r in ROOTS:
        for f in r.rglob("*"):
            if f.is_file() and f.suffix.lower() in EXTS:
                files.append(f)
    files.sort()
    print(f"auditing {len(files)} files", flush=True)
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["path", "size", "ext", "status", "detail"])
        with ProcessPoolExecutor(max_workers=6) as ex:
            for i, row in enumerate(ex.map(audit, files, chunksize=4), 1):
                w.writerow(row)
                if i % 100 == 0:
                    fh.flush()
                    print(f"{i}/{len(files)}", flush=True)
    print("done", flush=True)


if __name__ == "__main__":
    main()
