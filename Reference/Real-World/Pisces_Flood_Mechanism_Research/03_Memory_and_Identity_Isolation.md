# Memory and Identity Isolation — Supporting Material

Grounding for what it would technically mean for private, individual memory-space to stop being private —
both at the pure-engineering level (how does a computer normally keep processes' memory separate at all)
and the interpretive level (why would the same failure read as transcendence to one person and trauma to
another). See `00_Extraction_Checklist.md` section C — the highest-priority item here (Linux Memory
Manager, real address-space isolation mechanics) is still unread.

---

## 1. Collective memory — encode / store / retrieve

*Superminds* (Malone), Ch.15 "Smarter Remembering," pp.223-242. Actually read in full.

- Memory (individual or collective) breaks into three functions: **encoding** (getting information into
  a storable form), **storage** (keeping it over time), and **retrieval** (getting it back out when
  needed). A memory system can fail at any one of the three independently.
- The specific finding that distinguishes *collective* memory from a pile of *individual* memories sitting
  near each other: **communication**. A group only has collective memory, in the meaningful sense, once
  its members can actually exchange what they individually hold — otherwise it's just many separate
  private archives that happen to occupy the same room. Collective memory is therefore not a property of
  the individuals or the information itself, but of the *channel* connecting them.
- Applied to Pisces: this reframes "involuntary memory-sharing" usefully. The Flood wouldn't need to
  *create* memories that weren't there, or *erase* anyone's own memory — it would only need to force open
  a communication channel between minds that were never supposed to have one, at which point ordinary
  collective-memory dynamics (as already documented in real cognitive/social-systems literature) take
  over on their own. The horror/wonder is in the channel opening, not in anything being fabricated.

## 2. Process/address-space isolation — read (Ch.3), the single best technical grounding found

*The Linux Memory Manager* (Stoakes), Ch.3 "Virtual Memory," pp.123-140 in-book (PDF pp.138-155). Actually
read. **This is the strongest, most literal (least metaphorical) real-world grounding found in the entire
research pass for "what does it mean, mechanically, for private memory to stop being private."**

### Why isolation exists, and what breaks without it

The chapter opens by listing what goes wrong when hardware places *no* restriction on which memory a
running program can touch — directly relevant, phrased almost exactly in the terms the Flood needs:
- **Stability** — "a program can access memory regardless of whose it is — its own, another program's, or
  the system's," which can cause "unrecoverable memory corruption."
- **Security** — "every process is as privileged as any other and can access data no matter how
  sensitive at will... there is in effect no security between programs at all."

Virtual memory is the real, existing engineering answer: instead of programs touching physical memory
directly, they operate on **virtual addresses** that the kernel maps to physical addresses at page
granularity. "Once this [is] in place, you can have each process believe it has all of the memory
available to itself, which at a stroke eliminates all of the aforementioned issues." Crucially — and this
is the point worth keeping — **isolation is not a passive default state.** It is an *actively maintained
illusion*, requiring a strict privilege split ("the concept of virtual memory really does necessitate a
separation between 'privileged' kernel code and 'unprivileged' user space") because only the
kernel is trusted to change the mappings that keep one process's memory from being another's.

### The actual mechanism: page tables

Isolation is implemented as a **hierarchy of page tables** — for x86-64, up to five levels (PGD → P4D →
PUD → PMD → PTE), each level's entries holding the physical address of the next level down, terminating
in a PTE that finally points to the actual physical data page. A process's own top-level table (its PGD)
is what makes its address space *its own* — two processes with different PGDs are, definitionally,
looking at different (if occasionally overlapping-by-design, e.g. shared libraries) maps from virtual to
physical memory.

Each page table entry (PTE) also carries **flags** controlling exactly what that specific mapping permits:
`_PAGE_PRESENT` (is this mapping actually valid right now), `_PAGE_RW` (writable or not), `_PAGE_USER`
(accessible from unprivileged user-mode code, or kernel-only), `_PAGE_NX` (non-executable — a real
security-critical flag specifically preventing code injected into data regions from being run),
`_PAGE_DIRTY`/`_PAGE_ACCESSED` (has this page been written to / read from). Every single memory access
gets checked against these flags; a violation (writing to a read-only mapping, executing in a marked
non-executable page, touching memory that isn't `_PAGE_PRESENT` at all) triggers a **page fault** — a
hardware exception the kernel traps and responds to (in the ordinary case, by killing the offending
process — "segfault").

### The precise, literal answer for the Flood

Given this, "someone's private memory stopped staying private" has an exact, non-metaphorical engineering
translation: **the page-table mapping that was supposed to keep two processes' physical memory distinct
stopped doing so.** Concretely, any of several real, well-understood failure classes would produce exactly
this outcome:
- Two processes' page tables get corrupted such that their PTEs end up pointing at the *same* physical
  page without either process intending to share it (an ordinary, if serious, class of memory-management
  bug — not exotic).
- The `_PAGE_USER`/permission-flag checks that are supposed to gate access get bypassed or never properly
  set for a given mapping — the physical separation of the memory is intact, but the *enforcement* layer
  that's supposed to keep it private silently stops checking.
- A firmware-level fault (see `04`) corrupts the top-level page-table pointer itself for a given "process,"
  causing its entire virtual address space to transparently resolve into physical memory that used to
  belong exclusively to someone else's session.

None of these require inventing new technology — they're all real, if serious, classes of bugs in
memory-management hardware/firmware that already exists. Applied to Pisces: if the clinics' neural-
interface hardware runs some embedded analog of this page-table system (one "process" or address space per
connected mind), the cascading backend failure from `01` corrupting that specific bookkeeping — rather
than merely dropping a network connection — is what would turn "the backend crashed" into "I can't tell
which memories are mine anymore." The isolation didn't get willfully removed by anyone; the specific,
actively-maintained structure whose entire job was keeping it up simply stopped being maintained correctly
under cascade conditions.

## 3. Process address space, VMAs — read, contains the single most precise mechanism found in this pass

Same book, Ch.4 "Process Memory," §4.1-4.3.3, pp.209-225 in-book (PDF pp.224-240). Actually read.

### `struct mm_struct` and the literal `owner` field

Every process's entire address space is described by one kernel data structure, `struct mm_struct` —
"the core data structure describing a process's entire address space." Among its fields, one is exactly,
almost eerily on-topic: **`owner`** — "Indicates which process... 'owns' this virtual address space." This
is not a passive label — it's an explicit, actively-managed field: it's set by `mm_init_owner()`, can be
**cleared** by `mm_clear_owner()` (used on certain error branches), and can be **reassigned to a different
owner** by `mm_update_next_owner()` (fired specifically when a process exits but its address space needs
to persist for other reasons — e.g., other threads still using it).

**This is the cleanest literal mechanism found in the entire research pass.** "Ownership" of a given
memory/address space is not an intrinsic property of the memory itself — it's a separate, explicit,
*reassignable* field maintained by the kernel, normally updated only in narrow, well-defined
circumstances (a process exiting, an error path). If that reassignment logic fired incorrectly — triggered
by the cascading failure from `01` corrupting whatever handles ordinary session teardown on the clinics'
hardware — memory that legitimately belonged to one person's session could have its `owner` field silently
reassigned to point at a different person's session, while the underlying data (their actual memories)
stays exactly where it was. This gives an exact, non-metaphorical description of "whose memories are
these" that doesn't even require the data itself to move or corrupt — only the *ownership bookkeeping*
around it.

### Reference counting and a real "identity persists past its owner" mechanism

`mm_struct` maintains **two separate reference counts**: `mm_users` (userland references) and `mm_count`
(kernel references, which also counts the object's own existence). When `mm_users` reaches zero, "all
userland-specific metadata is torn down... [but] the object as a whole" persists until `mm_count`
separately reaches zero. This is a real, named two-stage teardown: a process's user-facing identity can
be fully torn down while the underlying structure lingers, kept alive by other references, before final
cleanup. Echoes (and gives a second real citation for) the "zombie process" flavor material in `05` —
a session's identity can, in entirely ordinary kernel bookkeeping, formally end while something of it
persists a while longer, waiting on references that may or may not still be pointing at it.

### Page Table Isolation (PTI) / Meltdown — real precedent for isolation failing *without* corruption

§4.3.3 covers **Page Table Isolation (PTI)**, a real, named kernel mitigation implemented specifically in
response to the **Meltdown** hardware vulnerability. Before PTI, kernel and userland mappings could
coexist in a single page table, distinguished only by permission flags — and Meltdown demonstrated that
permission flags *alone* were not actually sufficient: a real, documented hardware side-channel
(speculative execution) could leak supposedly-isolated kernel memory to userland *without ever violating
the stated page table permissions at all*. The fix required a structural change — literally separating
kernel and userland mappings into two distinct PGD tables rather than trusting flags on a shared one.

**Why this matters for Pisces specifically:** this is real-world precedent that memory isolation can fail
through a channel that has *nothing to do with corruption* — the permission-flag system can be completely
intact and correctly enforced, and data can still leak across the boundary through the underlying
hardware's own side effects. This gives the mechanism an additional, even less dramatic failure mode to
draw on if needed: not "the clinics' isolation was corrupted," but "the clinics' isolation was checked
correctly and still wasn't actually sufficient," which is arguably an even better fit for a district whose
tech runs on unregulated, cost-cut hardware unlikely to have back-ported every mitigation the legitimate
Aquarius-tier equivalent would have shipped with.

## 3. Pattern Theory of memory — read (Ch.1 intro), strong fit for the transcendence/trauma split

*Pattern Theory: Memory, Interpretation, Understanding, Meaning* (Ellaway), TOC + Ch.1 "An Introduction,"
pp.1-3. Actually read. **This is the best-fitting source found so far for constraint A5 (individual
variance must fall out of the mechanism, not be explained away).**

- Core framing: patterns are not objective properties sitting "out there" in events — they are minds'
  own "theories of regularities," a cognitive act of interpretation. The book opens by establishing that
  "a group of observers may witness the same regularities but perceive them differently based on the
  different patterns that are triggered in their minds." This is close to a direct statement of what the
  Flood needs: the same underlying event, read differently by different minds, as an ordinary and
  expected property of how interpretation works — not an inconsistency requiring explanation.
- **Bistable images** — genuinely ambiguous stimuli with two or more legitimate readings (the classic
  example: an image readable as either a little girl with her parents, or a bearded man's face). The key
  finding: "our minds fix on one reading but can (with effort) switch between them... it is nearly
  impossible for us to perceive more than one reading at a time." People don't hold both readings at once
  — they anchor on one. Directly useful: this gives a real cognitive-science precedent for "different
  people (or the same person at different times) land on one of two genuinely incompatible readings of the
  same ambiguous event, hold that reading firmly, and only rarely can even glimpse the other."
- **Pareidolia** — illusory perception, where "external stimuli trigger perceptions of non-existent
  entities, reflecting erroneous matches between internal representations and sensory inputs."
- **Apophenia** — a related, stronger phenomenon: patterns "not only perceived erroneously, they are seen
  as particularly meaningful to the point of delusion." Useful specifically for the *transcendence* side
  of the split — not as a diagnosis to apply to Pisces residents, but as a real, named cognitive category
  for "an anomalous experience gets assigned profound significance, rather than dismissed as noise."
- **"Patternicity" (Shermer, cited)** — the general tendency to find meaningful patterns in both
  meaningful *and* meaningless noise, framed via Type I/Type II error trade-offs: patternicity occurs
  "when the cost of making a Type I error [false positive — seeing a pattern that isn't there] is less
  than the cost of making a Type II error [false negative — missing a real one]." The book notes a
  plausible evolutionary argument that humans are broadly biased toward Type I errors, since failing to
  perceive real danger is more costly than perceiving danger that isn't there — meaning the tendency to
  over-read meaning into ambiguous experience isn't a flaw, it's close to a species-wide default setting.
- **Agnosia/prosopagnosia** (inability to recognize things/faces generally) are cited as evidence that
  pattern-recognition capability itself varies dramatically person to person, "sometimes to the point of
  genius, sometimes to the point of disability, and sometimes both" — direct precedent for real,
  substantial individual variance in how any two minds process the same category of input.

## 3a. Pattern Theory Ch.4, "Patterns and Memories" — read, best single passage found for the mechanism

Same book, Ch.4 "Perception and Pattern," §"Patterns and Memories" and §"Pattern Perception," pp.36-46.
Actually read. This section turned out to matter for *both* remaining open questions — not just the
transcendence/trauma split, but a genuinely new angle on the mechanism itself.

### The normal boundary the Flood violates, stated precisely

"That we cannot directly experience or share our memories with others means that memories are
intrinsically cognitive and personal. Although we cannot access each other's memories directly, that we
can express and share abstractions of our memories means that we can access our own memories in ways that
allow us to create meaningful representations thereof... and that we can build new memories based on
abstractions of memories that have been shared with us." This is a precise, citable statement of the
*normal* boundary: memories are never transferred directly, person to person — only ever shared as lossy,
reconstructed *abstractions* (words, stories, images). **This reframes what the Flood actually violates.**
It isn't simply "too much sharing" — it's specifically bypassing the normal abstraction/narrativization
layer that every ordinary act of human memory-sharing (a conversation, a story, a photograph) already
depends on to keep identity boundaries intact even during real intimacy. The clinics' neural-interface
tech, whatever its intended legitimate purpose, would have had to be doing something that skips this layer
entirely — reading or writing something closer to raw memory-state rather than narrated abstraction.

### Memory reconsolidation — real neuroscience that gives the mechanism its "why now" moment

The chapter cites real, mainstream memory science establishing that memories are not stable, static
archives — every time a memory is recalled, it briefly **destabilizes**, becoming editable
("labile") again before "returning to a stable state through a process known as **reconsolidation**"
(citing Bisaz et al. 2014). This is a genuinely load-bearing real finding: the single most vulnerable
moment in a memory's entire existence is not when it's formed, but *every time it's recalled*. Coherent
memory formation itself depends on "connections between memory fragments (engrams)" being properly
established, with the hippocampus described as memory's "primary weaver."

**Applied to Pisces:** if the clinics' legitimate (pre-catastrophe) neural-interface service was something
like assisted memory recall or memory-sharing-by-consent — plausible, ordinary clinic offerings that would
fit the district's established "dissolution/escape tech" character — then the technology's entire normal
mode of operation already meant interfacing with people's memories at exactly the single moment real
neuroscience says memory is most fragile and editable. The Flood wouldn't need some exotic new capability
to reach into memory; it would only need the *already-fragile, already-editable* reconsolidation window
that ordinary memory recall opens on its own, at the exact moment the interdependent-network cascade
(`01`) corrupted the isolation layer (`03` section 2) that was supposed to keep each person's reconsolidating
memory bounded to their own address space. This satisfies constraint A5 (no new tech tier) about as
cleanly as anything found in this whole research pass — it's not new technology, it's an ordinary
technology interacting with an ordinary, already-documented vulnerability window at the worst possible
moment.

### Pattern development — a third mode, useful for the Syncretic Religion's origin specifically

The chapter distinguishes three modes of pattern-matching: **preconscious recognition** (fast, immediate,
matches something familiar), **conscious recognition** (slower, effortful, still matches something
existing), and — critically — **pattern development**: what a mind does when *no* existing pattern fits
at all, requiring genuinely new interpretive structure to be built from scratch, "much more deliberate and
analytical... and relatively slow and effortful" than either recognition mode. This gives a principled
reason survivors would have constructed an entirely *new* framework (eventually the Syncretic Religion's
own doctrine) rather than assimilating the Flood into any existing category or dismissing it outright —
their minds were doing exactly what "pattern development" describes when confronted with something that
had no precedent to recognize it against.

## 4. Pattern Theory Ch.5, "Shared Pattern Thinking" — read; bridges individual experience to the religion

Same book, Ch.5 "Pattern Thinking," §"Shared Pattern Thinking," pp.82-85. Actually read. This section
isn't about the Flood mechanism itself — it's about the step *after* it: how private, individually-varied
experience (transcendence for some, trauma for others — `03` section 3) becomes a shared doctrine (the
Syncretic Religion), which `10b` already identifies as the natural next link in the chain ("the Flood is
what that doctrine looks like happening to you for the first time... the religion is what it looks like
once the district built one").

- **The book states almost exactly the same paradox `10b`'s doctrine implies:** "patterns are a
  phenomenon of mind and as such they cannot exist in any other medium, and yet I can clearly share my
  pattern thinking and so can we all... if our minds are inaccessible to others and the minds of others
  are inaccessible to us, how is it that we engage in shared pattern thinking?" This is a real academic
  treatment of the *ordinary* version of the exact boundary-dissolution question the Flood makes literal.
- **Shared pattern thinking outlives and exceeds any single mind that contributed to it:** "since shared
  pattern thinking does not depend on any one individual mind, even if all participating minds are lost
  the products of their shared pattern thinking may persist." Useful directly for the religion's origin —
  it doesn't need to reduce to any one survivor's account, and can genuinely outgrow and outlast the
  founding generation's own individually-imperfect memories of the event.
- **Not uniform — a real vocabulary for internal factional variation:** "some minds may influence shared
  pattern thinking more than others... some individuals may accept the shared pattern thinking of their
  community... 'as-is', while others reject it or seek to change it, and dispositions change such that
  heretics and discontents may become more orthodox over time, while others may be more heterodox or even
  heretical." Gives a ready, real-grounded structure for imagining doctrinal variation/schism within
  the Syncretic Religion without inventing the dynamics from scratch.
- **A legitimate darker reading, useful for the "no good endings" discipline:** the same material raises
  "the potential for coercive imposition of social reality (shared pattern thinking) on others," and asks
  directly: "might we understand indoctrination, radicalisation, and the phenomena of cults and sects in
  terms of the manipulation of shared (and thereby imposed) pattern thinking?" This opens a real,
  non-invented angle for the religion to be genuinely ambiguous rather than simply a benign coping
  response — some Flood survivors' individual, private interpretation of what happened to them could have
  been overwritten by whoever got to the framing first and had the most influence, which is a substantive,
  citable version of exactly the kind of moral complication this project's standing discipline requires.
- **Memetic/temporal framing:** shared pattern thinking "changes through use and in response to
  environmental, social, political, and technical challenges... reproduces itself from one mind to
  another" — supports the doctrine having genuinely drifted over the (still undated, previously-moved)
  decades since the Flood rather than being fixed at the moment of the event.

## 4. The Forgetting Machine (flagged, not yet opened)

*The forgetting machine: memory, perception* — not yet opened. Same intended purpose as Pattern Theory
above; also worth checking whether it has anything on the *inverse* problem (what it means for forgetting/
boundary-drawing to fail, as opposed to what it means for memory to work correctly) — the Flood is
arguably a forgetting-machine failure as much as a memory-machine failure, since the core problem is that
people who used to reliably forget "not mine" stopped being able to.

## 5. Cognitive Systems Engineering (flagged, not yet opened)

*Cognitive Systems Engineering: The Future for a Changing...* — not yet opened. Possible source for how
human operators of a failing engineered system interpret/misinterpret that failure in real (not
hypothetical) human-factors research — could ground the transcendence/trauma split at the human-response
level specifically, as a complement to `01`/`04`'s purely structural/technical grounding.

## 6. Deprioritized

*Computational Models of Cognitive Processes* — spotted in the folder, not opened, low priority; only
worth a look if items 3-5 above turn out thin.
