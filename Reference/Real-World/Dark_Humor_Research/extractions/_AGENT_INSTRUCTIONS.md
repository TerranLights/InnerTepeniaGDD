# Extraction agent instructions — Dark Humor Research

*Written 2026-10-05. Every extraction agent reads this in full before starting. It restates the rules of `../README.md`.*

## What the work is for

The project is gathering **real, documented patterns of military and combat gallows humor**, so that a fictional ex-military
character (the Cancer district's unnamed defector: human, roughly 10-15 years out of service, left on principle, functional but
still carrying it, chronic injury, a Boone-style companion in a sci-fi CRPG) and other soldier-type characters, factions and
cultures can be written from real patterns rather than guesswork. **Research, NOT canon. Do not write his voice, sample lines,
or dialogue for any character.** Your job is to distill what the source *establishes*, in your own words.

The lens, for every source: **how does dark humor actually work?**
- *Functions* (cohesion, boundary, coping, resistance, rank negotiation, morale, discipline, grief, identity).
- *Targets* (self, unit, brass, institution, enemy, civilians, the dead, the wounded, the weather, the mission).
- *Forms and mechanics* (deadpan, understatement, euphemism, institutional language over horror, absurdity, repartee, parody, songs, nicknames, ritual jokes, pranks, memes).
- *Rules of license* (who may joke, when, with whom, how often; the earned right; audience; benign-violation distance).
- *Limits and failure modes* (humor that stops, humor that turns to contempt or numbness, misfires, hazing, self-defeating humor, concealment, what it covers up).
- *Time course* (in combat, after service, in old age; how it changes with distance).
- *Civilian-facing register* (translation, sanitizing, the funny version vs. the sad version).
- *Defector/exile/dissent specifics* (jokes about the institution one left, humor without a unit, humor as community in exile).
- *Cross-cultural differences* (which army, which era).
- *Craft observations* (what writers and designers say works or fails when depicting it).

## Output format

Write ONE file at the path your brief names, in `../extractions/`. Structure:

1. `# <Unit title>` and a header block: sources covered (with their `source_manifest` IDs and local file paths), your name for the pass (`E##`), date 2026-10-05, and the line **"Research note, NOT canon."**
2. **Source-shape notes** (read first): for EACH source, 2-5 lines on what it is, its evidence base (sample size, period, army, method), and, importantly, **what it does NOT contain** (no joke texts, no defector content, abstract only, OCR damage, etc.). Report honestly if you could not read part of a source.
3. **Numbered findings**, in source order, labelled `**[E##-n]. Short bold title.** (source ID, page/section)`. Each finding is **own-words distillation** with every concrete specific: definitions, named constructs, numbers and sample sizes, mechanisms, documented examples *described* (what the joke does, who it is aimed at, what the reaction was), caveats the authors state. Then a line `*Candidate application:*` of 1-3 sentences (how this could shape a soldier-type character, faction, culture or the defector, flagged as candidate, not settled; **never a sample line of dialogue**). Add `*Cross-use:*` only when it clearly applies to robots, exiles, other factions, or Outer Tepenia.
4. **Quotations:** short only (a phrase to one sentence, in quotation marks, with page or section). **Exception:** sources marked `public domain` in the manifest (pre-1931 U.S. publication) may be quoted at greater length where an *example is the point* (a joke, an advertisement, a verse): quote it, with its location, and say what the mechanism is. Every quotation must be exact; if you cannot be sure of exact wording from the text file, paraphrase instead.
5. **Pattern roll-up** at the end: a short list of the documented patterns this unit establishes, organized by the lens headings above (only the headings your sources actually speak to).
6. **Gaps and cautions:** what the sources leave open, apparent errors or tensions between sources, OCR/format damage, claims that need the original read in a browser.
7. A final line: `Read: <list of source IDs>; complete: yes/no (and what was skipped).`

## Rules

- **Read every line of your assigned sources with the Read tool** (use offset/limit, about 250 lines per call; for `.txt` copies with `[p.N]` markers cite those page numbers). Do not substitute grep for reading. If a source is longer than your brief expects, say what you read and what you skipped.
- **Own words.** Do not copy sentences. No more than the quotation allowance above.
- **American English spelling everywhere**, including in titles and quotations (the project rule has no proper-noun or quotation exception; never alter a URL).
- **Honest scope.** Where a source documents a pattern only for one army, era, or occupation, say so; do not generalize it.
- **Skip bibliography/reference lists and boilerplate** (note that you skipped them), except where a reference title is the only evidence of something and you flag that.
- **No pronoun guessing:** refer to named authors and speakers by their names or "the author/speaker"; use they/them when a pronoun is needed and none is stated.
- **Size:** aim for roughly 10-18% of the source word count in findings, more for dense theory, less for repetitive material.
- If your Write tool call is refused, put the entire extraction in your final reply instead.
- Your final reply is brief: path written, number of findings, what you skipped, anything blocked. Do not paste the extraction into the reply.

## Content-filter register (added 2026-10-05, at the developer's request)

Some source passages (gore, atrocity, sexual content, slurs, graphic death) may trigger an automated output filter on the model you run on, which can cut an agent off with no output. **The developer will re-run the affected items on a different model later, so every withheld item must be recorded precisely.**
1. **Handling:** describe such passages in restrained, summarizing terms and do not reproduce graphic wording; quote only non-graphic examples. Write your output file in several smaller steps (create it, then append) so a failure part-way leaves a usable partial file.
2. **Register:** every extraction file must end, just before the final `Read:` line, with a section **`## Restrained-handling register`** listing each item you summarized, paraphrased or omitted for content reasons: the finding number, the source ID and line number (or `[p.N]`), and one line saying what kind of content it is and what was NOT reproduced. If there were none, write "None."
3. **If your run is cut off,** your last act (if you can) is the same register for what you had read so far.
