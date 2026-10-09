**I pick Option 2**, with one tweak: set the measure on the text element, not the page wrapper.

**Why Option 2 works**
- **Line length:** a 680px column at 18px gives roughly 65–75 characters per line. That's the top of the comfortable range for continuous reading. Option 1 runs at about 150 characters per line, which is far too long. Readers lose their place when moving from the end of one line to the start of the next.
- **Line height:** 1.6 suits long-form text with long-ish lines. Option 1's 1.4 is on the tight side for 15px text on a 1100px line. Option 3's 1.3 is too tight for body copy in any layout.
- **Size:** 18px is a bit above the 16px default, which helps here. Tax content is dense and people read it to act on it, so it should stay comfortable. 15px is too small for text people have to follow carefully.
- **Option 3's two columns:** each column is a decent width at about 60–65 characters, but two columns are the wrong pattern for a help center on screen. Readers have to scroll down one column and back up to the next. Steps and cross-references also break across the column boundary.

**Implementation notes**
- Use `font-size: 1.125rem` rather than `18px`, so the text follows the user's browser setting.
- Use `line-height: 1.6`, unitless.
- Put `max-width: 65ch` on the paragraphs and lists, not on the container. Tables, screenshots and form-field examples, which are common in tax help, can then run wider than the prose.
- Headings should be tighter (about 1.2) and have roughly twice as much space above as below.
- Use `font-variant-numeric: tabular-nums` for any dollar amounts or tax-form tables, and right-align them.
- On narrow screens, let the column fill the width with normal side padding. The line length will drop on its own.

If the help center also needs a sidebar or table of contents, put it outside the 680px column. That keeps the reading column the same width.
