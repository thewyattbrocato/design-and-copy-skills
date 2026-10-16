The footer has `margin: 0`, and the last section only adds an 8px bottom margin, so the only separation between content and the footer's top border is that 8px (`main`'s 24px bottom padding sits inside `main`, but it's the only real buffer, and it's overwhelmed by the tiny 8px section gap and the footer's compact 8px padding). The result is a cramped transition with little visual breathing room around the border line.

The single change that fixes it is to give the footer top margin, for example `footer { margin: 32px 0 0; }`, which pushes it clear of the content.
