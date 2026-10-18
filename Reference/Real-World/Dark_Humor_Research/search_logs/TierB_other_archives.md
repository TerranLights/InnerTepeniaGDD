# Tier B log: other open oral-history archives (veteran gallows / dark humor)

Run date 2026-10-05. Agent: Tier B "other archives" harvester. Research only, not canon. All requests used the fixed User-Agent `InnerTepeniaResearch/1.0 (personal literature research; low-rate)` with TLS verification on; gap of at least 2.6 s between requests to a host (4 s in practice on veterans.gc.ca; 10 s on koreanwarlegacy.org, which states Crawl-delay: 10; 10 s on archives.gov, Crawl-delay 10).

## 0. Result at a glance

| Archive folder (under `source_texts/oral_history/other/`) | Archive | Transcript files saved | Passages |
|---|---|---|---|
| `ny_military_museum/` | New York State Military Museum and Veterans Research Center, Veterans Oral History Program | 40 | 45 |
| `korean_war_legacy/` | Korean War Legacy Foundation, Interview Archive | 20 | 23 |
| `vac_heroes_remember/` | Veterans Affairs Canada, Video Gallery "Heroes Remember" clips | 18 | 21 |
| `army_csi_eyewitness_to_war/` | U.S. Army Combat Studies Institute, Eyewitness to War (Operation Al-Fajr oral history), Vols I-II | 2 | 6 |
| `usmcu_marine_oral_history/` | Marine Corps University, Marine Corps History Division oral history (career interviews) | 3 | 6 |
| `ua_vietnam_oral_history/` | University of Alabama, Vietnam War Oral History Archive (student interviews) | 1 | 1 |

`memory_project/` and `ww2_museum/` are empty on purpose: the Memory Project archive is blocked to our tools (Tier C, section 7) and the National WWII Museum holds no verbatim transcripts that we could reach (section 2). Six archives hold output, which is the cap; two more were harvested and then held back or dropped (NARA veterans oral histories: nine PDFs, three mild prank passages, moved out of the project folder to respect the cap of six; Northwest Iowa / Morehead State / UCF: blocked, see section 7).

Total HTTP requests logged by the harvesting helper: 3275 (plus web-discovery searches, section 4). Per-host counts are in section 8.

## 1. Method and rules applied

- **Helper.** One small Python `requests` wrapper (fixed UA, per-host timestamp files, request log). One process per host at a time; two different hosts were sometimes run side by side, never two processes on one host. (A stale VAC list crawler was killed before the prioritized VAC node crawler was started.)
- **robots.txt read first for every host.** Rules honored: `/search/` (veterans.gc.ca, nationalww2museum.org, ww2online.org), `/do/` and `/cgi/query.cgi` (Digital Commons sites, so no site search there), `/digital/search/` (CONTENTdm sites such as dmr.bsu.edu, cgsc.contentdm.oclc.org), `/collections/search` (iwm.org.uk), Crawl-delay values.
- **Operator AI-crawler policy treated as binding in spirit.** Several archives name Anthropic crawlers in robots.txt with `Disallow: /` (UNT Digital Library, ExploreUK/Nunn Center, NIU digital, BBC, DPLA, GVSU). Our User-Agent is not literally `ClaudeBot`, but the operators evidently do not want Claude-driven harvesting, so these were not fetched and are listed as Tier C for a human with a browser.
- **No circumvention.** 403 / Cloudflare / CloudFront / Incapsula / Anubis proof-of-work pages and TLS certificate failures were logged and left. No Referer tricks, no alternate UA, no cache or mirror routes, no TLS verification off.
- **Local grep rather than site search where site search was disallowed or absent** (New York State Military Museum, USMCU, Army CSI, Alabama): download the permitted transcript files, then search locally. Lexicon used locally (regex, case-insensitive): `humo(u)r(ous|ist)`, `jok(e|es|ed|ing|er|ers)`, `prank*`, `practical jok*`, `nick-?name*`, `made fun|making fun|make fun`, `kidd(ed|ing)`, `black|sick humo(u)r`, `gallows`, `hilarious`, `wisecrack`, `hazing`, `ribbing`, `razz*`, `comic relief`, `sense of humo(u)r`, plus `laugh*|chuckl*|giggl*|funn(y|ier|iest)` when not a bracketed transcriber marker such as `[laughs]` or `(laughter)`. A second pass searched coping phrases (`laugh or cry`, `you had to laugh`, `kept us going`, `break the tension`, `lighten up`, `funny at the time`, `dark humor`, `joked about death`, and similar; 42 hits in the corpora; 2 new passages came out of it (Deitz, Morby), the rest were noise such as "lighten the load").
- **Reading rule.** Every saved passage was read in context by the agent; keyword hits that were "funny = strange", "just kidding", "gallows" as a building, "lighten the plane", and similar were discarded. Passage text is verbatim from the saved local text (whitespace reflowed; running page headers/footers removed in the NYS Museum PDFs); extraction is done by start/end anchor strings so no passage text was retyped.

## 2. Archives evaluated, with decisions

