# Token log — the ULM run of Ariun Nuur

**Why this file exists** (developer, 2026-11-18): *"During each step and or phase, keep track of how many tokens actually get used. Keep those
numbers recorded in a log file, and then we'll use that as a reference to measure how much resources each step, each phase of the ULM
actually requires. We'll do this for both Kunlun and Ariun Nuur so that we can get a rough, approximate average of how much resources the
ULM actually needs in order to be able to run on any one particular given city, from beginning to end, start to finish."*

## How to record (the orchestrator, during the run)
- **Every agent's tokens come from its task notification:** the `subagent_tokens` figure, with `tool_uses` and `duration_ms`.
- **The figure is cumulative per agent.** A reader resumed for Round 3, a repair or an addendum reports its running total each time. Record
  each notification as it arrives, and compute the **delta** (this notification minus that agent's previous one). The unit's cost is the sum of
  every agent's **last** figure.
- **One row per notification**, in the table below, written when the notification arrives (not reconstructed later).
- **A unit's total line** when the unit is recorded: readers, Round 3, repairs and addenda, the merge writer, and any helper agent.
- **The orchestrator's own tokens are not reported per unit** by any tool. They are captured by the **allotment-meter readings** the developer
  gives: at the start, at the end, and (if the developer is present) at each morning close. Record each reading with its time.
- **Web calls** per unit, from the readers' own counts and from `Tools/web_quota_count.py` (which reads higher).

## Preparation, 2026-11-18 (by the session that ran Relung Panen; **not part of the run's measurement**)
| Agent | Task | subagent_tokens | Tool uses | Duration (min) |
|---|---|--:|--:|--:|
| validator A | the Pre-Trip, ledger, README, Steps −1 to 3 sheets | 275,693 | 75 | 13.0 |
| validator B | the Phase 2 to 6 sheets | 185,660 | 54 | 8.0 |
| validator C | the Phase 7 to 10 and Step 5 to 10 sheets | 196,791 | 78 | 10.9 |
| memory scan | memory and required reading, by shape | 92,899 | 18 | 3.1 |
| fix writer | applying the corrections | 314,841 | 59 | 14.6 |
| checker | verifying the corrections | 275,543 | 79 | 12.6 |
| **Preparation, subagents in all** | | **1,341,427** | | |

## Allotment-meter readings (the developer's)
| Date and time | Reading | Note |
|---|---|---|
| 2026-11-18 13:16 | **12%** | the start of the run; given by the developer with the handover of the startup file |
| 2026-11-18 14:01 | **13%** | after the readiness check and Step −1 (Step −1's subagents: 914,005 tokens); given by the developer |
| 2026-11-18 15:42 | **14%** | the first day's close, after Step 0 (Step 0's subagents: 1,246,877 tokens; day total 2,160,882); given by the developer |
| 2026-11-19 14:10 | **35%** | the second day's close: Phases 5–9 recorded; Phase 10's three units through Round 3 (Phase 10's own Round 3 being closed by repairs) |
| 2026-11-19 14:36 | **35%** | the new session's start, given by the developer: after the handoff was read, the two morning jobs were set and the web-search limit (1,000) was checked; no run work done in this session yet |
| 2026-11-20 13:10 | **53%** | the run's close, given by the developer on their return: read about two hours after Step 10 was recorded (~11:05); no run work and no subagent ran in between. This session (Phase 10R2 through Step 10) moved the meter 35% → 53% |

## Per notification
| Date and time | Unit | Role (reader A/B/C · Round 3 · repair · addendum · merge · helper) | Agent ID | subagent_tokens (cumulative) | Delta | Tool uses | Duration (min) |
|---|---|---|---|--:|--:|--:|--:|
| 2026-11-18 13:34 | Step −1 | reader B | a4f16872c4e1e396b | 170,621 | 170,621 | 42 | 9.1 |
| 2026-11-18 13:35 | Step −1 | reader C | ae8de1fc7b5ce0842 | 171,488 | 171,488 | 42 | 9.7 |
| 2026-11-18 13:37 | Step −1 | reader A | a098665c856e2f16e | 188,874 | 188,874 | 44 | 12.0 |
| 2026-11-18 13:39 | Step −1 | Round 3, reader C | ae8de1fc7b5ce0842 | 218,681 | 47,193 | 3 | 1.4 |
| 2026-11-18 13:40 | Step −1 | Round 3, reader B | a4f16872c4e1e396b | 222,028 | 51,407 | 3 | 2.0 |
| 2026-11-18 13:40 | Step −1 | Round 3, reader A | a098665c856e2f16e | 237,879 | 49,005 | 3 | 2.1 |
| 2026-11-18 13:54 | Step −1 | merge | a5be549d0b010f72b | 235,417 | 235,417 | 20 | 12.5 |
| 2026-11-18 14:14 | Step 0 | reader A | aa3736c660d86e995 | 248,957 | 248,957 | 35 | 10.3 |
| 2026-11-18 14:14 | Step 0 | reader B | a6dd3497d646e97b8 | 249,550 | 249,550 | 32 | 10.8 |
| 2026-11-18 14:17 | Step 0 | reader C | ac704552f301ca3e5 | 278,346 | 278,346 | 106 | 13.4 |
| 2026-11-18 14:20 | Step 0 | Round 3, reader B | a6dd3497d646e97b8 | 313,656 | 64,106 | 3 | 1.8 |
| 2026-11-18 14:20 | Step 0 | Round 3, reader A | aa3736c660d86e995 | 314,754 | 65,797 | 4 | 1.9 |
| 2026-11-18 14:20 | Step 0 | Round 3, reader C | ac704552f301ca3e5 | 341,505 | 63,159 | 4 | 2.0 |
| 2026-11-18 14:33 | Step 0 | merge | a9a2aca37c405fda7 | 276,962 | 276,962 | 27 | 10.4 |
| 2026-11-19 05:16 | Step 1 | reader B | a38b6273db4f0b5cd | 217,519 | 217,519 | 25 | 10.2 |
| 2026-11-19 05:16 | Step 1 | reader C | ac5fe2ae648244950 | 229,210 | 229,210 | 48 | 11.2 |
| 2026-11-19 05:18 | Step 1 | reader A | a5bc9b004881b40f4 | 243,549 | 243,549 | 23 | 13.0 |
| 2026-11-19 05:22 | Step 1 | Round 3, reader A | a5bc9b004881b40f4 | 291,558 | 48,009 | 2 | 1.9 |
| 2026-11-19 05:22 | Step 1 | Round 3, reader B | a38b6273db4f0b5cd | 268,445 | 50,926 | 2 | 2.0 |
| 2026-11-19 05:22 | Step 1 | Round 3, reader C | ac5fe2ae648244950 | 280,233 | 51,023 | 2 | 2.2 |
| 2026-11-19 05:32 | Step 1 | merge | ab34b78a16d71ff2d | 199,176 | 199,176 | 13 | 9.5 |
| 2026-11-19 05:57 | Step 2 | reader B | a170394fda7c1d9ae | 396,144 | 396,144 | 58 | 19.2 |
| 2026-11-19 05:57 | Step 2 | reader A | aa587206e9c860f01 | 413,014 | 413,014 | 58 | 20.3 |
| 2026-11-19 05:58 | Step 2 | reader C | aecc44464638fcb83 | 405,510 | 405,510 | 56 | 20.9 |
| 2026-11-19 05:59 | Step 2 | repair, reader B | a170394fda7c1d9ae | 398,008 | 1,864 | 3 | 0.3 |
| 2026-11-19 06:03 | Step 2 | Round 3, reader C | aecc44464638fcb83 | 488,275 | 82,765 | 5 | 2.2 |
| 2026-11-19 06:03 | Step 2 | Round 3, reader B | a170394fda7c1d9ae | 495,581 | 97,573 | 7 | 2.5 |
| 2026-11-19 06:03 | Step 2 | Round 3, reader A | aa587206e9c860f01 | 512,616 | 99,602 | 6 | 2.6 |
| 2026-11-19 06:22 | Step 2 | merge | acc4022660a2ec56e | 324,562 | 324,562 | 20 | 18.7 |
| 2026-11-19 06:51 | Step 3 | reader A | a88f560c09525c0b1 | 499,138 | 499,138 | 123 | 25.9 |
| 2026-11-19 06:51 | Step 3 | reader C | a1879c648055b7df2 | 539,640 | 539,640 | 136 | 26.0 |
| 2026-11-19 06:54 | Step 3 | reader B | af75d84c90d158f49 | 564,652 | 564,652 | 152 | 28.3 |
| 2026-11-19 06:54 | Step 3 | repair, reader A | a88f560c09525c0b1 | 499,417 | 279 | 2 | 0.3 |
| 2026-11-19 06:54 | Step 3 | repair, reader C | a1879c648055b7df2 | 539,972 | 332 | 2 | 0.3 |
| 2026-11-19 06:58 | Step 3 | Round 3, reader A | a88f560c09525c0b1 | 592,560 | 93,143 | 7 | 2.4 |
| 2026-11-19 07:00 | Step 3 | Round 3, reader C | a1879c648055b7df2 | 643,591 | 103,619 | 7 | 3.9 |
| 2026-11-19 07:00 | Step 3 | Round 3, reader B | af75d84c90d158f49 | 656,645 | 91,993 | 8 | 4.0 |
| 2026-11-19 07:35 | Step 3 | merge | a76377cb40ad9b459 | 358,608 | 358,608 | 36 | 33.8 |
| 2026-11-19 07:54 | Phase 2 | reader C | a6176778716dc7d88 | 434,595 | 434,595 | 67 | 14.6 |
| 2026-11-19 07:55 | Phase 2 | reader A | a7cec8f4a16d2896d | 440,590 | 440,590 | 86 | 15.8 |
| 2026-11-19 07:57 | Phase 2 | reader B | a1c36e1a95e5d4c04 | 453,478 | 453,478 | 88 | 17.5 |
| 2026-11-19 08:00 | Phase 2 | Round 3, reader A | a7cec8f4a16d2896d | 502,846 | 62,256 | 4 | 1.8 |
| 2026-11-19 08:00 | Phase 2 | Round 3, reader B | a1c36e1a95e5d4c04 | 511,729 | 58,251 | 3 | 1.8 |
| 2026-11-19 08:00 | Phase 2 | Round 3, reader C | a6176778716dc7d88 | 511,419 | 76,824 | 6 | 2.5 |
| 2026-11-19 08:13 | Phase 2 | merge | adfe36a5491c2295e | 235,482 | 235,482 | 16 | 11.9 |
| 2026-11-19 08:31 | Phase 3 | reader A | a0cfd7be9faa745d5 | 452,859 | 452,859 | 61 | 14.9 |
| 2026-11-19 08:31 | Phase 3 | reader C | a501ccf2152b29d85 | 464,751 | 464,751 | 60 | 15.3 |
| 2026-11-19 08:31 | Phase 3 | reader B | a0ee1650da70c3a02 | 462,922 | 462,922 | 58 | 15.6 |
| 2026-11-19 08:35 | Phase 3 | Round 3, reader C | a501ccf2152b29d85 | 537,435 | 72,684 | 4 | 2.2 |
| 2026-11-19 08:35 | Phase 3 | Round 3, reader B | a0ee1650da70c3a02 | 537,327 | 74,405 | 5 | 2.2 |
| 2026-11-19 08:35 | Phase 3 | Round 3, reader A | a0cfd7be9faa745d5 | 527,382 | 74,523 | 5 | 2.2 |
| 2026-11-19 08:51 | Phase 3 | merge | a352cd80d3044a312 | 277,595 | 277,595 | 18 | 15.5 |
| 2026-11-19 09:09 | Phase 4 | reader C | acd0d5637c10b90dc | 541,047 | 541,047 | 115 | 15.5 |
| 2026-11-19 09:09 | Phase 4 | reader A | a5efa60e35cbbe927 | 541,770 | 541,770 | 104 | 15.5 |
| 2026-11-19 09:14 | Phase 4 | reader B | af5024ee92da32de7 | 607,572 | 607,572 | 119 | 19.7 |
| 2026-11-19 09:17 | Phase 4 | Round 3, reader C | acd0d5637c10b90dc | 618,433 | 77,386 | 5 | 1.8 |
| 2026-11-19 09:17 | Phase 4 | Round 3, reader A | a5efa60e35cbbe927 | 619,091 | 77,321 | 5 | 2.1 |
| 2026-11-19 09:17 | Phase 4 | Round 3, reader B | af5024ee92da32de7 | 679,127 | 71,555 | 4 | 2.3 |
| 2026-11-19 09:31 | Phase 4 | merge | afabdb3ba11d112d4 | 283,223 | 283,223 | 27 | 13.9 |
| 2026-11-19 09:54 | Phase 5 | reader A | ad3557ee4f637e544 | 605,900 | 605,900 | 111 | 18.8 |
| 2026-11-19 09:54 | Phase 5 | reader B | a31e24a206965fbef | 614,411 | 614,411 | 126 | 20.2 |
| 2026-11-19 09:57 | Phase 5 | reader C | aae1241a89891e37d | 634,763 | 634,763 | 100 | 23.2 |
| 2026-11-19 09:58 | Phase 5 | repair, reader C | aae1241a89891e37d | 636,504 | 1,741 | 3 | 0.4 |
| 2026-11-19 10:02 | Phase 5 | Round 3, reader C | aae1241a89891e37d | 719,851 | 83,347 | 6 | 2.1 |
| 2026-11-19 10:02 | Phase 5 | Round 3, reader B | a31e24a206965fbef | 697,605 | 83,194 | 7 | 2.1 |
| 2026-11-19 10:02 | Phase 5 | Round 3, reader A | ad3557ee4f637e544 | 690,146 | 84,246 | 6 | 2.2 |
| 2026-11-19 10:18 | Phase 5 | merge | a960c95222c3e0750 | 308,193 | 308,193 | 27 | 15.9 |
| 2026-11-19 10:35 | Phase 6 | reader B | a2af1048b1ca54155 | 622,565 | 622,565 | 84 | 13.4 |
| 2026-11-19 10:35 | Phase 6 | reader C | aa3e20a974c33ecc9 | 633,854 | 633,854 | 89 | 14.7 |
| 2026-11-19 10:37 | Phase 6 | reader A | ae9bff3f654e3a4fa | 642,200 | 642,200 | 107 | 16.2 |
| 2026-11-19 10:38 | Phase 6 | repair, reader A | ae9bff3f654e3a4fa | 642,317 | 117 | 2 | 0.6 |
| 2026-11-19 10:41 | Phase 6 | Round 3, reader A (first part) | ae9bff3f654e3a4fa | 693,544 | 51,227 | 3 | 1.3 |
| 2026-11-19 10:41 | Phase 6 | Round 3, reader B | a2af1048b1ca54155 | 694,091 | 71,526 | 6 | 1.7 |
| 2026-11-19 10:41 | Phase 6 | Round 3, reader C | aa3e20a974c33ecc9 | 701,456 | 67,602 | 6 | 1.8 |
| 2026-11-19 10:41 | Phase 6 | Round 3, reader A (addendum) | ae9bff3f654e3a4fa | 711,900 | 18,356 | 4 | 0.6 |
| 2026-11-19 10:42 | Phase 6 | second repair, reader A | ae9bff3f654e3a4fa | 712,935 | 1,035 | 2 | 0.3 |
| 2026-11-19 10:57 | Phase 6 | merge | af22cd0aef19d5709 | 268,738 | 268,738 | 19 | 14.7 |
| 2026-11-19 11:20 | Phase 7 | reader B | a3916ca2fc449b82d | 731,156 | 731,156 | 148 | 21.2 |
| 2026-11-19 11:20 | Phase 7 | reader C | a00736454068d547c | 742,840 | 742,840 | 136 | 21.9 |
| 2026-11-19 11:22 | Phase 7 | reader A | a570442ff51c2c541 | 760,025 | 760,025 | 144 | 22.5 |
| 2026-11-19 11:24 | Phase 7 | Round 3, reader B | a3916ca2fc449b82d | 833,922 | 102,766 | 8 | 2.2 |
| 2026-11-19 11:26 | Phase 7 | Round 3, reader C | a00736454068d547c | 855,223 | 112,383 | 8 | 2.6 |
| 2026-11-19 11:26 | Phase 7 | Round 3, reader A | a570442ff51c2c541 | 866,036 | 106,011 | 8 | 2.6 |
| 2026-11-19 11:43 | Phase 7 | merge | adc0104f47613d90f | 334,283 | 334,283 | 30 | 16.5 |
| 2026-11-19 12:00 | Phase 8 | reader A | a3f9569ea3e37f045 | 746,393 | 746,393 | 86 | 14.5 |
| 2026-11-19 12:00 | Phase 8 | reader C | aeaa888763a2fab1f | 757,348 | 757,348 | 90 | 15.9 |
| 2026-11-19 12:03 | Phase 8 | reader B | a23200a1c88d4a8ea | 775,394 | 775,394 | 120 | 17.9 |
| 2026-11-19 12:06 | Phase 8 | Round 3, reader A | a3f9569ea3e37f045 | 830,814 | 84,421 | 7 | 2.1 |
| 2026-11-19 12:06 | Phase 8 | Round 3, reader B | a23200a1c88d4a8ea | 852,788 | 77,394 | 8 | 2.2 |
| 2026-11-19 12:06 | Phase 8 | Round 3, reader C | aeaa888763a2fab1f | 841,702 | 84,354 | 8 | 2.2 |
| 2026-11-19 12:17 | Phase 8 | merge | afe1f7ca115bfcec2 | 249,905 | 249,905 | 18 | 11.1 |
| 2026-11-19 12:39 | Phase 9 | reader A | adebb94b6ad637160 | 800,371 | 800,371 | 102 | 15.6 |
| 2026-11-19 12:39 | Phase 9 | reader B | a882c212672744290 | 838,844 | 838,844 | 113 | 19.9 |
| 2026-11-19 12:40 | Phase 9 | reader C | ae5e9421635bbc9c5 | 833,851 | 833,851 | 88 | 20.1 |
| 2026-11-19 12:41 | Phase 9 | repair, reader B | a882c212672744290 | 839,073 | 229 | 2 | 0.2 |
| 2026-11-19 12:45 | Phase 9 | Round 3, reader C | ae5e9421635bbc9c5 | 930,409 | 96,558 | 7 | 2.2 |
| 2026-11-19 12:45 | Phase 9 | Round 3, reader A (first part) | adebb94b6ad637160 | 888,317 | 87,946 | 8 | 2.3 |
| 2026-11-19 12:45 | Phase 9 | Round 3, reader B | a882c212672744290 | 938,298 | 99,225 | 10 | 2.5 |
| 2026-11-19 12:46 | Phase 9 | Round 3 addendum and two fixes, reader A | adebb94b6ad637160 | 909,231 | 20,914 | 4 | 0.5 |
| 2026-11-19 13:00 | Phase 9 | merge | a0a5ca9bb2b96f99c | 294,890 | 294,890 | 18 | 13.5 |
| 2026-11-19 13:27 | Phase 10 | reader C | a6d2fde08b3308891 | 177,561 | 177,561 (as reported; low against 131 tool uses, likely context compaction inside the agent) | 131 | 20.7 |
| 2026-11-19 13:27 | Phase 10 | reader B | afda8b0f677e90431 | 221,538 | 221,538 (as reported; low against 143 tool uses, likely compaction) | 143 | 24.4 |
| 2026-11-19 13:32 | Phase 10 | reader A | a8512e8622c5ceca0 | 237,406 | 237,406 (as reported; low against 152 tool uses, likely compaction) | 152 | 27.1 |
| 2026-11-19 13:43 | Phase 10C | reader C | ae83a693644bdf1dc | 206,040 | 206,040 | 25 | 8.3 |
| 2026-11-19 13:43 | Phase 10C | reader A | ab5d6702e7133dc82 | 210,731 | 210,731 | 27 | 8.9 |
| 2026-11-19 13:44 | Phase 10C | reader B | a708cb7e27d160bf3 | 209,095 | 209,095 | 19 | 9.3 |
| 2026-11-19 13:47 | Phase 10C | Round 3, reader B | a708cb7e27d160bf3 | 257,702 | 48,607 | 2 | 1.4 |
| 2026-11-19 13:47 | Phase 10C | Round 3, reader A | ab5d6702e7133dc82 | 260,670 | 49,939 | 2 | 1.7 |
| 2026-11-19 13:47 | Phase 10C | Round 3, reader C | ae83a693644bdf1dc | 257,283 | 51,243 | 2 | 1.7 |
| 2026-11-19 13:51 | Phase 10 | Round 3, reader C | a6d2fde08b3308891 | 259,528 | 81,967 | 9 | 2.3 |
| 2026-11-19 13:51 | Phase 10 | Round 3, reader A | a8512e8622c5ceca0 | 323,048 | 85,642 | 17 | 2.6 |
| 2026-11-19 13:51 | Phase 10 | Round 3, reader B | afda8b0f677e90431 | 311,761 | 90,223 | 12 | 3.0 |
| 2026-11-19 13:59 | Phase 10R | reader A | a2680014a5d996970 | 386,401 | 386,401 | 146 (113 web) | 23.0 |
| 2026-11-19 13:59 | Phase 10R | reader C | a0e3ef825f1aa7435 | 374,411 | 374,411 | 155 (103 web) | 27.0 |
| 2026-11-19 14:00 | Phase 10R | reader B | a50d469a441911aba | 395,694 | 395,694 | 161 (110 web) | 28.2 |
| 2026-11-19 14:03 | Phase 10R | Round 3, reader C | a0e3ef825f1aa7435 | 444,338 | 69,927 | 7 | 1.8 |
| 2026-11-19 14:04 | Phase 10R | Round 3, reader A | a2680014a5d996970 | 464,067 | 77,666 | 7 | 2.3 |
| 2026-11-19 14:04 | Phase 10R | Round 3, reader B | a50d469a441911aba | 469,742 | 74,048 | 7 | 2.4 |
| 2026-11-19 14:14 | Phase 10 | repair, reader A | a8512e8622c5ceca0 | 335,337 | 12,289 | 5 | 0.5 |
| 2026-11-19 14:14 | Phase 10 | repair, reader B | afda8b0f677e90431 | 326,499 | 14,738 | 12 | 1.0 |
| 2026-11-19 14:14 | Phase 10 | re-verdict, reader A | a8512e8622c5ceca0 | 338,805 | 3,468 | 7 | 0.5 |
| 2026-11-19 14:14 | Phase 10 | re-verdicts, reader C | a6d2fde08b3308891 | 265,118 | 5,590 | 11 | 0.7 |
| 2026-11-20 05:23 | Phase 10R | research merge (Entry 3) | a685f057e947dc906 | 284,363 | 284,363 | 35 | 13.7 |
| 2026-11-20 05:30 | Phase 10R2 u2 | reader B | a7dc8436f9542ebdc | 404,429 | 404,429 | 126 (90 web) | 22.0 |
| 2026-11-20 05:32 | Phase 10R2 u3 | reader A | a840afcb48c13671f | 412,981 | 412,981 | 127 (83 web) | 24.6 |
| 2026-11-20 05:32 | Phase 10R2 u3 | reader B | a53d95721d00536c0 | 413,637 | 413,637 | 128 (87 web) | 24.8 |
| 2026-11-20 05:34 | Phase 10R2 u2 | reader A | a96d2dd325873730c | 396,310 | 396,310 | 133 (90 web) | 26.3 |
| 2026-11-20 05:35 | Phase 10R2 u2 | reader C | a57032566839a55bc | 397,508 | 397,508 | 130 (86 web) | 27.0 |
| 2026-11-20 05:35 | Phase 10R2 u1 | reader C | adf290d90ee74078f | 394,276 | 394,276 | 121 (90 web) | 27.0 |
| 2026-11-20 05:35 | Phase 10R2 u1 | reader B | aec4b9a526189d74c | 421,991 | 421,991 | 143 (89 web) | 27.5 |
| 2026-11-20 05:36 | Phase 10R2 u2 | repair, reader B | a7dc8436f9542ebdc | 404,743 | 314 | 3 | 0.2 |
| 2026-11-20 05:36 | Phase 10R2 u1 | reader A | a482c2bba4a8e7752 | 424,418 | 424,418 | 121 (88 web) | 27.9 |
| 2026-11-20 05:37 | Phase 10R2 u3 | reader C | a4b39ae9e149ae569 | 440,477 | 440,477 | 125 (85 web) | 29.1 |
| 2026-11-20 05:39 | Phase 10R2 u2 | Round 3, reader B | a7dc8436f9542ebdc | 509,405 | 104,662 | 7 | 3.1 |
| 2026-11-20 05:39 | Phase 10R2 u1 | Round 3, reader B | aec4b9a526189d74c | 525,097 | 103,106 | 7 | 3.0 |
| 2026-11-20 05:40 | Phase 10R2 u2 | Round 3, reader A | a96d2dd325873730c | 504,769 | 108,459 | 4 | 3.8 |
| 2026-11-20 05:40 | Phase 10R2 u1 | Round 3, reader A | a482c2bba4a8e7752 | 523,086 | 98,668 | 5 | 3.2 |
| 2026-11-20 05:40 | Phase 10R2 u2 | Round 3, reader C | a57032566839a55bc | 502,234 | 104,726 | 7 | 3.9 |
| 2026-11-20 05:41 | Phase 10R2 u1 | Round 3, reader C | adf290d90ee74078f | 505,599 | 111,323 | 7 | 4.0 |
| 2026-11-20 05:41 | Phase 10R2 u3 | Round 3, reader A | a840afcb48c13671f | 526,338 | 113,357 | 5 | 3.9 |
| 2026-11-20 05:42 | Phase 10R2 u3 | Round 3, reader B | a53d95721d00536c0 | 526,360 | 112,723 | 5 | 4.3 |
| 2026-11-20 05:42 | Phase 10R2 u3 | Round 3, reader C | a4b39ae9e149ae569 | 551,308 | 110,831 | 5 | 4.6 |
| 2026-11-20 06:03 | Phase 10R2 u2 | research merge (Entry 5) | a542515cdf6eeab01 | 377,244 | 377,244 | 41 | 21.9 |
| 2026-11-20 06:05 | Phase 10R2 u1 | research merge (Entry 4) | a6bcb8e2cae2035c2 | 395,128 | 395,128 | 36 | 23.8 |
| 2026-11-20 06:09 | Phase 10R2 u3 | research merge (Entry 6) | a366d419d46f6e887 | 398,044 | 398,044 | 51 | 24.8 |
| 2026-11-20 06:29 | Phase 10 | merge, stage A | a2b26ae9899c6f3c2 | 410,379 | 410,379 | 45 | 19.4 |
| 2026-11-20 06:38 | Phase 10 | merge, stage B1 | a28fa8261db3f0f4d | 308,959 | 308,959 | 28 | 9.9 |
| 2026-11-20 06:41 | Phase 10 | merge, stage B2 | ac4838d4ca4880a45 | 367,544 | 367,544 | 43 | 12.2 |
| 2026-11-20 07:04 | Step 5 A1 | reader C | ad6e6945ba933e4f1 | 512,331 | 512,331 | 74 | 13.3 |
| 2026-11-20 07:05 | Step 5 A2 | reader B | a9c5e80b1ac51e13a | 471,561 | 471,561 | 71 | 14.1 |
| 2026-11-20 07:05 | Step 5 A2 | reader C | a24ded4aa8b17378d | 470,842 | 470,842 | 68 | 14.4 |
| 2026-11-20 07:07 | Step 5 A1 | reader A | a9f53404197bd8bcb | 557,951 | 557,951 | 81 | 15.8 |
| 2026-11-20 07:07 | Step 5 A1 | reader B | a7dcce33ffe45608c | 544,258 | 544,258 | 88 | 16.3 |
| 2026-11-20 07:08 | Step 5 A2 | reader A | a0391f0acfcfcd1a3 | 487,617 | 487,617 | 69 | 16.5 |
| 2026-11-20 07:09 | Step 5 A1 | Round 3, reader C | ad6e6945ba933e4f1 | 580,104 | 67,773 | 4 | 1.7 |
| 2026-11-20 07:10 | Step 5 A1 | Round 3, reader A | a9f53404197bd8bcb | 624,784 | 66,833 | 4 | 2.0 |
| 2026-11-20 07:10 | Step 5 A2 | Round 3, reader A | a0391f0acfcfcd1a3 | 552,026 | 64,409 | 4 | 1.7 |
| 2026-11-20 07:10 | Step 5 A1 | Round 3, reader B | a7dcce33ffe45608c | 610,312 | 66,054 | 4 | 2.3 |
| 2026-11-20 07:10 | Step 5 A2 | Round 3, reader C | a24ded4aa8b17378d | 536,092 | 65,250 | 5 | 1.8 |
| 2026-11-20 07:10 | Step 5 A2 | Round 3, reader B | a9c5e80b1ac51e13a | 540,062 | 68,501 | 4 | 1.9 |
| 2026-11-20 07:28 | Step 5 | merge, stage A | a0f0a54528ec0df94 | 352,444 | 352,444 | 45 | 17.6 |
| 2026-11-20 07:45 | Step 5 B | reader C | a5bfbe85a5ecaa6f0 | 326,217 | 326,217 | 40 | 15.8 |
| 2026-11-20 07:47 | Step 5 B | reader A | af39240a5605140e7 | 337,930 | 337,930 | 40 | 17.5 |
| 2026-11-20 07:48 | Step 5 B | reader B | a5beb5224e4698b27 | 345,814 | 345,814 | 46 | 18.0 |
| 2026-11-20 07:48 | Step 5 B | repair, reader B | a5beb5224e4698b27 | 351,023 | 5,209 | 10 | 0.5 |
| 2026-11-20 07:48 | Step 5 B | repair, reader A | af39240a5605140e7 | 343,222 | 5,292 | 10 | 0.5 |
| 2026-11-20 07:48 | Step 5 B | repair, reader C | a5bfbe85a5ecaa6f0 | 331,758 | 5,541 | 10 | 0.5 |
| 2026-11-20 07:50 | Step 5 B | repair 2, reader C | a5bfbe85a5ecaa6f0 | 333,128 | 1,370 | 2 | 0.2 |
| 2026-11-20 07:51 | Step 5 B | repair 2, reader A | af39240a5605140e7 | 358,490 | 15,268 | 25 | 1.2 |
| 2026-11-20 07:53 | Step 5 B | Round 3, reader B | a5beb5224e4698b27 | 430,275 | 79,252 | 5 | 2.0 |
| 2026-11-20 07:53 | Step 5 B | Round 3, reader C | a5bfbe85a5ecaa6f0 | 408,499 | 75,371 | 5 | 2.1 |
| 2026-11-20 07:54 | Step 5 B | Round 3, reader A | af39240a5605140e7 | 439,512 | 81,022 | 6 | 2.5 |
| 2026-11-20 08:11 | Step 5 | merge, stage B | ad7c70388eaa69b02 | 347,029 | 347,029 | 31 | 16.6 |
| 2026-11-20 08:20 | Step 6 | reader B | a4177bf4a781378fd | 266,307 | 266,307 | 38 | 6.8 |
| 2026-11-20 08:21 | Step 6 | reader A | a9bef30b0e884e869 | 269,709 | 269,709 | 40 | 7.4 |
| 2026-11-20 08:23 | Step 6 | reader C | afdf554b937b79352 | 298,509 | 298,509 | 50 | 9.7 |
| 2026-11-20 08:24 | Step 6 | repair, reader C | afdf554b937b79352 | 300,478 | 1,969 | 3 | 0.7 |
| 2026-11-20 08:26 | Step 6 | Round 3, reader C | afdf554b937b79352 | 351,301 | 50,823 | 2 | 1.4 |
| 2026-11-20 08:26 | Step 6 | Round 3, reader A | a9bef30b0e884e869 | 325,709 | 56,000 | 2 | 1.8 |
| 2026-11-20 08:26 | Step 6 | Round 3, reader B | a4177bf4a781378fd | 321,638 | 55,331 | 2 | 1.9 |
| 2026-11-20 08:33 | Step 6 | merge | acbff6ffb34cc4f9f | 231,258 | 231,258 | 40 | 6.5 |
| 2026-11-20 08:51 | Step 7 Q2 | reader C | ac0f66ddc77138725 | 404,601 | 404,601 | 65 | 15.7 |
| 2026-11-20 08:51 | Step 7 Q2 | reader A | a0ba2c8c3ab4229c6 | 409,524 | 409,524 | 60 | 16.1 |
| 2026-11-20 08:52 | Step 7 Q2 | reader B | a0d68ec6f03e1c7df | 413,667 | 413,667 | 55 | 16.4 |
| 2026-11-20 08:52 | Step 7 Q3 | reader C | ad9eda89efb796fa2 | 505,561 | 505,561 | 73 | 17.1 |
| 2026-11-20 08:52 | Step 7 Q1 | reader B | a246fd6cf6787aab0 | 476,204 | 476,204 | 63 | 17.1 |
| 2026-11-20 08:53 | Step 7 Q1 | reader C | abd0e0f8c5ebedc72 | 494,109 | 494,109 | 84 | 17.8 |
| 2026-11-20 08:54 | Step 7 Q1 | reader A | a13678bd1c246ddff | 496,647 | 496,647 | 60 | 18.2 |
| 2026-11-20 08:54 | Step 7 Q2 | Round 3, reader A | a0ba2c8c3ab4229c6 | 475,500 | 65,976 | 4 | 1.4 |
| 2026-11-20 08:54 | Step 7 Q2 | Round 3, reader C | ac0f66ddc77138725 | 473,096 | 68,495 | 5 | 1.7 |
| 2026-11-20 08:54 | Step 7 Q3 | reader B | aaceb362dc8b8ce0c | 518,579 | 518,579 | 59 | 18.6 |
| 2026-11-20 08:54 | Step 7 Q3 | reader A | a1ca772d78f98d985 | 516,028 | 516,028 | 78 | 18.6 |
| 2026-11-20 08:55 | Step 7 Q2 | Round 3, reader B | a0d68ec6f03e1c7df | 482,730 | 69,063 | 5 | 1.9 |
| 2026-11-20 08:56 | Step 7 Q1 | Round 3, reader B | a246fd6cf6787aab0 | 556,038 | 79,834 | 4 | 1.8 |
| 2026-11-20 08:56 | Step 7 Q1 | Round 3, reader A | a13678bd1c246ddff | 568,900 | 72,253 | 5 | 1.9 |
| 2026-11-20 08:56 | Step 7 Q1 | Round 3, reader C | abd0e0f8c5ebedc72 | 571,265 | 77,156 | 4 | 2.1 |
| 2026-11-20 08:57 | Step 7 Q3 | Round 3, reader C | ad9eda89efb796fa2 | 581,686 | 76,125 | 6 | 1.7 |
| 2026-11-20 08:57 | Step 7 Q3 | Round 3, reader A | a1ca772d78f98d985 | 589,137 | 73,109 | 5 | 1.9 |
| 2026-11-20 08:57 | Step 7 Q3 | Round 3, reader B | aaceb362dc8b8ce0c | 600,028 | 81,449 | 5 | 2.4 |
| 2026-11-20 09:22 | Step 7 | merge writer | a155dafefbf66582d | 512,336 | 512,336 | 87 | 23.5 |
| 2026-11-20 09:32 | Step 8 R3 | reader C | af449a6df3da9505e | 397,551 | 397,551 | 41 | 9.3 |
| 2026-11-20 09:34 | Step 8 R1 | reader B | a67269888cc8d366b | 357,312 | 357,312 | 48 | 11.8 |
| 2026-11-20 09:35 | Step 8 R1 | reader C | a8d28e9476bdc1711 | 361,819 | 361,819 | 52 | 12.1 |
| 2026-11-20 09:35 | Step 8 R2 | reader B | acd852efbd8b445b1 | 344,508 | 344,508 | 47 | 12.4 |
| 2026-11-20 09:35 | Step 8 R2 | reader A | a8f14ca55d638c092 | 353,726 | 353,726 | 48 | 13.0 |
| 2026-11-20 09:36 | Step 8 R2 | reader C | accc28bed23135a59 | 353,117 | 353,117 | 56 | 13.2 |
| 2026-11-20 09:36 | Step 8 R1 | reader A | ade6f869eee9908dd | 376,785 | 376,785 | 54 | 13.5 |
| 2026-11-20 09:37 | Step 8 R3 | reader A | a97fbdac1f907abf0 | 431,833 | 431,833 | 62 | 13.8 |
| 2026-11-20 09:38 | Step 8 R3 | reader B | a4b8ee9c1a5af3787 | 443,976 | 443,976 | 55 | 15.3 |
| 2026-11-20 09:38 | Step 8 R2 | Round 3, reader C | accc28bed23135a59 | 404,443 | 51,326 | 2 | 1.5 |
| 2026-11-20 09:39 | Step 8 R2 | Round 3, reader B | acd852efbd8b445b1 | 396,214 | 51,706 | 2 | 1.7 |
| 2026-11-20 09:39 | Step 8 R1 | Round 3, reader A | ade6f869eee9908dd | 433,290 | 56,505 | 2 | 1.8 |
| 2026-11-20 09:39 | Step 8 R1 | Round 3, reader C | a8d28e9476bdc1711 | 418,680 | 56,861 | 2 | 1.8 |
| 2026-11-20 09:39 | Step 8 R2 | Round 3, reader A | a8f14ca55d638c092 | 409,387 | 55,661 | 2 | 2.0 |
| 2026-11-20 09:39 | Step 8 R1 | Round 3, reader B | a67269888cc8d366b | 414,060 | 56,748 | 2 | 2.0 |
| 2026-11-20 09:40 | Step 8 R3 | Round 3, reader A | a97fbdac1f907abf0 | 486,126 | 54,293 | 2 | 1.9 |
| 2026-11-20 09:40 | Step 8 R3 | Round 3, reader C | af449a6df3da9505e | 454,064 | 56,513 | 2 | 1.9 |
| 2026-11-20 09:41 | Step 8 R3 | Round 3, reader B | a4b8ee9c1a5af3787 | 496,022 | 52,046 | 2 | 2.0 |
| 2026-11-20 09:59 | Step 8 | merge writer | a6a8e45676f2fa9af | 424,373 | 424,373 | 68 | 18.4 |
| 2026-11-20 10:13 | Step 9 | reader B | a0ac10e43fde52717 | 247,292 | 247,292 | 64 | 13.0 |
| 2026-11-20 10:14 | Step 9 | reader A | a4fc08750a7fd7ba6 | 259,580 | 259,580 | 65 | 13.9 |
| 2026-11-20 10:15 | Step 9 | reader C | ae32dd3816ba6e283 | 274,866 | 274,866 | 72 | 15.2 |
| 2026-11-20 10:18 | Step 9 | Round 3, reader A | a4fc08750a7fd7ba6 | 331,565 | 71,985 | 4 | 1.9 |
| 2026-11-20 10:18 | Step 9 | Round 3, reader B | a0ac10e43fde52717 | 326,226 | 78,934 | 7 | 2.2 |
| 2026-11-20 10:18 | Step 9 | Round 3, reader C | ae32dd3816ba6e283 | 348,693 | 73,827 | 4 | 2.3 |
| 2026-11-20 10:37 | Step 9 | merge writer | a99fc70383f09d5e0 | 336,804 | 336,804 | 54 | 18.0 |
| 2026-11-20 10:49 | Step 10 | reader B | ab50ccee84a1114c2 | 207,147 | 207,147 | 36 | 9.8 |
| 2026-11-20 10:50 | Step 10 | reader C | a3abd1af894fabe32 | 207,504 | 207,504 | 36 | 10.0 |
| 2026-11-20 10:50 | Step 10 | reader A | a9dc713a1f997434e | 211,121 | 211,121 | 37 | 10.7 |
| 2026-11-20 10:52 | Step 10 | Round 3, reader A | a9dc713a1f997434e | 262,012 | 50,891 | 2 | 1.7 |
| 2026-11-20 10:52 | Step 10 | Round 3, reader C | a3abd1af894fabe32 | 260,409 | 52,905 | 2 | 1.7 |
| 2026-11-20 10:52 | Step 10 | Round 3, reader B | ab50ccee84a1114c2 | 261,385 | 54,238 | 3 | 2.0 |
| 2026-11-20 11:01 | Step 10 | merge writer | a45bf9576ac822f6a | 214,283 | 214,283 | 22 | 8.7 |

## Per unit (filled when each unit is recorded)
| Unit | Readers | Round 3, repairs, addenda | Merge | Helpers | Unit total | Web calls |
|---|--:|--:|--:|--:|--:|--:|
| Readiness check before Step −1 | 0 | 0 | 0 | 0 | **0** (orchestrator only; no subagent) | 0 (tool: 0) |
| Step −1 (input contract) | 530,983 | 147,605 | 235,417 | 0 | **914,005** | 0 (tool: 0) |
| Step 0 (frame; Phase 0) | 776,853 | 193,062 | 276,962 | 0 | **1,246,877** | 0 (tool: 0) |
| Step 1 (audit of inherited material) | 690,278 | 149,958 | 199,176 | 0 | **1,039,412** | 0 (tool: 0) |
| Step 2 (spine; Phase 1) | 1,214,668 | 281,804 (Round 3 279,940 · repair 1,864) | 324,562 | 0 | **1,821,034** | 0 (tool: 0) |
| Step 3 (research) | 1,603,430 | 289,366 (Round 3 288,755 · repairs 611) | 358,608 | 0 | **2,251,404** | 256 by readers (A 73 · B 95 · C 88); tool: 284 |
| Phase 2 (composition and arrival) | 1,328,663 | 197,331 | 235,482 | 0 | **1,761,476** | 0 (tool: 284, unchanged) |
| Phase 3 (surface and texture) | 1,380,532 | 221,612 | 277,595 | 0 | **1,879,739** | 0 (tool: 284, unchanged) |
| Phase 4 (ordinary life) | 1,690,389 | 226,262 | 283,223 | 0 | **2,199,874** | 0 (tool: 284, unchanged) |
| Phase 5 (relation and geometry) | 1,855,074 | 252,528 (Round 3 250,787 · repair 1,741) | 308,193 | 0 | **2,415,795** | 0 (tool: 284, unchanged) |
| Phase 6 (meaning) | 1,898,619 | 209,863 (Round 3 208,711 · repairs 1,152) | 268,738 | 0 | **2,377,220** | 0 (tool: 284, unchanged) |
| Phase 7 (order) | 2,234,021 | 321,160 (Round 3) | 334,283 | 0 | **2,889,464** | 0 (tool: 284, unchanged) |
| Phase 8 (making) | 2,279,135 | 246,169 (Round 3) | 249,905 | 0 | **2,775,209** | 0 (tool: 284, unchanged) |
| Phase 9 (populations) | 2,473,066 | 304,872 (Round 3 304,643 · repair 229) | 294,890 | 0 | **3,072,828** | 0 (tool: 284, unchanged) |
| Phase 10R2 u1 (candidate rows 1–29) | 1,240,685 | 313,097 (Round 3) | 395,128 | 0 | **1,948,910** | 267 (readers) |
| Phase 10R2 u2 (candidate rows 30–58) | 1,198,247 | 318,161 (Round 3 317,847 · repair 314) | 377,244 | 0 | **1,893,652** | 266 (readers) |
| Phase 10R2 u3 (candidate rows 59–85) | 1,267,095 | 336,911 (Round 3) | 398,044 | 0 | **2,002,050** | 255 (readers) |
| Phase 10R2, all three (tool after Round 1: 891 for the session) | 3,706,027 | 968,169 | 1,170,416 | 0 | **5,844,612** | 788 (readers) · tool 891 |
| Phase 10 (catalog; readers, repairs, re-verdicts; merge stage A 410,379 · B1 308,959 · B2 367,544) | 930,422 (last figures) | (in readers' last figures) | 1,086,882 | 0 | **2,017,304** | 62 (readers) |
| Phase 10R (research on the official picks) | 1,378,147 (last figures, incl. Round 3) | (in readers' last figures) | 284,363 | 0 | **1,662,510** | 326 (readers) |
| Phase 10C (candidate reading check, no web) | 775,655 (last figures, incl. Round 3) | (in readers' last figures) | 0 | 0 | **775,655** | 0 |
| **Phase 10, all six units** (Phase 10, 10R, 10C, 10R2 u1–u3) | | | | | **10,300,081** | 1,176 (readers) |
| Step 5 (A1 1,815,200 · A2 1,628,180 · B 1,278,286; readers with repairs and Round 3) | 4,721,666 | (in readers' last figures) | 699,473 (stage A 352,444 · stage B 347,029) | 0 | **5,421,139** | 0 |
| Step 6 (write-only differentiation) | 998,648 (last figures, incl. repair and Round 3) | (in readers' last figures) | 231,258 | 0 | **1,229,906** | 0 |
| Step 7 (QA gates; Q1 1,696,203 · Q2 1,431,326 · Q3 1,770,851; readers with Round 3) | 4,898,380 (last figures, incl. Round 3) | (in readers' last figures) | 512,336 | 0 | **5,410,716** | 0 |
| Step 8 (Review Panel; R1 1,266,030 · R2 1,210,044 · R3 1,436,212; readers with Round 3) | 3,912,286 (last figures, incl. Round 3) | (in readers' last figures) | 424,373 | 0 | **4,336,659** | 0 |
| Step 9 (record; readers with Round 3) | 1,006,484 (last figures, incl. Round 3) | (in readers' last figures) | 336,804 | 0 | **1,343,288** | 0 |
| Step 10 (readiness check; readers with Round 3) | 783,806 (last figures, incl. Round 3) | (in readers' last figures) | 214,283 | 0 | **998,089** | 0 |

## The run's totals (filled at Step 10)
| Measure | Value |
|---|---|
| Subagent tokens, all units | **55,684,215** (readiness check 0 · Steps −1 to 3: 7,272,732 · Phases 2–9: 19,371,605 · Phase 10, six units: 10,300,081 · Step 5: 5,421,139 · Steps 6–10: 13,318,658); per-unit rows above |
| Allotment at start · at end · used | start **12%** (2026-11-18 13:16) · end **53%** (2026-11-20 13:10, given by the developer on their return; Step 10 was recorded ~11:05 and nothing ran in between) · used: **41 points** of the weekly allotment (day 1: 2 points · day 2: 21 points · day 3, this session: 18 points). ⚠ **Provisional** (developer, 2026-11-20): it may be **50–55%**, since the developer recalls the allotment starting at zero after a manual reset and what used the 12 points before the run is not known for certain; Kunlun's full run (week of 2026-11-29) is expected to give the more accurate figure. See `ULM_Token_Measurements.md`'s allotment note. |
| Orchestrator share (meter used minus subagent sum, approximate) | **Not computable as a subtraction:** the meter reads in percent of the weekly allotment and its size in tokens is not shown, so the subagent sum cannot be taken away from it. What the readings do give: 41 points covered 55,684,215 subagent tokens **plus** all of the orchestrator's, so one point stood for at least ~1.36 million tokens of run work. The orchestrator's own share stays unmeasured. |
| Web calls (readers' counts · the tool's count) | readers **1,432** (Step 3: 256 · Phase 10: 62 · 10R: 326 · 10R2: 788); the tool: 284 for the first session's Step 3 (see its row), 891 for this session after 10R2's Round 1, no web call after that; per-session tool counts are in the rows |
