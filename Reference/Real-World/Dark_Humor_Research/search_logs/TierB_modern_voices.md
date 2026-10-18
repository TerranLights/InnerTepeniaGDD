# Tier B search log: modern veteran voices (Iraq/Afghanistan era and Vietnam-era retrospectives)

Run date 2026-10-05. Scope: free, openly readable veteran writing in which military dark humor is practiced or discussed, saved as raw text for later own-words extraction. Research only, not canon. Raw texts are local-only (`source_texts/` is git-ignored).

## 1. Result summary

- Files saved: **103** (cap 150), about **198,618** words in the file bodies. Index: `source_texts/modern_voices/_INDEX_tierB_modern.tsv`.
- By folder: `mea_journals/` 17 (MEA site and MEA PDF volumes 13, O-Dark-Thirty 4) | `sandbox/` 46 (Doonesbury Sandbox archive posts 35, personal milblog posts 11) | `other/` 40.
- By angle (index column 5, primary letter): a=13, b=43, c=30, d=7, e=5, f=5. Secondary letters after `;` mark a second angle (for example `b;d`).
- Angle key: a = MEA periodicals; b = O-Dark-Thirty / Warrior Writers / Sandbox / Operation Homecoming; c = milblogs, memoir excerpts and first-person essays about humor; d = leaving the military; e = medics, corpsmen, mortuary, EOD, chaplains and hospital settings; f = talks, interviews and broadcast transcripts.
- Not saved because the free text is not reachable by the tool: see section 6 (Tier C).
- Genre caution: several MEA pieces and all O-Dark-Thirty fiction are labeled fiction or genre-unstated in the index. Sandbox, milblog, War Horse, Havok and Task & Purpose items are nonfiction; as-told-to items (Confessions Of, Szoldra interview) are marked in the author field.
- Identification caution: the seven Sandbox posts signed "Adrian B." are filed as `bonenberger_*`; that surname is inferred (Yale English degree, Afghanistan, "The Satirist at War" milblog) and is not stated in the posts.

## 2. How the fetching was done (and three things that went wrong)

- Every fetch used the required User-Agent `InnerTepeniaResearch/1.0 (personal literature research; low-rate)` via Python `requests` or `curl`. robots.txt was read per host and checked per URL; Crawl-delay was honored where declared (10 s for hekint.org, thisamericanlife.org and webharvest.gov). The default gap was at least 2.6 s per host, 8 s for web.archive.org. Search-engine queries (WebSearch) were used for discovery only; they are not requests to the target hosts.
- Request volume (tool log): militaryexperience.org about 970, scholarscompass.vcu.edu about 230 (Mighty Pen abstract pages), web.archive.org about 150, taskandpurpose.com 30, thewarhorse.org 24, everything else under 25 per host.
- Incident 1 (overlap): a first background crawl of militaryexperience.org that I believed had died kept running, and I started a second copy; for roughly two minutes two processes fetched that host together (some pages twice, about 0.04 s apart). I killed the first process as soon as the duplicate log lines showed it. No block or error followed. The per-host rate-limit state was then rewritten so each host has its own lock file.
- Incident 2 (Wayback load): after 11 Wayback requests in about 25 s (2.6 s gaps) web.archive.org began refusing connections (32 connection-refused errors across the run). I raised the Wayback gap to 8 s, waited about four minutes, and re-ran only the failed fetches. Nothing was forced.
- Incident 3 (shared scratch folder): the session's scratch directory turned out to be shared with other agents; one of my generic script names (`ctx.py`) was overwritten by another agent's file. I moved all my working files into a private subfolder. No source text was lost and no one else's files were edited.
- Blocks were not worked around: no browser User-Agent, no CAPTCHA/Cloudflare workaround, no login or paywall workaround. Every 403 or robots disallow is listed in section 6.
- Wayback use (please review): two groups of sources are read through the Internet Archive because the origin no longer serves them: O-Dark-Thirty (domain `o-dark-thirty.org` no longer resolves in DNS), the Doonesbury Sandbox blog (TypePad closed; `gocomics.typepad.com` now redirects to a Network Solutions notice; `www.gocomics.com/the-sandbox` returns 403). I judged these "dead origin, public archive copy" rather than a circumvented block. If you read it differently, delete `mea_journals/odt_*` and `sandbox/sandbox_*` (the SOURCE line of each file says it was read through the Internet Archive).

## 3. Exact search strings

Strings are exactly as typed into the search tool. A string in square brackets before the query is a domain filter (`allowed_domains`) applied to that search. "Died at the query" means the search engine never surfaced a usable source; "died at the source" means a candidate was found but could not be read or held no humor text.

