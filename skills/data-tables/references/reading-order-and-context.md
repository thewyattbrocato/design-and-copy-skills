# Reading order and context

Load this when a table is for comparing or ranking, has derived figures, will be printed or paged, or will be read by someone who was not in the room when it was made.

## Start from the job

Finish the sentence "The reader opens this to ___". Lookup ("what is the rate for this term") and compare ("which campaign is behind") want different tables. Lookup: sort for finding, keep rows plain. Compare: put the compared values next to each other, sort by the value that matters, and make the one cell that answers the question the easiest to spot. If the sentence has two verbs, build for the first and leave the second reachable but quiet.

## What the reader compares

**Rows or columns.** Rows hold the things people scan for; they can grow without breaking the layout. A short, fixed set of comparison points (a few periods, two or three plans) goes in columns when it fits without wrapping. When either side may grow, or rows get filtered, sorted or exported, keep one row per record.

**A grouped hierarchy** (region, then branch) reads as indented rows or a grouped header, never the same region name repeated on every row.

**Column order.**

1. Identifier on the left, then columns in the order the reader's question uses them.
2. A derived column sits right next to the figures it comes from: sessions, then sign-ups, then sign-up rate.
3. Columns that will be compared sit side by side, not separated by a note column.
4. A summary column is set apart by a rule or weight, so it is not mistaken for another period.

**Row order** comes from the data, not from habit:

- Time or any natural sequence (months, sizes, stages): keep that sequence.
- Ranking or "who needs attention": sort by the value, worst or best first, and say so in the caption.
- Names to look up: alphabetical.
- Never leave rows in database-id order. Alphabetical order on ranked data buries the answer.

## What the reader needs to trust it

**Provenance line.** One quiet line under the title or in the caption, using only facts given or visible in the data: what is measured, the period, the as-of date, the unit, the source. A table passed on without it gets misread. When a fact is missing, write a visible placeholder ("as of [date]") and say it needs filling; never guess a date or source.

**Totals and averages** follow [alignment and numbers](alignment-and-numbers.md#totals-and-sums).

**Long and printed tables.**

- Repeat the column header on every page: `thead { display: table-header-group; }` and `tr { break-inside: avoid; }`.
- Break pages between groups, not inside one. Repeat the group heading when a group spills over ("Group B, continued").
- On screen, keep the header sticky, and the group heading too when groups are long.
- Set the print version in black on white, 10 to 11pt, with hairlines only; drop the hover states and shading.
- Do not stretch to the full width. Size columns to their content, keep a gap of about half the row height between columns, and leave the right side empty rather than spreading the table across it.

## Before and after

Before: ID, channel, sign-up rate, sessions, sign-ups, alphabetical, no date, header lost on page two.
After: channel, then sessions, sign-ups, rate; sorted by rate, lowest first; a caption "Sorted by sign-up rate, lowest first. As of [date]."; repeating header; a labeled median row.
