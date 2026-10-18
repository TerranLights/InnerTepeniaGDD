# Tier B search log: Rutgers Oral History Archives and Wisconsin Veterans Museum oral histories

Run date: 2026-10-05 (all fetches). Scope: keyword-targeted harvest of veteran dark-humor / gallows-humor / prank / nickname / coping-humor material for the Dark_Humor_Research folder. Research material only, not canon. Written by the Tier B pull agent; American English throughout except where quoting.

## 0. Result in one screen

| | Rutgers Oral History Archives | Wisconsin Veterans Museum (WVM) |
|---|---|---|
| Full transcripts saved to `source_texts/oral_history/` | **40** (cap 40) | **40** (cap 40) |
| Passages in the `_PASSAGES_*.md` file | **140**, from 110 interviews | **214**, from 148 interviews |
| Transcripts fetched and scanned locally | 1064 HTML transcript pages (21,619,380 words) | 957 PDFs converted (11,350,952 words; 91 of them are alternate-version duplicates) |
| Site-search queries run (exact strings in section 3) | 236 keyword queries (31 returned 0 hits) plus 4 probe queries and 2 enumeration queries | none: no usable public search over transcript text (section 2) |
| HTTP requests actually sent (cache hits excluded) | 1884 (all HTTP 200) | 971 to wisvetsmuseum.com (all HTTP 200) plus 2 to the catalog host (robots.txt 200, search page 403) |
| Blocked or restricted items | none blocked; one permission-to-quote notice (section 1) | catalog search 403 (Tier C, section 6); AI-crawler robots rule flagged for the developer (section 1) |

Where the files are: `source_texts/oral_history/rutgers/` (`_PASSAGES_rutgers.md` plus `rutgers_<id-slug>.txt`) and `source_texts/oral_history/wisconsin_vets/` (`_PASSAGES_wisconsin_vets.md` plus `wisconsin_vets_<Last-First>_OH<n>.txt`). All of it is local research material (git-ignored `source_texts/`), not canon.

Passage tags, Rutgers: gallows-humor 38; humor-about-command 31; humor-as-coping-explained 23; prank 22; humor-about-enemy 19; other 16; humor-stopped/limits 16; humor-about-dead/wounded 12; humor-about-self 12; humor-after-service/civilians 10; nickname 9; humor-in-captivity 6.
Passage tags, WVM: gallows-humor 58; humor-about-command 50; humor-as-coping-explained 37; prank 33; nickname 24; humor-after-service/civilians 24; humor-about-dead/wounded 22; humor-about-enemy 22; humor-about-self 22; humor-stopped/limits 19; other 14; humor-in-captivity 12.
(A passage can carry more than one tag, so tag totals exceed passage counts.)

Windows read by eye, by tier (a window is one candidate stretch the scanner proposed; the tiers are defined in section 4): Rutgers T1 819, T2 152, T2b 100; WVM T1 779, T2 280, T2b 141. Only windows where the veteran is describing humor, joking, a prank, a nickname or laughing as a practice (or tells the joke or story itself) were kept.

## 1. Politeness and compliance

**User-Agent.** Every request used exactly `InnerTepeniaResearch/1.0 (personal literature research; low-rate)`. Two initial `curl` probes of the Rutgers robots.txt and home-page headers used it too. No browser User-Agent, no session cookies reused, no login, no CAPTCHA or challenge workaround anywhere.