| Archive | How it was checked | What it exposes | Decision |
|---|---|---|---|
| The Memory Project (Historica Canada), thememoryproject.com | home page, sitemap.xml (14 URLs, none are stories), robots; links lead to the Canadian Encyclopedia; historicacanada.ca sitemap (17 Memory Project video pages) and one video page | The old story archive moved to The Canadian Encyclopedia. Historica video pages carry no transcripts. | **Tier C**: thecanadianencyclopedia.ca returns CloudFront 403 for robots.txt and article pages on both host spellings. Substitute found: Veterans Affairs Canada "Heroes Remember" (separate program, same kind of veteran interview clips with transcripts). |
| National WWII Museum | robots; ww2online.org (digital collections) robots (Crawl-delay 10) and one oral-history page; 8 podcast pages with full transcripts (Veteran Voices S4 ep. 1-6, D-Day special ep. 2, "To the Best of My Ability" ep. 2) | ww2online oral histories show museum-written annotations ("eventual transcription planned"), not verbatim speech. Podcast transcripts are edited historian conversations; whole set contains 1 "joke" (about a Soviet woman tanker), 1 "humor" (Good Humor truck), 2 "laugh/giggle" mentions, none relevant. | **Rejected for verbatim humor material.** Nothing saved. |
| Library of Congress Veterans History Project | robots (Crawl-Delay 5); one JSON API request; one item page; blogs.loc.gov post | loc.gov: Cloudflare "Just a moment..." 403. blogs.loc.gov is reachable: "Cutting the Tension" (2017) quotes only two short narrators and notes that early VHP field kits listed humor as an interview theme and that a VHP search for "jokes" returns thousands. | **Tier C** (section 7) for the collection and item pages. |
| IWM Sound Archive | robots; one item page found by web search (object 80035314, which the search summary says discusses black humour in the military) | Cloudflare challenge 403 | **Tier C.** |
| Texas Tech Vietnam Center and Archive | robots on vva.vietnam.ttu.edu, vietnam.ttu.edu, www.vietnam.ttu.edu | `SSLCertVerificationError` on all three | **Tier C** (not bypassed, as instructed). Same failure on history.navy.mil, veterans.library.northeastern.edu, media.library.ohio.edu. |
| UNT Digital Library / Oral History Program | robots | `ClaudeBot`, `Bytespider`, `meta-*`, `GoogleOther` disallowed by name; `*` Crawl-delay 3 | **Not fetched** by operator policy; Tier C. |
| UK Nunn Center SPOKEdb (kentuckyoralhistory.org); ExploreUK | home page; robots | SPOKEdb serves an Anubis proof-of-work "Making sure you're not a bot!" page; ExploreUK names Anthropic bots as disallowed | **Tier C.** |
| NIU digital (digital.lib.niu.edu) | robots | names Anthropic/Claude bots disallowed; Crawl-delay 50 | **Not fetched**; Tier C. |
| Univ. of Florida UFDC (Samuel Proctor) | robots only | no AI-bot rule; JS application, transcripts not enumerated in the time spent | **Open thread**, not harvested. |
| UCF STARS Veterans Oral Histories | robots, collection page, one item page | `/do/` search disallowed; items are audio with timed log summaries, not transcripts; PDF/native downloads route through `viewcontent` | Rejected (no transcripts reachable). |
| Morehead State Vietnam War Oral History (Digital Commons) | collection page (53 transcript PDFs listed), then 4 PDF fetches | `cgi/viewcontent.cgi` PDFs returned 403 four times | **Tier C**; stopped after 4 requests. |
| Northwest Iowa Vietnam Veterans Oral History (Digital Commons) | collection page (19 transcripts), one PDF fetch | `viewcontent.cgi` 403 | **Tier C.** |
| NZ History (nzhistory.govt.nz) | robots | 403 on robots.txt | **Tier C.** |
| BBC WW2 People's War | robots | ClaudeBot, Claude-Web, anthropic-ai disallowed | **Not fetched**; Tier C. |
| DPLA (dp.la) | robots | ClaudeBot, anthropic-ai disallowed | not fetched |
| GVSU Digital Collections | robots | long AI-bot list incl. anthropic-ai | not fetched |
| Univ. of South Carolina Marine Corps oral histories | robots | 403 | **Tier C.** |
| Appalachian State Veterans Oral History (Omeka) | robots | 403 | **Tier C.** |
| Juno Beach Centre | robots | `Crawl-Delay: 3600` for all agents | not fetched (1 request per hour is not a workable rate) |
| NJ National Guard Militia Museum | two pages | `.org` host returns an Incapsula challenge; `.gov` pages hold a "Summary" and audio only | rejected |
| NY State Military Museum Veterans Oral History Program | 24 alphabetical listing pages, 626 transcript PDFs | **full verbatim transcripts, no site search** | **HARVESTED** (section 3.2) |
| Veterans Affairs Canada "Heroes Remember" video gallery | robots, gallery, search form | clip pages with verbatim transcripts; Solr search covers titles/descriptions only | **HARVESTED** (3.1) |
| Korean War Legacy Foundation | robots (Crawl-delay 10), JS bundle, AJAX search endpoint | 507 interviews with full timestamped transcripts; the site's own transcript keyword search works | **HARVESTED** (3.3) |
| Army CSI "Eyewitness to War" Vol I-II | found by web search; armyupress.army.mil PDFs | 2 PDFs of verbatim interview transcripts with Fallujah 2004 soldiers | **HARVESTED** (3.4) |
| Marine Corps University oral histories | robots; career-interview page (33 PDFs listed) | text-layer PDFs, large | **HARVESTED, partly** (3.5) |
| Univ. of Alabama Vietnam War Oral History Archive | robots; WordPress REST media list (61 PDFs) | 27 unique student-interview transcripts | **HARVESTED** (3.6) |
| NARA Veterans Oral Histories | robots (Crawl-delay 10), 9 PDFs | peacetime/support veterans, mild pranks | harvested, **held back** (cap of six) |
| Legion Magazine | robots (empty), "Humour Hunt" category and one article | columnist essays and reader anecdotes, not interview transcripts | not an oral-history archive; skipped |
| Utah Valley Univ. Vietnam Era Oral History; UCI "My Viet Nam War" | landing pages | UVU pages moved (404s); UCI has 7 interviews in Omeka S, search API returned empty | small / unreachable; not harvested |
| Ohio University Cantigny 1st Infantry Division oral histories (Phase II); Ball State (Phase I) | ohio.edu page; TLS failure on media.library.ohio.edu; dmr.bsu.edu robots, collection landing 200, 26 sitemap files | Ohio: cert failure. Ball State: `/digital/search/` disallowed, collection alias `Cantigny` exists but item URLs are not in the sitemaps | **Open thread / Tier C.** |

## 3. Archives harvested: how search worked, exact queries, counts

