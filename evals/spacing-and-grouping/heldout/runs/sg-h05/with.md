**Use a 1px hairline between rows, with comfortable padding inside each row.** Don't use extra space between rows or zebra striping.

**Why, for 30 uniform rows:**

- **Extra space between rows** only groups well when items form distinct units. Here every row is the same kind of thing, so gaps just cut the rows per screen and add scrolling. Space also gives your eye nothing to track along a row, from the date on the left to the amount on the right.
- **Alternating backgrounds** are built for wide tables with many columns, where the eye can lose its row. With three fields they add visual noise, and they break down when you add anything that already uses a background:
  - pending or selected states
  - date-group headers
  - the pressed state
  - dark mode, where low-contrast stripes tend to vanish or look muddy
- **A hairline** gives a scan line without using any extra height. It stays neutral, so you can still use background tint for meaningful states such as pending or selected.

**How to make it work:**

- **Padding:** give each row about 12–16px of vertical padding. The rule needs space on both sides of it. Touch targets should be at least 44px tall.
- **Rule style:** use a quiet color, such as a low-contrast gray. Use one weight throughout.
- **Rule inset:** start the rule at the text's left edge instead of the screen edge. It then reads as a list divider and not a table border.
- **Spacing owned by the container:** put the rule on the following row, or use a divider. That way the last row doesn't get a stray line.
- **Grouping:** with 30 rows, group by day or week with a sticky header, for example "Today" or "Oct 12". Put more space above each header than below it, so it sits closer to its own rows. This is where space is the right tool, because it separates groups and not individual rows.
- **Alignment:** right-align amounts and use tabular numerals so the digits line up. That does more for scanning than any row separator.

**Summary:** hairlines separate the rows, space separates the day groups, and tint is reserved for states.
