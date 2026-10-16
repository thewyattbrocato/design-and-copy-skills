**Recommendation: one open-licensed family for everything, self-hosted, with a system fallback. Use the same family on the web and in print.**

**Assumptions:** The guides are long reading, with small text at 16px or larger on screen and 10–11pt in print. They are in English. Your readers' older Android phones and library PCs may not load web fonts reliably, or may not have good system fonts.

**The pick: Source Sans 3** (SIL Open Font License, so free for web and print)
- It has a true italic, and regular, semibold and bold weights. Headings, body, callouts and "what to do next" boxes can all come from one family by changing weight and size.
- It is sturdy at small sizes and renders cleanly on low-density screens. Its I, l and 1 are distinct, which matters for case numbers, dates and dollar amounts.
- It is a humanist sans, so it reads well at length and still looks plain and trustworthy.
- Use one family so you only maintain one set of files and your print and web versions match.

**If you want a serif for body text,** use **Source Serif 4** (same foundry, same license) for the body and Source Sans 3 for headings, callouts and labels. Both are drawn to work together. Only do this if the printed handouts matter most to you. One family is simpler.

**Making it work on old devices and library computers (the web side):**
```css
@font-face {
  font-family: "Source Sans 3";
  src: url("/fonts/SourceSans3-Variable.woff2") format("woff2");
  font-weight: 200 900;
  font-display: swap;
}
@font-face {
  font-family: "Source Sans 3";
  src: url("/fonts/SourceSans3-Italic-Variable.woff2") format("woff2");
  font-weight: 200 900;
  font-style: italic;
  font-display: swap;
}
body {
  font-family: "Source Sans 3", "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  font-synthesis: none;
}
```
- **Self-host** the files. Don't link to Google Fonts. It's one less outside dependency, library networks sometimes block it, and readers' visits aren't sent to a third party.
- **Subset to Latin** and ship WOFF2 only. That keeps the two files small enough for slow connections. Get the fonts from the official Adobe/Google Fonts repositories.
- **`font-display: swap`** means text shows right away in the fallback and never stays invisible.
- **The fallback is deliberate.** Roboto is on nearly every Android phone and Segoe UI is on Windows. If the font doesn't load, the page still looks clean. Open the page with the font blocked and check this once.
- **Very old Android versions** may not support variable fonts. If you serve those readers, use static WOFF2 files for Regular, Italic, Semibold and Bold instead.

**For print:** Install the same family on the machine you use for layout, and embed the fonts when you export the PDF. Then the handouts match the web pages.

**Avoid:**
- Thin or light weights. They break up on cheap screens and on photocopies.
- Decorative or "friendly" display faces for headings.
- Monospace for anything except case numbers you want aligned.
- Faux bold or italic. This is why the italic file is included.

**Fonts that are also fine:** Noto Sans and Atkinson Hyperlegible are both open and legible. Atkinson Hyperlegible was designed for low-vision readers. I chose Source Sans 3 because it has more weights and its italic is better for long text.

**If your readers include Spanish speakers or other languages,** Source Sans 3 covers Spanish and Vietnamese. For other scripts, such as Arabic or Chinese, tell me. I'd pick Noto for those, and you'd need a partner for each script.

I haven't checked file sizes or the current license text, so download from the official source and confirm the OFL terms before you publish.
