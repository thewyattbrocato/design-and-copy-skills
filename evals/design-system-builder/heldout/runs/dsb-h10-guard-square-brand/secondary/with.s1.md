Define these three groups, and keep each one small. Boxcar's look comes from restraint, so a long scale would invite drift.

**Shape (radius)**
- Define `--radius-none: 0` and make it the value for every control, card, input, and image.
- Add `--radius-round: 50%` only for the few things that are genuinely circular, like avatars, status dots, and spinners. Naming it makes those exceptions deliberate.
- Don't define a `sm/md/lg` scale. A scale invites someone to pick `radius-md` "just a little."

**Depth (elevation and rules)**
Flat doesn't mean no depth. Express depth with rule weight and hard, unblurred offsets, not blur or gradients.
- Rules: `--rule-thin: 1px`, `--rule-thick: 3px`, `--rule-heavy: 6px`, all in `--ink`. Borders do most of the work.
- Elevation: `--elevation-0: none`, `--elevation-1: 0 0 0 var(--rule-thick) var(--ink)` for outlined raised items, `--elevation-2: 4px 4px 0 var(--ink)` for a hard block offset like a print drop shadow. Never use a blur radius, and don't put gradients on surfaces.
- Surfaces: `--surface-paper` (the off-white base) and `--surface-ink` for inverted blocks. Keep the number of surfaces low, because elevation should come from rules, not from tinting.
- Stacking: `--z-base`, `--z-raised`, `--z-overlay`, `--z-modal`, as a short ordered list.
- Focus: `--focus-ring: var(--rule-thick) solid var(--accent)`, with a visible offset. Tomato on paper meets contrast only at large sizes, so check that before you ship it. Ink is the safe fallback.

**Motion**
Motion should be almost absent, so the tokens should make the default obvious.
- `--motion-instant: 0ms` for nearly everything, including hover, press, and open/close states that just switch.
- `--motion-fast: 100ms` with `--ease-linear` (or `steps()`) as the only duration you allow, for the rare case where a change needs a beat.
- No token for entrance, scroll-linked, or looping animation. If someone needs one, that's a conversation, not a token.
- Use a press state that snaps: on `:active`, remove the offset shadow and translate by the offset amount, at 0ms. That gives tactile feedback in a flat style with no animation.
- Include a `prefers-reduced-motion` block that sets all durations to 0. It costs nothing and is a good habit even though you barely animate.

I can write these as a CSS custom properties file, or as a JSON token set if your print and web tooling read from one source. This folder isn't a git repo and has no existing tokens to match, so tell me where the file should go and whether it should be CSS or JSON.
