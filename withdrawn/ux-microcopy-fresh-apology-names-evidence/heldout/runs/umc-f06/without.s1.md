Here's the alt text for each image, in page order.

1. **Logo (links to home):** `alt="Harbour Lane Community Pool – home"`
   The image is a link, so the alt text should describe where it goes, not just what it looks like. Don't write "logo" or "image of". Screen readers already announce it as a link and an image.

2. **Lifeguard photo:** `alt="A lifeguard sitting on the high chair, watching over an empty lap pool"`
   This is informative content, so describe what's shown. If the photo is only atmosphere and nothing in the nearby text refers to it, you could shorten it to "Lifeguard on duty at the lap pool".

3. **Bar chart:** `alt="Bar chart of weekly visits over the last six months. Visits peaked in July and were lowest in January."`
   The text below the chart already gives the main finding, so there are two ways to do this:
   - **Short alt (my recommendation):** `alt="Bar chart of weekly visits, last six months"`. This identifies the image without reading the summary twice to screen reader users.
   - **Fuller alt:** the version above, if the chart might be reused somewhere without the summary text.

   If readers need the exact weekly numbers, add a data table or link to one. Alt text can't carry that much detail.

4. **Decorative wave pattern:** `alt=""`
   This one shouldn't have any descriptive alt text. Use an empty `alt=""` so screen readers skip it. Don't leave the attribute off, because some screen readers will then read out the file name. A CSS background image works too.

5. **Heart donation button:** the accessible name belongs on the button, not on the icon.
   ```html
   <button aria-label="Donate">
     <img src="heart.svg" alt="">
   </button>
   ```
   Use `alt="Donate"` on the image if you'd rather not use `aria-label`. If the heart is an inline SVG, use `aria-hidden="true"` on it. "Donate" or "Donate to Harbour Lane Pool" is better than "heart", because the name should describe the action and not the icon. Visible text next to the icon would be better still for sighted users who don't recognise the icon.

Since the audit says every image needs alt text, item 4 is the one to explain to the auditor. An empty `alt=""` is the correct way to mark a decorative image, and WCAG treats it as meeting the requirement.
