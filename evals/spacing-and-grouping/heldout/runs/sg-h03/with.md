I couldn't save the file because the Write tool is disabled in this session. The full file is below, so you can save it as `index.html`. I haven't opened it in a browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Library Catalog</title>
<style>
  :root {
    --s1: 4px;
    --s2: 8px;
    --s3: 12px;
    --s5: 24px;
    --s6: 32px;
    --ink: #1c1e21;
    --muted: #5b6168;
    --line: #d9dce0;
    --accent: #1d4ed8;
  }
  * { box-sizing: border-box; margin: 0; }
  body {
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
    color: var(--ink);
    background: #f4f5f7;
    line-height: 1.5;
    padding: var(--s6) var(--s5);
  }
  .list {
    max-width: 560px;
    margin: 0 auto;
    padding: 0;
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: var(--s5);
  }
  .card {
    background: #fff;
    border: 1px solid var(--line);
    border-radius: 12px;
    padding: var(--s5);
  }
  .title { font-size: 1.25rem; line-height: 1.3; font-weight: 650; }
  .author { margin-top: var(--s1); font-size: 0.9375rem; color: var(--muted); }
  .synopsis {
    margin-top: var(--s3);
    font-size: 0.9375rem;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
  .actions { margin-top: var(--s5); display: flex; flex-wrap: wrap; gap: var(--s3); }
  .btn {
    font: inherit;
    font-weight: 600;
    font-size: 0.9375rem;
    min-height: 44px;
    padding: var(--s2) var(--s5);
    border-radius: 8px;
    border: 1px solid var(--accent);
    cursor: pointer;
  }
  .btn-primary { background: var(--accent); color: #fff; }
  .btn-secondary { background: #fff; color: var(--accent); }
  .btn-primary:hover { background: #1e40af; }
  .btn-secondary:hover { background: #eef3ff; }
  .btn:focus-visible { outline: 3px solid #93b4ff; outline-offset: 2px; }
</style>
</head>
<body>
  <ul class="list">
    <li class="card">
      <h2 class="title">The Lighthouse Keeper's Atlas</h2>
      <p class="author">by Marian Ellery</p>
      <p class="synopsis">A retired cartographer inherits a remote lighthouse and a trunk of unfinished maps, each hinting at a coastline that does not exist. Charting them may cost her the only home she has left.</p>
      <div class="actions">
        <button class="btn btn-primary" type="button">Reserve</button>
        <button class="btn btn-secondary" type="button">Details</button>
      </div>
    </li>
    <li class="card">
      <h2 class="title">Salt and Circuitry</h2>
      <p class="author">by Devika Rao</p>
      <p class="synopsis">In a flooded future city, a marine engineer repairs tidal servers and discovers a message looping beneath the harbor. Someone has been listening to the city for decades.</p>
      <div class="actions">
        <button class="btn btn-primary" type="button">Reserve</button>
        <button class="btn btn-secondary" type="button">Details</button>
      </div>
    </li>
    <li class="card">
      <h2 class="title">A Field Guide to Quiet Places</h2>
      <p class="author">by Tomas Willbright</p>
      <p class="synopsis">Part memoir, part travelogue, this essay collection visits libraries, chapels, and empty train stations to ask what silence does for us and why we keep seeking it out.</p>
      <div class="actions">
        <button class="btn btn-primary" type="button">Reserve</button>
        <button class="btn btn-secondary" type="button">Details</button>
      </div>
    </li>
  </ul>
</body>
</html>
```

**What changed**
- **Spacing inside a card:** the gaps now grow as the content gets less related. Title to author is 4px, since the author line belongs to the title. Author to synopsis is 12px. Synopsis to buttons is 24px, because the buttons are a separate action area.
- **Spacing between cards:** cards are 24px apart instead of touching, which matches the card padding so they don't blur together. The list container sets this gap, so there are no per-element margins and no doubled space after the last card.
- **Card surface:** each card has a white surface with a hairline border and rounded corners. Each book is something you act on as a whole, so a card fits here. I used no shadow, to avoid stacking border, shadow and fill.
- **Buttons:** they are 44px tall with 24px horizontal padding, and sit 12px apart. Reserve is the filled primary button and Details is the outlined secondary one.
- **Synopsis:** it is clamped to 2 lines.
- **Spacing values:** they all come from one small scale of 4, 8, 12, 24 and 32px, defined as custom properties.