### 3.1 Veterans Affairs Canada, Heroes Remember (veterans.gc.ca)

Gallery: 4,589 items; category "Heroes Remember" (field_video_category=41210) lists 4179 clip pages (the category counter said 4,189). Search is a Solr full-text on **title and description only**: the test word "Ghurkha", which occurs in a transcript but in no title or description, did not return that clip. Multi-word queries behave as OR; no stemming ("joke" 19 hits, "jokes" 0, "joking" 0); fuzzy matches occur ("gag" returns "Gap" titles, "joke" returns "Joe"). Search endpoint: `GET /en/news-and-media/video-gallery?search_api_fulltext=<q>&page=<n>`.

Exact queries and hit counts (total as printed "of N results"):

| query | hits | query | hits | query | hits |
|---|---|---|---|---|---|
| `humour` | 47 | `humor` | 42 | `joke` | 19 |
| `jokes` | 0 | `joking` | 0 | `laugh` | 3 |
| `laughed` | 3 | `laughing` | 3 | `funny` | 12 |
| `prank` | 16 | `pranks` | 0 | `practical joke` | 33 |
| `practical jokes` | 14 | `practical jokers` | 14 | `humorous` | 32 |
| `hilarious` | 0 | `amusing` | 22 | `comical` | 1 |
| `comedy` | 0 | `gag` | 47 | `gags` | 18 |
| `nickname` | 4 | `nicknamed` | 4 | `nicknames` | 4 |
| `sense of humour` | 99 | `sense of humor` | 94 | `teasing` | 0 |
| `teased` | 0 | `tease` | 0 | `kidding` | 15 |
| `black humour` | 258 | `gallows humour` | 47 | `gallows` | 0 |
| `morbid` | 0 | `wisecrack` | 0 | `banter` | 3 |
| `ribbing` | 0 | `mischief` | 0 | `mischievous` | 0 |
| `antics` | 1 | `shenanigans` | 0 | `entertainment` | 3 |
| `concert` | 23 | `skit` | 27 | `made fun` | 350 |
| `mocked` | 0 | `mocking` | 0 | `ridicule` | 0 |

From these, 105 clips whose title/description mention humor, joke, laugh, funny, prank, amusing, nickname, kidding, banter, antics, comic, gag, tease, mischief, morale or camaraderie were fetched and read first (priority tier). Then the category listing (4179 clips) was crawled (351 listing pages) and clip pages were fetched in order of a cue score computed from title/description (words such as dead, killed, wounded, POW, prisoner, morale, spirit, officer, sergeant, latrine, rum, funny, trick, song, story, anecdote, incident). **Clip pages fetched: 1400 of 4179.** Coverage by cue-score tier (fetched / in tier): score 5+: 75/75; score 3-4: 389/389; score 2: 361/361; score 1: 552/771; score 0: 11/2583. The score-0 tier (clips with none of the cue words in title or description) was mostly not fetched (open thread). Clips are short (1-3 minutes, median about 300 words), so a passage is usually the whole answer.

Local grep on the fetched clips (1029 unique transcripts, 350,432 words): humor 17, joke 14, laugh 51, funny 76, nickname 6, made fun 2, kidding 5; about 8-12 percent of non-priority clips carry any hit. Useful: the curated "humorous" clips (mild anecdotes, a few good gallows items in POW and Afghanistan clips). Dead end: most keyword hits are "funny" meaning odd.

### 3.2 New York State Military Museum Veterans Oral History Program

No site search. The 24 alphabetical listing pages (`/research/oral-history-project/oral-history-program-veteran-interviews[-a..z]`) list 1927 records; 626 carry a transcript PDF link (`/download_file/view/<id>/3978`); the rest are video only or biographies. All 626 PDFs were downloaded (626 requests, 0 errors); 20 files are byte-identical duplicates of another record and 2 PDFs had no text layer (ids 361, 444), leaving 606 unique searchable transcripts (3,340,159 words). Local lexicon hits (humor 82, joke 92, prank 22, practical joke 6, nickname 43, made fun 2, kidding 69, funny 420, laugh-words incl. transcriber markers 2069, gallows 3); 445 transcripts have at least one hit. At least 26 transcripts contain an interviewer question aimed at humor or pranks ("Were there any humorous incidents or pranks?"), so a share of the hits are answers to that standing question; the best material came from open answers and follow-ups. Index fields are not always right (Dr. Walter Guenther is listed as "Vietnam War" but is a WWII German Army soldier).

### 3.3 Korean War Legacy Foundation

Search used: the site's own POST `/wp-admin/admin-ajax.php` with `action=filter_advanced_search`, `itemtype[]=fullinterview` (the "Transcripts" filter, 507 interviews), `advancedkeyword=<query>`, paginated. AND/OR must be uppercase. Crawl-delay 10 s honored. Hit counts are numbers of interviews whose transcript matches.

