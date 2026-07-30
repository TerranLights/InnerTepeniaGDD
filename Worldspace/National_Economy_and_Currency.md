# National Economy and Currency

**⚠️ Flagged 2026-07-29 for future renaming — "scrip" was never the developer's own term.** The word appears throughout this file and roughly 100+ others across the repo (course-of-events files, code architecture docs, city lore). Not touched in this pass — this is a name-and-mechanics task, not a quick swap: the actual mechanics of how the currency works also still need to be sorted out, not just its name. Revisit as its own dedicated pass; don't rename piecemeal.

**Established 2026-07-07.** Answers the open question flagged in `City_Logistics.md` ("Currency and economic system details" — TBD in lore). Confirmed design: an energy-backed currency during the Second Interwar Period, fracturing into regional currencies after the Planetary Split Brain — not two competing options, but one continuous history where the second state is a direct, mechanical consequence of the same catastrophe that caused everything else covered in `Energy_Grid_Failure_Rationale.md` and `Storyline/DLC_PSB_Framework.md`.

**Ruled out, and why:** a siligel/coolant commodity standard was considered and rejected — siligel and coolant are food and drink for robots, not something they would literally pay for goods with, even though bartering *with* them remains realistically plausible as a distinct, secondary practice. A nominal, rarely-trusted leftover "Federation Scrip" was also rejected outright.

---

## Phase 1: The Second Interwar Period — Energy-Backed National Scrip

**Placeholder name:** *the Federation Watt* (or similar — not yet settled).

From sometime after Amundsen Tower's completion (~2630–2640) onward, the currency was backed directly by verified energy allocation — a unit redeemable for a fixed amount of guaranteed grid capacity. This wasn't an abstract, faith-based fiat currency; it worked because it had something to be backed *by*: Amundsen Tower functioned as a literal continent-scale regulating flywheel for the entire Antarctic grid (see `Energy_Grid_Failure_Rationale.md` #11), meaning the grid itself was genuinely unified and continent-regulated for the whole of this period. A currency backed by verified energy allocation could be trusted nationally because the underlying infrastructure backing it was itself national in scale — the Tower is what made a single, cross-subnet currency actually credible, not merely convenient.

This currency naturally bridged the human/robot dual economy (see `City_Logistics.md`'s "Dual Economy" section) — human heating/food/water systems and robot siligel production/component maintenance both ultimately traced back to the same regulated grid, even though what each population actually spent it on looked completely different.

---

## The Fracture Point: Amundsen Tower's Destruction

The currency's fragmentation isn't a separate event from the Long Night War's other damage — it's the same event, viewed from the economic angle. Per `Energy_Grid_Failure_Rationale.md` #11 and `Storyline/DLC_PSB_Framework.md`, the Tower's collapse caused, in the same electrical instant: the acute continent-wide grid overload, the permanent loss of continental grid regulation, and — very likely the same underlying mechanism — the severance of the inter-subnet Arcanet backbone (the Planetary Split Brain itself).

**Applied to the currency specifically:** an energy-backed national scrip requires two things to keep functioning — a genuinely unified grid to back it, and a way to verify that backing across the whole territory it circulates in. The Tower's destruction removed both in the same moment: the grid fragmented into isolated regional pieces with no central regulation, and the Arcanet backbone that could have verified a subnet's currency claims to another subnet went down at the same time. The currency didn't gradually devalue or slowly fragment over subsequent decades — it lost both of its structural supports simultaneously, in the same catastrophe that ended space access and severed the subnets informationally from each other.

---

## Phase 2: Post-Split-Brain — Regional Scrip Plus a Cross-Subnet Trade Standard

**Present day (≈2822–2827).** With no unified grid left to back a single currency and no cross-subnet network left to verify it, the Federation Watt's national credibility didn't survive the transition. What almost certainly replaced it:

- **Regional/subnet-level energy scrip** — each subnet (plausibly even individual cities) now issues and verifies its own local currency against its own local grid capacity, since that's the only scale at which "verified energy allocation" still means anything concrete.
- **A separate, harder cross-subnet trade standard** — used by highway freight and long-haul traders (Neon Nomads and similar) moving between subnets that can no longer directly verify each other's local scrip. Likely accepted at negotiated, non-fixed rates rather than at instant par value, since there's no live network connection to confirm a distant subnet's currency is genuinely backed by what it claims.

This also gives the black market's established role (see `City_Logistics.md`) a cleaner structural reason to exist: a fragmented formal system, with real friction at every subnet boundary, leaves exactly the kind of gaps an informal parallel economy is well-suited to fill.

---

## What's Still Open

Per the developer's own framing, these are genuine open details, not yet resolved:
- What exactly backs or verifies the cross-subnet trade standard, given the grid itself is no longer unified even at that layer — a physical commodity, a trusted third-party verification method (Neon Nomads' own reputation network?), or something else entirely
- Whether individual cities within a subnet share one regional scrip or maintain their own city-level currencies
- Placeholder names for both the Second Interwar Period currency and its post-Split-Brain successor(s)
- Exact exchange mechanics at subnet boundaries — fixed discount rates, negotiated per-trade, or something else
- How (or whether) Upper Earth trade interacts with any of this — plausibly a fully separate settlement layer given Upper Earth almost certainly wouldn't accept Tepenia's internal currency, but this hasn't been addressed
- Cost-of-living variation by city type — a real market city (Palmer City) vs. a near-post-scarcity, institutionally-provisioned outpost (Kunlun, Vostok, Dome Fuji) likely relate to their own local currency very differently, worth developing once individual city economies are written in more depth

---

## Worth Your Attention

The most load-bearing fact here is that this isn't a designed-from-scratch economic system — it's a direct, mechanical consequence of the Amundsen Tower's already-established destruction. The same single catastrophe that ended space access, fried the grid, and severed the Arcanet backbone is also, now, confirmed as the exact moment Tepenia's currency stopped being a national system and became a fragmented regional one. That's one more piece of the Long Night War's damage that traces back to the same root cause rather than needing its own separate origin story.
