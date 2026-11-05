**Verdict: the controls are fine. The save model is the main problem.** Some settings apply instantly and others wait for Save, and nothing on screen tells the user which is which.

**Findings, in priority order**

1. **Mixed apply models (high).**
   - The C/F switch changes the screen behind it immediately, so it behaves like a live setting. Rain alerts only take effect after Save.
   - Someone who flips Rain alerts, sees nothing change and leaves has no alerts. The failure is silent, and for a weather app a missed alert is the costly kind.
   - Someone who flips C/F and backs out may find it changed anyway, with no "Save" to explain it.
   - **Fix:** pick one model. I'd apply everything immediately, which is the phone convention, and drop the Save button. Unit, theme and wind speed are cheap to reverse. If alerts need a confirmation, such as a permission prompt, show that step when the switch is toggled.
   - **If Save stays:** make the preview a true draft. Revert it on back or cancel, and prompt on unsaved changes.

2. **The Save button is ambiguous (medium).**
   - It is always full-width and always looks active, so it doesn't show whether anything is unsaved. With live-applying rows it also suggests that nothing has been applied yet, which is wrong for C/F.
   - **Fix:** if Save survives, disable it until something changes and show a confirmation afterward.

3. **Quiet hours appear and disappear (medium).**
   - The time picker shows under Rain alerts only when alerts are on. This is a reasonable pattern, but it moves everything below it down the page.
   - **Fix:** animate the expansion so the rows below don't jump. Keep the quiet-hours row's label and current value, such as "10 pm – 7 am", visible in a collapsed form.
   - **Also check:** make sure the Save button doesn't fall off-screen when the picker opens.

4. **Home location is a different kind of row (low).**
   - It is a navigation row inside a list of inline controls. The chevron handles that fine, but a screen reader and a tapping user can't tell it opens a search. A pending change there also interacts with Save in an undefined way.
   - **Fix:** say what happens when the user picks a city. Either apply it on return from search, or show it as an unsaved change.

5. **Row order (low, taste).**
   - Unit-style settings, the alert settings, location and theme are interleaved. Grouping them would help scanning: Units (temperature, wind), Alerts (rain, quiet hours), then Location and Appearance.
   - **Fix:** use short section headers. Location is arguably the most important setting for a weather app, so consider moving it to the top.

**What works and should stay**
- **Tap targets and labels.** You say they are comfortable and clear, so don't touch them.
- **Single column.** It suits a phone and has no competing layout.
- **Instant preview for units.** The user sees the effect right away, which is good. Extend it to the other settings rather than removing it.
- **Conditional quiet hours.** It hides an irrelevant control when alerts are off.

**Not checked:** contrast, type sizes, accessibility semantics (switch roles, announcing the quiet-hours reveal), and how the screen behaves on small phones or with large text. I judged from your description only, with no screenshot.
