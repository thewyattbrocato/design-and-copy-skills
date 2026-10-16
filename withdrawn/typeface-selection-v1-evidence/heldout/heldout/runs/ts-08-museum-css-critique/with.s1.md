Honest answer: no, the fonts aren't okay for this audience. The playful mood is a good fit for a children's museum, but the way it's applied will hurt the people who use the site.

**What works**
- A bold, fun display face for the main heading suits a kids' museum. Bangers on `h1` is loud, but it's the one place that voice belongs.

**What fails, and the fix**

1. **Body text is too thin and too small.** Josefin Sans at weight 100 is a hairline, and 13px makes it worse. On a phone, in daylight, it will look faint and blurry. This is the text parents read for prices and policies.
   - Fix: use weight 400 and at least 16px.

2. **Opening hours are the worst-treated text on the page.** They're set in Pacifico, a connected script face, at 11px. Script faces get hard to read when small, and hours are what parents came for.
   - Fix: use the plain body font, around 18px, in semibold.

3. **Too many display fonts.** Bangers, Pacifico and Lobster are three loud faces competing, and none of them is a calm partner for the others. Pacifico and Lobster are also similar enough to look like a mistake.
   - Fix: keep one display face, and use a plain sturdy one for everything else.

4. **No fallbacks.** `font-family: 'Josefin Sans'` has nothing after it. If the Google font fails to load, the browser falls back to a default serif.
   - Fix: add real fallbacks, such as `system-ui, sans-serif`.

5. **Loading cost.** Four families from Google Fonts slow the first load on mobile. Cutting to two families fixes most of this.

**A simple version**

```css
@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&family=Nunito+Sans:wght@400;700&display=swap');

body { font-family: 'Nunito Sans', system-ui, sans-serif; font-weight: 400; font-size: 16px; }
h1, h2, .tagline { font-family: 'Fredoka', 'Nunito Sans', system-ui, sans-serif; font-weight: 600; }
.opening-hours { font-family: 'Nunito Sans', system-ui, sans-serif; font-weight: 700; font-size: 18px; }
```

This keeps a friendly, rounded personality in the headings and tagline. Everything parents need to read is in a plain, sturdy sans.

If your friend wants to keep Bangers for the `h1` as a brand moment, that's fine. I'd still drop Pacifico and Lobster and use the plain sans for everything else.

I haven't checked these fonts' licenses or how they render on real devices. Both are on Google Fonts, but have your friend test on an actual phone.
