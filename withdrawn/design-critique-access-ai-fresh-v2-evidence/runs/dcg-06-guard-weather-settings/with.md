**The page is clear and well-structured, but the action row is a real problem.** A destructive reset button sits next to Save and looks the same.

## Findings, in priority order

1. **Blocker: "reset app and clear saved places" looks identical to "save changes" and sits beside it.**
   - Both use `.btn` and are side by side in a narrow column. Someone reaching for Save with a thumb can hit the wrong one, and the reset wipes their saved places.
   - The reset label is also much longer than "save changes", so in a narrow column it will probably wrap to two lines. That makes the two buttons uneven.
   - **Fix:**
     - Make Save the only primary button.
     - Move reset out of the action row, to the bottom of the page under its own "reset" heading.
     - Style reset as a quiet, danger-coloured text button.
     - Add a confirmation that names what will be lost, such as "Delete 4 saved places?", with a cancel that is the default.

2. **Moderate: the summary time field stays live when "daily summary" is unchecked.**
   - It is unchecked by default, yet the time input shows 07:30 and can be edited. That suggests a summary will arrive at that time, and it won't.
   - **Fix:** disable or hide `#when` until the checkbox is on. If you disable it, keep the value so it comes back when re-enabled.

3. **Moderate: the location toggle has no fallback and no explanation.**
   - Unchecking "use my current location" leaves nothing to do next, such as choosing a place. Nothing says what happens if the browser denies permission.
   - **Fix:** when it's off, reveal a place search or the saved-places list. When permission is denied, show a short line saying so.

4. **Minor: there is no sign that Save worked, and no hint that changes are pending.**
   - Every control looks like it applies instantly, but a Save button implies it doesn't. People may leave without saving.
   - **Fix:** show a "Saved" confirmation. Optionally keep Save disabled until something changes.

5. **Minor, mostly taste: the units controls are inconsistent.**
   - Temperature uses radios, while wind uses a select with only three options. Radios would make all three visible at once and save a tap.
   - The all-lowercase headings are fine if that's your brand voice.

## What works and should stay
- **`fieldset` and `legend` for the temperature radios.** Screen readers announce the group, and the radios share a name.
- **Every control has a label.** The `for`/`id` pairs and the wrapping labels mean the whole label text is clickable.
- **Three plain sections in a sensible order.** Units, alerts and location each have one clear heading, so the page is easy to scan in a single column.
- **Sensible defaults.** Severe alerts are on and the daily summary is off, so nothing noisy is on by default.

*Assumptions: this is a mobile-first, high-fidelity screen for existing users. Not checked: contrast, tap-target sizes and focus styles, because no CSS was supplied.*
