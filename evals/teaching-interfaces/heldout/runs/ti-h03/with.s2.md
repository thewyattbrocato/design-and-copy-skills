**Build (c), the interactive setup with a live preview.**

**Why**

- **It's the task itself.** New users fail at creating an alert, so they should create their first one with guidance. Option (c) is the only choice where the first real alert exists when they finish. (a) and (b) teach about the task and leave them to do it from memory.
- **The four settings only make sense against real conditions.** Swell range, wind limit and time window are abstract until you see them on a forecast. A preview such as "with these settings, today would have matched 3 of 8 hours" shows the effect of each choice right away. A wrong guess, like a wind limit that rules out every day, shows up on screen instead of as a silent alert that never fires.
- **It doesn't rely on memory.** Video and carousel put the explanation before the action, so users have to remember it when they reach the form. In (c) the explanation sits next to each control while they use it.
- **Skipping the video or carousel costs little.** People tend to skip both. A step-by-step flow can't be skipped without also skipping the thing they came to do.
- **It works with no data.** Whichever option you pick, you're guessing about your users. (c) is the safest guess because it doesn't depend on users watching or reading. Even if the explanations go unread, they still end up with a working alert.

**How to keep it small enough for one sprint**

- Use one screen per setting, in this order: beach, swell height, wind limit, time window. Keep earlier choices visible as the user goes.
- Give each step one sentence of explanation and a sensible default. For example, pre-fill a swell range that's typical for the chosen beach. Label defaults as suggestions, and let users change them in one tap.
- Show the live preview at every step. Mark it as today's real conditions at the chosen beach, so it can't be mistaken for sample data.
- End by stating what the alert will do, e.g. "You'll be notified when [your settings] match." Skip the congratulations screen.
- Include a visible skip, and an entry point from the empty alerts list so users can return to the flow later.

**Risks**

- **Forecast data.** The preview needs a conditions feed at the moment of setup. If it's slow or fails, the flow stalls. Plan a fallback that lets users continue without the preview.
- **Skill levels.** Experienced surfers may find the steps slow. The skip link and defaults should let them finish in a few taps.
- **Unknown audience.** Since you have no data, treat this as a bet and measure it.

**How to measure it**

Don't use flow completion as the measure. Track whether new users still have an active alert a week later. Also look at whether they create or edit a second alert without the guided flow, and whether early alerts get deleted or never fire. If you can, ship (c) to half of new users and keep the current setup for the other half, so you get a real comparison.