| # | Search string | Outcome | Where it died / what it led to |
|---|---|---|---|
| 1 | Military Experience & the Arts Blue Falcon Review free humor satire issue | useful | found Blue Falcon Review vol 1/2 pages at militaryexperience.org; search engine did not surface humor-specific pieces (query too generic), so site was crawled directly |
| 2 | militaryexperience.org "As You Were" military literary journal humor veterans | useful | volume index pages (vol 20, 21...); led to full volume list |
| 3 | O-Dark-Thirty Veterans Writing Project journal back issues PDF | useful | 5 PDF URLs at o-dark-thirty.org/wp-content/uploads |
| 4 | Doonesbury "The Sandbox" troop posts Milblogging.com online archive soldiers Iraq blog | partly | found Slate intro, NPR piece, MWSA book listing; no live archive found in results |
| 5 | Warrior Writers anthology free pdf veterans writing "Warrior Writers" Move Zone Mission | dead-end at query/source | results are book listings and reviews, no free full-text anthology |
| 6 | veteran essay "I miss the humor" military banter after leaving the service civilian jokes fell flat | partly useful | surfaced Task & Purpose "Go Easy on the Jargon" (already held by teammates), WATM, G.I. Jobs; also led to Dougie Brimson's blog post (British ex-serviceman), saved |
| 7 | "dark humor" veteran essay "civilians" "I told a joke" after deployment first-person Task & Purpose OR "Military.com" OR "The Mighty" | dead-end at query | returns the same 6-8 pages already collected (Levy/Erony essay, T&P jargon essay, ClearanceJobs, WATM listicles) |
| 8 | mortuary affairs veteran writes about gallows humor Dover OR "Mortuary Affairs" Iraq essay jokes coping | dead-end at sources | found Goodell memoir "Shade It Black" (book, no free text) and NPR Fresh Air transcript (read: no humor content); Dover items are journalist-written |
| 9 | "military humor" OR "gallows humor" veteran first-person essay "when I got out" civilians don't understand our jokes | dead-end at query | same results as above plus a milspouse blog (not a veteran) |
| 10 | Marine veteran essay why we joke about death gallows humor in combat "I laughed" Lit Hub OR Longreads OR Guernica OR "The Atlantic" | dead-end at query | no hits on those outlets; Levy/Erony essay again |
| 11 | combat medic OR corpsman essay dark humor "we joked" about wounded dead first person veteran writes | partly useful | led to medicinthegreentime.com (Vietnam medic site; only holds the Levy/Erony essay copy) and SOFREP op-ed (403 blocked: Tier C) |
| 12 | milblog archive deployment blog 2004 Iraq soldier humor still online | partly useful | Wikipedia/Frontline pages; Milblogging.com is dead; led to PBS Frontline milblog list (blog URLs) that were then tested one by one |
| 13 | early milblogs list Iraq war blogs 2003-2008 archived "Blackfive" OR "Sgt Hook" OR "Armor Geddon" OR "Doc in the Box" OR "Wartime Dispatches" still readable | dead-end at query | returns Wikipedia/CJR background only |
| 14 | "A Soldier's Perspective" OR "Greyhawk" OR "Sgt. Stryker" OR "Back to Iraq" soldier blog Iraq 2005 archive humor "Fobbit" memoir blog post | dead-end at query | Buzzell (already held) and book listings |
| 15 | TED talk veteran comedian military humor transcript "I was in the Army" funny coping war | partly useful | found Hoover Frontline Voices transcript (Robin Phoenix Johnson); no TED transcript located |
| 16 | The Moth story transcript Iraq soldier OR Marine OR medic funny dark humor deployment | dead-end at source | Moth Radio Hour Veterans Day Special 2014 transcript on happyscribe.com returns HTTP 403 (bot-blocked): Tier C |
| 17 | Operation Homecoming NEA writing from the front excerpt soldier humor Iraq essay "Operation Homecoming" anthology excerpt online | dead-end at source | only press pages; the NEA anthology booklet link is dead (see TIER C) |
| 18 | arts.gov "Operation Homecoming" anthology pdf full text download writings troops | dead-end at source | library records cite arts.gov/national/homecoming/OH_Booklet.pdf (dead); govdocs mirror host unreachable |
| 19 | "The Mighty" veteran writes "my sense of humor" changed after military "civilian" dark humor essay | dead-end at query | returns WATM staff listicles and a Royal Marines charity case study (124 words; too short) |
| 20 | Vietnam veteran memoir excerpt humor "black humor" "we laughed" medic OR grunt "free to read" chapter | partly useful | led to Long Daze at Long Binh (two Vietnam medics; website unreachable) and Purtell publisher sample PDF |
| 21 | EOD technician essay humor "bomb tech" gallows humor veteran writes about jokes in EOD community | useful | Task & Purpose EOD "Confessions Of" (saved); VCU Mighty Pen "Confessions of a Bomb Tech" (full text PDF blocked: Tier C) |
| 22 | "nobody gets my jokes" veteran "since I got out" military humor transition essay | dead-end at query | same transition-humor pages; G.I. Jobs staff piece (not first-person veteran) |
| 23 | veteran substack essay "dark humor" "in the Army" OR "in the Marines" "the first time I" laughed at death deployment reflection | dead-end at query | nothing new |
| 24 | "the funniest people I've ever met" veteran essay military humor platoon banter missing it after discharge | partly useful | LOC Folklife VHP jokes post (staff-written; not saved); CS Monitor 2004 reader note (344 words) |
| 25 | MFA thesis veteran memoir Iraq OR Afghanistan "dark humor" creative nonfiction thesis repository pdf Army OR Marine OR Navy | useful | Terrell Fox UW MFA thesis (saved); Prichard UW thesis (read; humor incidental, not saved); Macer (Liberty) and Mujica (UCF) located but not readable via tool |
| 26 | veteran creative writing thesis "gallows humor" war memoir essays soldier author scholarworks OR digitalcommons OR repository pdf | partly useful | same theses |
| 27 | Vietnam veteran self-published memoir free online chapters humor "grunt" OR "medic" OR "REMF" website entire book online | dead-end at source | Smashwords/booklocker/retail pages only; no free chapters reachable |
| 28 | military chaplain essay humor in combat zone "dark humor" soldiers coping chaplain writes reflection Iraq Afghanistan | useful | Hektoen International "Combat hospital chaplain" (saved); CS Monitor chaplain piece (journalist-written; not saved) |
| 29 | "Shade It Black" Jessica Goodell excerpt mortuary affairs Marines humor jokes read online excerpt | dead-end at source | only retailer/library pages; NPR transcript has no humor discussion |
| 30 | Army combat medic memoir excerpt humor Iraq OR Afghanistan "medic" "we laughed" dark humor chapter excerpt publisher free read | dead-end at source | retail/publisher blurbs only |
| 31 | Modern War Institute OR "War on the Rocks" OR "Proceedings" essay humor military culture soldiers dark humor Iraq veteran author argues | partly useful | War on the Rocks "A New Era of Military Comedy from the Ranks" (author Caroline Bechtel; not a veteran; noted, not saved) |
| 32 | Coffee or Die Magazine essay veteran humor gallows "dark humor" first-person Marine OR Army deployment | dead-end at query | a profile of Jack Mandaville; nothing first-person on humor |
| 33 | "Marine Corps Gazette" OR "Military Review" "humor" combat "dark humor" article veteran officer on why troops joke about death morale | dead-end at query | WATM listicles only |
| 34 | Task & Purpose "Confessions Of" series James Clark "hilarious, embarrassing, and revealing stories" corpsman OR medic OR "mortuary affairs" OR chaplain | partly useful | series exists; tag page returns 410; EOD and Marine-grunt entries found |
| 35 | taskandpurpose.com "Confessions Of" "combat medic" OR "Navy corpsman" OR "mortuary affairs" OR "Army chaplain" stories from troops and vets about their job | dead-end at query | no medic/corpsman/mortuary entry surfaced |
| 36 | Larry Heinemann essay Vietnam combat humor jokes "Black Virgin Mountain" OR "Close Quarters" excerpt soldiers laughed | dead-end at query | only the Levy/Erony "War Jokes Wanted" essay (already held) and book/review pages |
| 37 | Karl Marlantes "What It Is Like to Go to War" excerpt humor OR jokes OR laughter chapter free excerpt | dead-end at source | reviews and retailer pages; no free chapter text |
| 38 | Paul Szoldra OR "Duffel Blog" founder essay Marine veteran why veterans joke dark humor first-person | useful | WNYC On the Media transcript with Szoldra (saved); CJR and Herald pieces are journalist-written (read, not saved) |
| 39 | "Dark Laughter" Marine captain Duffel Blog writer pseudonym adjusting to civilian life Afghanistan humor interview | dead-end at source | only the journalist-written Duffel Blog profiles |
| 40 | NPR transcript veterans comedy dark humor soldiers coping interview Iraq veteran comedian "humor" Weekend Edition OR "All Things Considered" | useful | NPR transcripts for Bobby Henline and Tom Irwin (saved) |
| 41 | "This American Life" transcript Iraq soldiers humor OR jokes episode soldier interview "dark humor" thisamericanlife.org | useful | TAL #280 "In Country" transcript (saved) |
| 42 | veteran "dark humor" at work HR complaint joke veterans transition "I was written up" OR "got in trouble" military humor civilian workplace essay by veteran | dead-end at query | POGO story on a VA employee (journalism), WATM staff listicles |
| 43 | "military humor" "veteran" essay "cracking jokes" funeral OR casualty OR "body bag" coping "in my unit" first-person blog post gallows humor explained | dead-end at source | SOFREP piece (403, Tier C); Medium essays (403, Tier C); rest already held |
| 44 | "Colquhoun" Walter Reed wounded soldiers gallows humor restaurant Washington Post "that's how they communicate" | dead-end at source | original Washington Post article not located; only a 380-word blog excerpt |
| 45 | lithub.com excerpt memoir Marine OR soldier Iraq OR Afghanistan veteran author funny irreverent war memoir excerpt "Eat the Apple" OR "Kaboom" OR "Fobbit" OR "The Last Punch" | partly useful | no Lit Hub excerpts; led to NPR Fobbit excerpt and Task & Purpose Eat the Apple excerpt (both saved) |
| 46 | Matt Young "Eat the Apple" excerpt Marine memoir read online Iraq humor chapter | partly useful | retail/library pages; T&P excerpt found via the previous query |
| 47 | Matt Gallagher "Kaboom" excerpt OR chapter "Embracing the Suck" read online humor Iraq platoon leader | dead-end at source | retail pages; blog Kaboom is gone (feed 404) |
| 48 | funny stories deployment Iraq blog soldier "only in the Army" humor blog 2007 OR 2008 OR 2009 "my platoon" pranks hilarious milblog | partly useful | Slate Sandbox excerpt pages (not humor), names of "Fobbits Need Ice Cream Too" and Hartley blogs |
| 49 | Afghanistan deployment blog humor sarcasm soldier "Afghanistan Without A Clue" OR "All Expenses Paid Afghan Vacation" OR "Cheese's Milblog" OR "Castra Praetoria" | dead-end at query | none of the named blogs surfaced; they are only reachable through Sandbox excerpts |
| 50 | Navy corpsman blog humor "Doc" Marines deployment Iraq OR Afghanistan funny stories blog archive corpsman memoir blog "sick call" jokes | partly useful | Doc in the Box blog (807 short posts, humor sparse); WATM corpsman listicles (meme-based, not saved) |
| 51 | "Fobbits Need Ice Cream Too" blog National Guard Iraq convoy Kuwait irreverent | useful | Frontline Club page gave the real blog URL (kbrsecurity.blogspot.com); 3 posts saved |
| 52 | Jason Christopher Hartley "Just Another Soldier" blog Iraq 2005 Balad archive online posts | dead-end at source | blog offline; only NPR/Fresh Air summaries and book pages (open thread) |
| 53 | practical jokes pranks military deployment Iraq soldier blog "prank" "we got him" platoon funniest prank story veteran writes | dead-end at query | the StoryCorps Halloween prank (held by teammates) |
| 54 | Wrath-Bearing Tree veteran writing humor essay "wrath-bearingtree.com" funny OR humor OR laugh Army OR Marine essay | dead-end at source | site returns HTTP 403 to the tool (all paths): Tier C |
| 55 | Havok Journal veteran essay dark humor military "havokjournal.com" humor coping essay by veteran | partly useful | no hits without a domain filter; the domain-filtered form below worked |
| 56 | HuffPost blog veteran "dark humor" OR "gallows humor" Army OR Marine Iraq "I" personal why veterans joke about PTSD contributor | dead-end at query | no HuffPost results |
| 57 | blogs.va.gov Vantage Point veteran humor helped me heal "sense of humor" veteran writes about laughing deployment | dead-end at query | VA Whole Health and Psychology Today pieces are staff/clinician-written (read, not saved) |
| 58 | medium.com veteran "military humor" essay "civilian" "dark" jokes Afghanistan OR Iraq "my friends" written by infantry veteran reflection | dead-end at source | Medium returns 403 to the tool: Tier C |
| 59 | "things I miss about the military" OR "what I miss about the Army" OR "what I miss about the Marine Corps" humor banter jokes veteran essay | useful | Task & Purpose "8 Things I Miss About The Marine Corps" (saved) |
| 60 | Rob Riggle OR "Adam Driver" OR "Colby Buzzell" OR "Brian Castner" OR "Brian Turner" veteran interview transcript military humor "dark humor" coping Marine comedian | dead-end at query | interviews exist but not about humor; Buzzell held by teammates |
| 61 | "Operation Comedy" OR "Armed Services Arts Partnership" OR "ASAP" veteran comedy storytelling bootcamp transcript story "I was a" Army OR Marine funny dark | dead-end at source | program pages only; no transcripts |
| 62 | "Welcome to Confessions Of, a weekly series" Task & Purpose James Clark | dead-end at query | search engine drifted to unrelated "Confessions" titles |
| 63 | "Confessions Of" Task & Purpose "former" "pararescue" OR "combat medic" OR "Navy corpsman" OR "infantryman" OR "Army chaplain" OR "mortuary" series weekly stories troops vets job [extended mode] | useful | found Tank Commander entry (saved); series index page returns 410 |
| 64 | veteran recalls telling joke to civilians "they were horrified" OR "stunned silence" OR "the room went quiet" military dark humor after coming home first-person | partly useful | Coffee or Die "Humor in Combat" (403: Tier C); rest already held |
| 65 | "I learned to laugh again" OR "lost my sense of humor" veteran combat essay Iraq OR Afghanistan OR Vietnam personal essay humor returned | dead-end at query | results repeat held items |
| 66 | veteran essay humor "moral injury" jokes about killing OR dead enemy "laughed" regret later Marine OR soldier writes honest account | dead-end at query | results repeat held items; no new first-person essay |
| 67 | thewarhorse.org veteran essay humor laughter "dark humor" OR "gallows humor" OR "jokes" deployment first-person | dead-end at query | no domain hits without the domain filter |
| 68 | The War Horse "compelled to laugh along at racist jokes" service members Michael Flores Nate Tilton | useful | located "In on the [Racist] Joke" (saved) |
| 69 | [allowed_domains: havokjournal.com] dark humor veteran essay deployment jokes coping personal account | useful | Havok essay list; 6 later saved |
| 70 | [allowed_domains: sandboxx.us] veteran gallows humor military jokes civilians first-person essay | dead-end at source | listicles and joke collections, not first-person essays |
| 71 | [allowed_domains: thewarhorse.org, stripes.com, militarytimes.com] military humor veteran first-person essay jokes deployment dark | useful | War Horse submarine pranks, paratrooper essay, Plummer transition essay; Military Times Beyersdorfer pieces |
| 72 | [allowed_domains: thewarhorse.org] veteran jokes laugh humor deployment barracks banter nicknames first-person memoir essay | useful | Weiskopf, Lyons, Searls essays |
| 73 | [allowed_domains: thewarhorse.org] medic OR corpsman veteran essay jokes dark humor wounded patients deployment | partly useful | Plunkett EMT piece (16k words, humor sparse; not saved); Chrisinger medic essay (no humor) |
| 74 | [allowed_domains: thewarhorse.org, havokjournal.com] mortuary affairs OR chaplain OR EOD veteran essay humor laughter coping | useful | Havok Chamberlin and Smith essays; War Horse Seymour funeral essay |
| 75 | [allowed_domains: thewarhorse.org, havokjournal.com, lithub.com] Vietnam veteran humor memoir essay jokes laughing in Vietnam first person | useful | Meagher "Two Guys to a Bag" (saved) |
| 76 | [allowed_domains: lithub.com, longreads.com, guernicamag.com, narratively.com] veteran memoir excerpt war humor dark funny Iraq OR Afghanistan Marine OR soldier author | dead-end at query | essays about writing war, not humor texts |
| 77 | [allowed_domains: military.com, wearethemighty.com, stripes.com] veteran first-person humor jokes barracks deployment civilians "I" essay dark humor coping | dead-end at query | staff listicles and joke lists |
| 78 | [allowed_domains: substack.com, medium.com, wordpress.com, blogspot.com] Marine OR soldier OR corpsman writes dark humor essay deployment blog post gallows humor friends died laughed | dead-end at source | Medium pages 403 (Tier C); Substack authors were non-veterans |
| 79 | ted.com talk Isaura Ramirez Army veteran comedy talk transcript | dead-end at source | no transcript page found |
| 80 | [allowed_domains: ted.com, tedxtalks.ted.com, youtube.com, singjupost.com, happyscribe.com] TEDx talk veteran humor trauma "dark humor" military transcript soldier comedian "my unit" talk transcript | dead-end at source | TED transcript pages load via JavaScript (page returned about 120 words) |
| 81 | [allowed_domains: militarytimes.com, armytimes.com, marinecorpstimes.com, navytimes.com, airforcetimes.com] Observation Post veteran humor essay dark humor comedy jokes deployment writer veteran perspective | useful | Beyersdorfer's Navy Times Goofy Goober essay and Military Times veteran-writers essay |
| 82 | veteran writes why we laugh at death war humor memoir comic relief Iraq medic OR Marine OR soldier "dark humor" [extended mode] | useful | Michael Anthony "Funny War Memoirs" (saved); other hits held |
| 83 | [allowed_domains: npr.org, pri.org, theworld.org, wbur.org, kqed.org] veteran interview dark humor soldiers jokes coping Iraq war memoir author talks about humor transcript | partly useful | NPR items already held or journalist-voiced |
| 84 | [allowed_domains: taskandpurpose.com] veteran essay humor jokes deployment first-person "dark humor" OR "black humor" OR "gallows humor" coping Marine Army | useful | Mooney essay, Flowers essay; rest held by teammates |
| 85 | [allowed_domains: thewarhorse.org, havokjournal.com, taskandpurpose.com, militarytimes.com] hazing rite pranks nicknames teasing ribbing veteran essay memoir infantry platoon how we talked to each other insults affection | useful | Flowers hazing essay; Splash/chief-initiation essays found next |
| 86 | [allowed_domains: masscasualties.com] Michael Anthony Mass Casualties Army veteran blog humor war memoir dark humor interview OR essay masscasualties.com | partly useful | book pages only (blurbs) |
| 87 | "Mass Casualties" Michael Anthony excerpt Iraq medic operating room "excerpt" read chapter online Skyhorse OR Salon OR "Good Men Project" | dead-end at source | no free excerpt located |
| 88 | Brian Castner "The Long Walk" excerpt EOD team humor jokes read excerpt online bomb tech Iraq | dead-end at source | NPR interview transcript (read; little humor) and retail pages |
| 89 | mortuary affairs specialist veteran first-person account Iraq OR Afghanistan jokes dark humor "Mortuary Affairs" Marine OR Army personal essay site [extended mode] | dead-end at source | Berkeley alumni essay and NPR training story read: no humor content; DVIDS pieces are journalist-written |
| 90 | "The Satirist at War" blog Afghanistan soldier Adrian B. Yale satire milblog | partly useful | identified Adrian Bonenberger as the probable author; the blog itself is gone (feed 404); his Sandbox posts saved |
| 91 | "why are veterans so funny" OR "why soldiers are funny" OR "why military humor" essay by a veteran Iraq Afghanistan "I served" [extended mode] | dead-end at query | Coffee or Die (403, Tier C) and held items |
| 92 | [allowed_domains: mwsadispatches.com, mwsa.co] MWSA Military Writers Society of America dispatches humorous war memoir excerpt Iraq OR Afghanistan OR Vietnam "excerpt" funny veteran author humor chapter | dead-end at source | reviews of memoirs; no excerpt texts |
| 93 | [allowed_domains: vvaveteran.org, vvaw.org, historynet.com, vva.org, vietnamwar50th.com, thewarhorse.org] Vietnam veteran recalls humor in Vietnam jokes pranks gallows humor first-person recollection essay | partly useful | HistoryNet shower mishap (saved); VVA/VVAW items held or not humor |
| 94 | "Vietnam" veteran memoir humor "we laughed" medic OR grunt OR REMF OR chopper free online memoir website chapter "my tour" funny stories [extended mode] | dead-end at source | book-listing pages |
| 95 | [allowed_domains: historynet.com] Vietnam veteran funny story practical joke prank humor in Vietnam first-person recollection soldier | partly useful | Amy Chan hospital-volunteer and ribbons pieces (author status unclear; not saved) |
| 96 | [allowed_domains: historynet.com, military.com, stripes.com, armytimes.com] Iraq OR Afghanistan veteran funny story prank humor first-person recollection soldier "we laughed" deployment memoir article | dead-end at query | video pages and held items |
| 97 | vvaw.org veteran article humor Vietnam "gallows humor" OR "black humor" OR "sense of humor" Vietnam veteran writes The Veteran journal | dead-end at query | VVAW "The Veteran" items checked (ids 408, 1259, 2469, 2056, 3206, 3364, 3676, 3758): none humor-dense |
| 98 | "VVA Veteran" magazine vvaveteran.org humor in Vietnam essay laughter coping memoir veteran writes "humor" | dead-end at query | letters pages only |
| 99 | Vietnam veteran writes about humor in war "we laughed" "Nam" funny stories essay blog "Vietnam War humor" first-hand veteran website | dead-end at source | Together We Served blog pages return 403 (Tier C) |
| 100 | full transcript talk Army OR Marine veteran comedian "laughter" humor healing war "transcript" singjupost OR rev.com OR tedx veteran stand-up talk | dead-end at source | show notes only |
| 101 | podcast transcript veteran dark humor episode "transcript" Marine OR Army veteran host "dark humor" military jokes civilians podcast show notes full transcript | dead-end at source | show notes only; Podbean pages need login |
| 102 | [allowed_domains: taskandpurpose.com, stripes.com, thewarhorse.org] "I laughed" OR "we laughed" OR "made us laugh" veteran personal essay platoon deployment friend died humor remember | useful | Jones suicide-note essay (saved) |
| 103 | [allowed_domains: taskandpurpose.com, thewarhorse.org, havokjournal.com, militarytimes.com, stripes.com] veteran essay civilians ask "how many people did you kill" OR "thank you for your service" joke response humor deflect first person | dead-end at query | Gomez, Ufford and Havok pieces read: answers about civilians' questions, not humor texts |
| 104 | [allowed_domains: havokjournal.com] sarcasm insults banter humor military friends civilians don't get it veteran transition workplace | useful | Perna, Lajoie, Chamberlin essays (saved) |
| 105 | [allowed_domains: thewarhorse.org] dry humor sarcasm nicknames call signs jokes unit funny veteran remembers essay | useful | Chetlain "Splash", Van chief initiation, Hanf (saved) |
| 106 | [allowed_domains: havokjournal.com, thewarhorse.org, sandboxx.us, wearethemighty.com, military.com] humor veteran essay "dark humor" OR "inappropriate jokes" OR "gallows" first-person Army OR Marine OR Navy OR "Air Force" after service coping laughter | partly useful | confirmed held items |

