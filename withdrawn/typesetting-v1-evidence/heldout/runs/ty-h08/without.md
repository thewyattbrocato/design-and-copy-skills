The designer is right, and it's cheap. It's probably also less than you're imagining.

The setting is almost certainly tabular figures (`font-variant-numeric: tabular-nums`), not a different typeface. By default most fonts use proportional digits, so a "1" is narrower than an "8". In a table column, that causes three problems:

- **Prices:** decimal points don't line up, so you can't scan down a column and compare magnitudes.
- **ETAs and counts:** values that update live make the column jitter as the digits change width.
- **Right-aligned numbers:** the digits don't stack, so ones, tens and hundreds don't sit in the same positions.

Pair it with right-alignment, and use the same decimal places within a column for prices.

It's one CSS rule, applied to numeric cells, not to headings:

```css
td.numeric, .numeric {
  font-variant-numeric: tabular-nums;
  text-align: right;
}
```

Two caveats where you'd be right to push back:

- **A different font family for numbers:** if the designer means that, it's overkill. Tabular figures within the same family give you the benefit without a second font to load or maintain.
- **Font support:** a few fonts don't ship tabular figures. Check that yours does. Inter, Roboto, SF and most modern UI fonts do.

Headings are fine as proportional text. If a heading contains a number, such as "12 active orders", it doesn't need the setting.

If you point me at the dashboard code, I can add the rule.
