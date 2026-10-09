The core problem is that the layout is built from fixed pixel widths and then patched with a few breakpoints. Anything that isn't one of those exact sizes either overflows or leaves dead space.

## Problems

**1. Fixed-width page container**
`.page { width: 1100px }` forces horizontal scrolling on any viewport narrower than 1100px. The media queries swap in other fixed widths (740px, 460px), so a 600px tablet or a 390px phone still overflows or leaves odd gaps. Use `max-width: 1100px; width: 100%` with horizontal padding.

**2. Widths that don't add up**
- `.sidebar` (280px) + `.content` (780px) = 1060px, which leaves 40px unaccounted for inside the 1100px page.
- At 768px, `.page` is 740px but `.content` is 700px with the sidebar hidden. That's 40px of arbitrary slack.
- At 480px, `.page` is 460px. Phones are commonly 360–414px wide, so this overflows on almost all of them.

Replace these with `flex: 1; min-width: 0` on the content, and let the sidebar keep a fixed basis (`flex: 0 0 280px`).

**3. `float: left` on a flex child**
`.sidebar` is inside `.layout { display: flex }`, so the float does nothing. It's leftover code from an earlier layout and should be deleted.

**4. The sidebar is hidden on mobile**
`display: none` at 768px removes whatever is in it, which may be contact info, hours or filters. Patients on phones probably need that. Stack it above or below the content instead (`flex-direction: column` on `.layout`), or move it into a collapsible section.

**5. Time slots can't wrap**
`.slots { display: flex }` has no `flex-wrap`, and each slot is a fixed 120px, 100px or 80px. A row of 6+ slots will overflow at every size. This is probably the most visible breakage on the page. Use `flex-wrap: wrap` with `gap`, or a grid such as `grid-template-columns: repeat(auto-fill, minmax(96px, 1fr))`.

**6. `margin-right` on every slot**
This leaves a trailing margin on the last item, and it breaks once the slots wrap. `gap` fixes both. Drop the 10px and 4px margins.

**7. Fixed slot height**
`height: 48px` clips text if the user enlarges their font or the label wraps. For appointment times that's a real accessibility issue. Use `min-height: 48px`. That value is also a good minimum tap target, so keep it.

**8. Doctor photo is a fixed square**
320px and 200px are hard-coded. Use `width: 100%; max-width: 320px; height: auto; aspect-ratio: 1; object-fit: cover`. The `object-fit` matters because with fixed width and height, any photo that isn't square gets stretched. Check whether the `<img>` tags have `alt` text too.

**9. `.intro` is 900px wide and has no override**
It's wider than `.content` (780px) at desktop size, so it overflows its parent even on the developer's laptop. It's never reduced for smaller screens. Use `max-width: 65ch` instead. That also improves readability, since 900px lines are far too long.

**10. Font size in px**
`font-size: 15px` ignores the user's browser font-size setting, and 15px is small for a patient population that skews older. Use `1rem` (or a bit more) and set `.intro` relative to that.

**11. Desktop-first breakpoints with width overrides**
Because each query overrides pixel widths, every new element needs three sets of numbers. Once the base styles are fluid (`max-width`, `flex`, `gap`, `grid`), most of the media queries go away. You'd keep one at around 768px to stack the layout.

**12. Missing basics (not visible in the CSS, but worth checking)**
- The HTML needs `<meta name="viewport" content="width=device-width, initial-scale=1">`. Without it, phones render at ~980px and shrink the page, which alone could explain "looks awful on anything that isn't the developer's laptop."
- Add `box-sizing: border-box` globally. Without it, any padding you add will break these width calculations.

## What I'd change, in order
1. Check the viewport meta tag and add the `box-sizing` reset.
2. Make `.page` fluid (`max-width` plus padding).
3. Fix `.slots` with wrapping and `gap`. This is the biggest visible win.
4. Make `.content` flexible and delete the float.
5. Stack the sidebar on narrow screens instead of hiding it.
6. Fix the photo and intro sizing and move text to `rem`.
7. Delete the media queries that only existed to override pixel widths.

If you share the HTML, I can check the markup for things like the viewport tag, the image tags and what's inside the sidebar.
