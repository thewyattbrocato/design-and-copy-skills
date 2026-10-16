I made a handful of changes. I didn't touch the type scale, measure, or link and muted colors. Both colors pass AA contrast on white (the link color is about 7:1).

```css
:root { --ink: #1d2327; --muted: #5a646b; --link: #0b5cab; }
html { -webkit-text-size-adjust: 100%; text-size-adjust: 100%; }
body {
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  font-size: 1.125rem;
  line-height: 1.6;
  color: var(--ink);
  background: #fff;
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
td, th { padding: 0.5rem 0.75rem; text-align: left; border-bottom: 1px solid #d5dade; }
th { border-bottom-color: var(--muted); }
td.num, th.num { text-align: right; }
code { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 0.9em; }
```

**What changed and why**
- **`background: #fff` on body:** you set a text color but no background. Browsers that force a dark theme (some Android and extension setups) could otherwise put dark ink on a dark page.
- **Removed `p + p { margin-top: 0; }`:** it did nothing, because `p` already has a top margin of 0.
- **`.label` raised from 12px to 13px:** 12px uppercase is hard to read, especially for a legal aid audience.
- **Added `h3`, `ul`/`ol` and `li` styles:** a guide like this almost certainly uses subheadings and lists, and without these they'd fall back to browser defaults that don't match your spacing. Delete them if the guide has neither.
- **Table row rules:** I added light dividers and a stronger rule under the header. Without borders, wide rows are hard to follow across the line.
- **`text-wrap: pretty` on paragraphs:** this avoids single-word last lines. It's progressive enhancement and harmless where unsupported.
- **`overflow-wrap: break-word` on `main`:** long URLs and statute citations can't push the page sideways on phones.
- **Unprefixed `text-size-adjust`:** added alongside the `-webkit-` version.

**Check before launch**
- `hyphens: auto` only works if the page has `<html lang="en">` (or the right language). If it's missing, hyphenation silently does nothing. If you'd rather not hyphenate legal terms at all, change it to `hyphens: manual`.
- If the guide has a Spanish version, it needs its own `lang="es"`.
