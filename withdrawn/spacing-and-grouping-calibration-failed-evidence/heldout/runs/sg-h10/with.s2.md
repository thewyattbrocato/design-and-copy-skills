**Why it looks like a blob**

`form > * { margin-bottom: 16px }` gives every element the same gap, so the label-to-input gap (16px) equals the field-to-field gap (16px). Nothing tells the eye that a label belongs to its input, so the form reads as 13 evenly spaced items instead of 6 fields plus a heading and a button. Spacing is how a layout shows grouping, and uniform spacing shows none.

Smaller problems:
- The heading has the same space below it as everything else, so it doesn't attach to the form, and the button isn't set apart as the final action.
- Margin on every child means the last item adds a stray 16px at the bottom.
- The two emergency-contact fields are related to each other but look like any other two fields.

**What I'd change**

Make the space inside a group much smaller than the space between groups. Let the container own the gaps, and wrap each label and input in a wrapper.

```html
<form>
  <h2>Join the Larkspur Cycling Club</h2>

  <div class="field"><label for="name">Full name</label><input id="name"></div>
  <div class="field"><label for="email">Email</label><input id="email"></div>
  <div class="field"><label for="postcode">Home postcode</label><input id="postcode"></div>
  <div class="field"><label for="level">Ride level</label><select id="level"></select></div>

  <fieldset>
    <legend>Emergency contact</legend>
    <div class="field"><label for="ec-name">Name</label><input id="ec-name"></div>
    <div class="field"><label for="ec-phone">Phone</label><input id="ec-phone" type="tel"></div>
  </fieldset>

  <button>Join the club</button>
</form>
```

```css
form {
  display: flex;
  flex-direction: column;
  gap: 24px;            /* between fields */
  max-width: 28rem;
}
h2 { margin: 0 0 8px; } /* extra 8px on top of the 24px gap, so the heading sits ~32px from the first field */
.field { display: flex; flex-direction: column; gap: 4px; }  /* label hugs its input */
fieldset { border: 0; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 24px; }
legend { padding: 0; margin-bottom: 8px; }
button { align-self: flex-start; margin-top: 8px; padding: 12px 24px; }
```

Why these choices:
- **Label to input is 4px, field to field is 24px.** That's a 6:1 ratio, so each pair reads as a unit. Even 8px vs 24px would work.
- **Gaps come from the container** (`gap`), not from margins on each child, so there's no extra space after the last item.
- **The emergency contact is a real `fieldset` with a `legend`.** It groups the two fields semantically, which also helps screen readers. I renamed the labels to "Name" and "Phone" because the legend now supplies the context. If you'd rather keep the flat list, use a larger gap (say 40px) before the group.
- **The button gets a little extra room above it** and padding of about 2:1 horizontal to vertical, so it reads as the final action.
- **No cards, borders or tinted boxes.** Space alone is enough for a form this small. Add a hairline above the emergency section only if you later add more sections.
- **Label `for` and input `id` pairs** make clicking a label focus its field.

Keep every gap on one small scale (4, 8, 24 here) so the spacing stays consistent as the form grows.
