# Dark Humor — Where to Seek Real Basis-of-Reference Material (Leads, 2026-10-05)

> **Update 2026-10-05 (later):** the extraction and collection work these leads called for has begun in `../Dark_Humor_Research/` (folder README, extraction checklist, Tier C shopping list, extractions `E01`…). This file remains the lead-finding record and search log.

**What this is.** The developer's 2026-08-29 note (see `00_Extraction_Checklist.md`, "Developer insights") says the
Cancer district's unnamed ex-military defector would plausibly have an **extremely dark sense of humor** — *real,
documented military gallows humor, not invented quips* — and that none of the ten books in
`to-be-integrated/books/PTSD/` covers it. This file is the **lead-finding pass** that note asked for: where to
look, what is already confirmed, what is blocked, and which people and institutions are legitimate routes to real
veterans.

**What this is NOT.** It is **not** an extraction and **not** his voice. The checklist's rule stands: *do not
synthesize his voice/dialogue until real source material (or direct input) is actually in hand.* Nothing below is
canon. The "documented patterns" in §2 are **findings about how real military humor behaves**, offered as design
constraints and candidates — not as sample lines for him.

**How it was made.** Four parallel web-research agents, one angle each, instructed to open real pages (no recall),
query every category from more than one angle, and log dead ends. Detail files (full lead lists, exact search
strings, where each dead end died, open threads):

| File | Angle | Leads |
|---|---|---|
| `11a_Dark_Humor_Leads_Academic_and_Clinical.md` | scholarly and clinical literature | ~55 |
| `11b_Dark_Humor_Leads_Primary_and_First-Person_Sources.md` | soldier-made media, memoirs, oral-history archives | 36 |
| `11c_Dark_Humor_Leads_People_and_Communities.md` | veteran comics, satirists, writing programs, consultants, communities | ~45 |
| `11d_Dark_Humor_Leads_Craft_and_Cross-Cultural.md` | how fiction/games write it; other armies; defectors and exiles; civilian-facing register | ~45 |

**Reliability caveats (read before relying on any quote).**
1. Most page text came back through a **summarizing fetch tool**, so every quotation in the detail files must be
   **re-read on its source page** before it is used in a design document. Titles, dates, URLs and access status are
   the reliable part.
2. Tags: `VERIFIED-OPEN` = the researcher opened the page · `VERIFIED-META` = citation confirmed through a
   Crossref/OpenAlex record but publisher text was blocked · `UNVERIFIED` = search snippet only or blocked.
3. Spelling was swept to American English on import, including inside titles and quotations (never inside URLs), so
   a title here may differ in spelling from the printed original.
4. Several important sources were **blocked to the tools** (Library of Congress Veterans History Project, Imperial
   War Museum, Army University Press, several publishers). Those need a person with a normal browser (§5).
5. The origin military of this character is not fixed anywhere in this folder, so the material spans U.S., British,
   German, Danish, Norwegian, Israeli, Indian, Soviet/Russian and WWI-Commonwealth sources on purpose. Real-world
   sources are **mechanisms, not specifications** (project rule); Tepenian culture is produced locally.

---

## 1. Headline: what the search found, and what it did not

- **Plenty exists** on military humor in general — a real, citable scholarly literature (functions, ethnographies,
  surveys) and a large body of soldier-made primary material, much of it free (WWI trench newspapers, the
  Vietnam-era folklore bibliography, archived modern milblogs and webcomics).
- **Real veteran-humor practitioners are reachable through legitimate institutions** (§4) — comedy programs with
  public shows, writing programs, a media-industry veterans' association.
- **Almost nothing exists on the humor of someone who left their own military on principle.** No source documents
  the *content* of a principled defector's humor about his own break (searched from Soviet, North Korean,
  Vietnam-era, Iraq-era, East German, Syrian, refusenik and objector angles; logged in `11d`). The closest verified
  items are indirect (§2 item 10). **His humor about the break will have to be built by analogy from the material
  below, and ideally tested with real people — not copied from any source.**
