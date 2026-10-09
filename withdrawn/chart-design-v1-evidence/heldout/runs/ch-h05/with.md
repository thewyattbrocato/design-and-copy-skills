I couldn't save `chart.html` because the Write tool is disabled in this session. The full file is below, so you can save it yourself. I haven't opened it in a browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Q4 jumped to 90</title>
<style>
  body { margin: 0; padding: 32px 16px; font-family: system-ui, -apple-system, "Segoe UI", sans-serif; color: #1f2933; background: #fff; }
  figure { max-width: 640px; margin: 0 auto; }
  h1 { font-size: 20px; font-weight: 600; margin: 0 0 4px; }
  p.sub { margin: 0 0 12px; color: #616e7c; font-size: 14px; }
  svg { width: 100%; height: auto; display: block; }
  .grid { stroke: #e4e7eb; stroke-width: 1; }
  .base { stroke: #9aa5b1; stroke-width: 1; }
  .tick { fill: #616e7c; font-size: 12px; }
  .cat { fill: #323f4b; font-size: 14px; }
  .val { fill: #323f4b; font-size: 14px; font-weight: 600; }
  .val.hi { fill: #1d4ed8; }
  .bar { fill: #b8c2cc; }
  .bar.hi { fill: #2563eb; }
  table { margin-top: 12px; font-size: 13px; border-collapse: collapse; color: #616e7c; }
  th, td { padding: 2px 12px 2px 0; text-align: left; font-weight: normal; }
  details { margin-top: 8px; }
  summary { font-size: 13px; color: #616e7c; cursor: pointer; }
</style>
</head>
<body>
<figure>
  <h1>Q4 jumped to 90, up from 58 in Q3</h1>
  <p class="sub">Value by quarter (axis starts at 0)</p>
  <svg id="chart" viewBox="0 0 640 360" role="img"
       aria-label="Bar chart of value by quarter: Q1 52, Q2 61, Q3 58, Q4 90."></svg>
  <details>
    <summary>View data as table</summary>
    <table>
      <thead><tr><th>Quarter</th><th>Value</th></tr></thead>
      <tbody>
        <tr><td>Q1</td><td>52</td></tr>
        <tr><td>Q2</td><td>61</td></tr>
        <tr><td>Q3</td><td>58</td></tr>
        <tr><td>Q4</td><td>90</td></tr>
      </tbody>
    </table>
  </details>
</figure>
<script>
(function () {
  var data = [["Q1", 52], ["Q2", 61], ["Q3", 58], ["Q4", 90]];
  var max = 100, step = 20;
  var m = { top: 16, right: 16, bottom: 34, left: 36 };
  var W = 640, H = 360;
  var pw = W - m.left - m.right, ph = H - m.top - m.bottom;
  var ns = "http://www.w3.org/2000/svg";
  var svg = document.getElementById("chart");

  function el(name, attrs, text) {
    var e = document.createElementNS(ns, name);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (text != null) e.textContent = text;
    svg.appendChild(e);
    return e;
  }
  function y(v) { return m.top + ph - (v / max) * ph; }

  for (var t = 0; t <= max; t += step) {
    el("line", { x1: m.left, x2: m.left + pw, y1: y(t), y2: y(t), "class": t === 0 ? "base" : "grid" });
    el("text", { x: m.left - 8, y: y(t) + 4, "text-anchor": "end", "class": "tick" }, t);
  }

  var slot = pw / data.length, bw = slot * 0.55;
  data.forEach(function (d, i) {
    var hi = i === data.length - 1;
    var x = m.left + slot * i + (slot - bw) / 2;
    el("rect", { x: x, y: y(d[1]), width: bw, height: y(0) - y(d[1]), "class": "bar" + (hi ? " hi" : "") });
    el("text", { x: x + bw / 2, y: y(d[1]) - 6, "text-anchor": "middle", "class": "val" + (hi ? " hi" : "") }, d[1]);
    el("text", { x: x + bw / 2, y: y(0) + 22, "text-anchor": "middle", "class": "cat" }, d[0]);
  });
})();
</script>
</body>
</html>
```

**What changed**
- **3D and gradient:** The bars are now flat, solid fills with no shadows.
- **Y axis:** It runs 0–100 instead of 40–100. Bar length is the value, so a 40 baseline made Q4 look about four times Q1 when it's about 1.7 times. The ticks are every 20.
- **Gridlines:** They are faint gray and every 20 units, not black every 10. The zero baseline is slightly darker.
- **Legend:** It's gone, since a single series doesn't need one.
- **Value labels:** Each bar has its value printed on top, so the axis is a backup rather than something you have to read from.
- **Color:** Q1–Q3 are gray and Q4 is blue, so the eye goes to the jump.
- **Title:** "Chart" became "Q4 jumped to 90, up from 58 in Q3". The subtitle notes that the axis starts at 0.
- **Accessibility:** The SVG has an `aria-label`, and a collapsible "View data as table" sits under the chart.

Your data has no unit or measure name, so the subtitle just says "Value by quarter". Tell me what it measures, such as revenue in $k, and I'll add it to the subtitle and axis.
