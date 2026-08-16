# Text-Based Testing Harness

**Established 2026-08-16.** Answers a question the `00_Overview_and_Project_Structure.md` guiding principles
already implied but never made concrete: *"Build in layers — each system must be testable in isolation before
being wired to others."* This file is that principle turned into an actual plan for the game's interaction
logic specifically (dialogue, stat/skill/perk checks, combat, world state) — validate it as a numbered-menu
text interface, running in a terminal and a browser, before any camera/3D/graphics work gets built on top of it.
Revises the Build Order in `09_Build_Order_and_Key_Decisions.md` to put this first.

---

## The Core Idea: Same Code, Different Presentation Layer

This is not a throwaway prototype in a different language. Godot supports running headless (`godot --headless`
— no window, no rendering), which means a text-based version of the game is just **the real `MachineStats`,
`SkillSystem`, `DialogueManager`, `CombatManager`, `DistrictManager`, etc. classes, wired to a minimal
text-only front-end instead of the eventual 3D isometric scene.** Nothing about this needs to be reimplemented,
ported, or kept in sync with a separate "real" version later — it *is* the real version, running under a
different presentation layer. This is the same instinct behind the Godot Fallout Precedence Law already stated
in this folder's own README: prefer whatever's simplest to build and revise later over a clever solution that's
harder to change once real content sits on top of it. Building the actual logic classes once, validated headless
first, is that simplest path — a separate Python (or other) prototype would be the clever-but-harder-to-change
option, since it creates a second implementation that has to be manually kept faithful to the first.

**Two delivery targets, one codebase:**
- **Terminal:** `godot --headless`, reading player input from stdin, printing state/menus to stdout.
- **Browser:** the same project's HTML5 export target, with a bare `Control`-node scene (no 3D rendering
  enabled) standing in for the eventual isometric scene.

Both targets drive the identical GDScript/C++ logic classes that Phase 1 onward (see the revised Build Order,
below) eventually wires to the real camera/tilemap/combat-arena scenes.

---

## The Text Interface Paradigm

Established directly from the developer's own worked example. Every interaction type — dialogue, world
navigation, combat — renders as a **context header, a body block, and a numbered menu of actions**, and the
player responds by typing a number and pressing Enter. One shared component drives all of it (see
`TextInterfaceController`, below) regardless of which system is asking.

### Dialogue example (as specified 2026-08-16)

```
{{ Naizelle d'Edjordoś }}
1. Any suggestions on how to get this generator running?
2. [50 Repair] Why not just bypass the coupling? Should provide us with some light and heat until we come up with a better idea
3. [27/45 Narrative] Oh, come on. What's the worst that could happen?
4. [7/8 Investigation] Was it the yellow wire or the green wire? It was the yellow wire, I'm sure.
5. Go ahead and head back home for now. I'll see you after I get this working.
6. <leave>
```

**Format rules, generalized from this example:**

- **`{{ Character Name }}`** — the context header. For dialogue, the NPC currently being spoken to. Other
  contexts use their own header shape (see World and Combat, below) but the same double-curly-brace convention.
- **Numbered options, 1 through N, contiguous.** A player types the number and presses Enter to select.
- **`[<Stat or Skill Name>]` bracket, Checks only — display rule confirmed 2026-08-16, exactly matching
  Fallout: New Vegas's own convention, not a project invention:**
  - **Player's current value ≥ the requirement (would pass):** show the requirement only — `[50 Repair]`.
  - **Player's current value < the requirement (would fail):** show current, then required — `[17/50 Repair]`.
    Option 4 in the source example (`[7/8 Investigation]`) is exactly this case — a check the player would
    currently *fail*, phrased in-character as an overconfident wrong guess, still fully visible and selectable.
  - This is not cosmetic. The format itself is what tells the player, before committing, whether they'd pass —
    same information FNV's own colored/graded Speech checks convey, done here with plain text.
- **Checks are always visible, never hidden — this is what makes them Checks rather than Gates (see below).**
  Selecting a Check evaluates the condition and branches to a pass- or fail-specific response — the "two Topic
  rows sharing one trigger point" mechanic already established in
  `to-be-integrated/Dialogue_Tree_Spreadsheet_Setup_Guide.md`'s Conditions section, just surfaced here as what
  the player actually sees at the keyboard.
