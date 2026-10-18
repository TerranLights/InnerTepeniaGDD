# Synthesis brief — Dark Humor Research (shared by all five lens agents)

*Written 2026-10-06. Read this in full before starting. Folder rules: `../../README.md`; extraction rules: `../_AGENT_INSTRUCTIONS.md`.*

## What this is

Thirty-eight extraction files in `../` (`E01…E25e`; about 2,260 numbered findings, about 741,000 words) record what real military and veteran humor sources establish. **Your job is one cross-source synthesis along one lens.** The product is a document that tells the developer, for each pattern: *what is documented, how strongly, by which kinds of source, where sources disagree, what is missing.* It also lists **design-relevant candidates** (constraints a writer could treat as real-world facts about this kind of humor), clearly marked as candidates.

**Hard limits:** (1) **Do not write dialogue, sample jokes, or a voice for any character**, including the Cancer district's unnamed ex-military defector (human, roughly 10-15 years out of service, left on principle, functional but carrying it, chronic injury, a Boone-style companion in a sci-fi CRPG). (2) **Claim only what the extraction files support;** write "not documented in the corpus" where nothing is. (3) Real-world material is **mechanism, not specification**; the character's origin military is undecided. (4) American English spelling. (5) Describe sensitive content in restrained terms (the files already do; do not re-expand anything they withheld). (6) Pronouns: use names, "the author," or they.

## The corpus: what each file group is (and is not)

| Files | Kind of evidence | Main limits |
|---|---|---|
| E01-E05, E07 | scholarship: ethnographies, interview studies, surveys, reviews, theory (E05 mostly not military; E03 not soldiers) | mostly Western armies; small samples; E07 about cartoons and the home front |
| E06 | two theses: Pinkston (memoir-based reading of Iraq/Afghanistan accounts), Jensen (a game) | secondary; Jensen is about a game |
| E08-E10b | The Wipers Times: a WWI British trench newspaper, soldier-made, 1916-18, full run | one unit's paper, edited by two officers; public domain; period caricature |
| E11a-b | The Anzac Book (Gallipoli 1915 anthology) + Bairnsfather cartoons + Sassoon verse | edited anthology; Bairnsfather's drawings absent; Sassoon is an officer-poet |
| E12a-b | *Songs and Slang of the British Soldier* (songs and glossary, 1930) | editors' selection and cleaning |
| E13a-b | Richards, *Old Soldiers Never Die*: an other-ranks regular's memoir (WWI) | retrospective memoir (1933) |
| E15a-c | Graves, *Good-bye to All That*: officer memoir (WWI and after; E15c holds the best post-war evidence) | retrospective, literary, partly comic by design |
| E18 | Buzzell's blog (mostly pasted press, not his prose) | thin primary text |
| E19 | Terminal Lance (webcomic): 60-strip sample + 1,000-title list | sample biased to serious topics; image-only |
| E21 | veteran comedy and satire web sources | mostly journalism and promotion, one organization's programs repeat |
| E22a | authors' interviews (Klay, Abrams, Heller, Vonnegut, Gallagher...) | craft statements by novelists, not field evidence |
| E22b | screen, games and consulting web sources (incl. fan analysis of Fallout: New Vegas' Boone) | none discusses Boone's humor |
| E23 | defector, deserter, exile, cross-cultural and slang web pages | the only defector material; thin |
| E24a-d | oral-history passages (Rutgers; AWM + Witness to War; six other archives; UNSW Australians at War) | **keyword-selected harvests** (biased toward people who say 'humor'); counts are passages, not rates; excreta material excluded; Wisconsin held out |
| E25a-e | modern veteran writing (journals; Sandbox/milblogs; essays; transcripts/NPR; a thesis memoir) | genre mixed (fiction vs. nonfiction is labeled in the files); selection bias |

## Procedure

1. **Read the 'Pattern roll-up' and 'Gaps and cautions' sections of EVERY one of the 38 files** (`grep -n '^## ' <file>` finds them; read with the Read tool). Also read each file's 'Source-shape notes' head (first ~60 lines) for what it does and does not contain. About 75,000 words in all.
2. For your lens, **go back to the findings themselves** (grep your lens's keywords; read the relevant findings) to confirm, quote briefly (a phrase), and **cite by finding ID, e.g. [E08-12]**. Every claim in your document must carry at least one finding ID.
3. **Tag evidence strength** for each pattern: **A** = documented in at least three different kinds of source (e.g., scholarship + primary text + oral history or modern voices); **B** = several independent items within one kind of source, or two kinds; **C** = single source or anecdote; **D** = contested (sources disagree: say how). Say how many independent items support it, and flag **non-independent** support (the same event reported twice; one organization's pages; the same author in several outlets; sources that cite each other).
4. Record **scope**: which army, era, rank, occupation or genre the support comes from, and whether it is likely to travel.
5. **Contradictions and tensions** between sources are valuable: list them with IDs on both sides.
6. **Absences are findings:** where a topic that should appear does not (e.g., no first-hand defector jokes), say so and say which corpus part was searched.

## Output

Write one file at the path in your brief, in this structure:
1. `# <Lens title>` + header (lens, date 2026-10-06, files read: all 38, "Research synthesis, NOT canon; no voice or dialogue").
2. **Executive summary** (at most 350 words).
3. **Pattern table:** `ID | pattern (one sentence) | strength A-D | supporting findings | counter-evidence | scope`. Aim for 25-45 rows. Number patterns `<lens>-P1…` (e.g., `S1-P7`).
4. **Detailed sections** by theme: for each pattern group, 100-250 words of synthesis with finding-ID citations, short quotations only (a phrase), and the independence caveats.
5. **Contradictions and open questions.**
6. **What would resolve the gaps** (named source types; tie to the Tier C list where relevant: `../../Tier_C_Shopping_List.md`).
7. **Design-relevant candidates** (10-25 bullets): each is a constraint or fact a writer could use, stated as a candidate with its strength tag, with no dialogue.
8. A final line: `Read: all 38 roll-ups; findings consulted: <count>; complete: yes/no`.

**Size:** 6,000-10,000 words. Save as you go (create the file with the header and first sections, append as you finish each section).
