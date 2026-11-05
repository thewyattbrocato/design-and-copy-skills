This page is in good shape, and I found nothing that blocks a merge.

**What already works:**
- The page has `lang`, a title, one `h1`, a `main` landmark, a labelled `nav` with `aria-current`, and a skip link that shows on focus.
- Every input has a programmatic label and a sensible `autocomplete`, and the checkboxes sit in a `fieldset` with a `legend`.
- The focus ring is visible, the button is native, and the viewport meta doesn't block zoom.

**Findings, ranked by harm:**

1. **Required fields aren't marked visibly (WCAG 3.3.2).** Both inputs have `required`, but sighted users get no cue until the browser's validation bubble appears on submit. Fix by putting the cue in the label text, so nothing relies on color or an icon:
   ```html
   <label for='dn'>Display name (required)</label>
   <label for='em'>Email address (required)</label>
   ```
   Alternatively, add "All fields in Profile are required." above the first field.

2. **The result of saving isn't visible in this file.** The form does a full-page POST, so the page it returns has to carry the feedback:
   - **Success:** a "Settings saved" message with `role='status'`.
   - **Server-side errors:** an error summary or inline errors tied to the fields with `aria-describedby`, plus `aria-invalid='true'` on the bad fields.
   - **Focus:** moved to the first problem or the message.
   - **Typed values:** kept after a failed save.

   If the server handles this elsewhere, ignore this point. Check it before merging, because silent failure on save is the most likely real-world gap.

3. **Minor: make the skip target reliably focusable.** Add `tabindex='-1'` to `<main id='main'>`. Current browsers move focus anyway, but older Safari versions may not.

4. **Optional, cosmetic: the form fields are crowded.** Labels and inputs are inline with no spacing, so the label and input run together on a line. Reflow at 320px and 200% text still works, so this isn't a failure. A small fix, if you want it:
   ```css
   label, input:not([type=checkbox]) { display: block; }
   input:not([type=checkbox]) { margin-bottom: 1rem; }
   fieldset label { margin-bottom: .5rem; }
   ```

**Not checked:** I only read the markup. I didn't run a screen reader, test keyboard order in a browser, or measure contrast. The default black-on-white text and `#1a56db` focus ring should pass, but I haven't verified that. I also can't see the server's response states or any pre-filled values.
