# Steam Launch Strategy and AI Disclosure

**What this is:** a working reference for release-strategy questions, not a GDD design document — same
category as `Early_Access_vs_Launch_Content_Split.md`. Compiled 2026-07-24 from a Grok conversation the
developer had and dropped into `to-be-integrated/using_AI_and_advertising.txt`. **Source caveat, same as
every other Grok-derived file in this project:** treat the specific statistics cited below as directional
signal, not verified fact — I have no way to independently confirm the exact figures/sources Grok cited, and
this file should not be read as more authoritative than that. The practical strategic advice holds up
independent of the precise numbers; the numbers themselves should be re-checked against primary sources
before being used to justify a specific business decision.

---

## 1. Indie Sales Benchmarks ($10-20 Price Range)

Context for what's actually achievable at a typical indie price point — cited examples (unverified specific
figures, but useful as a sense of scale): *Mina the Hollower* (~300k copies in 3 days at $20), *Celeste*
(~500k in year one at ~$20), *Lethal Company* (~640k shortly after launch at $10), *Balatro* (1M+ in month
one at ~$15), *Slay the Spire* (~1.5M by 2019), *Megabonk* (1M+ quickly at $10). Common thread across all of
them: strong reviews/word-of-mouth, high discoverability, streamer amplification, and low price-sensitivity
impulse-buy positioning. Success is rare and top-heavy — most indies sell far fewer — but the $10-20 band is
a real, achievable price point for a breakout, not just a floor.

---

## 2. Steam Discoverability — Reasonably Reliable Tactics

**In rough order of leverage:**

1. **Optimize the Steam page first** — capsule art (see Section 3), gameplay-first screenshots/trailer (not
   menus), a genre-clear short description, and using all 20 tag slots with specific sub-genre tags first
   (drives "More Like This" and Discovery Queue matching). Launch a "Coming Soon" page 6-12 months early to
   compound wishlists over time.
2. **Wishlists are the core pre-launch algorithm signal** — velocity matters more than raw total. Cited
   rough targets: 7k-10k+ at launch for decent algorithmic help, 25k-50k for much stronger. Driven by
   consistent devlogs, social content with clear wishlist CTAs, and external traffic.
3. **A polished demo, especially timed to Steam Next Fest** (Feb/Jun/Oct) — release the demo *before* the
   Fest, not during, so it's bug-free with existing reviews/feedback going in. High demo-to-wishlist
   conversion and playtime signal engagement to Steam's own algorithm.
4. **External traffic via content creators and community** — targeted mid-tier creators in the exact genre
   niche convert better than big generic ones; build Discord/socials early for organic shares; short-form
   video (TikTok/YouTube Shorts) rewards "one weird mechanic" or chaotic/funny clips.
5. **Keep the page active** (regular devlogs prevent algorithmic "stale page" deprioritization), align pushes
   with Steam events, consider basic localization for key markets (Simplified Chinese cited specifically),
   and Steam Deck verification/controller support as positive signals.

**Suggested order of operations:** page assets → early page + demo → external traffic/wishlist velocity →
launch with momentum → post-launch visibility from sales.

---

## 3. The Capsule — Steam's Most Important Single Asset

The capsule is the game's promotional "box art" across the whole platform — search, Discovery Queue,
recommendations, wishlists, sale pages. Steam scales it down aggressively (as small as ~120×45px in some
contexts), so **design for the smallest size first.**

**Required dimensions:** Header 920×430 (store page top), Small 462×174 (search/wishlists/queues), Main
1232×706 (featured carousels), Vertical 748×896 (sale pages/grids).

**Six dimensions to optimize for:**
1. **Genre clarity** — nameable in under a second at thumbnail size.
2. **Title readability** — bold, high-contrast font, tested at tiny sizes.
3. **High contrast/color** — must pop against Steam's dark UI (#1b2838); check in grayscale.
4. **Single focal point** — one subject; clutter and fine detail vanish when scaled down.
5. **Uniqueness and polish** — stand out from genre neighbors; match the actual in-game art style.
6. **Brand consistency** — cohere with screenshots/trailer.

