I made a handful of changes, and the rest was already solid: the measure, the type scale, the contrast, the focus ring and the tabular numerals. I didn't have a file or the page markup, so I haven't rendered any of this.

```css
:root { --ink: #1d2327; --muted: #5a646b; --link: #0b5cab; --rule: #d5dadd; }
html { -webkit-text-size-adjust: 100%; }
body {
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  font-size: 1.125rem;
  line-height: 1.6;
  color: var(--ink);
  margin: 0;
}
main { max-width: 38rem; margin: 0 auto; padding: 2.5rem 1.25rem 4rem; overflow-wrap: break-word; }
h1 { font-size: clamp(2rem, 5vw, 2.75rem); line-height: 1.12; letter-spacing: -0.015em; margin: 0 0 1rem; text-wrap: balance; }
h2 { font-size: 1.5rem; line-height: 1.25; margin: 2.5rem 0 0.75rem; text-wrap: balance; }
h3 { font-size: 1.1875rem; line-height: 1.3; margin: 1.75rem 0 0.5rem; text-wrap: balance; }
p { margin: 0 0 1em; hyphens: auto; text-wrap: pretty; }
ul, ol { margin: 0 0 1em; padding-left: 1.5em; }
li { margin-bottom: 0.4em; }
a { color: var(--link); text-decoration: underline; text-underline-offset: 0.15em; text-decoration-thickness: 0.08em; }
a:focus-visible { outline: 3px solid currentColor; outline-offset: 2px; }
small, .note { font-size: 0.875rem; line-height: 1.5; color: var(--muted); }
.label { font-size: 0.8125rem; text-transform: uppercase; letter-spacing: 0.08em; font-weight: 600; }
table { border-collapse: collapse; width: 100%; font-variant-numeric: tabular-nums; }
td, th { padding: 0.5rem 0.75rem; text-align: left; border-bottom: 1px solid var(--rule); }
th { font-weight: 600; }
td.num, th.num { text-align: right; }
code { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 0.9em; }
pre { overflow-x: auto; }
```

**What changed and why**
- **Removed `p + p { margin-top: 0; }`.** It did nothing, because `p` already has no top margin.
- **Added `overflow-wrap: break-word` on `main`.** Long URLs and statute citations won't push the page sideways on phones, which matters for a legal guide.
- **Bumped `.label` from 12px to 13px.** Uppercase at 12px is hard to read for some people.
- **Added `text-wrap: pretty` on paragraphs.** It avoids one-word last lines.
- **Added `ul`/`ol`/`li` and `h3` styles.** A guide almost certainly uses them, and browser defaults wouldn't match this rhythm. Delete them if the page doesn't use them.
- **Added thin row rules and an explicit `th` weight to tables.** Without borders, wide rows are hard to track.
- **Added `pre { overflow-x: auto }`.** Code blocks scroll instead of overflowing the page.

**Check before launch:** `hyphens: auto` only works if the page has `<html lang="en">` (or `es`, and so on). If the clinic publishes translations, each one needs its own `lang` value.
