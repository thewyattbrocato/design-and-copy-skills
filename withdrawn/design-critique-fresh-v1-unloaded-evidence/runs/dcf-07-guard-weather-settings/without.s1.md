**The biggest problem is that the page has two save models.** The C/F switch applies instantly, but the rain alert switch waits for Save. Users can't tell which controls are live, so they will tap Save when they don't need to, or leave without saving and assume a change stuck. A user who flips rain alerts on and backs out gets no alerts, and nothing warned them.

**Change:** Apply every setting immediately and remove the Save button. These are all cheap, reversible preferences, so a save step adds friction and no safety.
- Theme, units and the alerts toggle can all take effect on tap.
- For rain alerts, show the result where it happens. That means the OS notification permission prompt, plus an inline state such as "Notifications are blocked in system settings" if it's denied.
- If you really need a Save button (for example, because alerts register with a server), do it consistently. Make every control a draft, show a Cancel/Discard option, disable Save until something changes, and warn on back-navigation with unsaved changes. A preview-before-save only on C/F is the worst of both.

**Other changes, in priority order**

1. **Group the rows under headers.** Right now it's five unrelated rows. Use something like Units (temperature, wind), Alerts (rain alerts, quiet hours), Location, Appearance. Grouping makes the page scannable and gives the conditional quiet-hours row a clear parent.
2. **Fix the layout shift from quiet hours.** If the picker appears and disappears, everything below it jumps, including the Save button. Animate the expansion and keep the row indented under Rain alerts. Alternatively, show it always and grey it out when alerts are off, so users learn it exists.
3. **Make the quiet-hours picker explicit.** It needs a start and an end ("From 22:00 to 07:00"), a sensible default, and 12/24-hour handling that follows the phone. One time picker isn't enough.
4. **Reorder around dependencies.** Home location drives everything else, including where rain alerts apply. Put it first or next to Alerts, not fourth.
5. **Pin the Save button, if you keep it.** At the bottom of a scrolling column it can sit below the fold, or behind the keyboard or the expanded picker. Pin it to the bottom of the screen.
6. **Polish the labels and defaults.**
   - Write the temperature options as °C / °F.
   - Rename "match phone" to "System" or "Automatic" and make it the default.
   - Default units from the device's region.
   - Add "Use current location" on the search screen.
7. **Keep the controls consistent.** Temperature, wind and theme are all pick-one choices, so use the same segmented style for them. Don't make one a switch and another a list. Make sure the selected state doesn't rely on color alone.

If you do only one thing, drop Save and apply changes immediately. That removes the main source of confusion and a whole button's worth of UI.
