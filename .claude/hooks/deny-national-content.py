#!/usr/bin/env python3
"""PreToolUse guard — refuse WebSearch/WebFetch calls that name a real-world
nation, nationality, or demonym.

This project's binding law (Worldspace/.../Reference/No_National_Stereotypes.md,
memory: feedback_no_national_stereotypes.md) holds that a Tepenian location's
real-world founding nation is a GPS coordinate only, never a cause of anything
in the fiction - and that even a neutral, structural-sounding reference to a
real nation (infrastructure, logistics, "who built/operates this") is exactly
as much a violation as an explicit character stereotype, because both make the
real nation's identity load-bearing.

A memory entry documenting this already existed, in detail, before this hook
was written - and was not enough on its own, because memory recall is
relevance-triggered and did not fire during two consecutive live violations in
one session (2026-09-03, Run 15, Shirayuki). This hook is the mechanical
backstop: it does not depend on recall timing.

Written to be a genuine trip-wire, not a precise parser: it flags on country
names and common demonyms appearing anywhere in a WebSearch query or a
WebFetch prompt/URL. False positives (an unrelated project needing to mention
a country) are possible and are the acceptable cost - see the escape hatch.
"""
import json
import re
import sys

# Country names and common demonyms/adjectival forms. Not exhaustive by design
# (a perfect list is not the point - this is a trip-wire) but broad enough to
# catch the cases that have actually recurred in this project's own history:
# India/Indian, China/Chinese/Sinian, Russia/Russian, Japan/Japanese,
# Korea/Korean, Germany/German, plus the wider set this project's own
# composition tables draw on.
COUNTRIES = [
    "Afghanistan", "Albania", "Algeria", "Argentina", "Argentine", "Armenia",
    "Australia", "Australian", "Austria", "Austrian", "Azerbaijan",
    "Bangladesh", "Belarus", "Belgium", "Belgian", "Bolivia", "Bosnia",
    "Brazil", "Brazilian", "Bulgaria", "Cambodia", "Cameroon", "Canada",
    "Canadian", "Chile", "Chilean", "China", "Chinese", "Sinian", "Colombia",
    "Croatia", "Cuba", "Cuban", "Czech", "Denmark", "Danish", "Ecuador",
    "Egypt", "Egyptian", "Estonia", "Estonian", "Ethiopia", "Finland",
    "Finnish", "France", "French", "Georgia", "Georgian", "Germany",
    "German", "Ghana", "Greece", "Greek", "Hungary", "Hungarian", "Iceland",
    "Icelandic", "India", "Indian", "Indonesia", "Indonesian", "Iran",
    "Iranian", "Iraq", "Iraqi", "Ireland", "Irish", "Israel", "Israeli",
    "Italy", "Italian", "Japan", "Japanese", "Jordan", "Kazakhstan",
    "Kenya", "Korea", "Korean", "Kuwait", "Laos", "Latvia", "Latvian",
    "Lebanon", "Lithuania", "Lithuanian", "Malaysia", "Malaysian", "Mexico",
    "Mexican", "Mongolia", "Morocco", "Nepal", "Netherlands", "Dutch",
    "New Zealand", "Nigeria", "Norway", "Norwegian", "Pakistan",
    "Pakistani", "Peru", "Peruvian", "Philippines", "Filipino", "Poland",
    "Polish", "Portugal", "Portuguese", "Romania", "Romanian", "Russia",
    "Russian", "Saudi Arabia", "Serbia", "Singapore", "Slovakia",
    "Slovenia", "South Africa", "African", "Spain", "Spanish", "Sri Lanka",
    "Sweden", "Swedish", "Switzerland", "Swiss", "Syria", "Taiwan",
    "Taiwanese", "Thailand", "Thai", "Turkey", "Turkish", "Ukraine",
    "Ukrainian", "United Kingdom", "British", "United States", "American",
    "Uruguay", "Venezuela", "Vietnam", "Vietnamese",
]
PATTERN = re.compile(r"\b(" + "|".join(re.escape(c) for c in COUNTRIES) + r")\b",
                      re.IGNORECASE)


def deny(matched, field):
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": (
                    f"Blocked: {field} names a real-world nation/demonym "
                    f'("{matched}"). This project\'s binding law is that a '
                    "location's real-world basis is a GPS coordinate only, "
                    "never a cause - and this holds even for neutral, "
                    "structural-sounding research (infrastructure, logistics, "
                    "who operates what). Rephrase toward pure place-name and "
                    "physical-property terms (terrain, climate, coordinates, "
                    "materials), with no national/political term in the query "
                    "at all. If a genuine exception applies, ask the user to "
                    "run this search themselves with the `!` prefix."
                ),
            }
        },
        sys.stdout,
    )
    sys.exit(0)


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return
    tool_input = payload.get("tool_input") or {}
    for field in ("query", "prompt", "url"):
        value = tool_input.get(field)
        if not value:
            continue
        m = PATTERN.search(value)
        if m:
            deny(m.group(0), field)


if __name__ == "__main__":
    main()
