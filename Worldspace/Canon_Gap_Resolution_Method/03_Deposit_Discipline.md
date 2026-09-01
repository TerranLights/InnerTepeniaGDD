# The Deposit Discipline

> **⚠ Read `00_RUNBOOK.md` first. This file is LAW B's operational half**, and it is the part of this system
> that did not exist anywhere in the project before 2026-08-31. Everything else here formalizes practices the
> project already had; **this is the genuinely new piece, and it exists because of one fully-documented
> failure** — the Cape Adare deposit chain (`00` LAW B).

**The rule in one sentence:** *every acquired fact is classified by KIND before it is written anywhere,
deposited into a destination matching that kind, tagged with provenance, and — where a conclusion must live
inside an attribute-tier file — marked with a mechanical boundary a future pass can find by running a command
rather than by reading far enough.*

---

# 1. The three kinds

**Classify before depositing. Always. The classification takes seconds and it is the whole ballgame.**

| Kind | What it is | The test |
|---|---|---|
| **ATTRIBUTE** | A property of the subject. Physical, factual, countable, dated, positional. | **Could two people who disagree about this subject's character still both accept it?** If yes → attribute. |
| **CONCLUSION** | An interpretation of the subject. Character, temperament, pace, aesthetic, capability, meaning. | **Does it say what the subject is *like*, rather than what it *has* or *is*?** If yes → conclusion. |
| **DECISION** | A settled choice with an author, not a discovered fact. A name, an official date, a scope ruling. | **Could it have been otherwise, purely by choice?** If yes → decision. |

**Worked, from the founding case — and fenced, for the reason the fence itself explains.**

<!-- CGRM:CONCLUSION-TIER:START -->
> ⚠ **Conclusion-tier content — Cape Adare specifics, not admissible as input to a cold pass on Cape Adare.**
> Retained because a real recorded case teaches this classification far better than an invented one would, and
> fenced because retaining it unfenced would make this rule file itself a contamination vector for exactly the
> location it is about. **This file demonstrates its own convention by using it.** Registered in the location
> methodology's `06_Worked_Example_Provenance.md`.

| Content | Kind | Why |
|---|---|---|
| Cape Adare sits at ~71°17'S on the Adare Peninsula | **Attribute** | Positional; nobody's reading of the city changes it |
| The rookery holds 250,000+ breeding pairs | **Attribute** | Countable |
| *"Strongly community-driven"* | **CONCLUSION** | An interpretation of what the place is like |
| *"Life moves slowly and deliberately"* | **CONCLUSION** | Same |
| *"Music leans heavily acoustic — guitars, violins, cellos, tagelharpas"* | **CONCLUSION** | A cultural reading, not an inventory |
| *"St. Carsten"* as Borchgrevink's honorific | **Decision**, since promoted to attribute | Someone chose it; once canon, it is simply a fact of the setting |

**All three of the conclusion rows above were deposited into `Specs/Cape_Adare.md` — the project's own
attribute tier — on 2026-07-05, and broke a cold pass on 2026-08-31.** The classification above is exactly the
step that was missing.
<!-- CGRM:CONCLUSION-TIER:END -->

**The generic form of the same test, for anyone who needs it without the case attached:** a *position*, a
*count*, and a *date* are attributes. A *temperament*, a *pace*, and an *aesthetic* are conclusions. A *name*
and an *official date-of-observance* are decisions. **If a single sentence contains one of each, it is three
deposits, not one.**

