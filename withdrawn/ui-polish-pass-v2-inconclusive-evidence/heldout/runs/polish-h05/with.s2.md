This is mostly in good shape. Each switch has a name from its label, the 44px rows give a large tap target, the focus ring is visible, the disabled row gives a reason, and the live region and reduced-motion rule are in place. I'd make four small changes.

**HTML**
```html
<div role="group" aria-labelledby="n-h" aria-describedby="n-d">
```
The group had a description but no name, so screen readers announced it as an unnamed group.

**CSS**
```css
.row{display:flex;justify-content:space-between;align-items:center;gap:1rem;padding:.875rem 0;border-bottom:1px solid var(--line);min-height:44px}
.row input{flex-shrink:0;accent-color:var(--accent)}
.row:has(input:disabled){cursor:not-allowed}
.status{min-height:1.5em}
```
- **`align-items:center`:** the checkbox no longer sits at the top of the row.
- **`flex-shrink:0`:** a long label can't squash the control.
- **`accent-color`:** the checked state uses the same blue as the focus ring.
- **`cursor:not-allowed`:** the locked row gets a cursor that signals it's locked.
- **`min-height` on `.status`:** the layout doesn't jump when "Saved" appears.

**Needs a decision before release**

The injection script wasn't in what you sent, so I couldn't check it. These are the places an auto-save panel usually breaks:
- **Failure:** if a save fails, the switch still shows the new value, so it looks saved when it isn't. Either revert the switch or keep the message up with a Retry button. "Couldn't save. Try again." has nothing to press at the moment. The message should stay until the next attempt rather than fade out.
- **Saving:** show "Saving…" in the same status region as soon as a switch changes, and use "Saved" only after the response comes back.
- **Dark mode:** the panel sets text color but no background, so it relies on the page background. Check that it sits on a dark surface in dark mode, because `--muted` is a light grey there.

I only read the code. I didn't run it in a browser or test it with a screen reader.
