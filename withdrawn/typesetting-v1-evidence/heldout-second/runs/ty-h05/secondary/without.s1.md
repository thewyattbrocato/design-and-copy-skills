**Ship B.** It's the only one that keeps each log line on one row, so the aligned timing columns and stack-trace indentation stay readable.

- **A** uses a proportional font with `white-space: normal`, so spaces collapse and columns stop lining up. The 60ch cap also forces 120 to 200 character lines to wrap into several fragments each.
- **C** has a monospace font and preserves spaces, but `pre-wrap` at 60ch still wraps every long line. Continuation lines start at column 0, so a stack frame or timing row breaks apart and the columns no longer line up.
- **B** uses `white-space: pre` with `overflow-x: auto`. Each line stays intact, and the 200-character lines scroll horizontally in the pane. At 13px monospace, 200 characters is about 1,500px, which is fine for a scrollable log pane.

Matching the blog's look is reasonable for colors, the header, and chrome. The body of a log viewer should follow the needs of the content, though, and the blog's prose typography works against it here.
