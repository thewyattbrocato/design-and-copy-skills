I'd use a serif for headings and the system UI sans for body. Serif headings suit a law-firm audience, since they read as established and trustworthy. They also separate the marketing site from the product, which is all one sans right now.

```css
--font-heading: "Iowan Old Style", Charter, "Palatino Linotype", Palatino, Georgia, serif;
--font-body: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--font-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
```

- **Headings (marketing site):** use the serif at 600 or bold, large and short. Headlines, section titles and pull quotes all work. Don't use it for small text.
- **Body, nav, buttons, forms:** use the system sans at 400, 500 and 600. It's sturdy at small sizes, and `system-ui` resolves to the native UI font on Mac, Windows, iOS and Android.
- **Product UI:** keep the sans throughout. At most, use the serif for page titles like "Invoices", if you want the brand to carry through. Set `font-variant-numeric: tabular-nums` on amounts, hours and tables so the columns line up.
- **Mono:** only for invoice numbers or matter IDs, if you need alignment there.

Also set `font-synthesis: none` so no browser fakes a weight.

**Rendering differs by platform.**
- **Mac and iPhone:** Iowan Old Style, which has a refined, bookish look.
- **Windows:** Palatino Linotype, or Georgia if that's missing.
- **Android:** neither Charter, Palatino nor Georgia is a standard Android font as far as I know, so it will probably use the generic serif, likely Noto Serif. That's acceptable, but check a real Android device before launch.

**Georgia numerals:** Georgia has old-style numerals, where some digits drop below the baseline. That's fine in a headline like "Bill in 6 minutes". Keep prices, dollar amounts and any screenshot-like numerals in the sans.

**Web fonts later:** when legal clears licenses, you only need to put a loaded face at the front of `--font-heading`. The rest of the stack stays as the fallback. I haven't checked any specific font's license terms, so that review is still legal's call.

I'm assuming this is Latin-script English only and that the marketing site and the product share one stylesheet. If the site needs other scripts, tell me, because that changes the stack.
