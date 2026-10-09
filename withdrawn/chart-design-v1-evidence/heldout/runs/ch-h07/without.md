I couldn't save the page to disk. The Write tool is disabled in this session, so I haven't written, opened or rendered anything. Here is the full file. Save it as `rail-fares.html` and open it in a browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Rail fares by distance</title>
<style>
  :root { color-scheme: light dark; }
  body { margin: 0; padding: 24px; background: #f9f9f7; font-family: system-ui, -apple-system, "Segoe UI", sans-serif; }
  .viz-root {
    color-scheme: light;
    --surface-1: #fcfcfb; --text-primary: #0b0b0b; --text-secondary: #52514e; --text-muted: #898781;
    --grid: #e1e0d9; --axis: #c3c2b7; --series-1: #2a78d6; --border: rgba(11,11,11,.10);
    position: relative; max-width: 760px; margin: 0 auto; padding: 20px 20px 16px;
    background: var(--surface-1); border: 1px solid var(--border); border-radius: 12px; color: var(--text-primary);
  }
  @media (prefers-color-scheme: dark) {
    body { background: #0d0d0d; }
    .viz-root {
      color-scheme: dark;
      --surface-1: #1a1a19; --text-primary: #fff; --text-secondary: #c3c2b7;
      --grid: #2c2c2a; --axis: #383835; --series-1: #3987e5; --border: rgba(255,255,255,.10);
    }
  }
  h1 { font-size: 18px; font-weight: 600; margin: 0 0 4px; }
  .sub { margin: 0 0 12px; font-size: 13px; color: var(--text-secondary); }
  svg { display: block; width: 100%; height: auto; }
  svg text { font-family: inherit; }
  .tick { font-size: 12px; fill: var(--text-muted); }
  .axis-title { font-size: 12px; fill: var(--text-secondary); }
  .lbl { font-size: 12px; fill: var(--text-primary); font-weight: 600; }
  .note { margin: 12px 0 0; font-size: 13px; color: var(--text-secondary); }
  .note b { color: var(--text-primary); }
  .tip { position: absolute; pointer-events: none; opacity: 0; transition: opacity .1s; padding: 6px 10px;
    background: var(--surface-1); border: 1px solid var(--axis); border-radius: 6px; font-size: 12px;
    color: var(--text-primary); box-shadow: 0 2px 8px rgba(0,0,0,.12); white-space: nowrap; transform: translate(-50%, -100%); }
  .tip span { color: var(--text-secondary); }
  details { margin-top: 12px; font-size: 13px; color: var(--text-secondary); }
  summary { cursor: pointer; }
  table { border-collapse: collapse; margin-top: 8px; font-variant-numeric: tabular-nums; }
  th, td { text-align: right; padding: 4px 14px; border-bottom: 1px solid var(--grid); }
  th:first-child, td:first-child { text-align: left; }
  th { color: var(--text-secondary); font-weight: 500; }
  td { color: var(--text-primary); }
</style>
</head>
<body>
<div class="viz-root" id="root">
  <h1>Rail ticket price by distance</h1>
  <p class="sub">Fare in US dollars; distance doubles at each step (log scale)</p>

  <svg viewBox="0 0 720 390" role="img" aria-labelledby="t d">
    <title id="t">Line chart of rail fare versus distance</title>
    <desc id="d">Fare rises from $2.10 at 5 km to $21.00 at 160 km, increasing more slowly as distance grows. Fares are capped at 160 km.</desc>

    <g stroke="var(--grid)" stroke-width="1">
      <line x1="70" x2="680" y1="30" y2="30"/>
      <line x1="70" x2="680" y1="90" y2="90"/>
      <line x1="70" x2="680" y1="150" y2="150"/>
      <line x1="70" x2="680" y1="210" y2="210"/>
      <line x1="70" x2="680" y1="270" y2="270"/>
    </g>
    <line x1="70" x2="680" y1="330" y2="330" stroke="var(--axis)" stroke-width="1"/>
    <g class="tick" text-anchor="end">
      <text x="62" y="334">$0</text><text x="62" y="274">$5</text><text x="62" y="214">$10</text>
      <text x="62" y="154">$15</text><text x="62" y="94">$20</text><text x="62" y="34">$25</text>
    </g>

    <g class="tick" text-anchor="middle">
      <text x="70" y="350">5</text><text x="192" y="350">10</text><text x="314" y="350">20</text>
      <text x="436" y="350">40</text><text x="558" y="350">80</text><text x="680" y="350">160</text>
    </g>
    <text class="axis-title" x="375" y="378" text-anchor="middle">Distance (km)</text>

    <line x1="680" x2="680" y1="30" y2="330" stroke="var(--text-muted)" stroke-width="1" stroke-dasharray="4 4"/>
    <text class="tick" x="674" y="46" text-anchor="end">Fare cap</text>

    <polyline fill="none" stroke="var(--series-1)" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"
      points="70,304.8 192,289.2 314,260.4 436,219.6 558,156 680,78"/>
    <g id="dots" fill="var(--series-1)" stroke="var(--surface-1)" stroke-width="2">
      <circle cx="70" cy="304.8" r="4"/><circle cx="192" cy="289.2" r="4"/><circle cx="314" cy="260.4" r="4"/>
      <circle cx="436" cy="219.6" r="4"/><circle cx="558" cy="156" r="4"/><circle cx="680" cy="78" r="4"/>
    </g>

    <g class="lbl" text-anchor="middle">
      <text x="70" y="292">$2.10</text><text x="192" y="277">$3.40</text><text x="314" y="248">$5.80</text>
      <text x="436" y="207">$9.20</text><text x="558" y="144">$14.50</text>
      <text x="670" y="66" text-anchor="end">$21.00</text>
    </g>

    <g id="hits" fill="transparent">
      <rect x="9" y="30" width="122" height="300" data-i="0"/><rect x="131" y="30" width="122" height="300" data-i="1"/>
      <rect x="253" y="30" width="122" height="300" data-i="2"/><rect x="375" y="30" width="122" height="300" data-i="3"/>
      <rect x="497" y="30" width="122" height="300" data-i="4"/><rect x="619" y="30" width="80" height="300" data-i="5"/>
    </g>
    <line id="cross" y1="30" y2="330" stroke="var(--text-muted)" stroke-width="1" opacity="0"/>
  </svg>

  <p class="note"><b>Note:</b> Fares are capped at 160 km, so trips longer than that cost the same $21.00.</p>

  <details>
    <summary>View as table</summary>
    <table>
      <thead><tr><th>Distance</th><th>Fare</th></tr></thead>
      <tbody>
        <tr><td>5 km</td><td>$2.10</td></tr><tr><td>10 km</td><td>$3.40</td></tr>
        <tr><td>20 km</td><td>$5.80</td></tr><tr><td>40 km</td><td>$9.20</td></tr>
        <tr><td>80 km</td><td>$14.50</td></tr><tr><td>160 km (cap)</td><td>$21.00</td></tr>
      </tbody>
    </table>
  </details>

  <div class="tip" id="tip"></div>
</div>

<script>
  const data = [[5, 2.10], [10, 3.40], [20, 5.80], [40, 9.20], [80, 14.50], [160, 21.00]];
  const svg = document.querySelector('svg'), root = document.getElementById('root');
  const tip = document.getElementById('tip'), cross = document.getElementById('cross');
  const dots = document.querySelectorAll('#dots circle');

  document.querySelectorAll('#hits rect').forEach(r => {
    r.addEventListener('mouseenter', () => {
      const i = +r.dataset.i, [km, fare] = data[i], d = dots[i];
      const s = svg.getBoundingClientRect(), p = root.getBoundingClientRect(), k = s.width / 720;
      tip.innerHTML = `<b>${km} km</b> <span>$${fare.toFixed(2)}${i === 5 ? ' · capped' : ''}</span>`;
      tip.style.left = (s.left - p.left + +d.getAttribute('cx') * k) + 'px';
      tip.style.top = (s.top - p.top + +d.getAttribute('cy') * k - 12) + 'px';
      tip.style.opacity = 1;
      cross.setAttribute('x1', d.getAttribute('cx')); cross.setAttribute('x2', d.getAttribute('cx'));
      cross.setAttribute('opacity', 1);
      d.setAttribute('r', 6);
    });
    r.addEventListener('mouseleave', () => {
      tip.style.opacity = 0; cross.setAttribute('opacity', 0);
      dots.forEach(d => d.setAttribute('r', 4));
    });
  });
</script>
</body>
</html>
```

- **Chart:** a single-series line chart with the x-axis on a log scale. Your distances double at each step, so the points are evenly spaced. The curve shows fares rising more slowly as distance grows: $2.10 at 5 km, $21.00 at 160 km.
- **Cap note:** a dashed "Fare cap" line sits at 160 km. A note below the chart reads "Fares are capped at 160 km, so trips longer than that cost the same $21.00." That second sentence is my reading of "capped". Edit it if the cap works differently.
- **Labels and hover:** every point has a direct dollar label, and hovering a point shows a tooltip and crosshair.
- **Accessibility:** there is a "View as table" toggle, and the SVG has a title and description.
- **Dark mode:** it follows the system setting. I used the skill's reference palette (blue `#2a78d6` in light mode, `#3987e5` in dark) without running its validator. With only one series there is no categorical palette to validate.

I haven't rendered the page, so the label spacing and tooltip position are unchecked. The hand-computed point coordinates are the likeliest thing to be off.
