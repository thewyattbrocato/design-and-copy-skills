I'd pair a serif for headings with the system UI sans for body text.

**Headings (marketing site, and large titles in the app):**
```css
font-family: Georgia, "Iowan Old Style", "Noto Serif", "Times New Roman", serif;
```

**Body and product UI:**
```css
font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

**Why this pairing**
- **Tone:** A serif heading reads as established and trustworthy, which suits law firms and money. The plain sans body keeps the product UI clean and fast to scan. That contrast is the main thing the marketing site is missing.
- **Coverage:** Georgia ships on Mac, Windows and iOS. Android doesn't have it, so it falls back to Noto Serif, which is a reasonable match. `system-ui` resolves to San Francisco on Apple devices, Segoe UI on Windows and Roboto on Android. Each platform gets a native-feeling body font, with no license questions because nothing is being loaded.
- **Legal:** Nothing is bundled or downloaded, so there's nothing for legal to review.

**Caveats**
- **Georgia's numerals:** Georgia uses old-style figures, where digits like 3, 4, 5, 7 and 9 dip below the baseline. That looks nice in prose but bad for billing amounts, so don't use it for invoices, tables or rates. Keep numbers in the sans with `font-variant-numeric: tabular-nums` so columns line up.
- **Where to use the serif:** I'd use it on the marketing site and for page titles in the app. I'd keep buttons, tables, forms and nav in the sans.
- **Rendering:** Rendering varies by platform. Georgia is slightly larger than the sans at the same `font-size`, so check heading sizes on Windows and Android as well as Mac.

**Alternative:** For a more refined look, use `Charter, "Iowan Old Style", "Sitka Text", Cambria, Georgia, serif`. It's nicer on Apple devices but resolves to different fonts on each platform, so the brand would look less consistent. I'd start with Georgia for that reason.

If you tell me where the styles live, I can wire this in as CSS variables.
