The motion is in good shape. The durations are short, the entrance uses an ease-out curve, the exit is faster than the entrance, the movement is subtle, and your reduced-motion handling keeps a fade instead of removing feedback. I'd change two small things before shipping.

**1. The button press has no transition.**
`.confirm-btn` only transitions `background-color`. The `:active` scale therefore snaps in and snaps back, which can feel jumpy next to the smooth modal. Add transform to the transition:

```css
.confirm-btn { transition: background-color 120ms ease-out, transform 100ms ease-out; }
```

**2. The closed modal is still reachable.**
This is about the exit more than the motion. `pointer-events: none` blocks taps, but the closed overlay is still in the tab order and the accessibility tree, so keyboard and screen-reader users can land on invisible buttons. Fix it with `visibility`, delayed on close so the fade-out still plays:

```css
.modal-overlay {
  visibility: hidden;
  transition: opacity 160ms ease-out, visibility 0s linear 160ms;
}
.modal-overlay.open {
  visibility: visible;
  transition-delay: 0s;
}
```

If you toggle `hidden` or `inert` in JS, you can skip this.

**Smaller notes, optional:**
- The overlay fades out over 160ms while the modal takes 120ms, so the card disappears slightly before the dim layer. That's fine and arguably nice. If you want them to finish together, set both to 140ms.
- The CSS you pasted doesn't center the modal, so I assume the overlay's `display: flex` and centering rules are elsewhere.
- Since you've tested on phones, check one more case: open and close the modal quickly a few times. The transitions should reverse smoothly, and they should with this setup.
