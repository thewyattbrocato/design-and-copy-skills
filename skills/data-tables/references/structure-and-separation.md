# Structure and separation

Load this when styling the table itself: headers, row separation, density, totals, grouping, widths and wrapping.

## Rule hierarchy

Use as little furniture as the content permits, and make each line mean something:

1. Heaviest: a rule under the header (about 1.5 to 2px, or a color step).
2. Medium: a rule above a total row, and between major groups.
3. Lightest: a hairline between ordinary rows (1px, low contrast), or none at all when spacing does the work.
4. Vertical rules: rare. Use them only to split groups of columns or when two columns would be read together by mistake.

Choose one of the following for the body rows, never all three:

- Space only: tall enough rows with consistent padding; works for narrow tables of 3 to 5 columns.
- Hairlines: the default for most tables.
- Alternating shading: for wide tables where the eye follows a row across many columns. Keep the contrast gentle; text on the tinted rows must still meet the contrast minimum.

Add a hover or focus highlight to rows that are clickable, and make it a quiet background change. Selected rows get a clearer, different state than hovered ones.

## Header design

- Short, sentence case, one line when possible; the unit goes in parentheses.
- Distinguish the header with weight or a quiet background, not a loud fill.
- Header cells follow the alignment of their column.
- Spanning headers group related columns (such as four quarters under "2026"); use one level, rarely two.
- For long tables, keep the header visible when scrolling (`position: sticky; top: 0` with an opaque background and a bottom rule so rows do not show through).
- Do not rotate header text. Shorten it, widen the column, or allow two lines.

## Density

| Level | Row height | Use |
| --- | --- | --- |
| Comfortable | 44 to 56px | Short tables, occasional readers, touch use |
| Default | 40 to 48px | Most business tables |
| Compact | 32 to 36px | Expert tools with many rows |

Cell text stays at 14px or larger; 13px is the floor in compact tables. Tighten the vertical padding, not the font. Let the user switch density in a tool they live in. Keep horizontal padding at 12 to 16px so columns do not touch. Large tables do not need larger rows, but they do need a visible header and a consistent rhythm.

## Column widths

- Size numeric columns to their widest value plus padding; they should not stretch.
- Let one or two text columns take the remaining space.
- Set a `min-width` and a `max-width` on text columns so one outlier value does not set the width for every row.
- Keep the identifying column wide enough to hold a typical name without wrapping.
- With `table-layout: fixed`, set widths on the header row so columns do not jump when data loads or when paging.

## Wrapping and truncation

- Wrap descriptive text columns; give them a readable maximum width (about 40 to 60 characters).
- Keep numbers, dates, codes and status on one line (`white-space: nowrap`).
- Truncate with an ellipsis only text that is not needed to understand the row, and provide the full value on focus and hover, in a detail view, or by expansion. A truncated id that people must copy needs a copy control.
- Do not truncate a value that distinguishes two rows (two files named alike, differing at the end): truncate the middle, or wrap.

## Totals, subtotals and grouped rows

- A final total row sits under a medium rule, in heavier weight, labeled in the first column.
- Subtotals sit under their group, with a lighter rule and regular or semibold weight.
- Group headings in a statement can be indented rows; indent children by about 1 to 1.5em, not by adding columns.
- Collapsible groups show a chevron, say whether the group is open, and keep totals visible when collapsed.
- For very long tables, repeat the totals at the top or pin them.

## Emphasis

One quiet signal per idea. Total: weight. Outlier or best value: a small marker or a tinted background plus a note that explains it. Overdue or failed row: a label in words and a subtle row tint, not a screaming fill. If more than about one in five rows is emphasized, nothing is.

## Inline bars and small trends

A bar inside a cell works when the reader compares magnitude across rows. Keep the bar light, anchored at a common baseline, scaled consistently across the column, and keep the exact number beside it. A tiny trend line works when the shape matters more than the values; give it a label. For anything richer, pass the problem to chart-design.
