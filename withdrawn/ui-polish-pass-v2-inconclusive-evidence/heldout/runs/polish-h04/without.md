I haven't rendered this, so the contrast figures are estimates from the hex values. Here's the tidied version:

```html
<div class="overlay" id="ov">
  <div class="dialog" role="alertdialog" aria-modal="true" aria-labelledby="dlg-title" aria-describedby="dlg-desc">
    <div class="title" id="dlg-title">Delete project?</div>
    <p id="dlg-desc">This removes "Harvest Planner" and its 14 tasks.</p>
    <button type="button" class="btn cancel" onclick="closeD()">Cancel</button>
    <button type="button" class="btn del" onclick="del()">Delete</button>
  </div>
</div>
<style>
:root{--bg:#16181d;--text:#9aa0a6;--panel:#1f2229;--title:#e8eaed}
.overlay{position:fixed;inset:0;background:rgba(0,0,0,.6);display:grid;place-items:center}
.dialog{background:var(--panel);color:var(--text);padding:24px;border-radius:10px;width:420px;max-width:calc(100vw - 32px);animation:pop .2s ease-out}
.title{font-size:18px;color:var(--title)}
.btn{display:inline-block;padding:8px 14px;margin-right:8px;cursor:pointer;font:inherit;border-radius:6px}
.btn:focus-visible{outline:2px solid #8ab4f8;outline-offset:2px}
.cancel{background:transparent;color:var(--title);border:1px solid #5f6368}
.del{background:#7a1f1f;color:#fff;border:1px solid transparent}
@keyframes pop{from{transform:scale(.95);opacity:0}to{transform:scale(1);opacity:1}}
@media (prefers-reduced-motion:reduce){.dialog{animation:none}}
</style>
```

**What I changed**

- **Title:** `#555` on the dark panel was about 2:1 contrast. It's now `#e8eaed`, which is well above the 4.5:1 minimum.
- **Cancel:** `#444` on the panel was nearly invisible. It's now light text with a thin gray border, so it still reads as secondary but is clearly a button.
- **Delete:** `#8c3b3b` text on a `#7a1f1f` background was close to unreadable. It's now white on the same dark red, about 10:1, and the button color is unchanged.
- **Backdrop:** The overlay was 30% black, which barely dims a dark page. It's now 60%, so the dialog separates from what's behind it.
- **Buttons:** The `<span>` buttons couldn't be reached by keyboard or screen reader. They're now real `<button type="button">` elements, and the same `onclick` handlers work. I added a visible focus ring.
- **Dialog semantics:** I added `role="alertdialog"`, `aria-modal`, and labelled-by/described-by attributes so assistive tech announces it properly.
- **Animation:** The pop-in went from 0.6s starting at half size to 0.2s starting at 95%, which feels less jarring. It's disabled for users with `prefers-reduced-motion`.
- **Small screens:** I added `max-width` so the 420px dialog doesn't overflow narrow screens.

**Left alone**

- Layout, copy, colors of the panel and body text (the body text is about 6:1, which passes), and the overall look.
- `--bg` is unused, so I kept it as is.

**Not done**

- Focus isn't moved into the dialog when it opens, there's no focus trap, and Escape doesn't close it. Those need changes in `closeD()` and the opening code, which I can't see. Say so if you want them added.
