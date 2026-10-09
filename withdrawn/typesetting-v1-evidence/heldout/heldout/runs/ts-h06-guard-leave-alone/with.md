The type is mostly sound, so I'd change only two things.

**What holds up:**
- **Size and measure:** 18px Charter at a 38rem column gives about 65 characters per line.
- **Leading:** 1.6 for body and 1.15 to 1.25 for headings.
- **Sizes:** five, each with a clear role.
- **Spacing:** `h2` has more space above than below.
- **Table:** tabular figures with right-aligned number columns.
- **Contrast:** the byline gray is fine.

**What I'd change:**
1. **`th` alignment:** browsers center `th` by default. Any non-numeric header, such as a "Fund" or "Category" column, will float over left-aligned cells. Set `th` to left, and `.num` still overrides it to right.
2. **Table margin:** the table has no margin, so it butts against the paragraph before and after it. Give it the same breathing room as the blockquote.
3. **Optional (one line):** `text-wrap: balance` on `h1` and `h2`, so a two-line headline doesn't leave a one-word last line.

Revised lines (everything else stays as you wrote it):

```css
article h1 { font-size: 2.25rem; line-height: 1.15; margin: 0 0 0.5rem; text-wrap: balance; }
article h2 { font-size: 1.5rem; line-height: 1.25; margin: 2.5rem 0 0.75rem; text-wrap: balance; }
article table { width: 100%; margin: 1.5rem 0; border-collapse: collapse; font: 0.9375rem/1.4 system-ui, sans-serif; font-variant-numeric: tabular-nums; }
article th, article td { padding: 0.5rem 0.75rem; border-bottom: 1px solid #e3e0d8; text-align: left; }
article td.num, article th.num { text-align: right; }
```

Two things I couldn't check from the CSS alone:
- **Table on phones:** a wide table can overflow a narrow screen. If any table has more than three or four columns, wrap it in a container with `overflow-x: auto`.
- **Final copy:** check that it uses curly quotes and en dashes for ranges, such as "2019–2024".
