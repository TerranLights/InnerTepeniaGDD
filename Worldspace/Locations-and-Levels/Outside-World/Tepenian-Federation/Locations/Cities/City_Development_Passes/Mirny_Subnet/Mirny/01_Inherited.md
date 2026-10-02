# Mirny — Step 1 · Audit what is inherited

**Pass:** Mirny · ULM · Step 1 · WARM · 2026-09-30 · **Frame:** Second Interwar (default, per `00_Frame.md`)
**T8:** Round 2 **UNANIMOUS** (3 / 3 files) · Round 3 **6 / 6 CONSISTENT** → cleared to write. Record: `01b_T8_Rounds_Step_1.md`.
**Instruction** (`00_RUNBOOK.md` L2530–2533): *"Run the asymmetry check on existing findings before writing new
ones. For every inherited finding describing a threshold, gate, conversion, verdict, admission or status change:
the mechanism runs both ways — did the file write both? Ask what happens to someone it decides against, whether
that outcome is as durable, and whether there is a route back."*
**Inherited material:** `Specs/Mirny subnet/Mirny.md` (230 lines), audited on the spans the Step −1 contract admits.

## Result

| # | Inherited mechanism (spec, admitted span) | Type | Both ways written? | Against side | As durable? | Route back? | Result |
|--:|---|---|:--:|---|:--:|:--:|---|
| 1 | **Station handoff to the exiles** — *"No institutional knowledge … survived that chain of handoffs"*; journals, logs and manuals gave *"a real documentary starting point"*; *"Learning from a written record isn't the same as being taught by a living institution."* (L150, chars 362–612) | conversion | Yes | Written | Written | Partial, and written | **Does not fire** *(A, B, C)* |
| 2 | **The founding by exile** — *"Settled: Post-Falkland Treaty"* (L150, 1–34); built on *"the genuinely substantial, functional station that remained"* (L150, 717–786); founding population (L152, 1–124, demoted). Founders per `DR-9`: exiles from Russia, China and Australia | verdict + admission | **No** — only what the site offered the arrivals | **Not written** — what exile cost the founders | Not written | Not written | **FIRES** *(A, B, C)* |
| 3 | **Relay failure** — *"if it fails, the whole Mirny subnet loses contact with itself"* (L184, 487–549); hub status (L5) | threshold / status | Yes — the failure case is written | Written, for the subnet | **Not written** | **Not written** — no restoration | **FIRES** *(A, B, C)* |
| 4 | **Harbor window** — navigable but *"not year-round"* (L57); ice *"can change quickly"* (L133); wind *"can close the harbor even within the navigable window, creating supply interruptions"* (L143) | gate | Yes | Written | Written (seasonal) | Carried by the season | **Does not fire** *(B, C; A withdrew in Round 3)* |
| 5 | **One quarry base, two claims** — *"Mirny's own quarries supply both the eastern-highway construction materials … AND this new, nationally significant chamber-manufacturing supply chain"* (L176, 433–607) | conversion | **No** — only the case where the output serves both | **Not written** — what happens when it cannot | Not written | Not written | **FIRES** *(C; A and B read it as relation — split carried as a handoff, not a finding)* |
| 6 | **The Antarctic Circle** (L8, L55) · **katabatic hazard** (L131) | physical threshold | Both physical sides written | **No one is decided against** | — | — | **No subject** — the check has nothing to ask *(A, B, C)* |

## Handoffs — the unwritten sides, carried to the steps that build them (nothing is answered here)

- **From #2 → Step 2 (G4) and Phase 2:** what did exile cost the people who founded Mirny, was it for life, and was
  there any way back?
- **From #3 → Phase 5 (with request R-11):** when the relay fails, how long does the subnet stay cut off, and who
  restores contact?
- **From #5 → Phase 7 (with request R-12):** when the quarries cannot meet both claims, which is served, and who
  decides?

## Not audited — excluded by the Step −1 contract

- **Post-war material** (frame): war damage (L4, L208), refugees (L202), the Planetary Split Brain cut and Hwy
  110's post-war state (L140, L198, L200, L222), the relay's post-war status (L192, L208).
- **The wind ring and sheltered placement** (L162, L168 — both excluded; L168 is developer-vision material, `DR-10`).
- **The kept name** (L154): *"The name was kept."* is a naming fact only — no meaning is built on it (`DR-28`); the
  rest is GPS-excluded. The official name stays reserved (RV-1) — **not adopted.**
- **Other inherited Mirny files** (`Local_Cultures`, `City_Enneagram_Personalities`, the Full Extrapolation):
  read-last or withheld under the contract — not Step 1 inputs.

## Execution log

| # | What the instruction demanded | Where | Found? | Evidence |
|--:|---|---|:--:|---|
| 1 | Audit inherited findings before writing new ones | `00_RUNBOOK.md` L2530 | Yes | Spec audited; no new finding written |
| 2 | Both ways · against side · durability · route back, for each mechanism | L2531–2533; `G10` L36–39 | Yes | Table above |
| 3 | Open the gate's entry for its worked case | L2526–2528 | **No** | `G10` L50: the worked case is archived in `Test_Runs/Worked_Examples_Archive/`, outside the read set |

**Verdict:** ☑ step complete.
