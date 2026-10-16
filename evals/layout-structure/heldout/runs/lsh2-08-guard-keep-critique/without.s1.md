The structure is sound and I'd ship it. The 66-character measure, 18px type, subheads every ~300 words, and the order of post-article elements are all good choices. There are a few edge cases I'd check first. They're about the gaps between your breakpoints, not the design itself.

**Worth fixing before shipping**
1. **Pull quotes at in-between widths.** An 80px overhang only works if each side margin is at least 80px. A 66ch column at 18px is roughly 600-650px wide. On a 768-1024px tablet or a narrow laptop window, the margins are smaller than that, so the quotes will clip or cause horizontal scroll. Gate the overhang behind a min-width (about column width + 2×80px + some buffer), and below that keep quotes inside the column.
2. **The wider lead image has the same problem.** Give it a `max-width` and make sure it falls back to the column width, or to full-bleed, below the same breakpoint. Check that it doesn't produce a horizontal scrollbar from `100vw` including the scrollbar width.
3. **The "one-line" standfirst will wrap on phones.** Design for two or three lines there, and don't truncate it or lock its height.

**Smaller things to check**
- **Image captions and alt text.** You didn't mention either. Archive templates tend to get these wrong, so make sure the template has a caption slot and a required alt field.
- **Archive navigation.** A reader who lands from search has a bar with only a logo and Subscribe. A link to the archive and to the issue itself, either in the top bar or as breadcrumb text above the headline, will help. Previous/next issue links would also fit near "More from this issue".
- **Duplicate Subscribe prompts.** The top bar and the end box are fine together. Just make sure the top bar button is quiet, so it doesn't compete with the headline.
- **Phone details.** 20px padding is fine. Make sure pull quotes drop any negative margins, and that long words, URLs, and wide tables or code blocks scroll or wrap instead of pushing the page wider.
- **Line height.** "Generous" is good. About 1.55-1.65 for body text works, and the headline and subheads should be tighter, around 1.2-1.3.

If you'd like, point me at the template files and I'll check the CSS for these cases directly.
