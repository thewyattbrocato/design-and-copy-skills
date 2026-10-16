This stylesheet is already well set, so I changed nothing.

- **Body:** 17px with 1.55 leading and a 38rem column gives about 65 to 70 characters a line.
- **Headings:** The h1 uses a `clamp()` with tight 1.1 leading and slight negative tracking, which suits display size. The h2 has 2rem above and 0.5rem below, so it clearly belongs to the text that follows it.
- **Scale:** There are five sizes, each with its own job.
- **Labels:** `.label` is 12px, uppercase and tracked at 0.08em, as it should be.
- **Times:** `.time` uses tabular figures, so appointment times will line up in a column.
- **Fine print:** `.fineprint` is small but not below the floor, and its gray is still readable.

If you want one optional tweak, add `h1, h2 { text-wrap: balance; } p { text-wrap: pretty; }`. It avoids a one-word last line on headings and paragraphs, and it has no effect on browsers that don't support it.

I also left `font: 17px` on `body` as it is. Switching it to `1.0625rem` would make the page follow a visitor's browser text-size setting, which could matter for a dental practice's patients. That's a one-line change if you want it.
