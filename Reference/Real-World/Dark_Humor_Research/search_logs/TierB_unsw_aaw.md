# Tier B search log: UNSW Australians at War Film Archive (AAWFA)

Run started: 2026-10-06 (agent run; previous run of this task was stopped before saving anything).
Host: https://australiansatwarfilmarchive.unsw.edu.au/
User-Agent used on every request: `InnerTepeniaResearch/1.0 (personal literature research; low-rate)`
Spacing: at least 5 s (measured end-of-request to start-of-next) on this host; one process; no parallelism. In practice every gap was 6 s or more (see section 2).

## 0. RESULT SUMMARY

- **Terms outcome:** permitted; proceeded (section 1). robots.txt does not exist (HTTP 404); the archive's FAQ and home page expressly allow reuse of quotes and extracts and free download for non-commercial use, with acknowledgment. Nothing was blocked, so there is no Tier C hold-back; section 6 lists instead what a human could still pull.
- **Saved:** 40 full transcripts (the cap) in `source_texts/oral_history/unsw_aaw/` and **172 passages** in `_PASSAGES_unsw_aaw.md`, every one machine-checked as a contiguous verbatim span of its saved transcript (0 failures), each at most 350 words (longest 349), all tags from the allowed set.
- **Coverage of the saved set:** Vietnam (about 15 narrators, Army, Navy and RAAF, including a nurse, a medic-radiographer, a Civil Affairs officer and a pioneer sergeant who later served in East Timor); Korea (Australian and British units, RAN); Malaya, Borneo and Confrontation-era Navy and Army; peacekeeping and modern operations (Somalia, Rwanda, East Timor, Bougainville, SAS counter-terrorism and Sinai peacekeeping); WWII Army (Middle East, Greece, Crete, Kokoda, Gona, Bougainville), WWII air force, Burma-railway POWs and a prisoner in Java, and women's service (AWAS, nurses).
- **Passage tag totals:** nickname 42; humor-as-coping-explained 59; humor-about-command/brass 50; gallows-humor 38; prank 37; humor-about-dead/wounded 30; humor-about-self 29; humor-after-service/civilians 28; other 27; content-note 26; humor-stopped/limits 24; humor-about-enemy 16; humor-in-captivity 16.
- **Not covered:** the archive holds almost no Afghanistan or Iraq veterans (filmed 1999-2004; the Gulf War II and War on Terror themes are empty), so that gap cannot be filled from this source.
- **Content boundary applied:** passages built around excreta, latrines or other bodily waste were skipped and are listed in section 5; graphic or cruel material was kept and tagged `content-note`.

## 1. TERMS CHECK (mandatory, done before any crawl)

Outcome: **PROCEED.** No prohibition on automated access, copying or reuse; no AI-crawler disallow; reuse is expressly permitted for non-commercial use.

| Item | URL | Fetched | Result |
|---|---|---|---|
| robots.txt | https://australiansatwarfilmarchive.unsw.edu.au/robots.txt | 2026-10-06 07:52 UTC | **HTTP 404** (default nginx "page not found"). No Disallow lines, no Crawl-delay, no named-crawler rules exist. (Standard practice: no robots file = no robots restrictions; we still hold ourselves to the 5 s spacing.) |
| Home page statement | https://australiansatwarfilmarchive.unsw.edu.au/ | 2026-10-06 07:52 UTC | See quote A |
| FAQ | https://australiansatwarfilmarchive.unsw.edu.au/faq | 2026-10-06 07:52 UTC | See quote B |
| About | https://australiansatwarfilmarchive.unsw.edu.au/about | 2026-10-06 07:53 UTC | See quote C |
| UNSW Copyright & Disclaimer (linked from the home page, "See also") | https://www.unsw.edu.au/copyright-disclaimer | 2026-10-06 07:53 UTC | See quote D |

Quote A (home page, verbatim):
> "The Australians at War Film Archive is a repository of lived war time experiences told by the people who were there. It is shared freely in the public domain to be used in good faith and with respect to the interviewees who generously shared their stories. Content may be freely downloaded for appropriate non-commercial use. For commercial enquiries contact [email protected] to discuss. See also the UNSW Copyright disclaimer."

Quote B (FAQ, "Do I need permission to copy or publish materials from the Archive?"):
> "No, the Australians at War Film Archive is a self-service resource made freely available to all in the public domain. You can use and reproduce content - including publish quotes, extracts, audio, video or photographs in your project - without seeking further permission. Please acknowledge the Archive as the source of the material: Transcript of interview with [First name Surname], [DD Month YYYY], Australians at War Film Archive (Archive No […]) http://australiansatwarfilmarchive.unsw.edu.au retrieved [DD Month YYYY]"

Quote B2 (FAQ, "Can I have a copy of the interview transcript?"):
> "Yes, you can directly download a PDF copy of a transcript by selecting the option on the left-hand side of the interview or you can select the HTML option and save as a PDF using your browser's 'print to PDF' functionality."

Quote C (About, 2021 refresh):
> "The refreshed site offers direct download of digital transcripts, photographs and interview videos that provide an unparalleled resource for historians, students, teachers, researchers, writers, film makers and all Australians interested in our wartime heritage." ... "The refreshed Archive enables searching on or offline and easier access and re-use of the content." ... "Powerful keyword searching enables precise and systematic research to be undertaken across the archive content as was originally intended by the original project team."

