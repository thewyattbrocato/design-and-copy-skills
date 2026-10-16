```css
body { font: 1.0625rem/1.55 Arial, sans-serif; color: #2b2b2b; background: #fbfaf7; margin: 0; }
.page { padding: 1.5rem 3rem; }
h1 { font-size: 2rem; line-height: 1.2; margin: 0 0 1rem; text-wrap: balance; }
h2 { font-size: 1.375rem; line-height: 1.25; margin: 2.25rem 0 0.75rem; text-wrap: balance; }
p { margin: 0 0 1em; max-width: 65ch; text-wrap: pretty; }
.note { font-size: 0.875rem; color: #777; }
```

Colors and HTML are unchanged.

- **Body text:** It's now 17px, up from 13px, with line height 1.55 instead of 1.2. Both were making the text tiring to read.
- **Line length:** Paragraphs are capped at 65 characters (`max-width: 65ch`) so they no longer run edge to edge on a 1440px screen. The cap is on `p`, not `.page`, so headings and any other elements can still use the full width.
- **Headings and spacing:** `h2` now has about three times as much space above it as below (36px against 12px), so each heading sits with the section it introduces. Paragraphs are separated by a one-line gap.
- **Sizes:** The sizes are 32px for `h1`, 22px for `h2`, 17px for body and 14px for notes.

Two things to check:
- `.note` is 14px, up from 10px, but its `#777` gray on the cream background is a bit light. You asked me not to touch colors, so I left it. If the notes hold anything tenants need to act on, consider darkening it.
- The paragraph cap leaves the right side of the page empty on wide screens. If that looks lopsided, you could add `margin-inline: auto` to `.page` with a `max-width`, but I haven't made that change.
