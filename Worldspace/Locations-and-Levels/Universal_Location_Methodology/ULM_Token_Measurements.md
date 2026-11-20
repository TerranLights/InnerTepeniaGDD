# ULM token measurements — the per-city average

**Developer, 2026-11-18:** measure how much one full ULM city run takes, step by step and in all, on Kunlun and Ariun Nuur, to reach a rough
average per city. The per-run logs are `TOKEN_LOG_Ariun_Nuur.md` and `TOKEN_LOG_Kunlun.md` (beside this file). When both runs have
recorded Step 10, copy each run's per-unit totals here and average them.

| Unit | Ariun Nuur | Kunlun | Average |
|---|--:|--:|--:|
| Readiness check | 0 (orchestrator only) | | |
| Step −1 | 914,005 | | |
| Step 0 | 1,246,877 | | |
| Step 1 | 1,039,412 | | |
| Step 2 | 1,821,034 | | |
| Step 3 | 2,251,404 | | |
| Phases 2 to 10 (each) | P2 1,761,476 · P3 1,879,739 · P4 2,199,874 · P5 2,415,795 · P6 2,377,220 · P7 2,889,464 · P8 2,775,209 · P9 3,072,828 · P10 (six units: catalog 2,017,304 · 10R 1,662,510 · 10C 775,655 · 10R2 5,844,612) 10,300,081 | | |
| Step 5 (both stages) | 5,421,139 | | |
| Steps 6 to 10 (each) | S6 1,229,906 · S7 5,410,716 · S8 4,336,659 · S9 1,343,288 · S10 998,089 | | |
| **Run total (subagents)** | **55,684,215** | | |
| **Allotment used (meter)** | start 12% · end 53% (2026-11-20 13:10) · **used 41 points** of the weekly allotment (⚠ provisional: possibly 50–55%; see the note below) | | |

*Ariun Nuur column copied 2026-11-20 at Step 10 from `TOKEN_LOG_Ariun_Nuur.md`'s per-unit rows (subagent tokens only; Phase 10 ran as six units because the LAW 0-P ruling of 2026-11-19 added the candidate-list research mid-run). The closing allotment reading, 53% at 2026-11-20 13:10, was given by the developer on their return and entered the same day; nothing ran between Step 10 (~11:05) and that reading.*

*Allotment note, Ariun Nuur (developer, 2026-11-20): log **41%** for the run, with the caveat that it may be **50–55%**. The 41 is the meter's
end reading (53%) minus its start reading (12%, given by the developer at the run's start, 2026-11-18 13:16). The developer recalls the
allotment beginning at zero after a manual reset, so the 12 points already on the meter at the start may include work that belongs to the
run's cost; what used them is not known for certain (the 11-18 datasheet preparation, about 1 point by the run's own rate, and possibly the
11-17 evening's work, if the reset came before it). **Kunlun's full run (week of 2026-11-29 to 12-04) is expected to give the more accurate
figure.** For that run: read the meter at the reset, again just before the run starts (with nothing else run in between, or a note of what
was), and at each close.*
