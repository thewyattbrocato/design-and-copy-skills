It looks fine if you only use a mouse and can see the screen. The popup is built from generic elements with click handlers, so it loses most of the behavior people expect from a dialog.

**Likely causes of the "broken" feeling**

1. **Keyboard users can't answer the popup.** "Keep her" and "Remove" are `<span>`s. They can't be tabbed to, and Enter and Space do nothing on them. Someone who opens the popup with the keyboard is stuck, because they can't confirm or cancel.
2. **Focus stays behind the popup.** `openConfirm()` never moves focus into the dialog. Tab keeps moving through the page underneath, and nothing traps focus. On close, focus isn't returned to the trash button, so keyboard users lose their place.
3. **Escape and clicking outside do nothing.** Most people try these first to dismiss a popup.
4. **Screen readers don't know it's a dialog.**
   - The overlay has no `role="dialog"`, `aria-modal`, or `aria-labelledby`, and the title is a plain `div`.
   - Nothing announces the popup when it opens.
   - The trash button has no accessible name. The SVG has no title and the button has no `aria-label`, so it's announced as just "button".
5. **Nothing happens after "Remove".** `doRemove()` closes the popup immediately.
   - There's no pending state, so a double-click can post twice.
   - There's no success message and no error handling if the post fails.
   - Unless the rota row visibly changes, people can't tell whether it worked, which feels broken.

**Smaller issues**

- Spans have no pointer cursor, hover state, or focus ring unless your CSS adds them. "Keep her" styled as a link is also a small touch target on phones.
- The safe option should get initial focus, since this is a destructive action.
- The name, the day, and "She/her" are hard-coded in the markup. Make the copy data-driven, or use neutral wording like "They will be notified".

**Fix**

- Use real `<button type="button">` elements for both actions.
- Use a `<dialog>` opened with `showModal()`. That gives you focus trapping, Escape to close, and focus restoration for free.
- Add `aria-label="Remove Dana Okafor from the rota"` to the icon button.
- Disable the Remove button while the request runs, then show a confirmation or an error message.

I can rewrite the snippet with these changes if you'd like.
