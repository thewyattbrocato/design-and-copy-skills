The setup is sound, and I'd ship it with a few small tweaks. It uses no webfonts, so there's no load cost or layout shift. Charter/Sitka/Cambria is a good long-form stack, and using tabular figures on the tide table is the right call.

**Worth changing**
- **h4–h6 aren't covered.** Only h1–h3 get the sans. If you ever use a deeper heading, it falls back to the serif at its default weight and looks inconsistent. Use `h1, h2, h3, h4, h5, h6`, or just `h1…h6`.
- **Add `Georgia` before the generic `serif`.** It covers older Windows and some Linux and Android setups that lack the other fonts. Without it, they get the browser's default serif, which is often Times-like and noticeably worse for long reading.
- **Add `BlinkMacSystemFont` after `-apple-system`.** Older Chrome on macOS needs it. This is minor.

**Not in the snippet, but check them before shipping**
- **Body line-height and measure.** Long-form text wants roughly `line-height: 1.5–1.65` and a column of about `65ch`.
- **Font size.** Make sure the body is at least 17–18px. Charter and Cambria look small at 16px.
- **Tide table on mobile.** Check that it doesn't overflow. Wrap it in `overflow-x: auto` if it can.

**Optional**
- Some fallbacks (Cambria, Sitka) have different x-heights from Charter, so the look shifts a bit across platforms. That's normal for system stacks and fine for a small newsletter.
- If tide numbers ever appear inline in prose, such as "high at 6:42", they'll use the serif's default figures. That's usually fine, but check how they look in Sitka.

Here's the tweaked version:

```css
:root {
  --serif: Charter, 'Bitstream Charter', 'Sitka Text', Cambria, Georgia, serif;
  --sans: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}
body { font-family: var(--serif); }
h1, h2, h3, h4, h5, h6 { font-family: var(--sans); font-weight: 700; }
.tide-table, .meta { font-family: var(--sans); font-variant-numeric: tabular-nums; }
```
