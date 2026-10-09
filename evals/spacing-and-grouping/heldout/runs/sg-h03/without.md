I couldn't save the file because the Write tool is disabled in this session. Here is the full HTML. Save it as `index.html`. I haven't opened it in a browser.

**What changed**
- **Spacing:** The 16px margin on every element is gone. Spacing now follows grouping:
  - Title to author is 4px, so they read as one block.
  - Author to synopsis is 12px.
  - Synopsis to buttons is 20px, the largest gap inside a card.
  - The cards sit 16px apart, and each has 20px of padding.
- **Synopsis:** It's clamped to 2 lines so the cards stay even.
- **Buttons:** "Reserve" is the filled primary button and "Details" is the outlined secondary one. They have a hover state and a visible keyboard focus ring. On narrow screens (400px or less) they stack full-width.
- **Fonts and assets:** It uses system fonts and has no external assets. The cards are an accessible `<ul>` list.
- **Placeholder content:** The three books and their synopses are placeholders I wrote. Replace them with your own.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Library Catalog</title>
<style>
  :root {
    --bg: #f5f4f0;
    --card: #ffffff;
    --text: #1f2328;
    --muted: #5d6570;
    --border: #e2e0d9;
    --accent: #2f5d50;
    --accent-hover: #244a40;
  }

  * { box-sizing: border-box; }

  body {
    margin: 0;
    padding: 32px 16px;
    background: var(--bg);
    color: var(--text);
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
    line-height: 1.5;
  }

  .card-list {
    max-width: 640px;
    margin: 0 auto;
    padding: 0;
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 20px;
  }

  .title {
    margin: 0;
    font-size: 1.125rem;
    line-height: 1.3;
    font-weight: 650;
  }

  .author {
    margin: 4px 0 0;
    font-size: 0.875rem;
    color: var(--muted);
  }

  .synopsis {
    margin: 12px 0 0;
    font-size: 0.9375rem;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .actions {
    margin-top: 20px;
    display: flex;
    gap: 8px;
  }

  .btn {
    font: inherit;
    font-size: 0.875rem;
    font-weight: 600;
    padding: 8px 16px;
    border-radius: 6px;
    border: 1px solid var(--accent);
    cursor: pointer;
    transition: background-color .15s, color .15s;
  }

  .btn-primary { background: var(--accent); color: #fff; }
  .btn-primary:hover { background: var(--accent-hover); }

  .btn-secondary { background: transparent; color: var(--accent); }
  .btn-secondary:hover { background: #e9f0ed; }

  .btn:focus-visible { outline: 3px solid #86b5a6; outline-offset: 2px; }

  @media (max-width: 400px) {
    .actions { flex-direction: column; }
    .btn { width: 100%; }
  }
</style>
</head>
<body>
  <ul class="card-list">
    <li class="card">
      <h2 class="title">The Salt Road to Marrow</h2>
      <p class="author">Odile K. Harrowgate</p>
      <p class="synopsis">An envoy travels to the frozen world of Veskara to persuade its people to join a distant alliance, and must learn to trust a society that defies his every assumption.</p>
      <div class="actions">
        <button class="btn btn-primary" type="button">Reserve</button>
        <button class="btn btn-secondary" type="button">Details</button>
      </div>
    </li>

    <li class="card">
      <h2 class="title">Lantern Meridian</h2>
      <p class="author">Marian Teal Okafor</p>
      <p class="synopsis">After a long blackout collapses the cities, a traveling troupe of actors and musicians performs old plays for the scattered settlements of the surviving world.</p>
      <div class="actions">
        <button class="btn btn-primary" type="button">Reserve</button>
        <button class="btn btn-secondary" type="button">Details</button>
      </div>
    </li>

    <li class="card">
      <h2 class="title">Halcyon Reach</h2>
      <p class="author">Selwyn Ashcombe</p>
      <p class="synopsis">Corvane lives in a vast house of endless halls and tides, recording its wonders in his journals, until evidence of another person upends his quiet world.</p>
      <div class="actions">
        <button class="btn btn-primary" type="button">Reserve</button>
        <button class="btn btn-secondary" type="button">Details</button>
      </div>
    </li>
  </ul>
</body>
</html>
```
