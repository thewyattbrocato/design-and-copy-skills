## What's going on

The scan checks that things have names, contrast, valid ids and so on. It can't tell whether a control can be operated or whether a state change is announced. The time picker fails on both counts. Automated scans typically catch only a fraction of real barriers.

**Probably what blocked her**
1. **The time slots aren't controls.** They're `<div onclick>`, so they can't be reached with Tab and have no role. They also don't respond to Enter or Space. A screen reader user can hear "6:00 pm" as plain text but can't select it. This stops the booking.
2. **The selection is only visible.** The chosen slot is shown by a blue background (`.on`). Nothing like `aria-checked` or `aria-pressed` says which slot is selected.
3. **"Full" is only grey text.** The 7:00 pm slot isn't marked unavailable. It's also `#bbb` on white, about 1.9:1 contrast, which should fail. Either the scanner treats the `full` class as disabled, or it missed it.
4. **Booking gives no feedback.** `book()` only adds a green border. Nothing is announced, focus doesn't move, and nothing checks that a time was chosen. She would hear nothing at all after pressing the button.

**Other defects**
5. `aria-labelledby` on a plain `<div>` with no role is ignored, so the group has no name. The `<span>` also isn't a real label.
6. The button's `aria-label="confirm reservation"` overrides the visible text "book it". The input's `aria-label="number of guests"` overrides the visible label "party size". Names that don't contain the visible text break WCAG 2.5.3 and make voice control ("click book it") fail. The input's `aria-label` also makes its `<label>` redundant.

## What I'd change

Use native radio buttons inside a fieldset. They give you keyboard support, roles, selected state and disabled state for free. Add a live region for the result.

```html
<section class="step" id="step-time">
  <h2>Choose a time</h2>
  <form id="booking" novalidate>
    <fieldset class="timepicker">
      <legend>Pick your table time</legend>
      <label class="slot"><input type="radio" name="time" value="18:00"> 6:00 pm</label>
      <label class="slot"><input type="radio" name="time" value="18:30"> 6:30 pm</label>
      <label class="slot full"><input type="radio" name="time" value="19:00" disabled> 7:00 pm (fully booked)</label>
      <label class="slot"><input type="radio" name="time" value="19:30"> 7:30 pm</label>
    </fieldset>

    <label for="party">Party size</label>
    <input id="party" name="party" type="number" min="1" max="8" required>

    <button type="submit" class="go">Book it</button>
    <p id="status" role="status" tabindex="-1"></p>
  </form>
</section>
<script>
  document.getElementById('booking').addEventListener('submit', async e => {
    e.preventDefault();
    const status = document.getElementById('status');
    const f = e.target;
    if (!f.time.value) { status.textContent = 'Please choose a time.'; return; }
    if (!f.party.checkValidity()) { status.textContent = 'Please enter 1 to 8 guests.'; f.party.focus(); return; }
    // await sendRequest(...)  and handle failure with an error message
    status.textContent = `Booked: ${f.time.value}, party of ${f.party.value}.`;
    document.getElementById('step-time').classList.add('done');
  });
</script>
<style>
  .slot{display:inline-block;padding:10px 14px;border:1px solid #767676;cursor:pointer}
  .slot:has(input:checked){background:#1b4f8a;color:#fff}
  .slot:has(input:focus-visible){outline:3px solid #000;outline-offset:2px}
  .slot.full{color:#595959;cursor:not-allowed;text-decoration:line-through}
  .step.done{border:3px solid #2a9d3f}
</style>
```

Notes on the fix:
- You can hide the radio visually, but don't use `display:none`. That removes it from the keyboard and the accessibility tree.
- Make sure the error and success text is also visible, not only announced. The `role="status"` region handles the announcement.
- After the change, test it yourself. Unplug the mouse and complete the booking with Tab, arrows, Space and Enter. Then run it with VoiceOver (Cmd+F5 on your Mac) and Safari or Chrome. Better still, ask the customer who reported it to try again.
