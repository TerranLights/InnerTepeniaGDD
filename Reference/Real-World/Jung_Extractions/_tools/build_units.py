#!/usr/bin/env python3
"""Build the extraction unit list (agent-sized pieces) for the Jung + Enneagram sources."""
import json
import re
from pathlib import Path

S = Path("/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/462f6b67-5cf4-4e6a-9bd4-27aaf5e5b77e/scratchpad")
TEXT = S / "text"
MARK = re.compile(r"^=== (PDF PAGE|EPUB SECTION) (\d+)")
HEAD = re.compile(r"(chapter|part\s+[ivx0-9]+|introduction|foreword|preface|conclusion|epilogue|appendix|contents)", re.I)

JUNG_OUT = "Reference/Real-World/Jung_Extractions"
ENN_OUT = "Worldspace/Enneagram/Source_Book_Extractions"


def markers(fn):
    """list of (line_index_0based, marker_number, words_in_segment, head_flag)"""
    lines = (TEXT / fn).read_text(encoding="utf-8").split("\n")
    idx = [i for i, l in enumerate(lines) if MARK.match(l)]
    segs = []
    for k, i in enumerate(idx):
        j = idx[k + 1] if k + 1 < len(idx) else len(lines)
        body = "\n".join(lines[i + 1:j])
        n = int(MARK.match(lines[i]).group(2))
        segs.append((i, n, len(body.split()), bool(HEAD.search(body[:500]))))
    return lines, segs


def split(fn, parts, lo=None, hi=None):
    """split markers [lo..hi] (marker numbers, inclusive) into `parts` word-balanced pieces"""
    lines, segs = markers(fn)
    segs = [s for s in segs if (lo is None or s[1] >= lo) and (hi is None or s[1] <= hi)]
    total = sum(s[2] for s in segs)
    cuts = [0]
    acc = 0
    cum = []
    for s in segs:
        acc += s[2]
        cum.append(acc)
    for p in range(1, parts):
        target = total * p / parts
        win = total / parts * 0.18
        cands = [k for k, c in enumerate(cum) if abs(c - target) <= win and k + 1 < len(segs) and segs[k + 1][3]]
        if not cands:
            cands = [min(range(len(cum)), key=lambda k: abs(cum[k] - target))]
        k = min(cands, key=lambda k: abs(cum[k] - target))
        cuts.append(k + 1)
    cuts.append(len(segs))
    out = []
    for a, b in zip(cuts, cuts[1:]):
        sl = segs[a:b]
        if not sl:
            continue
        start_line = sl[0][0] + 1
        end_line = (segs[b][0] if b < len(segs) else len(lines))
        out.append({"first": sl[0][1], "last": sl[-1][1], "words": sum(s[2] for s in sl),
                    "line_start": start_line, "line_end": end_line})
    return out


units = []


def add(book_key, title, author, edition, out_dir, parts, text_file, source_rel, lo=None, hi=None, note="", label="p"):
    ranges = split(text_file, parts, lo, hi) if parts else []
    for i, r in enumerate(ranges, 1):
        units.append({"book": book_key, "title": title, "author": author, "edition": edition,
                      "part": i, "of": len(ranges), "text_file": text_file, "source": source_rel,
                      "out_dir": out_dir, "note": note, "label": label, **r})


# ---------------- Jung ----------------
J = "Reference/Materials/books/philosophy/Carl Gustav Jung/"
add("aion", "Aion: Researches into the Phenomenology of the Self (Collected Works vol. 9 part ii)", "C. G. Jung",
    "Bollingen / Princeton, CW 9ii", JUNG_OUT, 3, "aion_cw9ii.txt",
    J + "Aion-- researches into the phenomenology of the self/The Collected Works of C. G. Jung-- Aion - C.G. Jung.pdf",
    note="Cite by CW paragraph number (the section numbers) where visible, with PDF page. A cleaner EPUB copy exists at "
         "/tmp/.../text/aion_epub.txt (same book, no page numbers) for cross-checking garbled passages.")
add("modern_man", "Modern Man in Search of a Soul", "C. G. Jung", "1933 (EPUB)", JUNG_OUT, 2, "modern_man.txt",
    J + "Modern Man in Search of a Soul - Carl Gustav Jung [1933].epub", label="s")
add("symbols_of_transformation", "Symbols of Transformation (Collected Works vol. 5)", "C. G. Jung",
    "Bollingen / Princeton, 1952 revised", JUNG_OUT, 5, "symbols_of_transformation.txt",
    J + "Symbols of Transformation - Jung, Carl Gustav [1952].pdf",
    note="Includes extensive footnotes and the Miller fantasies; extract the argument, the amplification method, "
         "and the key concepts (libido, hero, mother, night sea journey, sacrifice, etc.); footnote apparatus is secondary.")
