I couldn't save this to a file because the Write tool is disabled in this session. Here is the full single-file version to paste in as `card.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Studio B rental</title>
<style>
  .card {
    background: #fff;
    border: 1px solid #ddd;
    padding: 16px;
    max-width: 280px;
    font-family: system-ui, sans-serif;
  }
  .card h3 {
    margin: 0 0 4px;
    font-size: 18px;
    font-weight: 600;
  }
  .card .meta {
    margin: 0 0 12px;
    font-size: 13px;
    color: #666;
  }
  .card .price {
    margin: 0 0 16px;
    font-size: 20px;
    font-weight: 700;
  }
  .card .btn {
    display: inline-block;
    padding: 8px 16px;
    background: #0b5fff;
    color: #fff;
    text-decoration: none;
    border-radius: 4px;
  }
  .card .btn:hover { background: #0049d6; }
  .card .btn:focus-visible { outline: 2px solid #0b5fff; outline-offset: 2px; }
</style>
</head>
<body>
  <div class="card">
    <h3>Studio B rental</h3>
    <p class="meta">Mon-Fri, 9-5</p>
    <p class="price">$40/hr</p>
    <a class="btn" href="#">Book</a>
  </div>
</body>
</html>
```

I kept the structure and your specs as they were. The changes are small:
- **Markup:** I quoted the attributes and added the doctype, `lang`, charset and viewport tags.
- **Spacing:** I reset the default margins and gave the heading, meta and price a small, consistent gap.
- **Button:** It's a filled blue (`#0b5fff`) with white text, padding and a 4px radius. It also has hover and keyboard-focus states.
- **Width:** I capped the card at 280px so it doesn't stretch across the page. You can drop that if you don't want it.
