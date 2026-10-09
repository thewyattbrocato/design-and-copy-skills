# Stacks, loading and scripts

Load when fonts cannot load, or when shipping web fonts, variable fonts or several scripts.

## System stacks by role

Order: the face you want first, then close system matches, then a generic family. Name only fonts that will be loaded or are on the target platform.

```css
--font-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--font-reading: "Iowan Old Style", Charter, "Palatino Linotype", Palatino, Georgia, serif;
--font-humanist: "Avenir Next", Avenir, "Segoe UI", Optima, Candara, sans-serif;
--font-display-serif: "Iowan Old Style", Palatino, Georgia, serif; /* big and short only */
--font-mono: ui-monospace, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
--font-rounded: ui-rounded, "SF Pro Rounded", "Hiragino Maru Gothic ProN", Quicksand, sans-serif;
```

- Each platform renders the first match it has, so the same stack looks different on each: a reading page becomes Charter or Iowan on Apple, Georgia elsewhere. Check one fallback per platform you care about.
- A named web font with no loading code (`font-family: 'Name', sans-serif` and no `@font-face`) renders as the generic family. Either load it properly or remove the name.
- A bare `serif` or `sans-serif` is a generic family, not a choice; the browser picks.
- `font-synthesis: none` stops faked bold, italic and small caps.

## Loading web fonts

1. Self-host and subset to the scripts and glyphs used; WOFF2 only.
2. Two to four files in all. A variable file replaces several static weights.
3. `font-display: swap` for body text (or `optional` when a late swap would shift layout badly); never block text invisibly.
4. Preload the one or two critical files with `crossorigin`.
5. Tune the fallback to the web font's metrics (`size-adjust`, `ascent-override`, `descent-override`, `line-gap-override` on a local fallback `@font-face`) so the swap does not shift the layout.
6. Test throttled, with the font blocked, and with the cache empty.

## Variable fonts

- Map named instances to weight tokens; avoid raw axis values at call sites.
- Optical size: `font-optical-sizing: auto` lets small text get sturdier drawings and large text finer ones.
- Grade, where offered, adjusts apparent weight without reflow; use a lower grade on dark grounds.
- Check the file really contains the axes you set; a static fallback may silently drop them.

## Licensing

- Open licenses (embedding and web use allowed) are the safe default when rights are unclear.
- Commercial faces: confirm desktop, web, app and embedding rights separately, and the traffic or seat limits. Never use font files copied from another source.
- Do not state a license as fact unless the user gave it. Say what to check.

## Scripts and languages

- Start from the script with the least choice (Arabic, Hebrew, Devanagari, Thai, CJK), then find a Latin partner designed or matched to it, or a single family that covers both.
- Vietnamese needs stacked diacritics: check coverage and leave extra line height. Greek and Cyrillic need real glyphs, not look-alike Latin substitutes.
- Match apparent size: Arabic and CJK often need a different size and line height than Latin to look equal.
- Do not use italics where the script has no italic tradition; use weight or color for emphasis instead.
- Use `lang` on the element so the browser picks the right glyph variants and fallbacks.
- Do not set a living language with a symbol or icon font; if a glyph is missing, change the font.