- **Gates (Perk possession, Trait possession, Reputation tier, quest flag, item, companion presence, Wild Child
  status) hide the option entirely if unmet — no bracket, no visible attempt, no feedback at all.** Confirmed
  directly, 2026-08-16: "if the player has some particular perk and/or trait and/or reputation-status, then the
  dialogue option appears. If not, then the dialogue option doesn't appear." Perks and Traits are gates, not
  numeric Checks, because there's no meaningful in-fiction way to attempt-and-fail possessing a Perk the way you
  can fail a Repair check. An option gated this way simply isn't in the list at all if unmet — the numbering
  stays contiguous over whatever *is* available, never skipping a number or showing a grayed-out entry.
- **Forbidden Trait is the one deliberate exception to "Gates are silent."** Already binding canon in
  `Companion_System.md`'s "Forbidden Traits" section (confirmed 2026-07-28), scoped to Romance Gate 2: if the
  player carries a companion's forbidden trait, the romance-eligibility interaction is never simply absent —
  it always surfaces the character's own distinct rejection line, evaluated *before* (and instead of) the
  ordinary stat-gate Check display, so the player understands why and can plan a future playthrough
  accordingly. Full syntax and precedence rule in
  `to-be-integrated/Dialogue_Tree_Spreadsheet_Setup_Guide.md`'s Conditions section — not reproduced twice here
  to avoid the two files drifting apart.
- **`<angle-bracket>` options are system actions, not spoken lines.** `<leave>` ends the conversation (the
  Goodbye Flag column, rendered). The same convention generalizes to any context: `<end turn>` and `<flee>` in
  combat, `<travel to Rothera>` in world navigation — anything that isn't a line of dialogue or an in-fiction
  action gets angle brackets so it's visually distinct at a glance from real content.

### World state example (extrapolated from the same paradigm)

```
{{ Rothera — Refuge District }}
A cramped, sturdy prefab block, snow-scoured on its windward face. Overhead cabling feeds three buildings from
a single generator that sounds like it's one bad week from failing entirely.

Present: Imelda Sánchez, [unnamed NPC — Repair Technician]

1. Talk to Imelda Sánchez
2. Talk to the Repair Technician
3. Examine the generator
4. [Investigation] Look for anything else worth noticing
5. <travel to Palmer City>
```

Same rules apply: header block, body description, numbered actions, checks shown inline, system actions in
angle brackets. "Who's in the area" is just another line in the body block, sourced from whatever
`DistrictManager`/location system already tracks as present.

### Combat example (extrapolated — full detail stays owned by `04_Combat_System.md`)

```
{{ Combat — Round 2 }}
AP: 4/6 | HP: 22/30 | Target: [hostile] Overclocked Sentry (NODE: Torso)

1. Move (1 AP/tile)
2. Attack — Torso [2 AP, 65% hit]
3. Attack — Head [3 AP, 40% hit, NODE: disable optics]
4. Use item
5. [Framejacking, 8 AP] Attempt to seize control
6. <end turn>
7. <flee>
```

Same paradigm again — this file doesn't redesign combat itself, just confirms the same numbered-menu interface
covers it without a separate UI convention.

---

## `TextInterfaceController` — the shared component

One node, not three separate implementations for Dialogue/World/Combat. Any system that needs the player to
choose from a menu feeds it a list of options; it handles numbering, check-annotation display, input, and
returns the selected option back to whichever system asked.

