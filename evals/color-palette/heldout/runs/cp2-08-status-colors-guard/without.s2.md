No, I'd skip that. Status colors work best when they're predictable, and a brand-derived set will cost you clarity.

**The main problem is that your brand color is a failure color.** #d93a35 reads as "error" to almost everyone. If it's on your primary buttons, "Deploy" and "Approve" will look like danger actions. If it's also your "failed" color, users can't tell a call to action from a broken deploy. If you derive the other statuses from the same palette, you'll get colors that are either too close together or that contradict what people expect.

**What I'd do:**
- **Use conventional semantics for status.**
  - Succeeded: green
  - Failed: red
  - Running: blue (or a neutral/cyan with an animated spinner)
  - Waiting for approval: amber/yellow
- **Keep the failed red distinct from the brand red.** Shift it slightly, for example a cooler or deeper red, and use it only for status. Better still, consider a non-red primary button, or a neutral or dark one. Your brand red on a primary button next to red "Failed" badges will keep causing confusion.
- **Don't rely on color alone.** Pair each status with an icon and a text label (✓, ✕, spinner, clock). Red and green are hard to tell apart for many colorblind users, and a deploy dashboard is something people scan quickly.
- **Check contrast.** Badge text and icons should meet WCAG AA (4.5:1 for text) in both light and dark themes.
- **Keep the brand in the surroundings.** Use it for the logo, nav accents, links, and focus states. Don't use it for status.

Brand colors tell people who you are, while status colors tell them what happened. Mixing the two makes the dashboard slower to read.

If you'd like, I can draft a concrete palette with hex values for light and dark themes and check the contrast ratios.
