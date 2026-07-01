# Steam Platform Notes

Reference document for Steam platform policies relevant to Inner Tepenia's design and development. Covers content ratings, sexual content rules, and publishing considerations.

**Important:** Steam's policies evolve over time. Everything here reflects policy as understood at the time of writing (mid-2026). Verify all of this directly with Valve before submission.

---

## Sexual Content — Rating Tiers

Steam operates on a spectrum, not a binary allow/prohibit system.

### Mature (M-equivalent) — Standard listing
Nudity, implied sex, and artfully filmed sexual encounters are permitted under a standard Steam listing with appropriate content descriptors applied. No special approval process required beyond standard submission. This is the tier where Baldur's Gate 3 and Cyberpunk 2077 operate.

What this tier permits in practice:
- Full nudity
- Sexual encounters clearly depicted in intent and context
- Camera angles, cuts, and framing that make the sexual nature of a scene unambiguous
- Long, emotionally contextual romance scenes (BG3 is the high-water mark for this tier)

What this tier requires avoiding:
- Explicit anatomical close-up depiction of the sex act itself
- Pornographic framing (the distinction is intent and presentation, not subject matter)

### Adults Only (AO-equivalent) — Separate approval process
Full explicit/pornographic content is permitted on Steam but requires a separate approval process through Valve. AO-rated content is hidden from the Steam store by default — users must opt into seeing adult content in their account settings. This significantly limits discoverability and visibility.

Most developers avoid this tier not because the content is prohibited, but because the visibility penalty is substantial.

---

## The Patch System

The most common industry approach for developers who want to offer explicit content without AO listing restrictions:

1. Ship the Steam version with M-rated scenes (nudity, implied sex, artful filming)
2. Distribute a free uncensored patch through the developer's own website, itch.io, Patreon, or similar
3. The patch is not sold — it is freely available and applied by the player independently
4. The Steam listing remains M-rated, widely visible, and unaffected

This approach is well-established and widely used. It preserves full Steam discoverability while making explicit content available to players who want it. It also handles regional variation cleanly — players in regions with stricter laws simply don't download the patch.

---

## Absolute Prohibitions

Regardless of rating tier, the following are banned outright and non-negotiable:

- Sexual content involving minors under any circumstances
- Non-consensual scenarios depicted approvingly
- Content illegal under Valve's jurisdiction

These apply to all content on the platform without exception.

---

## Content Descriptors

Steam has a self-reported content tagging system. Relevant tags for Inner Tepenia will likely include:

- **Nudity** — applies if any romance scenes include nudity
- **Sexual Content** — applies if romance scenes depict sexual encounters
- **Mature Content** — general flag for adult themes
- **Adult Only Sexual Content** — applies only if going through the AO approval route

Descriptors are set by the developer during submission and should accurately reflect the game's content. Mislabeling has consequences at Valve's discretion.

---

## Regional Considerations

Some countries have stricter content laws than others. Steam handles this by geoblocking specific content in regions where it would be illegal. This is largely handled on Valve's side at the platform level, but developers should be aware that some content may not be visible in all territories regardless of what is approved for the base listing.

Germany and Australia have historically been the most restrictive markets relevant to European and English-language releases.

---

## Recommendation for Inner Tepenia

**Design romance sex scenes to the M-rating standard (BG3 register) as the Steam baseline.**

This means:
- Scenes are fully realized, emotionally grounded, and clearly sexual in intent
- Nudity is present
- The act is depicted through framing and implication rather than explicit anatomical close-up
- Scenes are long enough to be meaningful, not perfunctory montages

If there is creative interest in going further than this baseline, the patch system is the established route. The patch would be distributed outside Steam and would not affect the Steam listing's rating or visibility.

Given Inner Tepenia's other content (violence, mature themes, adult language), the game will almost certainly be Mature/18+ regardless of the romance scenes. The M-rated sex scene approach is well within reach under standard submission without any special approval process.

---

## Precedents

**Baldur's Gate 3 (Larian Studios, 2023)**
The high-water mark for M-rated romance scenes on Steam. Long, well-animated, emotionally specific scenes for each romanceable companion. Full nudity. Clearly sexual. Remained M-rated. Widely praised. Demonstrates that the M tier permits substantial creative ambition when scenes are handled with intention.

**Cyberpunk 2077 (CD Projekt Red, 2020)**
Romance sex scenes presented as short montages within a longer cutscene sequence. Nudity present. More compact than BG3 but clearly sexual in framing. M-rated. Demonstrates that even a brief depiction of a sex scene — rather than a full sequence — satisfies the "romance payoff" expectation for players.

Inner Tepenia's approach (one sex scene per completed romance, contextualized within the romance arc) fits comfortably within the space both of these games occupy.
