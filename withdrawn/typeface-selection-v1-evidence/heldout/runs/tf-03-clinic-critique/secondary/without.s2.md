The main problem is that the page uses six typefaces, and the mix makes it look unplanned. Your CSS sets:

- **Open Sans** (body, sans-serif)
- **Playfair Display** (h1, high-contrast serif)
- **Montserrat** (h2, wide geometric sans)
- **Lora** (h3 and doctor names, serif)
- **Poppins** (buttons and nav, geometric sans)
- **Courier New** (phone numbers, monospace)

Each has a different x-height, letter width, and stroke weight, so headings, nav, body text, and phone numbers look like they came from different designs. Switching between serif and sans-serif on the same page adds to the effect.

Some choices are also hard for older readers:

- **Playfair Display** has very thin hairlines that break up at smaller sizes and on screens.
- **Courier New** is thin and typewriter-like. Phone numbers are the most important thing many of your patients need, and this is the least readable choice for them.
- **Montserrat and Poppins** are wide and have small lowercase letters, so they take more space and read more slowly at small sizes.

I can only see this CSS, so I can't tell you the font sizes, weights, or line heights. I also can't tell whether the Google Fonts `<link>` or `@import` is loaded. If it's missing, the browser falls back to system fonts, which would add more inconsistency.

A simpler version, with one family and larger, more readable text:

```css
body {
  font-family: 'Open Sans', Arial, sans-serif;
  font-size: 18px;
  line-height: 1.6;
  color: #1a1a1a;
}

h1, h2, h3, .doctor-name, .btn, nav a {
  font-family: 'Open Sans', Arial, sans-serif;
  font-weight: 700;
  color: #1a1a1a;
}

h1 { font-size: 2.2rem; }
h2 { font-size: 1.7rem; }
h3, .doctor-name { font-size: 1.3rem; }

.phone-number {
  font-family: 'Open Sans', Arial, sans-serif;
  font-size: 1.25rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
}
```

Why these choices:

- **One family** removes the mismatch. Open Sans is already your body font and has large, clear letterforms.
- **18px body text and 1.6 line height** are easier to read for older patients than the usual 16px.
- **Bold, same-family headings** keep the hierarchy clear without needing a serif.
- **`tabular-nums` and `nowrap`** keep phone numbers evenly spaced and stop them from breaking across lines.

If you want to keep a serif for branding, use it only for the h1 logo-style title, and keep everything else in Open Sans.

It would also help to check the patient-facing pages on a phone and on an older desktop browser, since small text is often the first thing that looks messy. If you send the full stylesheet, including font sizes, weights, and the font `<link>`, I can point out the specific rules causing the rest of the mess.
