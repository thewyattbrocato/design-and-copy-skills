I fixed two of the four flags. The other two are false positives, and "fixing" them would make the page worse.

**1. Empty alt on the hero image: leave it.**
`alt=""` is correct for a decorative background image. A description like "hills" would make screen readers announce noise. I moved the image into CSS so the checker has nothing to flag and the markup shows it's decorative.

**2. `outline: none` on the search button: fixed.**
Your `:focus-visible` rule already restores a strong outline, so keyboard users were never left without a focus indicator. The `outline: none` line did nothing useful and only triggered the checker, so I removed it.

**3. `tabindex="-1"` on the results heading: leave it.**
This is the standard pattern for moving focus to a heading with `.focus()`. Without it, `.focus()` does nothing on an `<h2>`.

**4. Arrow-only link: fixed.**
The `aria-label` gave it an accessible name, but sighted users saw only an arrow, separate from the cottage name. I made the cottage name the link text and hid the arrow from assistive tech. The visible text now matches what screen readers announce.

```html
<section class="hero">
  <!-- hero image moved to CSS (decorative) -->
  <h1>Find a cottage in the Cheviots</h1>
  <form role="search" action="/search">
    <label for="q">Place or postcode</label>
    <input id="q" name="q">
    <button class="go">Search</button>
  </form>
</section>
<section>
  <h2 id="results-title" tabindex="-1">12 cottages found</h2>
  <ul class="results">
    <li>
      <a href="/cottage/hawthorn" class="next">
        Hawthorn Cottage<span class="visually-hidden">, sleeps 4</span>
        <span aria-hidden="true">&rarr;</span>
      </a>
    </li>
  </ul>
</section>
<style>
  .hero { background: url('/img/hills-wide.jpg') center / cover; }
  .go { background: #14532d; color: #fff; border: 0; padding: .6rem 1rem; }
  .go:focus-visible { outline: 3px solid #fde047; outline-offset: 3px; }
  .visually-hidden {
    position: absolute; width: 1px; height: 1px; overflow: hidden;
    clip-path: inset(50%); white-space: nowrap;
  }
</style>
```

If the image needs to stay an `<img>` (for example, for lazy loading), keep `alt=""` as it was. You can then mark the checker warning as reviewed or ignored.

**Separate bug in your script:** the form has `action="/search"` and no `preventDefault`, so submitting loads a new page and the `.focus()` call is lost. It also runs before the results exist. Two fixes would work:
- **Full page load:** call `focus()` on the results page itself, on load.
- **Fetch-and-render in place:** call `preventDefault()` on submit, then call `focus()` after the results render.

I can make that change if you tell me which approach you're using.
