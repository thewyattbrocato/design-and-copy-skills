This is sound, so I'd ship it. The serif for long reading and the sans for headings, table and meta line have clearly separate jobs. Every stack ends in a real fallback, and nothing depends on a web font loading. `tabular-nums` on the tide table is the right call, because the digits will line up in columns. Charter, Sitka and Cambria all have true bold and italic, so you won't get faux styles in the articles.

If I changed one thing, it would be this:

```css
button, input, select, textarea { font: inherit; }
```

Form controls don't inherit `font-family` by default. A newsletter site almost certainly has a signup field, and without this it will render in the browser's default UI font instead of your stack.

Two small things to check:
- `h4` through `h6` aren't in your heading rule, so they'll render in the serif. That's fine if you never use them. Otherwise, add them to the rule.
- On Android, none of the named serifs exist, so body text falls to the generic `serif` (usually Noto Serif). It reads fine, but check it once on a phone.