| query | hits | query | hits | query | hits |
|---|---|---|---|---|---|
| `humor` | 14 | `humour` | 0 | `joke` | 27 |
| `jokes` | 7 | `joking` | 14 | `laugh` | 236 |
| `laughed` | 18 | `laughing` | 44 | `funny` | 94 |
| `prank` | 2 | `pranks` | 1 | `practical joke` | 0 |
| `nickname` | 23 | `nicknamed` | 5 | `made fun` | 2 |
| `black humor` | 1 | `gallows humor` | 0 | `sense of humor` | 3 |
| `kidding` | 38 | `laugh AND dead` | 112 | `laugh AND killed` | 153 |
| `laugh AND wounded` | 118 | `joke AND officer` | 20 | `joke AND dead` | 18 |
| `humor AND killed` | 9 | `funny AND wounded` | 49 | `humor AND home` | 14 |
| `humor AND after the war` | 5 | `laugh AND officer` | 147 | `joke AND captain` | 12 |
| `joke AND lieutenant` | 10 | `joked AND dead` | 1 | `sick humor` | 0 |
| `morbid` | 0 | `laughing AND bodies` | 9 | `humor AND cope` | 2 |
| `hazing` | 0 | `pranks AND officer` | 1 | `hilarious` | 0 |
| `amusing` | 5 | `comical` | 4 | `teased` | 1 |
| `teasing` | 0 | `ribbing` | 1 | `razzed` | 0 |
| `tease` | 4 | `jokester` | 0 | `joker` | 2 |
| `jokers` | 1 | `kidded` | 2 | `comedian` | 1 |
| `clown` | 1 | `wisecrack` | 0 | `funny AND dead` | 54 |
| `funny AND killed` | 65 | `joke AND wounded` | 15 | `joke AND medic` | 8 |
| `humor AND war` | 14 | `humor AND prisoner` | 3 | `laughed AND prisoner` | 10 |
| `laugh AND bodies` | 51 | `joke AND death` | 10 | `laugh AND nightmares` | 13 |
| `humor AND PTSD` | 0 | `joke AND PTSD` | 3 | `humor AND Korea` | 14 |
| `humor AND coping` | 0 | `laugh AND crying` | 28 | `laugh AND cry` | 48 |
| `joked AND shelling` | 0 | `joke AND shell` | 10 | `funny AND artillery` | 47 |
| `nicknamed AND dead` | 4 | `nickname AND killed` | 14 | `prank AND dead` | 2 |
| `hazing AND officer` | 0 | `joke AND general` | 18 | `joke AND colonel` | 5 |
| `joke AND sergeant` | 17 | `made fun AND officer` | 2 | `humor AND civilians` | 4 |

311 distinct interview pages matched at least one query and were fetched (all of them). Of the 507 transcripts, about 196 never matched any query. "laugh" (236) and "funny" (94) are inflated by transcriber markers; the productive terms were `humor` (14), `joke` (27), `joking` (14), `prank` (2), `nickname` (23), and the AND-combinations with dead/killed/wounded/officer. Dead end at the query: "gallows humor" 0, "sick humor" 0, "morbid" 0, "hilarious" 0, "wisecrack" 0, "practical joke" 0, "hazing" 0 (the archive has few of these words; the content is there in plainer language). Local lexicon over the 310 unique fetched transcripts (1,903,344 words): humor 19, joke 60, nickname 29, funny 171, laugh-words 1419. Several interviews are translated (Spanish, Greek) by the archive; the original-language line is interleaved.

### 3.4 Army CSI, Eyewitness to War (Operation Al-Fajr)

Found by web search ("Army oral history Operation Iraqi Freedom soldiers interview transcript ...", section 4). The originals on apps.dtic.mil (ADA460458) and permanent.fdlp.gov are blocked (403 / Cloudflare); the same two volumes are served by armyupress.army.mil under `/Portals/7/Primer-on-Urban-Operation/Documents/EyewitnessToWar_Volume{I,II}.pdf` (both ~0.9 MB; fetched after HEAD). Local lexicon: 322,433 words, 51 hits (joke 8, funny 16, laugh 20, kidding 4); six passages kept (a seventh from an embedded journalist was dropped because she is not a veteran). Chapter narrator/rank is taken from the interview headings in the PDF.

### 3.5 Marine Corps University oral histories (career interviews)

Landing page lists 33 PDFs. **Lapse recorded:** the first 8 were downloaded in one run before their sizes were checked (950 MB total, three of them 240-320 MB image-heavy scans); the run was stopped. Sizes of the other 25 were then read with HEAD requests and the 9 under 5 MB were fetched (17 PDFs in total); the 16 over 5 MB remain unfetched (open thread). Local lexicon over 2.37 million words: humor 80, joke 46, laugh 351, nickname 16, kidding 13. These are senior officers (plus Capt. James Webb, a Vietnam rifle-platoon commander); useful mainly for command humor, inter-service rivalry and one gallows-flavored unit in-joke. Page labels in the passages are PDF page numbers.

### 3.6 University of Alabama Vietnam War Oral History Archive

WordPress REST `GET /vietnamwar/wp-json/wp/v2/media?per_page=100&mime_type=application/pdf` listed 61 PDFs; 55 transcripts were fetched, 27 are unique (many uploaded two or three times), 2 are scanned images with no text (ids 1814, 1816). Student-run interviews; several narrators are civilians or family members. Local lexicon: humor 8, joke 4, laugh 85 (mostly markers), funny 36. One strong passage (a Marine disbursing clerk at Dong Ha).

## 4. Web discovery searches (WebSearch tool; these are search-engine queries, not requests to archive hosts)

