Here are the changed pieces. The layout, palette family, wording and sizes are the same.

```html
<div class="overlay" id="ov">
  <div class="dialog" role="alertdialog" aria-modal="true" aria-labelledby="dt" aria-describedby="dd">
    <div class="title" id="dt">Delete project?</div>
    <p id="dd">This removes "Harvest Planner" and its 14 tasks.</p>
    <button type="button" class="btn cancel" id="cancelBtn" onclick="closeD()">Cancel</button>
    <button type="button" class="btn del" onclick="del()">Delete</button>
  </div>
</div>
<style>
:root{--bg:#16181d;--text:#9aa0a6;--panel:#1f2229;--title:#e8eaed}
.overlay{position:fixed;inset:0;background:rgba(0,0,0,.65);display:grid;place-items:center}
.dialog{background:var(--panel);color:var(--text);padding:24px;border-radius:10px;width:min(420px,calc(100vw - 32px));animation:pop .15s ease-out}
.dialog p{overflow-wrap:anywhere}
.title{font-size:18px;color:var(--title)}
.btn{display:inline-block;padding:8px 14px;margin-right:8px;cursor:pointer;font:inherit;border:0;background:none}
.btn:focus-visible{outline:2px solid #e8eaed;outline-offset:2px}
.cancel{color:var(--title)}
.del{background:#7a1f1f;color:#fff}
@keyframes pop{from{transform:scale(.95);opacity:0}to{transform:scale(1);opacity:1}}
@media (prefers-reduced-motion:reduce){.dialog{animation:none}}
</style>
<script>
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeD()});
</script>
```

**What I changed, most important first**

1. **Contrast, which is likely behind the complaints.** Estimated ratios, not measured:
   - The title was `#555` on the dark panel, about 2.2:1. It's now `#e8eaed`.
   - Cancel was `#444`, about 1.7:1. It now uses the same light color as the title.
   - Delete was `#8c3b3b` text on a `#7a1f1f` background, about 1.4:1 and nearly unreadable. The text is now white on the same red, so the button looks the same but you can read it.
   - The body text (`#9aa0a6`) already passed, so I left it.
2. **Overlay.** The scrim went from 30% to 65% black. At 30% the dialog barely separated from the dark page behind it.
3. **Real buttons.** The `<span>` buttons couldn't be reached by keyboard or announced as buttons. They're now `<button>` elements with a reset so they look the same, plus a visible focus ring.
4. **Dialog semantics.** I added `role="alertdialog"`, `aria-modal`, and a label and description. Escape now closes the dialog.
5. **Animation.** It was 0.6s starting at half size, which is slow for a confirm step. It's now 0.15s from 95% scale, and it's removed for reduced-motion users.
6. **Narrow screens and long names.** The width is now `min(420px, 100vw − 32px)`, and long project names wrap instead of overflowing.

**Not done**
- I can't see your `closeD()`, `del()` or the code that opens the dialog. When it opens, move focus to `#cancelBtn`. Cancel is the safe default for a destructive action. On close, return focus to the control that opened it. Without this, keyboard users can still tab behind the overlay.
- I didn't test in a browser or with a screen reader. The contrast numbers come from calculation.
