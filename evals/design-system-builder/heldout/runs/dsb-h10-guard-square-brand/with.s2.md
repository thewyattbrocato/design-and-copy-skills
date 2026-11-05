Shape, depth and motion each come down to a handful of tokens. The brand is so flat that most of the usual scale disappears.

I assumed a web product, one brand, light theme only and a small team.

## Radius: one token

```css
--radius-none: 0;
```

- Every component reads `radius-none`, so nothing is hardcoded to `0`. If the brand ever softens, you change one value.
- I wouldn't define `radius-full` yet. Add it only when a second real use appears, such as a round avatar. Checkboxes and radios can stay square.

## Elevation: borders, with one optional offset shadow

Depth comes from rule weight, not blur. That means two token groups.

**Rule weights**
```css
--border-width-thin: 1px;   /* table rows, dividers inside a block */
--border-width-base: 2px;   /* inputs, cards, buttons */
--border-width-heavy: 4px;  /* section breaks, the masthead rule, focus ring */
--border-color-strong: var(--color-ink);  /* semantic: the black rule */
```

**Elevation levels (semantic, three)**
```css
--elevation-flat:    none;                                   /* on the page */
--elevation-raised:  none;                                   /* same shadow; component adds a base border */
--elevation-overlay: 4px 4px 0 0 var(--color-ink);           /* menus, dialogs, popovers */
```

- `flat` and `raised` don't differ in shadow. `raised` means "has a `border-width-base` rule around it". You can drop `raised` and just use the border token if you'd rather keep the set to two levels.
- `overlay` is my proposal, not something you asked for. A menu floating over content needs something to separate it from what's underneath, and a hard offset with no blur matches the brand. If you'd rather have no shadows at all, use a `border-width-heavy` rule on overlays instead.
- There are no blur shadows and no opacity-based depth. Surfaces are paper or white, never tinted.

## Motion: nearly nothing

```css
--duration-instant: 0ms;     /* default: hover, press, focus, toggle all snap */
--duration-quick:   120ms;   /* only where a sudden jump would confuse: overlay appear, disclosure open */
--easing-standard:  cubic-bezier(0, 0, 0.2, 1);

@media (prefers-reduced-motion: reduce) {
  :root { --duration-quick: 0ms; }
}
```

- Hover and press states change by inverting colors (black fill, paper text, or the tomato accent), and they do it instantly. That is `duration-instant`, so components still read a token.
- Anything over 150ms, any bounce and any slide-in is out of the system. A single easing is enough at these durations.
- No page transitions, scroll effects or skeleton shimmer. For loading, use a static text state such as "Loading…" in the condensed headline face.

## Tiers and exceptions
- **Raw:** `0`, `1/2/4px`, `0/120ms`, the one cubic-bezier, and the black and tomato colors from your color tokens.
- **Semantic:** the names above, which components consume.
- **Component-level:** none. Add one only if a component needs its own knob.
- Anything outside these values, such as a one-off print-style hero rule, stays local and is marked as an exception.

## Open decisions
1. Whether to keep the `overlay` offset shadow or use a heavy border instead.
2. Whether any element needs a round shape, which would justify `radius-full`.

I haven't contrast-checked anything here. These tokens reference your ink and tomato colors but don't set them.