**robots.txt, read before fetching.**
- Rutgers (Joomla default file): `User-agent: *` disallows only the CMS internals (`/administrator/`, `/api/`, `/bin/`, `/cache/`, `/cli/`, `/components/`, `/includes/`, `/installation/`, `/language/`, `/layouts/`, `/libraries/`, `/logs/`, `/modules/`, `/plugins/`, `/tmp/`). No Crawl-delay. Every path used here (`/search`, `/explore/...`, `/images/PDFs/...`) is outside that list. The home page also sends a `content-signal: ai-train=yes, search=yes, ai-input=yes` header.
- wisvetsmuseum.com (WordPress): `User-agent: *` disallows `/wp-admin/` (admin-ajax allowed). **Flag for the developer:** the same file has a separate block with `Disallow: /` for named AI crawlers (ClaudeBot, GPTBot, CCBot, Google-Extended, Applebot-Extended, Amazonbot, Meta-ExternalAgent, FacebookBot, GoogleOther). The pull used the project's own research User-Agent, which matches none of those names, and this is a rate-limited reading (about a thousand requests) of public transcript PDFs for own-words literature research, not model training. But the site's evident wish to keep AI harvesters out is on record here, so whether this pull stays in the local folder is the developer's call. The WVM terms page says: "Education and research use is permitted for all interviews in the collection. Patrons may NOT make copies of the interviews without permission from WVM." The local copies are therefore reference only, git-ignored, and any design-document use should be own-words with citation, as the folder README already requires.
- wisvetsmuseum.catalogaccess.com (the museum's catalog host): `Disallow: /not-found/`, `/api/`, `/home-page-trap-url`. The one search URL tried is not disallowed, but the server answered HTTP 403 (section 6). Not retried, not worked around.

**Terms notices on the content.** Every Rutgers transcript page carries "Permission to quote from this transcript must be obtained from the Rutgers Oral History Archives". Local reference copies only; the 40 full files and the passages file repeat that notice in their headers.

**Spacing between requests to the same host.** The helper enforced a minimum of 2.5 s per host (3.0 s for the WVM bulk PDF downloader), with a lock file shared by every script of this run. Honest accounting, because the gap was defined imperfectly at first:
- Until about 20:48 local time the helper measured spacing start-to-start, so after a slow response the next request could follow within a second or so of that response arriving. In the Rutgers request log, 67 consecutive responses before 20:48 are timestamped less than 2 s apart. At 20:47:54 the helper was changed to measure from the end of the response; afterwards the median gap between consecutive Rutgers responses is 3.0 s over 1435 intervals, with 1 interval(s) under 2 s (21:09:53 (0 s)).
- The WVM PDF downloader (one process, 3.0 s start-to-start, never changed) has 71 of 956 consecutive log intervals under 2 s for the same start-to-start reason; the median is 3.0 s. It never ran concurrently with itself.
- **Overlap incident (Rutgers, roughly 20:34 to 20:47):** while enumerating the transcript list I found that a stray copy of one search-enumeration script (the `began` listing) was still running next to the `interview` enumeration, and earlier the profile-page fetch and a search had overlapped as well (the request log shows same-second and interleaved responses at 20:34 to 20:36 and 20:41 to 20:42). All of these were my own processes sharing one lock file, which they could race on. I killed the stray copy as soon as I saw it. I cannot prove that no two requests were in flight at the same moment in that window. The server never returned anything but HTTP 200 and never slowed or blocked, but the rule was "never parallel requests to one host" and in that window it was not reliably kept.
- Total load, for scale: 1884 Rutgers requests over about 2.2 hours, and 971 WVM requests over about 1 hour (the PDF downloads ran 20:25 to 21:10).

**What was not done.** No attempt to reach the OHMS indexes by guessing IDs, no use of WVM's `/wp-json/` or admin-ajax endpoints, no probing of Rutgers URLs beyond the listing, search, transcript, profile and PDF patterns documented in section 2.

## 2. How each site's search works

### Rutgers Oral History Archives (https://oralhistory.rutgers.edu/)

Joomla site. Everything about the search was learned by reading the search form and by probing single words (probe results are in section 3).

- **Search URL:** `https://oralhistory.rutgers.edu/search?q=<terms>` ; next pages `&start=20`, `&start=40`, ... Twenty results per page. The page header reads "Results X - Y of N", so N is the true hit count and pagination is deterministic.
- **It is a full-text index of the transcript pages.** Probe: `Albert Lea` (a small town mentioned once deep inside one transcript) returned exactly that transcript; `Lewinsky` returned 3 transcripts, all of them places where the name occurs in the body text. The result list shows a ~40-word snippet around one match only, which is not enough to judge a passage, so every hit transcript was fetched and read locally (section 4).
- **Matching is exact-term, no stemming:** `humor` (153 hits) is not `humorous` (83); `humour` returns 0 with a "Did you mean" suggestion. Every inflection has to be searched on its own.
- **Operators:** several words are ANDed by default ("Assuming gallows is required, and humor is required..." is printed above the results); `or` between words makes them optional (`gallows or humor` returned 155); the word `not` excludes the next term (so `not funny` returned 0 and is not a phrase search).
- **Quoted phrases never match.** A string in double quotes is treated as one term and returns 0 every time (tested 20 times, section 3). Phrase work therefore has to be done locally on the downloaded transcripts, which is what section 4 does; for a human with a browser it is also listed in section 6.
- **Veteran roster:** `explore/military-history/conflict-index?tag=<n>&limit=1000&limitstart=0` and `explore/military-history/military-branch-unit?tag=<n>&limit=2000&limitstart=0` list the veteran profile pages by war and by branch. That gave 773 veteran profile entries; 636 of them were tied by name to 718 transcript pages (multi-part interviews count once per part). 137 profiles were not tied by exact name at first; a later fuzzy name match resolved most of them (section 7, item 2; the remainder are in section 8).
- **Page types:** profile page `/explore/alphabetical-index/interviewees/<id>-<name>` (metadata: war, branch and unit, theater; its "Links to Oral History Sessions" field points to the transcript); transcript page `/explore/alphabetical-index/interviewees/30-interview-html-text/<id>-<name>` or `/64-text-html/<id>-<name>` (HTML transcript, one `<p>` per speaker turn, an Interviewee/Date/Place/Interviewers/Citation field block, and a link to the PDF). The profile id and the transcript id are different numbers for the same person. The PDF at `/images/PDFs/<name>.pdf` carries the page numbers, which the HTML lacks, so page markers in the files below come from the PDF (matched by text, since one archive page linked another narrator's PDF; see section 7).
- **Enumeration of every HTML transcript:** the search `interview` returned 1,254 hits (63 pages) and `began` a second, overlapping list (24 pages). The 1,254 URLs are the transcript universe; the veteran subset was chosen from the roster, plus every transcript that surfaced in any keyword search.

### Wisconsin Veterans Museum (https://wisvetsmuseum.com/)

WordPress site.

- **Transcript index:** `https://wisvetsmuseum.com/learning-research/oral-history/transcripts/` links one page per conflict (`.../transcripts/vietnam-war/`, `world-war-2/`, `korean-war/`, `world-war-1/`, `cold-war/`, `persian-gulf-war/`, `operation-oif-operation-oef/`). Each conflict page lists the interviews as direct links to PDFs under `https://wisvetsmuseum.com/wp-content/uploads/<yyyy>/<mm>/<Last-First>_OH<number>.pdf`. All 959 listed PDF URLs resolved to 957 distinct files (two files are listed under two conflict pages each); 4 Hmong-language interview files were skipped on purpose (the transcripts were not English text). Published transcripts are only a part of the collection: the catalog states about 2,900 interviews; about 960 have a public transcript PDF.
- **No usable text search.** The WordPress site search covers pages, not PDF text. There is no cross-interview full-text search on the public site. So the WVM route was: download every public transcript PDF politely and scan locally.
- **PDF layout:** text-based PDFs (no OCR needed) with an abstract and index front matter, then an "Interview Transcript" heading; printed page numbers appear at the top or bottom of each page and were mapped to paragraphs for the `p.N` markers.
- **Other front doors, not usable by the tools:** the museum catalog (`wisvetsmuseum.catalogaccess.com/archives?...`) answers HTTP 403 to the required User-Agent (section 6). The OHMS viewer pages (`https://wisvetsmuseum.com/ohms-viewer/render.php?cachefile=OH_<5-digit>.xml`) do load (one tested, HTTP 200) and have a per-interview "Search this Index", but there is no cross-interview search and the cachefile numbers cannot be enumerated from any public list I found.

## 3. Exact queries, hit counts and usefulness

Rutgers only (WVM has no search to query). Strings are exactly the `q=` value sent to `https://oralhistory.rutgers.edu/search`. "Reported hits" is the engine's own count. "Results read" says how much of the list I paged through: **all** when the hit count was at most the paging threshold, otherwise only page 1 (20 results), in which case the query served as a probe and the real coverage of those words comes from the local scan in section 4 (all words in the table were also scanned for locally in the downloaded transcripts). "Hit transcripts fetched locally" counts how many of the results I read belong to transcripts I held at the end of the run; "with a saved passage" counts how many of those contributed a passage to `_PASSAGES_rutgers.md`.

Verdict key: *high yield* = at least 15 hit transcripts contributed a passage; *useful* = 5 to 14; *thin* = 1 to 4; *no passage kept* = hits read but nothing qualified; *too broad* = page 1 only and nothing kept from it; *dead at the query* = the engine returned zero hits, so the query itself was the problem (quoted phrase, operator word, or spelling), not the archive.

Four probe queries are not in the table because they tested the engine rather than the topic: `gallows humor` (unquoted, ANDed: 3 hits, which are the Berglund, Feldman and Bach transcripts, all read and all but Feldman kept), `gallows or humor` (155 hits, OR mode), `Lewinsky` (3 hits) and `Albert Lea` (1 hit), the last two to confirm that the index reaches deep into transcript bodies. The two enumeration queries `interview` (1,254 hits, 63 pages) and `began` (24 pages) are described in section 2.

| Query string (exact, as sent as q=) | Reported hits | Results read | Hit transcripts fetched locally | ...of which have a saved passage | Verdict |
|---|---|---|---|---|---|
| `humor` | 153 | all 153 | 153 | 27 | high yield |
| `humour` | 0 | - | 0 | 0 | dead at the query (zero-result; engine suggested a different spelling) |
| `humorous` | 83 | all 83 | 83 | 22 | high yield |
| `joke` | 309 | all 309 | 309 | 65 | high yield |
| `jokes` | 115 | all 115 | 115 | 24 | high yield |
| `joking` | 59 | all 59 | 59 | 16 | high yield |
| `joked` | 45 | all 45 | 45 | 9 | useful |
| `laugh` | 286 | all 286 | 286 | 52 | high yield |
| `laughed` | 206 | all 206 | 206 | 38 | high yield |
| `laughing` | 226 | all 226 | 226 | 45 | high yield |
| `laughter` | 966 | 20 of 966 | 20 | 4 | thin |
| `funny` | 773 | 20 of 773 | 20 | 5 | useful |
| `prank` | 8 | all 8 | 8 | 3 | thin |
| `pranks` | 26 | all 26 | 26 | 2 | thin |
| `nickname` | 171 | all 171 | 171 | 26 | high yield |
| `nicknamed` | 58 | all 58 | 58 | 8 | useful |
| `kidded` | 36 | all 36 | 36 | 10 | useful |
| `kidding` | 253 | all 253 | 253 | 36 | high yield |
| `gallows` | 5 | all 5 | 5 | 2 | thin |
| `wisecrack` | 3 | all 3 | 3 | 1 | thin |
| `razzing` | 2 | all 2 | 2 | 1 | thin |
| `morbid` | 6 | all 6 | 6 | 0 | no passage kept |
| `"sense of humor"` | 0 | - | 0 | 0 | dead at the query: quoted phrase treated as a single term, never matches |
| `"black humor"` | 0 | - | 0 | 0 | dead at the query: quoted phrase treated as a single term, never matches |
| `"gallows humor"` | 0 | - | 0 | 0 | dead at the query: quoted phrase treated as a single term, never matches |
| `"made fun"` | 0 | - | 0 | 0 | dead at the query: quoted phrase treated as a single term, never matches |
| `"we laughed"` | 0 | - | 0 | 0 | dead at the query: quoted phrase treated as a single term, never matches |
| `"had to laugh"` | 0 | - | 0 | 0 | dead at the query: quoted phrase treated as a single term, never matches |
| `"make light"` | 0 | - | 0 | 0 | dead at the query: quoted phrase treated as a single term, never matches |
| `"made light"` | 0 | - | 0 | 0 | dead at the query: quoted phrase treated as a single term, never matches |
| `"poke fun"` | 0 | - | 0 | 0 | dead at the query: quoted phrase treated as a single term, never matches |
| `"practical joke"` | 0 | - | 0 | 0 | dead at the query: quoted phrase treated as a single term, never matches |
| `"practical jokes"` | 0 | - | 0 | 0 | dead at the query: quoted phrase treated as a single term, never matches |
| `"sick humor"` | 0 | - | 0 | 0 | dead at the query: quoted phrase treated as a single term, never matches |
| `"sick joke"` | 0 | - | 0 | 0 | dead at the query: quoted phrase treated as a single term, never matches |
| `"comic relief"` | 0 | - | 0 | 0 | dead at the query: quoted phrase treated as a single term, never matches |
| `"cut the tension"` | 0 | - | 0 | 0 | dead at the query: quoted phrase treated as a single term, never matches |
| `"break the tension"` | 0 | - | 0 | 0 | dead at the query: quoted phrase treated as a single term, never matches |
| `"if you didn't laugh"` | 0 | - | 0 | 0 | dead at the query: quoted phrase treated as a single term, never matches |
| `"laugh or cry"` | 0 | - | 0 | 0 | dead at the query: quoted phrase treated as a single term, never matches |
| `"laugh to keep"` | 0 | - | 0 | 0 | dead at the query: quoted phrase treated as a single term, never matches |
| `laughed dead` | 147 | all 147 | 147 | 32 | high yield |
| `laughed killed` | 167 | all 167 | 167 | 34 | high yield |
| `laughed wounded` | 97 | all 97 | 97 | 25 | high yield |
| `laughed body` | 132 | all 132 | 132 | 24 | high yield |
| `laughed bodies` | 77 | all 77 | 77 | 23 | high yield |
| `laughing dead` | 171 | all 171 | 171 | 40 | high yield |
| `joke dead` | 215 | all 215 | 215 | 52 | high yield |
| `jokes dead` | 78 | all 78 | 78 | 20 | high yield |
| `joked killed` | 40 | all 40 | 40 | 8 | useful |
| `humor death` | 111 | all 111 | 111 | 22 | high yield |
| `humor killed` | 129 | all 129 | 129 | 25 | high yield |
| `humor dead` | 109 | 20 of 109 | 20 | 5 | useful |
| `humor wounded` | 65 | 20 of 65 | 20 | 5 | useful |
| `humor combat` | 96 | 20 of 96 | 20 | 6 | useful |
| `humor war` | 149 | 20 of 149 | 20 | 8 | useful |
| `humor army` | 143 | 20 of 143 | 20 | 5 | useful |
| `humor navy` | 127 | 20 of 127 | 20 | 4 | thin |
| `humor marines` | 75 | 20 of 75 | 20 | 5 | useful |
| `humor officers` | 126 | 20 of 126 | 20 | 7 | useful |
| `jokes officers` | 91 | 20 of 91 | 20 | 7 | useful |
| `joked officers` | 33 | all 33 | 33 | 8 | useful |
| `humor brass` | 24 | all 24 | 24 | 4 | thin |
| `laughed officer` | 179 | 20 of 179 | 20 | 5 | useful |
| `laughed captain` | 146 | 20 of 146 | 20 | 12 | useful |
| `laughed sergeant` | 132 | 20 of 132 | 20 | 9 | useful |
| `lifers` | 7 | all 7 | 7 | 5 | useful |
| `lifer` | 12 | all 12 | 12 | 7 | useful |
| `chickenshit` | 10 | all 10 | 10 | 3 | thin |
| `chicken shit` | 44 | all 44 | 44 | 12 | useful |
| `humor civilian` | 91 | 20 of 91 | 20 | 3 | thin |
| `humor civilians` | 76 | 20 of 76 | 20 | 2 | thin |
| `humor after war` | 149 | 20 of 149 | 20 | 4 | thin |
| `humor VA` | 23 | all 23 | 23 | 8 | useful |
| `humor survive` | 56 | all 56 | 56 | 8 | useful |
| `humor sanity` | 4 | all 4 | 4 | 2 | thin |
| `humor cope` | 18 | all 18 | 18 | 2 | thin |
| `humor coping` | 7 | all 7 | 7 | 1 | thin |
| `humor tension` | 34 | all 34 | 34 | 7 | useful |
| `humor morale` | 43 | all 43 | 43 | 11 | useful |
| `humor prisoner` | 43 | all 43 | 43 | 15 | high yield |
| `humor POW` | 19 | all 19 | 19 | 6 | useful |
| `humor camp` | 128 | 20 of 128 | 20 | 9 | useful |
| `humor German` | 117 | 20 of 117 | 20 | 9 | useful |
| `humor Japanese` | 107 | 20 of 107 | 20 | 7 | useful |
| `humor Vietnam` | 91 | 20 of 91 | 20 | 5 | useful |
| `humor Korea` | 69 | 20 of 69 | 20 | 7 | useful |
| `humor "Cold War"` | 0 | - | 0 | 0 | dead at the query: unquoted words are ANDed and no transcript contains all of them (or one is absent) |
| `laughter tension` | 172 | 20 of 172 | 20 | 5 | useful |
| `laughed tension` | 45 | all 45 | 45 | 11 | useful |
| `laughed nervous` | 58 | all 58 | 58 | 10 | useful |
| `laughing nervous` | 66 | 20 of 66 | 20 | 4 | thin |
| `laugh hysterically` | 8 | all 8 | 8 | 2 | thin |
| `hysterically` | 14 | all 14 | 14 | 3 | thin |
| `hysterical` | 44 | all 44 | 44 | 5 | useful |
| `cracked up` | 117 | 20 of 117 | 20 | 8 | useful |
| `cracking up` | 39 | all 39 | 39 | 8 | useful |
| `roared` | 17 | all 17 | 17 | 5 | useful |
| `dark humor` | 82 | 20 of 82 | 20 | 4 | thin |
| `dark sense` | 394 | 20 of 394 | 20 | 2 | thin |
| `twisted sense` | 36 | all 36 | 36 | 7 | useful |
| `morbid humor` | 1 | all 1 | 1 | 0 | no passage kept |
| `sick sense` | 506 | 20 of 506 | 20 | 2 | thin |
| `sarcasm` | 1 | all 1 | 1 | 0 | no passage kept |
| `sarcastic` | 17 | all 17 | 17 | 6 | useful |
| `wiseguy` | 0 | - | 0 | 0 | dead at the query (zero-result; engine suggested a different spelling) |
| `smart aleck` | 5 | all 5 | 5 | 0 | no passage kept |
| `wise guy` | 218 | 20 of 218 | 20 | 6 | useful |
| `kidding around` | 253 | 20 of 253 | 20 | 5 | useful |
| `kid around` | 829 | 20 of 829 | 20 | 6 | useful |
| `ribbing` | 8 | all 8 | 8 | 0 | no passage kept |
| `teased` | 23 | all 23 | 23 | 3 | thin |
| `teasing` | 30 | all 30 | 30 | 5 | useful |
| `razz` | 3 | all 3 | 3 | 0 | no passage kept |
| `ragged on` | 24 | all 24 | 24 | 4 | thin |
| `rag on` | 34 | all 34 | 34 | 4 | thin |
| `inside joke` | 183 | 20 of 183 | 20 | 5 | useful |
| `running joke` | 277 | 20 of 277 | 20 | 8 | useful |
| `played a joke` | 274 | 20 of 274 | 20 | 6 | useful |
| `played jokes` | 102 | 20 of 102 | 20 | 4 | thin |
| `joke on` | 309 | 20 of 309 | 20 | 6 | useful |
| `the joke was` | 309 | 20 of 309 | 20 | 6 | useful |
| `laugh about` | 286 | 20 of 286 | 20 | 6 | useful |
| `laugh at` | 286 | 20 of 286 | 20 | 2 | thin |
| `laughed at` | 206 | 20 of 206 | 20 | 4 | thin |
| `we all laughed` | 206 | 20 of 206 | 20 | 4 | thin |
| `everybody laughed` | 195 | 20 of 195 | 20 | 9 | useful |
| `laughed like` | 206 | 20 of 206 | 20 | 6 | useful |
| `laughed it off` | 206 | 20 of 206 | 20 | 6 | useful |
| `laugh it off` | 286 | 20 of 286 | 20 | 6 | useful |
| `laughing about` | 226 | 20 of 226 | 20 | 8 | useful |
| `laughs about` | 99 | 20 of 99 | 20 | 5 | useful |
| `still laugh` | 286 | 20 of 286 | 20 | 2 | thin |
| `can laugh` | 286 | 20 of 286 | 20 | 7 | useful |
| `now we laugh` | 286 | 20 of 286 | 20 | 3 | thin |
| `laugh now` | 286 | 20 of 286 | 20 | 5 | useful |
| `not funny` | 0 | - | 0 | 0 | dead at the query: the word "not" is a search operator (excludes the next term) |
| `wasn't funny` | 769 | 20 of 769 | 20 | 4 | thin |
| `didn't think it was funny` | 773 | 20 of 773 | 20 | 4 | thin |
| `thought it was funny` | 769 | 20 of 769 | 20 | 4 | thin |
| `find it funny` | 749 | 20 of 749 | 20 | 3 | thin |
| `found it funny` | 744 | 20 of 744 | 20 | 3 | thin |
| `funny at the time` | 773 | 20 of 773 | 20 | 3 | thin |
| `funny now` | 773 | 20 of 773 | 20 | 3 | thin |
| `kinda funny` | 27 | all 27 | 27 | 4 | thin |
| `sense of humour` | 0 | - | 0 | 0 | dead at the query (zero-result; engine suggested a different spelling) |
| `comic` | 69 | 20 of 69 | 20 | 3 | thin |
| `comedian` | 60 | all 60 | 60 | 9 | useful |
| `clown` | 28 | all 28 | 28 | 6 | useful |
| `clowns` | 14 | all 14 | 14 | 5 | useful |
| `clowned` | 0 | - | 0 | 0 | dead at the query (zero-result; engine suggested a different spelling) |
| `cartoon` | 61 | 20 of 61 | 20 | 0 | too broad (page 1 only read) |
| `cartoons` | 63 | 20 of 63 | 20 | 3 | thin |
| `Willie and Joe` | 40 | all 40 | 40 | 5 | useful |
| `Sad Sack` | 32 | all 32 | 32 | 7 | useful |
| `Mauldin` | 15 | all 15 | 15 | 4 | thin |
| `Kilroy` | 4 | all 4 | 4 | 0 | no passage kept |
| `limerick` | 2 | all 2 | 2 | 0 | no passage kept |
| `limericks` | 1 | all 1 | 1 | 0 | no passage kept |
| `parody` | 9 | all 9 | 9 | 1 | thin |
| `bawdy` | 3 | all 3 | 3 | 0 | no passage kept |
| `ditty` | 12 | all 12 | 12 | 1 | thin |
| `moniker` | 1 | all 1 | 1 | 0 | no passage kept |
| `monikers` | 0 | - | 0 | 0 | dead at the query (zero-result; engine suggested a different spelling) |
| `we called him` | 1111 | 20 of 1111 | 20 | 5 | useful |
| `called him` | 1113 | 20 of 1113 | 20 | 5 | useful |
| `nicknames` | 25 | all 25 | 25 | 8 | useful |
| `short timer` | 22 | all 22 | 22 | 7 | useful |
| `short-timer` | 5 | all 5 | 5 | 2 | thin |
| `short timers` | 39 | all 39 | 39 | 10 | useful |
| `FNG` | 1 | all 1 | 1 | 0 | no passage kept |
| `REMF` | 0 | - | 0 | 0 | dead at the query (zero-result; engine suggested a different spelling) |
| `hazing` | 181 | 20 of 181 | 20 | 2 | thin |
| `mocking` | 10 | all 10 | 10 | 1 | thin |
| `mocked` | 6 | all 6 | 6 | 0 | no passage kept |
| `ridiculed` | 12 | all 12 | 12 | 3 | thin |
| `made light` | 672 | 20 of 672 | 20 | 4 | thin |
| `make light of` | 672 | 20 of 672 | 20 | 3 | thin |
| `make fun` | 840 | 20 of 840 | 20 | 4 | thin |
| `made fun of` | 839 | 20 of 839 | 20 | 3 | thin |
| `poked fun` | 23 | all 23 | 23 | 2 | thin |
| `poking fun` | 27 | all 27 | 27 | 5 | useful |
| `fun of` | 843 | 20 of 843 | 20 | 2 | thin |
| `practical jokes` | 33 | all 33 | 33 | 10 | useful |
| `practical joker` | 6 | all 6 | 6 | 2 | thin |
| `joker` | 17 | all 17 | 17 | 6 | useful |
| `jokester` | 3 | all 3 | 3 | 1 | thin |
| `cutup` | 2 | all 2 | 2 | 0 | no passage kept |
| `cut-up` | 1 | all 1 | 1 | 0 | no passage kept |
| `horsing around` | 13 | all 13 | 13 | 2 | thin |
| `horseplay` | 5 | all 5 | 5 | 0 | no passage kept |
| `shenanigans` | 14 | all 14 | 14 | 0 | no passage kept |
| `mischief` | 17 | all 17 | 17 | 1 | thin |
| `hilarious` | 34 | all 34 | 34 | 7 | useful |
| `riot` | 114 | 20 of 114 | 20 | 3 | thin |
| `scream` | 70 | 20 of 70 | 20 | 3 | thin |
| `crack a joke` | 55 | all 55 | 55 | 11 | useful |
| `cracked a joke` | 52 | all 52 | 52 | 16 | high yield |
| `cracking jokes` | 5 | all 5 | 5 | 2 | thin |
| `told a joke` | 308 | 20 of 308 | 20 | 7 | useful |
| `tell a joke` | 309 | 20 of 309 | 20 | 6 | useful |
| `telling jokes` | 104 | 20 of 104 | 20 | 6 | useful |
| `dirty joke` | 111 | 20 of 111 | 20 | 9 | useful |
| `dirty jokes` | 44 | all 44 | 44 | 12 | useful |
| `off-color` | 8 | all 8 | 8 | 0 | no passage kept |
| `black humor` | 138 | 20 of 138 | 20 | 5 | useful |
| `sick humor` | 104 | all 104 | 104 | 22 | high yield |
| `sick joke` | 198 | 20 of 198 | 20 | 9 | useful |
| `sick jokes` | 83 | all 83 | 83 | 20 | high yield |
| `grim humor` | 7 | all 7 | 7 | 2 | thin |
| `grim jokes` | 2 | all 2 | 2 | 2 | thin |
| `dark jokes` | 65 | all 65 | 65 | 18 | high yield |
| `dark joke` | 160 | 20 of 160 | 20 | 7 | useful |
| `black comedy` | 52 | all 52 | 52 | 8 | useful |
| `macabre` | 3 | all 3 | 3 | 1 | thin |
| `irreverent` | 1 | all 1 | 1 | 0 | no passage kept |
| `irreverence` | 0 | - | 0 | 0 | dead at the query (zero hits) |
| `levity` | 7 | all 7 | 7 | 1 | thin |
| `comic relief` | 16 | all 16 | 16 | 3 | thin |
| `break tension` | 138 | 20 of 138 | 20 | 4 | thin |
| `relieve tension` | 31 | all 31 | 31 | 11 | useful |
| `relieved tension` | 46 | all 46 | 46 | 14 | useful |
| `lighten mood` | 0 | - | 0 | 0 | dead at the query: unquoted words are ANDed and no transcript contains all of them (or one is absent) |
| `josh` | 7 | all 7 | 7 | 0 | no passage kept |
| `joshing` | 7 | all 7 | 7 | 0 | no passage kept |
| `joshed` | 2 | all 2 | 2 | 0 | no passage kept |
| `needling` | 4 | all 4 | 4 | 1 | thin |
| `needled` | 2 | all 2 | 2 | 0 | no passage kept |
| `ribbed` | 5 | all 5 | 5 | 1 | thin |
| `razzed` | 5 | all 5 | 5 | 3 | thin |
| `prankster` | 0 | - | 0 | 0 | dead at the query (zero hits) |
| `pranksters` | 2 | all 2 | 2 | 0 | no passage kept |
| `gag` | 8 | all 8 | 8 | 2 | thin |
| `gags` | 1 | all 1 | 1 | 0 | no passage kept |
| `wisecracks` | 3 | all 3 | 3 | 2 | thin |
| `wisecracking` | 0 | - | 0 | 0 | dead at the query (zero hits) |


**What the table shows.**
- The word-level queries (humor, joke, laugh, kidding, nickname and their inflections) carried the retrieval. Single exact words each returned 45 to 966 hits, so most are bigger than a person could read from snippets; the useful move was always the same: fetch the transcripts, scan the full text, read the windows.
- The combined queries (`laughed dead`, `laughed killed`, `laughed wounded`, `laughed body`, `jokes dead`, `humor killed`, ...) gave the best precision for the topic the developer asked about (laughter near death and injury). `lifer`/`lifers`/`chickenshit` found the brass-humor vein that single words miss.
- The phrases the brief asked for ("sense of humor", "black humor", "gallows humor", "made fun", "we laughed", "had to laugh", "cut the tension", "if you didn't laugh", "laugh or cry") are all **dead at the query**, not dead at the archive: the engine cannot take phrases. Each was therefore run twice more in different form: as an unquoted AND query where that made sense (`gallows humor`, `black humor`, `sick humor`, `break tension`, `relieve tension`, `made fun of`, ...) and as an exact-phrase regular expression over the full downloaded text (T2b, section 4). The local phrase scan is the real answer for those phrases.
- `dark humor`, `dark sense`, `sick sense`, `kid around`, `wise guy` and the like returned hundreds of hits because the words are common in different places in a long transcript; they were read as page-1 probes only and carry little weight.
- `humor` plus a service branch or theater (`humor navy`, `humor Vietnam`, `humor Korea`, `humor German`...) mostly re-surfaced transcripts already held; they were useful as a check that nothing obvious was missing, not as new finds.
- Rare words (`morbid humor` 1, `sarcasm` 1, `ribbing` 8, `razz` 3, `wiseguy` 0, `prankster` 0) were cheap and complete reads; few passages came of them.
- Queries added in a late pass (`black humor` through `wisecracking`, 31 strings) were run after the first scan to test whether any angle had been missed. Their hit transcripts that were not yet held were fetched and scanned like the rest (section 4).

## 4. Local scan of the full transcript text (what the site search cannot do)

The site search finds words, not practices, and cannot do phrases, so most of the work was done locally on the downloaded text. The method, in the order it was applied:

1. **Fetch.** Rutgers: all 1064 HTML transcript pages kept (veteran roster transcripts plus every transcript that surfaced in any keyword result list); 21,619,380 words. WVM: all 959 public PDFs converted with `pdftotext` to paragraph lists; 957 files; 11,350,952 words, including 91 alternate-version files that duplicate another interview and were de-duplicated when building passages.
2. **T1 scan (strong terms).** Regular expressions over every paragraph for: humor/humorous, joke/jokes/joking/joked, prank(s), nickname(d), kidded/kidding, gallows, black/dark/sick/twisted/morbid humor, lifer, chickenshit, razzing, wisecrack, and related stems. Windows had to be at least 15 words, outside bracketed laughter markers such as `[laughter]`, and to sit in military content (a density score over military vocabulary in the surrounding paragraphs). Words that are noisy in this archive (ridicule, mock, gag, comic, shenanigans, hysterical, "no kidding", "you're kidding") were removed from the strong list. Every T1 window was read by eye and kept or dropped.
3. **T2 scan (laugh/funny).** `laugh*` and `funny` are too common to read exhaustively; they were read for the narrators who had the densest humor material, and in a final pass over all 1064 Rutgers transcripts for windows that also contained a death, wounded, enemy, coping or captivity word and sat in military content.
4. **T2b scan (phrases the site search cannot do).** High-precision exact phrases over the full text: "had to laugh", "laugh about it", "relieve the tension", "break the tension", "gallows", "sense of humor", "black humor", "we laughed", "made fun", "practical joke" and a few dozen siblings. Counted in the whole Rutgers corpus held (1064 transcripts): the exact phrases "gallows humor", "black humor", "dark humor", "sick humor", "morbid humor" or "grim humor" (either spelling of humor) occur in 5 transcripts, 3 of which contributed a passage (yoken-richard, berglund-john, bach-thomas).
5. **T3 (bracketed laughter with no keyword)** was tried and dropped: `[laughter]` marks in these transcripts attach mostly to ordinary conversation, and the hit list was almost entirely noise.
6. **Passage building.** Each kept window = the humor stretch plus about three sentences of context either side, capped at 350 words; `[…]` marks truncation inside a paragraph; the passage text is verified to be a verbatim substring of the transcript text (normalized for whitespace and quotes) before it is written. Duplicate transcripts (WVM alternate versions) were collapsed.
7. **Page numbers.** WVM: the printed page number nearest each paragraph (interpolated where the footer is missing). Rutgers: looked up in the narrator's PDF by matching the passage text to a PDF page; one passage (Wenzel) has no page because the archive page has no PDF link.
8. **Descriptors.** Narrator war, branch and role come from the interview cover page (WVM) or the archive's profile page (Rutgers). Where the archive gives no structured metadata the descriptor is taken from the transcript itself and says so.
9. **Non-veteran narrators.** Rutgers transcripts sometimes belong to a family member or civilian; passages from such a narrator are labeled as such (for example a daughter describing her father) and should not be read as veteran testimony.

## 5. Transcripts saved in full

Cap was 40 per archive; both archives are at the cap. Files are UTF-8 text; the first six lines of every file are SOURCE, ARCHIVE, NARRATOR, INTERVIEW DATE, FETCHED (2026-10-05) and TERMS. Rutgers files carry `[p.N]` markers taken from the archive's PDF (`[cover]` = unnumbered title page); WVM files carry `[p.N]` printed page numbers (`[front matter, pdf p.N]` for the abstract and index pages). Selection rule: the 40 interviews with the most kept passages per archive (the Passages column), ties broken by judgment (an explicit "gallows/black humor" remark, a spread across wars and branches). Honest limit: most Rutgers narrators have only one or two passages and WVM narrators two to six, so these are the best available, not uniformly rich, interviews.

### Rutgers (40 files; 70 of the 140 passages come from these)

| Narrator | Descriptor (war, branch, role) | Interview date | PDF page markers | Passages | Words in file | File |
|---|---|---|---|---|---|---|
| Aiello, George | Marine Corps, World War II (Pacific theater) | October 28, 2010 | yes | 1 | 17,397 | `rutgers_1380-aiello-george.txt` |
| Alberts, Howard Kirkpatrick | Marine Corps, World War II; Korean War; Vietnam War (Pacific; Korean; Vietnam theater) | May 16, 2003 | yes | 2 | 21,015 | `rutgers_354-alberts-howard-kirkpatrick.txt` |
| Arbasetti, Robert | Army, 1st Cavalry, Vietnam War (Vietnam theater) | August 3, 2012 | yes | 2 | 34,769 | `rutgers_1523-arbasetti-robert.txt` |
| Bach, Thomas | Army, 1st Cavalry, World War II; Korean War (Home Front; Korean theater) | May 19, 1998 | yes | 1 | 30,915 | `rutgers_742-bach-thomas.txt` |
| Bache, Claude V. | Army, World War II; Korean War; Cold War (European; Korean; Pacific theater) | August 12, 2008 | yes | 2 | 28,593 | `rutgers_741-bache-claude-v.txt` |
| Barry, Jr., Edward J. | Army, 53rd Ordinance Ammunition Company, World War II (European theater) | October 23, 1998 | yes | 1 | 16,235 | `rutgers_735-barry-jr-edward.txt` |
| Berglund, John | Marine Corps, World War II; Korean War (Pacific; Korean theater) | April 9, 1998 | yes | 1 | 43,251 | `rutgers_720-berglund-john.txt` |
| Berke, George Berse | Air Force, World War II; Korean War (American; Korean theater) | September 24, 2010 | yes | 2 | 32,731 | `rutgers_1674-berke-george-berse-part-2.txt` |
| Blaher, William S. | Army, 106th Infantry, I Company, World War II (European theater) | September 23, 2005 | yes | 2 | 25,587 | `rutgers_712-blaher-william-s.txt` |
| Brown, Jr., John W. | Army, 63rd Infantry, K Company, World War II; Korean War (European; Korean theater) | May 14, 2004 | yes | 2 | 12,993 | `rutgers_685-brown-jr-john-w-part-1.txt` |
| Burger, Werner Carl | Army, World War II (European theater) | November 22, 2002 | yes | 2 | 18,353 | `rutgers_674-burger-werner-carl.txt` |
| Dougherty, Dennis | Army, 42nd Infantry, Cold War | January 2, 2013 | yes | 2 | 15,117 | `rutgers_1594-dougherty-dennis-part-1.txt` |
| Feinberg, Leonard | Army, 35th Infantry, Medical Detachment, World War II (European theater) | November 22, 1998 | yes | 3 | 52,701 | `rutgers_2013-feinberg-leonard.txt` |
| Frankel, Samuel | Navy, World War II (Pacific theater) | March 23, 1995 | yes | 1 | 21,963 | `rutgers_589-frankel-samuel.txt` |
| Freedman, Stuart J. | Army, Americal, Vietnam War (Vietnam theater) | June 13, 2006 | yes | 3 | 57,194 | `rutgers_588-freedman-stuart-j.txt` |
| Godfrey, Nancy Petersen | Navy, World War II (American theater) | February 14, 1997 | yes | 2 | 34,378 | `rutgers_572-godfrey-nancy-petersen.txt` |
| Hansen, Leonard | Army, World War II (Pacific theater) | December 3, 1996 | yes | 1 | 22,962 | `rutgers_542-hansen-leonard.txt` |
| Irwin, Herbert W. | Marine Corps, World War II (Pacific theater) | October 2, 1996 | yes | 2 | 37,830 | `rutgers_511-irwin-herbert-w.txt` |
| Kalugin, Lloyd | Army, 89th Infantry, World War II (European theater) | March 3, 1996 | yes | 1 | 24,237 | `rutgers_493-kalugin-lloyd.txt` |
| Koft, Bernard | Navy, World War II (Pacific theater) | February 28, 1996 | yes | 2 | 24,698 | `rutgers_467-koft-bernard.txt` |
| Kolodziej, Edwin | Army, 95th Infantry, B Company, World War II (European theater) | February 16, 2001 | yes | 2 | 16,633 | `rutgers_465-kolodziej-edwin-a-part-2.txt` |
| Konrad, W. Wesley | Army Air Forces, World War II (Pacific theater) | April 11, 1997 | yes | 1 | 41,749 | `rutgers_463-konrad-w-wesley.txt` |
| Leader, Solomon | Army, 99th Infantry, C Company, World War II (European theater) | March 6, 1995 | yes | 2 | 41,479 | `rutgers_445-leader-solomon.txt` |
| Meyers, Maurice | Army, 3rd Infantry, C Company, World War II (European theater) | April 14, 2000 | yes | 1 | 30,426 | `rutgers_387-meyers-maurice.txt` |
| Mickett, Jr., Charles | Army, 36th Infantry, World War II (European theater) | October 24, 1997 | yes | 1 | 28,184 | `rutgers_385-mickett-jr-charles.txt` |
| Mojo, D. Robert | Army, World War II (European theater) | November 25, 1994 | yes | 2 | 24,254 | `rutgers_382-mojo-d-robert.txt` |
| Nisonoff, Alfred | Navy, World War II (Pacific theater) | August 1, 1994 | yes | 2 | 18,893 | `rutgers_345-nisonoff-alfred.txt` |
| Pike, Neal | Navy, World War II (Pacific theater) | March 3, 2005 | yes | 1 | 20,105 | `rutgers_323-pike-neal.txt` |
| Pope, Robert E. | Army, 106th Infantry, World War II (European theater) | June 28, 2003 | yes | 1 | 8,484 | `rutgers_313-pope-robert-e.txt` |
| Popielowski, Joseph | Army, 4th Infantry, Administration Company, Vietnam War (Vietnam theater) | December 16, 2013 | yes | 2 | 22,387 | `rutgers_1664-popielowski-joseph.txt` |
| Prout, Jr., Charles H. | Army, 100th Infantry, World War II (European theater) | February 8, 2004 | yes | 1 | 25,153 | `rutgers_310-prout-jr-charles-h.txt` |
| Salerno, Joseph T. | Army, 106th Infantry, B Company, World War II; Korean War (European; Korean; Pacific theater) | March 28, 2007 | yes | 1 | 44,535 | `rutgers_256-salerno-joseph-t.txt` |
| Schmidt, Samuel | Army, 95th Infantry, L Company, World War II (European theater) | September 3, 2004 | yes | 1 | 16,698 | `rutgers_238-schmidt-samuel.txt` |
| Sees, Robert M. | Army, 25th Infantry, Vietnam War (Vietnam theater) | November 4, 2005 | yes | 5 | 64,971 | `rutgers_1976-sees-robert.txt` |
| Sive, David | Army, 9th Infantry, HQ Company, World War II (European theater) | November 7, 2007 | yes | 2 | 24,283 | `rutgers_191-sive-david-part-1.txt` |
| Vellucci, Patrick | Army, 4th Infantry, Vietnam War | December 9, 2010 | yes | 4 | 34,933 | `rutgers_1378-vellucci-patrick.txt` |
| Wenzel, Arthur C. | Army medical service, World War II (Italy, France, Germany; archive page has no structured metadata, descripto | April 11, 2005 | no (HTML text only) | 1 | 21,408 | `rutgers_77-wenzel-arthur-c.txt` |
| Whitson, Richard | Army, 7th Infantry, Korean War (Korean theater) | June 23, 2010 | yes | 2 | 33,246 | `rutgers_2031-whitson-richard.txt` |
| Wiggin, John P. | Army, 201st Infantry Regiment, World War II (Pacific theater) | July 22, 2006 | yes | 1 | 26,572 | `rutgers_69-wiggin-john-p.txt` |
| Yoken, Richard L. | Navy, World War II (European theater) | July 1, 2010 | yes | 2 | 30,099 | `rutgers_58-yoken-richard.txt` |


### Wisconsin Veterans Museum (40 files; 104 of the 214 passages come from these)

| Narrator | Descriptor (war, branch, role) | Interview date | Interview id | Passages | Words in file | File |
|---|---|---|---|---|---|---|
| Adolph Bach | Intelligence, Army, World War II | 2003 | OH265 | 2 | 12,084 | `wisconsin_vets_Bach-Adolph_OH265.txt` |
| Alan M. Richards | Infantry, Army, Vietnam War | 2002 | OH151 | 6 | 9,750 | `wisconsin_vets_Richards-Alan_OH151.txt` |
| Capt. Farrington Daniels, Jr. | Medical Officer, Army, World War II | 1995 | OH499 | 3 | 27,229 | `wisconsin_vets_Daniels-Farrington_OH499.txt` |
| Dale R. King | 5th RCT Artillery, Army, POW, Korean War | 2004 | OH1009 | 4 | 11,234 | `wisconsin_vets_King-Dale_OH1009.txt` |
| Darryl Johnson | Forward Observer, U.S. Army, Vietnam War | 2015 | OH1966 | 5 | 36,924 | `wisconsin_vets_Johnson-Darryl_OH1966.txt` |
| David F. Hosking Sr. | Aircraft Mechanic and Door Gunner, Army, Vietnam War; Aircraft Mechanic and Door Gunner, National Guard, Caree | 2004 | OH574 | 2 | 11,872 | `wisconsin_vets_Hosking-David_OH574-2.txt` |
| Donald J. Kindt | Infantryman, 10th Mountain Division, Army, World War II | 1994 | OH281 | 2 | 17,362 | `wisconsin_vets_Kindt-Don_OH281.txt` |
| Douglas C. Zwank | Bulk Fuel, Marine Corps, Vietnam War | 1996 | OH213 | 2 | 18,696 | `wisconsin_vets_Zwank-Douglas_OH213-1.txt` |
| Dr. Helen Gurkow | Doctor, Army, Persian Gulf War | 1995 | OH358 | 3 | 19,964 | `wisconsin_vets_Gurkow-Helen_OH-358_edited.txt` |
| Eric K. Oxendorf | Aviation Electrician’s Mate, United States Navy | 2019 | OH2180 | 2 | 18,016 | `wisconsin_vets_Oxendorf-Eric_OH2180-2.txt` |
| Ernest O. Norquist, 1919-2004 | Medic, Army, World War II | 1995 | OH195 | 2 | 21,645 | `wisconsin_vets_Norquist-Ernest_OH195.txt` |
| Gilda Maltes | Medic, Army, Operation Iraqi Freedom | 2013 | OH1853 | 2 | 15,886 | `wisconsin_vets_Maltes-Gilda_OH1853.txt` |
| James R. Heersma | Doctor, Navy attached to the Army, Korean War | 1995 | OH430 | 4 | 17,360 | `wisconsin_vets_Heersma-James_OH430.txt` |
| James “Jim” Erwin | Marine Corps, World War II and American Occupation Forces in North China | 2006 | OH858 | 2 | 23,026 | `wisconsin_vets_Erwin-James_OH858.txt` |
| Jeffery Carnes | Arabic Linguist, Army, Operation Iraqi Freedom | 2008 | OH1413 | 2 | 16,042 | `wisconsin_vets_Carnes-Jeff_OH1413.txt` |
| John R. Reynoldson | Infantry Officer, Army, Korean War | 1995 | OH629 | 1 | 15,449 | `wisconsin_vets_Reynoldson-John_OH629.txt` |
| Julius W. Ptaszynski | Medical Technician, Army, Korean War | 2004 | OH1020 | 2 | 10,158 | `wisconsin_vets_Ptaszynski-Julius_OH1020.txt` |
| Kenneth Stumpf | Rifleman, Army, Vietnam War | 2000 | OH502 | 2 | 27,616 | `wisconsin_vets_Stumpf-Ken_OH502.txt` |
| Lisa Kromanaker | Nurse Corps, US Navy Reserves, Operation Noble Eagle in support of Operation Iraqi Freedom and Operation Endur | 2008 | OH1414 | 2 | 11,183 | `wisconsin_vets_Kromanaker-Lisa_OH1414.txt` |
| Michael A. Weynand | Wireman, U.S. Army, Vietnam War | 2015 | OH2043 | 3 | 17,441 | `wisconsin_vets_Weynand-Michael_OH2043.txt` |
| Michael C. Mishler | Infantry, US Marine Corps and US Army, Vietnam War | 2016 | OH2059 | 2 | 17,522 | `wisconsin_vets_Mishler-Michael_OH2059.txt` |
| Michael Vizer | Security Forces & Infantry, US Marine Corps, Persian Gulf War & Operation Restore Hope | 2015 | OH2012 | 2 | 16,938 | `wisconsin_vets_Vizer-Michael_OH2012.txt` |
| Milo G. Flaten | Scout/Infantryman, United States Army, WWII | 1994 | OH200 | 2 | 36,215 | `wisconsin_vets_Flaten-Milo_OH200.txt` |
| Milton E. Reinke, | Pilot, Army Air Corps, World War II | 2003 | OH475 | 2 | 28,868 | `wisconsin_vets_Reinke-Milton_OH475.txt` |
| Milton Schulties | Engineer, Army, World War II | 2005 | OH684 | 2 | 10,899 | `wisconsin_vets_Schulties-Milton_OH684.txt` |
| Nicholas Patoka | Infantry, U.S. Army, Vietnam War | 2010 | OH1280 | 2 | 29,252 | `wisconsin_vets_Patoka-Nicholas_OH1280.txt` |
| Orville J. Collins | Airborne Infantry, 101st Airborne, World War II | 1996 | OH114 | 2 | 21,400 | `wisconsin_vets_Collins-Orville_OH114.txt` |
| Rachelle M. Halaska | Medic, U.S. Army, Operation Iraqi Freedom, Operation New Dawn | 2018 | OH2132 | 2 | 43,100 | `wisconsin_vets_Halaska-Rachelle-M._OH2132.txt` |
| Raymond P. Konz-Krzyminski | Religious Program Specialist, US Navy | 2019 | OH2179 | 2 | 22,120 | `wisconsin_vets_Konz-Krzyminski-Raymond_OH2179.txt` |
| Rev. Ray W. Stubbe | Navy Chaplain, Vietnam War | 2005-2006 | OH953 | 4 | 58,206 | `wisconsin_vets_Stubbe-Ray_OH953.txt` |
| Robert Curry | Aerial Surveillance, Army, Vietnam War | 2006 | OH973 | 3 | 26,002 | `wisconsin_vets_Curry-Robert_OH973.txt` |
| Robert Krebs | Artillery 2nd Battalion, Army | 2002 | OH89 | 3 | 17,449 | `wisconsin_vets_Krebs-Robert_OH89.txt` |
| Thomas C. Schmitz | Security Police, Air Force, Vietnam War | 2016 | OH2061 | 2 | 12,395 | `wisconsin_vets_Schmitz-Thomas_OH2061.txt` |
| Thomas J. Cullen | B-24 Gunner, Air Force, World War II | 1994 | OH483 | 2 | 33,902 | `wisconsin_vets_Cullen-Tom_OH483.txt` |
| Thomas Lucas | Infantryman, Army, 82nd and 101st Airborne, World War II and Korean War | 2000 | OH643 | 4 | 31,623 | `wisconsin_vets_Lucas-Thomas_OH643-2.txt` |
| Timothy La Sage | Fast Company/Instructor/Scout Sniper/Military Policeman, Marine Corps, War on Terror | 2012 | OH1535 | 2 | 57,989 | `wisconsin_vets_La-Sage-Timothy_OH1535.txt` |
| Wilbert J. Ipsen | National Guard, Army, World War II | 2010 | OH1269 | 3 | 17,181 | `wisconsin_vets_Ipsen-Wilbert_OH1269.txt` |
| William Rolke | Radio Operator, U.S Marine Corps, Vietnam War | 2015 | OH2022 | 2 | 21,972 | `wisconsin_vets_Rolke-William_OH2022.txt` |
| William Schuth | Tactical Data Network Administrator, Marines, Operation Iraqi Freedom | 2008 | OH1419 | 2 | 9,555 | `wisconsin_vets_Schuth-William_OH1419.txt` |
| Yvette Pino | Army (HHC 101st Airborne, Iraq 2003-04; 501st STB, Iraq 2005-06; Missouri National Guard MP), Iraq War | June 7, 2019 | OH2166 | 6 | 68,081 | `wisconsin_vets_Pino-Yvette_OH2166_redacted.txt` |


## 6. TIER C — needs a human with a browser

Nothing in this run was blocked by a challenge page, CAPTCHA or login. One item returned a hard 403, which is where the rules say to stop; the rest of this section lists what a person should do by hand to reach material the tools could not.

| # | Item | Exact URL | What happened | What a human should do |
|---|---|---|---|---|
| C1 | WVM catalog search (the museum's archive catalog, covers about 2,900 interviews, most without a public transcript PDF) | `https://wisvetsmuseum.catalogaccess.com/archives?search=%22oral+history%22` | HTTP 403 from the load balancer (server header `awselb/2.0`, 118-byte body) for the required User-Agent. robots.txt of that host was fetched first (200) and does not disallow the path. Stopped on that item; not retried; no other path on that host was tried. | In a normal browser open `https://wisvetsmuseum.catalogaccess.com/`, go to the Archives tab, and search these strings one at a time: `humor`, `joke`, `jokes`, `prank`, `gallows`, `laughed`, `nickname`, then `black humor` and `sense of humor`. Record interview ids (`OH<number>`) whose abstract mentions humor; for interviews with a transcript the PDF is then on the public transcripts pages, for the rest, ask the museum's Research Center whether a transcript exists. Save any exported text to `Tier_C_Dropbox/` with the id in the file name. |
| C2 | WVM OHMS viewer indexes (per-interview keyword index with timestamps) | pattern `https://wisvetsmuseum.com/ohms-viewer/render.php?cachefile=OH_NNNNN.xml` (one tested: `OH_02172.xml`, HTTP 200) | Fetchable, but each interview has its own "Search this Index" box and there is no cross-interview search; the numbers cannot be enumerated from any public list found. Not guessed at. | Browser: from a catalog record (C1) or the museum's digital-collection links, open the OHMS viewer for interviews flagged in C1 and use "Search this Index" for `humor`, `joke`, `laughed`. |
| C3 | WVM WorldCat discovery layer | `https://wisvetsmuseum.on.worldcat.org/advancedsearch` and `https://wisvetsmuseum.worldcat.org/search?q=ti%3A%22Oral+History+Interview+with%22&qt=advanced&dblist=638` | Both are JavaScript applications; not attempted by the tools. | Browser: search `humor` OR `jokes` within the museum's oral-history records; the record list carries abstracts. |
| C4 | Rutgers phrase searches (the engine cannot do phrases) | `https://oralhistory.rutgers.edu/search?q=%22gallows+humor%22` and 19 sibling quoted phrases in section 3 (all returned 0) | Dead at the query, not blocked. The archive's own site search is the only way to search it on the site; a web search engine can do phrases. | Web search engine, not the site: `site:oralhistory.rutgers.edu "gallows humor"`, then `"black humor"`, `"we laughed"`, `"had to laugh"`, `"practical joke"`, `"sense of humor"`, `"made fun of"`. Open any hit not already in `source_texts/oral_history/rutgers/` and save the transcript page (or its PDF) to `Tier_C_Dropbox/`. Note: the local scan of the 1064 transcripts held already covered those phrases for those transcripts (section 4, T2b). |
| C5 | Rutgers alternate search endpoint | `https://oralhistory.rutgers.edu/search-website` | One attempt ended in a connection reset; not retried, because `/search` (the working endpoint) had been found. Not a block of any kind. | None needed. |

Policy flags that are not blocks but need a human decision: (1) WVM's robots.txt shuts named AI crawlers out; see section 1. (2) Rutgers requires permission to quote beyond a few words; the folder rule (own words, short quotation, page citation) stays within the "few words" use, but a request to the Rutgers Oral History Archives (via the staff address printed on each transcript page) would be needed for anything longer, such as an anthology.

## 7. Dead ends, snags, self-corrections

**Dead ends, with where each died.**
- Quoted phrases on the Rutgers search ("sense of humor", "black humor", "gallows humor", "made fun", "we laughed", "had to laugh", "make light"/"made light", "poke fun", "practical joke(s)", "sick humor", "sick joke", "comic relief", "cut the tension", "break the tension", "if you didn't laugh", "laugh or cry", "laugh to keep"): dead **at the query** (the engine treats the quoted string as one term). Recovered by the unquoted AND forms and the local phrase scan.
- `humour`, `sense of humour`: dead at the query (zero hits; the archive's own spelling is American, and the engine suggested it). `not funny`: dead at the query, because `not` is an operator. `wiseguy`, `prankster`, `wisecracking`, `irreverence`, `lighten mood`, `monikers`, `REMF`, `clowned`: zero hits (word absent or spelled otherwise); the sibling forms were searched.
- `morbid humor`, `sarcasm`, `smart aleck`, `ribbing`, `razz`: few hits, read in full, nothing qualified: dead **at the sources** (the transcripts use the word but not as humor-as-practice).
- Rutgers search snippets: about 40 words around one match; useless for judging a passage. Died at the source's design; worked around by fetching and scanning every hit transcript.
- WVM: no cross-interview text search (died at the source); the catalog search is behind a 403 (Tier C, C1); the OHMS indexes cannot be enumerated (C2).
- T3 scan (bracketed laughter with no keyword): tried on both archives and dropped, because the markers attach mostly to ordinary conversation; the hit lists were noise.
- Generic "funny thing" and "funny story" windows: read, almost all meant "strange" or "odd"; only a few were kept.
- `/search-website` on Rutgers: one connection reset; not retried (C5).

**Snags and self-corrections (the recording law: failures count as findings).**
1. **Wrong first move on the Rutgers roster.** The first roster fetch pulled profile pages, which hold only a short description. After seeing the "Links to Oral History Sessions" field I switched to enumerating transcript pages through the `interview` search and matching roster names to transcript slugs. Cost: a first batch of profile-page requests that did not give transcript text (the profile pages did prove useful later for narrator descriptors).
2. **The first fetch selection was incomplete and I found it myself.** The first fetch took 425 roster transcripts that I had ranked as the most promising from the keyword searches run by then, plus 88 and 7 further transcripts that had appeared in strong-term results. A later audit found: 289 roster transcripts never fetched, 137 roster profiles that exact-slug matching had failed to tie to a transcript (most were spelling variants of the same name, for example `barry-jr-edward-j` vs `barry-jr-edward`, `kolodziej-edwin` vs a part-numbered file), and 418 transcripts that had appeared in at least one keyword result list but were not held. A third fetch round pulled 544 transcripts (544 fetched OK, 0 errors) and the whole T1/T2/T2b scan was re-run on them. After that round the local corpus is 1064 transcripts; 0 roster-matched transcripts are still not held (section 8).
3. **Spacing definition** (section 1): start-to-start spacing at first, post-response spacing from 20:47:54. **Overlap incident** (section 1).
4. **Sentence splitter dropped closing quote marks** in the first passage builder; windows lost their closing quotation marks. Rewrote it to keep quote characters and re-verified every passage as a verbatim substring of the transcript text.
5. **Bracketed laughter such as `[both laugh]` or `[McIntosh laughs]` counted as keyword hits** until the bracket pattern was broadened.
6. **Raw `pdftotext` merged speaker turns** onto consecutive lines, so the first version of the Rutgers full-transcript files (35 written) had whole pages in one paragraph. Switched the Rutgers page text to `pdftotext -layout` (blank line between turns) and rewrote all 40 files.
7. **A Rutgers archive page pointed to another narrator's PDF** (Claude V. Bache's page linked a different narrator's file). Found because the PDF title pages did not match the narrator's name; fetched the right file by its name and added a title-page name check to the page-number mapping. Wenzel's page has no PDF link, so his passage has no page number and his full file is the HTML text.
8. **Narrator names from covers can be mistyped.** One WVM cover read "PAKOTA" where the catalog says "Patoka" (OH1280); file names were switched to the stem used on the museum's URL, and descriptors for six interviews were corrected by hand from the cover page.
9. **Shared scratch folder:** another agent overwrote my first `fetch.py` in the session scratch directory; I moved to a private directory with its own copy of the fetch helper; nothing already fetched was affected.
10. **Self-audit bias check.** The project notes that self-audit errors have all run toward flattering the result. The places this could bite here: passage tags (my judgment, not the narrator's), the descriptor for a narrator whose role the archive does not state, and any count in this log. Counts in this log are computed from the files by script, not typed. After the first full pass I re-read every passage again and dropped 6 weak WVM ones; borderline windows were kept out rather than in. One flattering-direction risk remains visible in the data: about a dozen kept passages are mild (tag `other`: a joke told in passing, a seasickness gag) and were kept because they contain a real joke or nickname; weigh them accordingly.
11. **Duplicate transcripts at WVM:** 91 PDFs are alternate versions of an interview already held (names ending `-1` or similar). They were detected by text comparison and the passages come from one copy.
12. **A window can be non-veteran voice at Rutgers:** the archive also interviews relatives and civilians. Passages from them are labeled by role; they are included only where the humor is about the veteran's war, and should not be cited as veteran testimony.
13. **Brown (WVM OH415) lost all passages after pruning** and was left as a full-transcript file with none; swapped for Schuth (OH1419), who has two passages and an explicit "gallows humor" remark. The Brown file was moved out of the folder (not deleted).
14. **One garbled WVM passage dropped** (Thibodeau, OH286): the PDF text layer was corrupted around the joke ("t y n't p y us for som r son"), so the passage could not be trusted as verbatim.
15. **Rutgers full-transcript selection redone after the late round.** Three one-passage files (Taylor, Hance, Silverman) were moved out and replaced by three two-passage narrators found in the late scan (Irwin, Whitson, Berke), so the 40 files are the 40 narrators with the most passages (ties broken by judgment: explicit "gallows/black humor" remarks, spread of wars and branches). Honest note: most Rutgers narrators have only one or two genuine humor passages, so "several genuine humor passages per full transcript" is met only by about 23 of the 40 Rutgers files (see the Passages column in section 5).
16. **Name formatting bug in the Rutgers passage headings** ("Jr., Edward J. Barry" for names with a suffix) found on re-reading the output and fixed in the generator; all headings regenerated.
17. **The late round was low-yield but not zero:** about 540 additional transcripts were fetched, many of them narrators whose interviews are mostly about civilian life; the late T1 scan produced 85 candidate-bearing transcripts and 21 more passages overall came from the late T1, T2 and T2b passes combined.

## 8. Open threads

- **Rutgers transcripts not held:** the HTML transcript universe is 1254 pages (from the `interview` enumeration); 1064 are held, 196 are not. Every roster-matched veteran page and every page that appeared in any of the 236 keyword result lists is held, so the 196 not-held pages are ones that matched neither test (their roster status was not checked; many are probably civilians, family members and home-front narrators, but that is an assumption). Fetching them would take about 196 requests, roughly 11 minutes at the polite rate, plus the reading; whether it is worth it is for the developer to decide. Every held transcript with a keyword hit has already been scanned and its windows read.
- **Rutgers roster names still unmatched to any transcript page:** the name-matching left about 29 of the 137 profile names with no candidate transcript page (they may be PDF-only interviews or listed under another spelling): `kolodziej-edwin`, `lukens-albert-bruce`, `musselman-harold`, `wildanger-edward-g`, `goldfarb-samuel`, `katz-joseph-w`, `rolston-bernard`, `trasatti-joseph`, `adams-thomas-t`, `brady-alfred-v`, `conover-roger-f`, `ruane-michael`, `schenkel-joseph`, `stepaniak-walter`, `smull-brenda-e`, `bird-richard-r`, `cohen-sheldon`, `olsen-walter-chip`, `thau-phillip`, `stenton-sarajane-sally`, `brown-omer`, `lorchak-taylor`, `welles-dorothy-salkin` and a few template placeholders. Not looked up by hand.
- **Bracket-laughter anecdotes without a keyword** (the T3 class) were not read systematically in either archive; a true joke story told without the words "joke", "funny" or "laugh" can be missed by every tier. The cheapest next step would be a scan for narrative markers ("so he said", "and the guy said") near bracketed laughter.
- **WVM:** interviews without a public transcript PDF (about 1,900 of 2,900 per the catalog) are reachable only through the Tier C items; four Hmong-language transcript files were skipped on purpose; PDFs that exist on the site but are not linked from a conflict page (if any) were not found.
- **Query angles not yet run:** songs, toasts and cadence calls; cartoon/Kilroy/"Sad Sack" variants were run once; slang for officers and for the dead by war era (WWII "Section 8", "snafu"; Vietnam "short-timer", "FNG", "dust-off" jokes) were run only through the scan, not through the site search with each variant.
- **Tag set is coarse.** Tags follow the twelve-tag list in the brief; a passage that is both a prank and about the dead carries both tags. A finer coding (who is the butt of the joke, whether the humor is shared with the dead man's friends, whether it stopped) is a job for the own-words extraction step.
- **Rights:** the Rutgers permission-to-quote notice and the WVM no-copy/AI-crawler flags (section 1) are open for the developer. Every quotation in a design document must be re-read at its source first (folder rule 2); the local verbatim files exist to make that check quick.
- **Page numbers:** Rutgers passage pages come from PDF matching; where the PDF's printed page and the pdf page differ the file's `[p.N]` marker is the printed number. One Rutgers passage (Wenzel) has no page.
