**Recommendation: make the card respond to its own container (container queries).** Use viewport media queries only for page-level layout, such as how many columns the dashboard grid has.

**Why, based on your three placements**

- **The viewport can't tell the card which layout to use.** The card's width depends on where it sits, not on the screen size. On a 1440px screen it could be about 300px in the 4-up row, about 320px in the right rail, or about 500px in a modal. A viewport query would see the same screen in all three cases. You'd need hacks like `.rail .card { ... }` or `.modal .card { ... }` overrides, and those leak the card's internals into every page that uses it.
- **The modal is the clearest case.** Its width is set by the modal, not the viewport. A media query can't handle it at all.
- **The 4-up row changes width on its own.** At some breakpoints it becomes 2-up or 1-up, so the card's width shifts without any card-level logic. With container queries the card adapts automatically.
- **It matches what a design system component should be.** The card should be portable, so a consumer can place it anywhere without knowing its breakpoints. Media queries tie the component to the page that uses it.

**How to do it**

```css
.account-card-wrapper { container: account-card / inline-size; }

.account-card { /* compact by default */ }

@container account-card (min-width: 360px) {
  .account-card { /* roomy: sparkline beside balance, inline Transfer button */ }
}
```

- Write the compact layout as the default and add the roomy layout at a `min-width` container query.
- Put `container-type` on a wrapper element, not on the card itself. A container can't style itself, only its descendants.
- Set one or two breakpoints based on where the content actually breaks, such as when the sparkline no longer fits beside the balance. Don't set them from device sizes.
- Browser support is no longer a concern. Container size queries are in all current evergreen browsers. Check your credit union's minimum supported browsers if you have an unusual policy.

**Trade-offs to mention in the meeting**

- `inline-size` containment means the wrapper can't take its width from its content. That's fine in grid and flex layouts, but check it in the modal if the modal shrink-wraps its content.
- Container queries add a small amount of setup, and designers need to think in "card widths" instead of "screen sizes". Document the card's breakpoints in the design system and in Storybook, and add a story for each width.
- Viewport media queries still make sense for things that depend on the device, like touch target sizes, `prefers-reduced-motion`, and the dashboard's column count.

**Short version for the meeting:** the card's layout depends on the space it's given, and only a container query measures that. Media queries would force per-page overrides and can't handle the modal.
