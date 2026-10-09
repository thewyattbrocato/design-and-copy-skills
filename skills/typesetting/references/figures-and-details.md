# Figures and details

Load this when text holds figures, units, dates, quotes, dashes or capitals, or must be truncated.

## Figures

- **Tabular lining**: prices in lists, order summaries, tables, timers, counters, anything that updates in place. `font-variant-numeric: tabular-nums;` (add `lining-nums` if the face defaults to old-style).
- **Proportional**: running prose. **Old-style**: long editorial prose with lowercase only, in a face that has them; use lining figures beside full capitals. Never old-style in a column of numbers.
- If the face has no tabular figures, use a face that does for that column. Do not fake alignment with spaces.
- Right-align numbers so digits stack by place value; align on the decimal when decimals vary, and show the same decimals on every row (12.50, not 12.5 beside 8.00).
- Put the currency or unit in the header when every row shares it; repeat it per row when rows mix units. A total differs by one step (weight or a rule), not face, size and color together.
- Long digit strings (phone, card, account numbers) read better in groups with a little letterspacing.

```css
.amount { font-variant-numeric: tabular-nums; text-align: right; }
```

## Units and spacing

- Keep a number with its unit using a non-breaking space: `12&nbsp;kg`, `5&nbsp;min`, `25&nbsp;MB`. A leading symbol (`$12`) stays attached with no space. Do not let an amount wrap away from its currency.
- Use a non-breaking space inside dates and names that would be awkward to split. One space after a sentence.
- Follow the locale for decimal comma, thousands separators and day-month order when the audience is known.

## Punctuation

| Use | Instead of |
| --- | --- |
| Curly quotes and a proper apostrophe | Straight quotes |
| En dash for ranges (2019–2024) | Hyphen |
| Closed em dash, or spaced en dash, for a break (one style per product) | Double hyphen |
| Multiplication sign for dimensions (4 × 6) | The letter x |
| Primes for feet and inches (5′ 10″) | Straight quotes |
| True minus (−) in numbers; ellipsis character | Hyphen; three periods |

Code, data and URLs keep their literal characters. Spell names with their accents and set a whole word in one face.

## Capitals and emphasis

- Sentence case by default. All caps for one to three words (status tags, column heads), tracked 0.05 to 0.1em, at 12px or more. Several sentences in capitals: rewrite them in sentence case.
- Real small caps (`font-variant-caps: all-small-caps`), tracked a little, never shrunken capitals. Never letterspace lowercase running text; use weight or italic for emphasis.
- Keep punctuation next to bold or italic in the surrounding style unless the whole phrase is emphasized.

## Breaks and truncation

- Hyphenation (`hyphens: auto`, `lang` set): at least two characters before the break and three after, no more than three hyphenated lines in a row. Avoid lone words on the last line of a heading (`text-wrap: balance`).
- Truncate only non-critical text such as a file name, username or secondary description; truncate the middle for paths and ids when the ends matter. Offer a way to see it all; a tooltip alone fails on touch.
- Never truncate an amount, an error message or the only instruction on a screen: let it wrap.
