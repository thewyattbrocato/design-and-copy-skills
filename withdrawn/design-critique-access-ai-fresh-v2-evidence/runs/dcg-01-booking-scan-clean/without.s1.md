The scan passes because it only checks things a tool can verify, like names present, contrast and ids. Your problems are in behaviour and semantics, which it doesn't test. I haven't run this with a screen reader, so this comes from reading the markup.

## What blocks her

1. **The time slots can't be used without a mouse.** They're `<div onclick>`, so they aren't focusable, have no role, and don't respond to Enter or Space. A screen reader user can't reach or activate them, so she can't choose a time. This is almost certainly why she couldn't finish.
2. **The selected state is only visual.** `.on` changes the background colour, and nothing is exposed to assistive tech.
3. **The full slot is only grey text.** It isn't announced as unavailable. `#bbb` on white is about 1.9:1, so it's also hard to read. The scan likely exempts it as "disabled", but it isn't actually disabled.
4. **The group has no real label.** `aria-labelledby` on a plain `<div>` with no role is ignored, and the label is a bare `<span>`. She hears no question or context for the slots.
5. **The submit gives no feedback.** `book()` only adds a green border. A screen reader user gets no confirmation or error, and nothing stops her submitting with no time or party size chosen. Even if she got that far, she'd have no sign that it worked.

## Smaller problems the scan can't see

- `aria-label="number of guests"` overrides the visible label "party size". Voice-control users who say "party size" won't match it.
- `aria-label="confirm reservation"` on the button overrides the visible text "book it", which is the same mismatch (WCAG 2.5.3, Label in Name).

## What I'd change

Use native radio inputs. They give you focus, arrow-key navigation, selected state and disabled state without custom code.

```html
<section class="step" id="step-time">
  <h2>Choose a time</h2>

  <fieldset class="timepicker">
    <legend>Pick your table time</legend>
    <label class="slot"><input type="radio" name="time" value="18:00"> 6:00 pm</label>
    <label class="slot"><input type="radio" name="time" value="18:30"> 6:30 pm</label>
    <label class="slot full"><input type="radio" name="time" value="19:00" disabled> 7:00 pm (fully booked)</label>
    <label class="slot"><input type="radio" name="time" value="19:30"> 7:30 pm</label>
  </fieldset>

  <label for="party">Party size</label>
  <input id="party" type="number" min="1" max="8" required>

  <button type="button" class="go" onclick="book()">Book it</button>

  <p id="status" role="status" tabindex="-1"></p>
</section>

<script>
  function book(){
    const status = document.getElementById('status');
    const time = document.querySelector('input[name=time]:checked');
    const party = document.getElementById('party');
    if (!time) { status.textContent = 'Please choose a time.'; return; }
    if (!party.checkValidity() || !party.value) { status.textContent = 'Please enter a party size from 1 to 8.'; party.focus(); return; }
    /* send the request, then on success: */
    document.getElementById('step-time').classList.add('done');
    status.textContent = `Booked: ${time.value} for ${party.value}.`;
  }
</script>

<style>
  .slot{display:inline-block;padding:10px 14px;border:1px solid #767676;cursor:pointer}
  .slot:has(input:checked){background:#1b4f8a;color:#fff}
  .slot:has(input:focus-visible){outline:3px solid #000;outline-offset:2px}
  .slot.full{color:#595959;text-decoration:line-through;cursor:not-allowed}
  .step.done{border:3px solid #2a9d3f}
</style>
```

- **Selection:** the radios give the group a name and expose which time is checked. The "(fully booked)" text and `disabled` mean the full slot is announced as unavailable, not just coloured differently.
- **Visible focus:** I added a focus ring, which the original lacked.
- **Label mismatches:** removing both `aria-label`s lets the visible text be the accessible name.
- **Feedback:** the `role="status"` region announces errors and the success message. Make sure your real request handler also reports server failures there.

## Testing

- **Automated scans:** add axe or Lighthouse for a baseline, but don't rely on them. A score of 100 here coexisted with a flow that was unusable.
- **Keyboard:** complete the booking using only Tab, arrows, Space and Enter.
- **Screen reader:** do the same with VoiceOver (Safari) and NVDA (Firefox or Chrome).

If her setup differs, such as mobile TalkBack or VoiceOver on iOS, the radio approach should still work, but it's worth retesting there. It would also be worth asking her which device and screen reader she used.