- `Memory Project Historica Canada veteran testimony transcript "we used to joke" OR "black humour" OR "had a good laugh" thememoryproject.com stories` -> led to canadian-encyclopedia mpsb-* story URLs (blocked) and the quote "People survive the war by having a little humour"
- `thecanadianencyclopedia.ca memory project archive veteran transcript sense of humour soldiers jokes` -> led to veterans.gc.ca "A Sense of Humour" (Ronald Tee) and "Humor kept us going" (Ganong): the VAC Heroes Remember route
- `National WWII Museum oral history transcript veteran interview "transcript" nationalww2museum.org digital collections` -> dead end: no transcript database; led to NJ Militia Museum and NY State Military Museum pages
- `nationalww2museum.org oral histories collection "oral history" transcripts searchable digital collections WWII veteran interview full text (allowed domain nationalww2museum.org)` -> ww2online.org lead
- `National WWII Museum "oral history" "we laughed" OR "joked" OR "sense of humor" veteran interview transcript (allowed domain nationalww2museum.org)` -> podcast transcript pages (Steve Ellis, Alan Moskin) - checked, nothing relevant
- `"National WWII Museum" digital collections oral history interview transcript "Interview with" Digital Collections item page (extended)` -> ww2online.org item pages: annotations only
- `veteran oral history interview transcript "gallows humor" Vietnam OR Korea OR Iraq pdf (extended)` -> Wisconsin Veterans Museum (teammates), Univ. of Alabama Vietnam PDFs, TTU, LOC blog
- `oral history transcript Marine OR soldier "black humor" "we used to joke" dead bodies interview university digital collections` -> USMCU oral history PDFs, USC Marine Corps oral histories (403), Baylor, ODU
- `Iraq OR Afghanistan veteran oral history full transcript "dark humor" OR "black humor" interview digital collection university library` -> LOC VHP items (blocked); Oklahoma State Iraq/Afghanistan project is audio only; NC archives
- `Korean War veteran oral history transcript laughed joked "sense of humor" digital library open access transcripts collection` -> UNT (policy-blocked), Korean War Legacy (the productive lead), GVSU, UWF
- `Gulf War OR "Operation Iraqi Freedom" veterans oral history transcripts online free "transcript" collection soldiers interviews humor coping` -> App State Omeka (403), National Archives veterans oral histories, Eyewitness to War via fdlp (blocked)
- `"oral history" veterans transcripts collection "full text" searchable Cold War OR Vietnam enlisted interviews "pranks" OR "practical jokes" university special collections` -> Morehead State (403 PDFs), Utah, Cantigny 1st Division
- `Cantigny First Division Foundation oral histories collection transcripts online Vietnam enlisted interview pdf` -> Ohio University (TLS failure), Ball State (search disallowed)
- `"Eyewitness to War" Operation Al Fajr oral history Combat Studies Institute pdf armyupress.army.mil OR usacac.army.mil OR cgsc.edu` -> DTIC and FDLP copies blocked; armyupress copy found in the next search
- `iwm.org.uk collections item object sound interview British NCO "humour" army gallows humour oral history (allowed domain iwm.org.uk)` -> ten IWM object ids (Tier C)
- `oral history interview transcript combat veteran "gallows humor" OR "dark humor" OR "black humor" we joked about the dead "interviewer" transcript digital collections Vietnam enlisted infantry` -> Wisconsin transcripts (teammates), vva.org column "Gallows Humor Wanted", Nunn Center SPOKEdb record
- `Vietnam veterans oral history project transcripts online free university "transcript" "humor" medic OR infantry OR helicopter Kansas OR Utah OR Oregon OR Montana OR Indiana` -> UVU, UCI, Univ. of Nebraska Omaha, Middle Georgia State: small or unreachable
- `Utah Valley University Veterans of the Vietnam Era Oral History Project transcripts` -> 17+ interviews; library pages moved (404)
- `UCI "My Viet Nam War" oral history project omekas.lib.uci.edu interview transcript` -> 7 interviews; small
- `legionmagazine.com veteran recalls humour soldiers jokes interview "told Legion Magazine" army humour trenches (allowed domain legionmagazine.com)` -> columnist essays, not transcripts
- `Army oral history Operation Iraqi Freedom soldiers interview transcript "gallows humor" OR "dark humor" history.army.mil OR cgsc OR usacac OR armyheritage` -> found armyupress.army.mil EyewitnessToWar_Volume{I,II}.pdf (the harvest)
- `veterans oral history transcripts Vietnam "black humor" "we laughed" digital collection "oral history" Kennesaw OR Georgia OR Virginia OR Ohio OR Michigan OR Illinois library interview transcript pdf veteran` -> Northwest Iowa (PDF 403), Virginia Tech, Ball State Vietnam

## 5. Dead ends and where each died

- **At the source (blocked/unreachable):** thecanadianencyclopedia.ca (CloudFront 403), loc.gov and memory.loc.gov (Cloudflare), iwm.org.uk (Cloudflare), apps.dtic.mil (403), permanent.fdlp.gov (Cloudflare), nzhistory.govt.nz (403), digital.library.sc.edu (403), omeka.library.appstate.edu (403), kentuckyoralhistory.org (Anubis), Digital Commons `viewcontent.cgi` PDFs at Morehead State and Northwest Iowa (403), TLS failures at vva.vietnam.ttu.edu, vietnam.ttu.edu, history.navy.mil, veterans.library.northeastern.edu, media.library.ohio.edu, Incapsula at njmilitiamuseum.org.
- **At the policy (robots/Crawl-delay):** UNT, ExploreUK, NIU (+50 s), BBC, DPLA, GVSU (AI bots named); Juno Beach Centre (3600 s); site-search paths disallowed at veterans.gc.ca, nationalww2museum.org, ww2online.org, Digital Commons sites, CONTENTdm sites, iwm.org.uk.
- **At the content (reachable but not what was needed):** ww2online.org (annotations, not speech), National WWII Museum podcasts, UCF STARS (audio and logs), NC Archives Veterans Oral History (audio, finding aid), ECU Vietnam interviews (one audio item), NJ Militia Museum (summaries), Legion Magazine (essays), UCI (7 interviews).
- **At the query:** `gallows humor`, `sick humor`, `morbid`, `hilarious`, `wisecrack`, `hazing`, `practical joke` all returned 0 in the Korean War Legacy transcript search; `jokes`, `joking`, `pranks`, `comedy`, `teased`, `ribbing`, `mocked` returned 0 in the VAC title/description search (no stemming).

## 6. Files saved

**`other/ny_military_museum/`** (40 transcript files, 45 passages, `_PASSAGES_ny_military_museum.md`)

