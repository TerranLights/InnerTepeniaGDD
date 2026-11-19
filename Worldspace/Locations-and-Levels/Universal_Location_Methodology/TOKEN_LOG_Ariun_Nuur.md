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

## The run's totals (filled at Step 10)
| Measure | Value |
|---|---|
| Subagent tokens, all units | |
| Allotment at start · at end · used | |
| Orchestrator share (meter used minus subagent sum, approximate) | |
| Web calls (readers' counts · the tool's count) | |
