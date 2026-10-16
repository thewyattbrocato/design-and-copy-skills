**Why it's a blob:** Your rule gives every element the same 16px bottom margin, so the spacing carries no information. Each label sits 16px from its own input, and each input sits 16px from the next label. Proximity is how people see grouping, and here "label → its input" and "input → next field" are equal distances. The label doesn't look attached to its field, and the fields don't look separate from each other. The `h2` and the button get the same gap too, so nothing stands out as a heading or an action. There's also no grouping between the two kinds of information (who you are vs. who to call in an emergency).

**What I'd change:**

1. **Tight inside a field, loose between fields.** Wrap each label/input pair in a div (or use a `fieldset`-style group). Use about 4–6px between label and input and about 20–24px between fields.
2. **Group related fields.** Put the first four under "About you" and the last two under "Emergency contact," with more space (about 32–40px) between groups. Then you can shorten the labels to "Name" and "Phone" inside the emergency group.
3. **Give the button its own space.** Add extra top margin (about 24–32px) so it reads as the end of the form.
4. **Make the heading clearly bigger and farther from the form.** For example, 24px below it.
5. **Style the controls.** Add visible borders, padding, and a consistent width so the inputs read as boxes and the labels read as small text above them.

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
form { max-width: 420px; }
h2 { margin: 0 0 24px; }

fieldset { border: 0; padding: 0; margin: 0 0 36px; }
legend { font-weight: 600; margin-bottom: 12px; padding: 0; }

.field { margin-bottom: 20px; }
.field:last-child { margin-bottom: 0; }

label { display: block; margin-bottom: 6px; font-size: 14px; }
input, select {
  display: block; width: 100%; box-sizing: border-box;
  padding: 8px 10px; border: 1px solid #bbb; border-radius: 4px;
}

button { margin-top: 4px; padding: 10px 20px; }
```

The labels now have `for`/`id` pairs, which also makes clicking a label focus its input and helps screen readers. Your original markup didn't have that connection.

The general rule is to make the spacing vary on purpose: small gaps within a unit, medium gaps between units, and large gaps between sections. When every gap is the same, the eye has nothing to group by.
