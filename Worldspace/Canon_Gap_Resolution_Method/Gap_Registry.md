# Gap Registry — live, standing, scope-agnostic

**The demand-driven work queue for the whole project.** Holds only gaps admitted into the queue — **not** an
attempt at the project's ~2,872 `TBD` occurrences, which is deliberately and permanently out of scope
(`01` §2).

> ## ⚠ This file is the METHOD's registry. Instance data lives in `Test_Runs/`.
>
> **Standing separation, per developer instruction 2026-08-31.** A test-run instance's own gap list, triage
> ratios, and path distribution are properties of *that scope*, not of this system. **They must not be read
> back into the method, and this registry must not become one instance's ledger wearing a general title.**
>
> **How the two relate:** a run works from an instance file; **only gaps that are genuinely still open, still
> wanted, and not yet closed get promoted into the table below** — and they arrive stripped of that instance's
> framing. A row here is a live commitment; a row in a `Test_Runs/` file is a record of what one run found.

---

## Current open rows

| ID | Scope | Gap | Triage | Path | Status | Log ref |
|---|---|---|---|---|---|---|
| **CGRM-001** | **Denison** | **How is the city physically built on Cape Denison — what does the megastructure actually stand on, geologically?** | **LIVE** | **4 — light real-world research** *(partly run)* | ⏸️ **PARKED by developer, 2026-09-03** | — |

> ### ⏸️ CGRM-001 — parked deliberately, with partial research already banked. **Do not re-run the searches.**
>
> **Developer, 2026-09-03:** *"the problem regarding Denison is that I don't actually know how it would be
> physically built (geographically, geologically speaking). I'd like to get that settled before running a
> proper ULM run"* — **then, the same session:** *"no, we'll do that later. That is a problem for later."*
> ***Parked, not abandoned. `Specs/Denison.md` must not be cold-run until this closes.***
>
> **⚠ What is ALREADY settled and does NOT need redoing** — `Specs/Denison.md` carries a full worked block:
> the 1.11 km² / 1,066,143 density problem *(~960,489 per km², ~3× the figure already rejected at Cape Adare)*,
> the four-ridge / three-valley topography, the enclosing ice cliffs ruling out a linear coastal city, the
> §15 *"one continuous, interlinked, load-sharing structure"* reinterpretation, the Byrd differentiation
> constraint, and **options (A)–(E) with (E) recommended by the analyst.** ***The remaining question is
> narrow: can the geology actually carry option A/E?***
>
> **⭐ RESEARCH BANKED 2026-09-03 — the unexamined premise was the bedrock itself, and it checks out:**
>
> | Finding | Bearing on the megastructure |
> |---|---|
> | **The rock is GNEISS** — Mawson's own account calls it *"more than ordinarily tough."* Felsic gneiss: plagioclase, quartz, biotite, K-feldspar, hypersthene, garnet; plus metapelites and mafic dikes | ⭐ **Gneiss is excellent foundation rock** — high compressive strength, low porosity. **The premise holds** |
> | **Metamorphic crystallization c. 2500 Ma, retrograde c. 1710 Ma** (SHRIMP U–Pb on zircon) | Ancient, deeply consolidated shield rock — not young or weak |
> | **Mawson anchored the 1912 huts by BLASTING HOLES IN BEDROCK** and setting timber uprights in them, held with rock and ice — *"no earth or gravel existed"* | ⭐⭐ **Direct historical precedent for the anchoring method**, at the same site, in the same wind |
> | **Upper moraine** (near the ice edge): diverse rock types, angular, poorly sorted — likely true glacial deposit | The valleys are fill, not rock — **spans must reach ridge to ridge** |
> | **Lower moraine** (below 12 m asl): local rock, rounded, sorted, water-worn, includes lithified beach sand with foraminifera — likely **ice push**, not glacial | Shallow, unconsolidated — **not a foundation** |
> | Cape is a **1.2 km rocky outcrop**; Mawson's huts sit **60 m from shore**; **Boat Harbor** is a 400 m coastal indent | Usable scale figures |
> | Little-studied **red sandstone and crystalline limestone** also present | Minor; unexamined |
>
> **⛔ Still unresearched when parked:** jointing/foliation orientation *(governs which way the rock will
> split under load)* · frost-shattering depth · moraine depth in the valleys · permafrost/ground-ice ·
> ice-cliff heights · ice-cap thickness behind the cape.
>
> **Sources reached:** AAD *Mawson's Huts — Cape Denison landscape*; Wikipedia *Cape Denison*, *Commonwealth
> Bay*; Geoscience Australia *Geology of Cape Denison* **(GA20109 — ⚠ PDF exceeds fetch size limit; needs
> another route)**; ASPA-162 management plan **(⚠ PDF text layer not extractable via fetch; a copy was saved
> locally during the attempt)**; Mawson's Huts Foundation; Mawson, *Home of the Blizzard*.

**Honest status of the rest of this registry, 2026-08-31: otherwise empty, and that is correct.** The system
has been built but not yet *run* at scale. Eighteen triaged items exist in
`Test_Runs/2026-08-31_Seed_CapeAdare_and_Highway37.md` awaiting a first acquisition session; **they are
deliberately not pre-promoted here**, because a registry populated with work nobody has started is a registry
that immediately reads as stale.

---

## Schema

| Column | Contents |
|---|---|
| **ID** | `CGRM-nnn` — continuous across the whole project, never reused, never restarted per scope |
| **Scope** | the location / **person** / subsystem / consumer-pass it belongs to |
| **Gap** | the question, in one sentence |
| **Triage** | `LIVE` · `SCHEDULED` · `SCAFFOLD` · `RESERVED` (`01` §4) |
| **Path** | the acquisition path chosen (`02`), or `—` for non-LIVE |
| **Status** | `open` · `in progress` · `closed` · `unresolved` · **`protected`** |
| **Log ref** | the `Resolution_Log.md` entry, once closed |

**`protected` is a positive outcome, not a failure state.** It marks a gap this system has deliberately
declined to close — a scheduled deferral, a load-bearing open question — so that the next session does not
"helpfully" close it. **Per LAW A, a run's protected count is reported as prominently as its closed count.**

## Standing rules

1. **Check here before acquiring anything** (`00` Step 4). If a question has already been asked, answered, or
   attempted, do not re-run it. **This is the file's single most important job** — it is the only thing in the
   project that prevents two sessions independently researching the same question for two different scopes.
2. **IDs are never reused and never restart per scope.** Continuous numbering is what makes recurrence visible
   across scopes — the same reasoning behind the observations-log numbering the location methodology already
   uses.
3. **Non-LIVE items get rows too.** A SCHEDULED item recorded as SCHEDULED is a real output: it tells the next
   session the question has been seen, understood, and correctly left alone.
4. **A closed row keeps its log reference forever.** A closed gap with no traceable provenance is
   indistinguishable from canon that was never questioned — which is Gate 5's whole concern.
