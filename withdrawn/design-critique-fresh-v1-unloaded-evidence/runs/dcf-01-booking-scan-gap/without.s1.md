The scan passes because it only checks what automated rules can detect. The real problems are in things it can't judge, and the three "review manually" notices are probably pointing at some of them. Here's what in your markup would block a screen reader user.

## Blockers

**1. The time slots aren't controls.**
`<div class='slot' onclick=...>` has no role, no name-as-control, no tabindex, and no key handler. For a screen reader user (and keyboard-only users):
- The slots aren't focusable, so she can't tab to them.
- They're announced as plain text, not as options or buttons.
- Enter and Space do nothing, because only `click` is wired up.

She can hear the times read out but can't select one. **This is almost certainly why she couldn't finish.** The form can't be completed without a time.

**2. Selected and taken states are visual only.**
- Selected is a thicker border, which is invisible to a screen reader. She can't tell what she picked.
- Taken is light grey with no `disabled` or `aria-disabled`, so "7:00 pm" sounds just as available as the others. It's also low-contrast by design, which the scan may have flagged as a notice instead of an error.

**3. The result is communicated only by border color.**
On success (`ok`, green border) or failure (`fail`, red border), no text is added and nothing is announced. She submits and hears nothing, so she can't tell whether the booking worked or the slot was lost. Even sighted users with color-vision deficiency would miss red versus green. This is a likely cause of "could not finish": she may have submitted successfully and not known, or failed and not known why.

## Smaller issues

- **`aria-label='Reserve'` on a button that says "Confirm table".** The accessible name no longer matches the visible label (WCAG 2.5.3 Label in Name). Voice-control users saying "click Confirm table" will fail, and screen reader users hear a different word than what's on screen. Remove the `aria-label`.
- **The time group has no label.** The picker has no name, so nothing says "choose a time". Party size has a label, but the time picker doesn't.
- **The `<select>` options have no `value` attributes.** This works, but set them explicitly.
- **Focus isn't managed after submit.** There's nowhere for the result message to land.

## Suggested fix

Use native radio inputs, which give you keyboard support, selected state, and grouping for free:

```html
<form id="slot-step">
  <label for="party">Party size</label>
  <select id="party">
    <option value="2">2</option>
    <option value="4">4</option>
    <option value="6">6</option>
  </select>

  <fieldset id="time-picker" class="picker">
    <legend>Choose a time</legend>
    <label class="slot"><input type="radio" name="time" value="18:00"> 6:00 pm</label>
    <label class="slot"><input type="radio" name="time" value="18:30"> 6:30 pm</label>
    <label class="slot taken"><input type="radio" name="time" value="19:00" disabled> 7:00 pm (unavailable)</label>
    <label class="slot"><input type="radio" name="time" value="19:30"> 7:30 pm</label>
  </fieldset>

  <button type="submit">Confirm table</button>

  <div id="booking-status" role="status"></div>
</form>
```

Then in the script:
- On success, set `#booking-status` text to something like "Table booked for 4 at 6:30 pm." Keep the green border if you like, but don't rely on it.
- On failure, set the text to "Sorry, 7:30 pm was just taken. Please choose another time." Use `role="alert"` for errors if you want them announced immediately, and move focus to the first available slot.
- Style `input:checked + …` or `.slot:has(input:checked)` for the selected state. Keep the thicker border, and the radio itself carries the state for assistive tech.

## Why the scan missed it

Automated scanners typically catch roughly a third of WCAG issues. They can verify that an attribute exists, but not that a `div` with `onclick` should have been a button, that a color change carries meaning, or that a dynamic outcome was announced. The three "review manually" notices are worth opening now. I'd guess they relate to the click handlers, the color-only status, and the grey text.

The most reliable check is to complete the booking yourself with a screen reader (VoiceOver on Mac, NVDA on Windows) and keyboard only. Ideally, ask the customer who reported it to re-test after the fix.
