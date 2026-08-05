# Population Balancing Math — Dev Notes Only

**This file is not in-fiction. Nothing below is lore, and nothing below should ever be read as source
material for Historical Vignettes, Course of Events chains, quest design, or any other lore-generation pass.**
It exists purely to preserve the arithmetic history behind several cities' current census numbers, in case
that math ever needs to be independently re-verified or re-derived. The census figures themselves (the
tables, the totals, the per-nation tiers) all stay exactly as they are — only the in-line "how/why" narration
that used to sit in `Official_Population_Census.md`, `Upper_Earth_Immigration_Composition.md`,
`Specs/Palmer_City.md`, and `Local_Cultures/Palmer_Subnet/Palmer_City.md` has moved here.

**Developer-confirmed, 2026-08-06:** none of the mechanisms below ever happened in-fiction. There was no
in-world "population redistribution," no administrative decision, no dated relocation event any city's
citizens experienced. Every population change described below was purely a dev-side math technique to make
the census numbers balance — nothing more. Language like "over-cap redistribution," "cap-correction trim,"
"over-cap violation," and "population redistribution" repeatedly got picked up and treated as real in-fiction
history by later lore-generation passes reading these files as source material — most visibly for Byrd, where
it produced actual narrative content (Historical Vignettes entries, a DLC 2 quest design note, several DLC 2
questline candidates, Byrd's own Megasheet files, and a companion's romance/home design file all ended up
narrating "the redistribution" as a real historical event before this correction). Moving the raw math here,
out of any file that gets read as lore source material, is meant to prevent that from happening again for any
city, not just Byrd.

**Byrd's own in-fiction population story has been rewritten** (see `Local_Cultures/Byrd_Subnet/Byrd.md`) as
an organic multi-wave labor migration: a first wave of Palmer + Halley subnet citizens who came to establish
the city, then larger, later waves of workers from Palmer, Halley, Janbogo, Mirny, and — to a lesser extent —
Mawson, drawn by the work Byrd's growing industry offered. No other city's in-fiction population story has
been rewritten yet — see "Not yet addressed" at the bottom.

---

## Byrd's Census I population blend (2026-07-03)

Byrd's first-ever population figures (186,268 humans / 190,622 robots / 376,890 combined) were derived from
two source pools, blended by applying each source's own Gini-adjusted weights proportionally:

- **139,376 humans** — the portion carried over from the former Framheim/Little America population figures
  (855,540H/891,723R combined, before those two cities were removed from canon — see below).
- **47,656 humans** — the portion carried over from Palmer City's own population, moved specifically to bring
  Palmer City back under its documented 364,000-combined island cap (see below).

**Notable-tier nation-count math:** Byrd's 36-nation Notable tier splits as 2 nations (New Zealand, Chile)
from the Framheim/Little America portion, and 34 nations from the Palmer City portion — riding along with
Palmer City's own earlier 43-nation master-list expansion project. This is why Byrd ended up the
second-most nationally diverse Tepenian city after Palmer City itself — a real, keepable structural fact.
Only the in-fiction *explanation* for it changed.

## Palmer City's population expansion and over-cap correction (2026-07-03)

Palmer City's national composition was deliberately broadened to include all 33 previously-unrepresented
nations from the master Gini-adjusted effective exiles list. For each nation, a randomly-generated share
between 0.2% and 1.8% of Palmer City's then-current total was assigned and added (total added: 119,648,
Census I) — a genuine net addition to Tepenia's population, not a transfer.

That expansion left Palmer City 113,970 over its documented 364,000-combined island cap. 30% of Palmer City's
total population was moved to bring it back under cap: 20% (the 47,656 humans referenced above) to Byrd, 10%
to Concordia. Census II's equivalent trim was never separately computed — a flagged data gap, not an
oversight.

## Palmer City's per-nation table reconstruction (2026-07-13)

`Specs/Palmer_City.md`'s detailed 43-nation per-nation breakdown table was rebuilt using each nation's relative
weight immediately after the 2026-07-03 expansion, then rescaled proportionally to the final totals
(332,808/332,170). This assumes the later cap-correction trim (30% of the over-cap total moved to
Byrd/Concordia) was applied uniformly across all 43 nations rather than targeting specific ones — consistent
with this project's established convention that population moves preserve source composition rather than
reshaping it (`feedback_population_balancing_simplicity`) — since no per-nation breakdown of that specific
trim exists anywhere in the corpus to check against. Verified: sums to 332,805/332,170 against targets of
332,808/332,170 (trivial rounding across 43 independently-rounded rows). This uniform-trim assumption has
never been independently confirmed — if a genuine per-nation breakdown of the trim ever surfaces, this table
should be checked against it.

## Framheim/Little America removal and population carry-over (2026-07-03)

Framheim and Little America were removed from Tepenian canon entirely (real-world verification found their
shared reconstruction site, the Bay of Whales, was eliminated by the 1987 Iceberg B-9 calving event, and
neither city had any surviving pre-exile infrastructure to justify a war-era status instead — this part *is*
a legitimate in-fiction fact and stays in `Official_Population_Census.md`). Their combined Census I population
(855,540H/891,723R/1,747,263 combined) was carried over into the census math for seven cities: Vostok received
a new 100,333H/261,078R; Esperanza received +74,860H; Concordia and Byrd each received a blend of direct
shares plus Kunlun/Dome Fuji's un-allocated shares (redirected once those two were dropped as destinations on
altitude-viability grounds); Zukelli, Janbogo, and Cape Adare each received +20,000H. Kunlun and Dome Fuji
were deliberately excluded from receiving any share, per their established "too high in altitude to be a
viable population center" canon.

