Overall it's in good shape and nothing in the markup blocks a merge. These parts are already right:
- Language, title and viewport are set.
- The skip link is hidden until focused and then revealed.
- There is one h1 with a logical h2 structure.
- The nav is labelled and uses `aria-current`.
- Every input has a programmatic label.
- The checkboxes are grouped in a fieldset with a legend.
- The `autocomplete` tokens are correct.
- The focus ring is visible and has no `outline: none` anywhere.

Findings, ranked by harm:

1. **Save feedback isn't in this file.** After the POST, the response page needs a visible result, such as "Settings saved". Server-side validation errors need the same treatment.
   - Put the message in a `role="status"` region for success. For errors, use `role="alert"` or move focus to an error summary.
   - Put each error text beside its field and link it with `aria-describedby` and `aria-invalid="true"`.
   - Keep what the person typed when re-rendering.
   - Also check that the template prefills the display name, email and saved checkbox states. As written, the checkboxes would misreport the user's current settings.

2. **Required fields have no visible cue.** `required` is announced to screen readers, but sighted users get no hint until they submit. Add a short note and mark the labels:
   ```html
   <p>All fields in Profile are required.</p>
   ```
   If you'd rather mark each label, use `Display name <span aria-hidden="true">*</span>` and explain the asterisk in the note.

3. **Labels and inputs run inline.** Nothing sets their layout, so "Display name [input] Email address [input]" will flow together on one line, and it gets worse at 320px or 200% zoom. This is a readability and reflow problem, not a name-association problem.
   ```css
   label, input:not([type=checkbox]) { display: block; }
   input:not([type=checkbox]) { margin: .25rem 0 1rem; max-width: 100%; }
   fieldset label { margin-bottom: .5rem; }
   ```

4. **No pending state on Save.** A slow POST gives no acknowledgement, and the button can be pressed twice. If you add a small submit handler that sets `disabled` and changes the label to "Saving…", also make sure the page still works without JavaScript.

5. **Skip target hardening (minor).** Add `tabindex="-1"` to `<main id="main">` so focus reliably moves there in older Safari builds.

I only read the code. I didn't run a screen reader, test keyboard flow in a browser, or measure contrast on rendered pages. The default link and button colors depend on the browser, so check them against your site CSS.
