**I'd use Georgia for headings and the system UI sans for body text.**

```css
:root {
  --font-heading: Georgia, "Times New Roman", "Noto Serif", serif;
  --font-body: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}
```

**Why this pairing**
- **Availability:** Georgia ships with macOS, Windows and iOS. Android doesn't include it, so those users fall back to Noto Serif, which looks fine in the same role.
- **Tone:** A serif heading gives you the "established, trustworthy" feel that suits law firms. A plain sans body keeps the product feeling modern and uncluttered, and it avoids the "stuffy legal software" look.
- **Body text:** `system-ui` resolves to San Francisco on Apple devices, Segoe UI on Windows and Roboto on Android. It's crisp on every platform and costs nothing to load. If your product UI already uses the default sans, this keeps the app and marketing site consistent.

**Billing figures**
- Georgia uses old-style (lowercase-height) numerals by default, so 1, 3, 4, 5, 7 and 9 sit above or below the baseline. That looks elegant in a headline but poor for invoice amounts, and it makes columns hard to scan.
- Use Georgia only for marketing headings and page titles. Keep the sans for anything numeric, with `font-variant-numeric: tabular-nums` so digits line up in tables and invoices.
- If a marketing headline has a number in it, like "Bill 6 minutes faster", Georgia's old-style numerals will look a bit quirky. You can live with that or write the number out as a word.

**Scope**
- In the product UI, I'd keep the sans everywhere, or use the serif only for page titles if you want a little brand carryover. A serif on dense billing screens works against you.
- Marketing site: serif for h1/h2, sans for everything else. Use a slightly tighter `letter-spacing` (around `-0.01em`) and `font-weight: 600–700` on the headings. Georgia's bold is sturdy enough to carry a hero.

**Alternative:** If you'd rather have a more contemporary look than Georgia, use the sans for everything and add contrast through weight and size. That's less distinctive, but it's the safest option for a product that's mostly numbers.

Once legal clears web fonts, the variables above make it a one-line swap. A good next step would be something like Source Serif or Fraunces for headings and Inter for body.
