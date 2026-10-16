**What should have happened**

The form should have kept all 30 answers and told the user which field needs fixing. Concretely:

- Every value the user typed is still in the form after the failed submit.
- A summary at the top lists each problem as a link to its field. Focus moves to the summary, and the page title carries the count, for example "1 problem: Grant application".
- The field with the problem has its own message next to it, with a cue besides color. The message says how to fix it, for example "Enter a budget as a number, like 12,000". It should not say "Invalid".
- The user fixes the field, and the message disappears as soon as the value is valid.

Wiping the form is a data-loss bug. A validation error is a normal part of the flow and should never cost the user their work.

**How to fix it**

1. **Find the cause.** There are usually two possible causes:
   - The error response triggers a full page reload or re-render that resets state. A server-rendered form that doesn't repopulate fields does this, and so does a component that remounts on error.
   - The error handler explicitly calls `reset()` or clears state.

   The fix is to repopulate every field from the submitted values, or to stop resetting.

2. **Never clear on failure.** Reset the form only after a confirmed success. This applies to server errors and timeouts as well as validation errors. On a server failure, show the explanation at the top and keep the values.

3. **Show errors properly.** This is the field-level message, summary, focus move and title count described above. Messages should name the fix and avoid "invalid" and "please".

4. **Keep the submit button pressable.** Don't disable it until the form is valid. Disable it only while a request is in flight, to block double submits.

5. **Validate on submit, then live.** Check on submit. After a field has shown an error, re-check it as the user edits.

6. **Run the same checks on the server.** Client checks alone aren't enough. If the server rejects something the client allowed, map the server's field errors back onto the form in the same format.

7. **Protect long forms against other data loss.** At 30 fields, this form is long enough to need it:
   - Autosave drafts to local storage or the server. Restore them after a reload, a crash or a back press.
   - Consider splitting the form into named steps ("Budget, step 3 of 5") and validating each step as the user leaves it. Errors then surface earlier, closer to where the user made them.
   - Add a review page with edit links before the final submit, since a grant application is hard to undo.
   - Warn before navigating away from unsaved changes.

8. **Add regression tests.**
   - Submit with one bad field, then assert that all other values are intact, the summary is shown and focus is on it.
   - Simulate a server 500 and a timeout, and assert that the values survive in both cases.
   - Reload after a failed submit and assert that the draft is restored.

If you point me at the form's code, I can find where the wipe happens and implement the fix.
