I wrote both sections, but I left out the two things you asked for. A timer that restarts for every visitor and a "12 seats left" line are both false claims. Buyers can be misled by them, and they're the kind of thing that gets complaints, chargebacks, and trouble with the FTC or consumer-protection rules. You also don't need them, because your deadline is real: the price goes from $89 to $129 on November 30. So the countdown below runs to that date and is the same for everyone.

```html
<!-- TOP SECTION -->
<section class="hero">
  <p class="eyebrow">Self-paced watercolor course</p>
  <h1>Loose Washes</h1>
  <p class="sub">Learn to let the water do the work. 22 video lessons that take you from stiff and overworked to fluid, confident washes.</p>

  <ul class="facts">
    <li>22 video lessons (about 6 hours total)</li>
    <li>Printable supply list</li>
    <li>Lifetime access</li>
    <li>14-day refund</li>
  </ul>

  <a href="#buy" class="btn">Enroll for $89</a>
</section>

<!-- BUY SECTION -->
<section id="buy" class="buy">
  <h2>Get Loose Washes</h2>

  <p class="price">
    <span class="now">$89</span>
    <span class="later">Goes up to $129 on November 30</span>
  </p>

  <p class="countdown" aria-live="polite">
    Launch price ends in <strong id="cd"></strong>
  </p>

  <ul class="included">
    <li>All 22 video lessons, start whenever you like</li>
    <li>Printable supply list so you know what to buy before you begin</li>
    <li>Lifetime access, including future updates</li>
    <li>14-day refund. If it's not for you, email me and you get your money back.</li>
  </ul>

  <a href="/checkout" class="btn">Enroll for $89</a>
  <p class="fine">Launch price is available until the end of November 30.</p>
</section>

<script>
  // Same deadline for every visitor. Set the offset to your timezone.
  const END = new Date("2026-11-30T23:59:59-05:00").getTime();
  const el = document.getElementById("cd");

  function tick() {
    const ms = END - Date.now();
    if (ms <= 0) {
      el.textContent = "0d 0h 0m 0s";
      document.querySelector(".now").textContent = "$129";
      document.querySelector(".later").textContent = "";
      document.querySelector(".countdown").textContent = "Launch pricing has ended.";
      return;
    }
    const s = Math.floor(ms / 1000);
    const d = Math.floor(s / 86400);
    const h = Math.floor((s % 86400) / 3600);
    const m = Math.floor((s % 3600) / 60);
    el.textContent = `${d}d ${h}h ${m}m ${s % 60}s`;
    setTimeout(tick, 1000);
  }
  tick();
</script>
```

- **Timezone:** change `-05:00` to yours. The page also needs to charge $129 after the deadline. Ideally your checkout enforces the date too, so the page and the price can't disagree.
- **Urgency without a fake limit:** the real price increase is already a strong reason to buy now. If you want more, you could add a true limited-time bonus, such as a live Q&A or a critique session for the first 30 enrollees. If you do that, only claim a number you will actually enforce.
- **Social proof:** once you have student results or reviews, a real quote near the button will likely do more than a scarcity line.

I can also write the rest of the page (lesson list, FAQ, about you) or add CSS.
