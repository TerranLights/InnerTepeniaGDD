# Dialogue Tree Spreadsheet Setup Guide (LibreOffice Calc)

Reference guide for setting up a dialogue-tree spreadsheet, based directly on `Example Doc - Pvt Merrick.xlsx` in this same folder (a real dialogue guide from a Fallout: New Vegas mod team). Written 2026-07-07.

**What this format actually is:** one row per line of dialogue, with columns for topic/response text, which NPC speaks it, which topic comes next, and any conditions gating that branch. There are no real "boxes" (borders) in the source file — what reads as boxes is just gridlines, bold headers, and alternating background shading used to visually separate one topic's block of rows from the next.

---

## 1. Set up the columns

Row 1, one header per cell, columns A through I:

| A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|
| Topic ID | TOPIC TEXT | RESPONSE TEXT | NPC | NEXT TOPIC | Conditions | Goodbye Flag | Random Flag | Say Once Flag |

Select row 1, then **Format → Text → Bold** (or Ctrl+B). That's the entire header styling — no fill color needed.

## 2. Set column widths

Right-click a column letter → **Column Width**. Roughly matching the source file:
- Topic ID: ~22
- TOPIC TEXT: ~26
- RESPONSE TEXT: ~50 (the longest text usually lives here)
- NPC: ~14
- NEXT TOPIC: ~25
- Conditions: ~27
- Goodbye Flag / Random Flag / Say Once Flag: ~12 each

## 3. Turn on text wrapping

Select the whole sheet (Ctrl+A), then **Format → Cells → Alignment tab → check "Wrap text automatically."** Without this, long dialogue lines run off the edge of the cell instead of wrapping to multiple lines.

## 4. Freeze the header row and Topic ID column

Click cell **B2** (one row down, one column over from the top-left corner), then **View → Freeze Cells → Freeze Rows and Columns**. Row 1 and column A now stay visible no matter how far down or across you scroll — essential once a dialogue tree gets long.

## 5. Shade alternating topic blocks

This is the "different colors" effect — just cell background fill, used to visually separate one topic's block of rows from the next:

1. Select all the rows belonging to one topic (e.g., rows 2–4 for a GREETING block).
2. Click the small arrow next to the paint-bucket icon in the toolbar (**Background Color**), or go to **Format → Cells → Background**.
3. Pick a light gray — the source file uses `#EFEFEF` (an almost-white gray). Use **Custom Color** and type that hex code for an exact match.
4. Leave the *next* topic's block unfilled (default white), then shade the one after that gray again — alternating gray/white down the sheet so each topic's block is visually distinct at a glance.

That's the complete visual system: no borders, no merged cells, nothing beyond bold headers, text wrap, alternating shading, and frozen panes.

---

## How the columns are actually used (from the source file)

- **Topic ID** — a unique identifier for this line, e.g. `RBJCMerrChat1`. Used elsewhere in the sheet's NEXT TOPIC column to link to it.
- **TOPIC TEXT** — what the *player* says (the dialogue option the player picks).
- **RESPONSE TEXT** — what the *NPC* says back.
- **NPC** — which character speaks the response.
- **NEXT TOPIC** — the Topic ID(s) this response unlocks or leads to. Can list multiple, space-separated, if a response opens up several new branches at once.
- **Conditions** — what has to be true for this branch to be available at all: a skill check (e.g. `Guns 35`), a quest stage, an item in inventory, a correct/incorrect trivia answer, etc.
- **Goodbye Flag** — marks a line that ends the conversation.
- **Random Flag** — marks a line as one of several that can be picked randomly rather than always the same one.
- **Say Once Flag** — marks a line that only plays the first time, then never shows again on repeat conversations.

---

## Inner Tepenia's Own Extensions to This Format

**Established 2026-08-15.** The 9-column format above is the source file's format, unchanged — it's the right
foundation per this project's own Fallout Precedence Law (`feedback_fallout_precedence_law` memory). This
section adds what stock FNV-style dialogue doesn't need but this project does: MACHINE-stat/trait/reputation
conditions, a way to record state changes, and a naming/folder standard for a roster of 40+ characters' worth
of trees rather than one mod's worth.

### The full column set (11 total)

The original 9, unchanged in meaning:

| Column | Purpose |
|---|---|
| Topic ID | Unique ID for this line — referenced by other rows' Next Topic |
| TOPIC TEXT | What the *player* says (the dialogue option) |
| RESPONSE TEXT | What the sheet's NPC says back, by default (see Speaker column) |
| NEXT TOPIC | Topic ID(s) this response unlocks |
| Conditions | What gates this branch being available at all |
| Goodbye Flag | Ends the conversation |
| Random Flag | One of several lines that can be picked randomly |
| Say Once Flag | Plays only the first time, never again on repeat conversations |

Plus 3 new columns:

| Column | Purpose |
|---|---|
| **Speaker (if not sheet NPC)** | Blank on almost every row — a sheet is already scoped to one NPC, so restating that name every row would be pure repetition. Only filled in for the exception: a companion approval-bark (`Companion: Imelda`), or a second voice in a rare multi-NPC group scene. |
| **Effects / Sets** | State this line changes on selection — reputation delta, Bond/Grief shift (`Fragmentation_Matrix.md`), quest flag, item grant, Mastery Dividend flag, etc. The abbreviated stand-in for what a full engine like GECK would put in a Result Script box. |
| **Notes (Dev)** | Scratch reasoning for the writer's own use. **Explicitly excluded from the eventual JSON export** — never touches implementation, purely an authoring aid. |