**Avoid:** fine detail/thin lines, review scores/awards/dates baked into the image (discouraged/banned on
base capsules), low-contrast or busy compositions, generic stock-feeling scenes.

---

## 4. AI Disclosure — The Part That Actually Matters for This Project

**Why this section exists, stated plainly:** a large portion of Inner Tepenia's actual narrative and
questline design work has run through AI assistance (this GDD's own development process, plus prior Grok
sessions per the source conversation). Steam's disclosure requirement is not hypothetical for this project —
it's a real, specific obligation to plan for when the Steam page actually goes up.

### What Steam Requires

Disclosure is mandatory (via the Content Survey in Steamworks) for **generative AI content that ships with
the game and that players consume** — this explicitly includes narrative structure, questline drafting,
dialogue generation, and lore development, not just visual/art/audio assets. Non-generative "efficiency"
tools (code assistants, etc.) do not require disclosure per Valve's own 2026 clarification cited in the
source conversation.

### The Actual Sentiment Data (treat specific numbers per the source caveat above)

A cited 2025 analysis of ~10,000 Steam games found AI-disclosed titles received roughly 53% fewer reviews
than comparable non-AI games, with a slightly lower positive-review rate (84.6% vs. 88.3%) — a real but not
universal penalty, reportedly stronger for higher-profile/bigger projects. A cited 2026 GameDiscoverCo
player poll (~3,800 respondents) found roughly 43% okay/accepting of AI use, 26% neutral, 31% negative — but
only about 8% saying they'd categorically never play a game using AI at all. **Read together: real
backlash risk exists and is louder online than it is in the actual player base, but it is not a hard
dealbreaker for the large majority of players.**

### Recommended Disclosure Approach

**Be specific, not vague.** A recommended wording template for narrative/structural AI use, adapted from the
source conversation:

> "This game uses generative AI tools to assist with narrative structure, questline drafting, dialogue
> generation, and lore development. All AI-generated text was reviewed, heavily edited, rewritten, and
> directed by the developer to ensure it fits the intended vision, tone, and quality standards. No raw AI
> output appears in the final game without human curation."

**Channels to disclose through, in order of importance:**
1. **Steam's own Content Survey / AI Generated Content Disclosure section** — the mandatory, official
   channel; update it if usage changes over the project's lifetime.
2. **A clear "Development" section or paragraph on the store page itself** — plain, neutral language framing
   AI as a productivity tool the developer directed, not a replacement for creative decision-making.
3. **Devlogs and community channels, ongoing** — sharing process transparently (e.g., "generated N quest
   outline variations, picked and rewrote the best few from scratch") before launch builds trust that pays
   off at launch, rather than reading as a defensive reaction to criticism after the fact.
4. **A calm, consistent response posture for negative reviews/comments** — engage constructively with good-
   faith concerns, don't engage with bad-faith trolling.

**Framing that reduces backlash risk, per the source conversation:** emphasize human oversight and final
creative authority ("a tool in my hands, like any other software — I made the creative decisions"), frame
the benefit honestly (a solo/small-team developer's ability to explore more variations and ship more
content), and — the single strongest lever available — **lead with quality.** The stigma lands hardest on
titles that read as low-effort; a well-crafted, well-directed final product blunts most of the criticism
regardless of the tools used to help build it.

**Realistic expectation:** even with full, honest, proactive disclosure, some review-bombing from the
committed anti-AI minority is likely unavoidable. The strategic goal isn't eliminating that risk entirely —
it's making sure the much larger neutral-to-accepting majority sees an honest, well-made game rather than
something that reads as hidden or defensive about its own process.

---

## Open Questions / Not Yet Decided

- Exact final wording for Inner Tepenia's own Steam disclosure — draft above is a template, not finalized
  copy.
- Whether to lead with AI-assisted development as a devlog talking point pre-launch, or disclose primarily
  through the required Steamworks channel without making it a marketing centerpiece either way.
- Capsule art concept/design — not started; this file's Section 3 is the guideline to design against
  whenever that work begins.
- Wishlist-building strategy and timeline — not started; depends on how far out from an actual playable
  build/demo the developer wants to begin a public-facing presence.
