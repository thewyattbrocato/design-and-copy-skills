Here's the tidied dialog. The main problem was contrast: dark mode left several colors that were tuned for a light background.

```html
<div class="overlay" id="ov">
  <div class="dialog" role="alertdialog" aria-modal="true" aria-labelledby="dt" aria-describedby="dd">
    <div class="title" id="dt">Delete project?</div>
    <p id="dd">This removes "Harvest Planner" and its 14 tasks.</p>
    <button type="button" class="btn cancel" onclick="closeD()" autofocus>Cancel</button>
    <button type="button" class="btn del" onclick="del()">Delete project</button>
  </div>
</div>
<style>
:root{--bg:#16181d;--text:#9aa0a6;--panel:#1f2229}
.overlay{position:fixed;inset:0;background:rgba(0,0,0,.6);display:grid;place-items:center}
.dialog{background:var(--panel);color:var(--text);padding:24px;border-radius:10px;width:420px;max-width:calc(100vw - 32px);animation:pop .15s ease}
.title{font-size:18px;color:#e8eaed}
.btn{display:inline-block;padding:8px 14px;margin-right:8px;cursor:pointer;font:inherit;border:1px solid transparent;border-radius:6px;background:none}
.cancel{color:#e8eaed;border-color:#6b7178}
.del{background:#a62b2b;color:#fff}
.btn:focus-visible{outline:2px solid #8ab4f8;outline-offset:2px}
@keyframes pop{from{transform:scale(.95);opacity:0}to{transform:scale(1);opacity:1}}
@media (prefers-reduced-motion:reduce){.dialog{animation:none}}
</style>
<script>
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeD()});
</script>
```

**What I changed**
1. **Contrast (the likely source of the complaints):** all ratios are my estimates from the hex values, not measured.
   - Title went from `#555` (about 2:1) to `#e8eaed`.
   - Cancel went from `#444` (about 1.6:1, nearly invisible) to `#e8eaed`. I added a thin border so it reads as a button.
   - Delete went from `#8c3b3b` on `#7a1f1f` (about 1.3:1) to white on `#a62b2b`, which is roughly 7:1. It's still the same dark red.
   - Body text `#9aa0a6` was already fine, so I left it.
2. **Scrim:** raised from 30% to 60% black. At 30% the dialog barely separated from a dark page.
3. **Real buttons:** the `<span onclick>` elements couldn't be reached or activated from the keyboard. They are now `<button>`s with a visible focus ring. Cancel gets initial focus, so Enter doesn't delete by accident.
4. **Dialog semantics and Escape:**
   - Added `role="alertdialog"`, `aria-modal` and labels, so screen readers announce it.
   - Escape now closes it.
5. **Delete label:** "Delete" is now "Delete project", so the button names what it does.
6. **Motion:** the pop animation went from 0.6s scaling up from 50% to 0.15s from 95%. It's off under reduced-motion.
7. **Narrow screens:** added `max-width` so the 420px dialog no longer overflows small screens.

**Not changed:** layout, palette, copy and the overall look.

**Notes**
- I haven't seen `closeD()` or `del()`. Make sure `closeD` returns focus to the button that opened the dialog. Also, `del()` is irreversible with no undo, so check that's intended.
- I didn't run this in a browser or with a screen reader. Focus is also not trapped inside the dialog, so Tab can still reach the page behind it. Using `<dialog>` with `showModal()` would fix that if you want it.
