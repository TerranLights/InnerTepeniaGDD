#!/usr/bin/env python3
"""
MAP BOOKS TO TOPICS  —  screens the book library BY CONTENT against the per-city research topics
(November To-Do N-6, 2026-10-21).

  usage:  python3 map_books_to_topics.py --texts <dir of extracted .txt> --ids <_ids.tsv> --out <dir> [--topics FILE]

  --texts DIR   the extracted full text of each book (one .txt per book, named by the id in the ids file)
  --ids FILE    tab-separated `id<TAB>relative path of the book under Reference/Materials/books/`
  --out DIR     writes `book_topic_scores.json` and `topic_results.md` there
  --topics FILE the research-topics file (default: Reference/Real-World/City_and_District_Research_Topics.md)

HOW IT WORKS (mechanical; it never reads for meaning)
  1. Parses `Part 0` (national topics, the `N#` rows), and `Part 2` (the 35 cities + Amundsen-Scott Station): each
     city's bullets are its topics. Part 1 (the 13 Concordia districts) is not a city and is skipped.
  2. A topic whose own wording describes later-era conditions (a war, a destruction, a ruin) is NOT scored: it lies
     outside the Second Interwar default scope. It is listed as skipped, with its line.
  3. Each topic becomes a set of single words and two-word phrases. A term is weighted by how RARE it is across the
     library (inverse document frequency), so "engineering" and "history" count for almost nothing and "glaciology" or
     "metrology" count for a lot.
  4. A book's score for a topic = the sum over the topic's terms of weight x log(1 + occurrences), divided by the book's
     length in thousands of words, and it counts only if at least 3 DIFFERENT topic terms occur at least twice (or 2 of
     a 2-term topic). The evidence shown is the matched terms and their counts.
  This is a SUBJECT-LEVEL screen. It cannot say which chapters answer a city's actual Step 2 deficit (that exists only
  once the city's Step 2 has run), and it cannot judge whether a book is good: it says where the words are.
"""
import argparse
import collections
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
DEFAULT_TOPICS = os.path.join(REPO, "Reference", "Real-World", "City_and_District_Research_Topics.md")
STOP = set("""the and for with that this from into about their there which while where when what also than then them they have been being were
are was its not but can may more most such only over under between within without across among through during before after other
each both very much many some any all one two three four real world case studies study literature history sociology psychology
theory practice systems system model models direct directly existing already actually worth research researching pulling
precedent parallel examples example including include includes historical cases institutional like just often into onto per via""".split())
WAR = re.compile(r"\b(war|wartime|post-war|destroy\w*|destruction|ruin\w*|damaged|refugee\w*|casualt\w+|survived|abandon\w*|collapsed|strike|besieged)\b", re.I)


def parse_topics(path):
    ls = open(path, encoding="utf-8").read().split("\n")
    topics, skipped = [], []
    in_p2 = in_p0 = False
    city = None
    cur = None

    def flush():
        nonlocal cur
        if cur:
            (skipped if cur["war"] else topics).append(cur)
        cur = None
    for i, l in enumerate(ls, 1):
        if l.startswith("## "):
            flush()
            in_p0 = "Part 0" in l
            in_p2 = "Part 2" in l
            city = None
            continue
        if l.startswith("### ") and in_p2:
            flush()
            m = re.match(r"^### (Amundsen-Scott Station)", l)
            city = m.group(1) if m else None
            continue
        if in_p2:
            m = re.match(r"^\*\*([^*]+)\*\*(?:\s*\((.*)\))?", l)
            if m and not l.startswith("- "):
                flush()
                city = m.group(1).strip()
                continue
            if l.startswith("- ") and city:
                flush()
                cur = {"scope": city, "line": i, "text": l[2:].strip()}
                cur["war"] = bool(WAR.search(cur["text"]))
                continue
            if cur and l.startswith("  ") and l.strip():
                cur["text"] += " " + l.strip()
                cur["war"] = bool(WAR.search(cur["text"]))
                continue
            if not l.strip():
                flush()
        elif in_p0:
            m = re.match(r"^\| \*\*(N\d+)\*\* \| (.*?) \|", l)
            if m:
                flush()
                cur = {"scope": "NATIONAL " + m.group(1), "line": i, "text": re.sub(r"[*⭐]", "", m.group(2)).strip(), "war": False}
                flush()
            elif l.startswith("**Subjects worth sourcing for"):
                flush()
                cur = {"scope": "NATIONAL N1", "line": i, "text": re.sub(r"[*]", "", l) + " " + " ".join(re.sub(r"[*]", "", x).strip() for x in ls[i:i + 4]), "war": False}
                flush()
    flush()
    return topics, skipped


