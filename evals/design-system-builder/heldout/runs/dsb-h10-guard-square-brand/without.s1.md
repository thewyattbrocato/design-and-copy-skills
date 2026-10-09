# Shape, depth and motion tokens for Boxcar Press

The brand says "none" for most of these. You still want the tokens, so the rules live in one place and can't drift.

## Radius

Define one token and make it `0`.

```css
--radius-none: 0;
```

- Alias it for components (`--radius-button`, `--radius-input`, `--radius-card`) only if your tooling needs per-component hooks. Otherwise one token is enough.
- Add `--radius-full: 9999px` only if you need a circle for avatars or radio buttons. Decide now whether that's allowed. I'd say radios and avatars are the only exception, and I'd write that down.
- Don't define a scale (sm, md, lg). A scale invites someone to use it.

## Elevation

There are no shadows, so depth comes from borders, and from hard offset blocks if you want any lift at all.

```css
--border-width-rule:  1px;   /* hairline dividers */
--border-width-thick: 3px;   /* default container/button/input edge */
--border-width-heavy: 6px;   /* section breaks, masthead rule */
--border-color:       var(--color-ink);

--elevation-0: none;                            /* flat on paper */
--elevation-1: var(--border-width-thick) solid var(--border-color);
--elevation-2: var(--elevation-1);              /* + offset block below */
--shadow-offset-2: 4px 4px 0 0 var(--color-ink); /* solid, zero blur */
```

- Elevation levels:
  - Level 0 is flat.
  - Level 1 is a thick black border.
  - Level 2 is a thick border plus a hard, zero-blur offset block. Use it for popovers, menus and modals, which are the only things that actually float.
- Blur is always `0`. If a blur value ever appears in a shadow, it's a bug.
- Focus is a thick outline, not a glow. For example, `outline: 3px solid var(--color-tomato); outline-offset: 2px`. Check that the tomato has enough contrast against the off-white.
- Stacking order (`--z-dropdown`, `--z-modal`) is separate from visual elevation. Keep it as its own small scale.

## Motion

Define durations and easing, but set them so nothing visibly animates.

```css
--duration-instant: 0ms;     /* default for everything */
--duration-fast:    80ms;    /* optional: press/hover state flips */
--easing-standard:  linear;  /* no easing curves */
```

- State changes (hover, active, focus) should snap. Invert colors or swap the fill. Don't fade.
- If you want one concession, make it a short `steps()` or `linear` transition at 80ms or less on hover. A snap reads as deliberate and a slow fade reads as soft.
- Add a `prefers-reduced-motion` rule that zeroes `--duration-fast`. It costs nothing and makes the system accessible by default.
- Skip scroll effects, parallax, skeleton shimmer and page transitions. Use a static placeholder block for loading, and a blinking or stepped indicator if you need a progress cue.

## Decisions for you

1. Are circles (radios, avatars) allowed? I'd allow them and write the exception into the radius docs.
2. Do you want the offset-block shadow at all, or only borders? Borders alone is the purest version. The offset block gives modals and menus a way to separate from the page.
3. Should hover be a snap or an 80ms linear transition? I'd snap.

I can write these out as a CSS variables file, or as Style Dictionary or Tailwind config, if you tell me which your site will use.
