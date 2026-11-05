The popup works if you click it with a mouse, which is probably how you've tested it. It has real problems for anyone using a keyboard, a screen reader, or sometimes a phone. I haven't run it, so this comes from reading the code.

**Main problems**

1. **The Keep and Remove controls aren't buttons.** They're `<span onclick>`, so they can't be reached with Tab and don't respond to Enter or Space. A keyboard user can open the dialog but can't confirm or cancel it. Screen readers don't announce them as controls either. They're also probably small tap targets on touch screens.
2. **Focus isn't managed.**
   - Opening the dialog doesn't move focus into it, so focus stays on the trash icon behind the overlay.
   - Tab walks through the page underneath, and Enter on the icon opens the dialog again.
   - Closing the dialog doesn't return focus to the trigger, so focus is lost.
3. **Escape doesn't close it.** Clicking the dimmed backdrop probably doesn't either. Most people expect both to work.
4. **It isn't marked as a dialog.** There's no `role="dialog"`, `aria-modal`, or label, so assistive tech doesn't know a modal appeared. The title is a `div`, not a heading.
5. **The trigger has no accessible name.** It's an icon-only button with no `aria-label`, so a screen reader just says "button". The SVG paths also have no `stroke` set here. If your CSS doesn't supply one, the icon may not render at all.
6. **Remove gives no feedback.** `doRemove()` closes the popup straight away and fires the request. There's no sign it worked, no loading state, and no error if the request fails. The user can't tell whether Dana was removed, which fits "feels broken."

**Smaller issues**
- The text hard-codes "She" and "Keep her". If it isn't templated by person, it will be wrong for some volunteers, so use their name or neutral wording.
- The page behind can still scroll.

**Fix**

The native `<dialog>` element handles focus trapping, Escape, the backdrop, and focus return for you:

```html
<button class="icon-btn" aria-label="Remove Dana Okafor from the Saturday rota"
        onclick="confirmDlg.showModal()">…</button>

<dialog id="confirmDlg" aria-labelledby="confirmTitle">
  <h2 id="confirmTitle">Remove Dana Okafor from the Saturday rota?</h2>
  <p>Dana will be notified by email.</p>
  <form method="dialog" class="row">
    <button value="cancel" autofocus>Keep Dana</button>
    <button value="remove" class="danger" onclick="doRemove()">Remove</button>
  </form>
</dialog>
```

Also make `doRemove()` show a result, such as a "Dana removed" message or an error. Style `dialog::backdrop` for the overlay.

To check this yourself, unplug the mouse and try to remove someone using only Tab, Enter, and Escape. Then turn on VoiceOver (Cmd+F5), which should make the problems obvious.
