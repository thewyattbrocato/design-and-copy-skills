I don't have file write permissions enabled in this session, but here's your homepage HTML—copy and save it as `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Halloway Loaf Co. | Sourdough Bread</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            line-height: 1.6;
            color: #2c2c2c;
            background: #fafaf8;
        }
        header {
            background: white;
            padding: 3rem 2rem;
            text-align: center;
            border-bottom: 1px solid #e8e8e6;
        }
        h1 {
            font-size: 2.5rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
            letter-spacing: -0.5px;
        }
        .tagline {
            font-size: 1.1rem;
            color: #666;
            font-weight: 300;
        }
        main {
            max-width: 700px;
            margin: 0 auto;
            padding: 3rem 2rem;
        }
        section {
            margin-bottom: 2.5rem;
        }
        h2 {
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 1rem;
            color: #1a1a1a;
        }
        p {
            margin-bottom: 1rem;
            color: #4a4a4a;
            line-height: 1.7;
        }
        .highlight {
            background: #f5f3f0;
            padding: 2rem;
            border-radius: 4px;
            margin: 1.5rem 0;
        }
        .breads {
            display: grid;
            gap: 1rem;
            margin-top: 1rem;
        }
        .bread {
            padding: 1rem;
            background: white;
            border-left: 3px solid #8b7355;
        }
        .bread strong {
            display: block;
            margin-bottom: 0.25rem;
            color: #1a1a1a;
        }
        .details {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
            margin: 1.5rem 0;
            font-size: 0.95rem;
        }
        .detail-item {
            padding: 1.25rem;
            background: white;
            border-radius: 4px;
        }
        .detail-label {
            font-weight: 600;
            color: #1a1a1a;
            margin-bottom: 0.5rem;
        }
        .cta {
            display: inline-block;
            background: #8b7355;
            color: white;
            padding: 0.875rem 2rem;
            border-radius: 4px;
            text-decoration: none;
            font-weight: 500;
            margin-top: 1rem;
            border: none;
            cursor: pointer;
            font-size: 1rem;
        }
        .cta:hover {
            background: #6f5844;
        }
        footer {
            text-align: center;
            padding: 2rem;
            color: #999;
            font-size: 0.9rem;
            border-top: 1px solid #e8e8e6;
        }
    </style>
</head>
<body>
    <header>
        <h1>Halloway Loaf Co.</h1>
        <p class="tagline">Sourdough bread from Kestrel Falls, Oregon</p>
    </header>

    <main>
        <section>
            <h2>About Us</h2>
            <p>We're two people baking out of a converted garage in Kestrel Falls, Oregon. We started this spring, dedicated to making exceptional sourdough using the simplest possible ingredients: flour, water, and salt. Nothing else. Every loaf ferments for about 36 hours to develop deep flavor and excellent texture.</p>
        </section>

        <section>
            <h2>Our Breads</h2>
            <div class="breads">
                <div class="bread">
                    <strong>Country White</strong>
                    <p>Classic sourdough with a crispy crust and open crumb</p>
                </div>
                <div class="bread">
                    <strong>Rye-Caraway</strong>
                    <p>Hearty rye with the warm spice of caraway seeds</p>
                </div>
                <div class="bread">
                    <strong>Seeded Spelt</strong>
                    <p>Ancient grain spelt with a blend of seeds</p>
                </div>
            </div>
        </section>

        <section class="highlight">
            <h2 style="margin-top: 0;">How It Works</h2>
            <div class="details">
                <div class="detail-item">
                    <div class="detail-label">Delivery</div>
                    <p>Saturday mornings within 15 miles of Kestrel Falls</p>
                </div>
                <div class="detail-item">
                    <div class="detail-label">Price</div>
                    <p>$14 per loaf</p>
                </div>
                <div class="detail-item">
                    <div class="detail-label">Subscribe</div>
                    <p>Weekly or every two weeks, skip any week until Wednesday night</p>
                </div>
                <div class="detail-item">
                    <div class="detail-label">One-Off Orders</div>
                    <p>Order individual loaves as needed</p>
                </div>
            </div>
        </section>

        <section style="text-align: center;">
            <button class="cta" onclick="alert('Order form coming soon')">Order Now</button>
        </section>
    </main>

    <footer>
        <p>Halloway Loaf Co. • Kestrel Falls, Oregon</p>
    </footer>
</body>
</html>
```

Clean, minimal design with warm earth tones. The "Order Now" button placeholder is ready for you to wire up to your actual ordering system.
