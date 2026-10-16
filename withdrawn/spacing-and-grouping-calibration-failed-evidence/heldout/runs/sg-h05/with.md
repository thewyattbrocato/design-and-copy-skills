The label spacing is the one thing I'd fix before you merge.

**Must fix**

- **`.field label { margin-bottom: 24px }`** is backwards. The label sits 24px from its own input, but fields are only 12px apart. So a label looks closer to the field above it than to its own input. Spacing inside a group should be about half the spacing between groups, or less. Try 6–8px under the label and 20–24px between fields.
- **`.field { margin-bottom: 12px }`** is too tight for the same reason. Once the label gap drops, 12px between fields won't separate them. Raise it to about 20–24px.

**Should fix**

- **Off-scale values.** Most of the file sits on a 4/8/12/24 scale, but a few values don't:
  - `gap: 6px` in `.amounts` → 8px
  - `padding: 0 10px` on the input → 12px
  - `margin: 10px 0 0` on `.fineprint` → 8px or 12px
- **Touch targets.** The amount buttons are 36px tall with 6px between them. If this will be used on phones, make them 44px tall (the submit button already is) with an 8px gap.
- **Bottom margins on every field.** The last field leaves a stray margin, and it stacks with `.amounts` margin-top. Put the spacing on the parent instead, for example `.pledge form { display: grid; gap: 24px; }`. I can't see your HTML, so check how this plays out in the real markup.

**Already fine**

- The heading and intro spacing (12px, then 24px to the form) groups correctly.
- `.hint` at 4px reads as attached to its input.
- `.amounts` has more space after it (24px) than inside it, so it reads as one cluster.
- The submit button has enough room above it and a good height.

**Suggested changes**

```css
.field { margin-bottom: 24px; }          /* or parent gap */
.field label { display: block; margin-bottom: 8px; font-weight: 600; }
.field input { width: 100%; height: 40px; padding: 0 12px; }
.amounts { display: flex; gap: 8px; margin: 12px 0 24px; }
.amounts button { height: 44px; padding: 0 16px; }
.fineprint { margin: 8px 0 0; font-size: 12px; }
```

I haven't seen it rendered, so squint at it in the browser once. Each label should clearly belong to its input, and the fields should read as separate units.
