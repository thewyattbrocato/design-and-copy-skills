It's mostly fine. The measure is right (66 characters is in the sweet spot), 18px body with generous leading suits long reading, and the single column suits continuous prose. The lead image running wider than the text and the pull quotes hanging into the margin each have a clear job, so they aren't arbitrary grid breaks. I'd check four things before it ships.

1. **Top bar edges vs. the column.** This is the one real issue. The logo and Subscribe sit at the far edges of the page, while the text is a narrow centered column. On a wide desktop the bar and the content share no vertical edge, so the logo floats far from the headline. Constrain the bar's inner width to the lead image's width. Then the logo lines up with the image edge and Subscribe with the other edge. Alternatively, align to the text column. Pick one and use it on every page.

2. **Pull quote room at in-between widths.** An 80px overhang on each side needs about 66ch plus 160px plus your page margins. That fails on small laptops and tablets in portrait, where the quote would clip or cause horizontal scroll. Set the overhang breakpoint from that arithmetic, not from a generic "desktop" value. Below it, pull quotes should sit inside the column.

3. **Worst-case content.** Test with a three-line headline and a standfirst that wraps. On phones, "one-line standfirst" will wrap, so make sure that's styled on purpose and not clipped. Also test an article with no lead image, two subheads in a row, and a pull quote right after a subhead.

4. **Phone details.** Say whether the lead image bleeds to the screen edge or stays inside the 20px padding. Bleeding usually looks better, but then the in-text images should do the same, or the two will look inconsistent. Also check that the text-width images aren't cropped to a fixed ratio. Tall or wide whole images should keep their shape.

You didn't mention captions and credits. If images carry them, decide now whether they sit under the image at the text width, including under the wider lead image. For an archive, you might also want previous/next issue links or a link back to the archive index near "More from this issue". That's a content call, not a layout flaw.

I haven't seen the actual page or CSS. This review is based only on your description.
