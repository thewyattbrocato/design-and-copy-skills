I read through the markup and CSS but haven't run it in a browser or with a screen reader. The page is in good shape overall. I'd fix one thing before merging and add a few smaller ones.

**Fix before merge**

- **The checkbox picks up the text-input styles.** `input{width:100%;padding:8px;...}` also matches `input[type=checkbox]`. The checkbox gets stretched to full width with padding, and its focus ring will look wrong. The label also inherits `display:block` and `font-weight:600`. Suggested fix:
  ```css
  input[type=checkbox]{width:20px;height:20px;padding:0;margin-right:8px;vertical-align:middle}
  label.check{font-weight:400}
  ```
  Then use `<label class="check">` on the newsletter label. Sizing the checkbox to 20px also helps with the WCAG 2.2 target-size criterion.

**Worth adding**

- **Save feedback:** The form has no way to announce success or errors. When you wire up submit, add something like `<p role="status" id="save-status"></p>`. For validation errors, use `aria-invalid="true"` plus `aria-describedby` pointing at the error text. Move focus to an error summary or the first invalid field.
- **Skip link target:** Add `tabindex="-1"` to `<main id="main">`. Some older browsers, Safari in particular, don't move keyboard focus to a non-focusable fragment target.
- **Nav markup:** The two links sit in a bare `<nav>` separated by whitespace. A `<ul>` is more conventional and gets list announcements in screen readers. The nav also has no spacing, so the links run together visually.
- **Hint wording:** "We send booking confirmations here" works as the email's description. If the field is required, add `required` and say so visually. Don't rely on the browser's default message alone.

**Already fine**

- `lang`, the title, the viewport (zoom isn't disabled), and a single `h1`.
- The landmarks are right: a labelled `nav` and a `main`.
- All inputs have programmatic labels, `autocomplete` tokens are correct (WCAG 1.3.5), and the hint is linked with `aria-describedby`.
- Contrast passes:
  - Body text is about 14:1.
  - The input border is about 5.9:1 against the 3:1 requirement.
  - The white-on-blue button is about 6.9:1.
  - The 3px focus ring is clearly visible.
- The skip link becomes visible on focus.

If you'd like, I can apply these changes to the file. Paste the real path or the current version if it differs from this snippet.
