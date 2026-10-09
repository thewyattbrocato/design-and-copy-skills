**Option 2.**

- **Line length:** At 18px, a 680px container gives roughly 60–75 characters per line, which is the range where long-form reading is most comfortable. Option 1 gives about 150+ characters per line at 1100px, which is far too long. Eyes lose their place on the return sweep. Option 3's 480px columns are about 55–60 characters, which is fine.
- **Line height:** 1.6 suits sustained reading and helps people track lines. Option 3's 1.3 is too tight for body text at this length, and Option 1's 1.4 is borderline, especially paired with its long lines.
- **Font size:** 18px is easy to read and accessible. 15px (Option 1) is small for dense, anxiety-prone content like taxes. Many users will be older or reading on mobile.
- **Option 3's columns:** Two columns suit print or short scannable content. In a long scrolling help article, they force users to scroll back up to start the second column, and they break down on narrow screens. They also work badly with step-by-step instructions, inline screenshots and tables.

**Caveats:**
- Keep the 680px column for prose only. Let tables, code blocks and screenshots break out wider if needed.
- Use `max-width: 680px` (or about `65ch`) rather than a fixed width, so it collapses cleanly on mobile.
- Add a sticky table of contents or sidebar to use the leftover horizontal space on desktop. This is also how most good long-form docs handle it.
- Keep headings and callouts well differentiated, since tax content has a lot of "important exception" notes.

If you want to validate it, a quick A/B test on task completion for a few common help articles would settle any doubt, but Option 2 is the strong default.
