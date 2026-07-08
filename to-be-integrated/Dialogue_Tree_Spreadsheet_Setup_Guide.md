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

## Next step

Once a blank sheet is set up this way, the next step is filling in a first real topic block for one of Inner Tepenia's own characters as a worked example, then (when ready) converting a completed sheet into the game's actual dialogue data format.
