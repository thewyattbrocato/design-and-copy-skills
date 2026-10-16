You're right. A mandatory forty-shortcut walkthrough on day one is the wrong tool for this audience. Don't replace it with nothing. Replace it with help that shows up while people work.

**Why the tour fails**
- People can hold only a few new things in mind at once. Forty shortcuts means they retain none of them.
- Nobody practices a shortcut they have no use for yet. Nothing in a tour makes a new user need "jump between matters" in the first five minutes.
- These users work eight hours a day and have habits in other tools. A forced tutorial reads as an interruption, and they will skip it as fast as they can.
- Shortcuts are the one thing here that users tend to learn well on their own. The only open question is when and how you tell them.

**What to do instead**

The goal is that in week two, users reach for a shortcut without thinking about it. Everything below serves that.

1. **Show the shortcut where the mouse action happens.** Put the key combo in menu items, button tooltips, and the command palette. Every mouse use then teaches the keyboard route for free. This does most of the work, and it costs nothing in onboarding time.

2. **Add a command palette that shows shortcuts beside every action.** Users who search for "split view" see the key next to it. Searching becomes the way they learn.

3. **Nudge after repeated mouse use.** If someone clicks "split view" for the third time, show one small, dismissible hint: "Split view: `[shortcut]`". Wait until they've done the action by hand a few times, because that's when they're ready to hear it. One hint at a time, with a "don't show these" option.

4. **Teach a starter set of 3 to 5 in the first session.** Pick the ones tied to the first real task, such as creating a note, jumping to a matter, and quick-cite. Introduce each one when the user is doing that task for the first time, not in a separate tour. Use "try it now" in the real product.

5. **Give the rest a reference, not a lesson.** Provide a searchable cheat sheet, grouped by task (research, drafting, matter navigation), opened with `?` or from the Help menu. Pair it with a short "what's new" note when you ship new shortcuts, so power users aren't left finding them by accident.

6. **Offer an optional "Keyboard tips" track.** Make it opt-in, surfaced in settings and the cheat sheet, and mention it once. Experts can choose to take it. It shouldn't gate anything.

7. **Fix the design first.** Check that shortcuts are guessable and consistent (a pattern like one modifier for navigation and another for editing). Check that they don't collide with the OS, with browsers, or with Word and Westlaw habits your users already have. A predictable scheme means fewer shortcuts need teaching.

**What to tell the PM**

The PM wants every user to know the shortcuts. That's a fair goal. A day-one walkthrough doesn't achieve it, because people forget what they haven't used. Frame it as "teach each shortcut at the moment it's useful." Both approaches aim at the same outcome, and this one gets there more reliably.

**How to settle it**

Don't use tour completion as the measure. Use shortcut use at days 7 and 30: the share of users who run each core action by keyboard unprompted. You could test it directly by sending half of new users through the full tour and half through the in-context approach. If the tour wins on that measure, you'll have the evidence to say so.

Two assumptions: I assumed a desktop app with a menu bar and tooltips, and I haven't named specific key combos because I don't have your shortcut map. If you share the list, I can help pick the starter 3 to 5 and decide which shortcuts deserve a nudge.
