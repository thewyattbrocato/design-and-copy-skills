Your numbers are probably left-aligned or in a proportional font, so the digits don't line up. Fix it in two steps:

1. Right-align the column (`text-align: right`) so the decimal points stack.
2. Use tabular figures (`font-variant-numeric: tabular-nums`) so every digit has the same width.

Also keep two decimals on every value, like `$98.00`.