Direct crawls and fetches that were not search strings:

- militaryexperience.org: home page, then all 35 volume index pages (As You Were Vols 1-24, Blue Falcon Review 1-2, Blue Nostalgia 1-4, Blue Streak 1-2, Journal of Military Experience 1-3), then 841 piece pages (1,070,208 words in the text pass). Scored by humor-keyword density and read in context; 13 saved. Full-volume PDFs scanned the same way: JME 1-3, Blue Falcon Review 1-2, Blue Nostalgia 1, Blue Streak 1-2, As You Were 3. Blue Nostalgia Vol 2 PDF returned 404 on the official files host.
- O-Dark-Thirty: the journal's own index pages (read through Wayback) list 27 issue PDFs (fall 2012 to 2021). 23 were retrieved and scanned (about 490,000 words). 4 are not in the Internet Archive (listed in section 6). 4 pieces saved, with PDF page ranges.
- Doonesbury Sandbox: monthly archive pages for 2006-10 through 2011-12 (62 months) read through Wayback; 865 posts parsed (about 715,000 words), scored in three passes (general humor keywords, explicit humor phrases, pop-culture/prank vocabulary), candidates read in part or whole; 35 saved. Months 2006-06 to 2006-09 and 2010-05 return 404 from the archive; 2012-01 failed twice.
- Blogspot milblogs through the standard Blogger feed endpoint (`/feeds/posts/default`), one request per 150 posts. Evaluated:

