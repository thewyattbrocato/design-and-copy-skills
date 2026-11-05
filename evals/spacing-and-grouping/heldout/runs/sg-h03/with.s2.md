I couldn't save the file because the Write tool is disabled in this session. The full HTML is below, so you can save it as `index.html`. I haven't opened it in a browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Library Books</title>
<style>
  :root {
    --space-1: 4px;
    --space-2: 8px;
    --space-3: 12px;
    --space-4: 16px;
    --space-5: 24px;
    --space-6: 32px;
    --ink: #1c1f26;
    --muted: #5b6270;
    --line: #dde1e8;
    --bg: #f4f5f7;
    --accent: #1f5fbf;
  }
  * { box-sizing: border-box; margin: 0; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: var(--ink);
    background: var(--bg);
    line-height: 1.5;
    padding: var(--space-6) var(--space-4);
  }
  .list {
    display: flex;
    flex-direction: column;
    gap: var(--space-5);          /* parent owns the gap between cards */
    max-width: 560px;
    margin: 0 auto;
    list-style: none;
    padding: 0;
  }
  .card {
    display: flex;
    flex-direction: column;
    gap: var(--space-4);          /* between text block and actions */
    padding: var(--space-5);
    background: #fff;
    border: 1px solid var(--line);
    border-radius: 12px;
  }
  .text { display: flex; flex-direction: column; gap: var(--space-3); }
  .head { display: flex; flex-direction: column; gap: var(--space-1); }  /* title + author: tightest */
  h2 { font-size: 1.25rem; line-height: 1.3; }
  .author { font-size: 0.9375rem; color: var(--muted); }
  .synopsis {
    font-size: 0.9375rem;
    color: #333844;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
  .actions { display: flex; gap: var(--space-2); }
  button {
    font: inherit;
    font-weight: 600;
    min-height: 44px;
    padding: var(--space-3) var(--space-5);
    border-radius: 8px;
    border: 1px solid var(--accent);
    cursor: pointer;
  }
  .reserve { background: var(--accent); color: #fff; }
  .details { background: transparent; color: var(--accent); }
  button:focus-visible { outline: 3px solid #9ec0f5; outline-offset: 2px; }
  @media (max-width: 420px) {
    .actions button { flex: 1; padding-inline: var(--space-4); }
  }
</style>
</head>
<body>
  <ul class="list">
    <li class="card">
      <div class="text">
        <div class="head">
          <h2>The Stillness of Dusk</h2>
          <p class="author">Kaspar Ingleby</p>
        </div>
        <p class="synopsis">An aging steward reflects on a lifetime of service and the choices he made in the name of dignity, loyalty and duty, as a coastal trip forces him to face what he gave up.</p>
      </div>
      <div class="actions">
        <button class="reserve" type="button">Reserve</button>
        <button class="details" type="button">Details</button>
      </div>
    </li>
    <li class="card">
      <div class="text">
        <div class="head">
          <h2>Merriwick</h2>
          <p class="author">Suzanne Clayborn</p>
        </div>
        <p class="synopsis">Merriwick lives in a vast house of endless corridors and fog, keeping careful journals of its wonders, until signs appear that someone else is there and his world begins to unravel.</p>
      </div>
      <div class="actions">
        <button class="reserve" type="button">Reserve</button>
        <button class="details" type="button">Details</button>
      </div>
    </li>
    <li class="card">
      <div class="text">
        <div class="head">
          <h2>A Guest at the Grand Meridian</h2>
          <p class="author">Amos Thornbury</p>
        </div>
        <p class="synopsis">Sentenced to house arrest in a grand harbor hotel, Count Halvard finds a life of unexpected purpose and friendship while decades of upheaval unfold outside its doors.</p>
      </div>
      <div class="actions">
        <button class="reserve" type="button">Reserve</button>
        <button class="details" type="button">Details</button>
      </div>
    </li>
  </ul>
</body>
</html>
```

**What changed in the spacing**
- **Three levels instead of one value:**
  - Title to author is 4px, so they read as one heading.
  - Heading to synopsis is 12px.
  - Text block to buttons is 16px.
  - The closer items sit, the more closely related they are.
- **Cards:** there is now a 24px gap between cards, where before they touched. Each card has 24px of padding, so the gap is never smaller than the padding and the cards don't blur together. Each card is a white surface with a hairline border and no shadow.
- **Gaps owned by the parent:** spacing comes from flex `gap` on the containers, not from margins on every element. There's no doubled space after the last item.
- **Buttons:** each is at least 44px tall, with horizontal padding about twice the vertical, and an 8px gap between them. "Reserve" is the filled primary button and "Details" is the outlined secondary one. On narrow screens they share the row equally.
- **Synopsis:** it is clamped to two lines.
- **Spacing scale:** every value comes from one scale (4, 8, 12, 16, 24 and 32px), kept as CSS custom properties.

The book titles and synopses are placeholders. Swap in your real data.
