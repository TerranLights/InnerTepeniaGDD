# Dark Humor Research — Extraction Checklist (source of truth)

*Updated 2026-10-06. Folder purpose and rules: `README.md`. Agent rules: `extractions/_AGENT_INSTRUCTIONS.md`. Withheld/denied items for the Opus retry: `Content_Filter_Denials_Log.md`. Tier C list for the developer: `Tier_C_Shopping_List.md`. Exact queries and dead ends: `search_logs/`. Manifest: `source_manifest.json` / `.csv`. Everything here is research, NOT canon; no character voice has been written.*

## 1. Status in one line

**First pass complete for Tiers A and B: 38 extraction files, 2,259 numbered findings, about 741,000 words (plus E26a/E26b, Sassoon's *Memoirs of an Infantry Officer*: 91 + 88 findings, so 40 files and 2438 findings in all).** **Cross-source synthesis done 2026-10-06: `extractions/synthesis/00_PATTERN_SYNTHESIS.md` and lens files S1-S5.** Next: the developer's Tier C fetches, the Opus retry of withheld items, and the optional second harvests in §6.

## 2. Collected (raw text in `source_texts/`, git-ignored)

| Group | Collected | Extracted in |
|---|---|---|
| Tier A open-access scholarship (38 items) | yes (manifest `AC-*`) | E01-E07 |
| Tier A public-domain WWI: Wipers Times 1930 omnibus (`PW-01`), Anzac Book, Bairnsfather, Sassoon, Graves, Songs and Slang | yes | E08-E12, E15 |
| Tier A Richards memoir (`PW-07`; U.S. copyright status uncertain, treated as copyrighted) | yes | E13 |
| `PW-02` Wipers Times 1918 edition | yes | **not extracted on purpose**: an earlier, noisier reprint of the same issues (no "Better Times"); use only to cross-check OCR in `PW-01` |
| Tier A web articles (`WA-001`…`WA-096`) | yes (96; WA-092/093 duplicate 051/052) | E21, E22a, E22b, E23 |
| Tier A Buzzell CBFTW blog (72 posts) | yes | E18. **Caveat:** only about 3 of the 72 posts are his own connected prose; the rest are pasted press and one-liners (he deleted the original archive in 2004). |
| Tier A Terminal Lance (all 1,000 listed titles + 60-page sample, 57 images) | yes | E19. **The title list looks truncated and the sample is biased toward serious topics.** |
| Tier B Rutgers (40 transcripts, 140 passages) | yes | E24a |
| Tier B AWM (40 transcripts, 55 passages) + Witness to War docs (14 docs, 21 passages; 50 video descriptions) | yes | E24b |
| Tier B other archives (NY State Military Museum, Korean War Legacy, VAC, Army CSI, USMCU, Alabama) | yes (about 102 passages) | E24c |
| Tier B UNSW Australians at War (40 transcripts, 172 passages) | yes | E24d |
| Tier B modern veteran writing (103 files, about 199k words) | yes | E25a-E25e |
| Tier B Wisconsin Veterans Museum (40 transcripts, 214 passages) | yes | **HELD, NOT EXTRACTED**: robots.txt disallows named AI crawlers and terms bar copying; awaiting the developer's decision |
| Tier B StoryCorps | **not harvested** (Terms of Use prohibit scraping) | Tier C list C-80 |

## 3. Extractions done (`extractions/`)

| Unit | Source | Findings |
|---|---|---:|
| E01 | core military-humor scholarship (Johais ×2+blogs, Sløk-Andersen, Tidy) | 65 |
| E02 | other armies and wars (Indian Army, Norway, Gallipoli, Vietnam songs, small items) | 44 |
| E03 | humor under extreme peril and in exile (genocide, Ukrainian memes, DP camps) | 41 |
| E04 | veterans, PTSD and reintegration studies | 37 |
| E05 | occupational humor and theory (Kuiper, Sliter, Bitterly, ambulance review, Freud, Vonnegut essay) | 55 |
| E06 | Pinkston and Jensen theses | 50 |
| E07 | Gregory thesis on WWI cartoons | 50 |
| E08, E09a, E09b1-b3, E10a, E10b | The Wipers Times, whole run (lines 1-37,164) | 86 / 60 / 29 / 36 / 32 / 88 / 92 |
| E11a, E11b | The Anzac Book, Bairnsfather, Sassoon | 69 / 64 |
| E12a, E12b | Songs and Slang of the British Soldier | 72 / 57 |
| E13a, E13b | Richards, *Old Soldiers Never Die* | 83 / 157 |
| E15a, E15b, E15c | Graves, *Good-bye to All That* (E15c: the best post-war evidence) | 53 / 131 / 93 |
| E18 | Buzzell CBFTW blog | 35 |
| E19 | Terminal Lance strip sample (visual) | 60 |
| E21 | veteran comedy and satire web sources | 41 |
| E22a, E22b | authors on war humor; screen, games and consulting | 65 / 37 |
| E23 | defector, exile, cross-cultural and slang web sources | 47 |
| E24a, E24b, E24c, E24d | oral-history passages: Rutgers; AWM + Witness to War; other archives; UNSW | 30 / 41 / 33 / 43 |
| E25a-E25e | modern veteran writing: MEA/ODT; Sandbox/milblogs; War Horse/Havok/T&P; transcripts/NPR; Fox thesis memoir | 57 / 55 / 37 / 47 / 87 |
| E26a, E26b | Sassoon, *Memoirs of an Infantry Officer* (1930; autobiographical novel; E26b holds the protest statement and its handling: dissent from inside) | 91 / 88 |

## 4. Open items and flags

1. **Content-filter retry (Opus).** `Content_Filter_Denials_Log.md`: Part A (2 outright denials, both on the Wipers Times), Part B (15 hand-entered items), Part B2 (auto roll-up of every file's register; re-run `python3 extractions/_rollup_register.py` after any new extraction). E09b1's Rubaiyat of the Kaiser (`PW-01` L20,713-20,836) is the likeliest trigger.
2. **Wisconsin Veterans Museum:** hold (see §2). The scratch copies of all 957 transcript PDFs from the harvest are temporary files in the session scratchpad; delete them if you decide against WVM.
3. **Stale temp file:** `/tmp/e10a_backup_pre_sed.md` (a backup an agent could not delete). Safe to delete by hand.
4. **Tier C:** `Tier_C_Shopping_List.md` is current through the Tier B harvests (Section 7). Files dropped into `Tier_C_Dropbox/` need inventory, a manifest row and an extraction unit.
5. **E01 findings E01-62 to E01-65** came from a live fetch of the AC-26 blog post (paraphrase only); the real blog text is now local (`source_texts/academic/AC-26_*`): re-verify.
6. **Licence note:** `AC-31` (Freud 1928, "Humour"): the text copy ends with a notice that the English translation is copyright-protected until 2032; the manifest said public domain. Short quotations only (E05 did this).
7. **Manifest corrections to make:** `AC-26` URL (now `publicanthropologist.cmi.no/2025/05/21/international-joking-relationships/`); `PW-07` is a proofread eBook (fadedpage/Distributed Proofreaders Canada), not raw archive.org OCR; `MV-CBFTW-*` note about press clippings; `AC-24` not collected; Terminal Lance title list truncated.

## 5. Next steps (in order)

1. ✅ **Cross-source pattern synthesis: DONE 2026-10-06** (`extractions/synthesis/`: `00_PATTERN_SYNTHESIS.md`, `S1…S5_*.md`; 227 patterns, evidence-tagged; candidates only, **no voice, no sample dialogue**). **E26a/E26b folded into `S4` (addendum: patterns S4-P45…P64) and the master synthesis, 2026-10-06.**
2. **Developer's Tier C fetches** (§4.4) → extraction units `E26+`.
3. **Opus retry** of the withheld items (§4.1).
4. **Optional second harvests** (§6).
5. When the synthesis and Tier C are in: decide with the developer whether and how to ask real veterans (see `../PTSD_Military_Trauma_Research/11_Dark_Humor_Source_Leads.md` §4) and only then draft any character voice, as candidates.

## 6. Optional further harvests (named by the harvest agents)

- Terminal Lance: pull the trauma-related slugs the sample missed ("Dark Days", "Triggered", "Defense Mechanism", "It Catches Up to You", "Going Internal", "Left Behind") with the 10-second crawl delay.
- Buzzell's original 2004 posts: he deleted them; Internet Archive snapshots of `cbftw.blogspot.com` may hold them, but retrieving withdrawn text is the developer's call.
- UNSW: about 30 high-signal interviews never read in full; Afghanistan/Iraq not coverable there.
- VAC "Heroes Remember": 2,779 clip pages not fetched; KWLF: about 196 transcripts never matched a query.
- Marine Corps University career interviews (16 very large PDFs).
- Russian- and Hebrew-language queries; Vietnamese-side humor; defector/deserter memoirs (list in `Tier_C_Shopping_List.md` C-69).
- Brown & Penttinen 2013, "'A Sucking Chest Wound' Is Nature's Way of Telling You to Slow Down: Humor and Laughter in War Time" (*Critical Studies on Security* 1(1)): cited by two sources, not obtained (add to Tier C).