| Blog | Posts | Outcome |
|---|---|---|
| airborneparainf82.blogspot.com (Eighty Deuce on the Loose, 82nd Airborne team leader, 2006-08) | 115 | humor posts found; 4 saved |
| kbrsecurity.blogspot.com (Fobbits Need Ice Cream Too, Guard infantry, 2009-13) | 44 | irreverent; 3 saved |
| billandbobsadventure.blogspot.com (Old Blue, Afghanistan 2006-09) | 227 | 2 saved (rules of license); Sandbox reposts also saved |
| acutepolitics.blogspot.com (Teflon Don, Ramadi 2006-10) | 185 | 1 saved; mostly politics |
| desertflier.blogspot.com (Air Force officer, Iraq 2007) | 94 | 1 saved |
| armyofdude.blogspot.com, lifeinacrackerbox, mcneillysperspective, sackiniraq, docinthebox, calmbeforethesand, warriorwriters, chaplain.blogspot.com, cybirr, thereplacements, iraqpartii, mdfay, corpsdjour | various | readable; scored; humor sparse or incidental; none saved from the blog itself |
| theunlikelysoldier, navygal, roodawg, badgersforward, desertphoenix, stoplossandawakeup (blogspot) | - | robots.txt disallows crawling: not fetched (Tier C) |
| kerplunkjournal, afghanistanshrugged, thesatiristatwar, funwithhandgrenades, kaboomwarjournal, iraqifreedomadventure | 0-14 | blog deleted or purged; nothing humor-relevant left |

