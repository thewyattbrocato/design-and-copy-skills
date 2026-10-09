Several things stack up. In rough order of likely impact:

**1. The video background plus logo is a heavy, empty first screen.**
- Full-bleed video is often the biggest load cost. On mobile or slow connections it delays first paint, and it can eat data.
- A logo alone above the fold doesn't say what the event is, when it is, where it is, or what to do next. There's no headline, date, location, or CTA.
- Check that the video has a poster image, is muted and `playsinline`, and is compressed. Also check that text over it has enough contrast.

**2. No clear call to action.**
- Nothing in your structure says "Register" or "Get tickets". If a visitor can't find that within a few seconds, they leave. Put it in the hero and in the nav.

**3. Sponsors come before content.**
- Twelve sponsor logos in a 4-column grid, directly after the hero, push the actual value (what, when, who, why attend) down the page. Sponsors are about your needs, not the visitor's. Move them lower, or show a smaller strip.

**4. The 1300px body paragraph is unreadable.**
- Comfortable line length is about 60–80 characters, roughly 600–700px at normal sizes. At 1300px, lines run 150+ characters, and people lose their place and skip it.
- It's also a single paragraph. Break it up with headings, key facts (date, venue, price), and scannable chunks.
- 1300px is also wider than many laptop viewports once you account for padding, so check for horizontal overflow on smaller screens.

**5. The navigation is a mess.**
- Eleven items is too many. Visitors can't scan them, and they'll likely wrap or overflow on mobile. Aim for 5–7, and group the rest under a menu or the footer.
- It sits *below* most of the content, so it isn't a navigation aid on arrival. Visitors have to scroll past the hero, sponsors, and paragraph to see it. Since it's sticky, I'd guess you meant it to be at the top. Confirm where it actually renders.
- It's left-aligned while everything else is centered. That reads as an accident and makes the page feel unfinished.
- A sticky nav with 11 items takes up a lot of screen space, especially on mobile.

**6. Speakers are buried.**
- Speakers are usually the main draw for a conference, and here they come after sponsors and a wall of text. Put them higher. Make sure each has a photo, a name, and an affiliation, and that the grid collapses to 1–2 columns on mobile.

**7. Layout and responsiveness.**
- The 4-column and 3-column grids need breakpoints. Logos and photos will get tiny on phones otherwise.
- The mix of alignments (centered content, left-aligned nav) and widths (1300px text against grid containers) suggests there's no consistent container width.

**Suggested order**
1. Hero: headline, date and location, a Register button, and a lightweight video with a poster image.
2. Short, readable "what and why" copy at about 65 characters per line, with key facts pulled out.
3. Speakers.
4. Agenda or schedule, if you have one. I don't see it in your structure, and visitors usually want it.
5. Sponsors, smaller and lower.
6. Footer.
7. A sticky nav at the top with 5–7 items and a CTA, aligned to match the content.

**To confirm the cause**
I'm inferring from the structure alone. To confirm, check:
- Lighthouse or PageSpeed results, mainly LCP and total page weight.
- Scroll-depth and click maps, to see where people drop off.
- A mobile pass, since bounce rates are usually worst there.

If you share the code or a URL, I can look at the actual markup and performance.
