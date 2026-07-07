# City Megasheet Compilation Guide

**Progress tracking:** see `Megasheet_Progress_Checklist.md` in this same folder — check off each city there as it completes the process.

**What this is:** a record of the actual thinking process used to go from a city's five raw source inputs (`Specs/`, `City_Enneagram_Personalities/`, `City_Vision_Notes/`, `Local_Cultures/`, and `Inspirational-Influences.md`) all the way to that city's final `README.md` — reconstructed step by step, after the fact, using Dome Fuji (the first city to go through this process) as the worked example. Written so the same process can be repeated for any future city without having to rediscover the reasoning each time. Written 2026-07-06.

**Naming convention, corrected 2026-07-06:** `README.md` is reserved for the *final*, fully-detailed end result — the concatenation of all three output stages, in order. It is **not** the first-pass synthesis file. Step 1's own output gets its own name instead, along the lines of `[City]_Mega_Init.md` — an initial synthesis pass, not the finished product. Only after Steps 2 and 3 both exist and everything is concatenated together does the combined result become `README.md`.

**The core insight the whole process rests on:** these five inputs were written at different times, for different purposes, by asking the developer different questions. None of them were written *with each other in mind*. That means simply reading all five and writing a summary undersells what's actually there — the real content lives in what happens when you make them argue with, complete, and contradict each other, which requires three genuinely different cognitive postures in sequence, not one. Those three postures became the three output files, and the combined file is just those three postures stacked in the order they naturally occur in: **synthesize → invent → find what emerges from combining both.**

---

## Step 0: Gather every existing input, and read all of it before writing anything

Before any synthesis work starts, pull all five sources in full:

1. `Specs/[City].md` — the established, load-bearing facts: population figures, geographic data, highway access, founding history, status. This is the file everything else has to remain *consistent* with; nothing invented later is allowed to contradict it.
2. `Local_Cultures/[Subnet]/[City].md` — the 32-section post-culture spec. This is usually the richest single source, already containing a lot of speculative "likely..." framing from earlier passes — the Megasheet's job includes identifying which of that hedged language has since been *confirmed* (often by a City Vision Notes session) and which is still genuinely open.
3. `City_Vision_Notes/[City].md` — the developer's own direct creative input: what they said when asked to picture themselves in the city, plus any follow-up Q&A. This is the highest-authority *creative* source — anything here overrides speculation in the Local_Cultures file, since it's the developer's own voice, not an inference.
4. `City_Enneagram_Personalities/[Subnet]/[City].md` — the personality read (Major Theme, Hornevian Group, Harmonic Group), plus, if the city shares its exact result with other cities, whatever the `Distinguishing_Overlapping_Profiles.md` file says about what actually sets it apart from its Enneagram-siblings.
5. `Inspirational-Influences.md`'s entry for this specific city — the developer's own hand-picked real-world Primary/Secondary city or site picks. If this is still `x`/`x`/`x` (unfilled), the Megasheet process can't fully proceed yet — this is the one input the developer has to supply before research can start, per the project's own established 9-step pipeline (this is step 6, feeding step 7).

**Why read everything before writing anything:** the whole value of the later cross-reference step depends on already holding all five sources in mind at once. Reading them sequentially and writing as you go risks missing a connection between input #1 and input #4 that only becomes visible once both are already loaded.

---

## Step 1: Build the Mega-Init (`[City]_Mega_Init.md`) — the synthesis pass

**Cognitive posture: summarize and reconcile, don't invent yet.**

