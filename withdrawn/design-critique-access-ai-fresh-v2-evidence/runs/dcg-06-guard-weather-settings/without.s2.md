The structure is solid. The `fieldset`/`legend` for the radios, the explicit `for`/`id` pairs, and the heading hierarchy are all correct. The main problem is the buttons.

**1. The destructive button (the main issue)**
"Save changes" and "reset app and clear saved places" look identical and sit side by side. In a narrow column they'll be close together, and on a phone they'll be a thumb-width apart. Someone aiming for Save can easily wipe their saved places. Suggested fixes:
- Move the reset out of `.actions` into its own "Danger zone" or "Data" section at the bottom, away from Save.
- Style it differently, for example an outline or red treatment, and make Save the only primary button.
- Add a confirmation step, such as a dialog that says "This will delete 4 saved places. This can't be undone."
- Say exactly what it does. "Reset app" and "clear saved places" are two different things. Either split them or use one clear label like "Delete saved places and reset settings".
- Add `type="button"` to both buttons so they don't submit a form if you wrap this in one later.

**2. Dependent controls**
"Summary time" stays active when "daily summary" is unchecked. Disable it (or hide it) until the box is checked, and consider moving it under that checkbox so the relationship is visible.

**3. Feedback on save**
Nothing tells the user their changes saved. Add a status message in an `aria-live="polite"` region, or switch to autosave and drop the button. If you keep the button, consider disabling it until something has changed.

**4. Location**
- Say what happens when it's off. Is there a way to pick a location manually?
- Handle the browser permission being denied. The checkbox shouldn't look "on" if permission was refused.
- A short line of helper text about why you need location would help.

**5. Layout and touch targets**
- Make each checkbox and radio row at least about 44px tall, with the whole label clickable. It is already clickable because of the wrapping label, so this is just padding.
- Put `label` and `select` on separate lines or use a consistent row layout. As written, the bare labels and inputs may run together inline.
- Stack the buttons vertically at narrow widths, full width, with Save on top.

**6. Smaller points**
- The `<option>` elements have no `value` attributes, so you'll be storing display text like "km/h". Use stable values such as `kmh`, `mph` and `ms`.
- The inputs have no `name` attributes, except the radios' `t`. Rename `t` to `temperature` so it's readable.
- Consider whether wind units should default based on the temperature choice or the user's locale.
- Notifications usually need a browser or OS permission. If "severe weather alerts" is on by default, make sure the permission prompt and its denied state are handled.
- `<section>` only becomes a landmark if it has an accessible name. Add `aria-labelledby` pointing at each `h2` if you want that.

If you only do one thing, separate and confirm the reset button. The rest is polish.
