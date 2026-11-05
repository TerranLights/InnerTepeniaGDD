# Mirny: language shares by actual speakers (2026-11-04)

**Status: PROPOSED, a calculation for the developer's decision (DEC-011). Nothing in any pass, spec, culture file or ruling was changed.** Requested by the developer on 2026-11-04 ("See if you can calculate by actual speakers and find out what those numbers look like based on time-zone geography"); hours waived by the developer for this named task, result held for in-window review. Mirny only, on its own terms; no other city is read, ranked or compared.

## What was computed
Mirny's composition table already comes from its time-zone window, so it was kept exactly as it is (36 national-origin rows, shares totaling 99.98 %; the rows are in `../Language_Blocs_By_City_2026-11-03.md`, section Mirny). The earlier arithmetic put each nation's whole share into one language. This calculation instead multiplies each row's share by the share of that nation's people who can function in each language (native speakers plus fluent second-language speakers, the developer's supporting-tier definition). Five research files (this folder, `01` to `05`) hold the real-world figures, each with what the source measured, its year and a confidence level. Script and inputs: `07_speakers_calc.py`.

## Result: share of Mirny's people who can function in each language
| Language | Low % | Best % | High % | Largest contributors (best) |
|---|--:|--:|--:|---|
| English | 29.1 | 32.8 | 37.3 | United Kingdom 13.5; Australia 6.7; New Zealand 4.1; Philippines 2.0; Malaysia 1.7; Korea 0.9; South Africa 0.8; Indonesia 0.6 |
| Mandarin | 14.7 | 16.2 | 17.6 | Sinian Federation 10.5; Taiwan 2.8; Manchuria 0.9; Malaysia 0.65; Mongolia 0.4; East Turkestan 0.3 |
| Korean | 13.3 | 13.5 | 14.1 | Korea 13.5 |
| Indonesian | 11.7 | 12.1 | 12.7 | Indonesia 11.7; West Papua 0.2; Aceh 0.2 |
| Russian | 9.2 | 9.4 | 10.1 | Russia (core state) 2.1; Idelsk-Uralia 2.1; Belarus 1.45; Kazakhstan 1.2; Siberia 0.85; Donska-Kubania 0.8; Künnarantaiga 0.5 |
| Japanese | 7.7 | 7.9 | 8.7 | Japan 7.7; Korea 0.2 |

Shares are not additive: a person who speaks English and Russian counts in both rows. Cells the research files call negligible are counted as 0 low, 0 best and 0.5 % high.

**Where the English figure comes from:** 24.5 points from the four nations whose people are native English speakers (United Kingdom, Northern Ireland, Australia, New Zealand) and 8.3 points from everyone else's second-language English.
**Russian:** 6.7 points from the thirteen successor states of Russia (Finland's Karelia row included), 2.7 from Belarus and Kazakhstan. Russian is near-universal as a second language in those places, so the successor states are fully counted, and the language still tops out at 9.4 % because those rows are about 9.5 % of Mirny.

## The 12-point test on speaker shares (supporting tier = within 12 points of the largest)
| English against | Gap at best estimates | Closest case (English low against the other's high) |
|---|--:|--:|
| Mandarin | 16.6 | 11.5 |
| Korean | 19.3 | 15.1 |
| Indonesian | 20.7 | 16.4 (13.2 if Malaysia's Malay speakers are counted as Indonesian speakers) |
| Russian | 23.4 | 19.0 |
| Japanese | 24.9 | 20.4 |

**Reading:** On actual speakers English is the largest by a wide margin and, at best estimates, no other language is within 12 points. Mandarin comes within 12 only in the single most favorable corner (English at its lowest estimate against Mandarin at its highest), a gap of 11.5, which is the same kind of near-end result the national-origin arithmetic gave (8.5). Russian is not close in any case: 9.4 % of Mirny, 19 or more points behind English even in the corner case. Counting speakers does not change the answer to the earlier Russian question; it puts Russian below where the national-origin arithmetic did at its high end, because the old high end (9.73 %) counted every row that might speak Russian as fully Russian.

## How strong the numbers are
- **Strong (census or national survey, high or medium confidence):** the English-native nations (United Kingdom, Northern Ireland, Australia, New Zealand), Russian in the successor states where regional census tables exist (Tatarstan, Bashkortostan, Buryatia and the national figure), Korean in Korea, Japanese in Japan, Indonesian in Indonesia (BPS census, "can speak").
- **Weak (modeled or judged):** English in most of Asia and in Russia's regions (national surveys and test scores, not regional census rates; the Rosstat tables did not load), Mandarin ability in the western and highland rows (derived, no regional rates exist), Malay and English in Malaysia (no census or random survey exists), the six small Caucasus republics (estimates from ethnic shares), Thai in Patani, English in Thailand and Vietnam (no survey; Vietnam's circulating "53.81 %" is a misread test score and was rejected).
- **How much the verdict depends on second-language English (checked, and corrected here from an earlier wrong sentence):** 24.5 of English's 32.8 points come from the four native-English nations; 8.3 come from second-language English elsewhere (low case 5.0, high case 12.6), and those are the weak cells. If all of that were zero, English would be 24.5 and its lead would be 8.3 over Mandarin (inside 12), 11.0 over Korean (inside 12), 12.5 over Indonesian, 15.1 over Russian and 16.6 over Japanese. To keep Mandarin outside the 12-point band English needs at least 3.7 points of second-language English from outside the native-English nations (best estimate 8.3, low estimate 5.0), and to keep Korean outside it needs at least 0.95. So: **Russian, Japanese and Indonesian stay outside the tier whatever the weak cells turn out to be; the Mandarin and Korean verdicts rest on second-language English being at least a few points, which every estimate here supports but which is not measured precisely.**
- **Not counted:** Hawaiian (later Tepenian), the dominant language by ruling; regional languages below 10 % of their own nation; the minority languages inside the Sinian Federation (Cantonese, Wu, Min, Hakka), which are not separately modeled.
- **One interpretation to flag:** Malay and Indonesian are standard forms of nearly the same language. The table does not count Malaysians as Indonesian speakers (no source measures it); counting Malaysia's Malay speakers would raise Indonesian to 15.2 %.

## What this does and does not settle
It does not make any language other than English a supporting tier by the 12-point rule. It does show that the earlier "English alone" result is not an artifact of assigning each nation to a single language. Whether Russian (or Mandarin) is nonetheless named as a special case, as the language ruling did for another place, is the developer's decision (DEC-011).
