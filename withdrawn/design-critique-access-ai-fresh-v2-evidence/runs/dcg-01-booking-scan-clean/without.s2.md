## What's going on

The scan only checks static rules, such as whether names exist, contrast, and ids. It can't tell whether the controls work without a mouse. Your time slots are `<div onclick>` elements, so a screen reader user can't operate them, and without a time she can't finish a booking.

**Blockers**
- **Slots can't be reached or activated.** A `div` isn't focusable, has no role, and has no key handler. Keyboard and screen reader users can't tab to a time or select one. This is almost certainly why she got stuck.
- **Selection is invisible to her.** The chosen slot is shown only by a CSS background colour. There's no `aria-checked` or `aria-pressed`, so nothing tells her a time is selected.
- **"Full" is only a grey colour.** The 7:00 pm slot is announced the same as the others, with no "unavailable".
- **The result is silent.** `book()` only adds a green border. Nothing is announced, focus doesn't move, and no text says "booked". It also marks the step done before the request succeeds, and it doesn't check that a time or party size was chosen.

**Other problems**
- `aria-labelledby` on a plain `div` with no role is unreliable. The group name can be dropped, and the `span` isn't a real label anyway.
- The party size input has `<label>party size</label>`, but `aria-label="number of guests"` overrides it. The spoken name no longer matches the visible text (WCAG 2.5.3 Label in Name).
- The button's `aria-label="confirm reservation"` has the same mismatch with the visible "book it". Voice-control users saying "click book it" will fail.
- There are no visible focus styles.

## What I'd change

Use native controls, so the browser supplies the semantics and keyboard behaviour. Radio buttons fit "choose one time" well.

```html
<section class="step" id="step-time">
  <h2>Choose a time</h2>

  <fieldset>
    <legend>Pick your table time</legend>
    <label><input type="radio" name="time" value="18:00"> 6:00 pm</label>
    <label><input type="radio" name="time" value="18:30"> 6:30 pm</label>
    <label><input type="radio" name="time" value="19:00" disabled> 7:00 pm (fully booked)</label>
    <label><input type="radio" name="time" value="19:30"> 7:30 pm</label>
  </fieldset>

  <label for="party">Party size</label>
  <input id="party" type="number" min="1" max="8" required>

  <button class="go" type="button" onclick="book()">Book it</button>

  <p id="status" role="status"></p>
</section>
<script>
  async function book(){
    const status = document.getElementById('status');
    const time = document.querySelector('input[name=time]:checked');
    const party = document.getElementById('party');
    if (!time) { status.textContent = 'Please choose a time.'; return; }
    if (!party.checkValidity()) { status.textContent = 'Please enter a party size from 1 to 8.'; party.focus(); return; }
    try {
      await sendRequest(time.value, party.value);   // your real call
      status.textContent = `Booked for ${time.value}, party of ${party.value}.`;
      document.getElementById('step-time').classList.add('done');
    } catch {
      status.textContent = 'Sorry, the booking failed. Please try again.';
    }
  }
</script>
```

CSS to go with it:
- Style the selected state with `input:checked + …` or wrap the text in a `span`. Don't rely on colour alone, for example add a check mark or a bolder border.
- Keep a visible `:focus-visible` outline.
- Show "fully booked" as text, as above, not only as grey.
- Add a text confirmation next to the green border, which the status message already does.

## Next steps
- Test with a real screen reader (VoiceOver, NVDA) and with keyboard only (Tab, arrow keys, Space). I haven't run anything here, so this diagnosis comes from reading the markup.
- Ask her what she heard at each step if she's willing, to confirm the diagnosis.
- Treat the 100/100 score as a baseline. Automated scans catch only a minority of accessibility problems, so add a manual keyboard pass to your release checklist.
