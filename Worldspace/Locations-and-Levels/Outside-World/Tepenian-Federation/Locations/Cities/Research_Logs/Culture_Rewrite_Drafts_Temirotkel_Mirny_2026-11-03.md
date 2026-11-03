# Rewrite drafts for the Temirötkel and Mirny culture files (2026-11-03)

**Status: DRAFT FOR REVIEW. Nothing here is applied.** Neither culture file was edited. Both files were built on a "China is the Primary" frame that the population rework (`DR-85`) ended. No web research was done; every figure comes from the two spec tables (`Specs/Mawson subnet/Temirotkel.md`, `Specs/Mirny subnet/Mirny.md`) and `Founding_Register.md`. Sums marked DERIVED are mine.

**Rules followed.** One location on its own terms: no other city is named in any proposed text. Founders come only from `Founding_Register.md`; a station's real-world builder is not a founder. Language: Hawaiian (later Tepenian) is the civic default; the next language is that of whoever holds a majority; no majority means the second-language slot is left open, and the draft says so. (Contrapunto's English and Spanish supporting tier is that city's own ruling and is not used here.) Where a passage describes invented culture (food, music, belief) that rested on the old frame, the draft removes the false demographic claim and marks the cultural content for the ULM pass instead of inventing a replacement.

## Current facts used

| | Temirötkel (spec) | Mirny (spec) |
|---|---|---|
| Primary | Australia 9.37%, Indonesia 9.34%, United Kingdom 8.78%, Germany 7.81% | United Kingdom 13.73%, Korea 13.71%, Indonesia 12.03%, Sinian Federation 12.00%, Japan 7.81%, Australia 6.96% |
| Significant | Sinian Federation 5.91%, Korea 5.73%, France 5.66%, Kazakhstan (founding wave) 5.13% | Philippines 4.24%, New Zealand 4.22%, Malaysia 3.44%, Thailand 3.39%, Taiwan 2.86%, Idelsk-Uralia (founding wave) 2.14%, Russia (core state) 2.14%, Vietnam 1.65%, Belarus 1.49%, South Africa 1.47%, Kazakhstan 1.45% |
| Other | Japan 2.62% (Notable), Russia (core state) 0.50% (Notable) | Siberia 0.85% and the rest Notable |
| Largest share | 9.37% (no majority) | 13.73% (no majority) |
| Founders (Register) | Founded and established by Kazakhstan, later assisted in a joint venture, with the CIN providing follow-up support; industrialized primarily by Kazakh industrialists (`DR-30`, `DR-62`) | Founded by Idelsk-Uralia (replacing Russia); exile groups present: Russia, Australia and the Sinian Federation (`DR-9`, `DR-46`, `DR-54`) |

## Developer-decision points (not decided in this draft)

