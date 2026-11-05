I read through the file statically. I didn't run axe or test with a screen reader. I found no blockers, but there are a few things worth fixing before you merge.

## What's already good
- `lang`, a descriptive `<title>`, and a viewport meta tag that doesn't block zoom.
- A working skip link that becomes visible on focus, pointing at a `<main id>`.
- Every input has a programmatic label, and the checkboxes are properly grouped in a `fieldset` and `legend`.
- `autocomplete` tokens on name and email satisfy WCAG 1.3.5.
- The heading order is clean (h1, then h2s).
- `:focus-visible` uses a 3px outline in #1a56db, which has strong contrast on white.
- Sizing is in `rem`, so the layout should reflow and scale with zoom.

## Recommended fixes

1. **Required fields aren't marked visually (WCAG 3.3.2).** `required` is announced to screen readers, but sighted users get no cue until they submit. Since both fields are required, add a line above them, for example `<p>All fields in Profile are required.</p>`. Or add `(required)` to each label.

2. **The nav label is confusing (WCAG 2.4.6, best practice).** `aria-label='Account'` on a nav that also contains an "Account" link reads as "Account navigation, Account link". Use something like `aria-label='Main'`. Putting the links in a `<ul>` also gives screen reader users an item count.

3. **The current page is only marked for assistive tech.** `aria-current='page'` has no visual styling. Add a rule such as `nav [aria-current='page'] { font-weight: 700; text-decoration: none; border-bottom: 3px solid currentColor; }`. Don't rely on color alone (1.4.1).

4. **There's no layout for the form, which hurts readability.** Labels and inputs are all inline, so they'll run together on one line. This isn't a strict WCAG failure, but it hurts comprehension and touch use. Put each label and input pair in a block, for example `label, input:not([type=checkbox]) { display: block; }` with some margin. Keep the checkbox labels as full-row click targets (2.5.8).

## Things I can't verify from this file
- **Server-side errors (3.3.1, 3.3.3).** On a failed POST, the page needs an error summary or inline messages. Link each message with `aria-describedby`, set `aria-invalid='true'` on the bad field, and move focus to the summary.
- **Save confirmation (4.1.3).** If "Saved" appears without a page load, put it in a `role='status'` element. If the page reloads, make sure the message is near the top or receives focus.
- **Current values.** Check that the rendered page pre-fills the inputs and checkboxes with the saved settings.
- **Custom styling.** If you later style the input borders or checkboxes, they need at least 3:1 contrast against the background (1.4.11).

I can apply fixes 1–4 to the file if you'd like.