- **The studio's own precedent does not help with humor.** No developer commentary on *Fallout: New Vegas*' Boone
  was found that discusses his humor, and the one fan analysis opened reads him as "all restraint and almost no
  venting." He is not a joker. A Boone-style companion with a dark sense of humor therefore needs its basis from the
  real-world record, which is exactly why this lead file matters.
- **Two gaps the developer may care about:** no peer-reviewed study ties **humor to moral injury** (the nearest is
  Molendijk 2025, a moral-injury scholar writing on military humor), and none was found on **humor used to deflect
  disclosure in therapy** or **humor as a suicide-risk marker**. These sit right on the defector's profile (see
  Findings 185–205 and 233–266 in file `07`).

---

## 2. Documented patterns worth carrying into design (candidates, not his voice)

Each is a finding about real military/occupational humor, with the lead that supports it. All need the source
re-read before use.

1. **What it does:** controlled resistance to hardship; cohesion and in-group boundary; negotiating rank and power;
   individual stress relief; and — Obrdlik's original 1942 point — a **double edge**: solidarity inward, corrosion
   aimed outward. *(Johais 2025 `11a` B2 / `11d` C1; Godfrey 2016; Obrdlik 1942 `11a` A1.)*
2. **Where the jokes are aimed:** mostly at **the soldiers themselves, the institution, rear-echelon brass and the
   weather — not at the enemy.** Self-deprecation (a collective "us idiots"), black humor and understatement are the
   three recurring styles. *(Molendijk 2025 `11a` B1; Mauldin `11b` 17; Blackadder writers' principle in `11d` A8:
   target "the madness that led to those people dying," never the dead.)*
3. **Form:** institutional or civilian language laid over horror, played **deadpan, the joke never explained** —
   mock hotel ads for a shattered salient, a mock insurance scheme with absurdly small death payouts, a golf column
   where the hazards are gas and corpse smell. *(The Wipers Times and The Anzac Book, `11b` 1-5.)* Modern grunt
   register is profane, fast and unedited. *(Buzzell's blog, `11b` 24; Gallagher: soldiers detect fake dialogue
   instantly, `11b` 25.)*
4. **A joke has to be built, not quipped.** Heller: "you can't be funny just by saying a joke, you have to lead up
   to it." Klay: the best comedy is "both humorous and serious at once." *(`11d` A1, A5.)*
5. **The known failure — the quip after the kill.** EA Montreal's own postmortem on *Army of Two* named
   fist-pumping and a funny line after killing as the mistake: "people just felt... this is wrong." The joke landed
   on the kill, not on the institution, the self, or the aftermath. *(`11d` B8.)* A banter-heavy veteran also reads as
   false until the humor shows **wear and cost** (Spec Ops: The Line analysis, `11d` B7).
6. **Who may say it, when, and how often.** A joke is funny or monstrous depending on who tells it, the moment, the
   content and the frequency; the same line about a dead man is fine in the squad and unforgivable to a stranger or
   to the dead man's brother (benign-violation theory; Dutch firefighter ethnography; veteran comics' "earned the
   right"). A newcomer's dead-comrade joke before he has earned it costs status. *(`11a` A6, A8, D3; Wicked Comedy
   quotes in `11c` A8.)*
7. **Two registers — and the funny version is a shield.** Soldiers conceal their humor from civilians (the
   "WARFUN taboo," `11a` B3); veterans sanitize what they send to strangers who ask for jokes (Levy & Erony: only
   about half a dozen real gallows jokes among the submissions, `11b` 21); Klay: war stories come in a **funny
   version and a sad version, chosen by audience** (`11d` A2). Veteran comics deliberately translate for civilians
   and drop jargon (`11c` (f)). After leaving, combat medics in one small study **suppressed their dark humor** and
   felt unable to be fully themselves anywhere (`11a` C3), while British veterans describe banter that "made rooms
   go quiet" (`11a` C4).
