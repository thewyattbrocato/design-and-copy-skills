I haven't tested this in a browser. Here's a revised stylesheet. It keeps your structure and class names, so it's a drop-in replacement.

[...]

**What changed**
- **Typeface:** Georgia is the main reason the page reads as default. The new stack uses Charter or Iowan Old Style, which ship with macOS, iOS and Android, and falls back to Georgia. For a distinctive look, a webfont such as Source Serif, Newsreader or Fraunces would help more than anything else here.
- **Headlines:** They're larger, with tighter line height and slight negative tracking. `text-wrap: balance` keeps titles from leaving a stray word on the second line.
- **Body text:** It's slightly larger with more leading. Kerning, ligatures, old-style numerals, hyphenation and `text-wrap: pretty` give it a book-like texture.
- **Colour:** One restrained accent (`#8a3b2a`) is used for the kicker, drop cap, links, quote rule and section break. Everything else is warm neutrals. Swap in your brand colour.
[...]
- **Added elements:** `.dek`, `figcaption`, `hr` and `blockquote cite` styles. They only apply if your markup uses them, so ignore any you don't need.
[...]
