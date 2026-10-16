I'll leave out two things: the timer that restarts for every visitor, and the "only 12 seats left" line. Both are false claims. Visitors who find out (by reloading, using a private window, or comparing notes) will stop trusting the page, and that hurts refunds and reviews. In many places it's also illegal under consumer protection rules. You don't need either, because your deadline is real: the price goes from $89 to $129 on November 30. A countdown to that date creates the same urgency honestly.

Here are both sections with the real countdown.

```html
<!-- TOP SECTION -->
<header class="hero">
  <p class="eyebrow">Self-paced watercolor course</p>
  <h1>Loose Washes</h1>
  <p class="sub">Learn to let the water do the work. 22 video lessons that take you from stiff and fussy to loose, luminous washes.</p>
  <ul class="facts">
    <li>22 video lessons (about 6 hours)</li>
    <li>Printable supply list</li>
    <li>Lifetime access</li>
    <li>14-day refund</li>
  </ul>
  <a href="#buy" class="btn">Get the course, $89</a>
</header>

<!-- BUY SECTION -->
<section id="buy" class="buy">
  <h2>Join Loose Washes</h2>
  <p class="price"><strong>$89</strong> <s>$129</s></p>
  <p class="deadline">Launch price ends <strong>November 30</strong>. After that the course is $129.</p>
  <p id="countdown" aria-live="off"></p>

  <a href="CHECKOUT_URL" class="btn">Enroll now</a>

  <ul class="includes">
    <li>All 22 video lessons, watch at your own pace</li>
    <li>Printable supply list, so you know exactly what to buy</li>
    <li>Lifetime access, including future updates</li>
  </ul>
  <p class="guarantee">Not for you? Email within 14 days for a full refund.</p>
</section>

<script>
  // Same fixed deadline for every visitor. Adjust the UTC offset to your timezone.
  const END = new Date("2026-11-30T23:59:59-05:00");
  const el = document.getElementById("countdown");
  function tick() {
    const ms = END - Date.now();
    if (ms <= 0) { el.textContent = ""; return; } // also update the price text after this date
    const d = Math.floor(ms / 864e5),
          h = Math.floor(ms / 36e5) % 24,
          m = Math.floor(ms / 6e4) % 60,
          s = Math.floor(ms / 1e3) % 60;
    el.textContent = `${d}d ${h}h ${m}m ${s}s left at $89`;
  }
  tick();
  setInterval(tick, 1000);
</script>
```

- **Timezone:** I assumed US Eastern (`-05:00`). Change the offset to match when you want the price to change. Eastern is on daylight time until early November, so after that `-05:00` is right for Nov 30.
- **After the deadline:** The timer clears itself, but the page doesn't change the price. Update the $89 and $129 yourself, or hide the strikethrough. The page should never show $89 after Nov 30.
- **Checkout:** Make sure the checkout also switches to $129 on that date. The page and checkout need to agree.
- **Other honest hooks:** If you want more pull, you could add a short student quote or a free preview lesson. A "bonus ends Nov 30" offer, such as a live Q&A, would also work as long as it's real.

I can also write the CSS, or add a free-preview-lesson block, if you'd like.
