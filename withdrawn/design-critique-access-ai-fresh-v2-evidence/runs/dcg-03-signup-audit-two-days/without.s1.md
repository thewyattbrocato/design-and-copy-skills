# Sign-up accessibility audit

This audit is based only on the descriptions you gave me. I haven't run the screens or tested them with a screen reader. The contrast figure assumes a white background.

## Priority order

| # | Issue | Screen | Impact | Effort |
|---|---|---|---|---|
| 1 | Distorted-text CAPTCHA with no alternative | 2 | Complete block for blind and many low-vision, dyslexic or cognitive-disability users | Medium to high, since it depends on your backend or vendor |
| 2 | 10-minute timeout wipes the form and returns to screen 1 | 3 | Data loss, and people who need more time can never finish | Medium |
| 3 | No labels, only placeholders | 1 | Screen readers get no reliable field name, and the hint vanishes once someone types | Low |
| 4 | Errors shown only as a red border | 1 | Invisible to blind and color-blind users, and nobody is told what is wrong | Low |
| 5 | Placeholder and text color `#999` | 1 | About 2.8:1 on white, below the 4.5:1 minimum | Trivial |
| 6 | Hero image alt text is too long and unneeded | 3 | Screen reader users hear a paragraph of noise | Trivial |
| 7 | Small refresh link and form structure | 2 and 3 | Hard to hit, and the long form is hard to navigate | Low |

## Details and fixes

**1. CAPTCHA (WCAG 1.1.1, 3.3.8 Accessible Authentication)**
- Transcribing distorted letters is a cognitive test with no alternative, so some users cannot pass it at all.
- The best fix is to remove it. Use a risk-based or invisible check, rate limiting, or email verification instead.
- If you must keep a challenge, offer at least one non-visual, non-memory alternative, such as audio or an emailed code. Offering several is better.
- Whatever you keep, give the image a text alternative that says what it is and where to find the alternative. Don't put the answer in the alt text.
- Make the refresh control a real `<button>` with a name like "Get new letters". It needs a hit area of at least 24×24px (2.5.8). Announce the change with a polite live region.
- Start this first. If it needs a vendor or backend decision, that decision is your biggest schedule risk.

**2. Timeout (WCAG 2.2.1 Timing Adjustable, 3.3.7 Redundant Entry)**
- Warn users about 2 minutes before expiry in a dialog that takes focus and is announced. Let them extend with a single action.
- Better still, make the timeout much longer or remove it. If it exists for security, save the draft on the client or server so a lapse doesn't clear fields.
- Never send people back to screen 1 with everything cleared. If they are logged out, return them to where they were with their entries restored.

**3. Labels**
```html
<label for="email">Email address</label>
<input id="email" type="email" autocomplete="email" aria-describedby="email-err">
<label for="pw">Password</label>
<input id="pw" type="password" autocomplete="new-password">
```
Keep the placeholder only as an optional example. Put any password rules in visible text tied to the field with `aria-describedby`. The `autocomplete` values also cover 1.3.5. Use the matching ones on screen 3 for name and address, such as `name`, `street-address` and `postal-code`.

**4. Errors (WCAG 1.4.1, 3.3.1, 3.3.3, 4.1.3)**
- Show text next to the field, such as "Enter an email like name@example.com". Don't rely on color, and add an icon too.
- Set `aria-invalid="true"` and link the message with `aria-describedby`.
- On submit, move focus to the first invalid field, or to an error summary with links to each field.
- Keep the 2px red border only as reinforcement. Check that it has at least 3:1 contrast against the background.

**5. Contrast (WCAG 1.4.3)**
- Use `#595959` or darker for text and placeholders on white. That gives about 7:1.
- Don't dim the placeholder with default browser opacity. Set `::placeholder` explicitly.

**6. Hero image**
- It is decorative, so use `alt=""`. That is better than shortening the text. If it's a CSS-able background, move it to CSS.
- A 40-word description of a plant and a cup of tea adds nothing to the task.

**7. Structure on screen 3**
- Group related fields in `<fieldset><legend>`, for example "Address" and "Preferences".
- Use a heading for each section and a visible label for each field.
- Mark required fields in text, not only with color or an asterisk.
- I can't see this markup, so check it against this list.

## Two-day plan

**Day 1**
- Morning: items 3, 4, 5 and 6. They are small and all fixable in a few hours.
- Afternoon: decide what replaces the CAPTCHA, and start the implementation. Begin the timeout warning and draft-saving too.

**Day 2**
- Finish the CAPTCHA replacement and the timeout.
- Do the item 7 cleanup.
- Test the full flow by keyboard only, then with VoiceOver on macOS (you're on Darwin) or NVDA. Run axe or Lighthouse too, but note that automated tools won't catch items 1 and 2.

If the CAPTCHA can't be replaced in two days, ship an interim alternative such as an emailed code or a support contact. Make that path visible on screen 2 and don't leave it to be discovered.

If you paste the real markup for screen 3, or the script that handles the timeout and the errors, I can give you specific patches.
