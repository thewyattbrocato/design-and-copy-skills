```html
<body>
 <header><a href="/"><img src="logo.png" alt=""></a></header>
 <main>
  <h1>Your order is ready to review</h1>
  <h3>Items</h3>
  <ul><li>2 x sourdough loaf</li><li>1 x rye</li></ul>
  <div class="btn" onclick="edit()">Edit order</div>
  <p style="color:#9aa0a6">Delivery is free over 20 pounds.</p>
 </main>
 <footer>
  <a href="/privacy">Privacy</a>
  <a href="/checkout/payment">Proceed to payment</a>
 </footer>
</body>
```

I changed only the footer link text, from "Proceed" to "Proceed to payment", to match its `/checkout/payment` destination. I left everything else as it was.