- Other direct fetches: PBS Frontline milblog page (source of blog URLs), Wikipedia Milblog page, Frontline Club milblog page, Slate Sandbox excerpt pages (not humor), Warrior Writers site and blog (225 posts, no humor-dense item), Rutgers-Camden Outside the Wire magazines 2025 and 2026 (two humor-adjacent poems; not saved), TED veterans playlist, webharvest.gov NEA pages.

## 4. Files saved (see the index for the full list with one-line reasons)

- mea_journals/ MEA: 13
- mea_journals/ O-Dark-Thirty: 4
- other/: 40
- sandbox/ Doonesbury Sandbox archive posts: 35
- sandbox/ personal milblog posts: 11

Highest-value items, by research question:

- Rules of license and targets: `billandbobsadventure_sacrosanct_updated`, `sandbox_oldblue_thanksgiving_land_of_sandcastles`, `thewarhorse_lyons_vietnam_veteran_camaraderie` ("we did not joke about more serious injuries"), `thewarhorse_flores_tilton_in_on_the_racist_joke`, `sandbox_nunn_best_victims_are_ourselves`, `havokjournal_chamberlin_*` (two essays).
- Form (pranks, nicknames, lists, mock-epic, storyteller role): `thewarhorse_chetlain_*` (two), `sandbox_raab_mcflurry`, `sandbox_bonenberger_*` (seven), `airborneparainf82_*` (four), `kbrsecurity_that_guy_issue_1`, `mea_jme1_martin_one_night_in_iraq`.
- When it stops or misfires: `sandbox_cleland_compassion_fatigue`, `mea_vol24_davis_ministry`, `mea_vol21_clifton_the_guard_tower`, `thewarhorse_jones_*`, `mea_vol6_laaser_you_laugh` (sensitive).
- After service: `thewarhorse_plummer_*`, `thewarhorse_weiskopf_*`, `taskandpurpose_young_eat_the_apple_excerpt`, `taskandpurpose_clark_8_things_i_miss_marine_corps`, `kbrsecurity_old_navy`, `sandbox_usualsuspect_*`, `odt_v4-2_weaver_jokes_with_civilians` (poem), `hoover_johnson_*` (transcript), `goodreads_brimson_*`.
- Medics, corpsmen, EOD, chaplains, funeral and casualty detail: `hektoen_riggs_*`, `taskandpurpose_confessions_navy_eod`, `sandbox_docinthebox_*`, `sandbox_hart_*`, `mea_vol16_inks_*`, `thewarhorse_meagher_*`, `thewarhorse_seymour_*`, `havokjournal_smith_*`, `sandbox_fathertim_*`.
- Talks and transcripts: `thisamericanlife_280_*`, `npr_tom_irwin_*`, `npr_henline_*`, `wnyc_onthemedia_duffel_blog_szoldra`, `hoover_johnson_*`.

