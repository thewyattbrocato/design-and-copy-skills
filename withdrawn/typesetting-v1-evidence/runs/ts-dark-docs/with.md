Keep the sizes and measure the same as in light mode. Change only the things that light-on-dark makes look different. Adjust by eye, comparing the same page in both themes at the same zoom.

**Body text**
- **Color:** Use off-white on a soft dark gray, not pure white on black. This cuts glare and the glowing look. Check contrast against your accessibility floor.
- **Weight:** Light text looks heavier on dark. If long articles look swollen, drop body weight one step (for example 400 to 350, or use a lighter grade if the font has one). If strokes start to break up, raise it again.
- **Tracking:** Open small text slightly, about +0.01 to 0.02em. Large headings don't need it.
- **Line height:** Add about 0.05 to the ~1.5 you use now if long paragraphs still feel dense after the weight change.
- **Size and measure:** Don't enlarge the text or narrow the column. Keep the ~65ch cap on text elements.

**Links**
- Links are the most likely thing to break in dark mode. The usual blue is too dim on dark, and a saturated one vibrates.
- Pick a lighter, slightly desaturated link color, and keep links distinct from body text by more than hue.
- Keep underlines in long articles, and consider `text-underline-offset` and a slightly thicker `text-decoration-thickness`. Thin underlines tend to disappear on dark.
- Give visited links a visible but not murky state. Check that the hover and focus states are still obvious.

**Inline code and code blocks**
- Keep code monospace and unwrapped, and don't apply the prose rules to it.
- Retune the syntax colors for dark. Palettes made for white often glare, and some hues (dark blues and reds) lose contrast.
- Give code a background one step lighter or darker than the page, not a hard-edged box. Inline code needs a subtle tint and some padding so it sits clearly in the line.
- Make inline code a touch smaller than the surrounding text (about 0.9em) so it doesn't look heavier. Use the same weight reduction as body text if it looks bold.
- Keep line height in code blocks close to prose. Don't add extra tracking there.

**Secondary text and small text**
- Dim metadata, captions and sidebar text by value, but check them on the dark ground specifically. Placeholder and "muted" grays are where contrast most often fails.
- Keep functional text at body size. Use about 12px only for captions and metadata, at regular or medium weight, with slightly open spacing.

**Headings**
- Headings often look too bold on dark. Drop their weight a step too, and keep the spacing above about twice the spacing below.
- Use value, not saturated color, to separate heading levels.

**Implementation tips**
- Put the changes behind theme tokens or custom properties (for example `--text-weight`, `--text-tracking`, `--link-color`), so the dark theme overrides only those and the sizes and scale stay shared.
- Set `color-scheme: dark` so the browser adjusts scrollbars and form controls.
- Check on a real low-density screen. Anti-aliasing changes the apparent weight, and it affects dark themes more.
- Zoom to 200% and shrink the window to confirm the text still reflows.

If you share the CSS, I can suggest the exact token values.