8. **It is not automatically protective.** In a 93-veteran U.S. survey, dark humor did **not** alienate civilian
   friends, but **self-defeating humor (jokes at one's own expense) tracked markedly lower life satisfaction** —
   the style writers most often assign as "charming" is the one associated with doing worse (Yoshimura 2024, `11a` C2).
   In 2,291 police officers, dark styles (cynicism, sarcasm) tracked distress and never protected against it
   (Anders 2025, `11a` C9). Large in-service data run the other way for humor *with a unit* (humor, morale and
   cohesion travel together and track fewer PTSD symptoms in 20,901 soldiers; Ward/Brown 2021, `11a` C1) — which
   suggests the cohesion half of the package is what **leaving removes**.
9. **Silence is information.** In Dutch firefighters, black humor goes **absent after certain incidents**, and "the
   absence of humor is a sign for the crew commander to pay extra attention to coping" (`11a` D3). Paramedics name
   the cost directly: it "makes a barrier... but covers up processing," "creeps into family and personal life"
   (`11a` D4). And Molendijk documents where it rots: once the soldier no longer feels the paradox, black humor
   turns to Schadenfreude, self-deprecation to self-dehumanization, understatement to **moral numbness**.
10. **Defector- and exile-specific evidence (thin, but real):**
    - **Russian deserters in Finland (*Barents Observer*, 9 June 2026):** their war jokes are intact, but **the
      humor dissolves when they talk about command brutality** — jokes about the war survive, jokes about *why they
      left* do not (`11d` D1). The closest verified rule for a *principled* defector.
    - **Belenko** (MiG-25 defector, 1976): a documented taste for bold practical jokes, aimed at his former side and
      at his own new dependence (`11d` D4). **Dovlatov** (ex-camp-guard turned émigré writer): deadpan,
      self-deprecating, humor intact (`11d` D3). **North Korean defector performers:** the *register* of humor is
      learned in the institution and has to be re-learned after leaving (`11d` D5).
    - **Exile humor is a community-maintaining practice** (Lithuanian displaced-persons camps; displaced Timbuktu
      residents) — which matters for a man who has **no unit left to share the jokes with** (`11d` D7).
    - **The defector can also be the butt of the joke** (Syrian protest banners, **unverified**).
    - **Missing:** a verified first-person defector humor source. Memoirs listed but unopened are in `11d` §4 item 3.
11. **How it ages.** Elderly WWII veterans: in combat, humor was an immediate coping device; in old age it becomes
    "a search for meaning" (Moran 2008, `11a` B15). Timing governs permission: Vietnam produced little comic work
    for decades because of guilt and anger still in the culture (Abrams, `11d` A4).
12. **Not every joke is a trauma response.** Norwegian soldiers' deployment was sometimes simply *fun*, and the fun
    faded as risk and responsibility rose (`11a` B9). Boredom is a generator (`11d` A10). Writing every quip as
    symptom is its own cliché.
13. **Humor treats the dead as people.** British MoD obituaries remember a dead soldier's service humor as part of
    the eulogy (`11a` B7), and the humor of the dead is a standard way a unit remembers them — usable in memorial
    scenes.

**How this connects to file `07`.** The moral-injury material (Findings 185–205) says a man like the defector
should not be talked out of self-blame with "it was war" (Finding 201); the growth chapter's "expert companion"
(Finding 251) and the separation-as-risk finding (Finding 183) sit next to items 8–10 here. Humor can coexist with
all of it — and per item 9, **its disappearance is the signal a companion would notice.**

---

## 3. Read first (combined, de-duplicated; ordered by yield for this character)

Free unless marked.

1. **Johais 2025, "Schlagfertigkeit. A soldier skill," *Critical Military Studies*** — open access PDF
   (`https://cmi.no/publications/file/9509-schlagfertigkeit-a-soldier-skill.pdf`). Best single map of what soldier
   humor does; its reference list is the way into the rest of the field. *(Read in full by two researchers.)*
2. **Molendijk 2025, "Humor in dirty work…," *Public Anthropologist*** — open (`https://hdl.handle.net/2066/317974`).
   The best account of *what military humor is* and where it turns rotten; written by a moral-injury scholar.
3. **Yoshimura et al. 2024, "Sanity through Insanity," *Behavioral Sciences*** — free on PMC
   (`https://pmc.ncbi.nlm.nih.gov/articles/PMC11351593/`). The only open empirical study of veterans' dark humor
   *after* service; the corrective to the "charming wounded wisecracker."
4. **"If it stops, then I'll start worrying" (Dangermond et al. 2022, *Humor*)** — repository page and abstract
   free. Who/when/how often; the funny man going quiet as a distress signal; concealment from outsiders.
5. **Levy & Erony, "War Jokes Wanted: No Laughing Matter" (VVAW)** with the Levy–Bao Ninh interview — free, short,
   contains actual joke texts, and states the rule that the humor works inside the unit and repels civilians.
6. **The Wipers Times** (full run, `https://archive.org/details/wiperstimes`) **and The Anzac Book**
   (`https://www.gutenberg.org/ebooks/70441`) — soldier-made originals showing the deadpan-over-horror mechanic.
7. **Phil Klay interviews** (*Image Journal*; *Mother Jones*) — "humorous and serious at once"; the funny version
   versus the sad version. **Heller** (Koval interview) — build-up; and the **Blackadder** target principle.
8. **The *Army of Two* postmortem** (`11d` B8) **with the Spec Ops: The Line thesis** (`11d` B7) — the designer's
   own account of the quip-after-the-kill failure and why banter needs visible wear.
9. **The *Barents Observer* deserters piece (2026)** — the only verified instance of deserters' actual gallows humor,
   with the topic where it stops.
10. **Buzzell's CBFTW blog** with **Gallagher's Q&A** — modern grunt voice, unedited, plus the stated writing
    problem. **Terminal Lance** (free comic archive) and **Duffel Blog** (partly paywalled) for current registers.
11. **Mercer, Morgan & Lotto 2024** (paramedics, free) **and Anders et al. 2025** (police, free) — practitioners'
    own sense of the line, and the strongest quantitative warning.
12. **Tuleja & Eliason, *Warrior Ways* (2012)** — the book-length U.S. military folklore treatment, including jokes
    (library; full PDF restricted). **Lydia Fish's Vietnam folklore bibliography** (free) as a finding aid to the
    actual folk artifacts (songs, copier sheets, graffiti, short-timer calendars). **Pinkston 2018** (free thesis on
    Iraq/Afghanistan combat humor) and **Madsen 2013** (Texas A&M thesis; blocked to the tools — try a browser).

---

## 4. Real veterans: legitimate routes (research only — **no one was contacted, nothing was posted**)

The developer noted that getting the voice right may mean **seeking out people with former-military backgrounds
directly**. Whether and how to do that is the developer's call; these are the verified routes, with the researcher's
ethical-approach conclusions (`11c` §2).

- **Observe before asking.** Public, ticketed veteran comedy shows are produced for an audience, so watching them
  needs no one's consent. **Time-sensitive: ASAP's Comedy Bootcamp public graduation shows run Oct 20 to Nov 17, 2026**
  (DC, Indianapolis, Hampton Roads, San Antonio, San Diego, virtual; $5-$10). Combat Zone 360 lists shows Nov-Dec 2026.
  Also active: Rapid Fire Comedy Tour, Irreverent Warriors, VET Tv, Duffel Blog (takes tips and pitches), Terminal
  Lance (Max Uriarte; recent podcast interviews on dark humor, April and May 2026).
- **Hire through institutions, not cold contact.** Veterans in Media & Entertainment (searchable member directory and
  consulting), the Military Writers Society of America (open to non-veterans who write about the military; $50/year),
  the U.S. Veterans' Artists Alliance directory, the Writers Guild Foundation veterans program (through the foundation
  only). Military Experience & the Arts, Warrior Writers and the Veterans Writing Project publish veteran-authored
  work that can be read immediately.
