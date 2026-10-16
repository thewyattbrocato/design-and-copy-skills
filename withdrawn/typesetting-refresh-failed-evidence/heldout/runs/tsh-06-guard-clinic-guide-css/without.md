I made a few small changes. The rest was already solid: the measure, the line heights, the contrast, the focus ring, and `tabular-nums`.

```css
:root { --ink: #1d2327; --muted: #5a646b; --link: #0b5cab; }
html { -webkit-text-size-adjust: 100%; text-size-adjust: 100%; }
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
h3 { font-size: 1.25rem; line-height: 1.3; margin: 2rem 0 0.5rem; text-wrap: balance; }
p { margin: 0 0 1em; text-wrap: pretty; }
ul, ol { margin: 0 0 1em; padding-left: 1.5em; }
li { margin-bottom: 0.35em; }
a { color: var(--link); text-decoration: underline; text-underline-offset: 0.15em; text-decoration-thickness: 0.08em; }
a:focus-visible { outline: 3px solid currentColor; outline-offset: 2px; }
small, .note { font-size: 0.875rem; line-height: 1.5; color: var(--muted); }
.label { font-size: 0.8125rem; text-transform: uppercase; letter-spacing: 0.08em; font-weight: 600; }
table { border-collapse: collapse; width: 100%; font-variant-numeric: tabular-nums; }
td, th { padding: 0.5rem 0.75rem; text-align: left; }
th { font-weight: 600; border-bottom: 2px solid currentColor; }
td { border-bottom: 1px solid #d5d9dc; }
td.num, th.num { text-align: right; }
code { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 0.9em; }
```

**What changed and why**
- **Removed `hyphens: auto` on `p`.** At this measure (about 65–70 characters) it isn't needed. Auto-hyphenation also splits legal terms and names awkwardly, and it only works if `<html lang="en">` is set. Added `text-wrap: pretty` instead, which avoids orphaned last lines.
- **Removed `p + p { margin-top: 0 }`.** It was a no-op.
- **`.label` is now 13px instead of 12px.** Small uppercase text with wide tracking gets hard to read at 12px.
- **Added `ul`, `ol`, `li` and `h3` rules.** A tenant guide almost certainly has lists and subheads, and without these they fall back to browser defaults that don't match your rhythm. If the guide has none, delete them.
- **Table header and row rules.** I gave `th` a weight and a bottom border, and `td` a light divider. Right-aligned numbers are hard to follow across a row without something to guide the eye.
- **`overflow-wrap: break-word` on `main`.** Long URLs, such as links to court or agency pages, won't force horizontal scrolling on phones.
- **Added the unprefixed `text-size-adjust`.** It sits alongside the `-webkit-` version.

**Before you hand off**
- Confirm `<html lang="en">` is set. It matters for screen readers and for any hyphenation or quote handling.
- If the tables are wide, wrap them in a container with `overflow-x: auto` so they scroll on small screens.
