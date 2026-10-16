**Why it looks like a blob:** every element gets the same `margin-bottom: 16px`, so the space between a label and its own input is identical to the space between one field and the next. Nothing says which label belongs to which input, and nothing separates the field groups. Proximity is the main way people see grouping, and you've removed all of it. Two other things add to the effect:

- The 16px gap between a label and its input is big enough to loosen the pair.
- The button and the heading get the same spacing as the fields, so they have no distinct role.

**What I'd change:**

1. **Group each label and input as a unit.** Keep them tight (about 4–6px apart), and put more space (about 20–24px) between units.
2. **Group related fields.** Your fields fall into three sets: identity (name, email, postcode), riding (level), and emergency (contact, phone). Use `<fieldset>` and `<legend>`, or extra space between sets, so the form reads as short chunks instead of six fields in a row.
3. **Give the heading and button their own spacing.** The heading needs more room below it, and the button needs more room above it.
4. **Fix the markup.** The labels aren't connected to the inputs. Wrap each pair in a `div`, and use `for`/`id` (or wrap the input in the label) so clicking a label focuses its field and screen readers announce it.

```html
<form>
  <h2>Join the Larkspur Cycling Club</h2>

  <fieldset>
    <legend>About you</legend>
    <div class="field"><label for="name">Full name</label><input id="name"></div>
    <div class="field"><label for="email">Email</label><input id="email" type="email"></div>
    <div class="field"><label for="postcode">Home postcode</label><input id="postcode"></div>
  </fieldset>

  <fieldset>
    <legend>Riding</legend>
    <div class="field"><label for="level">Ride level</label><select id="level"></select></div>
  </fieldset>

  <fieldset>
    <legend>Emergency contact</legend>
    <div class="field"><label for="ec-name">Name</label><input id="ec-name"></div>
    <div class="field"><label for="ec-phone">Phone</label><input id="ec-phone" type="tel"></div>
  </fieldset>

  <button>Join the club</button>
</form>
```

```css
form h2     { margin: 0 0 24px; }
fieldset    { border: 0; padding: 0; margin: 0 0 32px; }
legend      { font-weight: 600; margin-bottom: 12px; padding: 0; }
.field      { margin-bottom: 20px; }
.field:last-child { margin-bottom: 0; }
label, input, select { display: block; }
label       { margin-bottom: 4px; }
button      { margin-top: 8px; }
```

The rule is that the gap inside a unit is smaller than the gap between units, and the gap between groups is larger again. That gives you three clear levels of spacing: 4px, 20px and 32px. Using one margin everywhere gives you only one level.

I've also renamed "Emergency contact" and "Contact phone" to "Name" and "Phone" under an "Emergency contact" legend. That's optional, but it removes the ambiguity of a bare "Contact phone" label.
