Two of the four flags are real fixes. The other two are false positives, and I'd leave the code alone for those.

**Changed**

- **(2) Outline on the search button:** I deleted `outline: none`. Your `:focus-visible` rule already gives keyboard users a strong focus ring. Browsers only match `:focus-visible` on keyboard focus, so mouse clicks won't show the default outline either.
- **(4) Arrow-only link:** The `aria-label` gave the link an accessible name, but sighted users and voice-control users only saw "→". I made the cottage name the link text and hid the arrow from screen readers. "Sleeps 4" moved into visually hidden text, so screen readers still announce it.

**Left as is**

- **(1) Empty `alt` on the hero image:** `alt=""` is the correct markup for a decorative background image, and the `<h1>` already carries the meaning. Adding alt text like "hills" would only add noise for screen-reader users. If the checker still complains, mark it as a reviewed false positive. Or move the image to CSS `background-image` on `.hero`, which removes the `<img>` and the warning together. That depends on how `.hero-bg` is positioned, so I didn't do it without seeing your stylesheet.
- **(3) `tabindex="-1"` on the results heading:** This is the standard way to move focus to a heading after results load. Without it, `.focus()` does nothing on a non-interactive element. It doesn't add the heading to the tab order. Removing it would break your script.

```html
<section class='hero'>
  <img src='/img/hills-wide.jpg' alt='' class='hero-bg'>
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
        <span>Hawthorn Cottage</span><span class='visually-hidden'>, sleeps 4</span>
        <span aria-hidden='true'>&rarr;</span>
      </a>
    </li>
  </ul>
</section>
<style>
  .go { background: #14532d; color: #fff; border: 0; padding: .6rem 1rem; }
  .go:focus-visible { outline: 3px solid #fde047; outline-offset: 3px; }
  .visually-hidden {
    position: absolute; width: 1px; height: 1px; margin: -1px; padding: 0;
    overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0;
  }
</style>
```

I also moved the cottage name inside the link, so the `<li>` no longer has a separate `<span>`. If you want the name styled differently from the arrow, target the spans inside `.next`.

Separately, the form submits to `/search` as a normal navigation, so the page reloads and the `submit` handler's `focus()` call never takes effect. To get the focus behaviour, run `document.getElementById('results-title').focus()` on the results page's load. Or fetch results with JavaScript and call `preventDefault()`. I haven't changed this, since it's outside the four flags.
