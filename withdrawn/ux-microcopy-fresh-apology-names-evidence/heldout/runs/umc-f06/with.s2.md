Here's the alt text for each image, in page order:

1. **Logo (links to home):** `alt="Harbour Lane Community Pool – home"`
   Since the logo is a link, the alt text should describe where it goes, not the picture. Don't write "logo" or "blue wave". The name plus "home" tells screen reader users what the link does.

2. **Lifeguard photo:** `alt="A lifeguard sits on the high chair, watching over an empty lap pool."`
   This is informative content, so a short description of what's shown works. Add details only if the surrounding text doesn't already cover the photo's purpose.

3. **Bar chart:** `alt="Bar chart of weekly visits over the last six months."`
   The text just below already gives the key finding (peak in July, lowest in January), so the alt text doesn't need to repeat it. It only needs to identify what the image is. If the chart has other important details that the summary leaves out, put them in the surrounding text, not in a long alt attribute.

4. **Decorative wave pattern:** `alt=""`
   This should have an empty alt attribute, not a missing one. An empty alt tells screen readers to skip it. If it's a CSS background image, that's even better, because it needs no alt at all.

5. **Heart donation button:** `alt="Donate"`, or better, give the button an accessible name
   The button's function is what matters, not the icon. If it's an `<img>` inside a `<button>`, use `alt="Donate"`. If the heart is an inline SVG or icon font, mark the icon `aria-hidden="true"` and put `aria-label="Donate"` on the button. Don't use "heart" or "round button". Because it's a round, icon-only button, make sure it also has a visible focus style, and consider a tooltip so sighted users know what it does.
