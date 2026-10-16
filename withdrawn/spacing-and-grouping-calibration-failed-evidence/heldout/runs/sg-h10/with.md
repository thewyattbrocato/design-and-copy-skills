**Why it looks like a blob**

`form > * { margin-bottom: 16px }` gives every element the same gap, so the label→input gap (which should be small) equals the input→next-label gap (which should be large). Nothing says which label belongs to which input. A label floats at the same distance from the field above it as from its own field, so the form reads as 13 evenly spaced lines. The `<h2>` has the same problem: it sits as far from the first label as from anything else, and the button has no more separation than a field does.

Consistent margins aren't the same as consistent relationships. The same relationship should get the same space, and different relationships should get different space.

**What I'd change**

1. **Map the relationships:**
   - Label + input form a unit, with a tight gap of about 4–8px.
   - Units are siblings, with a larger gap of about 16–24px.
   - "You" (name, email, postcode, ride level) and "Emergency contact" (name, phone) are two natural groups, separated by about 32px.
   - The button is the action, so it gets extra space above it.
2. **Let the parent own the gap** instead of putting a bottom margin on every child. This also stops the last item from adding stray space.
3. **Wrap each label and input in a `div`, and group the sections with `fieldset` and `legend`.** That makes the groups explicit for CSS, and it also helps screen readers. The emergency contact fields are the obvious group.
4. **Tie each label to its input** with `for`/`id`, or by nesting the input inside the label. This is accessibility, and it also makes the label clickable.
5. **Use a small scale** (4, 8, 16, 32) instead of one-off values.

```html
<form>
  <h2>Join the Larkspur Cycling Club</h2>

  <fieldset>
    <legend>About you</legend>
    <div class="field"><label for="name">Full name</label><input id="name"></div>
    <div class="field"><label for="email">Email</label><input id="email"></div>
    <div class="field"><label for="postcode">Home postcode</label><input id="postcode"></div>
    <div class="field"><label for="level">Ride level</label><select id="level"></select></div>
  </fieldset>

  <fieldset>
    <legend>Emergency contact</legend>
    <div class="field"><label for="ec-name">Name</label><input id="ec-name"></div>
    <div class="field"><label for="ec-phone">Phone</label><input id="ec-phone"></div>
  </fieldset>

  <button>Join the club</button>
</form>
```

```css
form {
  display: flex;
  flex-direction: column;
  gap: 32px;              /* between groups */
  max-width: 28rem;
}
h2 { margin: 0; }

fieldset {
  display: flex;
  flex-direction: column;
  gap: 16px;              /* between fields */
  border: 0;
  padding: 0;
  margin: 0;
}
legend { padding: 0; margin-bottom: 16px; font-weight: 600; }

.field { display: flex; flex-direction: column; gap: 4px; }  /* label to input */

input, select { padding: 8px 12px; }
button { align-self: flex-start; padding: 12px 24px; }
```

The result is label→input at 4px, field→field at 16px, group→group at 32px. That's roughly 1 : 4 : 8, so the groups show up without any boxes, borders or cards. If you want one more cue, make the legends slightly bolder. I wouldn't wrap the groups in cards, because space alone should be enough here.

Two smaller notes:
- I renamed the emergency fields to "Name" and "Phone" because the legend now supplies the "Emergency contact" context. If you'd rather keep your original labels, that works too.
- The button's padding is about twice as wide as it is tall, which is a comfortable proportion. It's also taller than 44px with the default line height, so it's easy to tap.
