# What's going on

The scan only checks that things exist: a name, an alt, a contrast ratio. It can't check whether a control can be operated. Your time slots are the problem, and the scanner has no rule that catches them.

## Why she got stuck

1. **The time slots can't be reached or used.** They're `<div onclick>` elements. They have no role and no `tabindex`, and they don't respond to Enter or Space. A keyboard or screen reader user can't focus them, and the reader announces them as plain text, not as choices. She couldn't select a time, so she couldn't finish.
2. **The group label is ignored.** `aria-labelledby` on a `div` with no role is not reliably exposed. The `<span>` label is therefore disconnected, and she never hears "pick your table time" as a question.
3. **Selection is shown by colour only.** `.on` changes the background and nothing else. There's no `aria-checked` or `aria-pressed`, so even if she could activate a slot, she'd never hear which one is chosen.
4. **The full slot is only grey.** Nothing says "unavailable" to assistive tech. The grey text is also below contrast minimums, and the scan likely treats it as exempt.
5. **Booking gives no feedback.** `book()` adds a green border, which is visual only.
   - There's no confirmation message, no live region, and no focus change.
   - It also doesn't check that a time was picked.
   - She could press "book it" and hear nothing.
6. **Some accessible names don't match the visible text.**
   - The input has both a `<label>` ("party size") and an `aria-label` ("number of guests"). The `aria-label` wins, so the visible label is overridden.
   - The button shows "book it" but is named "confirm reservation". Voice-control users who say "click book it" won't match it.
   - Both pass the scan because a name exists. That's the check it makes.

## What I'd change

Use native controls instead of ARIA patches. A radio group gives you focus, arrow-key navigation, selected state, and disabled state without extra work.

```html
<section class="step" id="step-time" aria-labelledby="h-time">
  <h2 id="h-time">Choose a time</h2>

  <fieldset class="timepicker">
    <legend>Pick your table time</legend>
    <label class="slot"><input type="radio" name="time" value="18:00"> 6:00 pm</label>
    <label class="slot"><input type="radio" name="time" value="18:30"> 6:30 pm</label>
    <label class="slot full"><input type="radio" name="time" value="19:00" disabled> 7:00 pm (fully booked)</label>
    <label class="slot"><input type="radio" name="time" value="19:30"> 7:30 pm</label>
  </fieldset>

  <label for="party">Party size</label>
  <input id="party" type="number" min="1" max="8" required>

  <p id="err" role="alert"></p>
  <button type="button" class="go">Book it</button>
  <p id="status" role="status" tabindex="-1"></p>
</section>

<script>
  const $ = id => document.getElementById(id);
  document.querySelector('.go').addEventListener('click', () => {
    const time = document.querySelector('input[name=time]:checked');
    const party = $('party');
    $('err').textContent = '';
    if (!time) { $('err').textContent = 'Please choose a time.'; return; }
    if (!party.checkValidity() || !party.value) { $('err').textContent = 'Enter a party size from 1 to 8.'; party.focus(); return; }
    // send the request, then on success:
    $('step-time').classList.add('done');
    $('status').textContent = `Booked: ${time.value} for ${party.value} guests.`;
    $('status').focus();
  });
</script>
```

```css
.slot{display:inline-block;padding:10px 14px;border:1px solid #767676;cursor:pointer}
.slot:has(input:checked){background:#1b4f8a;color:#fff;font-weight:600}
.slot:has(input:focus-visible){outline:3px solid #000;outline-offset:2px}
.slot.full{color:#595959;cursor:not-allowed;text-decoration:line-through}
```

Notes on the changes:
- The slot inputs can stay visually styled, but don't `display:none` them, because that removes them from the keyboard and the accessibility tree.
- The selected slot is now announced as "checked" and also shown by weight, not by colour alone.
- Fully booked is stated in text, not just greyed out.
- I removed both redundant `aria-label`s, so the visible text is the accessible name.
- Errors and the confirmation are announced, and focus moves to the confirmation.

## Preventing this next time

- Test the flow yourself with the keyboard only (Tab, Space, Enter, arrows).
- Run it once with VoiceOver, since you're on a Mac, or NVDA.
- Treat the scan score as a floor. Automated tools catch roughly a third of WCAG issues, and custom widgets are where they miss most.
- Reply to the customer once it's fixed. She'd also be a good person to ask to retest.
