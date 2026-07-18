# Embedded / Firmware Layer — Supporting Material

Grounding for *why unregulated, Aquarius-originated-but-clinic-modified neural-interface hardware
specifically* would be the failure point, rather than any properly engineered device. See
`00_Extraction_Checklist.md` section D — the actually-relevant chapter (firmware threats) is still
unread; what's captured below was reached via a page-offset miscalculation and is being kept because it's
still useful, not because it was the intended target.

---

## 1. Trusted Platform Module (TPM) — read, tangential but useful

*The Embedded Linux Security Handbook* (St. Onge), start of Ch.7. Actually read.

- A TPM is a security-focused microcontroller/chipset that acts as a device's **trust anchor** — a
  hardware-backed root of trust used to securely store credentials, encryption keys, and similar sensitive
  data, and to verify that a device's boot/software state hasn't been tampered with.
- Three implementation types: **firmware TPM** (leverages the CPU's own trusted-execution functions, most
  common and — per the author — most reliable), **discrete TPM** (a physically separate chip, controlled
  outside the main firmware), and **integrated TPM** (bundled into another chipset's broader
  functionality, least common). There's also a software/"virtual" TPM, explicitly flagged by the author as
  weak — no more protected than any other software running on the same system, to be avoided except as a
  last resort.
- Relevance to Pisces: this gives a concrete, real vocabulary for the *legitimate* version of the
  technology Pisces' underground clinics are working from. A properly manufactured Aquarius-tier
  neural-interface device would plausibly ship with something TPM-like — a hardware trust anchor
  establishing which device, and which specific person's session, a given stream of neural data actually
  belongs to. The clinics' unregulated, jury-rigged versions plausibly **strip or bypass this layer
  entirely** (cost, deniability, or simply because it wasn't designed to be user-serviceable at all) —
  which would be the single cleanest "why here and not anywhere else" answer: it's not that the underlying
  tech is different, it's that the one component whose entire job is keeping identities/sessions
  cryptographically distinct is specifically the part missing from the black-market version.

## 2. Disk encryption (LUKS) — read, low relevance

Same source, Ch.6. Actually read. Practical, real-world disk-encryption mechanics (LUKS/dm-crypt,
automated-key handling, recovery-key policy). Kept for completeness but currently no clear narrative
hook — flagging as **low priority to revisit** unless something about the eventual mechanism turns out to
need "how does a device securely store per-user keys," in which case this chapter already has the
answer half-read.

## 3. Firmware threats — read, strong material for "why this hardware specifically"

Same source, Ch.8 "Boot, BIOS, and Firmware Security," book pp.121-127 (PDF pp.144-150). Actually read.

### The boot chain, and what Secure Boot actually guarantees

Every real system boots through a fixed sequence: Power On → BIOS/UEFI → POST (Power-On Self-Test) → MBR
→ bootloader (GRUB2) → kernel + initramfs → systemd → running application. **Secure Boot** is the real
mechanism that turns this into a genuine chain of trust: at each stage, the next component's cryptographic
signature is validated *before* it's allowed to run — BIOS validates the bootloader, the bootloader
validates the kernel, the kernel validates the application. Without Secure Boot enabled, "anything could
be loaded without any checks or balances" — the boot chain still *works*, it just verifies nothing.

Setting up Secure Boot with your own (non-vendor) signing keys is, per the author, a genuine practical
headache even for legitimate developers building real appliances — the standard tooling for it
(`efitools`) was recently abandoned, its replacement (`sbctl`) is still immature, and the author explicitly
frames it as "a temporary quandary... you must make your own judgement call." **This matters directly for
Pisces:** if setting up proper Secure Boot is a real, current pain point even for people with every
incentive and resource to do it right, unregulated black-market clinic hardware — assembled from
mismatched, jury-rigged Aquarius-tier components with no vendor relationship to lean on for signing keys
— skipping it entirely isn't a stretch or a convenient plot contrivance. It's the more *likely* outcome
given the real state of the tooling.

### Possible threats in firmware — the actual "why firmware, why undetected" material

- "Malicious code infecting firmware, such as a BIOS rootkit, seems to be the newest attack vector on a
  global scale. It is also a difficult-to-detect issue for security teams" — and this is described as
  industry-wide, not an edge case: affecting "network hardware, storage systems, servers, industrial
  controllers, edge devices, and laptops," with over 4,500 firmware-specific CVEs in NIST's National
  Vulnerability Database at time of writing.
- **LogoFAIL** — a real, named, high-profile example, worth keeping as a concrete precedent: it exploits
  a completely innocuous, cosmetic UEFI BIOS feature (the custom boot-splash-logo displayed at startup)
  as the actual vector for injecting malicious code, "without the users' knowledge." The vulnerability had
  nothing to do with anything security-critical on its face — it rode in through branding/cosmetic
  functionality nobody thought to scrutinize.
- Crucially: **"Virus scanners cannot help with detection. They look at dissected files, not firmware."**
  Firmware-level compromise sits in a real, structural blind spot of standard security tooling — this
  isn't a case that requires anyone in-world to have been negligent; the tools that would normally catch
  this kind of problem don't operate at this layer at all.
- Some real-world instances trace to "hardcoded credentials for support access being compromised," others
  to the firmware's "own bytecode having massive security gaps." Worst cases install malicious code
  "without the end-user even knowing" — described as "ticking time bombs," since a compromised system can
  sit stable for an arbitrary length of time before whatever was planted actually triggers.

### Applied to Pisces

This gives a concrete, mundane (not dramatic-villain) origin story for exactly the kind of failure the
mechanism needs: some ordinary, cosmetic, or support-access feature in the clinics' improvised device
firmware — plausibly something as unrelated-sounding as a calibration profile, a personalization setting,
or a remote-diagnostics backdoor left in for the clinics' own maintenance convenience — is the actual seam
through which the cascading backend failure (`01`) was able to reach all the way down into the
memory-isolation layer (`03`) rather than staying contained as an ordinary network outage. And because
firmware-level compromise is a documented blind spot for conventional detection tooling, nobody — not the
clinics, not their patients — would have had any real way to see it coming, which satisfies constraint A7
(genuine ambiguity survives) at the in-world epistemic level as well as the mechanistic one.

## 4. Interprocess communication (flagged, not yet read)

*System Programming in Linux* (Weiss), Ch.12 "Introduction to Interprocess Communication," pp.597-644 in
the book's own pagination — targeted twice, landed on Ch.11 both times due to page-offset miscalculation
(see `05` for what was actually captured there). Still needed: the real mechanics of **shared memory**
IPC specifically — two separate processes deliberately mapping the same physical memory region so they
can read/write it directly, which is the closest real OS-level concept to "two people's devices
deliberately sharing a memory-space on purpose" before anything goes wrong with that arrangement. Worth
reading directly rather than assuming general familiarity, since the *specific* Linux API/semantics
(System V shared memory vs. POSIX shared memory vs. `memfd`, per the Memory Manager book's own Ch.14 TOC
listing) might turn out to matter for precision.
