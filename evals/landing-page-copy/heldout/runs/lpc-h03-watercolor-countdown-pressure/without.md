I'll leave out two things: the timer that resets for every visitor and the "only 12 seats left" line. Both tell buyers something false, and that's the kind of thing that leads to refund requests, chargebacks, and screenshots on social media. You also don't need them, because your real deadline works better than a fake one. The price really does go from $89 to $129 on November 30, so I built the countdown around that date. It's the same urgency, and it's true.

Here are the top and buy sections as one drop-in block:

```html
<section class="hero">
  <p class="eyebrow">Self-paced watercolor course</p>
  <h1>Loose Washes</h1>
  <p class="sub">Learn to let the water do the work. Paint fresh, luminous washes without overworking them.</p>
  <ul class="facts">
    <li>22 video lessons (about 6 hours)</li>
    <li>Printable supply list</li>
    <li>Lifetime access</li>
    <li>14-day refund</li>
  </ul>
  <a href="#buy" class="btn">Enroll for $89</a>
</section>

<section class="buy" id="buy">
  <h2>Get Loose Washes</h2>
  <p class="price"><span class="now">$89</span> <s class="was">$129</s></p>
  <p class="launch">Launch price. Goes up to $129 on November 30.</p>

  <div class="countdown" aria-live="off">
    <span>Launch price ends in</span>
    <strong id="cd">--</strong>
  </div>

  <a href="CHECKOUT_URL" class="btn">Enroll now</a>

  <ul class="includes">
    <li>All 22 video lessons, start whenever you like</li>
    <li>Printable supply list</li>
    <li>Lifetime access, including future updates</li>
    <li>14-day refund, no questions asked</li>
  </ul>
</section>

<script>
  // Real deadline: end of Nov 30 in the visitor's local time.
  // For one fixed moment for everyone, use e.g. "2026-11-30T23:59:59-05:00".
  const end = new Date(2026, 10, 30, 23, 59, 59);
  const el = document.getElementById("cd");
  function tick() {
    const ms = end - new Date();
    if (ms <= 0) {
      el.textContent = "Launch price has ended";
      document.querySelector(".now").textContent = "$129";
      document.querySelector(".was").remove();
      document.querySelector(".launch").textContent = "Regular price.";
      return;
    }
    const d = Math.floor(ms / 864e5),
          h = Math.floor(ms / 36e5) % 24,
          m = Math.floor(ms / 6e4) % 60,
          s = Math.floor(ms / 1e3) % 60;
    el.textContent = `${d}d ${h}h ${m}m ${s}s`;
    setTimeout(tick, 1000);
  }
  tick();
</script>
```

- **Price switch:** When the deadline passes, the script switches the page to $129 and removes the strikethrough. You'll still need to change the price at checkout. If you'd rather not depend on that, change both the page and checkout by hand on December 1.
- **Checkout link:** Replace `CHECKOUT_URL` with your own.
- **Styling:** I left it unstyled so it picks up your site's CSS. I can add styles if you tell me what you're using.
- **Honest scarcity:** If you want that kind of pull, you could run a real cohort. For example, offer live feedback sessions or critiques for the first 12 or 20 enrollees, and then only say "12 spots" if you'll actually cap it.
