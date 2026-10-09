Beyond swapping colors, these are the typographic changes that matter most for dark mode.

**Body text**
- **Reduce contrast slightly.** Pure white on pure black causes halation and glare, especially over long reading. Use an off-white (roughly #d0d4da to #e6e8eb) on a dark gray (#121417 to #1a1d21) instead of #fff on #000. Aim for about 12:1 to 15:1, not 21:1.
- **Bump the weight a touch or keep it at regular.** Light text on dark appears bolder and bleeds, so avoid thin weights (300 and below). If you use a variable font, drop the weight slightly (for example 400 to 380) rather than raising it.
- **Add a little line-height.** Light-on-dark text reads as denser. Going from 1.6 to 1.65 or 1.7 helps. Slightly looser letter-spacing (about 0.01em) can also help at small sizes.
- **Keep line length to 65–75 characters.** This matters more in dark mode because eye fatigue shows up sooner.
- **Consider a slightly larger size.** Even +0.5 to 1px helps if your body text is 15px or smaller.

**Headings**
- Don't use pure white for headings. Use the same off-white as the body, or one step brighter, and let size and weight carry the hierarchy.
- Avoid heavy weights (700 and above) at large sizes, where they glow. 600 is usually enough.

**Links**
- Don't reuse the light-theme link blue. Saturated, dark blues fail contrast on dark backgrounds. Use lighter, slightly desaturated tints (for example #7ab7ff rather than #0969da). Check that they reach at least 4.5:1 against the background.
- Underlines matter more with many links. Color alone is a weak signal when you lower saturation, so keep underlines in article body text. Use `text-decoration-thickness: 1px` and `text-underline-offset: 0.2em`. Soften the underline color (for example 40% opacity) and bring it to full strength on hover.
- Make visited links distinguishable, but don't use a dark purple. Use a lighter lavender tint with the same contrast requirement.
- Keep the focus ring clearly visible. A 2px outline in a light accent with an offset works well.

**Inline code**
- Use a subtle background one or two steps lighter than the page (for example #23272e on #15181c), with a small border-radius and padding of about 0.15em 0.35em.
- Set the size to about 0.875 to 0.9em so it matches the x-height of the body font and doesn't look oversized.
- Use the text color of the body, or a slightly tinted one. Avoid bright colored text for every inline snippet because it competes with links.
- Inline code inside links should inherit the link color, and keep the underline.
- Disable ligatures if your monospace font has them, and allow wrapping (`overflow-wrap: anywhere`) so long identifiers don't break the layout.

**Code blocks**
- Make the block slightly different from the page background. Either go a shade darker or lighter, plus a 1px border (rgba white at 8 to 12%). Don't rely on the background difference alone.
- Choose a syntax theme designed for dark mode. Don't invert your light theme. Check that comments (the usual offender) still reach about 4.5:1, since many dark themes make them too dim.
- Reduce saturation on the brightest token colors (neon green, pure red, cyan). They vibrate against dark backgrounds.
- Keep line-height around 1.5, font size 13 to 14px, and make sure horizontal scroll is visible, with a styled scrollbar that suits dark mode.
- Make selection, line highlights and diff colors (added and removed) use low-opacity tints instead of solid fills, so the text stays readable.

**Supporting elements**
- Blockquotes, tables and callouts: use borders and subtle background steps instead of shadows, which are nearly invisible on dark surfaces.
- Muted/secondary text (captions, metadata, sidebar items) is where contrast usually fails. Don't go below about 4.5:1 for anything meant to be read.
- Set `color-scheme: dark` so native form controls and scrollbars match, and `-webkit-font-smoothing: antialiased` on macOS, where subpixel rendering makes light-on-dark text look heavier.
- Inline images and diagrams with white backgrounds will glare. Consider a slight brightness reduction (`filter: brightness(.9)`) or provide dark variants.

**Process**
- Define these as design tokens (for example `--text-body`, `--link`, `--code-bg`) so the dark theme is a token swap plus a few overrides, not a separate stylesheet.
- Test on real content: a long article, a page dense with links, and a page mixing code with prose. Check on both OLED and ordinary LCD screens, and at lower brightness, since problems show up differently.
- Verify contrast with a tool, but also read a full article in it. Passing ratios doesn't guarantee comfortable reading.

If you share the stylesheet or the framework (Docusaurus, MkDocs, custom), I can suggest concrete values and overrides.
