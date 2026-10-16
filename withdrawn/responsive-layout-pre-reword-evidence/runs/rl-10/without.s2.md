Here's the updated CSS. It adds one shared rule for side padding, and `header .inner` and `main` now use it:

```css
body { margin: 0; font: 17px/1.55 Georgia, serif; color: #222; background: #fbfaf7; }
header { background: #1d3b2a; color: #fff; padding: 20px 0; }
header .inner { padding: 0; }
main { padding: 40px 0; }
main p, main li { margin: 0 0 1em; }
pre { background: #efece4; padding: 16px; overflow: auto; }
img { width: 100%; }

/* Readable column: ~720px max, at least 20px gutters on small screens */
header .inner,
main {
  padding-left: max(20px, calc((100% - 720px) / 2));
  padding-right: max(20px, calc((100% - 720px) / 2));
}
```

- **Big monitors:** the text and header content stay in a centered column about 720px wide (roughly 75 characters per line at 17px). The header's green background still spans the full width.
- **Phones:** the side padding never drops below 20px, so text no longer touches the edges.
- **Everything else:** colors, fonts, vertical spacing, code blocks and images are untouched. Images and `pre` blocks sit inside the same column.

I didn't see your HTML, so I assumed `header .inner` and `main` are the elements holding the content. I also picked 720px myself. If your laptop layout is wider than that, raise the value in both places to match.

I haven't viewed this in a browser.
