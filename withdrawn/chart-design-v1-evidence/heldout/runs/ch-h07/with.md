I couldn't save the page to disk because the Write tool is disabled in this session. The full HTML is below, so you can save it as `rail-fares.html` and open it in a browser. I haven't rendered it, so the layout is untested.

It's a line chart with distance on a linear x-axis and fare on a y-axis that starts at $0. Each point has its fare labeled directly, and a dashed flat line continues past 160 km to show the cap. A short note below the chart states that fares are capped at 160 km, and a data table underneath gives the exact values.

I added two things you didn't ask for. The title states the finding: longer trips cost more, but each extra kilometre costs less. The table also has a per-km column, which I calculated from your fares. The dashed line past 160 km assumes "capped" means the price stays at $21.00 for any longer trip.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Rail fares by distance</title>
<style>
  body { font-family: system-ui, sans-serif; color: #222; max-width: 760px; margin: 2rem auto; padding: 0 1rem; }
  h1 { font-size: 1.3rem; margin: 0 0 .25rem; }
  p.sub { margin: 0 0 1rem; color: #555; }
  svg { width: 100%; height: auto; display: block; }
  svg text { font-family: inherit; }
  .note { margin: 1rem 0; padding: .6rem .8rem; border-left: 3px solid #1f5fa8; background: #f3f6fa; }
  table { border-collapse: collapse; font-size: .9rem; }
  th, td { padding: .25rem .9rem; text-align: right; border-bottom: 1px solid #ddd; }
  th:first-child, td:first-child { text-align: left; }
  details { margin-top: 1rem; }
</style>
</head>
<body>
<h1>Longer trips cost more, but each extra kilometre costs less</h1>
<p class="sub">One-way rail ticket price by trip distance</p>

<svg viewBox="0 0 720 400" role="img" aria-labelledby="t d">
  <title id="t">Line chart of rail ticket price by distance</title>
  <desc id="d">Fares rise from $2.10 at 5 km to $21.00 at 160 km, rising more slowly as distance grows. Fares are capped at 160 km, so the price stays at $21.00 beyond that.</desc>

  <g stroke="#e3e3e3" stroke-width="1">
    <line x1="60" x2="690" y1="282" y2="282"/>
    <line x1="60" x2="690" y1="219" y2="219"/>
    <line x1="60" x2="690" y1="156" y2="156"/>
    <line x1="60" x2="690" y1="93" y2="93"/>
    <line x1="60" x2="690" y1="30" y2="30"/>
  </g>
  <line x1="60" x2="690" y1="345" y2="345" stroke="#888"/>
  <g font-size="12" fill="#666" text-anchor="end">
    <text x="52" y="349">$0</text>
    <text x="52" y="286">$5</text>
    <text x="52" y="223">$10</text>
    <text x="52" y="160">$15</text>
    <text x="52" y="97">$20</text>
    <text x="52" y="34">$25</text>
  </g>
  <g font-size="12" fill="#666" text-anchor="middle">
    <text x="60" y="364">0</text>
    <text x="186" y="364">40</text>
    <text x="312" y="364">80</text>
    <text x="438" y="364">120</text>
    <text x="564" y="364">160</text>
    <text x="690" y="364">200</text>
  </g>
  <text x="375" y="389" font-size="13" fill="#444" text-anchor="middle">Trip distance (km)</text>
  <text x="60" y="18" font-size="13" fill="#444">Fare (USD)</text>

  <line x1="564" x2="690" y1="80.4" y2="80.4" stroke="#1f5fa8" stroke-width="2.5" stroke-dasharray="6 4"/>
  <line x1="564" x2="564" y1="80.4" y2="345" stroke="#999" stroke-dasharray="2 4"/>
  <text x="690" y="66" font-size="13" fill="#1f5fa8" text-anchor="end" font-weight="600">Capped at 160 km: $21.00 for any longer trip</text>

  <polyline fill="none" stroke="#1f5fa8" stroke-width="2.5" stroke-linejoin="round"
    points="75.75,318.54 91.5,302.16 123,271.92 186,229.08 312,162.3 564,80.4"/>
  <g fill="#1f5fa8">
    <circle cx="75.75" cy="318.54" r="4"/>
    <circle cx="91.5" cy="302.16" r="4"/>
    <circle cx="123" cy="271.92" r="4"/>
    <circle cx="186" cy="229.08" r="4"/>
    <circle cx="312" cy="162.3" r="4"/>
    <circle cx="564" cy="80.4" r="4"/>
  </g>

  <g font-size="12" fill="#222">
    <text x="84" y="336">$2.10</text>
    <text x="100" y="319">$3.40</text>
    <text x="131" y="289">$5.80</text>
    <text x="194" y="246">$9.20</text>
    <text x="320" y="179">$14.50</text>
    <text x="572" y="97">$21.00</text>
  </g>
</svg>

<div class="note"><strong>Note:</strong> fares are capped at 160 km. Trips longer than 160 km cost the same $21.00.</div>

<details open>
  <summary>Data</summary>
  <table>
    <thead><tr><th>Distance</th><th>Fare</th><th>Per km</th></tr></thead>
    <tbody>
      <tr><td>5 km</td><td>$2.10</td><td>$0.42</td></tr>
      <tr><td>10 km</td><td>$3.40</td><td>$0.34</td></tr>
      <tr><td>20 km</td><td>$5.80</td><td>$0.29</td></tr>
      <tr><td>40 km</td><td>$9.20</td><td>$0.23</td></tr>
      <tr><td>80 km</td><td>$14.50</td><td>$0.18</td></tr>
      <tr><td>160 km</td><td>$21.00</td><td>$0.13</td></tr>
    </tbody>
  </table>
</details>
</body>
</html>
```

If you'd like me to save it to the working directory, enable Write and I'll do it.