def terms_of(text):
    t = re.sub(r"`[^`]*`|\*\*|\*|\(.*?\)", " ", text.lower())
    words = [w for w in re.findall(r"[a-z][a-z\-]{3,}", t) if w not in STOP]
    phrases = []
    toks = [w for w in re.findall(r"[a-z][a-z\-]{2,}", t)]
    for a, b in zip(toks, toks[1:]):
        if a not in STOP and b not in STOP and len(a) > 3 and len(b) > 3:
            phrases.append(a + " " + b)
    return sorted(set(words)), sorted(set(phrases))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--texts", required=True)
    ap.add_argument("--ids", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--topics", default=DEFAULT_TOPICS)
    a = ap.parse_args()
    topics, skipped = parse_topics(a.topics)
    for t in topics:
        t["words"], t["phrases"] = terms_of(t["text"])
    vocab_w = set(w for t in topics for w in t["words"])
    vocab_p = sorted(set(p for t in topics for p in t["phrases"]))
    ids = {}
    for line in open(a.ids, encoding="utf-8"):
        if "\t" in line:
            i, p = line.rstrip("\n").split("\t", 1)
            ids[i] = p
    books = {}
    tokre = re.compile(r"[a-z][a-z\-]{3,}")
    for n, (i, p) in enumerate(sorted(ids.items()), 1):
        f = os.path.join(a.texts, i + ".txt")
        if not os.path.exists(f):
            continue
        txt = open(f, encoding="utf-8", errors="replace").read().lower()
        words = tokre.findall(txt)
        c = collections.Counter(w for w in words if w in vocab_w)
        pc = {ph: txt.count(ph) for ph in vocab_p if ph in txt}
        books[i] = {"path": p, "words": len(words), "wc": dict(c), "pc": pc}
        if n % 100 == 0:
            print("read", n, file=sys.stderr)
    N = len(books)
    df_w = collections.Counter()
    df_p = collections.Counter()
    for b in books.values():
        for w, v in b["wc"].items():
            if v >= 2:
                df_w[w] += 1
        for ph, v in b["pc"].items():
            if v >= 2:
                df_p[ph] += 1
    idf = lambda df: math.log((N + 1) / (df + 1))
    results = collections.defaultdict(list)
    for t in topics:
        key = (t["scope"], t["line"])
        for i, b in books.items():
            if b["words"] < 3000:
                continue
            score, ev, distinct = 0.0, [], 0
            for w in t["words"]:
                n = b["wc"].get(w, 0)
                if n >= 2:
                    distinct += 1
                    s = idf(df_w[w]) * math.log(1 + n)
                    score += s
                    ev.append((w, n, round(s, 2)))
            for ph in t["phrases"]:
                n = b["pc"].get(ph, 0)
                if n >= 2:
                    s = 2 * idf(df_p[ph]) * math.log(1 + n)
                    score += s
                    ev.append((ph, n, round(s, 2)))
                    distinct += 1
            need = 3 if len(t["words"]) >= 4 else 2
            if distinct >= need:
                norm = score / (b["words"] / 1000.0) ** 0.5   # damp the length effect without letting a huge book swamp the rest
                ev.sort(key=lambda x: -x[2])
                results[key].append((round(norm, 3), i, ev[:6]))
        results[key].sort(reverse=True)
    out = {"topics": topics, "skipped": skipped, "books": {i: {"path": b["path"], "words": b["words"]} for i, b in books.items()},
           "results": {"%s|%d" % k: v[:12] for k, v in results.items()}}
    os.makedirs(a.out, exist_ok=True)
    json.dump(out, open(os.path.join(a.out, "book_topic_scores.json"), "w"), ensure_ascii=False)
    print("books read: %d · topics scored: %d · topics skipped as later-era: %d · topics with no book above the bar: %d" % (
        N, len(topics), len(skipped), sum(1 for t in topics if not results.get((t["scope"], t["line"])))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
