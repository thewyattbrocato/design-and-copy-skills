I couldn't save the file because the Write tool is disabled in this session. The full HTML is below, so you can save it as `cards.html`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Library Books</title>
<style>
  :root {
    --s1: 4px;
    --s2: 8px;
    --s4: 16px;
    --s5: 24px;
    --s6: 32px;
    --ink: #1c1b1a;
    --muted: #5f5b57;
    --line: #dcd7d0;
    --bg: #f5f3ef;
    --surface: #fff;
    --accent: #1f4e79;
  }
  * { box-sizing: border-box; margin: 0; }
  body {
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
    font-size: 16px;
    line-height: 1.5;
    color: var(--ink);
    background: var(--bg);
    padding: clamp(16px, 5vw, var(--s6));
  }
  .list {
    list-style: none;
    padding: 0;
    max-width: 560px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: var(--s5);
  }
  .card {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 8px;
    padding: var(--s5);
    display: flex;
    flex-direction: column;
    gap: var(--s4);
  }
  .text { display: flex; flex-direction: column; gap: var(--s1); }
  .title { font-size: 1.25rem; line-height: 1.3; font-weight: 650; }
  .author { color: var(--muted); font-size: 0.9375rem; }
  .synopsis {
    margin-top: var(--s2);
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
  .actions { display: flex; gap: var(--s2); }
  button {
    font: inherit;
    font-size: 0.9375rem;
    font-weight: 600;
    min-height: 44px;
    padding: var(--s2) var(--s5);
    border-radius: 6px;
    border: 1px solid var(--accent);
    cursor: pointer;
  }
  .primary { background: var(--accent); color: #fff; }
  .secondary { background: transparent; color: var(--accent); }
  button:focus-visible { outline: 3px solid #7aa7d1; outline-offset: 2px; }
</style>
</head>
<body>
<ul class="list">
  <li class="card">
    <div class="text">
      <h2 class="title">The Stillness of Dusk</h2>
      <p class="author">Kaspar Ingleby</p>
      <p class="synopsis">An aging steward reflects on a lifetime of service and a missed chance at love during a coastal trip late in his career.</p>
    </div>
    <div class="actions">
      <button class="primary" type="button">Reserve</button>
      <button class="secondary" type="button">Details</button>
    </div>
  </li>
  <li class="card">
    <div class="text">
      <h2 class="title">Merriwick</h2>
      <p class="author">Suzanne Clayborn</p>
      <p class="synopsis">A man lives in a vast house of endless corridors and fog, keeping careful journals, until evidence of another person upends his world.</p>
    </div>
    <div class="actions">
      <button class="primary" type="button">Reserve</button>
      <button class="secondary" type="button">Details</button>
    </div>
  </li>
  <li class="card">
    <div class="text">
      <h2 class="title">A Guest at the Grand Meridian</h2>
      <p class="author">Amos Thornbury</p>
      <p class="synopsis">Sentenced to house arrest in a grand hotel, an exiled count finds purpose and unexpected family as decades of history pass outside.</p>
    </div>
    <div class="actions">
      <button class="primary" type="button">Reserve</button>
      <button class="secondary" type="button">Details</button>
    </div>
  </li>
</ul>
</body>
</html>
```

I haven't opened this in a browser, so the layout is untested.

**What changed in the spacing**
- **Gaps by relationship:** The uniform 16px margin is replaced by a small scale (4, 8, 16, 24, 32) and the gaps now follow how the elements relate.
  - Title to author is 4px, because they're one tight unit.
  - Author to synopsis is 12px (4px gap plus 8px margin).
  - The text block to the buttons is 16px.
  - Between cards the gap is 24px.
  - The gap between cards equals the card padding, so cards no longer touch or blur together.
- **Parent-owned gaps:** Spacing comes from `gap` on the containers, not margins on every child. The last item in a card or list adds no extra space.
- **Card surface:** Each book is a discrete, actionable object, so each gets one light surface: a hairline border and a white fill, with no shadow.
- **Buttons:** They are at least 44px tall with 24px side padding and an 8px gap between them. Reserve is the filled primary action and Details is the outline secondary.
- **Synopsis:** It is clamped to 2 lines.
- **Page margin:** The page padding shrinks on narrow screens with `clamp()`.
- **Assets:** Only system fonts, with no external assets.

I wrote the book titles, authors and synopses as placeholders. Replace them with your real data.