Read and judged not worth saving (so no one re-reads them): Prichard "Stand-To" (UW thesis; humor incidental), the NPR Corrigan review of Eat the Apple (reviewer's voice), Task & Purpose "Ask A Veteran" and Gomez "Did you ever kill anyone" (civilian-question answers, no humor text), CS Monitor chaplain piece, Library of Congress VHP jokes post, Newsweek stateside medic Q&A, Providence "In Defense of Dark Humor" (author not a veteran), Cundall (philosophy professor), Psychology Today/VA Whole Health/Illinois State pieces (clinician or journalist voice), We Are The Mighty meme listicles, HistoryNet Amy Chan pieces and Marlantes (humor incidental or author status unclear), JME 3 "The One Left Behind" (clinician writing about a veteran's funny story), ODT "The Search for Tai" and "Box" (humor incidental).

## 5. Useful vs. dead-end summary

- Productive: direct crawl of MEA and Sandbox archives; the Blogger feed endpoint; domain-filtered searches (`allowed_domains` on thewarhorse.org, havokjournal.com, taskandpurpose.com) after un-filtered phrasing kept returning the same eight pages; transcripts from NPR, This American Life, WNYC and Hoover.
- Saturated: every un-filtered "dark humor / gallows humor / veteran" phrasing returned the Levy/Erony "War Jokes Wanted" essay, the Task & Purpose jargon essay, ClearanceJobs and We Are The Mighty listicles (all already held by teammates).
- Died at the source (found but unreadable or empty): Moth Veterans Day special (403), SOFREP, Coffee or Die, Medium, Together We Served, Wrath-Bearing Tree, Mighty Pen PDFs, Liberty University thesis PDF, UCF thesis (410), Long Daze at Long Binh site, NEA Operation Homecoming booklet, govdocs mirror.

