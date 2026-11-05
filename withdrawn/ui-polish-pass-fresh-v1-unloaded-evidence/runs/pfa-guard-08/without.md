Two of the four flags are false positives, so I fixed the other two and left those two as they are. Silencing the false positives would make the page worse for keyboard and screen-reader users.

**1. Empty alt on the hero image: keep it, but move the image to CSS.**
The image is a decorative background, and `alt=""` is the correct markup for that. Descriptive alt text would make screen readers announce noise. Moving it to CSS means there's no `<img>` for the checker to flag. If you'd rather keep the `<img>`, add a checker exception instead.

**2. `outline: none` on the button: fixed.**
You already have a `:focus-visible` style, so the `outline: none` rule does nothing useful. I removed it, and the focus ring is unchanged.

**3. `tabindex="-1"` on the results heading: keep it.**
It's what lets your script call `.focus()` on a non-interactive heading, so removing it breaks the focus management. It also doesn't add the heading to the tab order. I'd suppress this one in the checker.

**4. Link whose text is just an arrow: fixed.**
The link now wraps the cottage name, so its visible text is meaningful. The arrow is hidden from assistive tech and the `aria-label` is no longer needed.

```html
<section class='hero'>
  <h1>Find a cottage in the Cheviots</h1>
  <form role='search' action='/search'>
    <label for='q'>Place or postcode</label>
    <input id='q' name='q'>
    <button class='go'>Search</button>
  </form>
</section>
<section>
  <h2 id='results-title' tabindex='-1'>12 cottages found</h2>
  <ul class='results'>
    <li>
      <a href='/cottage/hawthorn' class='next'>
        Hawthorn Cottage, sleeps 4 <span aria-hidden='true'>&rarr;</span>
      </a>
    </li>
  </ul>
</section>
<style>
  .hero { background: url('/img/hills-wide.jpg') center / cover no-repeat; }
  .go { background: #14532d; color: #fff; border: 0; padding: .6rem 1rem; }
  .go:focus-visible { outline: 3px solid #fde047; outline-offset: 3px; }
</style>
<script>
  document.querySelector('form').addEventListener('submit', () => {
    // after results load:
    document.getElementById('results-title').focus();
  });
</script>
```

- **Styles:** I dropped the `.hero-bg` class. If it positioned the image, move those rules onto `.hero`.
- **Focus script:** it runs on submit, but the form does a full page navigation to `/search`. The focus call will only work if the results are loaded without a page reload, or if you call it on the results page at load.
