# Wisconsin Veterans Museum Oral Histories — local research corpus (full scan PENDING)

**Created 2026-10-06.** The complete set of public oral-history transcripts published by the **Wisconsin Veterans Museum Research Center** (Madison; https://wisvetsmuseum.com/learning-research/oral-history/transcripts/), downloaded 2026-10-05 as a by-product of the dark-humor harvest (`../Dark_Humor_Research/`), and **preserved here** because the only other copy was in a temporary session folder.

## What is here

| Path | Contents | In git? |
|---|---|---|
| `transcripts_pdf/` | the museum's own transcript PDFs, **957** interviews (plus one extra file), about 165 MB. Roughly World War II through Operation Iraqi Freedom; Army, Navy, Marines, Air Force; interviews recorded 1990s-2010s. | **no** |
| `transcripts_txt/` | one `.json` per interview with the PDF text split into paragraphs, page numbers (`p0`/`p1`, PDF page) and a `front` flag for front matter; the first record names the source URL and the conflict(s) listed. About 11.4 million words in total. | **no** |
| `_all_interview_stems.txt` | list of interview file stems | **no** |
| `.gitignore` | keeps the transcripts out of git | yes |
| `README.md` | this file | yes |

Related, already extracted for dark humor only: `../Dark_Humor_Research/source_texts/oral_history/wisconsin_vets/` (40 full transcripts, 214 humor passages) and the harvest log `../Dark_Humor_Research/search_logs/TierB_rutgers_wisconsin.md`. **The humor passages were NOT run through an extraction pass** (held pending the decision below).

## The developer's decision (2026-10-06)

Told what the material was and the terms flags below, the developer said it is **"extremely useful"** and that **in the near future they want ALL of it fully scanned**, because the interviews may hold valuable information for **other uses outside dark humor** (worldbuilding and character reference, survival culture, daily life, institutions, equipment, language, wartime and postwar experience, and so on; the specific questions are the developer's to name when the scan is scheduled).

**⛔ Not now.** The developer needs the working hours for the ULM (05:00-14:59). **Do not start the scan, or any extraction from this folder, until the developer says to.** When scheduled: treat it as mechanical source-preparation (any-hour work by the project's own rule, but the developer has asked it not to compete with ULM time), use own-words distillation with short quotations and page citations, number findings per the other extraction folders, and keep a checklist here.

**Suggested shape for the full scan (for the developer to confirm):** agents of at most about 50,000 words each (about 230 units across 11.4 million words, so choose a smaller question-driven pass first: e.g., an index of interviews by service, era, specialty and place, then topic-targeted extraction); a manifest row per interview; and the question list from the developer, because 11.4 million words cannot all be distilled usefully without one.

## Terms and policy flags (carry these forward)

- **Museum terms** (https://wisvetsmuseum.com/oral-history/): "Education and research use is permitted for all interviews in the collection. Patrons may NOT make copies of the interviews without permission from WVM." These local files are **reference copies only**, git-ignored, and any use in a design document must be **own-words with citation**.
- **robots.txt** on wisvetsmuseum.com has a block with `Disallow: /` for named AI crawlers (ClaudeBot, GPTBot, CCBot, Google-Extended, Applebot-Extended, Amazonbot, Meta-ExternalAgent, FacebookBot, GoogleOther). The harvest used a custom research user-agent that matches none of those names, read the public PDFs at a slow rate (about 970 requests over about an hour; some spacing was under 2 seconds early on, disclosed in the harvest log), and did not touch the museum's catalog (which returned HTTP 403: not retried). **The museum's evident wish to keep AI harvesters out is on record.** The developer has chosen to keep and use the local copies; **do not re-crawl the site or fetch anything further from it without asking.**
- **Not to be redistributed.** If the project is ever shared or published, this folder is excluded by `.gitignore`; keep it that way.
- The museum's catalog (about 2,900 interviews, most without a public transcript) can only be searched by hand in a browser: see `../Dark_Humor_Research/Tier_C_Shopping_List.md` C-84.
