**Why it looks like a blob:** Every element gets the same 16px bottom margin, so the spacing is uniform. That means nothing tells the eye which things belong together. A label is just as far from its own input as it is from the next field's label. Proximity is how people group things, and here it says everything is equally related to everything else.

Two specific effects:
- The label→input gap (16px) equals the input→next-label gap (16px), so labels float between fields and it's ambiguous which input they belong to.
- The heading, the fields, and the button are all spaced the same, so there are no sections or hierarchy. The two different kinds of information (personal details vs. emergency contact) run together.

**What I'd change:** Make the spacing unequal on purpose: tight within a group, loose between groups.

```html
<form>
  <h2>Join the Larkspur Cycling Club</h2>

  <div class="field">
    <label for="name">Full name</label>
    <input id="name">
  </div>
  <div class="field">
    <label for="email">Email</label>
    <input id="email">
  </div>
  <div class="field">
    <label for="postcode">Home postcode</label>
    <input id="postcode">
  </div>
  <div class="field">
    <label for="level">Ride level</label>
    <select id="level"></select>
  </div>

  <fieldset>
    <legend>Emergency contact</legend>
    <div class="field">
      <label for="ec-name">Name</label>
      <input id="ec-name">
    </div>
    <div class="field">
      <label for="ec-phone">Phone</label>
      <input id="ec-phone">
    </div>
  </fieldset>

  <button>Join the club</button>
</form>
```

```css
form > h2   { margin-bottom: 24px; }
.field      { margin-bottom: 20px; }
label       { display: block; margin-bottom: 4px; }   /* tight: label belongs to its input */
input, select { display: block; width: 100%; }
fieldset    { margin: 32px 0 0; padding: 0; border: 0; }  /* loose: new section */
legend      { font-weight: 600; margin-bottom: 12px; padding: 0; }
button      { margin-top: 32px; }
```

The key ratios are roughly 4px (label to input), 20px (between fields), and 32px (between sections). Also:

- **Group the emergency contact.** "Emergency contact" and "Contact phone" are really one unit, so a `fieldset` with a legend makes that explicit. I relabeled them "Name" and "Phone" since the legend now supplies the context.
- **Add `for`/`id` pairs** so clicking a label focuses its input, which also helps screen readers.
- **Give the button extra space above it** so it reads as the final action, not just another field.

The exact numbers matter less than the principle: spacing should encode relationships, so a single uniform margin will always flatten them.
