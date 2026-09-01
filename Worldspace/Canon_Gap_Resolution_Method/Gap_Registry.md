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
| — | — | *(no gaps promoted to the standing registry yet)* | — | — | — | — |

**Honest status, 2026-08-31: this registry is empty, and that is correct.** The system has been built but not
yet *run*. Eighteen triaged items exist in `Test_Runs/2026-08-31_Seed_CapeAdare_and_Highway37.md` awaiting a
first acquisition session; **they are deliberately not pre-promoted here**, because a registry populated with
work nobody has started is a registry that immediately reads as stale.

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
