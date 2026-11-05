I fixed two of the four flags, replaced the markup behind a third, and left one alone on purpose. Clearing the warning on that one would have broken the page.

**1. Empty alt on the hero image: markup changed, and `alt=""` was already correct.**
The image is a decorative background, so empty alt is the right answer. To clear the flag without hurting accessibility, I moved it to CSS, where no alt is needed.

**2. `outline: none` on the search button: fixed.**
Your `:focus-visible` rule already supplies a strong focus ring, so the `outline: none` is redundant. I removed it.

**3. `tabindex="-1"` on the results heading: left as is.**
Your script calls `.focus()` on that heading to move keyboard and screen-reader users to the results. That only works because of `tabindex="-1"`. It keeps the heading out of the tab order but still lets it take programmatic focus. If you remove it, the focus move silently stops working. The checker is flagging a legitimate pattern, so I'd mark this one as a reviewed exception.

**4. Arrow-only link: fixed.**
The `aria-label` gave it an accessible name, but the visible text was only an arrow, and the label didn't match what sighted users see. The link now wraps the cottage name, and the arrow is decorative.

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
        Hawthorn Cottage<span class='sr-only'>, sleeps 4</span>
        <span aria-hidden='true'>&rarr;</span>
      </a>
    </li>
  </ul>
</section>
<style>
  .hero { background: url('/img/hills-wide.jpg') center / cover no-repeat; }
  .go { background: #14532d; color: #fff; border: 0; padding: .6rem 1rem; }
  .go:focus-visible { outline: 3px solid #fde047; outline-offset: 3px; }
  .sr-only {
    position: absolute; width: 1px; height: 1px; overflow: hidden;
    clip-path: inset(50%); white-space: nowrap;
  }
</style>
```

I left the script unchanged. The `.hero-bg` class was on the old `<img>`, so if your existing CSS positioned it absolutely, you can delete those rules. Check that the hero text still has enough contrast over the background.

One thing the checker won't catch: the form does a normal GET to `/search`, which reloads the page and discards the submit handler. The focus call only works if the results are loaded in place with fetch or if you run the focus call on page load of the results page. Check which of those you're doing.
