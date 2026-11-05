This stylesheet is already well set, so I changed nothing.

- **Body:** 17px with 1.55 leading, and a `38rem` column that gives roughly 60 to 70 characters per line.
- **Headings:** The `h1` has tightened tracking and 1.1 leading, and it scales with `clamp()`. The `h2` has 2rem of space above and 0.5rem below, so the space above is well over double.
- **Small text:** `.label` is 12px, uppercase and tracked at 0.08em. `.fineprint` is 13px with 1.45 leading. The `#5a6470` gray has enough contrast on white for both.
- **Figures:** `.time` uses tabular numerals, so appointment times will line up.

One optional tweak is to add `text-wrap: balance` to `h1, h2` and `text-wrap: pretty` to `p`. That avoids a single-word last line when the headline wraps on phones. The page reads fine without it.
