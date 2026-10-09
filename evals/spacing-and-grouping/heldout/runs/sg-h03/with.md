I couldn't save the file because the Write tool is disabled in this session. The full HTML is below, so you can save it as `index.html`. I haven't opened it in a browser.

The spacing is based on the relationships between the elements:
- **Title and author:** 4px apart, so they read as one heading unit.
- **Author and synopsis:** 12px.
- **Synopsis and buttons:** 24px, so the actions read as a separate group.
- **Cards:** each is now a bordered surface with 24px padding. The gap between cards is 24px, set once by the list container rather than by margins on each card, so cards no longer touch.
- **Buttons:** 8px apart, at least 44px tall, with 24px side padding. "Reserve" is filled and "Details" is outlined, so the main action stands out.
- **Synopsis:** clamped to 2 lines.
- **Values:** every spacing value comes from a 4/8/12/16/24/32 scale.
- **Narrow screens:** card padding and the gap above the buttons drop to 16px.
- **Fonts and assets:** system fonts only, with no external assets.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Library Catalog</title>
<style>
  :root {
    --space-1: 4px;
    --space-2: 8px;
    --space-3: 12px;
    --space-4: 16px;
    --space-5: 24px;
    --space-6: 32px;
    --ink: #1c1f24;
    --muted: #5b6370;
    --line: #dde1e6;
    --bg: #f5f6f8;
    --surface: #fff;
    --accent: #1f5fbf;
  }

  * { box-sizing: border-box; margin: 0; }

  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 16px;
    line-height: 1.5;
    color: var(--ink);
    background: var(--bg);
    padding: var(--space-6) var(--space-4);
  }

  .card-list {
    max-width: 640px;
    margin: 0 auto;
    padding: 0;
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: var(--space-5);
  }

  .card {
    display: flex;
    flex-direction: column;
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 8px;
    padding: var(--space-5);
  }

  .title {
    font-size: 1.25rem;
    line-height: 1.3;
    font-weight: 650;
  }

  .author {
    margin-top: var(--space-1);
    font-size: 0.9375rem;
    color: var(--muted);
  }

  .synopsis {
    margin-top: var(--space-3);
    display: -webkit-box;
    -webkit-line-clamp: 2;
    line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .actions {
    margin-top: var(--space-5);
    display: flex;
    flex-wrap: wrap;
    gap: var(--space-2);
  }

  .btn {
    font: inherit;
    font-weight: 600;
    min-height: 44px;
    padding: var(--space-2) var(--space-5);
    border-radius: 6px;
    border: 1px solid var(--accent);
    cursor: pointer;
  }

  .btn-primary { background: var(--accent); color: #fff; }
  .btn-secondary { background: transparent; color: var(--accent); }

  .btn:hover { filter: brightness(0.94); }
  .btn:focus-visible { outline: 3px solid #8db4ee; outline-offset: 2px; }

  @media (max-width: 480px) {
    body { padding: var(--space-5) var(--space-4); }
    .card { padding: var(--space-4); }
    .actions { margin-top: var(--space-4); }
  }
</style>
</head>
<body>
  <ul class="card-list">
    <li class="card">
      <h2 class="title">The Hollow Canopy</h2>
      <p class="author">Reuben Ashgrove</p>
      <p class="synopsis">Nine strangers are drawn together by trees, each bringing a story of loss and wonder. Their paths converge in a fight to protect what remains of the American forest.</p>
      <div class="actions">
        <button class="btn btn-primary" type="button">Reserve</button>
        <button class="btn btn-secondary" type="button">Details</button>
      </div>
    </li>
    <li class="card">
      <h2 class="title">Halcyon Reach</h2>
      <p class="author">Selwyn Ashcombe</p>
      <p class="synopsis">Corvane lives in a vast house of endless halls and tides, keeping careful journals of its wonders. When strange signs appear, he begins to question everything he knows.</p>
      <div class="actions">
        <button class="btn btn-primary" type="button">Reserve</button>
        <button class="btn btn-secondary" type="button">Details</button>
      </div>
    </li>
    <li class="card">
      <h2 class="title">Weaving Wild Barley</h2>
      <p class="author">Rowan Hale Tamsen</p>
      <p class="synopsis">A field botanist weaves science and old family lore into essays on reciprocity. A guide to seeing the living world as a gift.</p>
      <div class="actions">
        <button class="btn btn-primary" type="button">Reserve</button>
        <button class="btn btn-secondary" type="button">Details</button>
      </div>
    </li>
  </ul>
</body>
</html>
```
