#!/usr/bin/env python3
"""_prep_text.py -- build page-marked plain-text copies of the Jung and Enneagram source books.

Why: extraction agents read these text files in segments instead of each one re-running pdftotext, and every page
carries a marker so extractions can cite pages. Output goes to a scratch directory (NOT the repo); this script is the
reproducible recipe. Re-run it if the scratch directory is gone.

Usage:  python3 _prep_text.py <out_dir> [key ...]
Keys:   see SOURCES. With no keys, builds all except the Red Book (OCR: use `redbook` explicitly; it takes ~30+ min).
"""
import os
import re
import subprocess
import sys
import zipfile
from pathlib import Path
from posixpath import dirname, join, normpath
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[3]
J = ROOT / "Reference/Materials/books/philosophy/Carl Gustav Jung"
E = ROOT / "to-be-integrated/books/Enneagram materials"

SOURCES = {
    # Jung
    "aion_cw9ii": J / "Aion-- researches into the phenomenology of the self/The Collected Works of C. G. Jung-- Aion - C.G. Jung.pdf",
    "aion_epub": J / "Aion-- researches into the phenomenology of the self/Aion-- researches into the phenomenology of the self - Carl Gustav Jung.epub",
    "modern_man": J / "Modern Man in Search of a Soul - Carl Gustav Jung [1933].epub",
    "symbols_of_transformation": J / "Symbols of Transformation - Jung, Carl Gustav [1952].pdf",
    "synchronicity": J / "Synchronicity-- nature and psyche in an interconnected universe - Carl Gustav Jung.pdf",
    "undiscovered_self": J / "The Undiscovered SelfSymbols and the Interpretation of Dreams - Carl Jung.epub",
    "man_and_his_symbols": J / "Man and His Symbols - Carl Gustav Jung.pdf",
    "redbook": J / "The Red Book-- Liber Novus - Carl Gustav Jung.pdf",
    # Enneagram
    "rohr_ebert": next(E.glob("The Enneagram - A Christian Perspective*.pdf")),
    "stabile": next(E.glob("The Path Between Us*.pdf")),
    "palmer": next(E.glob("love and relationships/The Enneagram in Love and Work*.pdf")),
    "blair": next(E.glob("love and relationships/The Enneagram For Relationships A Guide*Damian Blair*.epub")),
    "whitmoyer_ober": next(E.glob("love and relationships/The Enneagram for Relationships Transform*.epub")),
    "hall": next(E.glob("love and relationships/The Enneagram in Love A Roadmap*.epub")),
    "gomez": next(E.glob("love and relationships/The Enneagram You Understand*.epub")),
    "personality_types": next(E.glob("Personality Types Using the Enneagram*.epub")),
    "wisdom": next(E.glob("The Wisdom of the Enneagram*.pdf")),
    "chestnut": next(E.glob("The Complete Enneagram*.pdf")),
}


def pdf_to_text(src, out, ocr=False):
    if not ocr:
        txt = subprocess.run(["pdftotext", "-layout", str(src), "-"], capture_output=True, text=True).stdout
        pages = txt.split("\f")
        with open(out, "w", encoding="utf-8") as f:
            for i, p in enumerate(pages, 1):
                if i == len(pages) and not p.strip():
                    break
                f.write(f"\n=== PDF PAGE {i} ===\n{p}")
        return
    # OCR route (image-only scans such as the Red Book)
    info = subprocess.run(["pdfinfo", str(src)], capture_output=True, text=True).stdout
    n = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    tmp = Path(out).parent / "_ocr_tmp"
    tmp.mkdir(exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        for i in range(1, n + 1):
            png = tmp / f"p{i}"
            subprocess.run(["pdftoppm", "-f", str(i), "-l", str(i), "-r", "150", "-png", "-singlefile", str(src), str(png)],
                           capture_output=True)
            t = subprocess.run(["tesseract", f"{png}.png", "-", "-l", "eng"], capture_output=True, text=True).stdout
            f.write(f"\n=== PDF PAGE {i} (OCR) ===\n{t}")
            f.flush()
            try:
                os.remove(f"{png}.png")
            except OSError:
                pass


def epub_to_text(src, out):
    z = zipfile.ZipFile(src)
    opf = next(n for n in z.namelist() if n.lower().endswith(".opf"))
    root = ET.fromstring(z.read(opf))
    ns = {"o": "http://www.idpf.org/2007/opf"}
    manifest = {i.get("id"): i.get("href") for i in root.findall(".//o:manifest/o:item", ns)}
    spine = [manifest[r.get("idref")] for r in root.findall(".//o:spine/o:itemref", ns) if r.get("idref") in manifest]
    base = dirname(opf)
    with open(out, "w", encoding="utf-8") as f:
        for k, href in enumerate(spine, 1):
            name = normpath(join(base, href))
            if name not in z.namelist():
                continue
            raw = z.read(name).decode("utf-8", "ignore")
            raw = re.sub(r"(?is)<(script|style).*?</\1>", "", raw)
            raw = re.sub(r"(?i)</(p|div|h[1-6]|li|tr|blockquote|section)>|<br\s*/?>", "\n", raw)
            txt = re.sub(r"<[^>]+>", "", raw)
            txt = re.sub(r"&nbsp;", " ", txt)
            txt = re.sub(r"&amp;", "&", txt)
            txt = re.sub(r"&lt;", "<", txt)
            txt = re.sub(r"&gt;", ">", txt)
            txt = re.sub(r"&#?\w+;", "", txt)
            txt = re.sub(r"\n\s*\n\s*\n+", "\n\n", txt).strip()
            if txt:
                f.write(f"\n=== EPUB SECTION {k}: {href} ===\n{txt}\n")


def main():
    out_dir = Path(sys.argv[1])
    out_dir.mkdir(parents=True, exist_ok=True)
    keys = sys.argv[2:] or [k for k in SOURCES if k != "redbook"]
    for k in keys:
        src = SOURCES[k]
        out = out_dir / f"{k}.txt"
        if str(src).lower().endswith(".pdf"):
            pdf_to_text(src, out, ocr=(k == "redbook"))
        else:
            epub_to_text(src, out)
        words = len(out.read_text(encoding="utf-8").split())
        print(f"{k:28s} {words:9d} words  -> {out}")


if __name__ == "__main__":
    main()
