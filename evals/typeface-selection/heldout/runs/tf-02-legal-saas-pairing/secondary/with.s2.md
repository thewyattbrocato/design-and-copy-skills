**Recommendation: Georgia headings over the system UI sans for body and interface.**

Headings get a serif for gravitas. Body and UI get the system sans, which is what Mac, Windows and phones already draw best. The two faces differ plainly in category, and each has a fixed role.

```css
--font-heading: Georgia, Cambria, "Noto Serif", ui-serif, serif;
--font-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

- **Georgia (headings):** Ships on Mac and Windows, and it has a true italic. It reads as established without looking like a legal template.
- **Cambria, Noto Serif, ui-serif:** Fallbacks for Office-heavy Windows machines and for Android, where Georgia may be missing.
- **System UI sans (body, labels, buttons):** SF on Apple, Segoe UI on Windows, Roboto on Android. Every platform gets a sturdy grotesque with a full weight range.
- **Numbers:** Set `font-variant-numeric: tabular-nums` on invoice totals, balances and hours so columns align.

Things to know before you ship it:

- **Georgia has only regular and bold.** Don't map a semibold or medium token to it. Build hierarchy with size and bold, and use the sans for anything that needs more weight steps.
- **Set `font-synthesis: none`** so no faux styles appear where a face lacks them.
- **Use the serif for headings only.** Table headers, labels and form text stay in the sans.
- **Verify on real devices.** I can't render these stacks here, so check one page on a Mac, a Windows machine and an Android phone. The fallback differences are the main risk.

For the marketing site, the same pair works at large display sizes, with the serif set big and short. A more distinctive display face would need the licensing review to clear first.