## 6. TIER C: needs a human with a browser

Each item below was blocked, login-gated, JavaScript-only or dead for the tool. Nothing was worked around.

### 6a. Bot-blocked (HTTP 403 to the tool)

1. SOFREP op-ed "Some jokes aren't jokes at all": https://sofrep.com/news/op-ed-some-jokes-arent-jokes-at-all/ . Also, unfetched because the host blocked the first request: https://sofrep.com/news/veteran-humor-rolling-eyes-getting-amped/ and https://sofrep.com/news/this-is-why-dark-humor-memes-are-so-important/ . Save as TXT or HTML into `Tier_C_Dropbox/`.
2. Coffee or Die, "Humor in Combat: Veterans Share Their Funny War Stories": https://www.coffeeordie.com/article/humor-in-combat (and the older path https://coffeeordie.com/humor-in-combat). Also https://coffeeordie.com/military-habits-career-advice/ (not fetched).
3. The Moth Radio Hour, Veterans Day Special 2014 (Mike Scotti and others) transcript: https://www.happyscribe.com/public/the-moth/the-moth-radio-hour-veterans-day-special-2014 . Copy the transcript text.
4. Together We Served blog (Vietnam funny-story posts): https://blog.togetherweserved.com/?p=26581 and https://blog.togetherweserved.com/?p=7772 .
5. Wrath-Bearing Tree (veteran-run literary site, free online; its pages 403 for the whole host): https://wrath-bearingtree.com/ . Worth a hand search for humor, parody and satire pieces; none were identified by title because the site cannot be searched by the tool.
6. Medium: Jerry Glazer, "Humor in Hell: Laughter, Sarcasm, and Survival in Vietnam": https://jerryglazer.medium.com/humor-in-hell-laughter-sarcasm-and-survival-in-vietnam-8f205b1278c3 ; Rachel Brune, "Writing Military Humor": https://medium.com/@rachelbrune/writing-military-humor-9cb40e30b9a0 .
7. Takin' a Walk podcast notes, Thom Tran "Comedy Saved Me": https://takinawalk.com/podcast/comedy-saved-me-with-thom-tran-and-the-healing-power-of-laughter/ (show notes only expected).
8. VCU Mighty Pen Project archive (veteran memoir/fiction; abstract pages readable; the one full-text PDF tested, item 186, returned 403, so assume the rest do too). 213 items were inventoried by abstract and keyword tags. Items whose tags or abstracts suggest humor, pranks or hazing, to fetch by hand (open the item page and use its Download button):

| Item | Title | Author | Tags / abstract (short) | Item page |
|---|---|---|---|---|
| 41 | My Best Day at Sea | Rob Paylor | 1981-2000 Army, 2018: An Army chopper pilot off the coast of Beirut plays a trick on a Marine platoon on their carrier. | https://scholarscompass.vcu.edu/mighty_pen_archive/41 |
| 44 | Class 05-84 | Lacy Ward | 1981-2000 Navy, 2018: A young Navy pilot finds a humorous way to hold onto his individuality during basic training. | https://scholarscompass.vcu.edu/mighty_pen_archive/44 |
| 79 | Skyline | Charles Williamson | 2001-2020 Army, 2019: In Afghanistan, a convoy runs into trouble on the road back from Kabul airport. A violent yet humorous take on | https://scholarscompass.vcu.edu/mighty_pen_archive/79 |
| 115 | Who's Laughing Now | June Forte | 1961-1980 Army, 2020: Using the chain of command as an appeal process, a woman soldier in the '70s reports her company commander and | https://scholarscompass.vcu.edu/mighty_pen_archive/115 |
| 121 | Water Bucket | Ken Mick | 1961-1980 Army, 2020: Soldiers in Vietnam find time to have some fun while demonstrating the use of helicoptered water buckets. | https://scholarscompass.vcu.edu/mighty_pen_archive/121 |
| 131 | 3311 Elvis | Joe Maslanka | 1981-2000 Marines, 2020: Marine trainees at Parris Island enjoy music from one of their own, as he tries to avoid further hazing. | https://scholarscompass.vcu.edu/mighty_pen_archive/131 |
| 169 | Waterloo | John Price | 1961-1980 Army, 2022: A new recruit and his friend find a way to get back at two corrupt trainers. | https://scholarscompass.vcu.edu/mighty_pen_archive/169 |
| 185 | Sam's Club | Cam Torrens | 2001-2020 Air Force, 2024: A harrowing interview with The White House, a 45 pound briefcase called 'The Football" containing presidential | https://scholarscompass.vcu.edu/mighty_pen_archive/185 |
| 186 | TYFYS | Dustin Dunbar | 2001-2020 Army, 2024: Our narrator humorously recounts an uncomfortable conversation in a grocery store, and reflects on the complic | https://scholarscompass.vcu.edu/mighty_pen_archive/186 |
| 190 | A Day in the Life of a Beanhead | Patrick Potter | 1961-1980 Army, 2024: It's a beautiful spring morning at West Point Academy, and Cadet Potter is barefoot, late, and an easy target. | https://scholarscompass.vcu.edu/mighty_pen_archive/190 |
| 195 | Untouchable | Cam Torrens | 1981-2000 Air Force, 2024: Three 18 year old Air Force Cadets, finding themselves with a bit of cash and unsupervised free time, decide t | https://scholarscompass.vcu.edu/mighty_pen_archive/195 |
| 224 | Inshallah | Phillip Trezza | 2001-2020 Army, 2025: Set during a deployment in Iraq, Inshallah follows a U.S. Army medic reflecting on the chaos, camaraderie, and | https://scholarscompass.vcu.edu/mighty_pen_archive/224 |

