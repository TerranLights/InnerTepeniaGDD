#!/usr/bin/env python3
"""PreToolUse guard — refuse shell commands that destroy existing work.

Reads the hook payload on stdin and emits a `deny` permission decision when the
command would remove, truncate, or overwrite something that already exists.

Design notes:
  * Removal verbs (rm, shred, git clean, ...) are denied outright, except when
    every path they touch lives under /tmp (the session scratchpad, which is
    disposable by construction).
  * `mv` and truncating `>` redirects are denied ONLY when the destination
    already exists — creating a new file is not destruction, and blocking it
    would generate enough friction that the hook gets switched off.
  * Appending (`>>`), `/dev/null`, and fd duplication (`2>&1`) are never denied.

Written 2026-09-03 after a dispatched subagent deleted a sibling reader's
completed output during a ULM cold run. See commit ddb81fd.
"""
import json
import os
import re
import shlex
import sys

SCRATCH_PREFIXES = ("/tmp/", "/var/tmp/")

REMOVAL_VERBS = [
    (r"(?:\A|[;&|(]|&&|\|\|)\s*(?:sudo\s+)?rm\b", "rm"),
    (r"(?:\A|[;&|(]|&&|\|\|)\s*(?:sudo\s+)?rmdir\b", "rmdir"),
    (r"(?:\A|[;&|(]|&&|\|\|)\s*(?:sudo\s+)?shred\b", "shred"),
    (r"(?:\A|[;&|(]|&&|\|\|)\s*(?:sudo\s+)?truncate\b", "truncate"),
    (r"(?:\A|[;&|(]|&&|\|\|)\s*(?:sudo\s+)?dd\b", "dd"),
    (r"\bgit\s+clean\b", "git clean"),
    (r"\bgit\s+reset\s+--hard\b", "git reset --hard"),
    (r"\bgit\s+checkout\s+(?:--\s|\.\s*$)", "git checkout --"),
    (r"(?<![\w-])-delete(?![\w-])", "find -delete"),
    (r"-exec\s+(?:sudo\s+)?rm\b", "find -exec rm"),
    (r"\bshutil\.rmtree\b", "shutil.rmtree"),
    (r"\bos\.remove\b", "os.remove"),
    (r"\bos\.unlink\b", "os.unlink"),
    (r"\.unlink\(\)", "Path.unlink"),
]

# The unquoted branch consumes backslash escapes so that a path containing a
# space (this repo has one: "Inner Tepenia") is captured whole rather than
# truncated at the space into a path that does not exist — which read as "new
# file, allow" and silently defeated the check.
REDIRECT = re.compile(
    r"""(?<![>&0-9])>(?!>)\s*("[^"]+"|'[^']+'|(?:[^\s;&|<>()\\]|\\.)+)"""
)


def unescape(token):
    return re.sub(r"\\(.)", r"\1", token.strip("\"'"))


HEREDOC_OPEN = re.compile(r"""<<-?\s*(['"]?)([A-Za-z_][A-Za-z0-9_]*)\1""")


def strip_heredoc_bodies(command):
    """Drop heredoc payloads before pattern-matching.

    A heredoc body is DATA being written, not commands being run — documentation
    that merely mentions `rm` or `git clean` must not trip the guard. Found the
    hard way: the first thing this hook blocked was the methodology write-up
    describing the incident it was built for.

    Caveat: `bash <<EOF` really does execute its body. That case is not covered
    here; it is rare, and the alternative is re-implementing shell parsing.
    """
    kept, delim = [], None
    for line in command.split("\n"):
        if delim is None:
            kept.append(line)
            match = HEREDOC_OPEN.search(line)
            if match:
                delim = match.group(2)
        elif line.strip() == delim:
            delim = None
    return "\n".join(kept)


def deny(reason):
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason,
            }
        },
        sys.stdout,
    )
    sys.exit(0)


def is_scratch(path):
    return os.path.abspath(path).startswith(SCRATCH_PREFIXES)


def path_tokens(command):
    try:
        tokens = shlex.split(command)
    except ValueError:
        return None
    return [t for t in tokens if not t.startswith("-")]


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return
    raw = ((payload.get("tool_input") or {}).get("command") or "").strip()
    if not raw:
        return
    command = strip_heredoc_bodies(raw)

    # 1. Removal verbs — denied unless confined to scratch space.
    for pattern, label in REMOVAL_VERBS:
        if re.search(pattern, command):
            tokens = path_tokens(command)
            candidates = [t for t in (tokens or []) if "/" in t or os.path.exists(t)]
            if candidates and all(is_scratch(t) for t in candidates):
                break
            deny(
                f"Blocked: `{label}` destroys existing work. This project lost a "
                "completed reader's output to exactly this (commit ddb81fd). If the "
                "deletion is genuinely intended, ask the user to run it themselves "
                "with the `!` prefix, or to relax this hook via /hooks."
            )

    # 2. `mv` onto a path that already exists.
    if re.search(r"(?:\A|[;&|(]|&&|\|\|)\s*(?:sudo\s+)?mv\b", command):
        args = path_tokens(command)
        if args and len(args) >= 3:  # ["mv", src..., dest]
            operands, dest = args[1:-1], args[-1]
            clobbered = []
            if os.path.isdir(dest):
                clobbered = [
                    os.path.join(dest, os.path.basename(s))
                    for s in operands
                    if os.path.exists(os.path.join(dest, os.path.basename(s)))
                ]
            elif os.path.exists(dest):
                clobbered = [dest]
            clobbered = [c for c in clobbered if not is_scratch(c)]
            if clobbered:
                deny(
                    f"Blocked: `mv` would overwrite {clobbered[0]}, which already "
                    "exists. Move to a new path, or ask the user to run it with `!`."
                )

    # 3. Truncating `>` redirect onto a file that already exists.
    for match in REDIRECT.finditer(command):
        target = unescape(match.group(1))
        if target.startswith("/dev/") or target.startswith("&"):
            continue
        if os.path.isfile(target) and not is_scratch(target):
            deny(
                f"Blocked: `> {target}` truncates a file that already exists. Use "
                "`>>` to append, write to a new path, or use the Edit tool."
            )


if __name__ == "__main__":
    main()
