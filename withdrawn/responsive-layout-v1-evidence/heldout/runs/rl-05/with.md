**What's happening**

`flex: 1` is shorthand for `flex: 1 1 0%`. It lets `.info` grow and shrink, but it doesn't let it shrink below its minimum content size.

A flex item's `min-width` defaults to `auto`. For a flex item, that resolves to the width of its longest unbreakable content. Your email address has no spaces, so the browser can't wrap it. Its full width becomes the floor for `.info`.

The avatar, the button and the gaps can't shrink to make room, so the row overflows. The card gets wider than the screen, and the page scrolls sideways.

`flex: 1` isn't ignored. It just can't push `.info` below that floor.

**The fix**

```css
.volunteer-card { display: flex; align-items: center; gap: 12px; padding: 12px; }
.info { flex: 1; min-inline-size: 0; }
.info span { overflow-wrap: anywhere; }
.avatar, button { flex: none; }
```

- `min-inline-size: 0` (or `min-width: 0`) removes the floor, so `.info` can shrink to the space left over.
- `overflow-wrap: anywhere` lets the email break across lines. You'll see this wrapping on phones, and it keeps the full address readable.
- `flex: none` on the avatar and button stops them from being squeezed. Without it, the avatar could shrink and distort.
- `.info span` is a `span`, so it's inline by default. `overflow-wrap` still works on it, because the property applies to the text inside the block container `.info`.

If you'd rather truncate than wrap, use this instead:

```css
.info span { display: block; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
```

Truncation hides part of the address, so I'd wrap it. Volunteers may need to read the whole thing.

**Widths I checked by reasoning (not run in a browser)**

- **320px:** `.info` gets about 320 − 24 (padding) − 56 (avatar) − 24 (gaps) − the button width. The email wraps inside that space, so nothing overflows.
- **Wide screens:** There's no change. The text fits on one line, and `.info` takes the leftover space.

I kept the existing layout and added no media queries. The only changes are the overflow guards above.
