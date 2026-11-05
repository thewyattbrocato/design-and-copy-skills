# What's going on

The scan checks that things *have* names, contrast and valid ids. It can't check whether the step can be *operated* or whether its outcome is *announced*. A perfect score is compatible with a step that can't be completed. Several problems here are probably blocking her.

**Likely blockers**

1. **Time slots are `<div onclick>`.** They aren't focusable, have no role, and don't respond to Enter or Space. Keyboard and screen-reader users can't select a time at all. Even with a mouse or touch, the selected state (`.on`) is only a background colour, so nothing announces it.
2. **No feedback on booking.** `book()` only adds a green border. There's no text, no live region and no focus move, so a screen reader user gets no sign that anything happened. It also doesn't check that a time or party size was chosen, so there are no errors to hear either. She could press "book it" and not know whether it worked.

**Other problems the scan missed or passed**

3. **`aria-labelledby` on a plain `div`.** It has no role, so the name is ignored. The "label" is a `span`, which isn't associated with anything.
4. **Unavailable slot.** The 7:00 pm slot is "full" only through grey styling (`#bbb` is also well under 4.5:1 contrast). Assistive tech doesn't hear that it's unavailable.
5. **Accessible names that don't match visible text** (WCAG 2.5.3):
   - The input has a visible `<label>` "party size", but `aria-label="number of guests"` overrides it.
   - The button reads "book it" but is named "confirm reservation". Voice-control users saying "click book it" will fail.

   The scan counts both as passing because a name exists.

# What I'd change

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
  <input id="party" type="number" min="1" max="8" required aria-describedby="party-hint">
  <span id="party-hint">1 to 8 guests</span>

  <button class="go" type="button" onclick="book()">Book it</button>

  <div id="status" role="status" tabindex="-1"></div>
</section>

<script>
  function book(){
    const status = document.getElementById('status');
    const time = document.querySelector('input[name=time]:checked');
    const party = document.getElementById('party');
    if (!time) { status.textContent = 'Please choose a time.'; document.querySelector('input[name=time]').focus(); return; }
    if (!party.checkValidity()) { status.textContent = 'Please enter a party size from 1 to 8.'; party.focus(); return; }
    /* send request, then on success: */
    document.getElementById('step-time').classList.add('done');
    status.textContent = `Booked: table for ${party.value} at ${time.parentElement.textContent.trim()}.`;
  }
</script>
```

```css
.slot{display:inline-block;padding:10px 14px;border:1px solid #767676;cursor:pointer}
.slot:has(input:checked){background:#1b4f8a;color:#fff}
.slot:has(input:focus-visible){outline:3px solid #000;outline-offset:2px}
.slot.full{color:#595959;text-decoration:line-through;cursor:not-allowed}
.slot input{position:absolute;opacity:0}  /* hidden visually, still focusable */
```

**Why this works**
- Native radios give a role, arrow-key navigation, a "selected" state and a disabled state for free. The `fieldset` and `legend` give the group its name.
- Removing both `aria-label`s lets the visible text be the name, so speech users and screen reader users hear the same thing.
- The `role="status"` region announces validation errors and the confirmation. Errors move focus to the offending field. The green border stays as a secondary cue but is no longer the only signal.
- "Fully booked" is in the text, not just the colour.

# Verifying
Automated scans catch roughly a third of real issues. Before trusting this, I'd do these checks:
- Complete the booking with only the keyboard.
- Complete it with VoiceOver on Safari and NVDA on Firefox.
- Test voice control.
- Ask the customer to retry, if she's willing.

I'd also add a keyboard-and-screen-reader walkthrough of the booking flow to the release checklist.
