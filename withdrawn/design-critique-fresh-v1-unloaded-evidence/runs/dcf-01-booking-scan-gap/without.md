Automated scanners only catch a fraction of accessibility problems (roughly a third, by common estimates). The perfect score is real, but it measures only what a tool can check, and the three unreviewed "review manually" notices are very likely pointing at the problems below.

**What blocks her in this markup**

1. **The time slots aren't operable (the likely blocker).** They're `<div onclick>` elements. They have no role, aren't focusable, and don't respond to keyboard. A screen reader user (who is usually navigating by keyboard or by touch gestures) can't reach them or activate them, so she can't choose a time. Fix: use real controls, e.g. `<button type="button">` per slot, or a radio group (`<fieldset><legend>Time</legend>` with `<input type="radio">` and labels). Radios are a natural fit, since this is a single choice.

2. **Taken slots aren't communicated.** `.taken` is only light grey. Use `disabled` (or `aria-disabled="true"`) on the control, and ideally include text like "7:00 pm, unavailable".

3. **The selected state is visual only.** A thicker border tells a screen reader user nothing. Radios give you checked state for free. With buttons, use `aria-pressed="true"` or `aria-checked`, depending on the pattern.

4. **The result is never announced.** On success the border turns green, and on failure it turns red, with no text added. She submits and hears nothing, so she can't tell whether the booking worked or the slot was taken. This probably explains "could not finish". Add a message in a live region (`role="status"` for success, `role="alert"` for failure) that says, for example, "Booking confirmed for 6:30 pm" or "Sorry, that time was just taken. Please choose another." Don't rely on color alone either (this is also a WCAG 1.4.1 issue for sighted colorblind users). On failure, move focus to the message or back to the time group.

5. **The button's accessible name doesn't match its label.** `aria-label='Reserve'` overrides the visible text "Confirm table". That fails WCAG 2.5.3 (Label in Name), so voice-control users saying "click Confirm table" won't hit it, and it's confusing for screen reader users. Remove the `aria-label`.

6. **Smaller items:**
   - The party-size `<select>` has a label, which is fine. Add `name` attributes so the form data is valid.
   - Group the time options with a fieldset/legend or `role="radiogroup"` and an accessible name.
   - `.picker` is a div with no semantics, so it gives no context.

**Sketch of a fix**

```html
<form id="slot-step">
  <label for="party">Party size</label>
  <select id="party" name="party">…</select>

  <fieldset id="time-picker">
    <legend>Time</legend>
    <label><input type="radio" name="time" value="18:00"> 6:00 pm</label>
    <label><input type="radio" name="time" value="18:30"> 6:30 pm</label>
    <label><input type="radio" name="time" value="19:00" disabled> 7:00 pm (unavailable)</label>
    <label><input type="radio" name="time" value="19:30"> 7:30 pm</label>
  </fieldset>

  <div id="result" role="status"></div>
  <button type="submit">Confirm table</button>
</form>
```

The script then writes the success or failure text into `#result` (use `role="alert"` for the failure message, or swap the role).

**Process takeaways**

- Work through the three "review manually" notices. They're probably flagging some of the items above.
- Test with a real screen reader (NVDA, VoiceOver) and keyboard-only navigation. Ten minutes tabbing through this step would have found the problem.
- Ask the customer for details if she's willing. I'm inferring from the markup, and her account would confirm which of these she hit first.