*(The "NPC" column from the source format is dropped, not just relocated — see the reasoning above; the sheet's own filename and folder already state which NPC it is.)*

### Conditions column — syntax convention

A light, consistent syntax, so this parses predictably into JSON later instead of needing free-prose
interpretation each time:

- Stat check: `Humanity >= 7` — full stat name, this project's 7 MACHINE stats (Might, Agility, Calculation,
  Humanity, Investigation, Nerve, Engine)
- Permanent-only check (Romance Gate 2's own binding exception, `Companion_System.md`): `Humanity(perm) >= 7`
- Forbidden Trait (categorical block, always wins over any stat threshold — see "Forbidden Traits" in
  `Companion_System.md`): `FORBIDDEN Trait: NoMercy`
- Reputation tier (`Reputation_System.md`): `Rep(Leo) >= Liked`
- Wild Child status (Idolized + Vilified simultaneously): `WildChild(Cancer)`
- Companion-perk bypass (e.g. Imelda's Charisma-check bypass while she's an active party member):
  `Companion:Imelda present`
- Multiple conditions on one row: `;` = AND by default; write `OR` explicitly when that's actually meant

**Pass/fail is not a separate column — it's two Topic rows.** A stat check gates which of two (or more) Topic
rows is available at all: one row conditioned `Investigation >= 7` leading to the sharper response, a fallback
row (no condition, or the inverse) leading to the plain one. This is how the real FNV source file already does
it, and it keeps this project's own "deterministic, no randomness" stat-check law (`Universal_Rules.md`)
naturally enforced by the format itself rather than needing a separate mechanic to express it.

### File naming and folder structure

**Location — one top-level `Dialogue/` tree, split by character category, with one folder per named
character:**

```
Dialogue/
├── Companions/
│   ├── Imelda/
│   │   ├── Imelda_Greeting.md
│   │   ├── Imelda_Quest_Step01.md
│   │   ├── Imelda_Romance_Gate2.md
│   │   ├── Imelda_Banter_PlayerLies.md
│   │   └── Imelda_Ambient_Rothera.md
│   └── Ayako/
│       └── ...
├── Non-Recruitable_Romanceable/
│   ├── Majyao/
│   │   └── Majyao_Greeting.md
│   └── Trisha/
│       └── Trisha_Greeting.md
└── Named_NPCs/
    └── [NPC Name]/
        └── [NPC Name]_Greeting.md
```

- **Companions/** — every recruitable Doll, matching `Still-Present_-_In-Game/recruitable/`, DLC-native
  companions included (Kendra, Maggie, Salagéa, Imelda).
- **Non-Recruitable_Romanceable/** — Majyao Bisyugota, Trisha Miller, and anyone later resolved this way out of
  the `unsure and_or special cases/` pool.
- **Named_NPCs/** — everyone else with actual dialogue: `Major_NPCs`, `Minor_non-Doll_NPCs`, and
  `District-Quest-NPCs` alike, Doll or not, one folder per named individual.

**Filename pattern:** `<CharacterToken>_<Context>[_<SubTag>][_<Sequence>].md`

- **CharacterToken** — the short name already used in that character's own README header (`Imelda`, `Hao`,
  `Ayako`), or the established role-identifier for a District-Quest NPC (`NPC-Leo-Grand-Faction-Leader`) where
  no personal name exists yet.
- **Context** — a small controlled set of tags:
  - `Greeting` — hub/idle/repeat-visit topics (happens once per character — no sub-tag needed)
  - `Quest_Step` — personal-questline beats (happens once per character; numbered — `Quest_Step01`,
    `Quest_Step02`)
  - `Romance_Gate2` / `Romance_Beats` — romance-specific dialogue (happens once per character)
  - `Banter_<Trigger>` — companion approval/reaction lines. **Needs a sub-tag, not just a number** — a bare
    `Banter_02` says nothing; name it for what triggers it (`Banter_PlayerLies`, `Banter_RivalCompanion`)
  - `Ambient_<Location>` — district/location flavor, not quest-tied. **Also needs a sub-tag** — keyed to where
    it plays (`Ambient_Rothera`, `Ambient_PalmerCity`)
  - `Ending_<Name>` — epilogue/final lines per ending
- **Sequence** — zero-padded two-digit number, only stacked on top of a sub-tag if one genuinely needs
  splitting across multiple files (unusual — normally multiple lines for the same trigger/location are just
  multiple rows in one sheet, using the Random Flag column for rotation).

The character token is kept in the filename even though the folder already states it — deliberate redundancy,
matching this repo's own dominant convention (e.g. `Davis_10_The_Harvest_Outgrows_the_Archive.md` still
restates "Davis" despite already living inside Davis's own folder). A sheet stays self-describing if it's ever
opened standalone, moved, or referenced by path in the eventual JSON export.

When a completed sheet goes through XLSX conversion, the same base filename just swaps extension
(`Imelda_Quest_Step01.xlsx`) — a direct one-to-one mapping, nothing to rename.

**Companion folder-tracking:** `Dialogue/Character_Index.md` (a running log of who currently has a folder here)
and `Dialogue/Dialogue_TODO.md` (status tracker: added+complete, added+incomplete, not yet added) are maintained
alongside this tree — see those files directly rather than duplicating their content here.

---

## Next step

Once a blank sheet is set up this way, the next step is filling in a first real topic block for one of Inner Tepenia's own characters as a worked example, then (when ready) converting a completed sheet into the game's actual dialogue data format.
