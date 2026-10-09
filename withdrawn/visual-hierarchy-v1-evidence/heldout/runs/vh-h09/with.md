Here's the card as one file. I kept the structure and class names, quoted the attributes, and added only the styles you listed, plus a few small ones for spacing and the button. I couldn't write the file from here, so save it as `card.html`.

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
    background: #1a62d6;
    color: #fff;
    border-radius: 4px;
    font-size: 14px;
    font-weight: 600;
    text-decoration: none;
  }

  .card .btn:hover { background: #1550b0; }
  .card .btn:focus-visible { outline: 2px solid #1a62d6; outline-offset: 2px; }
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

What I changed:
- **Markup:** I added a doctype, `lang` and viewport meta, and quoted the attributes. The card's structure is unchanged.
- **Specs:** Everything you listed is applied as written: white background, 1px #ddd border, 16px padding, the h3, meta and price sizes, and one filled blue button.
- **Spacing:** I reset the default margins and set a small, consistent rhythm of 4px, 12px and 16px, so the title, meta, price and button group cleanly.
- **Button:** I used a darker blue (#1a62d6) so the white text has enough contrast. I also added hover and keyboard-focus states.
- **Width:** The card has a 280px max width so it doesn't stretch across the page.
