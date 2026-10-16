**Why it looks like a blob**

Every child gets `margin-bottom: 16px`, so the gap after a label (before its own input) is the same as the gap after an input (before the next label). Nothing is closer to anything else, so the eye can't pair labels with fields or see sections. You get 13 evenly spaced items in a column.

Two smaller side effects:
- The heading has the same space below it as everything else, so it doesn't read as a title.
- The button gets a trailing 16px margin, and the last child always adds a stray gap at the bottom.

**What I'd change**

1. **Make the space inside a group smaller than the space between groups.** A label and its input are one unit, so they should sit about 4–8px apart. Each label+input pair should sit about 16–24px from the next pair.
2. **Group the fields into sections.** There are two natural groups: "About you" (name, email, postcode, ride level) and "Emergency contact" (contact name, phone). Put 32px or more between sections and keep the pairs tighter than that.
3. **Put the gap on the parent instead of on every child.** Use `gap` on the container and wrap each label+input in a div. That also removes the trailing margin on the last item.
4. **Use less space under the heading than above.** Give the heading about 8px above its content's start, with the form padding or section gap above it.
5. **Give the button extra space above it** (about 32px) so it reads as the final action, and pad it about twice as much horizontally as vertically.
6. **Don't box each section.** Space alone is enough here. Use a hairline rule or a tint only if you later find the sections still don't separate.

**Markup**

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
    <div class="field"><label for="ec-name">Emergency contact</label><input id="ec-name"></div>
    <div class="field"><label for="ec-phone">Contact phone</label><input id="ec-phone"></div>
  </fieldset>

  <button>Join the club</button>
</form>
```

**CSS**

```css
form {
  display: flex;
  flex-direction: column;
  gap: 32px;              /* between sections */
}

form > h2 { margin: 0 0 -16px; }   /* heading pulls closer to the first section */

fieldset {
  display: flex;
  flex-direction: column;
  gap: 16px;              /* between fields */
  border: 0;
  padding: 0;
  margin: 0;
}

legend { padding: 0; margin-bottom: 16px; font-weight: 600; }

.field {
  display: flex;
  flex-direction: column;
  gap: 4px;               /* label to its input */
}

input, select { padding: 8px 12px; }

button {
  align-self: flex-start;
  padding: 12px 24px;
}
```

The spacing now uses four steps (4, 16, 32, plus the 8/12/24 padding values). The relationships are label→input at 4px, field→field at 16px, and section→section at 32px, so the groups should show when you squint at it.

I also made two content suggestions:
- **Rename the second group's first field** to "Contact name". "Emergency contact" is now the legend, so the label would repeat it.
- **Use `for`/`id` pairs** on the labels, which I included above. Your original labels weren't tied to their inputs, which hurts accessibility and click-to-focus.
