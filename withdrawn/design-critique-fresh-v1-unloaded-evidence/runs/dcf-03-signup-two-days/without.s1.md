# Sign-up accessibility audit

This audit is based only on the snippets and descriptions you gave me. I haven't seen the rendered pages, the full markup, or any screen-reader testing, so treat it as a prioritized starting point.

## Fix order

### 1. Screen 2 (human check): fix first, it's a hard blocker
- **Problem:** A distorted-letters image with no alternative locks out blind and low-vision users, and many dyslexic and cognitively disabled users. This fails WCAG 1.1.1 (A) and 3.3.8 Accessible Authentication (AA). These users can't create an account at all.
- **Fix (about half a day):** Replace the check rather than patching it. Restoring the audio button isn't enough, because it excludes deaf-blind users and many people with cognitive or auditory-processing disabilities.
  - Use an invisible or behavioral check, such as Cloudflare Turnstile, reCAPTCHA v3, or hCaptcha's accessibility mode.
  - Alternatively, use no challenge: rate limiting, a honeypot field, and email verification.
  - If you must keep a challenge, offer at least two non-cognitive alternatives.

### 2. Screen 3 (profile): the timeout destroys work
- **Problem:** A 10-minute idle logout with no warning and no way to extend it fails 2.2.1 Timing Adjustable (A). Losing the data on return makes it worse, and people who type slowly, use switch devices, or use screen readers are hit hardest. It also runs against 3.3.7 Redundant Entry.
- **Fix (about 1 day), in this order:**
  1. **Autosave the draft** to the server or `localStorage` and restore it after re-login. This is the biggest win.
  2. **Count typing, focus, and clicks as activity.** A user mid-form shouldn't be "idle."
  3. **Warn about 2 minutes before expiry** with a modal using `role="alertdialog"`. It should offer a keyboard-accessible "Stay signed in" button, and pressing it should extend the session.
  4. Don't hard-reload the page when the session expires.
- **Also check:** I can't see the 14 fields. Confirm each has a real `<label>`, that related fields are grouped with `fieldset`/`legend`, that required fields are marked in text, and that `autocomplete` is set.

### 3. Screen 1 (account): several fixes, mostly quick
In priority order:

1. **Labels (1.3.1, 3.3.2, 4.1.2).** Placeholders are the only labels. They vanish when the user types and are unreliable as accessible names.
   - Add a visible `<label for>` for each input.
   - Keep the placeholder only as an optional hint.
2. **Error handling (1.4.1, 3.3.1, 3.3.3).** A red border alone is invisible to colorblind and blind users.
   - Add error text next to the field, such as "Enter an email like name@example.com."
   - Link it with `aria-describedby`, and set `aria-invalid="true"`.
   - On submit, move focus to the first error or to an error summary. Alternatively, put the message in a `role="alert"` region.
   - Add an icon or text as well as color.
3. **Contrast (1.4.3).** `#aaa` on white is about 2.3:1 and needs 4.5:1. Use `#595959` or darker. Check the default placeholder color too, which is often similarly pale.
4. **Autocomplete (1.3.5).** Add `autocomplete="email"` and `autocomplete="new-password"`. For sign-in, use `current-password`. Also don't block paste, so password managers work (3.3.8).
5. **Hero image alt (1.1.1).** The 40-word description is noise for screen-reader users on every visit. If the image is decorative, use `alt=""`. If it carries meaning, shorten it to a sentence.
6. **Password help (minor).** State the password requirements before the user submits. Consider adding a show/hide toggle with an accessible name.

## Suggested schedule for one developer
- **Day 1 morning:** Replace the human check (Screen 2).
- **Day 1 afternoon to Day 2 midday:** Add draft autosave, activity detection, and the timeout warning (Screen 3).
- **Day 2 afternoon:** Do all the Screen 1 fixes. Labels, contrast, autocomplete, and alt are about an hour. The error handling is the larger piece.
- **Last hour:** Test with keyboard only and one screen reader (VoiceOver on Mac). Walk through all three screens, and zoom to 200%.

If something has to slip, let the Screen 1 contrast and alt-text fixes slip. Don't let the first two items slip, because they are the ones that stop people from signing up.
