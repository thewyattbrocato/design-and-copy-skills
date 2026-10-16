**Ship B.**

Build logs are fixed-width data, not prose. The columns of timings only line up in a monospace face. Stack traces and 120–200 character lines only stay legible if they don't reflow.

**Why not A:** It uses a proportional font, so the aligned timing columns break. `white-space: normal` collapses the indentation and newlines that stack traces depend on. `max-width: 60ch` would also wrap every long line. The blog's measure and leading are for prose, and a log isn't prose.

**Why not C:** It's the right face, but `max-width: 60ch` with `pre-wrap` wraps 120–200 character lines into 2–4 pieces. That wrapping breaks column alignment and makes a wrapped trace line look like a separate line. At 15px, even a wider cap would show fewer columns per screen.

**B's trade-off:** Long lines scroll horizontally. For logs that's the accepted cost, because the alternative is losing the structure. You can soften it:

```css
.log {
  font: 13px/1.45 ui-monospace, Menlo, Consolas, monospace;
  white-space: pre;
  overflow-x: auto;
  font-variant-numeric: tabular-nums; /* harmless in mono, helps if the fallback is proportional */
  tab-size: 4;
}
```

- Offer a "wrap lines" toggle that switches to `white-space: pre-wrap; overflow-wrap: anywhere`. Developers sometimes want it, but it shouldn't be the default.
- 13px is fine for a dense tool pane. If your users complain it's small, try 14px before changing anything else.

**For your teammate:** She can still get the blog look in the chrome around the log, such as the header, job title, step names and buttons. Only the log body needs to be monospace.
