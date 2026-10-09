**Ship B.** A and C both break the content you're displaying.

- **A** uses a proportional font, so aligned timing columns drift out of line. `white-space: normal` also collapses the indentation in stack traces, and `max-width: 60ch` forces a 150-character line onto three or more visual lines, which makes the log hard to scan.
- **C** keeps `monospace`, but `max-width: 60ch` still wraps every 120–200 character line. Wrapped continuation lines start at the left edge, so a stack frame's text no longer lines up under its own line. Columns also shift when wrapping happens at different points.
- **B** keeps every log line on one visual line, so columns and indentation stay aligned. `overflow-x: auto` lets developers scroll sideways to read the long lines. Monospace is what makes aligned columns work at all.

On matching the blog: the blog is prose and the log is machine output that people read for its exact columns, so the two should look different. A consistent typeface family is still a reasonable goal, but readability of the log matters more.

Two small adjustments to B:

- Set `tab-size` (for example `tab-size: 4`) if your output contains tabs, so indentation renders consistently.
- Make sure the pane has a fixed or constrained width. `overflow-x: auto` only produces a scrollbar when the containing element is narrower than the content.

If developers ask for wrapped lines, add a toggle that switches between `pre` and `pre-wrap`. Keep `pre` as the default.
