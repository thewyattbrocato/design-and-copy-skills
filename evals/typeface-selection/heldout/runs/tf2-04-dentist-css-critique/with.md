The site feels chaotic because it has five typefaces with no clear job each, and several of them are set in ways people can't comfortably read. The slowness comes mostly from how the fonts are loaded.

**What works**
- Playfair Display at 900 for the h1 is a legitimate display choice. It's big and short, which is what that kind of face is for. It's a formal voice for a kids' practice, though, so it's a judgment call.

**What's wrong**
1. **Body text is in Lobster at 13px with 1.2 line-height.** This is the biggest problem. Lobster is a bold script meant for a logo or a short headline. Paragraphs of it, small and tightly packed, are tiring to read, and the grey `#666` makes it worse. Parents are probably reading hours, insurance and appointment info in this face.
2. **Hairline weights.** The h2s use Montserrat 100 in uppercase with 4px tracking, and the nav uses Raleway 200 at 12px. Strokes that thin turn faint or vanish on ordinary and low-density screens. The nav is the most important text on the site and the hardest to see.
3. **Five families, no system.** Lobster, Playfair, Montserrat, Raleway and Comic Neue, plus Courier New, are each used once. Montserrat and Raleway are near-identical geometric sans faces, so pairing them looks like a mistake rather than a choice. Comic Neue on buttons and Courier New on prices and hours add two more unrelated voices.
4. **Courier New for prices and hours.** Monospace is for code and aligned columns. Here it looks like a typewriter dropped into a children's site, and Courier is thin as well. If you want aligned numbers, use `font-variant-numeric: tabular-nums`.
5. **No real fallbacks.** `'Montserrat'`, `'Raleway'` and `'Courier New'` have no generic family after them. Lobster falls back to `cursive`, which on many devices is Comic Sans or something worse.

**Why it's slow**
- `@import` inside CSS is a chain. The browser downloads the stylesheet, then discovers the import, then fetches Google's CSS, then fetches the font files. Nothing can start earlier.
- You're requesting about 15 weights and styles but using about 5. Playfair 400 and 700, Montserrat 200 to 700 (you use only 100), and Raleway 100 and 300 are all dead weight.
- `display=block` hides text for up to about 3 seconds while fonts load. Because the body is Lobster, the whole page can stay blank on a slow connection.

**Fix: one friendly family, one job per weight**

I'm assuming a Latin-script audience and web fonts that can load. Nunito is a rounded sans with an open license, a full weight range and a true italic. Its soft terminals suit a kids' practice without using a gimmick face for body text.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,400;0,600;0,800;1,400&display=swap">
```

```css
body {
  font-family: 'Nunito', system-ui, -apple-system, 'Segoe UI', sans-serif;
  font-size: 17px;
  line-height: 1.6;
  color: #333;
}
h1 { font-weight: 800; font-size: clamp(32px, 5vw, 44px); line-height: 1.15; }
h2 { font-weight: 800; font-size: 28px; line-height: 1.2; }  /* no uppercase, no tracking */
nav a { font-weight: 600; font-size: 16px; }
.price, .hours { font-variant-numeric: tabular-nums; }
.btn { font-weight: 800; }
```

This replaces six families with one and about 15 font files with 4. Text shows immediately in a system font and swaps when Nunito arrives. You can still use the hierarchy and a bit of personality, but it comes from weight and size rather than from switching typefaces.

If the practice wants to keep Playfair for the h1, that's fine as a single display accent over Nunito. Drop everything else.

Before launch, check Nunito's license terms and the fallback rendering yourself. I haven't verified either. Test the page once with fonts blocked to confirm the fallback looks acceptable.
