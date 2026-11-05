# Sign-up accessibility audit

I only had the snippets you pasted, not the running pages. Anything I flag as "check" is something I couldn't see.

## Fix order

### 1. Screen 2: the human check is a hard block (fix first)
- **Problem:** Distorted text with no alternative means blind and many low-vision, dyslexic and cognitive-disability users cannot sign up at all. It fails WCAG 1.1.1 (Level A), which requires a CAPTCHA to offer an alternative in a different modality. It likely also fails 3.3.8 Accessible Authentication.
- **Fix:** Replace it rather than restoring the audio button. Audio CAPTCHAs are hard to use and exclude deaf-blind users. Use a risk-based or invisible challenge (Turnstile, hCaptcha, reCAPTCHA v3, or similar), or verify by email link or code. This is probably a half-day swap with a vendor widget.
- **Check:** Whatever you pick must be operable by keyboard and screen reader, and any fallback challenge needs a non-visual path.

### 2. Screen 3: the timeout destroys the user's work
- **Problem:** A silent 10-minute inactivity logout that wipes a 14-field form fails 2.2.1 Timing Adjustable (Level A). It hits people who type slowly, use switch or voice input, have cognitive disabilities, or get interrupted.
- **Fix, in order of value:**
  1. Preserve the data. Autosave to `sessionStorage` or the server on `input`/`change`, and restore it after re-login. This removes most of the harm.
  2. Warn about 60 seconds before expiry with a modal (`role="alertdialog"`, focus moved into it) and an "I need more time" button that resets the timer.
  3. Consider a longer timeout, or none while the user is actively on a form.
- **Check:** Make sure all 14 fields have real `<label>`s, since I couldn't see them.

### 3. Screen 1: errors, labels and contrast
These are small fixes, roughly 2–3 hours together.

| Issue | WCAG | Fix |
|---|---|---|
| Errors shown only as a red border | 1.4.1, 3.3.1, 4.1.3 | Add visible text such as "Enter a valid email, like name@example.com". Set `aria-invalid="true"` and link the message with `aria-describedby`. On submit, move focus to the first error or an error summary. Add an error icon. |
| Placeholder is the only label | 1.3.1, 3.3.2 | Add visible `<label for>` elements. Placeholders vanish on typing and have poor contrast. |
| `color:#aaa` on white is about 2.3:1 | 1.4.3 | Use at least 4.5:1, for example `#595959` or darker. Also check the border (3:1, per 1.4.11) and the red error color. |
| No autofill hints | 1.3.5 | Add `autocomplete="email"` and `autocomplete="new-password"` (or `current-password` on sign-in). |
| The `alt` text is a 30-word scene description | 1.1.1 | The image is almost certainly decorative, so use `alt=""`. If it carries meaning, shorten it to a few words. |

**Check:** Look for a visible focus indicator, a submit button that is a real `<button>`, password requirements stated before submission, and no blocked paste in the password field.

## Suggested schedule
- **Day 1:** Screen 2 replacement and testing. This has the most unknowns.
- **Day 2 morning:** Screen 3 autosave and restore, then the timeout warning.
- **Day 2 afternoon:** Screen 1 fixes, then a keyboard-only and screen reader pass (VoiceOver or NVDA) over all three screens.

If time runs short, ship items 1 and 2 first, plus the `alt=""` and label changes from item 3 (about 15 minutes).
