I fixed two of the four flags. The other two are false positives, and "fixing" them would make the component less accessible.

**Changed**

- **(2) Search button outline:** I removed `outline: none` from `.go`. Browsers only show the default focus ring on keyboard focus for buttons, so the line wasn't doing anything useful. Your `:focus-visible` rule already gives keyboard users the yellow ring.
- **(4) Arrow-only link:** The link already had an accessible name through `aria-label`, but some checkers only look at the text content. I replaced the label with visually hidden text and hid the arrow from screen readers. The link now has real text content, and the visible arrow is unchanged.

**Left alone**

- **(1) `alt=''` on the hero image:** This is the correct markup for a decorative background image. Adding descriptive alt text would make screen readers read out noise. If the checker keeps flagging it, you could move the image to CSS `background-image`, which would remove the `<img>` element entirely. That may affect your layout, so I didn't do it unprompted.
- **(3) `tabindex='-1'` on the results heading:** This is deliberate. It lets your script move focus to the heading with `.focus()` without adding the heading to the tab order. Removing it would break that focus move, and keyboard and screen-reader users would lose their place after a search. Mark this one as reviewed or ignored in the checker.

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
        <span class='visually-hidden'>View Hawthorn Cottage, sleeps 4</span>
        <span aria-hidden='true'>&rarr;</span>
      </a>
      <span>Hawthorn Cottage</span>
    </li>
  </ul>
</section>
<style>
  .go { background: #14532d; color: #fff; border: 0; padding: .6rem 1rem; }
  .go:focus-visible { outline: 3px solid #fde047; outline-offset: 3px; }
  .visually-hidden {
    position: absolute; width: 1px; height: 1px; margin: -1px; padding: 0;
    overflow: hidden; clip-path: inset(50%); white-space: nowrap; border: 0;
  }
</style>
```

I didn't change the script, but there's a separate problem. The `submit` handler focuses the heading immediately, before any results exist. If the form does a normal navigation to `/search`, the focus call is lost when the page reloads. It only works if you intercept the submit and load results with fetch. In that case, call `focus()` after the results render.
