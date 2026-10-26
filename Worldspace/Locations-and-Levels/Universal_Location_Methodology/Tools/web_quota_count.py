#!/usr/bin/env python3
"""
WEB QUOTA COUNT  (2026-10-26; developer: watch the web search/fetch quota, believed to be about 1,000 per session)

  usage:  python3 web_quota_count.py [--tasks DIR]

Counts WebSearch and WebFetch tool calls made by this session's subagents, from their transcript files (counts only; prints no transcript text).
It also reports the largest single agent and any transcript line that mentions a quota or rate-limit error for web tools.
NOTE: the real limit, and what it counts (per session, per agent, or per window), is UNVERIFIED. This script only measures.
"""
import json, glob, os, sys, collections
D = "/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/3ccdb441-c6c0-49c3-a71c-ab4a4fdd3c1e/tasks"
if "--tasks" in sys.argv:
    D = sys.argv[sys.argv.index("--tasks") + 1]
tot = collections.Counter(); per = {}; errs = []
for f in sorted(glob.glob(os.path.join(D, "*.output"))):
    c = collections.Counter()
    for line in open(f, encoding="utf-8", errors="ignore"):
        try:
            d = json.loads(line)
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        m = d.get("message")
        cont = m.get("content") if isinstance(m, dict) else None
        if isinstance(cont, list):
            for b in cont:
                if isinstance(b, dict):
                    if b.get("type") == "tool_use" and b.get("name") in ("WebSearch", "WebFetch"):
                        c[b["name"]] += 1
                    if b.get("type") == "tool_result":
                        t = json.dumps(b.get("content"))[:600].lower()
                        if ("quota" in t or "rate limit" in t or "too many requests" in t) and ("web" in t or "search" in t or "fetch" in t):
                            errs.append(os.path.basename(f)[:12])
    per[f] = c
    tot.update(c)
print("agent transcripts:", len(per))
print("WebSearch:", tot["WebSearch"], "| WebFetch:", tot["WebFetch"], "| TOTAL:", tot["WebSearch"] + tot["WebFetch"])
top = sorted(per.items(), key=lambda kv: -sum(kv[1].values()))[:3]
print("largest single agents:", [sum(c.values()) for _, c in top])
print("transcripts mentioning a web quota/rate-limit error:", len(set(errs)), sorted(set(errs))[:6])
