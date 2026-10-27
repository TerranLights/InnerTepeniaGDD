# What to look for: the standing list of "other things"

**Written 2026-10-26, agreed with the developer the same day** (three adjustments by the developer are marked ✏️). This is the checklist every inspiration-place research agent uses, in both rounds, for every place, institution or tradition. It sets what counts as an "other thing" worth recording. **Real-world facts only.** Every finding is tagged with the number(s) of the kind(s) below, for example `[K2]` or `[K4, K9]`.

**Breadth rule (developer):** the kinds below are prompts, not boxes. Record what is actually relevant to the particular place at hand, even when it fits none of them (tag it `[K+]` and say what it is). An empty kind is a valid result: write "none found" and where you looked. Never force a place into a kind it does not have.

| Tag | Kind of thing | What to look for |
|---|---|---|
| **K1** | **Shared-problem institutions** | the bodies and rules a place built to manage its one big problem: water boards, co-ops, unions, volunteer fire and rescue, tourist-card or hotel-tax funds, and so on |
| **K2** ✏️ | **Festivals and customs tied to whatever is relevant to this particular place** | these can include, though are not limited to, light, ice, harvest, the closing and opening of access, and so on. Record whatever the place itself makes relevant. Name, date, origin, who runs and attends |
| **K3** | **Festivals created on purpose** | events invented to fill an empty season or draw visitors, and who funds them |
| **K4** | **Living apart, living together** | how groups share or avoid space: workers' housing, parallel festivals, the lodges or halls that take over in winter |
| **K5** | **Daily logistics** | how food, medicine, mail and people actually get in, how often, at what cost, and what happens when access is cut |
| **K6** ✏️ | **Rules of everyday behavior** | *Are there any* curfews, alcohol hours, bans, taboos, unwritten house rules, and so on? *If so, what are they, how do they work, who enforces them, and where did they come from?* "None found" is a valid result |
| **K7** | **Work rhythms** | shifts, rotations, seasonal contracts, and what time is for |
| **K8** | **Money flows and who pays for culture** | taxes, endowments, company towns, subsidies |
| **K9** | **Friction and loss** | rent displacement, closures, strikes, ruins, memorials, conflicts |
| **K10** | **Third places in the off-season** | where people meet when the visitors leave, including the shared buildings that hold a whole town |
| **K11** ✏️ | **Speech: VERY loosely only** | see the language caution below. In the place file, note only (a line or two at most) which languages or broad dialect groups are in use and where groups differ in speech. Slang, colloquialisms and nicknames that you happen to find go to the separate `slang_found/` file, never into the place file. |
| **K12** | **Food and drink culture** | worker cuisine, harvest foods, the drinks that mark gatherings |
| **K13** | **Arts and music: how they started** | the scenes that grew from cheap space, schools or a founder |
| **K14** | **Competence communities** | trades, repair cultures, apprenticeships, craft guilds, search and rescue, test crews |

## ⛔ Language caution (developer, 2026-10-26, amended the same day) ✏️
The project is building an actual Tepenian language and is also studying how the human mind creates slang. If the slang, colloquialisms and nicknames of one place get mixed into the place research, that can corrupt the data for the language patterns of a different place. So:
- **Agents do not hunt for slang**, and they **never write slang, colloquialisms, nicknames or local coinages into the place research files.** Kind K11 in those files is limited to a very loose note: which languages are spoken, whether a broad regional dialect or a minority language is in daily use, and which groups speak what.
- **Amendment:** whatever slang or colloquial expressions an agent **happens to find** while researching the other kinds, it writes to the **separate dedicated file** `slang_found/<unit>_R<n>_slang.md` (format in `slang_found/README.md`), because that material is relevant to the slang-synthesis repo. Each entry stays labeled with its place. The file is created only if something is found.
- Proper names of festivals and institutions are fine in the place files.
- **City passes and the place research do not read `slang_found/`**; the language work uses it, not the other way round.

## Other cautions
- **The deferred mortuary question.** The ULM reserves how the dead are handled and says not to decide it. Real-world burial and mourning facts may be recorded as facts (for example a settlement that forbids burials), but nothing is derived from them.
- **Names of real people** appear only as sources or as the named founder or holder of a documented institution, never as material.
- **The no-South-Asians rule (clarified 2026-10-26).** It means no South Asians in Antarctica, so the stations are non-Indian. It does **not** forbid South Asian places (Jamshedpur, Leh, Ladakh and the like) as inspirations or research topics. Candidates are never excluded for being in South Asia.
- **Sensitive histories** (colonialism, forced labor, displacement, war) are reported neutrally and plainly.

## Optional tags (accepted by the developer 2026-10-26, "everything else looks fine")
These three tags are added on top of the kind tags, for findings where they plainly apply.
- **`[P3] … [P10]`, the ULM phase a finding feeds:** P3 surface and texture · P4 ordinary life · P5 relation and geometry · P6 meaning · P7 order · P8 making · P9 populations · P10 catalog.
- **`[SM:<which>]`, the stories-for-men lens (PROPOSED, a lens and not a template):** competence shown under pressure · man versus society · a dangerous or fascinating figure or system · power rising step by step · humanity and technology questions. Source: the shared audience reference's checklist. Apply it only where a real-world fact plainly fits.
- **`[R]`, a robot-translation flag:** note where a finding bears on shared energy or rest rituals, maintenance and repair cultures, or swap and repair places. **Flag only; do not translate it into robot terms.** (The translation step is the method's own, later.)

## What is not decided
- **Whether the finished units are re-run against this list:** not answered. The Mirny-subnet units and Relung Panen were run under the earlier A–E briefs. Default: do not re-run; consider a short gap-fill pass later (K1, K3, K6, K14 are the likeliest gaps).
