[...]

I'd use one superfamily that was designed across all three scripts, and let one Latin face set every stop name. I'm assuming screen only and that you can bundle or self-host fonts.

[...]

Put the Latin face first in every stack. The Latin font has no Arabic or Japanese glyphs, so those characters fall through to the right script face. A stop name like "Cobalt Quay" then renders in the same Plex Latin whether it sits in an English, Arabic or Japanese sentence.

```css
:root {
  --font-ui: "IBM Plex Sans", "IBM Plex Sans Arabic", "IBM Plex Sans JP",
             system-ui, -apple-system, "Segoe UI", "Geeza Pro",
             "Hiragino Sans", "Yu Gothic", sans-serif;
}
:lang(ar) { line-height: 1.7; }
:lang(ja) { line-height: 1.6; }
:lang(en) { line-height: 1.45; }
body { font-family: var(--font-ui); font-synthesis: none; }
```

[...]

- **Fallback:** Block the web fonts and check what falls back on iOS and Android. Each system stack above should render all three scripts acceptably.

[...]
