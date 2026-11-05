# Sign-up accessibility audit: what to fix first

I audited from the snippets and descriptions you gave me. I haven't tested with a screen reader or seen the real styles. The contrast figure assumes a white background.

## Priority order

### 1. Screen 2, the human check (fix first, about half a day)
**Problem:** Distorted text with no alternative means blind and low-vision users, and many dyslexic or cognitively disabled users, cannot sign up at all. This fails WCAG 1.1.1 (non-text content) and 3.3.8 (accessible authentication, AA in 2.2). Removing the audio button also doesn't solve this. Audio CAPTCHAs have their own problems, and it was removed anyway.

**Fix, cheapest first:**
- Replace the check with a non-puzzle method: an invisible or behavioral check (Cloudflare Turnstile, reCAPTCHA v3, or hCaptcha's accessibility mode), a honeypot field, rate limiting, or email verification. This is usually a drop-in swap.
- If you must keep a challenge, offer at least one other route, such as email verification or a contact path with a human. Restoring audio alone isn't enough.

### 2. Screen 3, the session timeout (about half a day)
**Problem:** The timeout is silent and it wipes the form. This fails WCAG 2.2.1 (timing adjustable). Screen reader users, people with motor or cognitive disabilities, and anyone who is interrupted will lose up to 14 fields of work. It also fails 3.3.7 (redundant entry) in spirit.

**Fix:**
- Show a warning dialog at about 2 minutes remaining, with a "Stay signed in" button. Make it `role="alertdialog"` and move focus into it.
- Autosave the draft, either server-side or in `sessionStorage` on input, and restore it after sign-in. Don't store sensitive fields in browser storage.
- Without a warning, a 10-minute idle limit is hard to justify on a long form. Consider counting typing as activity, or extending the limit.

The autosave is the bigger win. It helps every user, and it covers you if the warning is missed.

### 3. Screen 1, labels and errors (about 1 day)
Do these in this order, since they all touch the same form:

1. **Add real labels.** Placeholder-only inputs fail 1.3.1, 3.3.2, and 4.1.2. The placeholder disappears when the user types, and it often isn't announced reliably. Add visible `<label for>` elements and keep the placeholders only as hints.
2. **Make errors more than a red border.** The border alone fails 1.4.1 (use of color), 3.3.1 (error identification), and 3.3.3 (error suggestion). Add:
   - Text next to the field, such as "Enter an email like name@example.com".
   - `aria-invalid="true"` and `aria-describedby` pointing to that message.
   - Focus on the first invalid field, or an error summary with `role="alert"`.
   - An error icon, so color isn't the only cue.
3. **Fix the text color.** `#aaa` on white is about 2.3:1, and the minimum is 4.5:1 (1.4.3). Use `#595959` or darker. Check the placeholder color too. Also make sure the red border has at least 3:1 against the background (1.4.11).
4. **Add `autocomplete`** (1.3.5 and 3.3.8): `autocomplete="email"` on the email field, and `current-password` or `new-password` on the password field. Also make sure paste works in the password field so password managers can fill it.
5. **Fix the image alt text.** The 170-character description is noise for a screen reader user. If the hero image is decorative, use `alt=""`. If it carries meaning, shorten the alt text to one short sentence.

## Two-day plan for one developer

| When | Work |
|---|---|
| Day 1 morning | Replace the CAPTCHA (item 1) |
| Day 1 afternoon | Timeout warning and draft autosave (item 2) |
| Day 2 | Screen 1 items 1–5 |
| Day 2, last hour | Keyboard-only and screen reader pass on all three screens (VoiceOver is already on your Mac) |

## Not checked yet
Because I only had snippets, check these during the final pass:
- Visible focus indicators.
- Labels on the 14 profile fields.
- Whether required fields are marked in text, not just with color or an asterisk.
- Whether there's a real `<form>` and submit button.
- Whether the timeout warning is reachable by keyboard.

If you paste the Screen 3 markup and the form's CSS, I can extend the audit to those.
