I made a light restyle and kept all the words, the sections and their order. Your page was never really a template. It has a paper ground, a serif, a safelight red and tabular figures. What reads as AI-made is that it's an editorial layout with nothing in it that only a darkroom would have.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fixer Street Darkroom</title>
<style>
:root{--paper:#f3efe6;--ink:#1c1a17;--soft:#5d574e;--rule:#cfc6b6;--safe:#a3271c;--sans:ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;--serif:Charter,Georgia,serif}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.55 var(--serif)}
.wrap{max-width:62rem;margin:0 auto;padding:3rem 1.5rem 4rem;display:grid;grid-template-columns:15rem 1fr;gap:1.5rem 3rem}
header{grid-column:1/-1;display:flex;flex-wrap:wrap;gap:.5rem 2rem;align-items:baseline;justify-content:space-between;margin-bottom:1.5rem}
/* step tablet: the strip of grey steps printers use to test exposure */
header::after{content:"";flex-basis:100%;height:.6rem;margin-top:.5rem;outline:1px solid var(--ink);
background:linear-gradient(to right,#e4ded1 0 14.28%,#c9c2b3 0 28.57%,#a9a295 0 42.85%,#857f74 0 57.14%,#5d574e 0 71.42%,#3a3631 0 85.71%,#1c1a17 0)}
.name{font:700 1.3rem/1 var(--serif);letter-spacing:-.005em}
.where{font:.9rem/1.4 var(--sans);color:var(--soft)}
h1{font-size:2.7rem;line-height:1.08;font-weight:400;letter-spacing:-.015em;margin:0 0 1rem;max-width:18ch}
.lede{font-size:1.2rem;color:var(--soft);max-width:36ch;margin:0 0 2.5rem}
h2{font:italic 400 1.35rem/1.2 var(--serif);margin:0 0 .5rem}
section{margin-bottom:2rem;max-width:38rem}
aside{font:.92rem/1.5 var(--sans);color:var(--soft)}
aside h2{color:var(--ink)}
table{border-collapse:collapse;width:100%;font:.95rem/1.4 var(--sans);font-variant-numeric:tabular-nums;color:var(--ink);margin-bottom:1.25rem}
th,td{text-align:left;padding:.45rem 0;border-bottom:1px solid var(--rule)}
th{font-weight:600;color:var(--soft);font-size:.85rem}
td:last-child,th:last-child{text-align:right}
/* the door sign */
.sign{margin:0;padding:.7rem .8rem;border:1px solid var(--safe);color:var(--ink)}
.light{display:inline-block;width:.6rem;height:.6rem;border-radius:50%;background:var(--safe);margin-right:.5rem}
a{color:var(--safe)}
a:focus-visible{outline:2px solid var(--ink);outline-offset:3px}
.join{display:inline-block;margin-top:.5rem;padding:.7rem 1.1rem;background:var(--ink);color:var(--paper);text-decoration:none;font:600 .95rem/1 var(--sans);transition:background-color .15s}
.join:hover{background:var(--safe)}
@media (max-width:46rem){.wrap{grid-template-columns:1fr;padding-top:2rem}h1{font-size:2rem}}
</style></head><body><div class="wrap">
<header><span class="name">Fixer Street Darkroom</span><span class="where">Back of the old print works, 9 Fixer Street, Calder Mills</span></header>
<aside>
<h2>Open sessions</h2>
<table>
<tr><th>Day</th><th>Hours</th><th>Enlargers</th></tr>
<tr><td>Tue</td><td>6&ndash;10 pm</td><td>6</td></tr>
<tr><td>Thu</td><td>6&ndash;10 pm</td><td>6</td></tr>
<tr><td>Sat</td><td>10 am&ndash;4 pm</td><td>8</td></tr>
</table>
<p class="sign"><span class="light" aria-hidden="true"></span>Red light on over the door means someone is printing. Knock and wait.</p>
</aside>
<main>
<h1>Black-and-white printing by hand, for anyone who wants to learn.</h1>
<p class="lede">Eight enlargers, shared chemistry, and someone on every session who has done this for years.</p>
<section>
<h2>Membership</h2>
<p>&pound;18 a month covers every open session, chemistry and a drying rack. Bring your own paper and negatives. Your first session is free if you come along with a member.</p>
<a class="join" href="mailto:hello@fixerstreet.example">Ask about joining</a>
</section>
<section>
<h2>Intro evening</h2>
<p>First Tuesday of each month. We develop one roll together and make a contact sheet. No experience needed; bring a roll of exposed black-and-white film.</p>
</section>
</main>
</div></body></html>
```

**What I changed and why**
- **Header rule:** the plain 2px line is now a seven-step grey strip, like the exposure test strips printers make. It's the one darkroom object on the page, and it does the same job as the rule it replaced.
- **Small labels:** the tiny tracked-out capitals (headings, column heads, the name) are now italic serif headings and sentence-case column heads. Spaced-out caps on every label is a common generated look, and the rest of the page already speaks in serif.
- **Door sign:** the red-light note now has a thin safelight-red border, like a sign taped to a door. The dot stays still because nothing on the page is live.
- **Join button:** it gets a hover state, which it didn't have before. I tightened the headline spacing slightly.

**Kept:** the paper and ink palette, the red, the Charter/Georgia serif and the tabular figures. They fit a darkroom, and I couldn't tie any replacement to something real.

**Worth confirming:** "someone on every session who has done this for years" is your claim, so I left it as written.

**Not done:** I didn't open it in a browser. The step strip uses hard colour stops, so check that it looks right on your screen.

If your friend still thinks it's too plain, a real photo or a scanned print is the next step. I didn't invent one.