- **Scope the ask to culture and voice, not operations.** Game-industry military advisors found are oriented to
  weapons, tactics and dialogue accuracy, so a brief must **ask explicitly for a humor-and-voice read**. The EA
  *Medal of Honor* consultant controversy (2012) is the vetting lesson.
- **Do not post in veteran communities unannounced.** Reddit rules could not be read (the site blocked the tools),
  so they are **unverified**; the indirect evidence is that research posts need moderator approval. Default to
  reading only.
- **Caution from the field:** when Vietnam-veteran activists asked veterans for war jokes, most sent sanitized
  material — **soliciting jokes from strangers yields cleaner, less true material than watching what veterans make
  for each other.** Pay veterans as contributors and authors, not as sources to be mined.
- **Academics worth knowing about** (public institutional pages only): the WARFUN project at the Chr. Michelsen
  Institute (Johais), Eliason (BYU, folklore), Yoshimura (U. Montana), Bjerke & Rones (FFI). A UK veterans-humor study
  (Plymouth) closed recruitment Feb 28, 2026 — look for its findings later; do not apply as a participant.

---

## 5. Gaps and what needs a human at a normal browser

Blocked or unread (details and exact URLs in the detail files' open threads):
- **Library of Congress Veterans History Project** (123,000+ narratives) and the LOC Folklife post "Cutting the
  Tension — VHP Narrators' Cracks, Jokes and Quips"; **Imperial War Museum** sound archive; **Texas Tech Vietnam
  Archive**; **Army University Press** "Comedy in Combat Culture" (*Military Review*, Sept-Oct 2023); Madsen 2013;
  Rowe & Regehr 2010 (the standard emergency-services review; paywalled); Obrdlik 1942 (paywalled).
- **Not found at all:** a scholarly source on Vietnamese-side or Soviet-army soldier humor; Hebrew- and
  Russian-language primary humor (all searches were in English); any veterans group inside the game industry; any
  organized military sensitivity-reader network; developer commentary on Boone's humor; verified Reddit rules.
- **Named by the researchers as worth opening next:** Tim O'Brien (no humor-specific primary source was opened);
  defector/deserter memoirs (Whitmore, Proctor, Key, Suvorov, Belenko's *MiG Pilot*, Haig-Brown's oral histories);
  the GI underground press and the *FTA* show (humor by members who broke with the institution while still inside);
  Hašek and *Švejk*; podcasts where veterans give examples (titles only so far).
- **Citation quirks to respect:** Molendijk dates Rowe & Regehr 2019 (true year 2010); sources disagree on author
  order for the 2021 Ward/Brown PTSD study; two statistics from search summaries (71% of ambulance staff using dark
  humor; about 90% of 608 paramedics) could not be traced and were **not used**.

---

## 6. Suggested next steps — **for the developer to approve; none started**

1. **A browser pass** over the blocked items in §5 (the LOC VHP keyword searches "joke", "humor", "prank",
   "nickname" filtered by war are the highest-value single task).
2. **An extraction pass** on the top free full texts in §3 (Johais, Molendijk, Yoshimura, Mercer, Anders, Levy &
   Erony, a sample of The Wipers Times, the Klay interviews), written up in the same own-words, finding-numbered
   style as files 01–10, as a new file `12_*`. This is what would actually put "real source material in hand"
   per the checklist's condition.
3. **Russian- and Hebrew-language queries** for the soldier-humor gaps; and the defector/deserter memoirs.
4. **If the developer wants direct veteran input:** attend or stream one public veteran comedy show first; then,
   once a draft exists, commission a paid humor-and-voice read through VME or a comparable institution.
5. Keep the checklist's guard: **no voice synthesis for the defector** until step 1 or 2 (or direct input) is done.
