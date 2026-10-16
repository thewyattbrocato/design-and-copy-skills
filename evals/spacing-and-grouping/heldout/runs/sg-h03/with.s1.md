I couldn't save the file because the Write tool is disabled in this session. The full HTML is below, so you can save it as `library-cards.html`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Library Books</title>
<style>
  :root {
    /* 4px-based scale */
    --s1: 4px;
    --s2: 8px;
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
    padding: var(--s6) var(--s5);
  }
  .list {
    display: grid;
    gap: var(--s5);
    max-width: 560px;
    margin: 0 auto;
  }
  .card {
    display: flex;
    flex-direction: column;
    gap: var(--s4);
    padding: var(--s5);
    background: #fff;
    border: 1px solid #dfe2e6;
    border-radius: 12px;
  }
  .text { display: flex; flex-direction: column; gap: var(--s1); }
  .text .synopsis { margin-top: var(--s2); }
  h2 { font-size: 1.25rem; line-height: 1.3; font-weight: 700; }
  .author { font-size: 0.875rem; color: #5b636d; }
  .synopsis {
    color: #333a41;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
  .actions { display: flex; gap: var(--s2); }
  button {
    font: inherit;
    font-weight: 600;
    min-height: 44px;
    padding: var(--s2) var(--s5);
    border-radius: 8px;
    border: 1px solid #1d4ed8;
    cursor: pointer;
  }
  .reserve { background: #1d4ed8; color: #fff; }
  .details { background: #fff; color: #1d4ed8; }
  button:hover { filter: brightness(0.95); }
  button:focus-visible { outline: 3px solid #93b4ff; outline-offset: 2px; }
  @media (max-width: 400px) {
    body { padding: var(--s4); }
    .card { padding: var(--s4); }
    .actions button { flex: 1; padding-inline: var(--s4); }
  }
</style>
</head>
<body>
  <main class="list">
    <article class="card">
      <div class="text">
        <h2>The Ashgrove</h2>
        <p class="author">Robert Pearsall</p>
        <p class="synopsis">Nine strangers, each drawn to the old orchard in different ways, join an effort to save the last of the valley's standing groves.</p>
      </div>
      <div class="actions">
        <button class="reserve" type="button">Reserve</button>
        <button class="details" type="button">Details</button>
      </div>
    </article>

    <article class="card">
      <div class="text">
        <h2>Merriwick</h2>
        <p class="author">Suzanne Clayborn</p>
        <p class="synopsis">Merriwick lives in a vast house of endless corridors and fog. As strange evidence of another person appears, his world begins to unravel.</p>
      </div>
      <div class="actions">
        <button class="reserve" type="button">Reserve</button>
        <button class="details" type="button">Details</button>
      </div>
    </article>

    <article class="card">
      <div class="text">
        <h2>The Stillness of Dusk</h2>
        <p class="author">Kaspar Ingleby</p>
        <p class="synopsis">An aging steward takes a coastal trip in 1956 and reflects on duty, dignity, and the choices that shaped a lifetime of service.</p>
      </div>
      <div class="actions">
        <button class="reserve" type="button">Reserve</button>
        <button class="details" type="button">Details</button>
      </div>
    </article>
  </main>
</body>
</html>
```

I haven't opened it in a browser, so the layout is untested.

**Spacing changes**
- **Gaps by relationship:** the uniform 16px margins are gone. The container now sets the gaps, and each one reflects how closely two things belong together.
  - Title to author is 4px, since they're one unit.
  - Author to synopsis is 12px (the 4px flex gap plus an 8px top margin on the synopsis).
  - Text block to buttons is 16px.
  - Card to card is 24px.
- **Cards:** they no longer touch. The 24px gap equals the card padding, so they don't blur together. Each card has one white surface with a hairline border and no shadow.
- **Padding:** cards have 24px padding on every side.
- **Buttons:** they're 44px tall, with 24px horizontal padding and 8px between them. Reserve is the filled primary button and Details is the outlined secondary one.
- **Scale:** all spacing comes from one small 4px-based scale, with no one-off values.
- **Synopsis:** it's clamped to 2 lines.
- **Narrow screens:** below 400px the padding shrinks and the buttons share the row width.