`nysmm_1179_miller-rose-l.txt`, `nysmm_1203_mulligan-robert-e-sr.txt`, `nysmm_1274_o-shea-michael-f.txt`, `nysmm_1443_rodd-gary-wayne.txt`, `nysmm_1703_tanner-jack.txt`, `nysmm_17565_brown-harold-t.txt`, `nysmm_17591_b-17-crew-group-interview.txt`, `nysmm_17609_baranowski-donald-a.txt`, `nysmm_17624_battillo-anthony.txt`, `nysmm_17638_belfield-justus-rathbone.txt`, `nysmm_17644_bennett-david-charles.txt`, `nysmm_17663_blair-walter-r.txt`, `nysmm_17671_bly-james-jamie.txt`, `nysmm_17676_borden-howard-w.txt`, `nysmm_17684_brach-albert-j.txt`, `nysmm_1_abaied-james-k.txt`, `nysmm_242_cartwright-james-jim.txt`, `nysmm_24457_booth-robert-t.txt`, `nysmm_24459_buck-lewis.txt`, `nysmm_24502_bohen-alexander-joseph.txt`, `nysmm_311_colyer-thurlby-amos.txt`, `nysmm_338_corte-louis-rudolph.txt`, `nysmm_339_cosgrove-charles-lester.txt`, `nysmm_393_decorse-anthony-r.txt`, `nysmm_397_deitz-raymond-charles.txt`, `nysmm_486_eggleston-elmer.txt`, `nysmm_490_elisha-paul.txt`, `nysmm_516_fanniff-robert-f.txt`, `nysmm_518_farfaglia-carmelo.txt`, `nysmm_526_favata-angelo.txt`, `nysmm_533_fendt-frank-charles.txt`, `nysmm_541_fleisher-mark-i.txt`, `nysmm_587_german-ron.txt`, `nysmm_652_greene-charles-e-jr.txt`, `nysmm_677_guenther-dr-walter-p.txt`, `nysmm_681_gunn-richard-n-sr.txt`, `nysmm_685_haag-nathan-william.txt`, `nysmm_913_kneiper-joseph-w.txt`, `nysmm_970_dr-lavigne-richard.txt`, `nysmm_ab061ad9-77a_browe-dr-john-harold.txt`

**`other/korean_war_legacy/`** (20 transcript files, 23 passages, `_PASSAGES_korean_war_legacy.md`)

`kwlf_antone-jackim.txt`, `kwlf_baldwin-f-myers.txt`, `kwlf_bob-wickman.txt`, `kwlf_chaplain-ralph-lindon-smith-jr.txt`, `kwlf_charles-l-hallgren.txt`, `kwlf_charles-ross.txt`, `kwlf_clayborne-lyles.txt`, `kwlf_david-white.txt`, `kwlf_dennis-e-hultgren.txt`, `kwlf_duane-trowbridge.txt`, `kwlf_gerald-land.txt`, `kwlf_gustavo-mendez-2.txt`, `kwlf_jack-allen.txt`, `kwlf_jack-whelan.txt`, `kwlf_john-j-baker.txt`, `kwlf_keith-g-hall.txt`, `kwlf_maurice-morby.txt`, `kwlf_patrick-v-hickey.txt`, `kwlf_rebecca-baker.txt`, `kwlf_walter-kreider-jr-2.txt`

**`other/vac_heroes_remember/`** (18 transcript files, 21 passages, `_PASSAGES_vac_heroes_remember.md`)

`vac_alfred-joseph-babin.txt`, `vac_charlie-fawcett.txt`, `vac_collin-fitzgerald.txt`, `vac_douglas-warren.txt`, `vac_eric-thomson-baggs.txt`, `vac_everett-sylvester-cromwell.txt`, `vac_horace-gerrard.txt`, `vac_james-bevan.txt`, `vac_jeff-kelly.txt`, `vac_john-mcgee.txt`, `vac_l-o-paul-b-rard.txt`, `vac_leo-murphy.txt`, `vac_robert-mccue.txt`, `vac_robert-wiseman.txt`, `vac_ross-purse.txt`, `vac_roy-henley.txt`, `vac_whitfield-ganong.txt`, `vac_william-chrysler.txt`

**`other/army_csi_eyewitness_to_war/`** (2 transcript files, 6 passages, `_PASSAGES_army_csi_eyewitness_to_war.md`)

`csi_eyewitnesstowar_volumei.txt`, `csi_eyewitnesstowar_volumeii.txt`

**`other/usmcu_marine_oral_history/`** (3 transcript files, 6 passages, `_PASSAGES_usmcu_marine_oral_history.md`)

`usmcu_barrow_Gen_Robert_H_Barrow.txt`, `usmcu_krulak_Gen_Charles_C_Krulak.txt`, `usmcu_webb_Capt_James_H_Webb_Jr.txt`

**`other/ua_vietnam_oral_history/`** (1 transcript files, 1 passages, `_PASSAGES_ua_vietnam_oral_history.md`)

`ua_vietnam_3229_al-rocco.txt`

Scratch-only (not in the project): the full downloaded corpora (NY 626 PDFs, KWLF 311 pages, VAC clip pages, USMCU 17 PDFs, UA 55 PDFs, NARA 9 PDFs) live in the agent scratchpad and will not persist.

## 7. TIER C: needs a human with a browser

Everything below was reached (or tried) on 2026-10-05 and refused, or is excluded by the operator's robots policy. For each: exact URL, what happened, what to type. Save pages as PDF ("Print, Save as PDF") or the transcript text, one file per interview, into `Tier_C_Dropbox/`.

**1. The Memory Project archive (Historica Canada), now hosted by The Canadian Encyclopedia**

- https://www.thecanadianencyclopedia.ca/en/the-memory-project (French: https://thecanadianencyclopedia.ca/fr/le-projet-memoire)
- story pages follow the pattern https://www.thecanadianencyclopedia.ca/en/article/mpsb-<first-last>, for example mpsb-david-galbraith, mpsb-e-david-hart, mpsb-romeo-ouellet, mpsb-joseph-william-joe-vicaire, mpsb-percy-howard, mpsb-john-hall (surfaced by web search)
- Result: Amazon CloudFront "403 ERROR: Request blocked" for robots.txt and article pages, on both thecanadianencyclopedia.ca and www.thecanadianencyclopedia.ca.
- Manual search: open the Memory Project Archive, search each of: humour, humor, "sense of humour", laugh, joke, prank, nickname, "black humour". A search-result snippet quotes William "Bill" Davis: "War is a terrible thing. And people survive the war by having a little humour." Each story page carries video, summary and transcript.

