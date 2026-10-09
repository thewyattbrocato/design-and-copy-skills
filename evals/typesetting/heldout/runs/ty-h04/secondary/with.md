Your text setup is mostly sound. The body size, line length, leading and heading spacing already work, so I left them alone. The plain look comes from the headings and the pull quote, so I changed those.

```css
.essay {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 1.125rem;
  line-height: 1.65;
  max-width: 36rem;
  margin: 0 auto;
  padding: 0 1.25rem;
  color: #222;
  font-synthesis: none;
}
.essay h1 {
  font-size: clamp(2rem, 5vw, 2.75rem);
  font-weight: 400;
  line-height: 1.15;
  letter-spacing: -0.015em;
  text-wrap: balance;
  margin: 0 0 0.5em;
}
.essay h2 {
  font-size: 1.5rem;
  line-height: 1.25;
  letter-spacing: -0.005em;
  text-wrap: balance;
  margin: 2.2em 0 0.6em;
}
.essay p { margin: 0 0 1em; text-wrap: pretty; }
.essay .kicker {
  font: 600 0.75rem/1 system-ui, sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 1rem;
}
.essay blockquote {
  margin: 1.5em 0;
  padding-left: 1.25rem;
  border-left: 3px solid #bbb;
  font-style: normal;
}
.essay .stat { font-variant-numeric: tabular-nums; }
```

- **h1 weight 400 with tighter tracking:** Display serifs at regular weight with slightly tight spacing read as magazine headlines. This is the biggest visual change. If it's too light, go back to `font-weight: 700`.
- **Blockquote upright instead of italic:** A quote gets one device, and the rule plus indent already sets it off. Restore `font-style: italic` if you want the italic back, and then drop the border.
- **`font-synthesis: none` and `text-wrap`:** These stop the browser from faking bold or italic and keep headlines from leaving one word alone on a line. They don't change how the page looks otherwise.

For a further editorial touch, add a lede paragraph (`.essay .lede { font-size: 1.25rem; }`) for the opening paragraph. Nothing is in a column here, so `.stat` only needs right-alignment if you put figures in a table.
