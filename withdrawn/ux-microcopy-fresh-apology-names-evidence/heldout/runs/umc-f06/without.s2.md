Here's what I'd put for each, in page order:

1. **Logo (linked to home):** `alt="Harbour Lane Community Pool, home"`
 Since the image is the link's only content, the alt text should describe where the link goes, not the picture. Don't say "logo" or "blue wave"; the pool's name plus "home" covers it.

2. **Lifeguard photo:** `alt="A lifeguard sits on the high chair, watching over an empty lap pool."`
 This is a content image, so describe what it shows in a short sentence. If the surrounding text already says something about the lifeguards or the pool, you can trim it, but I'd keep it as is.

3. **Bar chart of weekly visits:** `alt="Bar chart of weekly visits over the last six months. Visits peaked in July and were lowest in January."`
 The text below already gives the key takeaway, so the alt text just needs to identify the chart and its subject. If you'd rather not repeat that sentence for screen reader users, shorten it to `alt="Bar chart of weekly visits, last six months"`. Either way, the summary text beneath it is doing the real work. If the exact weekly figures matter, add a data table or link to one.

4. **Decorative wave pattern:** `alt=""` (empty)
 It carries no information, so it should have an empty alt attribute. Keep the attribute present but empty so screen readers skip it. Don't leave `alt` out entirely, because some screen readers will then read the file name. (If it's a CSS background image instead, no alt is needed.)

5. **Round heart button:** `alt="Donate"`, if the image is inside the button or link.
 The alt text should describe the action, not the icon, so avoid "heart". If the heart is an inline SVG or icon font rather than an `<img>`, the equivalent is `aria-label="Donate"` on the button, with the icon marked `aria-hidden="true"`. "Donate to Harbour Lane Community Pool" also works if you want more context, but keep the visible-or-accessible name consistent with any visible label.
