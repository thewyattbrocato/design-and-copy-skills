**Use container queries.** Your teammate who said "respond to its own container" is right.

**Why, for this card specifically**
- **The same viewport gives different card widths.** At a 1440px viewport, the card is about 300px wide in the 4-up dashboard row. In the transaction page's right rail it's about 320px. In a modal it might be 480px or more. A viewport media query can't tell these apart. It would give the dashboard card and the modal card the same layout even though their widths differ.
- **Viewport queries make the card depend on the page.** If the rail width changes, or the dashboard goes from 4-up to 3-up, every media query tied to the old layout breaks. With a container query, the card adapts to whatever space it gets, and nobody has to change the card.
- **Reuse is the point of a design system.** A fourth placement later (a drawer, a mobile list) should work without anyone touching the card's CSS.

**What viewport queries are still for**
Use them for questions about the whole page or device, such as the main navigation pattern, `prefers-reduced-motion`, `hover`/`pointer`, and print. The card doesn't need any of these.

**Sketch**
```css
.account-card-slot { container: account-card / inline-size; }

.account-card {
  display: grid;
  gap: 0.75rem;
  padding: 1rem;
}
.account-card__spark { display: none; }          /* compact default */

@container account-card (min-width: 22rem) {
  .account-card { grid-template-columns: 1fr auto; }
  .account-card__spark { display: block; }
  .account-card__transfer { grid-column: 1 / -1; }
}
```

**Practical points for the meeting**
1. **Put `container-type` on a wrapper, not on the card itself.** An element can't query its own size, so the card's root needs a parent that is the container.
2. **Use one breakpoint to start.** Compact below about 22rem, roomy above it. Find the real value by resizing until the content breaks, and write it in `rem`.
3. **Add `min-inline-size: 0` and `overflow-wrap: anywhere` to the balance and transaction text.** This guards against long merchant names.
4. **Browser support is not a concern.** Container queries are supported in all evergreen browsers. If you must support something older, fall back to the compact layout, which is the default above.
5. **Test it in Storybook, or any harness, at three container widths.** Use about 16rem, 22rem and 32rem, with a long merchant name. Check zoom at 200% too.

**Assumptions:** you target evergreen browsers, use plain CSS (tell me if it's Tailwind or CSS-in-JS and I'll translate), and the narrowest card is about 16rem.
