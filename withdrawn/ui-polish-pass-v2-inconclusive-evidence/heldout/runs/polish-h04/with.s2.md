I only had the snippet, so I haven't run any of this in a browser or with a screen reader.

```html
<div class="overlay" id="ov">
  <div class="dialog" role="alertdialog" aria-modal="true" aria-labelledby="dt" aria-describedby="dd">
    <div class="title" id="dt">Delete project?</div>
    <p id="dd">This removes "Harvest Planner" and its 14 tasks.</p>
    <button type="button" class="btn cancel" onclick="closeD()">Cancel</button>
    <button type="button" class="btn del" onclick="del()">Delete</button>
  </div>
</div>
<style>
:root{--bg:#16181d;--text:#9aa0a6;--panel:#1f2229;--title:#e8eaed}
.overlay{position:fixed;inset:0;background:rgba(0,0,0,.6);display:grid;place-items:center}
.dialog{background:var(--panel);color:var(--text);padding:24px;border-radius:10px;width:min(420px,calc(100vw - 32px));animation:pop .15s ease-out}
.title{font-size:18px;color:var(--title)}
.btn{display:inline-block;padding:8px 14px;margin-right:8px;cursor:pointer;font:inherit;border-radius:6px}
.cancel{background:none;color:var(--title);border:1px solid #80868b}
.del{background:#a32727;color:#fff;border:1px solid transparent}
.btn:focus-visible{outline:2px solid #8ab4f8;outline-offset:2px}
@keyframes pop{from{transform:scale(.95);opacity:0}to{transform:scale(1);opacity:1}}
@media (prefers-reduced-motion:reduce){.dialog{animation:none}}
</style>
```

**What I changed, most important first**
1. **Contrast.** The title (`#555`), Cancel (`#444`) and Delete (`#8c3b3b` on `#7a1f1f`) were all hard to read on the dark panel. The title and Cancel are now light grey (`#e8eaed`), and Delete is white on a slightly brighter red (`#a32727`), which is close to the old hue. Cancel also has a visible border so it reads as a button. The body text was already readable, so I left it.
2. **Real buttons.** Cancel and Delete were `<span>`s, so keyboard users couldn't Tab to them or press Enter. They're now `<button type="button">` with the font and radius reset to match the old look.
3. **Focus ring.** I added a visible `:focus-visible` outline to the buttons.
4. **Dialog semantics.** I added `role="alertdialog"`, `aria-modal`, and labels tied to the title and message, so screen readers announce the question and the consequence.
5. **Scrim.** I raised it from 30% to 60% black. At 30% the page behind the dialog still looked active in dark mode.
6. **Animation.** The pop-in went from 0.6s starting at half size to 0.15s starting at 95%. It's now disabled under `prefers-reduced-motion`.
7. **Narrow screens.** The width is now `min(420px, 100vw - 32px)`, so the dialog no longer overflows on small phones.

I left the layout, wording and colors otherwise unchanged.

**Not done**
- I can't see `closeD()` or the code that opens the dialog. When it opens, focus should move to Cancel, the safe choice. Escape should close it, and focus should return to the button that opened it. I didn't add this.
- You may want the button labels to say "Delete project" and "Keep it". I left the copy alone because you asked for tidying, not rewording.
