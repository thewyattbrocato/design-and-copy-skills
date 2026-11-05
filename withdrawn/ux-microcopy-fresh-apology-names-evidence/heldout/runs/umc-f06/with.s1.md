Here's the alt text for each, in page order:

1. **Logo (links to home):** `alt="Harbour Lane Community Pool – home"`
   Since the image is the link's only content, the alt text should name the destination. It shouldn't describe the wave. Screen reader users hear "link, Harbour Lane Community Pool – home."

2. **Lifeguard photo:** `alt="A lifeguard sits on the high chair, watching over an empty lap pool."`
   This is informative, so describe what's shown. Don't add "photo of," because screen readers already announce it as an image.

3. **Bar chart:** `alt="Bar chart of weekly visits over the last six months, with a peak in July and a low in January."`
   The text below already gives the key takeaway. So the alt text should say what the chart is and avoid repeating the summary at length. A shorter option is `alt="Bar chart of weekly visits, last six months"`. If the chart has more detail than the summary covers, such as exact weekly figures, add a data table or a longer description nearby.

4. **Decorative wave pattern:** `alt=""`
   Use an empty alt attribute, not a missing one, so screen readers skip it. If it's a CSS background image instead of an `<img>`, it needs no alt at all. Either way, don't write "decorative wave" as alt text.

5. **Heart donation button:** `alt="Donate"` if the icon is an `<img>` inside the button. If it's an SVG or icon font, put `aria-label="Donate"` on the button and mark the icon `aria-hidden="true"`.
   The text should describe the action and not the icon, so avoid "heart." If the button is more specific, such as "Donate to Harbour Lane Community Pool", use that wording. Also consider a visible tooltip or label, since sighted users may not know what the heart does.

On the chart (item 3): the alt text above repeats the peak and low from the text below it. A screen reader will read both, so the shorter version is better if the summary sits right next to the chart.
