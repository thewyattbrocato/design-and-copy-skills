**Short version:** the plan is aimed at a first-time user, and your users are six people who are past expert level. It would make the product worse for them. Only one part of the instinct is worth keeping.

**Assumption:** six coordinators, desktop and keyboard, eight hours a day, every day. I've treated that as a given. Dense, keyboard-driven, remembered state is the right design for it.

**1. Morning setup wizard: drop it.**
- The board already remembers each coordinator's filters and sort. A wizard asks something the product already knows, six people times every morning, for no benefit.
- If a coordinator's filters are wrong on a given day, they change them in two keystrokes. A wizard turns a rare correction into a daily obligation.
- If the PM's worry is "people forget to set the right filters", show the active filters in the header, with a one-key reset. That surfaces state without gating the board.

**2. First-login tour with tooltips: drop it, or replace it with something small.**
- With six users, a tour is a one-time cost that mostly lands on people who already know the tool. New hires are the only audience.
- If onboarding matters, add a shortcut cheat-sheet on `?` and a link to it in the header. It's cheap, it's always available, and it helps experts who want to speed up.
- Make sure every tooltip-worthy control has a visible label, so nothing needs explaining.

**3. Bigger rows and a card per truck: this does the most damage.**
- Density is the feature. Coordinators scan many trucks and doors at once. Larger padding and cards would cut how many rows fit on screen, probably by half or more, which means more scrolling and more lost context. I haven't measured this, so check it against your real screens.
- If the real complaint is "it looks intimidating", offer a **density toggle** that is remembered per user, with dense as the default. Or fix the real readability issues: contrast, row striping, a clearer status color plus a text or icon cue so color isn't the only signal.
- Ask the PM what prompted this. If it came from a new person's first impression, that's an onboarding problem, not a daily-use problem.

**4. Confirmation after every door-change drag: replace it with undo.**
- A confirmation on a frequent, reversible action trains people to click through without reading. After a week they'll confirm blindly, including the one time it matters.
- Moving a truck to another door is reversible, so give it an **Undo** (toast or `Ctrl+Z`, roughly 6–10 seconds) instead. Mistakes become cheap to fix and the flow stays fast.
- Make the result visible in place: briefly highlight the moved truck and show "Truck 42: Door 7 → Door 9".
- Check one thing: does a move trigger something external, like a driver notification or a carrier message? If so, that part can't be undone, and it's the one place a specific confirmation makes sense. Use a single named prompt, such as "This will notify the driver", and only for moves that trigger it.
- Confirm that dragging has a keyboard route too (select a truck, pick a door), since the board is keyboard-driven.

**What to keep from "friendlier":**
- Visible active-filter state with a reset.
- Undo on moves.
- A `?` shortcut sheet.
- An optional, remembered density setting.
- Clearer error and conflict messages, for example when a door is double-booked. That's where "friendly" pays off for people in a hurry.

**How to put it to the PM:** the plan optimizes for the first five minutes, and the product is used for thousands of hours. Suggest shadowing a coordinator for a shift and listing what slows them down. I'd bet it isn't any of these four items. If they still want to test one, A/B the density toggle with two or three coordinators for a week. It's the least risky of the four.