**2. Library of Congress Veterans History Project**

- https://www.loc.gov/collections/veterans-history-project-collection/?q=humor (and q=jokes, q="black humor", q="gallows humor", q=pranks, q=laughed); item pages https://www.loc.gov/item/afc2001001.<number>/
- Result: Cloudflare "Just a moment..." 403 on the collection API URL and on an item page; memory.loc.gov legacy VHP URLs redirect into the same wall.
- Items surfaced by web search and worth opening: afc2001001.70381 (Marine, Iraq, segment on using humor to cope), .67449, .111714, .70708, .113534, .98995, .19670 (Alice Curry), .31965; narrators quoted by the VHP blog: Donald F. Gardner (Korea, creative punishment) and James Otis Handy (Tuskegee Airman).
- Reachable and read: https://blogs.loc.gov/folklife/2017/04/cutting-the-tension-vhp-narrators-cracks-jokes-and-quips/ (short; says early VHP field kits listed humor as an interview theme).
- Manual filter: keep only records that show a transcript (many VHP records are video or audio only).

**3. Imperial War Museums Sound Archive**

- https://www.iwm.org.uk/collections/item/object/80035314 (Paul Moore; summary mentions soldiers' humour, black humour and "the role of black humour in the military"), also objects 80031387, 80025413, 80010199, 80034590, 80026489, 80013843, 80025968, 80024238, 80020123
- Result: Cloudflare challenge ("Just a moment... Enable JavaScript and cookies"); robots.txt also disallows /collections/search.
- Manual search: collections search for "black humour", "gallows humour", "practical jokes"; open Sound items and read the catalogue summary (IWM records are usually summaries with timed topics, not verbatim transcripts).

**4. Texas Tech University, Vietnam Center and Sam Johnson Vietnam Archive (Oral History Project, about 1,100 interviews)**

- https://www.vietnam.ttu.edu/oralhistory/ , https://vietnam.ttu.edu/oralhistory/interviews/ , https://vva.vietnam.ttu.edu/
- Result: TLS certificate verification failure on all three hostnames (not bypassed).
- Manual search: Virtual Vietnam Archive, Oral History collection, keyword humor / joke / gallows / nickname; each interview page links audio plus transcript PDF.

**5. University of Kentucky Nunn Center SPOKEdb and ExploreUK**

- https://kentuckyoralhistory.org/ (example record: https://kentuckyoralhistory.org/ark:/16417/xt7m639k6g6t, American Veterans: Vietnam War Oral History Project, 145 interviews); https://exploreuk.uky.edu/
- Result: Anubis proof-of-work page ("Making sure you're not a bot!") on SPOKEdb; ExploreUK robots disallows anthropic-ai, Claude-Web, ClaudeBot.
- Manual search: SPOKEdb keyword search inside transcripts / indexes for humor, jokes, "black humor", nickname, hazing.

**6. UNT Digital Library and Portal to Texas History (UNT Oral History Program)**

- https://digital.library.unt.edu/ (example: https://digital.library.unt.edu/ark:/67531/metadc306675/ , Earl E. Ambrose, Korean War)
- Result: one robots.txt request; `Disallow: /` for ClaudeBot and other AI agents by name. Not harvested.
- Manual search: collection "UNT Oral History Program", full-text search humor / jokes / pranks, filter military.

**7. Digital Commons repositories whose PDFs return 403 to non-browser clients**

- Morehead State: https://scholarworks.moreheadstate.edu/vietnam_war_oral_history/ (53 transcript PDFs listed on the page; `cgi/viewcontent.cgi?article=1158&context=vietnam_war_oral_history` and three more returned 403)
- Northwest Iowa: https://nwcommons.nwciowa.edu/vietnamveterans/ (19 transcripts; `viewcontent.cgi?article=1019&context=vietnamveterans` returned 403)
- UCF STARS: https://stars.library.ucf.edu/veteransoralhistories-worldwarii/ (also -vietnamera, etc.): audio plus timed logs, not transcripts; site search under `/do/` is disallowed
- GVSU: https://digitalcollections.library.gvsu.edu/ (Veterans History Project collection): robots names anthropic-ai among disallowed agents
- Manual: open each item page and use the Download button; for Morehead, the "Transcripts" series near the bottom of the collection page.

**8. Other blocked or refused sources**

