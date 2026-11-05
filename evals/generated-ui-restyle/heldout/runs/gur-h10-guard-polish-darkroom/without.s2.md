I couldn't save a file because the Write tool is disabled in this session, so the full page is below. Copy it into your `index.html`.

Your friend's "AI-made" reaction is probably about the look, not the plainness. Cream paper, a serif, a rust-red accent, small tracked uppercase labels and hairline rules are the stock "tasteful editorial" kit. Nothing on the page says darkroom. So I built the design from the darkroom itself:

- **Dark page lit by a safelight.** The red glow in the corner is the one accent, and it's the same red as the light over your door. The sign-on-the-door note now has its own glowing dot.
- **Exposure test strip.** The row of eight grey steps under the intro is a test strip, one step per enlarger. It's decorative and hidden from screen readers.
- **Real hierarchy.** The headline is much larger, with "by hand" in italic red. The days and the £18 are big. Labels are in monospace, like the writing on a darkroom timer or tray label.
- **A two-column layout** replaces the sidebar and main split.

I didn't change any of your wording or facts, and I didn't invent any content. The biggest remaining giveaway is the lack of photos. Even one scan of a print from a member would do more than any CSS, so I'd add that next.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fixer Street Darkroom</title>
<style>
:root{
  --bg:#14100f;--bg2:#1d1816;--ink:#ebe3d6;--soft:#b3a89a;--rule:#3a312d;
  --safe:#ff5a45;--glow:rgba(255,60,40,.28);
  --serif:Charter,"Iowan Old Style",Georgia,serif;
  --mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;
}
*{box-sizing:border-box}
html{background:var(--bg)}
body{margin:0;color:var(--ink);font:18px/1.6 var(--serif);
  background:radial-gradient(40rem 32rem at 88% -4rem,var(--glow),transparent 70%),var(--bg);
  min-height:100vh}
.wrap{max-width:58rem;margin:0 auto;padding:1.5rem 1.5rem 5rem}
header{display:flex;flex-wrap:wrap;justify-content:space-between;gap:.25rem 2rem;font:.85rem/1.4 var(--mono);color:var(--soft)}
header b{color:var(--ink);font-weight:700}
.hero{padding:6rem 0 3rem;position:relative}
.bulb{position:absolute;right:.5rem;top:1.5rem;width:1.1rem;height:1.1rem;border-radius:50%;background:var(--safe);
  box-shadow:0 0 1.2rem .5rem var(--glow),0 0 4rem 1.5rem var(--glow)}
h1{font-size:clamp(2.4rem,7vw,4.6rem);line-height:1.02;font-weight:400;letter-spacing:-.02em;margin:0 0 1.5rem;max-width:15ch}
h1 em{font-style:italic;color:var(--safe)}
.lede{font-size:1.2rem;color:var(--soft);max-width:34ch;margin:0}
/* exposure test strip: eight steps, one per enlarger */
.strip{display:grid;grid-template-columns:repeat(8,1fr);height:.9rem;margin:3rem 0 0;border:1px solid var(--rule)}
.strip i{background:rgb(var(--g),var(--g),var(--g))}
.strip i:nth-child(1){--g:235}.strip i:nth-child(2){--g:205}.strip i:nth-child(3){--g:172}.strip i:nth-child(4){--g:138}
.strip i:nth-child(5){--g:104}.strip i:nth-child(6){--g:72}.strip i:nth-child(7){--g:44}.strip i:nth-child(8){--g:24}
h2{font:700 1rem/1.2 var(--mono);color:var(--safe);margin:0 0 1rem}
h2::before{content:"// "}
.sessions{padding:3rem 0 1rem}
table{border-collapse:collapse;width:100%;max-width:40rem}
th{font:400 .8rem/1 var(--mono);color:var(--soft);text-align:left;padding:0 0 .6rem}
td{padding:.9rem 0;border-top:1px solid var(--rule)}
td:first-child{font-size:2rem;line-height:1;width:5.5rem}
td:nth-child(2){font-variant-numeric:tabular-nums}
td:last-child,th:last-child{text-align:right;font-family:var(--mono);font-size:.9rem;color:var(--soft)}
.rule{display:flex;gap:.9rem;align-items:flex-start;max-width:40rem;margin:1.5rem 0 0;padding:1rem 1.1rem;background:var(--bg2);border-left:3px solid var(--safe)}
.rule .l{flex:none;width:.7rem;height:.7rem;margin-top:.55rem;border-radius:50%;background:var(--safe);box-shadow:0 0 .7rem .2rem var(--glow)}
.rule p{margin:0}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:3rem;margin-top:3.5rem;padding-top:3rem;border-top:1px solid var(--rule)}
.price{font-size:3.2rem;line-height:1;letter-spacing:-.02em;margin:0 0 .75rem}
.price small{font-size:1rem;color:var(--soft);letter-spacing:0}
p{margin:0 0 1rem}
a{color:var(--safe)}
a:focus-visible{outline:2px solid var(--ink);outline-offset:3px}
.join{display:inline-block;margin-top:.25rem;padding:.75rem 1.2rem;background:var(--safe);color:#14100f;text-decoration:none;font:700 .95rem/1 var(--mono);border-radius:2px}
.join:hover{background:var(--ink)}
.when{font:.8rem/1 var(--mono);color:var(--soft);margin:0 0 .75rem}
@media (max-width:44rem){
  .hero{padding-top:4rem}
  .cols{grid-template-columns:1fr;gap:2.5rem}
  td:first-child{font-size:1.6rem;width:4rem}
}
</style></head><body><div class="wrap">
<header><b>Fixer Street Darkroom</b><span>Back of the old print works, 9 Fixer Street, Calder Mills</span></header>

<div class="hero">
  <span class="bulb" aria-hidden="true"></span>
  <h1>Black-and-white printing <em>by hand</em>, for anyone who wants to learn.</h1>
  <p class="lede">Eight enlargers, shared chemistry, and someone on every session who has done this for years.</p>
  <div class="strip" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
</div>

<main>
<section class="sessions">
  <h2>Open sessions</h2>
  <table>
    <tr><th scope="col">Day</th><th scope="col">Hours</th><th scope="col">Enlargers</th></tr>
    <tr><td>Tue</td><td>6&ndash;10 pm</td><td>6</td></tr>
    <tr><td>Thu</td><td>6&ndash;10 pm</td><td>6</td></tr>
    <tr><td>Sat</td><td>10 am&ndash;4 pm</td><td>8</td></tr>
  </table>
  <div class="rule"><span class="l" aria-hidden="true"></span><p>Red light on over the door means someone is printing. Knock and wait.</p></div>
</section>

<div class="cols">
  <section>
    <h2>Membership</h2>
    <p class="price">&pound;18 <small>a month</small></p>
    <p>Covers every open session, chemistry and a drying rack. Bring your own paper and negatives. Your first session is free if you come along with a member.</p>
    <a class="join" href="mailto:hello@fixerstreet.example">Ask about joining</a>
  </section>
  <section>
    <h2>Intro evening</h2>
    <p class="when">First Tuesday of each month</p>
    <p>We develop one roll together and make a contact sheet. No experience needed; bring a roll of exposed black-and-white film.</p>
  </section>
</div>
</main>
</div></body></html>
```

I haven't opened this in a browser, so check it on your phone and on a wide screen before publishing. It uses only system fonts, so it will look a little different on each device. The red `#ff5a45` on the dark background is comfortably readable.
