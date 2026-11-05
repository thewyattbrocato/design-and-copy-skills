Your page is already more designed than your friend's comment suggests. The paper ground, Charter serif, red safelight dot, tabular figures and the sidebar timetable all come from a real darkroom. I'd leave those alone. Making it fancier would make it look more generated, not less.

**What still reads as template**
1. The small uppercase, letter-spaced `h2` labels ("Membership", "Intro evening") are the stock section-label look. This is the strongest tell.
2. The page has no picture of what you do. The Intro evening copy describes a contact sheet, but nothing on the page shows one.
3. The hover and focus states on the join button are the browser's defaults.

**Changes**

Replace the `h2` rule:
```css
h2{font:italic 400 1.2rem/1.2 Charter,Georgia,serif;margin:0 0 .5rem}
```

Add these rules, plus a hover state for the button:
```css
.strip{display:grid;grid-template-columns:repeat(6,1fr);gap:.3rem;background:var(--ink);padding:1.1rem .5rem;margin-top:1.25rem;position:relative}
.strip::before,.strip::after{content:"";position:absolute;left:0;right:0;height:.4rem;background:repeating-linear-gradient(90deg,var(--paper) 0 .35rem,transparent .35rem .9rem);opacity:.85}
.strip::before{top:.35rem}.strip::after{bottom:.35rem}
.strip span{aspect-ratio:3/2;background:#38342e;color:var(--paper);font:.6rem/1 var(--sans);display:flex;align-items:flex-end;padding:.25rem}
.join:hover{background:var(--safe)}
```

Add this inside the Intro evening section, after its paragraph:
```html
<div class="strip" aria-hidden="true"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span><span>6</span></div>
```

**Decision notes**
- Section labels are now sentence-case italic serif. Small caps with tracking is the generic label style, and the page's own voice is bookish serif.
- The film strip is drawn in CSS from the Intro evening copy ("develop one roll… make a contact sheet"). It has no photos, captions or invented claims, and it doesn't pass the rival test for a gym or a yoga studio.
- The button turns safelight red on hover, reusing the existing accent. There is no new color, motion or glow.

**To check**
- The lede says "Eight enlargers", but Tuesday and Thursday list 6 and only Saturday lists 8. Say "Six to eight enlargers" or whatever is true.
- I haven't viewed it in a browser. Check that the sprocket holes line up on a narrow phone.
