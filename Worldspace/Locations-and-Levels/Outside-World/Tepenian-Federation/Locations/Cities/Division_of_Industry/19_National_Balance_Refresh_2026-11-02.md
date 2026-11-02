# National food balance and slack, refreshed for Esperanza's relocation (2026-11-02, `DR-90`)

> **Status: A REFRESH RECORD, like `17`.** No existing Division of Industry file was rewritten (one-line pointers were added to the titles of `04`, `13` and `17`). **Not a new model:** it re-runs `17`'s method under **convention B**, the national convention (`DR-73`: mandated-role percentages are shares of the distinctive tier under the three-tier method), on today's Census I populations, after Esperanza was reduced from 1,902,205 to 1,200,000 and its 702,205 were divided across the other non-island cities (`Universal_Location_Methodology/Population_Scenario_Esperanza_Relocation_2026-11-02.md`). Conventions A and C of `17` stay as the record of what other files assumed and were not re-run. **Slack = export capacity − the forced importers' humans** (`13` §15, `17` §0).

## 1 · What changed in the inputs

| Input | `17` §5 (after the Santa Luce scenario, `DR-68`) | Now |
|---|--:|--:|
| Humans in the forced importers (Halley, Neumayer, Vostok/Ariun Nuur, Byrd, Amundsen Station) | 1,689,045 | **1,748,771** (+59,726: each of the four continental ones gained about 14,930 humans; Amundsen Station's share went to the maritime fleet) |
| Import need (× 0.1207 × 1.20) | 244,641 | **253,292** |
| **Davis**: workforce, baseline, distinctive tier, agriculture (35%) | 894,362; 40.8%; 529,809; 185,433 | 915,098; 40.8%; 541,564; **189,548** |
| **Esperanza**: workforce, baseline, distinctive tier, agriculture (15%) | 1,418,467; 39.7%; 855,567; 128,335 | **894,835**; 39.7%; **539,733**; **80,960** |
| **Relung Panen** (D = 1.43, `DR-72`): workforce, baseline, distinctive tier, agriculture (25%, `DR-71`) | 733,228; 44.0%; 411,031; 102,758 | 753,964; 44.0%; 422,139; **105,535** |
| Terraformed belt; marine capture at its cap | 36,000; 15,600 | unchanged |

*The three-tier arithmetic is `17` §1b: baseline = humans × (120.7 × D + 85.6) ÷ 1,000 + residents × (64 × D + 113.2) ÷ 1,000, with food factor 1.00 for all three cities. It reproduces the `17` and `16` figures for Davis and Esperanza before the change (40.76% and 39.69%). Esperanza's `16` §11 table was refreshed with its held shares (39.7 / 60.3), so §11's agriculture is 80,938; the 22-person difference is rounding.*

## 2 · The result (convention B)

| | `17` §5, before | **Now** |
|---|--:|--:|
| **Export supply, with Relung Panen** (Davis + Esperanza + Relung Panen + belt + marine) | 468,126 | **427,642** (−40,484, −8.6%) |
| Balance (supply − import need) | +223,485 (+91%) | **+174,350 (+69%)** |
| Export capacity (people fed) | 3,232,022 | **2,952,513** |
| **Slack, with Relung Panen** | **9.9%** of national humans | **7.7%** (1,203,742 people) |
| Supply, without Relung Panen | 365,368 | 322,107 |
| Balance without Relung Panen | +120,727 (+49%) | +68,815 (+27%) |
| **Slack, without Relung Panen** | **5.3%** | **3.0%** (475,113 people) |

**Who supplies it.**

| Share of export supply (with Relung Panen) | Before | Now |
|---|--:|--:|
| Davis | 39.6% | **44.3%** |
| Esperanza | 27.4% | **18.9%** |
| Relung Panen | 22.0% | **24.7%** |
| Davis and Esperanza together | 67.0% | 63.3% |
| (without Relung Panen) Davis and Esperanza together | 85.9% | 84.0% |

## 3 · What it means

- **The country still feeds itself with room to spare.** The balance is still a large surplus (+69% with Relung Panen, +27% without it), so nothing here creates a deficit.
- **The slack, the room for people to work outside food, drops by about 2.2 points** with Relung Panen (9.9% → 7.7%) and by 2.3 without it (5.3% → 3.0%). **Without Relung Panen the margin is now thin**: about 3% of the country's humans could work outside food, so Relung Panen's food role (`DR-71`) is worth more to the national balance than it was.
- **Esperanza is no longer the second pillar.** It feeds about 559,000 people beyond itself (it fed about 886,000 before), while Davis feeds about 1,309,000 and Relung Panen about 729,000. Davis alone is now 44% of export supply; Esperanza is third. The 'breadbasket' identity belongs to Davis.
- **The cause is arithmetic, not an event:** Esperanza's workforce fell by 37% and its farm share with it, while the recipients' extra people mostly raised baselines (the forced importers' need) and a little of Davis's and Relung Panen's supply.

## 4 · Not done / open

- **Conventions A and C** of `17` were not re-run (retained as records).
- The per-city determinations in `16` for the recipients (their counts are still on the old workforces); the Davis/Esperanza denominator question (`16` Register item 11) is unchanged.
- **Wording that may need a look in other files:** statements that Esperanza is "the breadbasket" or a second major food region (`04` §3, the README's early lines, the Esperanza spec and culture files) now overstate it; they were not edited here.
- The census row and founding note for Relung Panen still carry the old "26.0% deficit" wording (`17` §4 item 1).
