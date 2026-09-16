# Tier U Reference — Robot Religions Roster

> **Corpus-wide constant, identical for every city.** Source: `Worldspace/Factions/Robot_Religions/`, directory
> enumerated and both religions' identity sections read 2026-09-15. **⛔ The roster is OPEN — new religions may
> be added; neither city-siting nor completeness is implied by this list. A zero match for a given city is
> always a legitimate result, never evidence the roster is exhausted or empty.**

## The current roster — 2 religions, 6 files total

**Polydimensional Animism** — status: *"functional working copy, not locked final design canon."* 5 files
(`README.md`, `Beliefs.md`, `Rituals.md`, `Culture.md`, `Open_Questions.md`). Carries the established **Robot
Death Doctrine** and a **"Death as Change of Vantage"** doctrine — cross-ref
`Corpus_Reference_Sheets/Robot_Physiology_Quick_Reference.md`'s own death/ossuary section, which notes robot
death is handled by religion and community rather than a professional trade.

**Cymatics Reverence** — status: *"placeholder name, early development."* 1 file. Reveres sound and vibration;
doctrinal root is a real, structural robot physiology fact — robots perceive sound/vibration across a
meaningfully wider range than humans, not a trained sensitivity. Central claim (whether treated as
science-in-progress or purely sacred/non-literal) is explicitly unresolved by design.

## How to check a specific city

`grep -rl -i "<city name>" Worldspace/Factions/Robot_Religions/` — **do not just check whether the directory
has files.** The roster's own existence is a corpus-wide fact (this file); a per-city datasheet's own job is
checking whether either religion NAMES that city specifically, which is a separate and much narrower question.
⛔ **A "the directory is empty" claim without actually enumerating it is a documented failure mode — caught
2026-09-15 after surviving uncorrected in one city's own datasheet.**
