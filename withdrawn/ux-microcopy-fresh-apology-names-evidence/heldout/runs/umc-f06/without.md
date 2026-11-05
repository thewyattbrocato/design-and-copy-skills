Here's the alt text for each, in page order.

**1. Logo (links to home)**
`alt="Harbour Lane Community Pool – home"`
The image is a link, so the alt text should describe where the link goes, not the picture. Don't write "blue wave logo". The name plus "home" tells screen reader users what the link does.

**2. Lifeguard photo**
`alt="Lifeguard seated on the high chair, watching over an empty lap pool"`
This is informative content, so describe what's shown. Keep it brief. If the surrounding text already covers the photo, you can shorten it further.

**3. Bar chart of weekly visits**
`alt="Bar chart of weekly visits over the last six months, peaking in July and lowest in January"`
The text below the chart already gives the key finding. Even so, the alt text should say what the image is (a bar chart of weekly visits, last six months). Repeating the peak and low is fine and short. Another option is to drop the findings and keep only "Bar chart of weekly visits over the last six months. Summary below." Either works. Don't put the full data in the alt text. If the exact weekly numbers matter, give them in a data table or longer description nearby.

**4. Decorative wave pattern**
`alt=""`
This one shouldn't have any descriptive alt text. Use an empty alt attribute (not a missing one) so screen readers skip it. If it's a CSS background image, that's even better, since it needs no alt at all.

**5. Heart donation button**
`alt="Donate"` on the icon image, or, if the button is an icon font or SVG, put `aria-label="Donate"` on the button and mark the icon `aria-hidden="true"`.
The button's accessible name should say what it does, not what it looks like. Avoid "heart". "Donate" is short and clear. "Donate to Harbour Lane Community Pool" is also fine if you want more context.

**Summary:** Four need text (logo, photo, chart, button), and the decorative wave gets an empty `alt=""`. For the logo and button, describe the action rather than the picture.
