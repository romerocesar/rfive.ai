# SPEC — MCP VSL, full script

Extends the approved five-second opening (`compositions/opening.html`, 0–5s) to the
full script in `../../docs/mcp-vsl-script.md`. The script is the story; its words are
carried on screen because there is no narration track yet.

## Assumptions (change any of these)
- 1920×1080, 30 fps, ~89 s total. Opening scene kept as approved.
- No voiceover: timing is written for a future narration track, line lengths at
  ~0.3 s/word + 0.5 s hold so the recorded voice can land on them.
- Music: light, free, added at the mix step. No SFX beyond the existing reveals.
- CTA is the real one: "Book a consultation" → cal.com/rfive.ai/free-consultation.

## Facts (all from docs/mcp-vsl-script.md + docs/mcp-service-offers.md)
- Adobe: traffic from AI assistants to U.S. retail grew more than tenfold in under
  two years → shown as "10×+ / under 2 years" with the Adobe source label.
- MCP: open standard proposed by Anthropic (Nov 2024), adopted across the AI
  industry (Mar 2025: OpenAI; Apr 2025: Google DeepMind), governed by the
  vendor-neutral Linux Foundation since Dec 2025 (Agentic AI Foundation fund,
  co-founded by Anthropic, Block and OpenAI); 45,000 servers on the official
  registry as of Oct 2026 (per Cesar).
- Offer: production-ready MCP interface over the few workflows customers care about
  (five example workflows, matching "up to 5 core user workflows").
- Work: tool design, auth, safeguards, testing with real agents, deployment, launch;
  managed operation available afterwards.

## Look (unchanged from the approved opening)
White ground; blueprint-blue #003153 panels with fine grid; square corners; IBM Plex
Serif for copy (big, tight), IBM Plex Mono for labels; blue is rationed to one
emphasis per beat. Every illustrative UI carries an ILLUSTRATIVE label; no invented
dashboards, no fake ChatGPT/Claude screens, names as type only.

## Scenes
| # | id | time | beats |
| - | -- | ---- | ----- |
| 1 | opening | 0–5 | approved opening (kept) |
| 2 | question | 5–13 | agent names take action → "can those agents actually use your product?" |
| 3 | tension | 13–22 | people click, agents can't → search/book/order/update/buy |
| 4 | mcp | 22–34 | MCP reveal + connectors → open-standard timeline (Anthropic → industry → Linux Foundation) |
| 5 | proof | 34–47 | the shift → 10×+ number lands → not a proprietary bet |
| 6 | offer | 47–59 | what I help with → five example workflows |
| 7 | how | 59–73 | six-item checklist → "operate it for you" |
| 8 | cta | 73–81 | successful product → book a consultation / learn how it works |
| 9 | closer | 81–89 | "Your customers already know…" → "Now their agents can too." → R5 end card |

## BANNED by default
Dark void with floating UI, glow/particles, fade-up-everything, three cards in a row,
docked logo, fake agent screenshots, logo montage, invented dashboards, stock footage.