> ### ⚠ The hard cases, and how to break the tie
>
> - **A conclusion that has hardened into a fact.** Old, load-bearing, cited everywhere. **Still a conclusion**
>   for admissibility purposes — age does not convert kind. *(This is the "canon migration launders provenance"
>   problem the input contract already names: a claim's provenance must travel with it.)*
> - **An attribute that implies a conclusion.** *"250,000+ breeding pairs"* strongly implies things about daily
>   life. **The number is the attribute; the implication is the consumer's job to derive.** Deposit the number,
>   never the implication — the implication is precisely what a synthesis pass exists to produce, and handing
>   it over pre-made is how a cold pass ends up confirming itself.
> - **Genuinely both.** Split it. Two deposits, two kinds, two destinations. **Do not deposit a mixed sentence.**

---

# 2. Destination mapping

| Kind | Deposit into | Marked? |
|---|---|---|
| **ATTRIBUTE** | The subject's own primary factual file — `Specs/[City].md`, an infrastructure reference (`Highways.md`, `Airports.md`), a census/registry file, a character's own `README.md` / `Personal_Background/` factual fields | **No.** This is the default admissible tier. |
| **CONCLUSION** | **Preferred:** the subject's own conclusion-tier home — `Local_Cultures/`, `*_Full_Extrapolation.md`, `City_Vision_Notes/`, a character's personality/arc material. **These are files consumers already treat as conclusion-bearing.** | Not required in a file that is *wholly* conclusion-tier |
| **CONCLUSION that must live in an attribute-tier file** | Only where a reader would genuinely look for it there and nowhere else | **YES — §3, mandatory** |
| **DECISION** | The canon home for that decision class, plus its own ruling record: a name into the subject's own file, an observance date into `Worldspace/National_Holidays.md`, a binding ruling into the relevant reference file | **No**, but provenance-tagged (§4) |

**Default hard, toward the preferred conclusion homes.** The marked-in-place option (§3) exists for genuine
cases, not for convenience — **and every use of it is a small permanent tax on every future consumer of that
file.**

---

# 3. The marker convention

**Purpose: convert admissibility from something a pass must *notice* into something it can *run*.**

**Why this is necessary, stated precisely.** The input contract already requires a cold pass to check whether a
file is wholly admissible, and warns that *"a file is admissible only if every section of it is."* **But that
check is a careful human read, and in the one case where it mattered it failed** — Run 7 cleared
`Specs/Cape_Adare.md` after reading its first ~20 lines, which matched the expected attribute pattern
perfectly, and caught the conclusion section 90 lines further down **only because it happened to read the whole
file for an unrelated reason.** A convention that depends on reading far enough is a convention that fails
whenever a file is long.

**No such convention existed before this one** — verified 2026-08-31: zero HTML-comment markers anywhere in
`Specs/`.

## 3.1 The format

```markdown
<!-- CGRM:CONCLUSION-TIER:START -->
> ⚠ **Conclusion-tier content — not admissible as input to a cold synthesis pass.**
> Acquired via Path 7 (developer creative elicitation), 2026-07-05. See
> `Worldspace/Canon_Gap_Resolution_Method/03_Deposit_Discipline.md`.

## Character & Culture

Cape Adare has the character of a city that knew it was first...

<!-- CGRM:CONCLUSION-TIER:END -->
```

**Two layers, deliberately:**
- **The HTML comments are the machine layer.** Invisible in rendered markdown, trivially greppable, stable.
- **The blockquote is the human layer.** Anyone editing the file sees immediately what tier they are in — which
  matters, because the commonest way a marked block goes wrong is someone appending new content just inside it,
  or just outside it, without realizing which side of the boundary they are on.

## 3.2 How a consumer actually uses it

**To find marked regions before trusting a file** *(one command, no reading required)*:

```bash
grep -n "CGRM:CONCLUSION-TIER" path/to/file.md
```

**To read only the admissible portion of a mixed file:**

```bash
awk '/CGRM:CONCLUSION-TIER:START/{skip=1; next} /CGRM:CONCLUSION-TIER:END/{skip=0; next} !skip' path/to/file.md
```

**This is the fix for the Run 7 failure mode, stated concretely:** a cold pass runs one command, gets the
attribute-only text, and never has to have noticed anything.

> ### ✅ Both commands were tested before being written into this file, with a proof-of-hit control
>
> **Verified 2026-08-31** against a mock file containing a deliberately-planted contaminant string inside a
> marked block, per the project's standing rule that *a scan which has never been shown to find a real hit has
> not been shown to find anything.*
>
> | Test | Expected | Result |
> |---|---|---|
> | Locate markers | 2 lines (START, END) | **2** ✅ |
> | Filter output retains attribute content | yes | **yes** ✅ |
> | Contaminant survives the filter | **0** | **0** ✅ |
> | **Control:** contaminant present in unfiltered file | **1** | **1** ✅ |
>
> **The control row is the one that matters** — without it, a `0` on the third row would be equally consistent
> with "the filter works" and "the grep was broken all along."

## 3.3 Rules for using it

1. **Mark the whole section, heading included.** A marker that starts below the heading leaves the heading
   itself — often the most quotable line — outside the boundary.
2. **Never nest markers.** If two conclusion regions are adjacent, merge or separate them cleanly.
3. **A marked block is not a warning label to be worked around.** If a pass finds itself reasoning about what
   is probably inside a marked block, that is a contamination event and should be recorded as one.
4. **Retrofitting is legitimate and encouraged.** Marking pre-existing conclusion content in attribute-tier
   files is exactly this system's kind of work — **but it is an edit to canon and takes a registry row and a
   log entry like any other deposit.**
5. **⚠ The marker is unambiguous in canon files and ambiguous in files that *teach* the convention.** Found by
   running the convention against this very file: `grep -c "CGRM:CONCLUSION-TIER"` on `03_Deposit_Discipline.md`
   returns **6** — but only four of those are real markers (two pairs), and one of those pairs is itself a
   *format example* rather than a live fence; the remaining two hits are the strings inside the §3.2 command
   blocks. **In canon this never arises**, since a Specs file has no reason to contain example markers.
   **In methodology files, count pairs by reading the line numbers, not by trusting a raw count.**

---

# 4. Provenance tagging — one tag, three jobs

**Every deposit carries a compact provenance tag**, inline where it fits, or on the section where it does not.
**The tag reads `CGRM` for "Canon Gap Resolution Method"** — spell this out in any deposit where a reader
plausibly would not know the system exists, since the tag lands in canon files whose readers have no reason to
have read this one:

```
[CGRM 2026-08-31 · Path 4 · Wikipedia: Dome C]
[CGRM 2026-08-31 · Path 6 · developer ruling]
[CGRM 2026-08-31 · Path 2 · derived: Census II ÷ Census I]
```

**Three jobs from one convention, which is why it is worth the small ugliness:**

1. **Provenance.** A later reader can tell a researched fact from an assumed one — the distinction the project's
   research-log convention already exists to preserve, now surviving at the level of the individual claim.
2. **Re-checkability.** The source is named, so a future session can verify rather than re-derive.
3. **⭐ Audit-findability.** `grep -rn "CGRM" .` returns **every fact this system has ever deposited, anywhere
   in the project.** This matters more than it looks: the project's own large audit sweeps have a known,
   recorded blind spot — **content written after a sweep closes is not covered by it**, which is exactly how
   two cities ended up with invalidated founding material that nothing caught for weeks. **A greppable deposit
   tag means the next audit can find this system's entire output in one command** and check it as a cohort.

**Status convention:** deposits enter as **`Proposed:`** where the project's existing convention calls for it,
**except** Path 6 output — a developer ruling is authoritative on arrival and does not carry a proposed status.

---

# 5. The deposit checklist

Run per deposit. Six items, none skippable.

```
1. KIND classified?            attribute / conclusion / decision      (§1)
2. Mixed sentence split?       yes / n-a                              (§1 hard cases)
3. Destination matches kind?   yes                                    (§2)
4. Marker applied?             yes / not-required                     (§3)
5. Provenance tag written?     yes                                    (§4)
6. Registry row + log entry?   yes                                    (04)
```

**And one question that is not a checkbox, asked last, every time:**

> **Would a cold pass reading this destination file, six weeks from now, be able to tell what it is allowed to
> use — without reading the whole file and without knowing this deposit ever happened?**

**That is the entire discipline.** If the honest answer is no, the deposit is not finished, however true its
content is.
