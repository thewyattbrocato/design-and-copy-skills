**Recommendation:** Georgia for headings and the system UI sans for body text. Georgia is the most reliably installed serif across your targets, and the system sans gives the product UI native rendering on each platform.

```css
:root {
  --font-heading: Georgia, Cambria, "Times New Roman", serif;
  --font-body: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
               "Helvetica Neue", Arial, sans-serif;
}

h1, h2, h3 { font-family: var(--font-heading); }
body       { font-family: var(--font-body); }

/* Billing amounts and tables need aligned digits */
.amount, td.numeric { font-variant-numeric: tabular-nums; }
```

**Why this pairing:**

- **Georgia** ships on macOS, iOS, and Windows. It was designed for screen legibility and reads as established and trustworthy, which suits a law-firm audience. On Android, where it's usually missing, the stack falls back to the generic serif (Noto Serif), which is a reasonable match.
- **The system sans** resolves to San Francisco on Apple devices, Segoe UI on Windows, and Roboto on Android. Users get the font their OS already uses for dense UI, so the product stays easy to scan.
- **Licensing:** referencing installed system fonts by name doesn't ship font files, so this should sidestep the license review. Legal should still confirm that reading.

**Tradeoffs and things to check:**

- **No single font matches everywhere.** Body text will look slightly different on each platform. That's the cost of not loading web fonts, and it's usually acceptable for system UI.
- **Fonts with more character, like Avenir Next, Gill Sans, or Palatino, aren't on every platform.** Avenir is Apple-only, and Gill Sans and Palatino are missing or inconsistent on Android or Windows without Office. Their fallbacks would look noticeably different from the intended design.
- **Test the billing views on a Windows machine and an Android phone, not just a Mac.** Segoe and Roboto are wider than SF at the same size, so check table columns, invoice totals, and any fixed-width labels for overflow.
- **I haven't rendered these stacks on real devices.** The font availability above is from my knowledge of the default installs, so spot-check on each target before committing.