add("synchronicity", "Synchronicity: Nature and Psyche in an Interconnected Universe", "C. G. Jung (with commentary)",
    "Texas A&M / Princeton edition", JUNG_OUT, 1, "synchronicity.txt",
    J + "Synchronicity-- nature and psyche in an interconnected universe - Carl Gustav Jung.pdf",
    note="Includes any editor/commentary essays: extract Jung's own text and label commentary separately.")
add("undiscovered_self", "The Undiscovered Self (with Symbols and the Interpretation of Dreams)", "C. G. Jung",
    "EPUB", JUNG_OUT, 1, "undiscovered_self.txt", J + "The Undiscovered SelfSymbols and the Interpretation of Dreams - Carl Jung.epub",
    label="s")

# Man and His Symbols: remaining sections, PDF pages (letter-spaced text layer; verify visually if needed)
for i, (a, b, what) in enumerate([(156, 232, "M.-L. von Franz, 'The Process of Individuation' (resume; the book's p.158 is about PDF p.158-160)"),
                                  (228, 319, "Aniela Jaffe, 'Symbolism in the Visual Arts' and Jolande Jacobi, 'A Case of Individuation' (Jacobi starts about PDF p.269), to the end of the book")], 1):
    lines, segs = markers("man_and_his_symbols.txt")
    sl = [s for s in segs if a <= s[1] <= b]
    nxt = [s for s in segs if s[1] == b + 1]
    units.append({"book": "man_and_his_symbols", "title": "Man and His Symbols (REMAINING sections)", "author": "C. G. Jung et al.",
                  "edition": "1964", "part": i, "of": 2, "text_file": "man_and_his_symbols.txt",
                  "source": J + "Man and His Symbols - Carl Gustav Jung.pdf", "out_dir": JUNG_OUT,
                  "note": what + ". TEXT LAYER IS LETTER-SPACED ('T h e  e g o'): de-space it (collapse single letters) or read the "
                          "PDF pages visually with the Read tool's `pages` parameter. Parts 1-158 are already extracted in "
                          "Reference/Real-World/Man_and_His_Symbols_Extraction.md: read its header first and do NOT redo them.",
                  "label": "p", "first": a, "last": b, "words": sum(s[2] for s in sl),
                  "line_start": sl[0][0] + 1, "line_end": (nxt[0][0] if nxt else len(lines))})

# ---------------- Enneagram ----------------
E = "to-be-integrated/books/Enneagram materials/"
add("rohr_ebert", "The Enneagram: A Christian Perspective", "Richard Rohr and Andreas Ebert", "2016 PDF", ENN_OUT, 3,
    "rohr_ebert.txt", E + "The Enneagram - A Christian Perspective -- Richard Rohr and Andreas Ebert [2016].pdf")
add("stabile", "The Path Between Us: An Enneagram Journey to Healthy Relationships", "Suzanne Stabile", "PDF", ENN_OUT, 1,
    "stabile.txt", E + "The Path Between Us (Suzanne Stabile) (z-library.sk, 1lib.sk, z-lib.sk).pdf")
add("palmer", "The Enneagram in Love and Work: Understanding Your Intimate and Business Relationships", "Helen Palmer", "PDF", ENN_OUT, 3,
    "palmer.txt", E + "love and relationships/The Enneagram in Love and Work Understanding Your Intimate Business Relationships (Helen Palmer) (Z-Library).pdf")
add("blair", "The Enneagram for Relationships: A Guide to Personality Types for Greater Self Discovery and Romance", "Damian Blair", "EPUB", ENN_OUT, 1,
    "blair.txt", E + "love and relationships/The Enneagram For Relationships A Guide to Personality Types for Greater Self Discovery and Romance (Understanding The... (Damian Blair) (Z-Library).epub", label="s")
add("whitmoyer_ober", "The Enneagram for Relationships: Transform Your Connections with Friends, Family, Colleagues, and in Love", "Ashton Whitmoyer-Ober", "EPUB", ENN_OUT, 1,
    "whitmoyer_ober.txt", E + "love and relationships/The Enneagram for Relationships Transform Your Connections with Friends, Family, Colleagues, and in Love (Ashton Whitmoyer-Ober MA) (Z-Library).epub", label="s")
add("hall", "The Enneagram in Love: A Roadmap for Building and Strengthening Romantic Relationships", "Stephanie Barron Hall", "EPUB", ENN_OUT, 1,
    "hall.txt", E + "love and relationships/The Enneagram in Love A Roadmap for Building and Strengthening Romantic Relationships (Stephanie Barron Hall) (Z-Library).epub", label="s")
add("gomez", "The Enneagram: Understand Your Personality Type and How It Can Transform Your Relationships", "Gina Gomez", "EPUB", ENN_OUT, 1,
    "gomez.txt", E + "love and relationships/The Enneagram You Understand Your Personality Type and How It Can Transform Your Relationships (Gina Gomez) (Z-Library).epub", label="s")
