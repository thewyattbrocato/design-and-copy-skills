**What should have happened**

On submit, the app should validate all 30 fields and keep everything the user entered. The user should then see:
- An error summary at the top that links to each invalid field. Here that is one field, but there could be several.
- An inline message next to the bad field. It should say what's wrong and how to fix it, e.g. "End date must be after start date", not "Invalid input".
- Focus moved to the first error, with the error announced to screen readers (`aria-invalid`, `aria-describedby`, and a live region or focus on the summary).
- Every other value still in place, including selects, checkboxes, and file uploads where the browser allows it.

A validation error is a normal outcome, not a failure. It should never cost the user their work.

**Likely causes**

I haven't seen your code, so these are the usual suspects:
1. The form posts normally and the server re-renders a fresh, empty form on error. It doesn't re-populate the values.
2. The client handler calls `form.reset()` or re-mounts the component, e.g. a `key` change or a conditional render that unmounts the form on error state.
3. On a validation error, the server returns a redirect or a 4xx, and the client navigates away or reloads.
4. Session expiry or a CSRF failure is being reported as a field error, and the form is then discarded.

**Fix**

1. **Preserve state on error.** This is the core fix.
   - Server-rendered: re-render the form with the submitted values and the errors.
   - SPA: keep the values in form state, and only clear them after a confirmed success response.
   - Never reset in a `finally` or on error.
2. **Validate earlier.** Check each field on blur, and re-validate on change once a field has been flagged. Add a client-side check before submit that mirrors the server rules. The server stays authoritative. Return field-level errors in a structured shape, e.g. `{field: message}`, not a single string.
3. **Autosave drafts.** For a 30-field application, save to `localStorage` or the server, debounced, and restore on load. This also covers crashes, tab closes, session timeouts, and flaky networks. It is the real "never again" protection.
4. **Warn before leaving.** Use a `beforeunload` guard while the form is dirty.
5. **Handle non-validation failures separately.** For a 500, a network error, or an expired session, keep the data, show a retry message, and offer to save the draft. Don't conflate these with field errors.
6. **Consider structure.** Break the form into sections with a progress indicator and per-section validation, so errors surface sooner and sit closer to where the user is working.

**Tests to add**
- Fill 30 fields with one invalid, submit, and assert that all 29 valid values remain, the error is shown, and focus is on the bad field.
- Do the same for multiple invalid fields.
- Simulate a server 500 and a network failure, and assert that the data persists.
- Reload mid-form and assert that the draft is restored.
- Submit successfully and assert that the draft is cleared.

If you point me at the form code, I can find which cause is responsible and make the change.
