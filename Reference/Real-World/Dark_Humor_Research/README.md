# Dark Humor Research — Real Basis-of-Reference Material on Military / Combat Gallows Humor

**Opened 2026-10-05** at the developer's direction, after the lead-finding pass (`PTSD_Military_Trauma_Research/11_Dark_Humor_Source_Leads.md`
and its detail files `11a`–`11d`) showed that real, documented military humor material exists, much of it free, and that a
character-voice for the Cancer district's unnamed ex-military defector must not be synthesized from guesswork.

**Status of everything in this folder: research, NOT canon.** It becomes design input only by explicit decision.
**No voice for the defector is written here.** The checklist's standing rule applies: *do not synthesize his voice or dialogue
until real source material (or direct input) is in hand, and then only as candidates.* This folder is where that source
material accumulates.

## Folder map

| Path | What it holds | In git? |
|---|---|---|
| `README.md` *(this file)* | purpose, rules, map, status | yes |
| `00_Extraction_Checklist.md` | **source of truth** for what is collected, extracted, blocked or open | yes |
| `Tier_C_Shopping_List.md` | what the developer is fetching by hand (sources the tools cannot reach), with exact search strings and save instructions | yes |
| `source_manifest.json` (a CSV copy is written at the end) | one row per collected source: id, tier, citation, URL, license class, local path, words, status, extraction file | yes |
| `Content_Filter_Denials_Log.md` | **everything the model's content filter denied, plus every passage summarized or omitted to avoid it**, so those specific items can be re-run later on another model | yes |
| `extractions/` | **own-words extractions** (38+ files, about 2,260 numbered findings), short quotations only, page citations | yes |
| `extractions/synthesis/` | **`00_PATTERN_SYNTHESIS.md`** (start here) plus five lens syntheses `S1`-`S5`: patterns with evidence-strength tags, contradictions, what the corpus cannot tell us, design-relevant candidates (no voice, no dialogue) | yes |
| `source_texts/` | raw text copies of what was collected (`academic/`, `primary_wwi/`, `primary_other/`, `modern_voices/`, `oral_history/`, `web_articles/`) | **no** (local only) |
| `Tier_C_Dropbox/` | **where fetched Tier C files go** (PDF, TXT, HTML, EPUB; any name, but see its README) | **no** (local only) |

`source_texts/` and `Tier_C_Dropbox/` are excluded by this folder's own `.gitignore`, the same convention as `Reference/Materials/books/`:
third-party text is retained locally for reference and is not redistributed. Public-domain and open-licensed items are still kept out of git
so one rule covers everything; their license class is recorded in `source_manifest.csv`.

## The tiers (as defined 2026-10-05)

| Tier | Meaning | Handled by |
|---|---|---|
| **A** | open and readable by the tools: open-access scholarship, public-domain primary texts, free modern voices (blogs, interviews, essays) | collected and extracted by Claude |
| **B** | searchable but huge: oral-history archives and the like, reachable only by keyword-targeted pulls | targeted pulls by Claude, logged by exact query |
| **C** | blocked or restricted to the tools: paywalls, bot-blocked archives, lending-only books | **the developer fetches by hand** from `Tier_C_Shopping_List.md` into `Tier_C_Dropbox/`; Claude then extracts |

## Rules (inherited from the rest of the project, restated because they bite here)

1. **Own words, short quotations only, page citations.** Public-domain text (pre-1931 U.S. publication) may be quoted at greater length where an
   example is the point; every other source gets own-words distillation with quotations of a few words to a sentence.
2. **Every quotation must be re-read at its source before it goes into a design document.** Pages fetched through a summarizing tool can
   mis-quote; the raw text copies in `source_texts/` exist so a quotation can be checked locally.
3. **Source-shape honesty.** Each extraction states what the source does *not* contain (no vignette, no joke texts, no defector content), so no one
   goes looking for it there.
4. **American English spelling everywhere**, including titles and quotations, never inside URLs (project rule; no proper-noun exception).
5. **Do not circumvent blocks, paywalls or lending limits.** If a source is blocked it goes on the Tier C list; it is not worked around.
6. **Real-world material is mechanism, not specification.** The defector's origin military is not fixed in this folder, so sources span armies on
   purpose. Tepenian culture is produced locally from its own divergence operator.
7. **Log dead ends** (query, source, where it died) in the checklist's search log, the same discipline as the research logs elsewhere.

## Cross-links

- Lead lists and search logs: `../PTSD_Military_Trauma_Research/11_Dark_Humor_Source_Leads.md` and `11a`–`11d`.
- The character this serves: `Worldspace/Characters/Humans/recruitable/Unnamed_Cancer_Defector/README.md`.
- Related clinical material: `../PTSD_Military_Trauma_Research/07_Treating_PTSD_Clinical_Handbook.md` (moral injury, Findings 185–205; complex trauma, 206–232; posttraumatic growth, 233–266).
- Index: `../Book_Extraction_Index.md` (this folder has a row in Section 4b).
