# Alignment and numbers

Load this whenever a table holds figures. Digits only compare well when they stack by place value, so most of this file is about making that happen.

## Alignment by data type

| Content | Align | Notes |
| --- | --- | --- |
| Names, descriptions, categories | Left | Header left too. |
| Integers, money, measures | Right | Header right, so it sits over the last digit. |
| Decimals with varying places | On the decimal point | See below. |
| Dates and times | Left | One fixed-width format throughout. |
| Short codes, icons, checkboxes | Center | Only when every value has the same width. |
| Long mixed text and numbers | Left | Treat as text. |

Keep each header aligned like its column. A right-aligned number under a left-aligned header looks like two unrelated things.

## Figure style

```css
td.num, th.num { text-align: right; font-variant-numeric: tabular-nums lining-nums; }
```

Tabular figures give every digit the same width, so a column of prices does not wobble. If the chosen typeface has no tabular figures, set the numeric columns in a system face or monospace that does. Proportional figures stay in running text.

## Decimal alignment

When a column holds values with different numbers of decimals (3, 3.5, 3.25), pad every value to the same number of places so right alignment already lines up the points. Pad with `.00` rather than leaving ragged ends. When a column mixes units, scales or ranges (12 kg, 4.5 g), split it into separate columns or convert to one unit.

## Precision

- Choose digits by the decision: a price comparison needs cents, a population comparison rarely needs units, a percentage change rarely needs more than one decimal.
- Use the same precision down a column. Different columns can differ.
- Do not show precision the data does not have. A sensor rounded to a tenth should not appear as 21.4000.
- Round for display and keep full values in the data. Sorting and totals use the full values; if displayed rows do not sum to a displayed total because of rounding, say so in a note.
- Compact forms (12.4K, 3.2M) fit a scanning table where order of magnitude matters. Tables used to check or reconcile figures should keep full numbers.

## Separators and locale

Use thousands separators in any number of four or more digits in a table (some styles leave four-digit numbers bare; pick one rule and keep it). Use the reader's locale when you know it: 1,234.56 in English, 1.234,56 in many European languages. In a table that spans locales, a thin space is a neutral separator. Never mix the two conventions in one column.

## Units and currency

- Put the unit in the header: "Weight (kg)", "Amount (USD)". Cells then hold bare numbers and the column reads cleanly.
- For one-currency financial tables, the symbol may also appear on the first row and on totals.
- When rows differ in currency or unit, put it in each cell, aligned in a consistent position (code after the number, or symbol before), and do not sum across them.
- Percent: put the percent sign in the header ("Change (%)") or in each cell, not both.
- Keep a number and its unit together on one line with a non-breaking space.

## Negatives and change

- Use a real minus sign or parentheses and keep one convention in the table. Accounting-style parentheses are right for statements; a minus sign is right almost everywhere else.
- Color can add a second cue (red for negative), never the only cue.
- For change columns, show an explicit sign on positive values too (+4.2%), so direction is readable without color.
- With parentheses, add a trailing space to positive values or use a figure-width pad so the digits still line up.

## Dates and times

Use one format everywhere in the table, fixed width where you can (2026-03-09, or 9 Mar 2026). Spell the month out or abbreviate it, so day and month order is never ambiguous. Put the time zone in the header or caption when times matter. Relative times ("3 days ago") hide the exact value; give the exact one on hover and focus, or in a title for the cell.

## Missing and special values

| Situation | Show |
| --- | --- |
| Not applicable | n/a or an em dash |
| Not yet known or not collected | An em dash, with a note |
| Truly zero | 0 |
| Below detection or threshold | "< 0.1" |
| Withheld or restricted | A labeled mark with a note |

Never leave a cell blank: the reader cannot tell missing from zero from a loading failure. If the table uses more than one kind of gap, give each a distinct mark and explain them in a note under the table.

## Totals and sums

Put totals in a final row or a pinned footer, above them a heavier rule, and in heavier weight. Label them in the first column ("Total"). Subtotals sit under their group with a lighter rule. Show the unit once on the total if the column header does not carry it.
