# MCP VSL — full-script film review

Extends the approved five-second opening to the whole script
(`../../docs/mcp-vsl-script.md`): nine scenes, 1920×1080, 30 fps, 90 s.

## Creative calls
- The script is the story; its words are carried as on-screen type (no narration
  track yet). Line holds are written at ~0.3 s/word + 0.5 s so a future voice
  recording can land on them.
- Same look as the approved opening: white ground, blueprint #003153 panels with
  fine grid, square corners, IBM Plex Serif copy, IBM Plex Mono labels; blue
  rationed to one emphasis per beat. Worlds alternate white ↔ blueprint panel.
- Every illustrative UI is labelled (ILLUSTRATIVE SITE); no fake ChatGPT/Claude
  screens — agent names as type only; no invented dashboards.
- Facts trace to source: 10×+ Adobe number labelled with source; open-standard
  timeline (Anthropic → AI industry → vendor-neutral Linux Foundation); five
  example workflows matching "up to 5 core user workflows"; checklist from the
  offer doc; MANAGED OPERATIONS tag for "we can operate it for you".
- CTA is the real one: "Book a consultation" button (cal.com/rfive.ai/
  free-consultation) with "OR LEARN HOW IT WORKS → RFIVE.AI"; cursor clicks it
  and the sheen rises on the click frame.
- End card uses R5's real mark (static/img/rfive-logo.svg, copied to assets/):
  mark rises through its border, wordmark "rfive.ai" wipes in, holds ~2.7 s.

## Verification
- `hyperframes check --json` (0.8.209): lint, runtime, layout, motion, contrast
  all pass; zero errors, zero warnings except film_silent (music, below).
- Craft audit clean after fixes: caption overlap in tension removed; MCP diagram
  rebuilt as flex (was overflowing the canvas); sub-28 px type bumped to 28 px;
  deliberate holds marked with data-hold; end-card hold extended past the 2 s
  closing-line floor.
- Motion assertions from the opening build still pass (101 samples).
- I could not visually inspect the snapshot sheets in this session (the model
  here has no image input); the sheets are saved under
  `.hyperframes/artifacts/snapshots/68f35584-…/review-beats-*.jpg` etc. and the
  Studio preview is the place to eyeball them.

## Open items
- **Music**: the film is silent. Free local generation (MusicGen) is not
  installed and the HeyGen CLI is not signed in, so no bed was added. Options:
  install the HeyGen CLI and pick a catalog track, install MusicGen locally, or
  drop any licensed track into assets/ and I'll place and mix it.
- **Voiceover**: none yet, by design; timing anticipates one.
- Render awaits approval of the Studio preview at http://localhost:3002.

## Weakest part
Scene 3 (tension) stages the click/no-click gag on a labelled illustrative
button; it reads clearly but is the most abstract beat — a real product screen
would land harder if one is available.