## Lazar's population increase (2026-07-03)

Lazar's population was rebalanced upward via a deliberate transfer from three other cities: Janbogo reduced
to 60% of its original total (865,531 combined transferred to Lazar), Zukelli reduced twice — first to 80%,
then to 90% of that (485,068 combined transferred total) — and Esperanza reduced to 85% of its original total
(319,374 combined transferred). National/ethnic tier composition for all four cities remained structurally
unchanged; only the underlying totals shifted. Grand total unaffected (pure transfer, verified: 31,906,952
unchanged). The same transfer applies to these four cities' Census II figures as well — Census II is not a
separately-computed instance of this mechanism, just the same underlying result reflected in both tables.

## Kunlun and Dome Fuji's population creation (2026-07-04)

Both cities received their first-ever population figures via two rounds of small-percentage population
pooling from every other city except Concordia — Kunlun first, then Dome Fuji, each contributor's humans
reclassified as robots for the destination city. Kunlun's population (123,449, entirely robot) was originally
a single-nation reclassification, later re-resolved 2026-07-06 to a curated 19-nation space/astronomy/comms-
heritage population (see `Specs/Kunlun.md`). Dome Fuji's population (55,072, entirely robot) preserved each
contributor's original nationality rather than reclassifying it, producing a genuine blend (USA and China
leading) representing Tepenia's Ice Cold Buddhism devotee population. Grand total unaffected — a pure internal
transfer (32,026,600 unchanged); human/robot balance shifted nationally by 87,548 in each direction.

**Rounding-verification note (National Origin Totals — Human Population table):** after the Sayowa→Vostok
transfer, this table's total ran 15,711,072 vs. a target of 15,711,071 (off by 1 across 28 affected nations,
rounding, immaterial). After the Kunlun/Dome Fuji population creation, it ran 15,623,526 vs. 15,623,523 (off
by 3 across 42 nations, rounding, immaterial).

## Denison's Census I figures (derivation)

Denison's Canon Census I figures (526,521 humans / 546,852 robots / 1,073,373 combined) were derived through a
different method than the standard island-overflow tier calculation: all other chartered cities contributed
proportional shares to fund the new coastal city. Census II retention rates are pending.

## The Sayowa→Vostok transfer (2026-07-03)

30,000 humans moved from Sayowa's own China-heavy composition to Vostok's existing (Framheim/Little
America-derived) USA/Japan-led profile. Per standing convention, this and similar balancing moves are treated
as simple numeric transfers adopting the destination city's existing composition, not as carrying the source
city's demographic weights along with them.

## Concordia's composition weighting (2026-07-04)

Concordia's population (504,799H/511,148R) was distributed across 12 timezone-eligible nations by
Gini-adjusted effective population, then half of the resulting China figure was deliberately redistributed
proportionally by Gini weight across the USA, Canada, Mexico, and 23 European nations (added by explicit
developer decision rather than the timezone rule) — reflecting Concordia Station's real founding nations
(France, Italy), which otherwise wouldn't have appeared in the composition at all. Full per-nation head counts
preserved in git history if ever needed again.

## Census II Orbital Population fix (2026-07-04)

The Census II "Orbital Population" table and figures were stale — computed once, early in the project, and
never updated through several subsequent rounds of population changes (the Lazar transfer, the Palmer City
expansion, the Framheim/Little America removal, and Kunlun/Dome Fuji/Concordia's new populations), even
though the "Antarctic Surface — Subnet Totals (Census II)" table was actively kept current through every one
of those changes. The old Orbital figure (4,965,736H/4,577,340R) was a relic from before all of that. Fixed
by treating the actively-maintained Antarctic Surface subnet totals as authoritative and recalculating
Orbital as the exact remainder needed to make Census II's Human and Robot totals match Census I's exactly
(population-conservation rule) — Orbital Humans = Census I Humans − Antarctic Surface Humans, same for
Robots. This raised the Orbital population's share of the total from ~30% to ~35.5%, and made the "grand
totals are identical" claim exactly true instead of off by 119,648.

---

## Not yet addressed

The in-fiction population *stories* for the following cities have not been reviewed or rewritten, and may
still describe the mechanisms above as real historical events in their own Local_Culture, Historical
Vignettes, Course of Events, or Megasheet files:

- **Esperanza, Concordia, Zukelli, Janbogo, and Cape Adare** — their own shares of the Framheim/Little America
  population carry-over. Vostok's own share was already retired as an in-fiction event on 2026-07-31
  (`project_vostok_redistribution_retcon`), but that pass didn't touch these five.
- **Lazar** — its population increase from Janbogo, Zukelli, and Esperanza.
- **Kunlun and Dome Fuji** — their population creation via cross-city pooling.
- **Vostok** (again) and **Sayowa** — the Sayowa→Vostok transfer specifically, as distinct from the
  Framheim/Little America question above.
- **Denison** — its Census I figures, funded by proportional contributions from every other chartered city
  rather than the standard island-overflow method.

If any of these show the same pattern (an in-fiction narrative built around a "redistribution" or similar
administrative-decision framing), they'd need the same kind of correction Byrd received — a real in-fiction
explanation for the population that exists, without treating dev-side math as something that happened to
citizens.
