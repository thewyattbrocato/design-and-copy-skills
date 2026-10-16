It's sound, and I'd ship it with a few small additions. Using system fonts means there's no webfont loading, so no flash of unstyled text and no layout shift.

**Worth changing**
- **Headings:** `h4, h5, h6` aren't covered, so they'll render in the serif body font. Use `h1, h2, h3, h4, h5, h6` if you might ever use them, even in a CMS or markdown output.
- **Reading settings:** The snippet sets no size, line-height, or measure, and those matter more than the font choice for long-form text. Something like this is a reasonable start:
  ```css
  body { font-size: 1.125rem; line-height: 1.6; }
  article { max-width: 65ch; }
  ```
  Charter and Cambria both read well at about 18px.
- **Tide table:** `tabular-nums` is the right call for aligned times and heights. Also give the table cells a slightly smaller size, and `text-align: right` on numeric columns, so the digits line up.

**Optional**
- **Serif fallbacks:** Charter ships with macOS and iOS, and Sitka and Cambria cover Windows. Android and most Linux fall through to generic `serif`, which is usually Noto Serif or DejaVu Serif and is wider. If you want those platforms to look closer to the rest, add `Georgia` before `serif`. Otherwise the stack is fine.
- **Line breaks:** `hyphens: auto` on the article, with `<html lang="en">` set, helps on narrow phone screens.

The `system-ui` stack is fine as written, and its numerals support `tnum` on all the major platforms.
