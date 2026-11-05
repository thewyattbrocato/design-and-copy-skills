Keep these three groups small. The brand is flat, so most tokens should resolve to zero or to a border, and the system should make it hard to add anything else.

## Shape

```css
--radius-none: 0;
```

Define the token even though it's zero. Components then reference `var(--radius-none)` instead of hard-coding `border-radius`, and a lint rule can reject any other radius. Skip `sm/md/lg/pill` scales, since they invite drift. Apply the same rule to inputs, images, tags, and focus rings.

## Depth

Boxcar's depth comes from heavy rules and stacking order, not blur. Define borders and z-index, not soft shadows.

```css
--ink: #111;                     /* or your black */

--rule-hairline: 1px;            /* table rows, dividers */
--rule-default: 3px;             /* edges of buttons, cards, inputs */
--rule-heavy: 6px;               /* masthead, section breaks */
--rule-color: var(--ink);

--z-base: 0;
--z-raised: 10;
--z-overlay: 100;                /* scrim behind dialogs */
--z-modal: 200;
--z-toast: 300;

--scrim: rgb(17 17 17 / 0.6);    /* flat, no backdrop-filter blur */
```

Don't define `--shadow-soft` or any blur-based token. Keeping them out of the system is what stops them from creating drift later.

One decision for you: do you want a **hard, unblurred offset block** for raised items, such as a card lifting on hover?

```css
--shadow-block: 4px 4px 0 var(--ink);
```

It fits the blunt look, but it's a real brand call. If yes, define this one token as your only elevation value. If no, elevation is just rules plus z-index, and you define no shadow tokens.

## Motion

Keep this section almost empty:

```css
--duration-instant: 0ms;         /* default for every state change */
--duration-short: 120ms;         /* only if something truly needs signalling */
```

- Hover, press, focus, and open/close should be **instant** color or rule swaps. Don't fade them.
- Skip easing tokens until you have a real use for one. If you need one, use `linear`.
- Add the reduced-motion baseline even though there's little motion to reduce:

```css
@media (prefers-reduced-motion: reduce) {
  :root { --duration-short: 0ms; }
}
```

## Confirm before building

1. Is the hard offset block shadow in, or is depth rules-only?
2. Are 1px, 3px, and 6px the right rule weights, or do you want different values?

Once you answer, I can write these into the design system's token file in whatever format you're using (CSS variables, JSON, or a Tailwind/Style Dictionary config).