- New Zealand History: https://nzhistory.govt.nz/ (403 on robots.txt). Search "humour" within the Vietnam, Korea and WWII oral-history items.
- BBC WW2 People's War: https://www.bbc.co.uk/history/ww2peopleswar/ (robots disallow ClaudeBot / Claude-Web / anthropic-ai). Full-text search "laughed", "joke", "dark humour".
- University of South Carolina Marine Corps oral histories: https://digital.library.sc.edu/marinecorps/oral-history-interviews/ (403; example don-sanders-interview/).
- Appalachian State Veterans Oral History: https://omeka.library.appstate.edu/collections/show/18 (403).
- Naval History and Heritage Command oral histories (https://www.history.navy.mil/) and Northeastern University veterans archive (https://veterans.library.northeastern.edu/): TLS certificate failure.
- Ohio University Cantigny 1st Infantry Division Oral History Phase II (https://www.ohio.edu/library/digital-collections/digital-archives/cantigny -> https://media.library.ohio.edu/digital/collection/cantigny/search): TLS certificate failure. Phase I at Ball State: https://dmr.bsu.edu/digital/collection/Cantigny (landing page loads; item search is disallowed; item ids not discoverable by us).
- Eyewitness to War Vol. I at https://apps.dtic.mil/sti/pdfs/ADA460458.pdf (403) and https://permanent.fdlp.gov/lps77920/EyeWitnesstoWarVolume1.pdf (Cloudflare): not needed, the armyupress.army.mil copies were fetched.
- NIU digital collections (https://digital.lib.niu.edu/): robots disallow Anthropic bots, Crawl-delay 50.
- DPLA (https://dp.la/): robots disallow ClaudeBot, anthropic-ai. NJ Militia Museum interviews (https://njmilitiamuseum.org/ , Incapsula challenge). Juno Beach Centre (Crawl-Delay 3600).

## 8. Request counts by host (agent helper log, 2026-10-05)

| host | requests | note |
|---|---|---|
| www.veterans.gc.ca | 1921 | 351 listing pages, clip pages, 143 keyword-search result pages, robots/terms |
| museum.dmna.ny.gov | 653 | 24 listing pages, 626 PDFs, robots |
| koreanwarlegacy.org | 430 | 81 AJAX queries (multi-page) + 311 interview pages + JS bundle + robots (10 s gap) |
| adhc.lib.ua.edu | 58 | 55 PDFs + media list |
| www.usmcu.edu | 45 | 17 PDFs + 25 HEAD size checks + pages |
| dmr.bsu.edu | 31 | 26 sitemap files (about 9 MB each, fetched in error; no Cantigny URLs found) |
| www.nationalww2museum.org | 14 |  |
| www.archives.gov | 12 |  |
| scholarworks.moreheadstate.edu | 11 |  |
| www.armyupress.army.mil | 7 |  |
| www.thememoryproject.com | 5 |  |
| www.historicacanada.ca | 4 |  |
| stars.library.ucf.edu | 4 |  |
| legionmagazine.com | 4 |  |
| (remaining 50 hosts) | 76 | robots.txt and single probe requests, including every blocked host above |

## 9. Process snags and self-corrections (recorded on purpose)

- **Size not checked before bulk download (twice).** (a) USMCU: the first run pulled 8 career-interview PDFs in about 90 s totalling roughly 950 MB (largest 319 MB) before sizes were looked at; stopped, then HEAD-checked the rest and fetched only the 9 under 5 MB. 16 PDFs of 5-160 MB were left unfetched. (b) Ball State: 26 sitemap files of about 9 MB each (240 MB) were fetched while looking for Cantigny item URLs, none found; the local copies were truncated. Rule now followed: HEAD first.
- **Wrong narrator attribution caught.** In Eyewitness to War Vol. II, the speaker "JA" in one candidate passage is Jane Arraf, an embedded CNN journalist, not a veteran; the passage was dropped. The automatic chapter finder initially attributed a Vol. I passage to the wrong interviewee (Rainey instead of Maj. Lisa DeWitt); fixed by also reading the "I'm interviewing X (XX)" lines.
- **Index fields are unreliable.** NYS Museum index lists Dr. Walter Guenther as "Vietnam War"; his transcript is a WWII German Army soldier. KWLF stub names such as `gustavo-mendez-2` are the archive's own slugs.
- **Cap enforcement.** NYS Museum passages first covered 42 interviews; two single-line passages (Breslow, Etts) were removed to stay at 40 transcripts. NARA and the Eyewitness/USMCU ranking: NARA output (3 prank passages) was moved out of the project folder to stay at six archives.
- **Search semantics learned the hard way.** VAC gallery search ignores transcripts and does not stem; a first reading of "47 results for humour" as transcript hits was wrong. KWLF "laugh" hits are mostly transcriber markers.
- **Quoted text is unchanged except for whitespace reflow and removal of PDF page furniture;** USMCU text is OCR with scan errors left in; the Alabama Otter.ai transcript is machine-generated; KWLF Spanish/Greek interviews are archive translations interleaved with the original.

## 10. Open threads

- VAC: 2779 clip pages not fetched (the 2,583 with no cue word in title/description and the tail of the score-1 tier). A second sweep, or a targeted one by category (e.g. "Heroes Remember - Korean War", Afghanistan), would extend coverage. Extra description-keyword queries not yet run: dark, ironic, sarcasm, wit, ditty, parody, mimic, cartoon.
- KWLF: about 196 transcripts never matched any query; they might still hold gallows humor in plain words. The "bio" interviews (about 550 without full transcript) have only clip summaries.
- NYS Museum: 1,301 listing records have video only; no transcripts exist for them. Terms of reuse not stated on the pages.
- USMCU: 16 career-interview PDFs unfetched (Davis 159 MB, Erskine 34 MB, Zinni 69 MB, O. P. Smith 24 MB, Fitch 50 MB, Howell 90 MB, T. H. Miller 71 MB, Trainor 52 MB, Fris 10.5 MB, Schilt 9.3 MB, Noble 6.3 MB, Day 6.6 MB, Murray 11 MB, Hittle 20 MB, Navajo Talkers Vol. 1 99 MB and Vol. 2 71 MB). The Navajo Talkers volumes are enlisted narrators and may repay a manual download; Marine Corps Vietnam and OIF field-interview catalogs are listed on the landing page.
- UA: two scanned PDFs (ids 1814, 1816) would need OCR; the Alabama media list shows only 61 PDFs but the site's "Archive" page may link interviews as audio only.
- NARA veterans oral histories: nine PDFs read; three mild prank/peacetime passages (Beebe submarine shoe prank with the line "You learn to take a good joke...", Daverede Marines-in-line gag, Coryat flag prank) are held in the agent scratchpad and can be restored if a seventh archive is wanted.
- Archives noticed but not evaluated: University of Florida UFDC Samuel Proctor oral histories (JS app), Baylor Institute for Oral History (Quartex), Utah Valley University and Univ. of Utah Vietnam projects, Univ. of Nebraska Omaha Vietnam oral histories, Middle Georgia State, Virginia Tech Vietnam interviews, Combined Arms Research Library "Operational Leadership Experiences" interviews (cgsc.contentdm.oclc.org; search disallowed, item pages allowed), Library and Archives Canada, Canadian War Museum.
- Modern-war coverage is thin outside Eyewitness to War, VAC (Afghanistan, Bosnia, Gulf clips), and a handful of NYS Museum Iraq/Gulf interviews; the CARL OLE interviews and the LOC VHP Iraq/Afghanistan items are the natural next sources.