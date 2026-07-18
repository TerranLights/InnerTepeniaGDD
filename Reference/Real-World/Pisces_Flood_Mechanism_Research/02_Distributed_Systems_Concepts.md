# Distributed Systems Concepts — Supporting Material

Grounding for *why* and *how* multiple separate devices/minds would even be in a position to converge on
(or be confused about) a shared state. Secondary to `01`'s cascading-failure mechanism — this material
explains the plumbing, not the collapse itself. Mostly still TOC-level; see `00_Extraction_Checklist.md`
section B for what's still unread.

---

## 1. Logical/vector clocks (flagged, not yet deep-read)

*Distributed Systems: An Algorithmic Approach* (Ghosh), Ch.6, "Time in a Distributed System" — **not yet
actually read**, only confirmed to exist via TOC. Concept as generally understood, to verify on read:
independent machines with no shared physical clock can still establish a consistent *causal* ordering of
events (which event happened before which) using logical clocks (Lamport) or vector clocks (which track
causality more precisely, including concurrent/unordered events). Potential relevance: if Pisces' device
network needed to establish "whose memory happened first" across independently-clocked hardware with no
shared authoritative time source, a logical-clock-style mechanism is exactly the kind of thing that would
be doing that job — and exactly the kind of thing that could produce a *wrong but internally consistent*
ordering if it broke.

## 2. Mutual exclusion (flagged, not yet deep-read)

Same source, Ch.7. Concept to verify on read: the formal distributed-systems guarantee that only one
process/node gets exclusive write-access to a shared resource at a time, and the various protocols
(token-passing, quorum-based, etc.) used to guarantee it across independent machines with no shared
memory. This is the *precise formal property* that "two clinic devices reading/writing the same
memory-space at once" would represent the violation of — worth reading directly rather than relying on
general familiarity, since Pisces' unregulated hardware plausibly never implemented this correctly (or at
all) in the first place.

## 3. Distributed snapshots / Chandy-Lamport (flagged, not yet deep-read)

Same source, Ch.8, "Distributed Snapshot." Concept to verify on read: the Chandy-Lamport algorithm is a
real, classical technique for capturing a *consistent* global state across a set of independent,
concurrently-running nodes with no global clock and no shared memory — it guarantees the resulting
snapshot reflects a state the system could actually have been in, even though no single moment of "the
system's true state" exists in a distributed system. Strong candidate for explaining a device network that
*tried* to take a consistent snapshot of "who currently owns which memories" and got an inconsistent one
instead — the algorithm exists specifically because getting this right is hard and non-obvious, which
means getting it wrong is a completely mundane engineering failure, not a mystery.

## 4. Rendezvous algorithms — read (§4.2-4.3), a genuinely valuable addition

*Distributed Control of Robotic Networks* (Bullo/Cortés/Martínez), §4.2 "Connectivity maintenance" and
§4.3 "Rendezvous algorithms," book pp.179-196 (no front-matter offset needed — this book's PDF pagination
matches its own printed page numbers exactly). Actually read.

### Connectivity maintenance — the enforcement layer underneath rendezvous

Before any convergence can happen, the network needs a guarantee that agents don't drift so far apart they
lose their ability to coordinate at all. §4.2 formalizes this as a **connectivity constraint set** — each
agent restricts its own next move to a region guaranteed to preserve whatever links currently exist in the
communication graph. This is a real, provable enforcement mechanism (Lemma 4.5, Lemma 4.8): given the
constraint is respected, the network's connectivity can only stay the same or improve, never spontaneously
fragment on its own from ordinary motion. Useful as a baseline: real distributed systems don't just hope
connectivity holds, they mathematically guarantee it — which sets up exactly how visible/detectable a
*violation* of that guarantee would be if something bypassed it.

### Rendezvous — real, simple, named algorithms for independent agents converging on shared state

§4.3 presents actual algorithms, not just the abstract concept:

- **The AVERAGING law**: each agent repeatedly computes the average position of itself and its currently-
  connected neighbors, then moves toward that average. Explicitly tied in the text to a real, established
  field: **"opinion dynamics under bounded confidence,"** known in the literature as the **Krause model**.
  This is a genuinely striking cross-reference — the *exact same* mathematical structure used here for
  robots converging on a shared spatial position is, in real social science, used to model how people's
  *opinions and beliefs* converge (or fail to converge) through repeated local interaction. It ties this
  session's structural material (rendezvous) and the earlier psychological material (`03`'s Pattern
  Theory work) together under one shared, real mathematical framework, rather than two unrelated
  metaphors bolted together.
- **The CIRCUMCENTER (CRCMCNTR) law**: each agent moves toward the circumcenter (center of the smallest
  enclosing circle) of itself and its neighbors, while respecting the connectivity constraint from §4.2.
  Provably maintains connectivity *throughout* the process, not just at convergence.
- Both laws come with real, cited convergence proofs (Theorem 4.15, Theorem 4.16/4.17) and are shown
  working under realistic constraints found throughout the rest of the chapter: bounded control authority,
  sparser/relaxed connectivity graphs, line-of-sight-limited sensing, nonconvex environments with
  obstacles. Rendezvous is a genuinely robust, well-studied *family* of algorithms adaptable to the same
  kind of real-world limitations (limited sensing range, obstacles, bounded actuation) a real device
  network would also have to contend with — not a fragile toy case that only works in ideal conditions.

### The genuinely valuable finding: convergence doesn't have to be universal

The book's own example run of the AVERAGING law (Figure 4.5, 51 agents on a line) notes explicitly:
**"some robots are connected at the simulation's beginning and not connected at the simulation's end"** —
meaning rendezvous doesn't necessarily pull the *entire* network into one single shared point. Depending
on the network's topology and how connectivity evolves during the process, agents can converge into
**multiple separate clusters that never merge with each other**.

**This is a real, mathematically-grounded reason the Flood need not have produced one single universal
merged consciousness.** Applied to Pisces: different sub-groups of connected devices/minds could have
rendezvoused into their *own* separate shared states — clusters of a few people whose minds fused with
each other but not with the district as a whole — rather than everyone in Pisces ending up in the same
undifferentiated collective mind. This adds real texture (and a real citation) to imagining the Flood's
aftermath as clustered/factional rather than monolithic, which also gives natural shape to how different
survivor groups might have developed *different* variants of the eventual Syncretic Religion doctrine
(see `03` section 4's "Shared Pattern Thinking" material on doctrinal schism) — different rendezvous
clusters, different resulting shared realities.

## 5. False Data Injection Attacks, repurposed as accidental failure

*Attack-and-Defense Games for Control Systems* (Analysis and...), Ch.1 read (intro/structure only), Ch.4
(FDIA detection specifically) still unread. FDIA is normally framed as a deliberate attack — corrupted
sensor/device data injected to fool a control system into acting on false information. **Constraint A4 in
`10b` rules out any external attacker or deliberate act.** The reframe that survives that constraint:
the *detection and consequence* side of FDIA research — what a control system does when it can no longer
tell legitimate synchronized data from corrupted data — is mechanism-agnostic. The same failure mode
(a system treats corrupted output as legitimate and acts on it) can arise completely by accident from a
hardware fault or a bad firmware update, with zero attacker required. Worth reading Ch.4 specifically for
the technical vocabulary of *how* a system is supposed to tell the difference, so the eventual mechanism
can describe precisely what that detection layer failed to catch.