add("personality_types", "Personality Types: Using the Enneagram for Self-Discovery", "Don Richard Riso and Russ Hudson", "EPUB", ENN_OUT, 4,
    "personality_types.txt", E + "Personality Types Using the Enneagram for Self-discovery (Don Richard Riso, Russ Hudson) (z-library.sk, 1lib.sk, z-lib.sk).epub", label="s",
    note="Only part of this book is mined (what is in Worldspace/Enneagram/Enneagram_Dynamics.md). Extract the WHOLE book for its own "
         "wording (esp. the Levels of Development, type descriptions, and any material not already in Worldspace/Enneagram/); "
         "check that folder's README first and cross-reference rather than silently duplicating.")

# Wisdom Part III: from the PDF page containing line 17432 of wisdom.txt to the end
lines, segs = markers("wisdom.txt")
p3 = [s for s in segs if s[0] <= 17432][-1]
rest = [s for s in segs if s[1] >= p3[1]]
units.append({"book": "wisdom_part3", "title": "The Wisdom of the Enneagram, PART III (Chapters 16-17, the spiritual-practice tools) and back matter",
              "author": "Don Richard Riso and Russ Hudson", "edition": "PDF", "part": 1, "of": 1, "text_file": "wisdom.txt",
              "source": E + "The Wisdom of the Enneagram The Complete Guide to Psychological and Spiritual Growth for the Nine Personality Types (Don Richard Riso, Russ Hudson).pdf",
              "out_dir": ENN_OUT, "label": "p", "first": p3[1], "last": rest[-1][1], "words": sum(s[2] for s in rest),
              "line_start": p3[0] + 1, "line_end": len(lines),
              "note": "Parts I and II of this book are ALREADY mined (Worldspace/Enneagram/); do not redo them. Part III opens at PDF page %d." % p3[1]})

# Chestnut: front matter + Ch.1-2 (lines 1-1844), and the back matter after Chapter 11
lines, segs = markers("chestnut.txt")
def seg_for_line(L):
    return [s for s in segs if s[0] <= L][-1]
a_end = seg_for_line(1844)
units.append({"book": "chestnut_front", "title": "The Complete Enneagram: 27 Paths to Greater Self-Knowledge, FRONT MATTER and CHAPTERS 1-2",
              "author": "Beatrice Chestnut", "edition": "PDF", "part": 1, "of": 2, "text_file": "chestnut.txt",
              "source": E + "The Complete Enneagram 27 Paths to Greater Self-Knowledge (Beatrice Chestnut) (z-library.sk, 1lib.sk, z-lib.sk).pdf",
              "out_dir": ENN_OUT, "label": "p", "first": segs[0][1], "last": a_end[1], "words": sum(s[2] for s in segs if s[1] <= a_end[1]),
              "line_start": 1, "line_end": 1844 + 1,
              "note": "Chapters 3-11 (the nine type chapters) are ALREADY mined into Worldspace/Enneagram/Type_*; skip them. Chapter 1 'The Enneagram as a Framework' and Chapter 2 'The Enneagram as a Universal Symbol' are NOT."})
c11 = seg_for_line(13373)
tail = [s for s in segs if s[1] >= c11[1]]
units.append({"book": "chestnut_back", "title": "The Complete Enneagram, BACK MATTER after Chapter 11 (conclusion, appendices, notes), plus Chapter 11's closing pages",
              "author": "Beatrice Chestnut", "edition": "PDF", "part": 2, "of": 2, "text_file": "chestnut.txt",
              "source": E + "The Complete Enneagram 27 Paths to Greater Self-Knowledge (Beatrice Chestnut) (z-library.sk, 1lib.sk, z-lib.sk).pdf",
              "out_dir": ENN_OUT, "label": "p", "first": c11[1], "last": tail[-1][1], "words": sum(s[2] for s in tail),
              "line_start": 13373, "line_end": len(lines),
              "note": "Chapter 11 (Point One) body is already mined: skip it, find where it ends, and extract everything AFTER it "
                      "(any conclusion, glossary, resources, notes). If there is nothing substantive after Chapter 11 say so in one line."})

# assign ids
for n, u in enumerate(units, 1):
    u["id"] = ("J" if u["out_dir"] == JUNG_OUT else "E") + "%02d" % sum(1 for x in units[:n] if x["out_dir"] == u["out_dir"])
    stem = re.sub(r"[^A-Za-z0-9]+", "_", u["book"]).strip("_")
    u["out_file"] = f'{u["out_dir"]}/{stem}_Extraction_Part{u["part"]:02d}_of_{u["of"]:02d}.md'
(S / "units.json").write_text(json.dumps(units, indent=1), encoding="utf-8")
for u in units:
    print(f'{u["id"]}  {u["book"]:26s} part {u["part"]}/{u["of"]}  {u["label"]}{u["first"]}-{u["last"]}  {u["words"]:7d} words  lines {u["line_start"]}-{u["line_end"]}')
print(len(units), "units;", sum(1 for u in units if u["id"][0] == "J"), "Jung,", sum(1 for u in units if u["id"][0] == "E"), "Enneagram")
