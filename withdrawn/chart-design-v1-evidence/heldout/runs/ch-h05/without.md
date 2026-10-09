I couldn't save the file because the Write tool is disabled in this session, so nothing has been written to disk and I haven't rendered the chart. The full file is below. Save it as `chart.html` and open it in a browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Quarterly results</title>
<style>
  :root { color-scheme: light dark; }
  body {
    margin: 0; padding: 32px 16px; background: #f9f9f7;
    font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  }
  .viz-root {
    --surface-1: #fcfcfb; --text-primary: #0b0b0b; --text-secondary: #52514e;
    --text-muted: #898781; --grid: #e1e0d9; --axis: #c3c2b7;
    --series-1: #2a78d6; --border: rgba(11,11,11,.10);
    position: relative; max-width: 560px; margin: 0 auto; padding: 20px 20px 12px;
    background: var(--surface-1); border: 1px solid var(--border); border-radius: 12px;
    color: var(--text-primary);
  }
  @media (prefers-color-scheme: dark) {
    body { background: #0d0d0d; }
    .viz-root {
      --surface-1: #1a1a19; --text-primary: #fff; --text-secondary: #c3c2b7;
      --grid: #2c2c2a; --axis: #383835; --series-1: #3987e5;
      --border: rgba(255,255,255,.10);
    }
  }
  h1 { margin: 0; font-size: 16px; font-weight: 600; }
  p.sub { margin: 4px 0 12px; font-size: 13px; color: var(--text-secondary); }
  svg { display: block; width: 100%; height: auto; overflow: visible; }
  svg text { font-family: inherit; }
  .tick { font-size: 12px; fill: var(--text-muted); font-variant-numeric: tabular-nums; }
  .cat  { font-size: 13px; fill: var(--text-secondary); }
  .val  { font-size: 13px; font-weight: 600; fill: var(--text-primary); }
  .grid { stroke: var(--grid); stroke-width: 1; }
  .base { stroke: var(--axis); stroke-width: 1; }
  .bar  { fill: var(--series-1); transition: opacity .12s; }
  svg.dim .bar { opacity: .45; }
  svg.dim .bar.on { opacity: 1; }
  .hit { fill: transparent; cursor: default; }
  #tip {
    position: absolute; pointer-events: none; opacity: 0; transition: opacity .1s;
    background: var(--surface-1); border: 1px solid var(--axis); border-radius: 8px;
    padding: 6px 10px; font-size: 13px; box-shadow: 0 2px 8px rgba(0,0,0,.12);
    transform: translate(-50%, -100%); white-space: nowrap;
  }
  #tip b { font-variant-numeric: tabular-nums; }
  details { margin-top: 8px; font-size: 13px; color: var(--text-secondary); }
  summary { cursor: pointer; padding: 4px 0; }
  table { border-collapse: collapse; margin-top: 4px; }
  th, td { text-align: left; padding: 4px 24px 4px 0; border-bottom: 1px solid var(--grid); }
  td:last-child, th:last-child { text-align: right; padding-right: 0; font-variant-numeric: tabular-nums; }
</style>
</head>
<body>
<div class="viz-root">
  <h1>Quarterly results</h1>
  <p class="sub">Score by quarter, Q1–Q4</p>
  <svg id="chart" viewBox="0 0 520 330" role="img"
       aria-label="Bar chart of quarterly values: Q1 52, Q2 61, Q3 58, Q4 90."></svg>
  <div id="tip"></div>
  <details>
    <summary>View as table</summary>
    <table><thead><tr><th>Quarter</th><th>Value</th></tr></thead><tbody id="rows"></tbody></table>
  </details>
</div>
<script>
  const data = [["Q1", 52], ["Q2", 61], ["Q3", 58], ["Q4", 90]];
  const L = 36, R = 516, T = 16, B = 290, MAX = 100, BAR = 24, R4 = 4;
  const y = v => B - (B - T) * v / MAX;
  const band = (R - L) / data.length;
  const svg = document.getElementById("chart"), tip = document.getElementById("tip");
  const NS = "http://www.w3.org/2000/svg";
  const el = (n, a, t) => {
    const e = document.createElementNS(NS, n);
    for (const k in a) e.setAttribute(k, a[k]);
    if (t != null) e.textContent = t;
    svg.appendChild(e); return e;
  };

  for (const t of [0, 25, 50, 75, 100]) {
    if (t) el("line", { class: "grid", x1: L, x2: R, y1: y(t), y2: y(t) });
    el("text", { class: "tick", x: L - 8, y: y(t) + 4, "text-anchor": "end" }, t);
  }
  el("line", { class: "base", x1: L, x2: R, y1: B, y2: B });

  data.forEach(([q, v], i) => {
    const cx = L + band * (i + .5), x = cx - BAR / 2, top = y(v);
    // rounded data-end, square at the baseline
    const bar = el("path", { class: "bar", d:
      `M${x} ${B}V${top + R4}Q${x} ${top} ${x + R4} ${top}H${x + BAR - R4}` +
      `Q${x + BAR} ${top} ${x + BAR} ${top + R4}V${B}Z` });
    el("text", { class: "val", x: cx, y: top - 8, "text-anchor": "middle" }, v);
    el("text", { class: "cat", x: cx, y: B + 22, "text-anchor": "middle" }, q);
    const hit = el("rect", { class: "hit", x: cx - band / 2, y: T, width: band, height: B - T + 30 });
    hit.addEventListener("mouseenter", () => {
      svg.classList.add("dim"); bar.classList.add("on");
      tip.innerHTML = `${q}: <b>${v}</b>`;
      const s = svg.getBoundingClientRect(), p = svg.parentNode.getBoundingClientRect();
      tip.style.left = (s.left - p.left + cx * s.width / 520) + "px";
      tip.style.top = (s.top - p.top + (top - 28) * s.height / 330) + "px";
      tip.style.opacity = 1;
    });
    hit.addEventListener("mouseleave", () => {
      svg.classList.remove("dim"); bar.classList.remove("on"); tip.style.opacity = 0;
    });
  });

  document.getElementById("rows").innerHTML =
    data.map(([q, v]) => `<tr><td>${q}</td><td>${v}</td></tr>`).join("");
</script>
</body>
</html>
```

**What I changed**
- **3D effect and gradient:** removed both. The bars are flat, one solid blue, with a 4px rounded top and a square base.
- **Gridlines:** they are now thin, light gray and solid instead of black. They sit every 25 units instead of every 10, which leaves 5 labelled ticks instead of 11.
- **Legend:** removed. With one series, the title already says what is plotted.
- **Y axis:** it now runs 0–100 instead of 40–100. Bar length encodes value, so starting at 40 made Q4 look about 4× Q1 when it is about 1.7×.
- **Labels:** each bar has its value at the tip and its Q1–Q4 label below. I kept the value on all four bars because there are so few.
- **Title:** I replaced "Chart" with "Quarterly results" and a subtitle. That is a placeholder, so swap in the real metric name and unit.
- **Added:** hover tooltips, a collapsible "View as table", and automatic dark mode.

I didn't run the palette validator. The blue comes from the skill's pre-validated palette (`#2a78d6` in light mode, `#3987e5` in dark), and a single series has no adjacent-color pairs to check.
