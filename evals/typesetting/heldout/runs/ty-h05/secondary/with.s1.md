**Ship B.** It's the only one that keeps the columns aligned, and alignment is the main thing a log viewer has to get right.

- **A** is the worst fit. A proportional font breaks the timing columns, and `max-width: 60ch` with normal wrapping turns each 120–200 character line into 2–4 ragged lines. Stack traces lose their structure.
- **C** is better than A because it's monospace and `pre-wrap` keeps leading indentation. But `max-width: 60ch` still forces wrapping, and continuation lines start at the left edge, so they don't line up under the column they belong to. The 60ch measure is a prose convention, and it's wrong for log output.
- **B** preserves every line exactly as the job printed it. Long lines scroll horizontally, which is how most CI log views (including GitHub Actions') handle them. At 13px monospace, a 200-character line is roughly 1,500px wide, so developers will scroll for the longest traces. That's the trade-off you're accepting.

Two small additions to B:

```css
.log {
  font: 13px/1.45 ui-monospace, Menlo, Consolas, monospace;
  white-space: pre;
  overflow-x: auto;
  tab-size: 4;             /* stack traces and aligned output often contain tabs */
}
```

If developers ask for wrapping later, add it as a toggle rather than the default. Use `pre-wrap` without `max-width`, and give continuation lines a hanging indent so they stay under the text they belong to.

On your teammate's point: matching the blog is reasonable for brand colors and the page chrome, but the log pane is reading data, not prose, so it should follow the rules for code and tables rather than the blog's text settings.

I reasoned this from how these CSS properties behave, not from rendering it. Before shipping, paste a real 200-character trace with timing columns into the pane and check that the columns line up.