```gdscript
class_name TextInterfaceController extends Node

# One menu option, as fed in by whichever system (DialogueManager, CombatManager, etc.) is asking
class MenuOption:
    var label: String                    # the spoken/action text
    var check: CheckAnnotation = null     # null if this option has no stat/skill check
    var is_system_action: bool = false    # true renders in <angle brackets> instead of numbered dialogue text
    var payload: Variant                  # whatever the calling system needs back (a Topic ID, a combat action enum, etc.)

class CheckAnnotation:
    var stat_or_skill_name: String
    var current_value: int
    var required_value: int
    func passes() -> bool:
        return current_value >= required_value
    func display_string() -> String:
        # FNV's own convention, confirmed 2026-08-16: only show the requirement when it'd pass;
        # show current/required when it'd fail. Never the other way around.
        if passes():
            return "[%d %s]" % [required_value, stat_or_skill_name]
        else:
            return "[%d/%d %s]" % [current_value, required_value, stat_or_skill_name]

# Gates (Perk, Trait, Forbidden Trait, Reputation tier, quest flag, item, companion presence, Wild Child)
# never reach TextInterfaceController as a MenuOption at all when unmet — the calling system (DialogueManager,
# etc.) filters them out before building the options list, so there's no GateAnnotation class to render;
# an unmet Gate simply means one fewer MenuOption, not a hidden/disabled one.

signal option_selected(payload: Variant, check_passed: bool)  # check_passed is meaningless/ignored for non-check options

func present(header: String, body: String, options: Array[MenuOption]) -> void:
    # Renders header ({{ ... }}), body text, then numbered options (visible ones only —
    # gated-and-unmet options should already be filtered out of `options` by the calling system
    # before they ever reach this function; this controller only handles display + input, not gating logic).
    ...

func _on_input_received(selection: int) -> void:
    var option := _visible_options[selection - 1]
    var passed := option.check.passes() if option.check else true
    emit_signal("option_selected", option.payload, passed)
```

**Where this lives:** presentation-layer only — it has no opinion about dialogue trees, combat rules, or world
state. `DialogueManager`, `CombatManager`, and whatever handles world navigation each build their own
`Array[MenuOption]` from their own data (a dialogue sheet's Topic rows; a combatant's available actions; a
location's present NPCs/objects) and call `present()`. The 3D game's eventual real UI will replace this
controller's rendering with actual UI widgets, but the systems calling into it — `DialogueManager` deciding
which Topics are visible, `CombatManager` deciding which actions are legal — don't change at all. That's the
whole point: the swap happens at the presentation boundary, not inside game logic.

**Terminal rendering:** `present()` prints the header/body/menu to stdout; `_on_input_received` is driven by a
blocking stdin read loop.
**Browser rendering:** `present()` updates `Label`/`RichTextLabel` nodes in a bare `Control` scene;
`_on_input_received` is driven by button presses or a text input field, same signal either way.

---

## Where Dialogue Data Actually Comes From

This harness is the consumer, not the source, of dialogue content — the source is the `Dialogue/` tree and its
schema, both already established:
- Column schema, Conditions/Effects syntax, pass/fail-as-separate-rows convention, and the naming/folder
  standard: `to-be-integrated/Dialogue_Tree_Spreadsheet_Setup_Guide.md`
- The actual per-character sheets: `Worldspace/Characters/Dialogue/{Companions,Non-Recruitable_Romanceable,
  Named_NPCs}/`
- What's been written vs. still needed: `Worldspace/Characters/Dialogue/Character_Index.md` and
  `Dialogue_TODO.md`

`DialogueManager`'s job is straightforward given that schema: load a sheet (eventually the XLSX → JSON export;
directly from Markdown is fine for early harness testing before that conversion pipeline exists), track which
Topic ID is current, filter Topic rows by their Conditions column into visible `MenuOption`s (check-type
conditions become visible-with-annotation, gate-type conditions become invisible-if-unmet), hand them to
`TextInterfaceController.present()`, and on `option_selected`, follow that Topic's Next Topic column to advance.

**Implied but not yet decided:** `DialogueManager` doesn't currently exist in `01_Global_State_and_Autoloads.md`'s
Autoload Roster. Given dialogue needs to be reachable from any NPC interaction the same way `CombatManager`-style
systems do, it likely belongs there — flagged here rather than silently added, since `01`'s roster is that
file's own decision to make, not this one's.

---

## Open Items

- **The `[50 Repair]` vs. `[27/45 Narrative]` format inconsistency** in the original worked example — resolved
  here as "always show current/required," but worth an explicit confirm since it wasn't stated outright.
- **Location/"who's in the area" content** isn't an authored data type anywhere yet, the same way dialogue
  wasn't before this session. If the World example above is the right shape, it needs the same kind of
  schema-and-tracker treatment `Dialogue/` just got, once world-navigation content actually starts getting
  written.
- **Save/load and quest-flag state** (`07_Save_System.md`) aren't explicitly folded into this harness, but
  `Effects / Sets` in the dialogue schema already assumes quest flags and reputation deltas exist as trackable
  state — the harness will need at least a minimal in-memory version of that state (not full save-file
  serialization) to make Conditions/Effects actually mean anything during text testing.
