I couldn't save the file because the Write tool is disabled in this session. The full HTML is below, so you can save it as `index.html`. I haven't opened it in a browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Library Catalog</title>
<style>
  :root {
    /* spacing scale (4px base) */
    --s1: 4px;
    --s2: 8px;
    --s3: 12px;
    --s4: 16px;
    --s5: 24px;
    --s6: 32px;
  }
  * { box-sizing: border-box; margin: 0; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    line-height: 1.5;
    color: #1f2328;
    background: #f4f5f7;
    padding: var(--s6) var(--s4);
  }
  .list {
    display: flex;
    flex-direction: column;
    gap: var(--s5);            /* between cards >= card padding */
    max-width: 560px;
    margin: 0 auto;
    list-style: none;
    padding: 0;
  }
  .card {
    display: flex;
    flex-direction: column;
    background: #fff;
    border: 1px solid #dfe2e6;
    border-radius: 10px;
    padding: var(--s5);
  }
  .title {
    font-size: 1.125rem;
    line-height: 1.3;
    font-weight: 650;
  }
  .author {
    margin-top: var(--s1);     /* title + author: tightest pair */
    font-size: 0.875rem;
    color: #5b636d;
  }
  .synopsis {
    margin-top: var(--s3);     /* text block, one step out */
    font-size: 0.9375rem;
    color: #333a42;
  }
  .actions {
    display: flex;
    gap: var(--s2);
    margin-top: var(--s5);     /* controls separated from content */
  }
  .btn {
    font: inherit;
    font-size: 0.9375rem;
    font-weight: 600;
    min-height: 44px;
    padding: var(--s2) var(--s5);
    border-radius: 8px;
    border: 1px solid #1d4ed8;
    cursor: pointer;
  }
  .btn-primary { background: #1d4ed8; color: #fff; }
  .btn-primary:hover { background: #1e40af; }
  .btn-secondary { background: #fff; color: #1d4ed8; }
  .btn-secondary:hover { background: #eef3ff; }
  .btn:focus-visible { outline: 3px solid #93b4ff; outline-offset: 2px; }
</style>
</head>
<body>
  <ul class="list">
    <li class="card">
      <h2 class="title">The Ashgrove</h2>
      <p class="author">Robert Pearsall</p>
      <p class="synopsis">Nine strangers are drawn together by an orchard and the fight to save it. A sweeping novel about how deeply human lives are rooted in the land.</p>
      <div class="actions">
        <button class="btn btn-primary" type="button">Reserve</button>
        <button class="btn btn-secondary" type="button">Details</button>
      </div>
    </li>
    <li class="card">
      <h2 class="title">Merriwick</h2>
      <p class="author">Suzanne Clayborn</p>
      <p class="synopsis">Merriwick lives in a vast house of endless corridors and fog. As he explores its mysteries, a dangerous truth about his world begins to surface.</p>
      <div class="actions">
        <button class="btn btn-primary" type="button">Reserve</button>
        <button class="btn btn-secondary" type="button">Details</button>
      </div>
    </li>
    <li class="card">
      <h2 class="title">Binding Switchgrass</h2>
      <p class="author">Rowan Hale Kimbrough</p>
      <p class="synopsis">A botanist weaves science and old family wisdom together. Essays on reciprocity between people and the living world.</p>
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
- **Spacing scale:** every gap and padding now comes from a 4px-based scale (4, 8, 12, 16, 24, 32). The old uniform 16px margin is gone.
- **Inside a card:** the title and author sit tight at 4px, since they read as one unit. The synopsis follows at 12px. The buttons sit further away at 24px, so they read as a separate action group.
- **Between cards:** the cards are separated by a 24px gap, which matches the card padding, so they no longer touch. Each card is a distinct item you can reserve or open, so I kept the card surface, with a border and no shadow.
- **Who owns the gaps:** the list container sets the space between cards, and the actions row sets the space between buttons. No child carries a bottom margin, so nothing doubles up.
- **Buttons:** they are at least 44px tall with 24px side padding, and 8px apart. Reserve is the filled primary button and Details is the outlined secondary one. Both have a visible keyboard focus ring.
- **Fonts and assets:** the page uses a system font stack and has no external assets.
- **Placeholder content:** the three books and their synopses are placeholder text I wrote, so swap in your real data.
