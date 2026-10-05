# City renames — alias table and sweep report (2026-10-03)

**Read this first if a file still says an old name.** Eight cities were renamed in two batches (batch 1 = §1–§6; **batch 2 = §7**, added the same day). Four cities were renamed in batch 1 by developer ruling on 2026-10-03 and the names were swept through the live canon in **one** sweep, as the developer ordered (*"Wait until all four names are settled, then just do one single sweep"*). Files that are **records, quotes, or frozen inputs** were deliberately left with the old names; **this table is how to read them.**

## 1 · The four names

| Old name (and placeholder) | New name | Ruling | Founders (unchanged) |
|---|---|---|---|
| `{{ Abowasa }}` / Abowasa | **Santa Luce** | `DR-36` | Italy and the CIN, jointly (`DR-22`) |
| Sayowa (`{{ Syowa/Showa }}`) | **Temirötkel** (темірөткел), "Iron Crossing" | `DR-37` | the CIN or Kazakhstan (open), then Kazakh industrialists (`DR-30`) |
| `{{ Princess Elisabeth }}` | **Utstein** (English/national) · **Utsteinen** (native) | `DR-38` | the Scandinavian Trade Union nations (`DR-22`) |
| `{{ Bunger Hills City }}` | **Relung Panen** | `DR-39` | Indonesia and Malaysia, jointly (`DR-34`) |

Derived names: **the Temirötkel Junction** (was the Sayowa Junction) · **the Temirötkel Spur** (was the Sayowa Spur) · **the Relung Panen Spur** (the Casey spur).
**Not renamed:** the real stations and features: Syowa Station, Aboa Station, Wasa Research Station, Princess Elisabeth Antarctica, Utsteinen nunatak, the **Bunger Hills oasis**, **Princess Elizabeth Land**.
**In-game use of Utstein vs Utsteinen** is not ruled; the sweep used **Utstein** everywhere.

## 2 · What was changed (181 files in scope, 170 changed)

- **~1,300 replacements** of the old city names, in the Specs, Local_Cultures, Local_Robot_Culture, City_Vision_Notes, City_Enneagram_Personalities, the city catalogs, the relationship and roster files, the Division-of-Industry analysis files (except the held ones), Highways / Airports / Ports, the DLC questline candidates, the Concordia district reference files that name them, the factions file, the character files that name them, and the maps.
- **Placeholder braces removed** (`{{ ... }}` → the new name; ~96) and obsolete "placeholder / not yet named" flags rewritten.
- **Real-station phrases kept** ("Princess Elisabeth Antarctica", "Princess Elisabeth Station", "Princess Elisabeth of Belgium").
- **City names joined by slashes** ("Hub/Sayowa", "Neumayer/Princess Elisabeth") were replaced; paths were not.
- **A rename notice** was added under the title of every file in each city's own set (spec, culture, robot culture, vision notes, enneagram, catalog).
- **22 narrative lines in the cities' own files were kept on purpose**: lines that tell the story of the *old* name (Sayowa's Syowa/Shōwa etymology and Japanese founding; Abowasa's Aboa + Wasa fusion and Finnish-Swedish founding). They are **revisit items** already queued (`DR-30`, `R-11`, `R-16`, `R-17`, the Register's revisit list), and the notices at the top of each file say so. The spec name lines (`Tepenian city name`, `Significance`) were rewritten by hand.

## 3 · File and folder renames (23)

| Old path (under `Cities/` unless noted) | New path |
|---|---|
| `Specs/Halley subnet/Abowasa.md` | `Specs/Halley subnet/Santa_Luce.md` |
| `Specs/Halley subnet/Princess_Elisabeth.md` | `Specs/Halley subnet/Utstein.md` |
| `Specs/Mawson subnet/Sayowa.md` | `Specs/Mawson subnet/Temirotkel.md` |
| `Specs/Mirny subnet/Bunger_Hills_City.md` | `Specs/Mirny subnet/Relung_Panen.md` |
| `Local_Cultures/Halley_Subnet/Abowasa.md` · `Princess_Elisabeth.md` · `Local_Cultures/Mawson_Subnet/Sayowa.md` | `…/Santa_Luce.md` · `Utstein.md` · `…/Temirotkel.md` |
| `Local_Robot_Culture/Halley_Subnet/Princess_Elisabeth.md` · `…/Mawson_Subnet/Sayowa.md` | `…/Utstein.md` · `…/Temirotkel.md` |
| `City_Vision_Notes/Abowasa.md` · `Princess_Elisabeth.md` · `Sayowa.md` | `…/Santa_Luce.md` · `Utstein.md` · `Temirotkel.md` |
| `City_Enneagram_Personalities/Halley_Subnet/Abowasa.md` · `Princess_Elisabeth.md` · `…/Mawson_Subnet/Sayowa.md` | `…/Santa_Luce.md` · `Utstein.md` · `…/Temirotkel.md` |
| `Neo-Races-and-Cultures/Halley_Subnet/Abowasa/Abowasa_Catalog.md` | `…/Santa_Luce/Santa_Luce_Catalog.md` |
| `Neo-Races-and-Cultures/Halley_Subnet/Princess_Elisabeth/Princess_Elisabeth_Catalog.md` | `…/Utstein/Utstein_Catalog.md` |
| `Neo-Races-and-Cultures/Mawson_Subnet/Sayowa/Sayowa_Catalog.md` | `…/Temirotkel/Temirotkel_Catalog.md` |
| `Cities/Bunger_Hills_City/` (README, Development_Brief, Climate, ULM_Input_Status) | `Cities/Relung_Panen/` |
| `Cities/Bunger_Hills_City_Dossier_2026-10-03.md` | `Cities/Relung_Panen_Dossier_2026-10-03.md` |

