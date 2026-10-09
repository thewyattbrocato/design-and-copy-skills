Here's the revised file. Wording is unchanged.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Pricing</title>
<style>
  *{box-sizing:border-box}
  body{margin:0}
  .pricing{
    min-height:100vh;
    background:linear-gradient(135deg,#6d28d9,#2563eb);
    padding:40px;
    font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
    display:flex;
    gap:24px;
    align-items:center;
    justify-content:center;
  }
  .card{
    flex:1;
    max-width:380px;
    background:rgba(255,255,255,.14);
    border:1px solid rgba(255,255,255,.4);
    border-radius:16px;
    padding:28px 24px;
    color:#fff;
    display:flex;
    flex-direction:column;
  }
  .card h3{
    margin:0;
    font-size:14px;
    font-weight:600;
    letter-spacing:.08em;
    text-transform:uppercase;
    opacity:.9;
  }
  .card h3 small{
    display:block;
    margin-top:4px;
    font-size:12px;
    font-weight:600;
    letter-spacing:.02em;
    text-transform:none;
  }
  .card .price{
    margin:14px 0 20px;
    padding-bottom:20px;
    border-bottom:1px solid rgba(255,255,255,.3);
    font-size:16px;
    line-height:1;
  }
  .card .price strong{font-size:48px;font-weight:800;letter-spacing:-.02em}
  .card .price span{font-size:15px;font-weight:500;opacity:.85;margin-left:2px}
  .card ul{list-style:none;margin:0;padding:0;flex:1}
  .card li{
    font-size:15px;
    line-height:1.4;
    padding:7px 0;
    display:flex;
    align-items:center;
    gap:8px;
  }
  .badge{
    background:#fbbf24;
    color:#000;
    border-radius:6px;
    padding:1px 6px;
    font-size:10px;
    font-weight:700;
    text-transform:uppercase;
    letter-spacing:.04em;
  }
  .card a{
    display:block;
    margin-top:24px;
    padding:12px 14px;
    background:#fff;
    color:#1d4ed8;
    border-radius:10px;
    text-align:center;
    font-weight:700;
    font-size:15px;
    text-decoration:none;
  }
  .card a:hover{background:#eef2ff}
  .card a:focus-visible{outline:3px solid #fbbf24;outline-offset:2px}

  /* Recommended plan */
  .card.featured{
    background:#fff;
    color:#1e1b4b;
    border-color:#fff;
    padding:40px 28px;
    box-shadow:0 20px 40px rgba(30,27,75,.35);
  }
  .card.featured h3{color:#6d28d9;opacity:1}
  .card.featured .price{border-bottom-color:#e5e7eb}
  .card.featured .price strong{font-size:60px}
  .card.featured a{background:linear-gradient(135deg,#6d28d9,#2563eb);color:#fff;padding:14px}
  .card.featured a:hover{filter:brightness(1.1);background:linear-gradient(135deg,#6d28d9,#2563eb)}
</style>
</head>
<body>
<section class="pricing">
  <div class="card"><h3>Starter</h3><p class="price"><strong>$9</strong><span>/month</span></p><ul><li>1 project <span class="badge">new</span></li><li>Basic reports <span class="badge">new</span></li><li>Email support <span class="badge">new</span></li></ul><a href="#">Choose Starter</a></div>
  <div class="card featured"><h3>Team <small>(recommended)</small></h3><p class="price"><strong>$29</strong><span>/month</span></p><ul><li>10 projects <span class="badge">new</span></li><li>Advanced reports <span class="badge">new</span></li><li>Priority support <span class="badge">new</span></li></ul><a href="#">Choose Team</a></div>
  <div class="card"><h3>Scale</h3><p class="price"><strong>$79</strong><span>/month</span></p><ul><li>Unlimited projects <span class="badge">new</span></li><li>Custom reports <span class="badge">new</span></li><li>Dedicated manager <span class="badge">new</span></li></ul><a href="#">Choose Scale</a></div>
</section>
</body>
</html>
```

**What changed**
- **Price:** the amount is now the largest element, and "/month" is smaller beside it. A divider separates it from the features.
- **Plan name:** it's now a small uppercase label, so it no longer competes with the price.
- **Recommended plan:** Team is a solid white card with a larger price, more padding, a shadow and a gradient button. It replaces the inline `margin-top:10px` hack. "(recommended)" sits on its own line under the name.
- **Features:** the list is cleaner and aligned, with more even spacing.
- **"new" badges:** they're smaller and quieter. They're still on every item, since I kept the content as is.
- **Buttons:** they're full-width. The Starter and Scale buttons are white, and the Team button is the filled one.
- **Fit:** the three cards sit side by side and are about 500px tall at 1280×800, so all three show without scrolling.

**Markup changes**
- I added `href="#"` to the links so they can be focused with the keyboard, and added focus and hover styles.
- I wrapped the price number and "/month" in `<strong>` and `<span>` so they can be sized separately. The text reads the same.
- I set the system font stack explicitly instead of `sans-serif`.
