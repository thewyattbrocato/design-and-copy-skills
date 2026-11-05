Your scan only checks properties that a tool can detect in the markup, like whether names exist, contrast ratios, and ids. It can't tell whether a screen-reader user can operate the page. The time picker fails that test, and the scan says nothing about it.

## What's going wrong

1. **The time slots can't be used without a mouse.** They're `<div onclick>`, so they aren't focusable and don't respond to Enter or Space. They also have no role, so a screen reader announces them as plain text. She can't select a time, and that's almost certainly where the booking failed.
2. **The selected time is shown only by colour.** `.on` changes the background, but nothing exposes "selected" to assistive tech.
3. **The full slot looks disabled but isn't marked as unavailable.** It's just grey text. It also fails contrast (`#bbb` on white is about 1.9:1), which the scan missed.
4. **The group label does nothing.** `aria-labelledby` on a role-less `div` isn't reliably exposed, so the "pick your table time" label never reaches her.
5. **Two `aria-label`s override the visible text.** The input is announced as "number of guests" while the label says "party size". The button is announced as "confirm reservation" while it shows "book it". This breaks WCAG 2.5.3 (Label in Name), so voice-control users can't say what they see. The scan counts these as passing because a name exists.
6. **Nothing is announced after pressing the button.** `book()` doesn't validate that a time or party size was chosen. Its only feedback is a green border, which a screen reader doesn't convey. If she got that far, she got no confirmation or error.

## What I'd change

Use native controls. Radio buttons give you keyboard support, grouping, selected state and disabled state for free.

```html
<form class="step" id="step-time" novalidate>
  <h2>Choose a time</h2>

  <fieldset class="timepicker">
    <legend>Pick your table time</legend>
    <label class="slot"><input type="radio" name="time" value="18:00"> 6:00 pm</label>
    <label class="slot"><input type="radio" name="time" value="18:30"> 6:30 pm</label>
    <label class="slot full"><input type="radio" name="time" value="19:00" disabled> 7:00 pm <span class="sr-only">(fully booked)</span></label>
    <label class="slot"><input type="radio" name="time" value="19:30"> 7:30 pm</label>
  </fieldset>

  <label for="party">Party size</label>
  <input id="party" type="number" min="1" max="8" required>

  <button class="go" type="submit">Book it</button>

  <p id="status" role="status"></p>
</form>

<script>
  const form = document.getElementById('step-time');
  const status = document.getElementById('status');
  form.addEventListener('submit', e => {
    e.preventDefault();
    const time = form.querySelector('input[name=time]:checked');
    const party = form.party.value;
    if (!time) { status.textContent = 'Please choose a time.'; form.querySelector('input[name=time]:not(:disabled)').focus(); return; }
    if (!party || party < 1 || party > 8) { status.textContent = 'Enter a party size from 1 to 8.'; form.party.focus(); return; }
    /* send request, then: */
    form.classList.add('done');
    status.textContent = `Booked for ${time.parentElement.textContent.trim()}, party of ${party}.`;
  });
</script>

<style>
  .slot{display:inline-block;padding:10px 14px;border:1px solid #767676;cursor:pointer}
  .slot input{position:absolute;opacity:0}                         /* visually hidden but still focusable */
  .slot:has(input:checked){background:#1b4f8a;color:#fff}
  .slot:has(input:focus-visible){outline:3px solid #000;outline-offset:2px}
  .slot.full{color:#6b6b6b;text-decoration:line-through;cursor:default}
  .sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
  .step.done{border:3px solid #2a9d3f}
</style>
```

What this changes:
- The slots are real radios in a `fieldset`/`legend`, so they can be reached with the keyboard, grouped and labelled, and they report their selected state.
- The full slot is truly `disabled`, says "fully booked" in text, and has darker text that passes contrast.
- The extra `aria-label`s are gone, so the visible text is the accessible name.
- Validation errors and the success message go through a `role="status"` live region. Focus moves to the problem field on error.
- A focus indicator is added. The old CSS had none because nothing could take focus.

## Making the scan useful

- Test the flow yourself with the keyboard only (Tab, Space, Enter), then with VoiceOver on macOS or NVDA on Windows. Ten minutes of that would have caught every issue above.
- Ask the customer to retest, or ask her what she heard at the point she got stuck.
- Treat a 100 score as "no detectable rule violations", not as proof of usability. Automated scans typically catch only a minority of real accessibility problems.