1. Write a one-line pitch capturing the city's whole identity in a single sentence — this forces an early check on whether you actually understand the throughline across all five inputs, before getting into detail.
2. Pull a "hard facts" table directly from Specs — this is quotable, load-bearing data, presented with zero interpretation.
3. Write a "who lives here, and why" section, reconciling Specs' demographic data with Local_Cultures' and City_Vision_Notes' narrative account of the same population — this is often the first place a real tension surfaces (e.g., Dome Fuji's documented national-origin table vs. the established fact that nationality is functionally irrelevant there), and naming that tension directly, rather than silently picking one framing, is more useful than smoothing it over.
4. Write a "what it feels like" section built specifically from the City Vision Notes session's own language — direct quotes and close paraphrase, since this is the developer's actual voice and shouldn't be diluted into generic description.
5. Summarize the Enneagram read in a few sentences, explicitly naming the closest-matching sibling city if one exists (per `Distinguishing_Overlapping_Profiles.md`) — this plants a thread that the later cross-reference step can pick back up.
6. **Only now, research the real-world Inspirational-Influences picks.** For each Primary/Secondary entry, run an actual web search on that specific real place — its architecture, history, cultural role, whatever's documented — and then ask, for each one individually: *what does this specific real place's own documented character give back to the Tepenian city that isn't already there?* This is the step most likely to be done badly if rushed: the failure mode is treating the research as decorative trivia ("here's a fun fact about Angkor Wat") rather than as material to actively fuse ("Angkor Wat's cosmology, inverted, explains something about Dome Fuji's own established flatness that nothing else in the existing lore explained"). Every research finding that makes it into the Mega-Init should be answering that fusion question, not just reporting what was found.
7. Close with a "what's actually open" section — carry forward the existing Open Questions from Specs/Local_Cultures verbatim, then add anything *new* that the research pass itself surfaced (a new question that didn't exist before this synthesis, distinct from old questions being carried forward).

---

## Step 2: Build the Full Extrapolation — the invention pass

**Cognitive posture: switch from summarizing to inventing, but every invention has to be traceable back to something already established.**

This is a genuinely different mental mode from Step 1, and it's worth treating it as a deliberate gear-change rather than a continuation. Step 1 asks "what do we already know, and how does it fit together?" Step 2 asks "given everything we know, what's the most specific, concrete, *earned* answer to everything we don't?"

1. Go through every "TBD," every open question, every place a source file hedges with "likely" or "possibly," and propose an actual answer — a name, a mechanism, a specific event, a resolved contradiction. The test for whether an invented answer is *earned* rather than arbitrary: can you point to which existing established fact made this specific answer more natural than any other equally plausible one? (Example: Dome Fuji's founding population's fate wasn't resolved with a dramatic invented crisis, because nothing in the existing files suggested one — it was resolved as a slow, undramatic demographic attrition, because that's what "extreme altitude, marginal habitability, centuries of time" actually implies on its own.)
2. Organize the invented content by natural category, not by the order questions happened to appear in the source files — group everything about history together, everything about doctrine/culture together, everything about physical space together, and so on. This makes the result readable as its own document, not just a patched list of answered questions.
3. Name things. A placeholder concept ("whatever central site the pilgrimage tradition venerates") becomes much more usable once it has an actual name, even a working one — naming forces specificity in a way that abstract description doesn't.
4. Propose Notable Figures even where none exist yet, explicitly labeled as placeholder/proposed rather than presented as settled — an empty "TBD" is much harder to react to than an actual, even mediocre, first draft.
5. Frame the entire document, at the top, as proposed extrapolation rather than locked canon. This isn't a formality — it's what allows the invention to be genuinely bold rather than hedged, since the developer retains full authority to keep, discard, or revise anything in it without the document having overclaimed its own status.

---

## Step 3: Build the Cross-Reference Synthesis — the implication-hunting pass

**Cognitive posture: hold multiple documents in mind simultaneously and look for what emerges only from their combination — this is the step that produces content neither Step 1 nor Step 2 could have produced alone.**

This is the highest-value and most distinct step, and the one most likely to be skipped if time is short — worth protecting deliberately rather than treating as optional polish.

1. Re-read all five original sources *plus* the Step 1 and Step 2 documents you've now created, specifically looking for pairs (or more) of facts that live in different documents and were never actually placed next to each other before. Good places to look:
   - A fact stated as a flat baseline in one file (e.g., "no Arcanet connectivity") next to a narrative detail in a different file that depends on that baseline being true (e.g., "devotees arrive from many different cities over time") — these often combine into something neither file states outright.
   - A "TBD" in one file that a *different* file, written for a different purpose, actually already answers or partially answers, without either file cross-referencing the other.
   - Two established facts that are individually true but create tension or a timeline problem when placed side by side — these are worth surfacing explicitly as corrections, not just interesting trivia.
   - A comparison the Enneagram file already set up (e.g., "this city's closest personality match is X") next to a completely different relationship established elsewhere (e.g., "this city's closest institutional/religious counterpart is Y") — when X ≠ Y, that asymmetry itself is usually worth naming as a finding.
2. For every finding, use a consistent structure so the reasoning stays checkable by someone else later: **(a)** name the specific facts and specific source files being combined, **(b)** state the 2nd-order effect that falls directly and necessarily out of combining them, **(c)** push to a 3rd-order effect, and **(d)** push once more to a 4th-order effect wherever the chain still holds up. Flag explicitly, at whichever order it first happens, the exact point where you're extrapolating past what's directly supported, rather than letting speculation quietly read as settled fact further down the chain.
3. Stop chasing a chain the moment it would require assuming something not actually implied by anything established — a shorter, well-supported chain is more valuable than a longer one that quietly smuggles in an unjustified assumption partway through. Not every finding will sustain a full four orders; stop at whichever order is the last one still genuinely earned, rather than padding a weak finding out to four for the sake of consistency.
4. **Design-role mapping for 3rd- and 4th-order effects — codified 2026-07-06, standing rule.** These two orders aren't just "more extrapolation, slightly further out" — they map onto two distinct, concrete design roles, and should be written with that role in mind rather than as generic speculation:
   - **A 3rd-order effect is a questline seed.** It should read as something substantial enough to build an actual quest or major story beat around — a real conflict, a genuine unresolved tension, a character motivation with stakes. When drafting a 3rd-order effect, ask: *could this be the spine of a quest on its own?*
   - **A 4th-order effect is a branch-point** — a direction the player could be led into via a dialogue option or an in-world discovery, growing out of the 3rd-order questline rather than standing alone. It's usually narrower and more specific than the 3rd-order effect it follows: not a new questline, but a fork within one, or a consequence that only surfaces if the player goes looking for it. When drafting a 4th-order effect, ask: *what could a player learn or choose that opens this up further, once they're already inside the 3rd-order situation?*
   - This distinction is *why* 4th-order effects tend to have "the most direct usable payoff" — they're the layer specifically meant to hand off to actual quest and dialogue design, not just theoretical depth for its own sake.
4. Close with a synthesis section that names *patterns recurring across multiple findings*, not just a recap of the findings themselves — this is where the real payoff of doing five or ten findings instead of one becomes visible, since patterns only show up once there's enough material to compare findings against each other too.

---

## Step 4: Concatenate into the final `README.md`

Once all three documents exist — `[City]_Mega_Init.md`, `[City]_Full_Extrapolation.md`, and `[City]_Cross_Reference_Synthesis.md` — combine them in the order they were produced, with a clear divider between each, and the result *becomes* `README.md`. No further editing at this stage; the combined file is a straight concatenation, not a fourth editorial pass. The three source files stay in the folder alongside it, since each is independently useful on its own — `README.md` is the definitive, extremely long, all-in-one version, not a replacement for the pieces it's built from. The ordering itself carries meaning: it's the same synthesize → invent → find-what-emerges sequence the whole process follows, preserved for a reader encountering the city for the first time.

---

## Standing Rule: Write the Highlights Into the Files, Not Just the On-Screen Reply

**Added 2026-07-06, binding for every future Megasheet.** Whatever gets said on-screen at the end of a Megasheet session — "here's what I'd flag as most worth your attention," the two or three standout findings — has to also be written directly into the actual files, not left only in the chat reply. Each of the three source documents (`Mega_Init`, `Full_Extrapolation`, `Cross_Reference_Synthesis`) should end with its own short "Worth Your Attention" callout naming the standout item(s) from that specific document, in the document's own words, before the file closes. The on-screen summary at the end of a session is a spoken-aloud version of what's already on the page, not the only place that judgment call lives — a document read cold, later, with no memory of the conversation that produced it, needs to be able to tell its own reader what mattered most about itself.

---

## What Made This Work, in One Paragraph

The three steps are not interchangeable and not optional filler around each other — they're three genuinely different things a single mind can do with the same material, done in an order where each one needs the last one to already exist. You can't synthesize what you haven't read; you can't responsibly invent answers until you know what's actually already settled (Step 1); and you can't find cross-file implications until there's enough material — including your own invented answers from Step 2 — to actually cross-reference. Skipping straight to invention risks contradicting something already established. Skipping straight to cross-referencing without first synthesizing risks missing the throughline that makes the later findings cohere into something more than a list of trivia. Doing all three, in this order, for every city that goes through the Megasheet process, is what turns five independently-written documents into something that reads like it was designed as one whole from the start — even though it wasn't.
