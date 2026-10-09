Your palette already works, and I wouldn't swap any colors. It's a warm paper, a dark ink with a green-blue tint, and one rust accent, which suits letterpress. I worked out the contrast ratios by hand, so treat them as estimates.

| Pair | Ratio | Verdict |
|---|---|---|
| Ink on Paper | about 13:1 | Excellent |
| Rust on Paper (links, button fill) | about 4.8:1 | Passes for text |
| Paper text on Rust button | about 4.8:1 | Passes |
| Muted on Paper | about 4.9:1 | Passes |
| Sage on Paper | about 3.0:1 | Fine for rules, too low for text |
| Ink on Sage | about 4.3:1 | Just under 4.5 |

**Changes, by impact**

1. **Sage tags with text.** Sage fails as a fill under ink text and as a text color on Paper. Keep `#7c9082` for rules and borders only. For tags, use a pale sage fill `#e1e6dc` with deep sage text `#4a5d50` (about 5.6:1), plus an optional 1px `#7c9082` border.
2. **Rust hover and pressed state.** Add `#9a3a21` (about 6.2:1 on Paper). This gives buttons and links a visible state without a second accent.
3. **One raised surface.** Add `#ece5d4` for cards, price-list rows and the footer. It's a small step darker than Paper, so sections separate without heavy borders. Ink and Muted both still pass on it, though Muted falls to about 4.3:1 there. Use Ink for anything small on that surface, or keep Muted text on Paper.
4. **Hairline dividers.** Use `#d9d0bc` for thin lines. It's quieter than sage and looks more refined.

Most of the "premium" feel will come from type, spacing, paper stock and the rust staying scarce, rather than from color. On the printed price list, rust and sage will shift depending on your ink and stock, so proof them. Screen hex values won't match.
