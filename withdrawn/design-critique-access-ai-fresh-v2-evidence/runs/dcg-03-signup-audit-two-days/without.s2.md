# Sign-up accessibility audit

This audit comes from the markup and descriptions you gave me. I haven't run the screens, so confirm the fixes with a keyboard-only pass and a screen reader (VVoiceOver or NVDA) before you ship.

## Fix order

| # | Issue | Screen | Why it's here | Effort |
|---|---|---|---|---|
| 1 | Image-only human check with no alternative | 2 | Blind and many low-vision or dyslexic users **cannot sign up at all** (WCAG 1.1.1) | Highest, so start first |
| 2 | Errors shown only as a red border | 1 | Users don't know a field failed or why. Screen reader users get no signal, and color-blind users may not see it (1.4.1, 3.3.1) | ~2 hrs |
| 3 | 10-minute timeout that wipes the form | 3 | Slower users lose everything and restart from screen one (2.2.1) | ~half day |
| 4 | Placeholder-only labels | 1 | Fields have no reliable accessible name, and the label vanishes on typing (1.3.1, 3.3.2, 4.1.2) | ~30 min |
| 5 | `#999` text, about 2.85:1 contrast | 1 | Fails the 4.5:1 minimum (1.4.3) | ~10 min |
| 6 | Verbose `alt` on the decorative hero | 3 | Screen readers read out 40+ words of noise (1.1.1) | ~1 min |
| 7 | Smaller items (below) | all | Polish | as time allows |

## Details and fixes

**1. Human check (screen 2).** A refresh link doesn't help someone who can't read the image. Two options:
- **Best:** replace the check with one that has no perceptual puzzle. Examples are an invisible or behavioral bot check, a honeypot field plus rate limiting, or email verification. This also avoids cognitive-test problems for people with dyslexia or memory disabilities.
- **Stopgap if you can't swap it in two days:** offer at least one non-visual alternative, such as an audio challenge, plus a human fallback like a support email or phone number. Audio alone still excludes deaf-blind users, so don't treat it as the final fix.

Either way:
- Give the image an `alt` that says what it is, such as "Distorted letters, human verification". It must **not** contain the answer.
- Give the text box a real `<label>`.
- Make the refresh control a `<button>` with an accessible name ("Get new letters") and a target of at least 24×24px (2.5.8).
- Announce the new image through an `aria-live` region.

**2. Errors (screen 1).** Keep the red border, but add a visible text message, an icon, and programmatic links:
```html
<label for="email">Email address</label>
<input id="email" type="email" autocomplete="email"
       aria-invalid="true" aria-describedby="email-err">
<p id="email-err">Enter an email address like name@example.com.</p>
```
- Message text should say what's wrong and how to fix it.
- On submit, move focus to the first invalid field, or to an error summary at the top that links to each field.
- Don't rely on red alone. The message text and icon carry the meaning.

**3. Timeout (screen 3).** The best fix is to remove it. If it's there for security, do these:
- Warn at about 8 minutes with a dialog that is focusable and announced.
- Let the user extend with one action, such as "Stay signed in". It must give at least 20 seconds to respond and allow extending at least 10 times.
- Save progress server-side or in `sessionStorage` so an expiry doesn't clear fields.
- If the session still has to expire, return the user to this step, not screen one, with their entries restored.

**4. Labels (screen 1).** Add visible `<label for>` elements, as in the snippet above. Keep placeholders only as optional hints. Also add `autocomplete="email"` and `autocomplete="new-password"` (1.3.5). State password rules in text before the user submits, and tie them to the field with `aria-describedby`.

**5. Contrast.** `#999` on white is about 2.85:1. `#767676` just passes at 4.54:1, and `#595959` gives comfortable headroom. Note that your inline style also colors the *typed* text, not just the placeholder. Make typed text dark (`#1a1a1a` or similar) and keep the placeholder as the lighter, still-compliant color.

**6. Hero image.** It's decorative, so use `alt=""` (or move it to CSS). Describing the plant and the tea adds nothing. If you want it to convey meaning, one short phrase is enough.

## Not enough information yet (screen 3 fields)
I can't audit the name, address, and preference fields or the long form from the description. Check them for:
- visible labels
- `autocomplete` tokens (`name`, `street-address`, and so on)
- `<fieldset>` and `<legend>` around grouped preferences or radios
- required fields marked in text, not just with an asterisk color
- the same error pattern as screen 1
- sensible tab order
- section headings, so the long form can be navigated

## Suggested schedule
- **Day 1 morning:** items 2, 4, 5, and 6. This is the quick work, and it makes screen 1 fully usable.
- **Day 1 afternoon through Day 2 midday:** item 3 (timeout and saved state), then item 1.
- **Day 2 afternoon:** keyboard and screen reader test of all three screens, then the screen 3 field review.

If item 1 can't be fully resolved in time, ship the stopgap (alt text, audio, human fallback) and schedule the replacement.

If you paste the screen 3 form markup, I can review it too.