File names use plain ASCII (`Temirotkel`); the official romanization in text is **Temirötkel**.
Path references to these files in the living reference docs were updated (Developer_Ruling_Queue, Extent_and_Density_Per_City, Extent_and_Area_APPROACH). **References in the records below still use the old paths** and will not resolve; use this table.

## 4 · What was NOT changed, and why (old names remain on purpose)

| Class | ~Files | Why left |
|---|--:|---|
| **Held: required reading of the in-flight Mirny T8 pass** | 6 | `Official_Population_Census.md` and `Division_of_Industry/09, 10, 11, 13, 16`. The Mirny pass quotes them and its readers prove them line by line; edits mid-pass break the proofs (`feedback_freeze_inputs_during_t8_round`). ✅ **Developer ruling 2026-10-03: sweep them AFTER the Mirny pass finishes.** The tool is ready: `Universal_Location_Methodology/Tools/rename_sweep_held_files.py` (dry run by default; `--apply` backs the files up to `Archive/` first). The reminder is in `MASTER_Process_Tracker.md`'s `📍 RESUME HERE` block |
| **Pass records** (Shirayuki, Sinheung, Zhongshan, Mirny frame, the four cities' pass folders and follow-up questions) | 26 | frozen, T8-cleared records that quote sources verbatim |
| **Background-Lore vignettes** | 64 | not canon, and **never edited** (`feedback_background_lore_vignettes_not_canon`); redo after the ULM |
| **Megasheets** (`City_Megasheets/`) | 73 | to be rewritten after the ULM, never edited (`feedback_dont_edit_megasheets`) |
| **Archive** | 35 | archived records |
| **Audit, tracker and log files** | 19 | history: Station_Heritage_Removal_Tracker, Full_City_Integrity_Check, ULM_Files_Mistake_Audit, Investigation_Loop_Round2_Tracker, National_Origin_Composition_Audit, DONE/TODO, the Local_Robot_Culture_Methodology digests, Neo-Races `_Method` trackers, and similar |
| **ULM method documents and trackers; rulings log; test runs; Canon Gap queue** | ~21 | verbatim developer quotes and dated findings; the rulings log keeps old names inside quotes (`DR-30`, `DR-32`) |
| **Research logs, `.t8_*` reader files** | 8 | records |
| **Concordia district work** (Staging, Deep_Dives, District_Megasheets, Final_Megasheet_Data_Processing) | 18 | district-method outputs and megasheets; the Hub district's "Sayowa reading" is a district record |
| **Real-world research and the BAS climate READER files** | 6 | real stations keyed by their real names (`READER/Sayowa.md`, `READER/Princess_Elizabeth.md` hold Syowa and Princess Elisabeth Antarctica data) |

## 5 · Open items this sweep created

1. **Demonyms.** "Sayowan", "Abowasian"/"Abowasan" and any "Princess Elisabethan" are unchanged, because no new demonyms are ruled. Needs the developer.
2. **Utstein or Utsteinen in-game** (which contexts use which form).
3. **Relung Panen's Malay form** ("Relung Tuaian") and its pronunciation, `DR-39`.
4. **The 22 protected lines** and the cities' founding text written around the old founders (Japan, Finland and Sweden, Belgium) are revisit items, not part of the rename.
5. **The 6 held files** (above).
6. **Graph rebuild** (`graphify`) is still on hold; it still indexes the old names.
7. **Nothing is committed.** `git status` shows the sweep as unstaged changes (23 renames recorded by `git mv`, ~190 modified files).

## 6 · Verification run

- Residual old names in the swept files: only the 22 protected lines, real-station and namesake references, "Princess Elizabeth Land", paths to the unrenamed megasheet and Background-Lore folders, and the demonyms.
- `Tools/quotation_audit.py` on the Mirny pass after the sweep: 80 not-found quotes, **none involving any of the four cities** (old or new names).
- Maps re-rendered with the new names (previous set archived under `working-stash/archive/`).
- Pre-sweep copies of every touched file were saved in `backup_before_sweep.tar.gz` in the session scratchpad (outside the repo).

---

## 7 · BATCH 2 (`DR-40`–`DR-43`, same day): four more names

| Old name | New name | Ruling | Meaning | Founders (unchanged) |
|---|---|---|---|---|
| Port Lockroy | **Puerto Abrigo** | `DR-40` | Spanish, "sheltered harbor" | Chile first (`DR-34`) |
| Juan Carlos | **Pergamino** | `DR-41` | Spanish, "parchment" (also a real city in Buenos Aires Province, a coincidence, not an input) | Uruguay first (`DR-34`) |
| Sejong | **Contrapunto** | `DR-43` | Spanish, "counterpoint"; in Chile, Argentina and Uruguay also a verse duel between two improvising poets | Chile first, then English-speaking arrivals, Palmer City, Korea as translators (`DR-35`) |
| Vostok | **Ariun Nuur** (Ариун Нуур) | `DR-42` | Mongolian, "the pure (or holy) lake" | Künnarantaiga and Mongolia (`DR-35`) |

⭐ **The central scientific district inside Ariun Nuur keeps the name "Vostok"** (`DR-42`), in honor of the scientists of the past. Its boundaries are not set. **Not renamed:** Vostok Station, Lake Vostok, King Sejong Station, King Sejong the Great, Sejong City, King Juan Carlos I, the Juan Carlos I Station, Port Lockroy (the real base, harbor and bay), Operation Tabarin.

**What was done (non-held files only, as the developer ordered):** 214 files in scope, 208 changed; ~1,800 name replacements (Port Lockroy 332, Juan Carlos 332, Sejong 476, Vostok 669, counted per line rule); 114 path references remapped; 40 slash-joined city lists replaced. **24 own-set files got a rename notice** (spec, culture, robot culture, vision notes, enneagram, catalog, per city); the four spec `Significance` lines were rewritten by hand. **35 narrative lines in the cities' own files were kept on purpose** (the Tabarin/museum story, the king namesakes, the Hangul naming story, the Soviet/Russian reputation); they are revisit items. **Files renamed with `git mv` (24, plus 4 Neo-Races folders):** `Specs/Palmer subnet/{Port_Lockroy→Puerto_Abrigo, Juan_Carlos→Pergamino, Sejong→Contrapunto}.md`, `Specs/Mirny subnet/Vostok.md → Ariun_Nuur.md`, and the same four names in `Local_Cultures`, `Local_Robot_Culture`, `City_Enneagram_Personalities` (each under its subnet folder) and `City_Vision_Notes`; `Neo-Races-and-Cultures/<Subnet>/<Old>/<Old>_Catalog.md → <New>/<New>_Catalog.md`. Left untouched: pass-record and concept-art folders (`City_Development_Passes/.../Vostok`, `Juan_Carlos`, `Port_Lockroy`, `Sejong`; `City_Concept-Art/...`), `Reference/Real-World/Vostok_Genetics_Research/` (real-world research), Background-Lore, megasheets, the BAS READER files, the Concordia district work, and every record class in §4.

**Still held:** the same 6 files, now with **both** batches. `Tools/rename_sweep_held_files.py` has been extended and dry-run (it covers all eight names). **After the Mirny pass finishes, run it once.**

**Verification:** residual old names outside the cities' own files: nine lines, all file-path references to unrenamed megasheet and Background-Lore files, or the demonym "Sejongite". `Tools/quotation_audit.py` on the Mirny pass: 80 not-found quotes, unchanged from batch 1, none naming any of the eight cities. Maps re-rendered (`Reference/Images/Maps/working-stash/`; previous set archived). Pre-sweep copy: `backup_before_sweep2.tar.gz` in the session scratchpad.

**Open items from batch 2:** demonyms (Pergamino, Puerto Abrigo, Contrapunto, Ariun Nuur; "Sejongite" and "Vostokan/Vostokian" belonged to the old names); native-speaker checks of Chilean and Rioplatense slang for *abrigo*, *pergamino* and *contrapunto*; whether "Ariun Nuur" is written with or without a hyphen; the district's boundaries; the cities' founding and namesake text written around the old names (revisit items); Mirny's own rename ("eventually").
