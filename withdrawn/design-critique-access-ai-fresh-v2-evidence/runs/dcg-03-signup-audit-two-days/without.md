# Sign-up accessibility audit: what to fix first

This audit is based only on the descriptions you gave me. I haven't run the screens or tested them with a screen reader. The WCAG references are to 2.2 AA.

## Priority order

**1. Screen 2: the letters puzzle is a hard blocker. Start the decision on day 1.**
- Blind users, many low-vision users, and many dyslexic users can't complete it, and nothing else is offered. This fails 1.1.1 (a CAPTCHA needs alternatives for different senses) and 3.3.8 (Accessible Authentication). Reading distorted letters is a cognitive test with no exemption.
- **Best fix:** remove the puzzle. Use an invisible or risk-based check, such as a honeypot field, rate limiting, or a bot-detection service that only challenges suspicious traffic.
- **If you must keep a challenge:** offer a different kind of alternative, such as an emailed or texted code. Audio alone isn't enough, because it excludes deaf-blind users and is hard for many others.
- **Smaller fixes, if it stays:**
  - Give the image alt text that says what it is, for example "Letter puzzle. Use the audio option or another method", but never the answer.
  - Add a real `<label>` to the text box.
  - Make the refresh link a labeled button with a target of at least 24×24px (2.5.8).
  - Announce the new image after a refresh.

**2. Screen 3: the timeout wipes the form.**
- A silent 10-minute timeout that clears every field and sends people back to screen one fails 2.2.1. It hits people who type slowly, use assistive tech, or have cognitive or motor disabilities. It also makes people re-enter data they already gave you (3.3.7).
- **Best fix:** drop the timeout. If there's a real security need, warn at about 2 minutes remaining with an accessible dialog ("Stay signed in"), and let people extend it with a simple action.
- **Either way:** save progress, and never clear the fields on expiry.

**3. Screen 1: errors are invisible to many users.**
- A red border alone fails 1.4.1 (color only), 3.3.1 (the error must be identified in text), and 3.3.3 (suggest a fix). Screen reader users get no signal at all.
- **Fix:**
  - Show text next to the field that says what's wrong and how to fix it.
  - Set `aria-invalid="true"` and link the message with `aria-describedby`.
  - On submit, move focus to the first invalid field or an error summary.
  - State the password rules up front, not only after a failure.

**4. Screen 1: labels and contrast.**
- Placeholders aren't labels. They vanish when typing starts, and support for naming the field is inconsistent. This fails 1.3.1, 3.3.2, and 4.1.2.
- `#999` on white is about 2.8:1. It needs 4.5:1 (1.4.3), so use `#767676` or darker.
- Add `autocomplete="email"` and `autocomplete="new-password"` (1.3.5). Allow password managers and paste.

**5. Screen 3: smaller fixes.**
- The hero image is decorative, so use `alt=""`. Screen reader users currently hear a 50-word description on every visit. This takes one minute, so do it early.
- Give every field a visible label. Add `autocomplete` tokens for name and address (`name`, `street-address`, and so on).
- Group related preferences with `<fieldset>` and `<legend>`.
- Mark required fields in text, and break the long form up with headings.
- Reuse the error pattern from fix 3.

## Suggested two-day plan
- **Day 1:** Decide on the CAPTCHA replacement and start it. It may need a vendor or backend work. In parallel, remove the timeout or add the warning, and save form state. Also change the hero `alt` to `""`.
- **Day 2:** Fix screen 1 labels, error messages, contrast, and autocomplete. Reuse that pattern on screen 3. Finish with a keyboard-only pass and a quick screen reader check (VoiceOver is already on your Mac) through the whole flow.

## Screen 1 sketch
```html
<form id="acct" novalidate>
  <label for="email">Email address</label>
  <input id="email" type="email" autocomplete="email"
         aria-describedby="email-err" style="color:#595959">
  <p id="email-err" class="error" hidden>Enter an email like name@example.com.</p>

  <label for="pw">Password</label>
  <p id="pw-hint">At least 12 characters.</p>
  <input id="pw" type="password" autocomplete="new-password"
         aria-describedby="pw-hint pw-err">
  <p id="pw-err" class="error" hidden></p>

  <button type="submit">Continue</button>
</form>
```
In the script, on a failed field, set `aria-invalid="true"`, unhide and fill its message, and keep the border change as extra reinforcement. Add an error icon so the signal doesn't rely on color alone. Then focus the first invalid field.

If you share the real code for any screen, I can check these against it.
