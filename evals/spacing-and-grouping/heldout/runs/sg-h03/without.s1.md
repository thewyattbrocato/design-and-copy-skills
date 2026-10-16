I couldn't save the file because the Write tool is disabled in this session. The full HTML is below, so you can save it as `index.html`.

The main change is spacing that follows how the elements relate to each other, instead of a uniform 16px margin:

- **Title to author:** 4px, so they read as one heading group.
- **Author to synopsis:** 12px.
- **Synopsis to buttons:** 20px, the largest gap inside a card, which separates the actions from the content.
- **Between cards:** 16px, using flex `gap`. Each card also gets a border, a rounded corner and 20px of padding, so the cards read as separate units.
- **Buttons:** 8px apart. "Reserve" is the filled primary button and "Details" is the outlined secondary one. Both are at least 40px tall and have a visible focus ring.
- **Synopsis:** clamped to 2 lines.

I haven't opened it in a browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Library Catalog</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    background: #f4f4f1;
    color: #1f2328;
    line-height: 1.5;
    padding: 24px 16px;
  }

  .card-list {
    list-style: none;
    max-width: 640px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .card {
    background: #fff;
    border: 1px solid #e2e2dc;
    border-radius: 10px;
    padding: 20px;
  }

  .title {
    font-size: 1.125rem;
    line-height: 1.3;
    font-weight: 650;
    letter-spacing: -0.01em;
  }

  .author {
    margin-top: 4px;
    font-size: 0.875rem;
    color: #5b6370;
  }

  .synopsis {
    margin-top: 12px;
    font-size: 0.9375rem;
    color: #3a414a;
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
    min-height: 40px;
    border-radius: 6px;
    border: 1px solid transparent;
    cursor: pointer;
  }

  .btn-primary { background: #1d4ed8; color: #fff; }
  .btn-primary:hover { background: #1e40af; }

  .btn-secondary { background: #fff; color: #1d4ed8; border-color: #c4cbd6; }
  .btn-secondary:hover { background: #f1f4fa; }

  .btn:focus-visible { outline: 3px solid #93b4ff; outline-offset: 2px; }

  @media (max-width: 400px) {
    .actions .btn { flex: 1; }
  }
</style>
</head>
<body>
  <ul class="card-list">
    <li class="card">
      <h2 class="title">The Lantern at Harrowmere</h2>
      <p class="author">Marian K. Oakhurst</p>
      <p class="synopsis">An envoy travels to the frozen world of Orvane, where the winters shape every custom, and must earn the trust of a society he struggles to understand.</p>
      <div class="actions">
        <button class="btn btn-primary" type="button">Reserve</button>
        <button class="btn btn-secondary" type="button">Details</button>
      </div>
    </li>

    <li class="card">
      <h2 class="title">Honor and Hesitation</h2>
      <p class="author">Jean Ashford</p>
      <p class="synopsis">Eleanor Marsh navigates family pressure, social expectation, and her own first impressions in a sharp comedy of manners in a market town.</p>
      <div class="actions">
        <button class="btn btn-primary" type="button">Reserve</button>
        <button class="btn btn-secondary" type="button">Details</button>
      </div>
    </li>

    <li class="card">
      <h2 class="title">A Plain Account of Tides</h2>
      <p class="author">Stanley Hallwick</p>
      <p class="synopsis">A clear, accessible tour of tides, storms, and the nature of the sea, written for readers without a physics background.</p>
      <div class="actions">
        <button class="btn btn-primary" type="button">Reserve</button>
        <button class="btn btn-secondary" type="button">Details</button>
      </div>
    </li>
  </ul>
</body>
</html>
```
