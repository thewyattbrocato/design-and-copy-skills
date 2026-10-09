Nothing is wrong with it, so I haven't changed anything.

- The `font` shorthand is valid. It has both a size and a family, which are the two required parts, and the `/1.6` line-height is in the right place.
- `max-width: 66ch` with `margin: 0 auto` centers the column at a comfortable reading width.
- The `h2` and `p` margins are fine. Vertical margins collapse between siblings, so the spacing between an `h2` and the paragraph after it behaves as you'd expect.

One optional nit: `17px` ignores a user's browser font-size setting. If you want that respected, use `1.0625rem`. It's a preference, not a bug.
