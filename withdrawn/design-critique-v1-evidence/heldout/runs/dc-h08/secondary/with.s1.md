I'd group the 14 toggles by what they're about, put the two master switches at the top, and turn the channel-specific toggles into a small grid. That cuts the visible rows from 14 to about 8.

**Proposed layout**

1. **Top: master controls.** Show Push and Email as column headers with a switch in each. Turning one off disables and greys out its per-topic toggles, with a short note such as "Push is paused."

2. **Garden alerts** (time-sensitive, most users want these)
   | | Push | Email |
   |---|---|---|
   | Watering reminders | ● | |
   | Frost alerts | ● | ● |
   | Harvest windows | ● | ● |

3. **Community**
   | | Push | Email |
   |---|---|---|
   | Friend requests | ● | ● |
   | Comments on my beds | ● | ● |
   | Shared bed invites | ● | ● |

4. **Ideas & summaries**
   | | Push | Email |
   |---|---|---|
   | New plant suggestions | ● | |
   | Plant of the week | ● | ● |
   | Weekly summary | | ● |

5. **Quiet hours.** Put this directly under the grid, not at the bottom. It controls when push arrives, so it belongs with the push settings. Use a time range picker here.

6. **News & offers** (collapsed by default, or at the bottom)
   - Product news (email)
   - Sale announcements (push or email)

   Keep these separate from the rest. They're marketing rather than app behavior, so they should be opt-in and easy to turn off as a group. Bundling them with frost alerts makes it unclear what turning them off actually does.

**Why this works**

- The grid shows the channel choice once per topic, so you don't need separate "weekly summary email" and "product news email" rows.
- Section headers say what each group is for, so people can scan for the category they care about instead of reading 14 identical labels.
- Masters at the top let people quiet everything in one tap, which is probably what the "overwhelming" feedback is really asking for.

**Small extras to consider**

- Show a count in each section header, like "Garden alerts · 3 on", so people can see the state without expanding anything.
- Give each row a one-line description. "Frost alerts: warnings when nighttime temperatures near your beds drop below freezing" does more than the bare label.
- Check your defaults. If everything starts on, the screen will feel overwhelming even when well-organized. Starting marketing off and keeping the garden alerts on is usually the right balance.

I didn't look at the Fernwood codebase, so this is a layout recommendation only. If you share the component file, I can help build it.
