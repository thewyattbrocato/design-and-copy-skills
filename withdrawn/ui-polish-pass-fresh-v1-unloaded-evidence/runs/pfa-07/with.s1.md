It looks fine with a mouse, which is why you don't see it. The problems show up with a keyboard, a screen reader, or a flaky connection.

**Most likely what people are feeling**

1. **The two choices aren't buttons.** "Keep her" and "Remove" are `<span onclick>`. They can't be reached with Tab, Enter and Space don't activate them, and screen readers don't announce them as controls. A keyboard user can open the popup but can't answer it. Use `<button type="button">` for both. Style "Keep her" as a secondary button, not a bare link.
2. **Focus isn't managed.**
   - Opening the popup leaves focus on the trash icon behind it, so Tab wanders through the page underneath.
   - Nothing traps focus inside the popup.
   - Closing doesn't return focus to the trigger, so keyboard users lose their place.
   - On open, move focus into the dialog, ideally onto the safe option ("Keep her") since the action is destructive. Trap Tab inside it. On close, restore focus to the trigger.
3. **It can't be dismissed the way people expect.** Escape does nothing, and clicking the backdrop does nothing. Both are muscle memory for a popup.
4. **"Remove" gives no feedback.**
   - `doRemove()` closes the popup immediately, before the server answers.
   - There's no pending state, so a double-click can post twice.
   - A failed request is silent.
   - Nothing confirms success. The person might vanish from the list, or might not.
   - Keep the popup open, disable the button and show "Removing…". Close only on success, and show an inline error on failure.

**Accessibility gaps that make it worse for assistive tech**

5. The icon button has no accessible name, so it's announced as just "button". Add `aria-label="Remove Dana Okafor from Saturday rota"`. Also add `aria-hidden="true"` to the SVG.
6. The overlay has no `role="dialog"`, `aria-modal="true"` or `aria-labelledby`, so a screen reader doesn't know a dialog opened. The title is a `<div>`, not a heading. Content behind it isn't inert, so use `inert` on the page or a native `<dialog>` with `showModal()`.
7. Nothing is announced on open or close.

**Smaller things**

- The icon is 20px with no padding specified, which is a small touch target. Aim for about 44px.
- The `<span>` controls probably have no hover, focus or active styling, so they don't feel clickable.
- The page behind can still scroll.
- The copy hardcodes "She". Use the name or "They" unless you store pronouns, and the name and rota are hardcoded rather than filled in per row.

The fastest fix is a native `<dialog>`. `showModal()` gives you the focus trap, Escape, inert background and focus restoration for free. You'd still need to add the real buttons, the labels and the pending/error handling.

I can rewrite the snippet that way if you'd like.
