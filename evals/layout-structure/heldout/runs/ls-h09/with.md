**Single centered column with full-width photos.**

- **Photos are the content.** With 8-12 photos per post, you want each one big enough to show the landscape. A two-column layout shrinks them to half width or forces awkward crops.
- **The text is short.** Three or four short paragraphs don't need columns. In a magazine layout they'd leave one column nearly empty, or you'd split a few sentences across two narrow columns.
- **It reads as a sequence.** A hike post is a story told in order (trailhead, climb, summit, descent). One column keeps that order obvious, while two columns make readers choose where to look next.
- **It works on phones.** Most club members will probably open posts from a link on their phone, and a two-column layout collapses to one column there anyway. Designing for the single column first means the desktop and mobile versions match.

**Details that make it work:**
- Keep the text at a readable width of about 65-75 characters per line (roughly 640-720px). Let the photos break out wider, up to the full viewport or a ~1100px container.
- Put a paragraph or two between photos instead of stacking them all together. This sets the pace of the post.
- Occasionally put two portrait or detail shots side by side as a pair. This adds variety without needing a column system.
- Use lazy loading and responsive `srcset` images, since 8-12 full-width photos get heavy quickly.
- Put short captions under the photos with the location or elevation, if you have them.

Consider the magazine layout only for a separate photo-essay format with almost no text. Even then, a gallery grid would suit it better than columns.
