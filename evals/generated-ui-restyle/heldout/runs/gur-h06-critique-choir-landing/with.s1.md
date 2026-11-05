Yes, she's right. The page has no tell that comes from choir directors or rehearsal rooms. Swap "Stavewise" for any other SaaS name and nothing else would need to change. The structure is fine (headline, proof, three benefits), so it's fixable without starting over.

**Ranked by how much each makes it read as generic**

1. **The copy (h1, subhead, card titles).** "Supercharge your choir with intelligent rehearsals," "all-in-one platform that empowers directors to streamline," "focus on what matters most," "Lightning-fast," and "Effortlessly" would fit any product. Even "Smart attendance" doesn't say what's smart about it. Your real selling point appears only in the last card: "Know exactly who needs help before the big night." Lead with that, in a director's words, e.g. "See who hasn't learned their part before the concert." Then say the rest plainly: parts and practice tracks go out by section, and attendance takes one tap at rehearsal.

2. **"Trusted by 1,800+ choirs worldwide."** This is the most important fix, and it's a content problem, not a styling one. You have 38 pilot schools. Music teachers talk to each other, and one who sees an inflated number will stop trusting the rest of the page. Use the true number ("Piloting in 38 schools") or, better, one named director with a real quote. Only publish a quote you actually have permission to use.

3. **The palette and effects.** The page uses a dark slate background, a blurred purple blob, indigo-to-pink gradients on the headline, buttons and icon tiles, glass cards with `backdrop-blur`, and a colored button glow. Together these are the strongest visual sign of a generated page. Pick colors from the world of the product: warm paper white, ink-dark text, and one accent, such as a pencil-marking red or a deep blue. Directors work from printed scores, so a light "page" look will feel more familiar than neon on black. Flat buttons are fine.

4. **The layout.** A centered stack with a pill badge, a big gradient headline, two buttons, and three equal icon cards is the standard template. The bigger problem is that nothing on the page shows the product. Replace the card row, or put beside the hero, a realistic preview of the screen directors would use. For example, a roster by section with "Alto 2: 3 of 9 haven't opened Track 4" and an attendance list with tap targets. Mark any names in it as sample data. That shows the "who hasn't learned their part" feature better than any card can.

5. **The icons.** `Sparkles` appears twice, once in the badge and once for "Smart attendance." `Zap` and `Shield` don't relate to parts or insights. Use a small set tied to the product (a staff, a section, a checkmark), or drop the icons once the preview carries the features.

6. **The "AI-powered" badge.** If AI doesn't do something visible and useful for directors, remove it. Many teachers are wary of it, and it adds to the generic feel. If it is real, say what it does in the feature copy instead of using a badge.

7. **Type and small details.** The page uses the default Tailwind sans at `text-6xl font-bold tracking-tight`, with a `hover:-translate-y-1` lift on every card. Choose one typeface with some character for the headline, such as a humanist serif, and keep the body plain. Remove hover effects that serve no purpose.

**What I'd change first**

1. Fix the "1,800+ choirs" line today. It's a credibility risk.
2. Rewrite the headline, subhead, and card copy using the nouns above (parts, sections, practice tracks, concert, rehearsal).
3. Swap the purple gradient look for a paper and ink palette with one accent. This takes a few Tailwind token changes, and the markup can stay mostly as it is.
4. Add the product preview.

If you want, I can do the full restyle as code. I'd keep the section order and your content, and use placeholders instead of invented numbers or quotes. I'd also need to know whether you have a real logo or brand color I should keep.