1. **Mirny's rename flag (T0 / M1).** The draft updates the facts only. Whether Mirny keeps its name, is renamed, or stays flagged is yours.
2. **Mirny's identity half "old-and-small beside new-and-large" (M5).** Idelsk-Uralia and Russia are each 2.14%, but two of the three exile groups (Australia 6.96%, Sinian Federation 12.00%) are now Primary. Whether the settlement-layering identity survives, or only the geographic threshold does, is yours.
3. **Who kept the name "Mirny" and why (M4).** The old text says Russia did, as a statement. The Register names Idelsk-Uralia as the establishing country. The draft leaves the "who" open.
4. **Temirötkel's founding tension (T4).** The old tension ("Japan founded it, then diluted") is wrong on the founders and on the frame. The draft offers a replacement built from the Register and the table (Kazakhstan at 5.13% beside four Primaries); whether that is the tension you want is yours.
5. **Whether the invented cultural content that named a Chinese or Russian layer (Mirny food, music, smell, belief; Temirötkel's references to "the subnet pattern") is kept as unverified flavor or cleared for the ULM pass.** The draft clears the demographic claim and keeps the rest, flagged.

## Noticed but not drafted

- **Temirötkel §2 (Founding Story), §6d and the Shōwa-era name passages** still build on Japan as founder and on the former name Sayowa. The file's own banner already calls these revisit items (`DR-30`, `DR-37`, `R-11`, `R-17`). Not part of the China frame, so not rewritten here; T4 only stops repeating the claim.
- **Comparisons to other cities** appear in both files (Temirötkel header and §5b "rank 32nd of ~35"; Mirny L29–35 "no other city", L63–70 and the cuisine correction naming other cities). They conflict with the one-location law and belong to the terminal differentiation pass or a cleanup. Only the ones inside a passage already being rewritten are removed in the drafts below.

---

# PART A · `Local_Cultures/Mawson_Subnet/Temirotkel.md`

### T1 · L24–26 · §1 table
**Old:**
```
| Primary | China |
| Significant | Japan, Germany, France, UK, South Korea, Indonesia, Australia |
| Notable | Poland, Netherlands, Czech Republic, Ukraine, Romania, Norway, Hungary, South Africa, Slovakia, Belarus, Croatia, Bulgaria, Serbia, Lithuania, Slovenia, Latvia, Estonia |
```
**Proposed:**
```
| Primary | Australia, Indonesia, United Kingdom, Germany |
| Significant | Sinian Federation, Korea, France, Kazakhstan *(founding wave)* |
| Notable | Serbia, Netherlands, Slovenia, Croatia, Austro-Bavaria, Lithuania, Norway, Belarus, Latvia, Japan, Romania, Hungary, Czechia, South Africa, Bulgaria, Poland, Estonia, Ukraine, Slovakia, Russia (core state), East Turkestan, Northern Ireland, West Papua, Aceh, Tibet |
```
*[Bracketed old table kept in the correction line below.]* Add under the table: `*(Corrected 2026-11-03 for the population rework, DR-85: the table follows the spec. Old table: Primary China; Significant Japan, Germany, France, UK, South Korea, Indonesia, Australia.)*`
**Reason:** copies the spec's current tiers; China is no longer Primary and four former Significant nations moved up.

### T2 · L28 · §1 note
**Old:** "*Japan, the actual founding nation, sits at Significant tier — diluted by the same China-Primary demographic current that reshaped this whole corner of the continent, consistent with Mawson's own founding-nation dilution pattern (and, before its 2026-07-05 move to Mirny subnet, Sinheung's). **Corrected 2026-07-06:** Temirötkel is no longer the primary Japanese Tepenian presence — that's Shirayuki now (34.20% … ) … Temirötkel's own Japan share is genuinely diluted, down to just 2.71% — plausibly the very outcome Japan's diplomats anticipated … See `Specs/Temirotkel.md` and `Specs/Shirayuki.md` for the full cross-reference.*"
**Proposed:** "*No nation holds a majority: the largest share is Australia's 9.37%, and four nations are Primary (Australia 9.37%, Indonesia 9.34%, the United Kingdom 8.78%, Germany 7.81%). Kazakhstan, which the Founding Register rules as the founder and establisher, is Significant at 5.13% (founding wave). Japan is Notable at 2.62%. The Sinian Federation is Significant at 5.91%. **Corrected 2026-11-03:** the earlier text (China Primary; Japan, \"the actual founding nation\", diluted to Significant at 2.71% by a China-Primary current) rested on a composition and on a founder that no longer stand (`DR-85`, `DR-30`, `DR-62`). See `Specs/Temirotkel.md` for the table.*"
**Reason:** removes the China-Primary frame, the "Japan founded it" claim (Register: Kazakhstan) and the cross-city reference to Shirayuki, Mawson and Sinheung.

### T3 · L62 · §5a Founding tension — **DECISION POINT 4**
**Old:** "- **a. Founding tension** — Japan founded the city and gave it its historically-weighted name, later diluted to Significant tier by the same China-Primary demographic pattern seen across the whole subnet — a standard tension, secondary to the city's structural significance as critical connective infrastructure."
**Proposed:** "- **a. Founding tension** — The Register has Kazakhstan found and establish the city and then industrialize it, yet Kazakhstan holds 5.13% (Significant), below four Primary nations that each hold between 7.81% and 9.37%. The founding nation's industrial work is the city's character (the name *Temirötkel*, \"Iron Crossing\", names the crossing and the iron); its population share is not. This tension is secondary to the city's structural significance as critical connective infrastructure. *(Corrected 2026-11-03: the earlier wording named Japan as founder and a China-Primary dilution; both were superseded. [Old: \"Japan founded the city and gave it its historically-weighted name, later diluted to Significant tier by the same China-Primary demographic pattern seen across the whole subnet.\"])*"
**Reason:** founders come only from the Register; the old pattern no longer exists.

### T4 · L86 · §8a Primary language(s) — language rule
**Old:** "- **a. Primary language(s):** Chinese as the demographic default (matching the subnet-wide pattern). **Corrected 2026-07-06:** Japanese presence here is genuine but no longer \"concentrated\" in the way this file used to claim — Shirayuki is the actual primary Japanese Tepenian city now; Sayowa's Japanese founding carries historical weight (the Shōwa-era name) rather than demographic weight."
**Proposed:** "- **a. Primary language(s):** Hawaiian (later Tepenian) is the civic default, as in every Tepenian location. No nation holds a majority (the largest share is 9.37%), so **the second-language slot is left open**; Kazakh, Indonesian, English, German, Korean, French and Mandarin communities are all present, and which languages are actually maintained is for the ULM pass. *(Corrected 2026-11-03: [old: \"Chinese as the demographic default (matching the subnet-wide pattern)\"]. The 2026-07-06 correction about Japanese presence is moot: Japan is 2.62% (Notable) and is not the founder; the \"Shōwa-era name\" belongs to the former name Sayowa, see the banner and `DR-37`.)*"
**Reason:** applies the Hawaiian-first rule and the no-majority rule; drops the Chinese default.

### T5 · L182 · §20 identity paragraph (the "broad Significant tier" line)
**Old:** "The broad Significant tier (China Primary; Japan, Germany, France, UK, South Korea, Indonesia, Australia Significant) and the extensive Notable list maintain identity through private, personal practice — Temirötkel's public civic face is organized around its junction responsibility rather than any single demographic group. **Corrected 2026-07-06:** no longer framed around a \"concentrated Japanese presence\" — Japan is genuinely diluted here (2.71%), same as every other nation outside China's Primary share."
**Proposed:** "The four Primary nations (Australia, Indonesia, the United Kingdom, Germany), the Significant tier (Sinian Federation, Korea, France, Kazakhstan) and the extensive Notable list maintain identity through private, personal practice — Temirötkel's public civic face is organized around its junction responsibility rather than any single demographic group. **Corrected 2026-11-03:** [old: \"China Primary; Japan, Germany, France, UK, South Korea, Indonesia, Australia Significant\" and \"Japan is genuinely diluted here (2.71%), same as every other nation outside China's Primary share\"]. Japan is now 2.62% (Notable); no nation is singled out by the public face."
**Reason:** same table correction; removes "outside China's Primary share".

### T6 · L198 · §22 Relationship to Upper Earth
**Old:** "Filtered through Temirötkel's own established junction role and its long research-station history, layered against the same China-Primary demographic current that reshaped the whole subnet. **Corrected 2026-07-06:** no longer \"the primary Japanese Tepenian relationship to Upper Earth\" — that distinction belongs to Shirayuki now."
**Proposed:** "Filtered through Temirötkel's own established junction role and its long research-station history, and shaped by a population with no majority: four Primary nations of similar size, so no single national tie to Upper Earth speaks for the city. **Corrected 2026-11-03:** [old: \"layered against the same China-Primary demographic current that reshaped the whole subnet\"]. The 2026-07-06 note about a primary Japanese relationship is moot (Japan 2.62%, Notable)."
**Reason:** removes the China frame and the Shirayuki comparison; states the no-majority fact.

*Other Temirötkel lines that mention Japan or Shirayuki but not China (cuisine L103, fashion L111, music L117, the Concordia diaspora line L275, the Shōwa export and holiday lines L220 and L228) are not drafted: they correct a Japanese framing downward and stay true. Only the "Shōwa" lines belong to the founder/name revisit noted above.*

---

# PART B · `Local_Cultures/Mirny_Subnet/Mirny.md`

### M1 · L3 · Rename flag — **DECISION POINT 1**
**Old:** "*(Flagged 2026-07-08 for an eventual rename — see `TODO.md`'s \"Mirny Rename\" entry. The city's actual national composition no longer resembles the Russian station/ship the name is built around; the founding-tension identity below (Sections 2 and 5 especially) would need to either survive under a new name or be replaced entirely once this is picked up. Not resolved now.)*"
**Proposed (facts updated; the flag is unchanged and undecided):** "*(Flagged 2026-07-08 for an eventual rename — see `TODO.md`'s \"Mirny Rename\" entry. **Updated 2026-11-03 for `DR-85`:** the national composition resembles the Russian station and ship the name is built around even less than when flagged. Russia (core state) and Idelsk-Uralia, the establishing country, are each 2.14% (Significant, together 4.28%, DERIVED); six other nations are Primary (United Kingdom 13.73%, Korea 13.71%, Indonesia 12.03%, Sinian Federation 12.00%, Japan 7.81%, Australia 6.96%). The identity in Sections 2 and 5 would need to survive under a new name or be replaced. **Not resolved: the developer decides whether the name stays.**)*"
**Reason:** records the stronger mismatch without ruling on it.

### M2 · L24–L26 · §1 table
**Old:**
```
| Primary | China |
| Significant | Japan, UK, South Korea, Russia *(founding/naming heritage)*, Indonesia, Australia *(founding wave)* |
| Notable | Thailand, Vietnam, Philippines, Malaysia, South Africa, New Zealand, Belarus |
```
**Proposed:**
```
| Primary | United Kingdom, Korea, Indonesia, Sinian Federation, Japan, Australia |
| Significant | Philippines, New Zealand, Malaysia, Thailand, Taiwan, Idelsk-Uralia *(founding wave)*, Russia (core state), Vietnam, Belarus, South Africa, Kazakhstan |
| Notable | Manchuria, Siberia, Donska-Kubania, Künnarantaiga, Mongolia, East Turkestan, Northern Ireland, West Papua, Aceh, Dagestan, Patani, Chechnya, Tibet, Kabardino-Balkaria, North Ossetia-Alania, Finland, Ingushetia, Karachay-Cherkessia, Tuva |
```
Add: `*(Corrected 2026-11-03 for DR-85: follows the spec. Old: Primary China; Significant Japan, UK, South Korea, Russia (founding/naming heritage), Indonesia, Australia (founding wave).)*`
**Reason:** copies the spec; Idelsk-Uralia is the Register's founder, Russia is an exile group, not "founding/naming heritage".

### M3 · L28–35 · §1 note
**Old:** "*Mirny is the first city in this project with no American presence at any tier — USA appears nowhere in its composition. China stands alone at Primary, a demographic profile unlike any other city covered so far (most have China and USA paired, or a more even multi-nation spread). Russia — the nation that founded and named the city, after the ship that first sighted Antarctica — sits at Significant tier: present, real, but not dominant. Not erased the way Belgrano's Argentina was, not carried forward by proxy the way Janbogo's Korea was — just one substantial community among several, in a city that ended up demographically Chinese by scale.*"
**Proposed:** "*No American successor region appears in Mirny's composition at any tier. No nation holds a majority: six nations are Primary, the largest being the United Kingdom at 13.73%, and the Sinian Federation is one of them at 12.00%. Idelsk-Uralia, which the Founding Register rules as the establishing country, and Russia (core state), an exile group, are each 2.14% (Significant): present and real, neither dominant. The city is named for the sloop that first sighted Antarctica, a name that predates Tepenia (see Section 2). **Corrected 2026-11-03:** [old: \"China stands alone at Primary … Russia — the nation that founded and named the city … ended up demographically Chinese by scale\"] — superseded by `DR-85` and the Register (`DR-46`, `DR-54`). The earlier comparisons to other cities were removed.*"
**Reason:** removes China-sole-Primary, "Russia founded" and the cross-city comparisons.

### M4a · L41 · §2 paragraph 1
**Old:** "Mirny Station was one of the oldest continuously occupied Antarctic stations in the real world, operating since 1956, and one of Russia's most significant Antarctic footholds. When the Falkland Treaty exiles arrived, Russian robots and their human allies inherited substantial Soviet-and-Russian-era infrastructure — a genuine head start, similar in kind to what Casey's founders inherited from Australia, though considerably older."
**Proposed:** "Mirny Station was one of the oldest continuously occupied Antarctic stations in the real world, operating since 1956; who built it is a coordinate, not a founder. When the Falkland Treaty exiles arrived, Idelsk-Uralia, the establishing country in the Founding Register, with exile groups from Russia, Australia and the Sinian Federation present, inherited substantial Soviet-and-Russian-era infrastructure — a genuine head start. *(Corrected 2026-11-03: [old: \"Russian robots and their human allies inherited … similar in kind to what Casey's founders inherited from Australia\"]; founders per `DR-46`, `DR-54`; the Casey comparison removed.)*"
**Reason:** Register founders; station-builder is not a founder; removes the cross-city comparison.

### M4b · L43 · §2 paragraph 2 — **DECISION POINT 3**
**Old:** "The name was never in question. *Mirny* — the sloop that carried Fabian von Bellingshausen's 1819–1821 expedition … predates Tepenia by centuries. Keeping it was a statement: Russia had been present at Antarctica's very beginning, long before any nation's robots were exiled here, and intended to remain woven into its story permanently."
**Proposed:** "The name was never in question. *Mirny* — the sloop that carried Fabian von Bellingshausen's 1819–1821 expedition … predates Tepenia by centuries. Keeping it was a statement about Antarctica's very beginning, long before any nation's robots were exiled here. **Whose statement it was, and what it meant to them, is OPEN:** the Register names Idelsk-Uralia as the establishing country, with Russia present as an exile group; this file does not rule which community kept the name or why. *(Corrected 2026-11-03: [old: \"Russia had been present at Antarctica's very beginning … and intended to remain woven into its story permanently\"].)*"
**Reason:** removes a motive attributed to Russia that the Register does not support; leaves the open question open.

### M4c · L45 · §2 paragraph 3 (no change needed)
"The founders didn't choose this position for its symbolism … founded by a nation whose flagship first saw the whole continent." — **Proposed:** replace the last clause only: "…, a city built exactly on the line, founded on a site whose namesake ship first saw the whole continent." *(Corrected 2026-11-03: [old: \"founded by a nation whose flagship first saw the whole continent\"].)*
**Reason:** the ship belonged to Russia's expedition, not to the Register's founder.

### M4d · L47 · §2 paragraph 4
**Old:** "As the exile generations passed, the city's demographics shifted the way most Tepenian cities' did — broad Pacific-corridor immigration eventually made China the dominant population by scale, with Russia settling into a strong but no-longer-singular Significant-tier presence, alongside meaningful Japanese, British, Korean, Indonesian, and Australian communities."
**Proposed:** "As the exile generations passed, broad Pacific-corridor immigration produced a city with no majority nation: six Primary nations (the United Kingdom, Korea, Indonesia, the Sinian Federation, Japan and Australia, from 13.73% down to 6.96%), with Idelsk-Uralia and Russia each at 2.14% (Significant). *(Corrected 2026-11-03: [old: \"made China the dominant population by scale, with Russia settling into a strong but no-longer-singular Significant-tier presence\"].)*"
**Reason:** states the current composition; drops the "most Tepenian cities" comparison.

### M5 · L77 · §5a Settlement-era layering — **DECISION POINT 2**
**Old:** "- **a. Settlement-era layering** — The city's founding-era population (predominantly Russian-heritage, inheriting the original station and giving Mirny its name) built the city's earliest institutional character generations before broader immigration arrived. The later, much larger wave of arrivals that brought China to the demographic Primary tier arrived into an already-established city rather than a blank one. The result isn't the sharp erasure Belgrano experienced (the founding-era community remains solidly Significant, not dropped to Notable) and isn't the total cultural absorption Janbogo saw … — it's a genuine, ongoing layering: an old, small founding population and a much larger, later one, each still visibly itself … That pattern of old-and-small beside new-and-large — not any particular pairing of nations — is what the city has made a stable, unresolved peace with, much the way it holds its geographic position at once inside and outside the polar zone."
**Proposed:** "- **a. Settlement-era layering** — The city's founding-era population (the establishing country Idelsk-Uralia and the exile groups from Russia, Australia and the Sinian Federation, inheriting the original station) built the city's earliest institutional character generations before broader immigration arrived. The later, much larger wave of arrivals arrived into an already-established city rather than a blank one. Two of the founding-era groups are now small (Idelsk-Uralia and Russia, each 2.14%, Significant) and two are Primary (the Sinian Federation 12.00%, Australia 6.96%), so the old-and-small beside new-and-large pattern holds for part of the founding generation, not all of it. **Open for the developer:** whether the settlement threshold stays an identity half beside the geographic one (the Antarctic Circle, which is unaffected), or whether the city rests on the geographic threshold alone. *(Corrected 2026-11-03: [old: \"predominantly Russian-heritage … that brought China to the demographic Primary tier … the founding-era community remains solidly Significant\"]; the comparisons to other cities were removed.)*"
**Reason:** founders per Register; China-Primary removed; the cross-city contrasts removed; the identity question left open.

### M6 · L97 · §7 who this city draws
**Old:** "… and people from Russian-heritage backgrounds specifically drawn to the city's historical weight."
**Proposed:** "… and people drawn to the city's historical weight (the old station, the sloop's name), including those with ties to Idelsk-Uralia or Russia." *(Corrected 2026-11-03: [old: \"people from Russian-heritage backgrounds\"].)*
**Reason:** matches the Register's establishing country and exile group.

### M7a · L105 · §8a Primary language(s) — language rule
**Old:** "- **a. Primary language(s):** Mandarin (reflecting the sole-Primary Chinese demographic weight), with substantial, actively maintained Russian, plus meaningful Japanese, English (UK-inflected), Korean, and Indonesian presence."
**Proposed:** "- **a. Primary language(s):** Hawaiian (later Tepenian) is the civic default, as in every Tepenian location. No nation holds a majority (the largest share is the United Kingdom's 13.73%), so **the second-language slot is left open.** Communities of all six Primary nations are present; which languages are actually maintained, and Russian's place among them, is for the ULM pass. *(Corrected 2026-11-03: [old: \"Mandarin (reflecting the sole-Primary Chinese demographic weight), with substantial, actively maintained Russian, plus meaningful Japanese, English (UK-inflected), Korean, and Indonesian presence\"].)*"
**Reason:** the Hawaiian-first rule and the no-majority rule; Chinese is one of six Primaries, not the sole one.

### M7b · L106 · §8b Linguistic character
**Old:** "… Russian and Mandarin are both genuinely fluent community languages rather than one dominating and the other surviving only as heritage."
**Proposed:** "… Which community languages are fluent and which survive as heritage is left open for the ULM pass. *(Corrected 2026-11-03: [old: \"Russian and Mandarin are both genuinely fluent community languages rather than one dominating and the other surviving only as heritage\"] — Russia is now 2.14% and the Sinian Federation 12.00%, one of six Primaries.)*"
**Reason:** the two-language pairing no longer describes the composition.

### M8 · L122 · §10a Human cuisine
**Old:** "- **a. Human cuisine:** A genuine Russian-Chinese layering — hearty, preservation-oriented Russian cold-weather food alongside Chinese culinary tradition, neither fully dominant, closer to coexistence than fusion. *(Corrected 2026-07-13 — previously contrasted … Zhongshan … )*"
**Proposed:** "- **a. Human cuisine:** Hearty, preservation-oriented cold-weather cooking is part of the city's inherited station table (Russia and Idelsk-Uralia, together 4.28%, DERIVED), set among the food traditions of six Primary nations. How these sit together is left open for the ULM pass. *(Corrected 2026-11-03: [old: \"A genuine Russian-Chinese layering … neither fully dominant, closer to coexistence than fusion\"]. The 2026-07-13 parenthetical about another city's cuisine is kept as history; it is a cross-city reference.)*"
**Reason:** the two-cuisine frame rested on Russia and China being the two big groups.

### M9 · L136 · §12 Music
**Old:** "A genuine layered coexistence of Russian and Chinese musical traditions, more separate than merged — residents move between both rather than experiencing a single hybrid form, a musical parallel to the city's overall settlement-era layering. No dominant singular Mirny sound the way Zhongshan or Denison each developed one."
**Proposed:** "Musical traditions of the six Primary nations and of the founding-era groups coexist, more separate than merged, with no dominant singular Mirny sound; the details are left open for the ULM pass. *(Corrected 2026-11-03: [old: \"layered coexistence of Russian and Chinese musical traditions … No dominant singular Mirny sound the way Zhongshan or Denison each developed one\"]; the cross-city reference was removed.)*"
**Reason:** removes the two-tradition frame and the comparison; keeps the "no single sound" claim, which still follows from six Primaries.

### M10 · L151 · Smell
**Old:** "… a specific layered mix of Russian and Chinese cooking smells in residential areas, kept more distinct from each other than in more fused-cuisine cities."
**Proposed:** "… a layered mix of cooking smells in residential areas, kept distinct from one another. *(Corrected 2026-11-03: [old: \"Russian and Chinese cooking smells … than in more fused-cuisine cities\"]; the two-cuisine frame and the comparison were removed.)*"
**Reason:** follows M8.

### M11 · L178 · §16 human-robot relations
**Old:** "Founded on the same shared-exile logic as most Tepenian cities — Russian robots and their human allies settling the site together gave the founding relationship real weight from the outset. … like Casey, Mirny's practical, function-first culture …"
**Proposed:** "Founded on a shared-exile logic — the establishing country's robots and humans, with the exile groups from Russia, Australia and the Sinian Federation, settling the site together — gave the founding relationship real weight from the outset. As the city's demographics broadened, this baseline of solidarity persisted without needing active maintenance; Mirny's practical, function-first culture leaves little room for human-robot relations to become a live political question. *(Corrected 2026-11-03: [old: \"Russian robots and their human allies settling the site together\"]; the \"like most cities\" and \"like Casey\" comparisons were removed.)*"
**Reason:** Register founders; one-location law.

### M12 · L190 · §18 belief line
**Old:** "- Russian Orthodox heritage persists quietly among Russian-descended families, alongside a growing range of Chinese-heritage secular and philosophical traditions — genuinely coexisting rather than merging, matching the city's broader cultural pattern"
**Proposed:** "- Russian Orthodox heritage persists quietly among Russian-descended and Idelsk-Uralian families, alongside the secular, philosophical and religious traditions of the six Primary nations' communities (to be itemized in the ULM pass; none invented here) — coexisting rather than merging. *(Corrected 2026-11-03: [old: \"alongside a growing range of Chinese-heritage secular and philosophical traditions … matching the city's broader cultural pattern\"].)*"
**Reason:** the Chinese-heritage line named one of six Primaries as if it were the other half of a pair.

### M13 · L287 · §26 timeline placeholder
**Old:** "- **[Placeholder — the demographic shift to Chinese-majority population]** — likely gradual rather than a single event, but a culturally significant era in the city's own self-understanding"
**Proposed:** "- **[Placeholder — the demographic shift to a population with no majority nation]** — likely gradual rather than a single event, but a culturally significant era in the city's own self-understanding. *(Corrected 2026-11-03: [old: \"to Chinese-majority population\"]; the Sinian Federation is 12.00%, one of six Primaries, and no nation holds a majority.)*"
**Reason:** a Chinese majority never existed in the current composition.

*Mirny lines that say \"Russian\" or \"Soviet\" about the station's physical inheritance (§9 architecture core, §11 fashion garment structures) describe the site, not the population, and stay. L303's founders note already states the Register and stays.*
