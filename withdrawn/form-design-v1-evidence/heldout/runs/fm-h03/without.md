I'd go with a variation of the third option: a stepper for travelers and radio cards for room type. Neither a dropdown nor plain radios fits both fields.

**Number of travelers (1–8): stepper**
- It's a small count, so people expect to nudge it up or down instead of picking from a list.
- It's faster than a dropdown. Most bookings are 1–4 travelers, so that's one or two taps.
- The bounds are easy to enforce: disable "−" at 1 and "+" at 8. Show the current value between the buttons.
- Make the number itself an editable input (`inputmode="numeric"`) or at least keep the buttons at least 44px. Don't make the stepper buttons the only way to change the value.
- Radios would work for 8 options, but they take up a lot of space for little gain. A dropdown hides a value that most people just want to see.

**Room type (3 choices): radio cards**
- Three mutually exclusive options is the classic case for radios, and they should all be visible at once so people can compare them.
- Room type is a decision, not just a value. Cards let you show a price, a one-line description, and maybe a photo for each room. A bare "Standard / Deluxe / Suite" dropdown can't do that.
- Pre-select Standard so the form is valid by default, or leave it unselected if you'd rather force a deliberate choice.
- Build them as real `<input type="radio">` elements inside a `<fieldset>` with a `<legend>`. Style the label as the card, and keep the focus ring and arrow-key navigation.

**Why not the other proposals**
- **Dropdowns for both:** this hides the options and takes two clicks. It also hurts the room choice, where comparing options matters. It's a reasonable fallback if the form is very space-constrained, and native selects are good on mobile.
- **Radios for both:** this is fine for room type. For travelers, eight radio buttons is clutter.

**Caveats**
- If room capacity depends on traveler count (e.g. a Standard room sleeps 2), the stepper should update the room cards. Mark rooms as unavailable, or show "2 rooms needed", instead of letting people hit an error on submit.
- If you have more than 8 travelers, send those users to a group-booking flow or contact link when they reach the max.
- If the design system doesn't have a stepper or card component, or you're short on time, a plain `<select>` for travelers and standard radios for room type is a perfectly good v1. The main thing is to avoid dropdowns for the room choice.
