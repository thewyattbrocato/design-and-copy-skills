I'd use **Georgia for headings and the system UI sans for body text.**

**Heading (serif):** `Georgia, "Palatino Linotype", Palatino, serif`

Georgia ships on Mac, Windows, and iOS, so it covers most of your users. It's sturdy and a little formal, which suits a law-firm brand without looking dated. Palatino Linotype and Palatino are fallbacks for some Windows and Mac setups. Android doesn't reliably have Georgia, so it falls through to the generic `serif`, which usually resolves to Noto Serif. That's acceptable.

**Body (sans):** `system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`

This uses each platform's native UI font: SF on Apple devices, Segoe UI on Windows, Roboto on Android. Product UI text will feel native everywhere, and the sans reads well at small sizes in dense tables. Don't name "SF Pro" directly in CSS. Use `-apple-system` or `system-ui` instead.

**Things to handle:**

- **Georgia's numerals are old-style** (descenders on 3, 4, 5, 7, 9), which makes invoice amounts hard to scan. Keep dollar figures and tables in the sans with `font-variant-numeric: tabular-nums`. Use Georgia for headings and prose only.
- **Metrics differ across platforms.** The same text is wider on Windows than on Mac. Leave slack in buttons and table columns, and check invoices and dashboards on a Windows machine and an Android phone before shipping.
- **Mixing product and marketing:** Use the same stacks in both so the brand carries from the marketing site into the app. Marketing can get more generous heading sizes and line heights.
- **Licensing:** Referencing these fonts by name in CSS is fine. Don't download or self-host the font files, since the OS vendors' EULAs cover those. Legal may want to confirm that reading, but it's the standard approach for system fonts.

If you want more personality later, Charter (on Mac and iOS only) or Palatino are the next steps up, but they're weaker on Windows and Android, so I'd start with the pairing above.
