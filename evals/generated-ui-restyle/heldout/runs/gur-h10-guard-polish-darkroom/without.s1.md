I couldn't save a file because the Write tool is disabled in this session. The full page is below, so you can paste it into `index.html`. I haven't opened it in a browser.

**What I changed**

Your friend's "AI made it" comment is probably about the cream paper, serif body, tracked uppercase labels, red accent and tidy sidebar grid. That combination is what generated "tasteful" pages tend to look like. I swapped it for choices that come from the darkroom itself:

- **Dark page with a working safelight.** The red dot is now a glowing element, and a faint red glow sits in the corner. The sign about the red light sits right under the headline.
- **Sessions as a test strip.** Tue, Thu and Sat are three panels, each a step lighter than the last, like the exposure steps on a test print.
- **A big headline.** It's tight, heavy and left-aligned, with one word in red.
- **Plainer labels.** The tracked uppercase headings are gone.
- **Uneven columns.** Membership gets a large "£18" and a wider column than the intro evening.

I kept your copy and facts the same and only split the intro evening text into two paragraphs. Text contrast, the focus ring, the mobile layout and `aria-hidden` on the decorative light are all still there.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fixer Street Darkroom</title>
<style>
:root{
  --bg:#12100e;--text:#efe9dc;--dim:#b3aa9a;
  --safe:#ff5a45;--glow:rgba(255,60,40,.22);
  --sans:"Helvetica Neue",Helvetica,Arial,sans-serif;
  --serif:Charter,"Iowan Old Style",Georgia,serif;
  --mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;
}
*{box-sizing:border-box}
html{background:var(--bg)}
body{margin:0;color:var(--text);font:18px/1.55 var(--serif);
  background:radial-gradient(40rem 28rem at 88% -6rem,var(--glow),transparent 70%),var(--bg);
  min-height:100vh}
.wrap{max-width:64rem;margin:0 auto;padding:1.5rem 1.5rem 5rem}

header{display:flex;flex-wrap:wrap;justify-content:space-between;gap:.25rem 2rem;font:.9rem/1.4 var(--sans);color:var(--dim)}
.name{color:var(--text);font-weight:700}

.hero{padding:clamp(3rem,10vw,7rem) 0 3rem}
h1{font:700 clamp(2.6rem,8.5vw,6rem)/.95 var(--sans);letter-spacing:-.035em;margin:0 0 1.75rem;max-width:14ch}
h1 em{font-style:normal;color:var(--safe)}
.lede{font-size:1.25rem;max-width:34ch;margin:0;color:var(--dim)}

.safelight{display:flex;gap:.9rem;align-items:center;margin:0 0 3rem;font:.95rem/1.4 var(--sans);color:var(--dim)}
.safelight i{flex:none;width:1.1rem;height:1.1rem;border-radius:50%;background:var(--safe);
  box-shadow:0 0 0 .3rem rgba(255,90,69,.18),0 0 2rem .4rem rgba(255,60,40,.55)}

.sr{position:absolute;left:-999px}
.strip{list-style:none;margin:0 0 4.5rem;padding:0;display:grid;grid-template-columns:repeat(3,1fr)}
.strip li{padding:1.5rem 1.25rem 1.25rem;min-height:11rem;display:flex;flex-direction:column;justify-content:space-between}
.strip li:nth-child(1){background:#26221e}
.strip li:nth-child(2){background:#34302a}
.strip li:nth-child(3){background:#443f37}
.day{font:700 2.4rem/1 var(--sans);letter-spacing:-.02em}
.hours{font:1rem/1.4 var(--mono)}
.count{font:.9rem/1.3 var(--sans);color:var(--dim)}
.strip li:nth-child(3) .count{color:#d6cdbb}

.cols{display:grid;grid-template-columns:1.25fr 1fr;gap:3rem 4rem;align-items:start}
h2{font:700 1.5rem/1.1 var(--sans);letter-spacing:-.015em;margin:0 0 .9rem}
p{margin:0 0 1rem}
.price{font:700 4.5rem/.9 var(--sans);letter-spacing:-.04em;margin:0 0 1rem}
.price small{font:400 1rem/1 var(--sans);letter-spacing:0;color:var(--dim);margin-left:.4rem}
.intro{padding-top:.4rem}
.intro p{color:var(--dim)}

.join{display:inline-block;margin-top:.5rem;padding:.8rem 1.2rem;background:var(--safe);color:#1a0f0d;
  text-decoration:none;font:700 1rem/1 var(--sans);border-radius:2px}
.join:hover{background:#ff7664}
.join:focus-visible{outline:2px solid var(--text);outline-offset:3px}

@media (max-width:46rem){
  .strip{grid-template-columns:1fr}
  .strip li{min-height:0;flex-direction:row;align-items:baseline;flex-wrap:wrap;gap:.25rem 1.25rem}
  .strip .day{min-width:4rem}
  .cols{grid-template-columns:1fr}
}
</style></head><body><div class="wrap">

<header>
  <span class="name">Fixer Street Darkroom</span>
  <span>Back of the old print works, 9 Fixer Street, Calder Mills</span>
</header>

<main>
<div class="hero">
  <h1>Black-and-white printing by hand, for <em>anyone</em> who wants to learn.</h1>
  <p class="lede">Eight enlargers, shared chemistry, and someone on every session who has done this for years.</p>
</div>

<p class="safelight"><i aria-hidden="true"></i>Red light on over the door means someone is printing. Knock and wait.</p>

<h2 class="sr">Open sessions</h2>
<ul class="strip">
  <li><span class="day">Tue</span><span class="hours">6&ndash;10 pm</span><span class="count">6 enlargers</span></li>
  <li><span class="day">Thu</span><span class="hours">6&ndash;10 pm</span><span class="count">6 enlargers</span></li>
  <li><span class="day">Sat</span><span class="hours">10 am&ndash;4 pm</span><span class="count">8 enlargers</span></li>
</ul>

<div class="cols">
  <section>
    <h2>Membership</h2>
    <p class="price">&pound;18<small>a month</small></p>
    <p>Covers every open session, chemistry and a drying rack. Bring your own paper and negatives. Your first session is free if you come along with a member.</p>
    <a class="join" href="mailto:hello@fixerstreet.example">Ask about joining</a>
  </section>
  <section class="intro">
    <h2>Intro evening</h2>
    <p>First Tuesday of each month. We develop one roll together and make a contact sheet.</p>
    <p>No experience needed; bring a roll of exposed black-and-white film.</p>
  </section>
</div>
</main>
</div></body></html>
```

**Things to check**

- The fonts are system fonts, so it will look slightly different on Windows and Android. A real typeface would help most. Something with character for the headline, like a condensed grotesque, would make it less generic.
- Real photos would do more than any CSS. Try a print in the tray, a contact sheet, or the room itself. Even one image of your own would stop it looking templated.
- I left your placeholder `hello@fixerstreet.example` email as it was.