Quote D (UNSW general disclaimer, generic site-wide text; the archive's own statements above are the specific ones):
> "...the information on this Web server is for personal and/or educational use only and is provided in good faith without any express or implied warranty." (Copyright paragraph: UNSW-owned material may be copied if unaltered and the University is acknowledged; "Permission is not given for any commercial use or sale".)

Reading: our use is personal/non-commercial literature research, with the transcripts kept verbatim and unaltered and the archive acknowledged in each saved file. Nothing found restricts automated retrieval at low rate. Standing caveats we honor: (1) non-commercial only — these files are research notes, not for redistribution or commercial use; (2) acknowledge the archive as source (done in each file header); (3) the FAQ and About warn that the content is "memories and reflections," "does not claim to be an accurate historical record," and may contain offensive language and negative stereotypes — passages are saved verbatim and tagged `content-note` where relevant; (4) transcripts contain editor insertions in square brackets [ ] (About page) — kept as-is.

Attribution format used in file headers (from FAQ): "Transcript of interview with [Name], [date], Australians at War Film Archive (Archive No ...) http://australiansatwarfilmarchive.unsw.edu.au retrieved [date]".

## 2. How listings / search work

- Site structure: `/` (home, with search box), `/search/browse` (Browse), `/faq`, `/about`, `/contact`, `/archive/<id>` (interview page; ids are the "Archive No", 1 to about 2,5xx), `/archive/htmlTranscript/<id>` (the archive's own "Interview transcript as HTML" download, offered on each interview page for printing/saving), `/archive/transcript/<id>` and `/archive/archive/<id>` (JSON used by the interview page's own script), `/search/browseThemeLists` and `/search/getThemeHierarchy` (JSON used by the Browse page).
- Search: the human-facing search form is `GET /search/?searchFor=<text>`, but the results are drawn by the page's own JavaScript from a JSON endpoint, `GET /search/issue?searchFor=<text>&startFrom=<n>&fetchCount=<n>` (optional `theme[]=<theme name>` and `servedwith[]=<unit>` facets). This is the same request a browser makes when a person presses Search; there is no robots.txt, so nothing is disallowed. I called only the permitted public search path, the interview-page links, the Browse JSON and the official transcript download, never anything behind a login.
- The back end is Solr (edismax): full-text over the entire 5-9 hour transcript of each interview (`alltext` plus a stemmed copy), `q.op=AND` (so a multi-word query without quotes matches any interview containing all the words anywhere), phrase search with double quotes works, and proximity phrases such as `"humour dead"~10` work. Stemming merges singular/plural and tenses (`jokes` = `joking`; `prank` = `pranks`; `nickname` = `nicknamed`), but not British/American spelling (`humour` and `humor` are different result sets). Each result carries up to 2 highlighted snippets of about 200 characters, which is how hits were triaged. Results are ranked by relevance and a response returns at most the fetchCount asked for; I paged 20 at a time (up to 3 pages = top 60 for the very common terms; common-term lists beyond the top 60 were not walked).
- Because the unit of a hit is a whole interview, a hit means "this interview contains the words" and not "this interview is about humor". Many hits on the practical-joke phrases are the interviewer's own question ("Did you play practical jokes?") followed by a short or negative answer. Candidates were therefore ranked by how many different high-signal queries they appeared in, and then every saved transcript was read at its keyword clusters before any passage was taken.
- Facets: Browse lists the top-level themes (Bougainville, East Timor, Gulf War I, Gulf War II, Indonesian Confrontation, Korea, Malaya, Normandy landing, Other themes, Solomon Islands, UN Operations, Vietnam, War on Terror, World War I, World War II, World War II - Women). The archive is overwhelmingly WWII (about 626 of the 828 interviews hitting `humour`), so the modern-conflict material had to be reached by adding `theme[]=` restrictions.
- Request discipline: single process, one request at a time, at least 6 seconds from the end of one request to the start of the next (the helper script locks and enforces this; the request log shows a minimum start-to-start gap of 6.0 s), one User-Agent string, responses cached on disk so no URL was fetched twice. Of the 597 logged requests (596 to the archive host and 1 to www.unsw.edu.au, 07:52 to 09:11 UTC on 2026-10-06), every one returned HTTP 200 except robots.txt (404, by design); no HTTP 403 or 429 was received at any point, so no 20-minute back-off was ever triggered. Measured over the whole request log the minimum start-to-start gap was 6.0 s and the median 7.0 s. The one request to another host was the linked UNSW copyright page. Request types: 470 search calls, 117 official transcript downloads, 10 other pages (terms pages, Browse, one interview page and its metadata).

- Working pipeline (so the saved text cannot drift from the source): (1) a polite fetch wrapper (single lock file, 6 s minimum gap measured after each response, response cache, request log); (2) a search wrapper that pages `/search/issue`, records each query with numFound and the retrieved ids, and keeps a running candidate table with which queries hit each interview; (3) a transcript saver that converts the official HTML transcript into plain UTF-8 text (tape markers `=== TAPE n ===`, timestamp lines `[Tn mm:ss]`, `Q:` and `A:` labels, square-bracket editor notes untouched), first into a staging area outside the project folder; (4) a keyword-cluster viewer used to read each staged transcript; (5) a passage extractor that takes a start phrase and an end phrase, cuts that contiguous span directly out of the saved text (ignoring only curly versus straight quotes and whitespace when locating the anchors), refuses spans over 350 words, and promotes the transcript into the project folder only when its first passage is added; (6) a verifier that re-checks every passage in the passages file as a contiguous substring of its saved transcript, plus word counts, tag vocabulary and the six-line file headers (last result: 172 passages, 0 failures).

<!--AUTO:QUERIES-->
## 3. Queries run (exact strings and hit counts)

Every query was sent to `/search/issue` (see section 2). `numFound` = number of interviews whose transcript matches; `retrieved` = how many of those were pulled (20 per page, usually up to 3 pages); a retrieved number below numFound means the rest of that list was not walked. Syntax: double quotes = phrase, `~N` = words within N of each other, `[theme=X]` = restricted to that theme facet. Queries were run in time order; the first run of each exact string is listed.

| # | UTC | query | numFound | retrieved |
|---|---|---|---|---|
| 1 | 07:54 | `gallows humour` | 15 | 15 |
| 2 | 07:54 | `"gallows humour"` | 11 | 11 |
| 3 | 07:55 | `"gallows humor"` | 0 | 0 |
| 4 | 07:55 | `"black humour"` | 33 | 20 |
| 5 | 07:55 | `"black humor"` | 0 | 0 |
| 6 | 07:55 | `"dark humour"` | 6 | 6 |
| 7 | 07:55 | `"black sense of humour"` | 1 | 1 |
| 8 | 07:56 | `"dark sense of humour"` | 0 | 0 |
| 9 | 07:56 | `"sick humour"` | 2 | 2 |
| 10 | 07:56 | `"sick sense of humour"` | 1 | 1 |
| 11 | 07:56 | `"practical joke"` | 71 | 60 |
| 12 | 07:56 | `"practical jokes"` | 71 | 60 |
| 13 | 07:57 | `"gallows"` | 23 | 23 |
| 14 | 07:58 | `humour` | 828 | 60 |
| 15 | 07:58 | `humor` | 332 | 60 |
| 16 | 07:59 | `jokes` | 1345 | 60 |
| 17 | 07:59 | `joking` | 1345 | 60 |
| 18 | 07:59 | `laughed` | 1408 | 60 |
| 19 | 08:00 | `laughter` | 205 | 60 |
| 20 | 08:00 | `"a good laugh"` | 75 | 60 |
| 21 | 08:00 | `prank` | 178 | 60 |
| 22 | 08:01 | `pranks` | 178 | 60 |
| 23 | 08:01 | `nickname` | 764 | 60 |
| 24 | 08:01 | `nicknamed` | 764 | 60 |
| 25 | 08:02 | `larrikin` | 276 | 60 |
| 26 | 08:02 | `"made fun of"` | 33 | 33 |
| 27 | 08:02 | `"we laughed"` | 154 | 60 |
| 28 | 08:03 | `"sense of humour"` | 498 | 60 |
| 29 | 08:03 | `"bush humour"` | 0 | 0 |
| 30 | 08:03 | `"Aussie humour"` | 10 | 10 |
| 31 | 08:03 | `"Australian humour"` | 32 | 32 |
| 32 | 08:03 | `"black comedy"` | 1 | 1 |
| 33 | 08:03 | `"laughed dead"~10` | 15 | 15 |
| 34 | 08:03 | `"laugh wounded"~10` | 9 | 9 |
| 35 | 08:04 | `"laughed killed"~10` | 76 | 60 |
| 36 | 08:04 | `"humour dead"~10` | 4 | 4 |
| 37 | 08:04 | `"joke dead"~10` | 6 | 6 |
| 38 | 08:04 | `"jokes body"~10` | 2 | 2 |
| 39 | 08:04 | `"humour officers"~10` | 19 | 19 |
| 40 | 08:04 | `"humour brass"~10` | 0 | 0 |
| 41 | 08:04 | `"humour coming home"~10` | 3 | 3 |
| 42 | 08:04 | `"humour civilians"~15` | 3 | 3 |
| 43 | 08:05 | `"nobody laughed"` | 4 | 4 |
| 44 | 08:05 | `"stopped laughing"` | 34 | 34 |
| 45 | 08:05 | `"humour wore thin"` | 0 | 0 |
| 46 | 08:05 | `"lost my sense of humour"` | 1 | 1 |
| 47 | 08:05 | `"couldn't laugh"` | 0 | 0 |
| 48 | 08:05 | `"wasn't funny"` | 4 | 4 |
| 49 | 08:05 | `"laughing at death"` | 4 | 4 |
| 50 | 08:05 | `"laughed at death"` | 4 | 4 |
| 51 | 08:06 | `"coping mechanism" humour` | 25 | 25 |
| 52 | 08:06 | `"humour kept us going"` | 0 | 0 |
| 53 | 08:06 | `"you had to laugh"` | 17 | 17 |
| 54 | 08:06 | `"laugh or cry"` | 9 | 9 |
| 55 | 08:06 | `"if we didn't laugh"` | 0 | 0 |
| 56 | 08:06 | `"sick joke"` | 5 | 5 |
| 57 | 08:06 | `"sick jokes"` | 5 | 5 |
| 58 | 08:06 | `"morbid humour"` | 0 | 0 |
| 59 | 08:06 | `"callous humour"` | 0 | 0 |
| 60 | 08:07 | `macabre` | 33 | 33 |
| 61 | 08:07 | `"piss-take"` | 4 | 4 |
| 62 | 08:07 | `"taking the piss"` | 20 | 20 |
| 63 | 08:07 | `"digger humour"` | 2 | 2 |
| 64 | 08:07 | `"army humour"` | 1 | 1 |
| 65 | 08:07 | `"military humour"` | 0 | 0 |
| 66 | 08:08 | `humour [theme=East Timor]` | 5 | 5 |
| 67 | 08:08 | `humor [theme=East Timor]` | 2 | 2 |
| 68 | 08:08 | `jokes [theme=East Timor]` | 7 | 7 |
| 69 | 08:08 | `laughed [theme=East Timor]` | 7 | 7 |
| 70 | 08:09 | `laughter [theme=East Timor]` | 0 | 0 |
| 71 | 08:09 | `prank [theme=East Timor]` | 2 | 2 |
| 72 | 08:09 | `nickname [theme=East Timor]` | 1 | 1 |
| 73 | 08:09 | `"black humour" [theme=East Timor]` | 0 | 0 |
| 74 | 08:09 | `"sense of humour" [theme=East Timor]` | 4 | 4 |
| 75 | 08:09 | `funny [theme=East Timor]` | 9 | 9 |
| 76 | 08:09 | `humour [theme=UN Operations]` | 12 | 12 |
| 77 | 08:09 | `humor [theme=UN Operations]` | 5 | 5 |
| 78 | 08:09 | `jokes [theme=UN Operations]` | 11 | 11 |
| 79 | 08:09 | `laughed [theme=UN Operations]` | 13 | 13 |
| 80 | 08:10 | `laughter [theme=UN Operations]` | 0 | 0 |
| 81 | 08:10 | `prank [theme=UN Operations]` | 1 | 1 |
| 82 | 08:10 | `nickname [theme=UN Operations]` | 5 | 5 |
| 83 | 08:10 | `"black humour" [theme=UN Operations]` | 0 | 0 |
| 84 | 08:10 | `"sense of humour" [theme=UN Operations]` | 8 | 8 |
| 85 | 08:10 | `funny [theme=UN Operations]` | 18 | 18 |
| 86 | 08:10 | `humour [theme=Gulf War I]` | 2 | 2 |
| 87 | 08:10 | `humor [theme=Gulf War I]` | 1 | 1 |
| 88 | 08:10 | `jokes [theme=Gulf War I]` | 2 | 2 |
| 89 | 08:11 | `laughed [theme=Gulf War I]` | 4 | 4 |
| 90 | 08:11 | `laughter [theme=Gulf War I]` | 0 | 0 |
| 91 | 08:11 | `prank [theme=Gulf War I]` | 0 | 0 |
| 92 | 08:11 | `nickname [theme=Gulf War I]` | 1 | 1 |
| 93 | 08:11 | `"black humour" [theme=Gulf War I]` | 0 | 0 |
| 94 | 08:11 | `"sense of humour" [theme=Gulf War I]` | 0 | 0 |
| 95 | 08:11 | `funny [theme=Gulf War I]` | 5 | 5 |
| 96 | 08:11 | `humour [theme=Gulf War II]` | 0 | 0 |
| 97 | 08:11 | `humor [theme=Gulf War II]` | 0 | 0 |
| 98 | 08:11 | `jokes [theme=Gulf War II]` | 0 | 0 |
| 99 | 08:12 | `laughed [theme=Gulf War II]` | 0 | 0 |
| 100 | 08:12 | `laughter [theme=Gulf War II]` | 0 | 0 |
| 101 | 08:12 | `prank [theme=Gulf War II]` | 0 | 0 |
| 102 | 08:12 | `nickname [theme=Gulf War II]` | 0 | 0 |
| 103 | 08:12 | `"black humour" [theme=Gulf War II]` | 0 | 0 |
| 104 | 08:12 | `"sense of humour" [theme=Gulf War II]` | 0 | 0 |
| 105 | 08:12 | `funny [theme=Gulf War II]` | 0 | 0 |
| 106 | 08:12 | `humour [theme=War on Terror]` | 0 | 0 |
| 107 | 08:12 | `humor [theme=War on Terror]` | 0 | 0 |
| 108 | 08:13 | `jokes [theme=War on Terror]` | 0 | 0 |
| 109 | 08:13 | `laughed [theme=War on Terror]` | 0 | 0 |
| 110 | 08:13 | `laughter [theme=War on Terror]` | 0 | 0 |
| 111 | 08:13 | `prank [theme=War on Terror]` | 0 | 0 |
| 112 | 08:13 | `nickname [theme=War on Terror]` | 0 | 0 |
| 113 | 08:13 | `"black humour" [theme=War on Terror]` | 0 | 0 |
| 114 | 08:13 | `"sense of humour" [theme=War on Terror]` | 0 | 0 |
| 115 | 08:13 | `funny [theme=War on Terror]` | 0 | 0 |
| 116 | 08:13 | `humour [theme=Bougainville]` | 36 | 36 |
| 117 | 08:14 | `humor [theme=Bougainville]` | 13 | 13 |
| 118 | 08:14 | `jokes [theme=Bougainville]` | 63 | 40 |
| 119 | 08:14 | `laughed [theme=Bougainville]` | 72 | 40 |
| 120 | 08:14 | `laughter [theme=Bougainville]` | 11 | 11 |
| 121 | 08:14 | `prank [theme=Bougainville]` | 8 | 8 |
| 122 | 08:14 | `nickname [theme=Bougainville]` | 43 | 40 |
| 123 | 08:15 | `"black humour" [theme=Bougainville]` | 2 | 2 |
| 124 | 08:15 | `"sense of humour" [theme=Bougainville]` | 21 | 21 |
| 125 | 08:15 | `funny [theme=Bougainville]` | 87 | 40 |
| 126 | 08:15 | `humour [theme=Solomon Islands]` | 0 | 0 |
| 127 | 08:15 | `humor [theme=Solomon Islands]` | 0 | 0 |
| 128 | 08:15 | `jokes [theme=Solomon Islands]` | 0 | 0 |
| 129 | 08:15 | `laughed [theme=Solomon Islands]` | 0 | 0 |
| 130 | 08:16 | `laughter [theme=Solomon Islands]` | 0 | 0 |
| 131 | 08:16 | `prank [theme=Solomon Islands]` | 0 | 0 |
| 132 | 08:16 | `nickname [theme=Solomon Islands]` | 0 | 0 |
| 133 | 08:16 | `"black humour" [theme=Solomon Islands]` | 0 | 0 |
| 134 | 08:16 | `"sense of humour" [theme=Solomon Islands]` | 0 | 0 |
| 135 | 08:16 | `funny [theme=Solomon Islands]` | 0 | 0 |
| 136 | 08:16 | `humour [theme=Indonesian Confrontation]` | 18 | 18 |
| 137 | 08:16 | `humor [theme=Indonesian Confrontation]` | 6 | 6 |
| 138 | 08:16 | `jokes [theme=Indonesian Confrontation]` | 33 | 33 |
| 139 | 08:17 | `laughed [theme=Indonesian Confrontation]` | 32 | 32 |
| 140 | 08:17 | `laughter [theme=Indonesian Confrontation]` | 5 | 5 |
| 141 | 08:17 | `prank [theme=Indonesian Confrontation]` | 3 | 3 |
| 142 | 08:17 | `nickname [theme=Indonesian Confrontation]` | 24 | 24 |
| 143 | 08:17 | `"black humour" [theme=Indonesian Confrontation]` | 3 | 3 |
| 144 | 08:17 | `"sense of humour" [theme=Indonesian Confrontation]` | 8 | 8 |
| 145 | 08:18 | `funny [theme=Indonesian Confrontation]` | 43 | 40 |
| 146 | 08:18 | `humour [theme=Malaya]` | 51 | 51 |
| 147 | 08:18 | `humor [theme=Malaya]` | 25 | 25 |
| 148 | 08:18 | `jokes [theme=Malaya]` | 80 | 60 |
| 149 | 08:19 | `laughed [theme=Malaya]` | 89 | 60 |
| 150 | 08:19 | `prank [theme=Malaya]` | 11 | 11 |
| 151 | 08:19 | `"black humour" [theme=Malaya]` | 2 | 2 |
| 152 | 08:19 | `"sense of humour" [theme=Malaya]` | 31 | 31 |
| 153 | 08:19 | `"gallows humour" [theme=Malaya]` | 0 | 0 |
| 154 | 08:20 | `funny [theme=Malaya]` | 103 | 60 |
| 155 | 08:20 | `"made fun of" [theme=Malaya]` | 2 | 2 |
| 156 | 08:20 | `humour [theme=Korea]` | 58 | 58 |
| 157 | 08:20 | `humor [theme=Korea]` | 29 | 29 |
| 158 | 08:21 | `jokes [theme=Korea]` | 115 | 60 |
| 159 | 08:21 | `laughed [theme=Korea]` | 116 | 60 |
| 160 | 08:21 | `prank [theme=Korea]` | 19 | 19 |
| 161 | 08:21 | `"black humour" [theme=Korea]` | 2 | 2 |
| 162 | 08:22 | `"sense of humour" [theme=Korea]` | 42 | 42 |
| 163 | 08:22 | `"gallows humour" [theme=Korea]` | 0 | 0 |
| 164 | 08:22 | `funny [theme=Korea]` | 150 | 60 |
| 165 | 08:22 | `"made fun of" [theme=Korea]` | 2 | 2 |
| 166 | 08:23 | `humour [theme=Vietnam]` | 173 | 60 |
| 167 | 08:23 | `humor [theme=Vietnam]` | 60 | 60 |
| 168 | 08:23 | `jokes [theme=Vietnam]` | 256 | 60 |
| 169 | 08:24 | `laughed [theme=Vietnam]` | 265 | 60 |
| 170 | 08:24 | `laughter [theme=Vietnam]` | 31 | 31 |
| 171 | 08:24 | `prank [theme=Vietnam]` | 22 | 22 |
| 172 | 08:24 | `nickname [theme=Vietnam]` | 163 | 60 |
| 173 | 08:24 | `"black humour" [theme=Vietnam]` | 16 | 16 |
| 174 | 08:25 | `"sense of humour" [theme=Vietnam]` | 113 | 60 |
| 175 | 08:25 | `funny [theme=Vietnam]` | 302 | 60 |
| 176 | 08:25 | `"a good laugh" [theme=Vietnam]` | 15 | 15 |
| 177 | 08:25 | `"we laughed" [theme=Vietnam]` | 26 | 26 |
| 178 | 08:26 | `"made fun of" [theme=Vietnam]` | 6 | 6 |
| 179 | 08:26 | `larrikin [theme=Vietnam]` | 49 | 49 |
| 180 | 08:26 | `"practical jokes" [theme=Vietnam]` | 17 | 17 |
| 181 | 08:26 | `"coping mechanism" humour [theme=Vietnam]` | 15 | 15 |
| 182 | 08:26 | `"gallows humour" [theme=Vietnam]` | 2 | 2 |
| 183 | 08:26 | `"dark humour" [theme=Vietnam]` | 0 | 0 |
| 184 | 08:26 | `"sick humour" [theme=Vietnam]` | 2 | 2 |
| 185 | 08:27 | `macabre [theme=Vietnam]` | 11 | 11 |
| 186 | 08:27 | `"taking the piss" [theme=Vietnam]` | 8 | 8 |
| 187 | 08:27 | `"humour officers"~10 [theme=Vietnam]` | 6 | 6 |
| 188 | 08:27 | `"laughed dead"~10 [theme=Vietnam]` | 3 | 3 |
| 189 | 08:27 | `"laughed killed"~10 [theme=Vietnam]` | 13 | 13 |
| 190 | 08:27 | `"laugh wounded"~10 [theme=Vietnam]` | 2 | 2 |
| 191 | 08:27 | `"you had to laugh" [theme=Vietnam]` | 1 | 1 |
| 192 | 08:27 | `"stopped laughing" [theme=Vietnam]` | 9 | 9 |
| 193 | 08:49 | `humour [theme=Prisoners of War]` | 112 | 60 |
| 194 | 08:49 | `"black humour" [theme=Prisoners of War]` | 2 | 2 |
| 195 | 08:49 | `"gallows humour" [theme=Prisoners of War]` | 3 | 3 |
| 196 | 08:49 | `jokes [theme=Prisoners of War]` | 137 | 40 |
| 197 | 08:50 | `laughed [theme=Prisoners of War]` | 153 | 40 |
| 198 | 08:50 | `"you had to laugh" [theme=Prisoners of War]` | 2 | 2 |
| 199 | 08:50 | `"sense of humour" [theme=Prisoners of War]` | 63 | 40 |
| 200 | 08:50 | `nicknamed [theme=Prisoners of War]` | 83 | 40 |
| 201 | 08:50 | `humour [theme=Prisoners of the Japanese (including Thai/Burma, Changi, Sandakan, Japan etc)]` | 56 | 56 |
| 202 | 08:51 | `"black humour" [theme=Prisoners of the Japanese (including Thai/Burma, Changi, Sandakan, Japan etc)]` | 0 | 0 |
| 203 | 08:51 | `"laughed dead"~10 [theme=Prisoners of the Japanese (including Thai/Burma, Changi, Sandakan, Japan etc)]` | 1 | 1 |
| 204 | 08:51 | `humour [theme=Prisoners in Germany]` | 30 | 30 |
| 205 | 08:51 | `"black humour" [theme=World War II - Women]` | 1 | 1 |
| 206 | 08:51 | `humour [theme=World War II - Women]` | 66 | 60 |
| 207 | 08:51 | `"laughed dead"~10 [theme=World War II - Women]` | 0 | 0 |
| 208 | 08:52 | `"dark humour" [theme=World War II - Women]` | 1 | 1 |
| 209 | 08:52 | `"laugh dead"~10` | 15 | 15 |
| 210 | 08:52 | `"laughing dead"~10` | 15 | 15 |
| 211 | 08:52 | `"joked killed"~10` | 23 | 23 |
| 212 | 08:52 | `"jokes wounded"~10` | 5 | 5 |
| 213 | 08:52 | `"joke casualties"~10` | 1 | 1 |
| 214 | 08:52 | `"humour casualties"~10` | 0 | 0 |
| 215 | 08:52 | `"humour dying"~10` | 0 | 0 |
| 216 | 08:52 | `"humour death"~10` | 4 | 4 |
| 217 | 08:53 | `"jokes death"~10` | 4 | 4 |
| 218 | 08:53 | `"laughed funeral"~10` | 2 | 2 |
| 219 | 08:53 | `"jokes burial"~10` | 0 | 0 |
| 220 | 08:53 | `"jokes officers"~10` | 48 | 48 |
| 221 | 08:53 | `"humour sergeant major"~10` | 1 | 1 |
| 222 | 08:53 | `"humour generals"~10` | 14 | 14 |
| 223 | 08:53 | `"jokes commanding officer"~10` | 5 | 5 |
| 224 | 08:54 | `"jokes padre"~10` | 5 | 5 |
| 225 | 08:54 | `"humour returned"~10` | 0 | 0 |
| 226 | 08:54 | `"jokes civilians"~15` | 5 | 5 |
| 227 | 08:54 | `"laugh civilians"~15` | 9 | 9 |
| 228 | 08:54 | `"humour welcome home"~15` | 0 | 0 |
| 229 | 08:54 | `"jokes after the war"~10` | 12 | 12 |
| 230 | 08:54 | `"jokes reunion"~10` | 4 | 4 |
| 231 | 08:54 | `"laugh reunion"~10` | 9 | 9 |
| 232 | 08:54 | `"humour PTSD"~15` | 0 | 0 |
| 233 | 08:54 | `"humour counselling"~15` | 1 | 1 |
| 234 | 08:55 | `"jokes counsellor"~15` | 0 | 0 |
| 235 | 08:55 | `"humour nightmares"~15` | 0 | 0 |
| 236 | 08:55 | `"no humour"` | 828 | 40 |
| 237 | 08:55 | `"lost humour"` | 0 | 0 |
| 238 | 08:55 | `"stopped joking"` | 0 | 0 |
| 239 | 08:55 | `"nothing funny"` | 5 | 5 |
| 240 | 08:56 | `"not funny"` | 1743 | 60 |
| 241 | 08:56 | `"humour wore off"` | 0 | 0 |
| 242 | 08:56 | `"sense of humour disappeared"` | 0 | 0 |
| 243 | 08:56 | `"black humor" Vietnam` | 0 | 0 |
| 244 | 08:56 | `humour Afghanistan` | 90 | 40 |
| 245 | 08:56 | `humour Iraq` | 364 | 40 |
| 246 | 08:57 | `jokes Afghanistan` | 141 | 40 |
| 247 | 08:57 | `jokes Iraq` | 559 | 40 |
| 248 | 08:57 | `humour Rwanda` | 23 | 23 |
| 249 | 08:57 | `humour Somalia` | 23 | 23 |
| 250 | 08:57 | `humour Cambodia` | 88 | 40 |
| 251 | 08:58 | `humour Namibia` | 3 | 3 |
| 252 | 08:58 | `humour Bougainville` | 138 | 40 |
| 253 | 08:58 | `humour Gulf` | 211 | 40 |
| 254 | 08:58 | `"black humour" Rwanda` | 2 | 2 |
| 255 | 08:58 | `"black humour" Somalia` | 0 | 0 |
| 256 | 08:58 | `"black humour" Timor` | 6 | 6 |
| 257 | 08:59 | `"black humour" Vietnam` | 22 | 22 |
| 258 | 08:59 | `"black humour" Korea` | 20 | 20 |
| 259 | 08:59 | `"black humour" Kokoda` | 12 | 12 |
| 260 | 08:59 | `"black humour" Tobruk` | 16 | 16 |
| 261 | 08:59 | `"black humour" bomber` | 22 | 22 |
| 262 | 08:59 | `"black humour" medical` | 31 | 31 |
| 263 | 09:01 | `"laugh about it now"` | 43 | 40 |
| 264 | 09:01 | `"laugh about it today"` | 3 | 3 |
| 265 | 09:01 | `"can laugh about it"` | 26 | 26 |
| 266 | 09:02 | `"look back and laugh"` | 8 | 8 |
| 267 | 09:02 | `"funny now"` | 37 | 37 |
| 268 | 09:02 | `"didn’t seem funny"` | 0 | 0 |
| 269 | 09:02 | `"laugh or you’d cry"` | 0 | 0 |
| 270 | 09:02 | `"cry or laugh"` | 5 | 5 |
| 271 | 09:02 | `"laugh instead of cry"` | 0 | 0 |
| 272 | 09:02 | `"kept us sane"` | 4 | 4 |
| 273 | 09:02 | `"kept me sane"` | 13 | 13 |
| 274 | 09:03 | `"humour sane"~10` | 5 | 5 |
| 275 | 09:03 | `"jokes sane"~10` | 1 | 1 |
| 276 | 09:03 | `"break the tension"` | 12 | 12 |
| 277 | 09:03 | `"relieve the tension"` | 30 | 30 |
| 278 | 09:03 | `"humour tension"~10` | 10 | 10 |
| 279 | 09:03 | `"make light of"` | 38 | 38 |
| 280 | 09:03 | `"made light of"` | 16 | 16 |
| 281 | 09:04 | `"joke about it"` | 296 | 40 |
| 282 | 09:04 | `"joked about it"` | 296 | 40 |
| 283 | 09:04 | `"laugh it off"` | 38 | 38 |
| 284 | 09:04 | `"wisecrack"` | 12 | 12 |
| 285 | 09:04 | `"wisecracks"` | 12 | 12 |
| 286 | 09:05 | `"cracked a joke"` | 26 | 26 |
| 287 | 09:05 | `"crack a joke"` | 26 | 26 |
| 288 | 09:05 | `"joke bodies"~10` | 2 | 2 |
| 289 | 09:05 | `"jokes bodies"~10` | 2 | 2 |
| 290 | 09:05 | `"joked corpses"~10` | 0 | 0 |
| 291 | 09:05 | `"laughed bodies"~10` | 8 | 8 |
| 292 | 09:05 | `"laughed wounded"~10` | 9 | 9 |
| 293 | 09:05 | `"joked wounded"~10` | 5 | 5 |
| 294 | 09:05 | `"humour wounded"~10` | 2 | 2 |
| 295 | 09:06 | `"jokes dying"~10` | 3 | 3 |
| 296 | 09:06 | `"laughed dying"~10` | 5 | 5 |
| 297 | 09:06 | `"laugh grief"~10` | 0 | 0 |
| 298 | 09:06 | `"joke funeral"~10` | 3 | 3 |
| 299 | 09:06 | `"humour funeral"~10` | 0 | 0 |
| 300 | 09:06 | `"humour hospital"~10` | 3 | 3 |
| 301 | 09:06 | `"jokes nurses"~10` | 13 | 13 |
| 302 | 09:06 | `"humour nurses"~10` | 2 | 2 |
| 303 | 09:06 | `"jokes padre"~5` | 1 | 1 |
| 304 | 09:07 | `"humour padre"~10` | 4 | 4 |
| 305 | 09:07 | `"jokes about officers"` | 0 | 0 |
| 306 | 09:07 | `"laughed at the officers"` | 0 | 0 |
| 307 | 09:07 | `"laughing at the officers"` | 0 | 0 |
| 308 | 09:07 | `"jokes about the army"` | 0 | 0 |
| 309 | 09:07 | `"taking the mickey"` | 56 | 40 |
| 310 | 09:07 | `"take the mickey"` | 56 | 40 |
| 311 | 09:07 | `"leg pull"` | 11 | 11 |
| 312 | 09:08 | `"pulling his leg"` | 17 | 17 |
| 313 | 09:08 | `"pulled his leg"` | 17 | 17 |
| 314 | 09:08 | `"set him up"` | 29 | 29 |
| 315 | 09:08 | `"windup"` | 2 | 2 |
| 316 | 09:08 | `"wind up"` | 370 | 40 |
| 317 | 09:08 | `"in good humour"` | 52 | 40 |
| 318 | 09:09 | `"in good fun"` | 538 | 40 |
| 319 | 09:09 | `"funny now" [theme=Vietnam]` | 10 | 10 |
| 320 | 09:09 | `"look back and laugh" [theme=Vietnam]` | 5 | 5 |
| 321 | 09:09 | `"laugh about it now" [theme=Vietnam]` | 17 | 17 |
| 322 | 09:09 | `"can laugh about it" [theme=Vietnam]` | 9 | 9 |
| 323 | 09:09 | `"kept us sane" [theme=Vietnam]` | 0 | 0 |
| 324 | 09:09 | `"humour tension"~10 [theme=Vietnam]` | 1 | 1 |
| 325 | 09:09 | `"jokes sane"~10 [theme=Vietnam]` | 0 | 0 |
| 326 | 09:10 | `"laughed wounded"~10 [theme=Vietnam]` | 2 | 2 |
| 327 | 09:10 | `"jokes bodies"~10 [theme=Vietnam]` | 1 | 1 |
| 328 | 09:10 | `"humour dead"~10 [theme=Vietnam]` | 1 | 1 |
| 329 | 09:10 | `"humour funeral"~10 [theme=Vietnam]` | 0 | 0 |
| 330 | 09:10 | `"laugh civilians"~15 [theme=Vietnam]` | 2 | 2 |
| 331 | 09:10 | `"jokes civilians"~15 [theme=Vietnam]` | 4 | 4 |
| 332 | 09:10 | `spat humour [theme=Vietnam]` | 42 | 40 |
| 333 | 09:10 | `"laugh or cry" [theme=Vietnam]` | 2 | 2 |

Total HTTP requests logged: 597 (including the terms pages, Browse, searches and transcript downloads; one of them went to www.unsw.edu.au).

<!--/AUTO:QUERIES-->

<!--AUTO:FILES-->
## 4. Files saved

Directory: `source_texts/oral_history/unsw_aaw/`. Passages file: `_PASSAGES_unsw_aaw.md` (172 passages so far).

| archive no | file | narrator | war / branch tags | interview date | words | passages |
|---|---|---|---|---|---|---|
| 894 | `unsw_894_lampard.txt` | Kerry Lampard (Lumpy) | Vietnam, Regular army, SAS | 20th November 2003 | 45313 | 3 |
| 575 | `unsw_575_elliot.txt` | Colin Elliot | Vietnam, RAN | 23rd September 2003 | 57996 | 5 |
| 2152 | `unsw_2152_cavanough.txt` | Ian Cavanough (Knackers) | Vietnam, National servicemen | 20th July 2004 | 67098 | 9 |
| 794 | `unsw_794_leis.txt` | Ian Leis (Bop) | Vietnam, Regular army | 28th August 2003 | 31122 | 4 |
| 1038 | `unsw_1038_newell.txt` | James Newell ('Blue') | World War II, New Guinea, Wewak | 30th September 2003 | 53585 | 5 |
| 2199 | `unsw_2199_jones.txt` | Trevor Jones | Vietnam, Regular army | 23rd July 2004 | 36167 | 3 |
| 1669 | `unsw_1669_lennox.txt` | Robert Lennox | Vietnam, National servicemen, Medical orderlies | 16th April 2004 | 55725 | 2 |
| 867 | `unsw_867_bruce.txt` | Barbara Bruce (Barb) | Vietnam, Civilian Medical Aid | 4th September 2003 | 45312 | 3 |
| 1749 | `unsw_1749_heslewood.txt` | John Heslewood (Heso) | Vietnam, National servicemen | 16th April 2004 | 52106 | 6 |
| 1706 | `unsw_1706_fletcher.txt` | Barry Fletcher | Vietnam, RAAF | 30th March 2004 | 55585 | 6 |
| 1399 | `unsw_1399_schunemann.txt` | Edward Schunemann | World War II, British & Commonwealth Occupation Force, Korea | 14th January 2004 | 55242 | 6 |
| 1249 | `unsw_1249_walford.txt` | Adrian Walford (Wally) | Indonesian Confrontation, Army - Indonesian incursions into Sarawak, Vietnam | 10th December 2003 | 52157 | 4 |
| 2304 | `unsw_2304_berg.txt` | Michael von Berg | Vietnam, Regular army | 15th July 2004 | 62927 | 4 |
| 2056 | `unsw_2056_coultmansmith.txt` | Grant Coultman-Smith | Vietnam, Regular army | 19th July 2004 | 40298 | 5 |
| 1182 | `unsw_1182_humphries.txt` | John Humphries | Vietnam, Regular army, East Timor | 5th December 2003 | 56395 | 3 |
| 1679 | `unsw_1679_thompson.txt` | Dale Thompson (Thommo) | UN Operations, Somalia | 24th March 2004 | 76959 | 6 |
| 1975 | `unsw_1975_seymour.txt` | Gregory Seymour (Ces) | UN Operations, Somalia | 27th April 2004 | 48168 | 5 |
| 2461 | `unsw_2461_ramsey.txt` | Wayne Ramsey | UN Operations, Rwanda | 25th August 2004 | 57780 | 3 |
| 1607 | `unsw_1607_fraser.txt` | John Fraser (JJ) | UN Operations, Other un operations, East Timor | 31st March 2004 | 75626 | 4 |
| 2021 | `unsw_2021_hamiltonsmith.txt` | Martin Hamilton-Smith | Other themes, RMC Duntroon all conflicts, MFO Sinai | 2nd July 2004 | 58067 | 4 |
| 1764 | `unsw_1764_andaloro.txt` | Jacqueline Andaloro (Jackie) | Bougainville | 2nd April 2004 | 61256 | 3 |
| 1108 | `unsw_1108_hamilton.txt` | Thomas Hamilton (Hammo or Tom) | Korea, RAN, Malaya | 26th November 2003 | 69798 | 2 |
| 1376 | `unsw_1376_ersser.txt` | Edward Ersser (Ted) | World War II, Children, Former allies living in Australia | 9th March 2004 | 38020 | 4 |
| 1919 | `unsw_1919_martin.txt` | Lyle Martin | World War II, British & Commonwealth Occupation Force, Korea | 4th May 2004 | 55594 | 2 |
| 761 | `unsw_761_joyce.txt` | Stephen Joyce (Steve) | World War II, Other attacks on Australia, Korea | 27th August 2003 | 37464 | 3 |
| 1309 | `unsw_1309_bianchi.txt` | Rudolph Bianchi (Rudi) | Malaya, RAN | 28th January 2004 | 51317 | 3 |
| 949 | `unsw_949_goodall.txt` | Harold Goodall (Harry) | Malaya, RAN | 25th September 2003 | 50039 | 2 |
| 716 | `unsw_716_binstead.txt` | Francis Binstead (Banjo) | World War II, Africa (service/training), Netherlands East Indies (NEI) | 18th August 2003 | 43423 | 9 |
| 607 | `unsw_607_reiter.txt` | Frank Reiter (Blue) | World War II, Bardia, Tobruk | 20th August 2003 | 57031 | 8 |
| 1021 | `unsw_1021_young.txt` | Thomas Young (Tom) | World War II, Africa (service/training), Fighter command | 8th October 2003 | 57463 | 6 |
| 1684 | `unsw_1684_peirce.txt` | Donald Peirce (Don) | World War II, Bardia, Tobruk | 23rd March 2004 | 44279 | 2 |
| 451 | `unsw_451_rowell.txt` | Francis Rowell (Frank) | World War II, Bardia, Tobruk | 10th June 2003 | 42437 | 6 |
| 104 | `unsw_104_medcalf.txt` | Noel Medcalf (Peter) | World War II, Bougainville | 12th May 2003 | 49460 | 6 |
| 1186 | `unsw_1186_simmons.txt` | Gilbert Simmons (Stewart) | World War II, Syria, Papua | 25th November 2003 | 56377 | 3 |
| 44 | `unsw_44_blundell.txt` | Neville Blundell | World War II, Bardia, Greece | 30th April 2003 | 39067 | 5 |
| 614 | `unsw_614_radford.txt` | David Radford (Drill Purposes) | World War II, Papua, Milne Bay | 14th August 2003 | 56710 | 3 |
| 235 | `unsw_235_mcclean.txt` | Douglas McClean (Mac) | World War II, Papua, Beach battles | 30th May 2003 | 40575 | 5 |
| 749 | `unsw_749_tolliday.txt` | John Tolliday (Jack) | World War II, Legacy, Malaya | 8th October 2003 | 41280 | 2 |
| 1018 | `unsw_1018_fazackerley.txt` | June Fazackerley | World War II - Women, Auxiliary Services, AWAS | 29th September 2003 | 50645 | 3 |
| 253 | `unsw_253_sly.txt` | Edward Sly (Ted) | World War II, El Alamein, Fighter command | 26th May 2003 | 47165 | 5 |

<!--/AUTO:FILES-->

## 5. Dead ends and what each died at

Each entry says where the line of inquiry died: at the **query** (the search could not express it, or the wording was wrong), at the **source** (the archive does not contain it), or at the **hit quality** (hits existed but were not usable).

**Died at the source**
- Afghanistan and Iraq (2003 onward): the archive was filmed 1999-2004, so these wars are essentially absent. Every themed query on `Gulf War II`, `War on Terror` and `Solomon Islands` returned 0 (10 terms each); the Browse sample list for Gulf War II is empty. Free-text `humour Afghanistan` (90 hits) and `humour Iraq` (364 hits) are interviews that merely mention the place, not veterans of those operations. `Gulf War I` is small (the Browse sample shows seven names) and most humor queries restricted to it returned 0.
- `"humour funeral"~10`, `"humour casualties"~10`, `"humour dying"~10`, `"jokes burial"~10`, `"joked corpses"~10`, `"laugh grief"~10`: zero or near-zero. The interviewers and veterans do not pair these words closely; the material exists but is described in other words (it was found instead through `"laughed dead"~10`, `"laughed killed"~10` and by reading clusters in the saved files).
- `"humour PTSD"~15`, `"jokes counsellor"~15`, `"humour nightmares"~15`, `"humour welcome home"~15`, `"humour returned"~10`: 0 to 1 hits. Veterans describe homecoming and after-service humor without the words "PTSD" or "counselling" next to "humour"; the best material on this angle was reached through `"laugh civilians"~15` (9 hits), `"laugh reunion"~10` (9), `"jokes reunion"~10` (4), `"jokes after the war"~10` (12) and then by reading whole transcripts.

**Died at the query**
- `"gallows humor"` and `"black humor"` (American spelling) returned 0: the archive's transcripts use British spelling, and the stemmer does not bridge `humor` and `humour` (`humor` alone returns a different set of 332 interviews).
- `"no humour"` returned 828 and `"not funny"` returned 1,743: these are the same counts as plain `humour` and `funny`, because `no` and `not` are stop words and the phrase collapses to its second word. The negative-humor angle (humor stopping) therefore could not be searched as a phrase; it was worked instead through `"stopped laughing"` (34), `"nobody laughed"` (4), `"wasn't funny"` (4), `"lost my sense of humour"` (1), `"sick joke(s)"` (5) and by reading each saved transcript's clusters. `"lost humour"`, `"stopped joking"`, `"humour wore thin"`, `"humour wore off"`, `"sense of humour disappeared"`, `"humour kept us going"`, `"if we didn't laugh"`, `"couldn't laugh"` and `"didn't seem funny"` returned 0; straight-apostrophe phrases do work in this index (`"wasn't funny"` hit), so these zeros are wording, not tokenization.
- `"humour brass"~10` (0): the word "brass" is almost never used; the officer angle was covered by `"humour officers"~10` (19), `"jokes officers"~10`, `"humour sergeant major"~10`, `"humour generals"~10` and `"jokes commanding officer"~10`.
- The broad `AND` behavior meant single-word and loose multi-word queries (`humour` 828, `jokes` 1,345, `laughed` 1,408, `nickname` 764, `"joke about it"` 296) are ranked lists of whole interviews, not of passages; only the top 40 to 60 of each were retrieved, so the tail of those lists was not walked.

**Died at hit quality**
- `"practical joke"` and `"practical jokes"` (71 hits each, same set): about half the hits are the interviewer's question ("Were there practical jokes?") followed by "not that I recall" or a one-line answer; only the interviews where the veteran then tells a story were kept.
- `"gallows humour"` (11) and `"black humour"` (33): many hits are the interviewer's own wording ("Was there a gallows humour?") answered with "No, we didn't have that" (for example 69, 849). Those negative answers are real data on limits but yielded no passage.

**Set aside under the project content boundary (excreta, latrines, bodily waste).** None of these were saved as passages. Locations are given so a human can judge them:
- 1706 Fletcher, Tape 6 about 36:30: flare booby-trapped to an ablution-block chain; Tape 3 about 31:00 to 32:30: a drunk comrade collapsing and vomiting.
- 2304 von Berg, Tape 8 about 32:30 to 34:00: the battalion hygiene corporal and drop-latrine stories; Tape 6 about 28:30: men falling into pit toilets ("hilarious at the time").
- 1399 Schunemann, Tape 3 about 34:30 to 35:00: a lit cigarette dropped into a toilet.
- 749 Tolliday, Tape 5 about 10:00 to 11:30: a match dropped into a thunderbox, and the discomfort that followed.
- 2056 Coultman-Smith, Tape 7 about 16:00 to 16:30: a grim ambush joke about a man killed while relieving himself. It sits between saved passages 1 and 2 of that file; the surrounding sick-humor and coping-mechanism explanation was kept and the joke itself was cut around.
- 1018 Fazackerley, Tape 7 about 12:30: a story in which a woman comrade wets herself while laughing.
- 253 Sly, Tape 2 about 27:30: a pilot urinating beside the aircraft before and after every sortie as a fear response (the rest of that passage was kept from the next sentence).
- 1919 Martin, Tape 2 about 39:30 to 40:30: latrine duty as a punishment.
- 2461 Ramsey, Tape 5 about 02:30: improvising a flush for a broken toilet.
- 1108 Hamilton, Tape 1 about 18:00: hiding in an outdoor toilet.
- 716 Binstead, Tape 5 about 41:00: a concert performer dressed as a woman going out to urinate and being grabbed by a guard.
- Borderline, set aside rather than saved: 1249 Walford, Tape 3 about 03:00 to 05:30 (a cook spitting on an officer's steak; bodily fluid, not waste); 575 Elliot, Tape 1 about 25:30 to 26:30 (the navy "turn in the barrel" gag, anatomical and with a stereotyping framing); 2199 Jones, Tape 5 about 12:00 (a racial-slur nickname given and defended by the veteran).
- Kept but flagged: 716 Binstead, Tape 5 about 39:00 (the Benjo/Banjo mix-up turns on the Japanese word for toilet, but the story is a nickname and language confusion with a guard's beating, not about waste); 1038 Newell, Tape 8 about 22:30 and 1182 Humphries, Tape 6 about 17:00 contain a passing mention of a toilet; remove if the boundary is read strictly.

**Other quality notes**
- The `Tags:` line `content-note` (26 passages) marks passages with graphic death or injury (burning, drowning, a corpse used as a prop), cruelty toward prisoners or the enemy, ethnic or racial wording by the veteran or in a nickname, and strong language.
- The archive's `Q:` and `A:` labels are the transcribers'; a few answers sit under a `Q:` label (for example the "Vietnamese girls there said" passage in 1038). They are left exactly as the archive has them.
- Mid-sentence cut points occur at the start or end of some passages; this is noted in the passages file header.
- Conversion fidelity check (all 40 saved files compared word by word with the official HTML transcript): the only differences are (1) the archive's own embargo notice lines ("This section of transcript is embargoed until 1 January 2034."), present in 7 files, kept as the archive prints them (embargoed stretches are simply absent from the transcript, so no passage was drawn across one), and (2) two timestamp markers written as `[Tn ??:??]` (files 104 and 749), where the archive row had no timestamp. The HTML contains no inline markup inside the question and answer text.


## 6. TIER C — needs a human with a browser

Not triggered. The terms permit use (section 1) and robots.txt does not exist.

**Nothing was withheld under the terms standard**: no prohibition on automated access, copying or reuse was found, and robots.txt does not exist (section 1). This section is therefore a pick-up list for a human with a browser, not a stop notice.

How to search by hand (public pages, no login):
- Site search: `https://australiansatwarfilmarchive.unsw.edu.au/search/?searchFor=<terms>`. Quote a phrase with `%22`, for example `https://australiansatwarfilmarchive.unsw.edu.au/search/?searchFor=%22black+humour%22`. A restriction by theme is added as `&theme=Vietnam` (other theme names: `Korea`, `Malaya`, `East Timor`, `UN Operations`, `Indonesian Confrontation`, `Bougainville`, `Prisoners of War`, `World War II - Women`). The results page lists interviews with highlighted snippets; open one, press the interview-transcript link, and use the browser's find-in-page for the keywords below.
- Official transcript downloads for any interview number N: `https://australiansatwarfilmarchive.unsw.edu.au/archive/htmlTranscript/N` (HTML) and `.../archive/htmlTranscript/N?asPdf=y` (PDF).
- Theme browser: `https://australiansatwarfilmarchive.unsw.edu.au/search/browse#themeHierarchy`.
- Keywords and phrases that were productive (use in the box): `"black humour"`, `"gallows humour"`, `"dark humour"`, `"sick humour"`, `"you had to laugh"`, `"laugh or cry"`, `"stopped laughing"`, `"nobody laughed"`, `"laughed dead"~10`, `"laughed killed"~10`, `"laugh civilians"~15`, `"laugh reunion"~10`, `"jokes after the war"~10`, `"coping mechanism" humour`, `"made light of"`, `"break the tension"`, `"taking the piss"`, `nicknamed`, `larrikin`. Terms that failed and should not be retried as phrases: anything beginning `no` or `not` (stop words), and American spellings.

Items a human could still pull:
1. The audio and video of any interview were not touched (transcripts only); tone, delivery and laughter are only in the recordings, which the archive allows to be downloaded.
2. The un-walked tails of the broad lists (`humour` 828, `jokes` 1,345, `laughed` 1,408, `nickname` 764, `"joke about it"` 296, `"in good fun"` 538).
3. The excreta-boundary and borderline passages listed in section 5, if the project owner decides otherwise.
4. The unread or only briefly read interviews in section 7.


## 7. Open threads

- **Downloaded, evaluated, not kept (staged outside the project folder, 7):** 1810 Le Page (RAAF aircrew; was kept at first, then dropped to respect the 40-file cap because its three passages were the lightest; they included the "hosed out the tail gunners" black-humor remark at Tape 3 about 40:00 and his brother's hoax of troops told not to have had sex before their injections at Tape 2 about 40:00, which are worth restoring if a slot opens); 1831 Gates (6 RAR; not read beyond the keyword hit "practical jokes and stuffing around"); 1493 S. Andaloro (East Timor, Military Information; 19 queries hit it); 2402 Schmitt (RAAF pilot, East Timor; one usable passage at Tape 1 about 24:30, apprentice pranks being "missing now" as "not politically correct"); 2135 Moss (Rwanda); 154 McKellar (AAMWS/AGH nurse, 84 humor-keyword hits, unread); 1770 Woodford (RAAF Vietnam; a story told at his brother's funeral that "everyone laughed").
- **Highest-scoring interviews never read in full** (rank = weighted overlap of the high-signal queries; ids are archive numbers): 1483 Webster (Vietnam recon flight, 27 queries); 1045 Naughton (senior medical officer, Vietnam, 22); 406 Owens (Vietnam logistics, comedian in the unit); 995 Hills (Malaya chaplain, 16); 1140 Roberts (Vietnam/Borneo); 1711 Dittmar (Korea/Vietnam REME); 1167 Plenty (Confrontation/Malaya/Vietnam); 1780 Espie (Vietnam field hospital nurse); 1599 Cunningham (Vietnam intelligence); 2067 Stuart; 634 Burns (Korea); 2226 Jamieson; 2482 White (Vietnam doctor, "black humour" hit); 1293 Laverty; 1375 Stein and 1252 Fry (Vietnam entertainers); 2415 Sheppard (Borneo, AATTV); 2118 Arundel (Korea, Navy); 583 Warland-Browne (WWII medical POW; "gallows humour" hit); 1217 Ward (WWII "Aussie black humour" hit); 2029 Bacskai (SAS); 935 McDermott (Vietnam, AATTV); 1008 Dalton (Korea); 924 Bentley (Bomber Command: a crew tried humor to break tension and it "was knocked on the head because it wasn't professional", a useful limit); 826 Skeers (WWII nurse laying out bodies: "they laughed at me"); 1255 Maidment (merchant navy); 2519 Thrupp (East Timor: practical jokes set up around a mate "and at the end you all laugh together"). Several of these were density-scored from a downloaded transcript (1483, 1045, 995, 656, 1711, 1599 and others) and read only through search snippets.
- **Thin angles** worth another pass with different wording: humor stopping (24 passages, mostly implicit); the first-person experience of civilians not getting the jokes (28 passages are about after-service humor, but few say civilians did not understand); humor around leaving service or discharge; humor by women who served (3 files); Vietnam-era homecoming and humor (very few direct hits, since the word pairs failed, section 5).
- **Method note for a repeat run:** candidate ranking by number of distinct high-signal queries worked, but a transcript is only worth saving after its keyword clusters are read; of the 117 transcripts downloaded, 47 were staged for reading, 42 of those were read at their keyword clusters and 40 were kept; the other 70 downloads were scored by keyword density only (hits per 10,000 words, and how many hits sit within 350 characters of a death, wound or killing word). The helper approach used (search wrapper, staging folder, anchor-based passage extractor that cuts a span out of the saved text so it cannot drift from the source, and a verifier) is recorded in this log's section 2; the scripts were kept in the session scratch area only.
- **Name handling:** passage headings use the narrator names as the archive publishes them (the archive's own citation format requires the name); no contact details, addresses or family details beyond what a veteran says in the quoted passage are included.

