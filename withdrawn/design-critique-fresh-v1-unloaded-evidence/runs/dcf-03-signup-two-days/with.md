**Verdict:** Screen 2 stops some people from signing up at all, and Screen 3 throws away their work. Fix those two first. Screen 1's problems are real but small, and one developer can clear them in a few hours.

I ranked by whether a named group can finish sign-up. I reviewed markup and descriptions only, so nothing was run with a screen reader, a keyboard or zoom. Effort figures are my estimates.

## Fix order

**1. [Blocker] Human check has no non-visual route (Screen 2)**
- **Seen:** An image of distorted letters and a text box. The audio button was removed, and there is no other way through. *(read from your description)*
- **Why it matters:** Blind and low-vision users can't pass. People with dyslexia or cognitive disabilities often can't either. Nobody in these groups can create an account.
- **Change:** Replace the test rather than patch it. The options below are in order of preference.
  - Drop the puzzle and use a behind-the-scenes check: rate limiting, a honeypot field and server-side risk scoring.
  - Use a vendor challenge that needs no puzzle.
  - If you must keep a puzzle, offer at least two routes, such as audio plus a simple text question. Restoring the audio button alone leaves deaf-blind users and many others out.
- **Effort:** About 0.5–1 day, depending on what your backend already has. Start here because it carries the most uncertainty.

**2. [Blocker] Timeout wipes the profile form (Screen 3)**
- **Seen:** A script ends the session after 10 minutes of inactivity. The page reloads to sign-in and the form is empty when the user returns. The form has about 14 fields. *(read from your description)*
- **Why it matters:** Screen-reader, switch and voice users, and people who need time to read or find information, often take longer than 10 minutes on a long form. They lose everything and have to start again, and the same thing happens again.
- **Change:** Do these in order, and stop once the first two are done if time runs out.
  - Warn at about 8 minutes with an "I need more time" button that resets the timer. Make the warning a focusable dialog and announce it to screen readers.
  - Save a draft so a timeout never loses data, either on field blur or in `sessionStorage`. Restore it after sign-in.
  - Consider lengthening the timeout or removing it on this screen, if security allows.
- **Effort:** About 0.5–1 day.

**3. [Major] Errors are shown by a red border only (Screen 1, and probably Screen 3)**
- **Seen:** "On a validation error the input gets a red border and nothing else changes."
- **Why it matters:** Color-blind and low-vision users may not notice the border. Screen-reader users get no announcement at all. Nobody is told what is wrong or how to fix it.
- **Change:** Add text next to each invalid field, such as "Enter an email like name@example.com". Link it with `aria-describedby` and set `aria-invalid="true"`. Add an error summary at the top and move focus to it on submit. Keep the border, but don't rely on it.
- **Effort:** About 2–3 hours as a shared component, reused on Screen 3.

**4. [Major] Fields have placeholders but no labels (Screen 1; Screen 3 not seen)**
- **Seen:** `<input type='email' placeholder='Email address'>` and `<input type='password' placeholder='Password'>`. There is no `<label>`, `id` or `autocomplete`. *(read in the code)*
- **Why it matters:**
  - Placeholders aren't a reliable accessible name.
  - The label disappears once the user starts typing, which hurts anyone with a memory or attention difficulty.
  - Voice-control users can't say "click Email".
  - Without `autocomplete`, password managers and autofill work worse.
- **Change:** Add a visible `<label for>` to every field. Add `autocomplete="email"` and `autocomplete="new-password"`, and the right values on Screen 3. Check whether Screen 3's 14 fields have the same problem.
- **Effort:** About 1–2 hours for Screen 1. Screen 3 depends on its markup, which I haven't seen.

**5. [Minor] Low-contrast text (Screen 1)**
- **Seen:** `color:#aaa` on the email input. *(computed)* On a white background (assumed, not supplied) that is about 2.3:1. The usual minimum for body text is 4.5:1.
- **Why it matters:** Low-vision users struggle to read what they typed.
- **Change:** Use `#595959` or darker (about 7:1 on white). Check the placeholder and label colors the same way, because I couldn't compute them.
- **Effort:** About 15 minutes.

**6. [Minor] Over-long alt text on a decorative image (Screen 1)**
- **Seen:** `alt` is a roughly 160-character scene description of the hero image. *(read in the code)*
- **Why it matters:** A screen reader reads all of it before the user reaches the form, and it adds nothing to the sign-up task.
- **Change:** Use `alt=""` if the image is decorative, which I assume it is. Otherwise shorten it to under about 10 words.
- **Effort:** 5 minutes.

## Two-day plan

| When | Work |
|---|---|
| Day 1 | Replace the human check (#1). Add the timeout warning and draft save (#2). |
| Day 2 morning | Shared error pattern and labels, applied to all three screens (#3, #4). |
| Day 2 afternoon | Contrast and alt text (#5, #6). Then a keyboard-only and screen-reader walk of the full sign-up. |

If #1 runs long, cut #2 to the warning and extend button and ship the draft save next. Don't skip #3 and #4. They are cheap and reach every user on every screen.

## What works
- **Real input types:** `type='email'` and `type='password'` give mobile users the right keyboard and give assistive tech the right role.
- **The hero image has alt text:** The image isn't unlabeled, and a quick edit fixes it.
- **Your instinct to mark errors visually:** The red border is a fine second signal once text is added.

## Not checked
- Screen 3's markup, so labels, grouping, tab order and focus behavior are unknown. Likewise the hero image's role, button styles, focus indicators and page language.
- Anything needing a person or device: screen-reader announcements, keyboard focus order, 200% zoom, a 320px width and forced colors.
- Any legal or compliance level. This review finds known faults and can't clear the product. Once the blockers are fixed, run a short session with a few disabled users on the real sign-up task.