9. Liberty University MA thesis, Joshua Macer, "The Weight of Gratitude and the Burden of Truth" (Army infantry, four combat tours; humor content unknown): abstract at https://digitalcommons.liberty.edu/masters/1113 , PDF https://digitalcommons.liberty.edu/cgi/viewcontent.cgi?article=2117&context=masters (403).
10. UCF thesis, Alejandro Mujica, "Escape Artist" (fictional memoir of a Marine; HTTP 410): https://ucf.digital.flvc.org/islandora/object/ucf%3A49732 .
11. TED talks with veteran speakers (transcripts load by JavaScript; the tool saw about 120 words): https://www.ted.com/talks/adam_driver_my_journey_from_marine_to_actor/transcript and https://www.ted.com/talks/wes_moore_how_to_talk_to_veterans_about_war/transcript . Neither is expected to be humor-dense; low priority.

### 6b. Origin blocks crawling by robots.txt (owner's choice; not fetched)

- http://theunlikelysoldier.blogspot.com (The Usual Suspect; one Sandbox post of his is saved), http://navygal.blogspot.com, http://roodawg.blogspot.com, http://badgersforward.blogspot.com, http://desertphoenix.blogspot.com, http://stoplossandawakeup.blogspot.com . Read in a browser if wanted.

### 6c. Dead, missing or not reachable at all

- O-Dark-Thirty issues that are not in the Internet Archive (domain `o-dark-thirty.org` is gone): Vol 5 No 1 (Fall 2016) https://o-dark-thirty.org/wp-content/uploads/2016/11/5-1_web_text.pdf ; Vol 2 No 4 https://o-dark-thirty.org/wp-content/uploads/2012/11/odt_text_2-4_web1.pdf ; Vol 2 No 1 https://o-dark-thirty.org/wp-content/uploads/2012/11/v-2-1_text_web_bsingle-pg.pdf ; Vol 1 No 4 https://o-dark-thirty.org/wp-content/uploads/2012/11/odt_vol_1_4-for-web.pdf . Ask the Veterans Writing Project (www.veteranswriting.org, which holds no archive) or a library. Issues 7.x (2018-19) are not listed on the journal's own index page and were not found.
- NEA Operation Homecoming anthology booklet: the library-record URL http://www.arts.gov/national/homecoming/OH_Booklet.pdf is dead; the webharvest.gov copies of arts.gov Operation Homecoming pages returned 404 or timed out. The Random House anthology (ed. Andrew Carroll, 2006) is a book, not free. Nothing from Operation Homecoming is in this set.
- Doonesbury Sandbox, other months: 2006-06 to 2006-09 and 2010-05 are not archived; 2012-01 fetch failed. Original blog host is gone; the book "Doonesbury.com's The Sandbox" (ed. David Stanford, Andrews McMeel, 2007) is not free.
- Warrior Writers anthologies (Re-Making Sense, After Action Review, Move Shoot and Communicate, and later): only sold; no free full text found. The organization's two Rutgers-Camden magazines (2025, 2026) are free but contained nothing humor-dense.
- Long Daze at Long Binh (two Vietnam medics, humorous memoir): longbinhdaze.com returned an 8-word page; sample chapters not reachable. Hellgate Press sample of Jim Purtell's "Vietnam: There and Back" (combat medic) exists as a PDF (https://www.hellgatepress.com/wp-content/uploads/2018/02/First_25_pages_purtell-1.pdf) but was not scanned for humor; low priority.
- Washington Post, "Gallows humor heals wounded vets" (Walter Reed; caretaker Ross Colquhoun): original not located; only a 380-word blog excerpt at https://sheckymagazine.com/?p=186 . Search the Post archive by hand.
- Colby Buzzell and Terminal Lance material: held by teammates, not touched.

## 7. Open threads

- More War Horse, Havok Journal and Task & Purpose first-person essays almost certainly exist: the un-filtered search engine could not surface them, the domain-filtered form could. Next step: run `allowed_domains` searches with other single-topic words ("nickname", "roast", "sarcasm", "funeral", "boot camp", "night shift", "sick call", "care package") and read the results through the same triage (author bio, body length after boilerplate strip, humor in context).
- Task & Purpose "Confessions Of" series: only Navy EOD, Marine grunt (Matt Young), Tank Commander and the staff piece were found. The tag index page returns 410; other installments (Navy diver is named in a search snippet) need exact titles.
- Dead milblogs worth a patient Wayback pull (8 s gap): Just Another Soldier (Jason Christopher Hartley), The Satirist at War (Adrian Bonenberger), traversa.typepad.com, tobynunn.typepad.com, Castra Praetoria, Red Bull Rising, Afghan Quest, The Gun Line, Cheese's Milblog, Afghanistan Shrugged. All appear in the Sandbox posts' "Milblog" fields; none has been tested for archive coverage. Note the same reviewer question as in section 2 about Wayback use.
- Sandbox posts that the keyword scoring may have missed: humor that uses no keyword (understatement, lists, mock-formal prose). A second human skim of the 865-post database is possible; the parse is in the scratch folder, not the repo.
- Foreign-army voices (British, Canadian, Israeli) were not sought; two incidental ones were saved (Brimson, Lajoie). Teammates cover other armies.
- Wounded-veteran comedy (Comedy Warriors cast: Rice, Kashnow, Henline, Tran, White): only Henline has a first-person transcript saved. Others are journalist-voiced pages; their own books and sets would need a library copy.
- Chaplain humor: two Sandbox chaplains and one Hektoen essay saved; the chaplain.blogspot.com blog (Brad Lewis, 103 posts) and Chaplain Andrews' site were only scored, not read in full.
- Genre labels for MEA pieces with no author bio (McPadden, Whitehead, Laaser, Bleuer, Watts) are unverified; check the print volumes if fiction-versus-memoir matters for an extraction.

## 8. Files and locations

- Raw texts: `source_texts/modern_voices/mea_journals/`, `sandbox/`, `other/` (first five lines of each file: SOURCE, AUTHOR, TITLE, PUBLICATION/DATE, FETCHED 2026-10-05; PDF-derived files carry `[p.N]` markers using PDF page numbers).
- Index: `source_texts/modern_voices/_INDEX_tierB_modern.tsv` (filename, url, author, title, category, words, why it matters).
- This log: `search_logs/TierB_modern_voices.md`.
- Not touched: `source_texts/modern_voices/terminal_lance/` and anything else in the research folder outside the three folders and the log above.
