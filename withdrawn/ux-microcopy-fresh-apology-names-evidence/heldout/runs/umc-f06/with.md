Here's the alt text for each image, in page order.

**1. Logo (header, links to home)**
`alt="Harbour Lane Community Pool, home"`
The image is the only content of the link, so the alt text has to describe where the link goes, not the picture. Leave out "logo" and "wave". The name plus "home" tells screen reader users what the link does.

**2. Lifeguard photo**
`alt="Lifeguard seated on the high chair, watching over an empty lap pool"`
This is informative content, so describe what it shows in one short sentence. If the photo has a caption or nearby text that already says this, you could shorten it, but a description is a safe default.

**3. Bar chart of weekly visits**
`alt="Bar chart of weekly visits over the last six months, peaking in July and lowest in January"`
The text below the chart already gives the key finding, so the alt text doesn't need to list every bar. It should say what kind of chart it is, what it measures and over what period. Repeating the peak and low is optional. If you want to avoid duplicating the summary, use `alt="Bar chart of weekly visits over the last six months"`, since the adjacent text carries the finding. If the exact weekly numbers matter, offer them in a data table or a longer description nearby, because alt text isn't the place for them.

**4. Decorative wave pattern**
`alt=""`
This one shouldn't have any alt text. Use an empty `alt` attribute (not a missing one), so screen readers skip it. If it's a CSS background image instead of an `<img>`, you don't need to do anything.

**5. Heart button (opens donation page)**
`alt="Donate"` if the icon is an `<img>` inside the button.
The button has no visible text, so the icon's alt text becomes the button's accessible name. Describe the action, not the icon: "Donate", not "Heart". If the heart is an inline SVG or icon font, set `aria-label="Donate"` on the button and mark the icon `aria-hidden="true"`. Sighted users also only see a heart, so consider adding a visible "Donate" label or a tooltip.

**Summary:** images 1, 2, 3 and 5 get alt text, and image 4 gets `alt=""`. Only the logo and the button need text that describes their function rather than their appearance.
