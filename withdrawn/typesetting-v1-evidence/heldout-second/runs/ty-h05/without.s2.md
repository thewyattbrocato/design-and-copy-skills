**Ship B**, with a couple of small tweaks.

**Why not A:** It's a proportional font with `white-space: normal`, which collapses whitespace and wraps lines. That breaks the two things your content depends on:
- Aligned timing columns fall apart, because proportional glyphs and collapsed spaces destroy the alignment.
- Stack traces lose their indentation, and a 60ch cap forces 120–200 character lines to wrap awkwardly. Matching the blog isn't worth that. A log viewer is a code-reading surface, not prose.

**Why not C:** Monospace and `pre-wrap` preserve whitespace, which is good. But `max-width: 60ch` wraps almost every line at roughly a third of its length. Wrapped columns misalign, and it's hard to tell where one log line ends and the next begins. 15px also shrinks how many lines fit on screen.

**Why B works:** Monospace plus `white-space: pre` keeps columns and indentation exact. `overflow-x: auto` lets long lines scroll instead of wrapping. 13px/1.45 is dense enough to scan a lot of output, which is what someone debugging a failed job needs.

**Tweaks I'd make to B:**
```css
.log {
  font: 13px/1.45 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  white-space: pre;
  overflow-x: auto;
  tab-size: 4;
  font-variant-ligatures: none;
}
```
- `tab-size` keeps tab-indented traces readable.
- Turning off ligatures stops `->` or `!=` from rendering as different glyphs.
- Optionally, add a "wrap lines" toggle that switches to `pre-wrap`. Some people want it for reading long error messages, but keep it off by default.

**For your teammate:** You can still tie the viewer to the blog's look through the surrounding UI, such as the header, colors, and buttons, and keep the blog's font for the chrome. The log body itself should be monospace.
