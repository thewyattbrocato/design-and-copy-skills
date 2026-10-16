**Short version:** the plan is designed for a first-time, occasional user. Your users are six experts who use the board all day, so most of it works against them. The underlying goal of making it friendlier is fine, but "friendly" for this group means faster, fewer interruptions, and fewer mistakes.

**1. Daily setup wizard: drop it.**
The board already remembers filters and sort, so a wizard adds a step to every morning and gives nothing back. Eight hours a day, six people, every day: that's a lot of wasted clicks. If coordinators sometimes need different filters (a shift change, a different dock group), offer one-click saved views or presets instead. The default should be "open exactly where I left off."

**2. First-login tour: cut it down.**
Tours are fine for new hires, but they should be skippable, shown once, and ideally replayable from a help menu. Six existing users will just dismiss it. The more useful investment is a discoverable keyboard shortcut cheat sheet (`?` to open) and a short note on what the board remembers. A tour that explains the dense grid doesn't help much, since density isn't what trips people up.

**3. Bigger rows and cards per truck: this is the one that does harm.**
Density is the feature here. Coordinators scan many trucks and doors at once to spot conflicts and gaps. Cards with padding might cut the visible trucks by half or more, which means more scrolling and more lost context. It also likely breaks the keyboard flow they've built habits around. If the real complaint is that the grid is hard to read, there are cheaper fixes:
- better typography and column alignment
- clearer status color (with a non-color cue as well)
- zebra striping or a row-hover highlight
- an optional "comfortable" density toggle that is off by default

Ask the PM what specifically feels unfriendly. I suspect it's a first impression from someone who hasn't used it all day.

**4. Confirmation after every door-change drag: wrong tool for the problem.**
Confirm dialogs on a frequent, routine action train people to click through without reading, so they stop protecting anyone, and they slow down the most common task on the board. The real risk is an accidental drag. Better options:
- **Undo** (toast with an Undo button, plus Ctrl/Cmd+Z). This is faster and safer than confirming.
- Confirm only for genuinely risky moves, such as a truck already checked in or at a door, a conflict with another booking, or a door that's blocked or the wrong type.
- Make drags harder to trigger by accident, for example with a movement threshold.

**What I'd suggest instead:**
- Keep persistence, and make it more visible (for example, "Your view is saved").
- Add undo and conflict warnings for moves.
- Add a keyboard shortcut reference.
- Make small readability improvements to the grid.
- Offer an optional density toggle if someone really wants it.

**Before building anything:** sit with two or three coordinators for an hour, or ask them directly what annoys them. The PM's plan comes from assumptions, and the people using it eight hours a day can tell you where the real friction is. If they don't say any of these four things, that's your answer.
