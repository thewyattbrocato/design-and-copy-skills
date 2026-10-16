The panel is in good shape: the labels, 44px rows, focus ring, reduced-motion rule and the disabled-row explanation all work. I'd make these changes before release, most important first.

**1. The group has no accessible name.** `role="group"` only has a description, so screen readers announce an unnamed group.
```html
<div role="group" aria-labelledby="n-h" aria-describedby="n-d">
```

**2. The disabled row isn't dimmed.** `input:disabled+*` matches nothing, because the text `<span>` comes before the input. Only the checkbox fades, so "Product news" looks active.
```css
.row:has(input:disabled){opacity:.6}
```
Replace the `input:disabled+*,input:disabled{opacity:.6}` rule with this one.

**3. Long labels can squash the switch.** In the flex row, a long translated label can shrink the input.
```css
.row{align-items:center}
.row input{flex-shrink:0}
```

**4. The status line shifts the layout.** It's empty until a save happens, so "Saved" pushes content down. Reserve its height:
```css
.status{min-height:1.5em;margin:.75rem 0 0}
```

**Needs your JS, which I can't see**
- **Failed saves:** after "Couldn't save. Try again.", the switch still shows the unsaved value. Either revert it, or put a real Retry button next to the message. The text alone gives nothing to press.
- **Saving state:** write "Saving…" into the status region as soon as a switch is toggled, so there's feedback before the result arrives. Disable nothing, so people can keep toggling.

**Not checked**
- I only read the code. I didn't run it, use a screen reader, or check the panel against the page background in dark mode. `.panel` sets a text color but no background, so it depends on the host page.
