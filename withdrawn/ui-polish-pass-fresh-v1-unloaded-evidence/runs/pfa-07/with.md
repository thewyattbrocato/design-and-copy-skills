It looks fine with a mouse, which is probably why you haven't spotted it. The problems show up with a keyboard, a screen reader, or a second click.

**Most likely what people are feeling**

1. **The two choices aren't buttons.** "Keep her" and "Remove" are `<span onclick>`. They can't be reached with Tab, and Enter or Space does nothing on them. They also have no button role, so assistive tech doesn't announce them as actions. Keyboard users open the popup and can't do anything in it.
2. **No Escape, no click-outside.** People expect both to dismiss a modal. Here the only way out is the "Keep her" span.
3. **Focus isn't managed.** When the popup opens, focus stays on the trash icon behind the overlay. Tab then moves through the page underneath. On close, focus isn't returned to where it came from, so keyboard users lose their place.
4. **Remove gives no feedback.** `doRemove()` closes the popup immediately, with no spinner, no success message and no error handling. If the post is slow or fails, it looks as if nothing happened. A double-click can also send the request twice.

**Also wrong**

5. **The popup always says "Dana Okafor".** `openConfirm()` takes no argument and the name is hard-coded. If this is a per-row button, every row would open a popup naming Dana. Pass the volunteer's name or id in.
6. **"She" and "Keep her" assume a pronoun.** Use the name or "they", for example "Keep Dana" and "Dana will be notified by email."
7. **The trash button has no accessible name.** It's an icon-only button with no `aria-label`, so a screen reader just says "button". Add `aria-label="Remove Dana Okafor from rota"`.
8. **The overlay isn't marked up as a dialog.** It has no `role="dialog"`, `aria-modal="true"` or `aria-labelledby`, so a screen reader doesn't announce it as a popup.

**Minimal fix**

```html
<button class="icon-btn" aria-label="Remove Dana Okafor from the Saturday rota"
        onclick="openConfirm(this, 'Dana Okafor')">…</button>

<div id="confirm" class="overlay" style="display:none" onclick="if(event.target===this)closeConfirm()">
  <div class="box" role="dialog" aria-modal="true" aria-labelledby="confirm-title">
    <div class="title" id="confirm-title"></div>
    <p>They will be notified by email.</p>
    <div class="row">
      <button type="button" class="link" id="keep" onclick="closeConfirm()"></button>
      <button type="button" class="btn danger" id="remove" onclick="doRemove()">Remove</button>
    </div>
  </div>
</div>

<script>
  let opener;
  function openConfirm(btn, name) {
    opener = btn;
    confirm_title.textContent = `Remove ${name} from the Saturday rota?`;
    keep.textContent = `Keep ${name.split(' ')[0]}`;
    confirm.style.display = 'flex';
    keep.focus();                       // safe option gets focus
  }
  function closeConfirm() { confirm.style.display = 'none'; opener?.focus(); }
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && confirm.style.display !== 'none') closeConfirm();
  });
  async function doRemove() {
    remove.disabled = true; remove.textContent = 'Removing…';
    try { /* await post */ closeConfirm(); /* show success, update row */ }
    catch { /* show error inside the dialog */ }
    finally { remove.disabled = false; remove.textContent = 'Remove'; }
  }
</script>
```

You'll also need a visible `:focus-visible` style on the buttons, and a tab trap inside the dialog. If you use the native `<dialog>` element with `showModal()`, you get the focus trap, Escape and the dialog role for free.

To confirm, put your mouse aside and try the whole flow with Tab, Enter and Escape. You'll hit the first three problems straight away.
