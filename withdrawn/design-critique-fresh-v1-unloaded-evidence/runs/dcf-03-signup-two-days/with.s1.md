**Fix first: the human check on Screen 2. It's a barrier, and Screen 3's timeout is a close second.** Both stop a group of people from finishing sign-up, and the three smaller fixes on Screen 1 are cheap enough to batch around them. I ranked by who can't complete the task, not by how many rules a scanner would flag.

**Scope:** I only had the Screen 1 markup and your descriptions of Screens 2 and 3. I haven't run it, so I haven't checked focus order, screen-reader announcements, zoom, or whether the sign-up buttons have names.

## Findings, in fix order

**1. [Blocker] Distorted-text check with no alternative (Screen 2)** — *read from your description*
- **Seen:** The only way through is reading distorted letters. The audio option was removed last year.
- **Why it matters:** Blind users and many low-vision or dyslexic users can't pass it. It also can't be read by a screen reader, so they can't create an account at all.
- **Change:** Remove the test. Swap it for an invisible or risk-based check that asks the person for nothing, or for a vendor check with a documented non-visual route. Don't just put the audio button back, because audio versions are hard for deaf-blind users and for many others. If the swap needs a vendor decision, start that conversation on day 1.

**2. [Blocker] Timeout discards the profile form (Screen 3)** — *read from your description*
- **Seen:** After 10 idle minutes the page reloads to sign-in, and the 14-field form is empty on return.
- **Why it matters:** Anyone who types slowly, uses switch or voice input, or stops to find a document loses all their work. They then have to start over under the same clock.
- **Change:**
  - Save the draft on field blur or change, to the server. If you use `sessionStorage`, leave out sensitive fields.
  - Restore the draft after re-login.
  - Show a warning with an "extend session" button at least 60 seconds before logout.
  - Lengthen the idle limit if your security policy allows.
- The draft saving is the part that matters most. It's the larger piece of work, so start it by early day 2 at the latest.

**3. [Blocker] Errors shown only by a red border (Screen 1)** — *read in the code*
- **Seen:** Validation failure changes the border color and nothing else.
- **Why it matters:** Screen-reader users get no signal that anything failed. Color-blind and low-vision users may not see the change either.
- **Change:**
  - Add text next to the field, such as "Enter an email like name@example.com".
  - Set `aria-invalid="true"` on the field and link the message with `aria-describedby`.
  - Move focus to the first invalid field on submit.
  - Keep the red border as a second cue.
  - Reuse this pattern on Screen 3's 14 fields.

**4. [Major] Placeholders are the only labels (Screen 1)** — *read in the code*
- **Seen:** Neither input has a `<label>`. The text disappears as soon as someone types.
- **Why it matters:** Some screen readers announce no reliable name for the field. Sighted users lose the prompt mid-entry, which hurts people with memory or attention difficulties most.
- **Change:** Add a visible `<label for>` above each field. Add `autocomplete="email"` and `autocomplete="new-password"` (or `current-password` on sign-in). Check Screen 3 for the same pattern.

**5. [Major] Low-contrast text on the email field (Screen 1)** — *computed*
- **Seen:** `color:#aaa` has a contrast ratio of about 2.3:1 on white. That is below the commonly used 4.5:1 for body text. I assumed a white background, since none was supplied.
- **Why it matters:** Low-vision users, and anyone in glare, can't read what they've typed.
- **Change:** Use `#595959` or darker for typed text, which gives about 7:1 on white. Also check the placeholder, border and focus-ring colors, which I haven't computed.

**6. [Minor] Hero image alt text is 170 characters (Screen 1)** — *read in the code*
- **Seen:** The alt text describes a scene (jumper, plant, three trees) that has nothing to do with signing up.
- **Why it matters:** Screen-reader users hear it on every visit before reaching the form.
- **Change:** Use `alt=""` if the image is decoration. If it carries meaning, describe that in one short sentence.

## Suggested plan

I estimated these times myself, so adjust them for your codebase.
- **Day 1:** Start the Screen 2 replacement. Fix findings 3–6 on Screen 1, which should take a few hours and are one pattern you'll reuse.
- **Day 2:** Build the Screen 3 draft saving and the timeout warning. Apply the label and error pattern to its fields. Then do a keyboard-only and screen-reader walk of all three screens.

## What to keep
- **Sign-up split across three short screens:** the 14 profile fields come after account creation, so people aren't facing them up front.
- **Real `<input type='email'>` and `type='password'`:** these give mobile keyboards and password managers the right hints.
- **Red as an error cue:** keep it once text and `aria-invalid` carry the meaning.

## Not checked
Focus visibility, heading structure, page language, button names, Screen 3's field labels and grouping, 200% zoom and 320px width, and the contrast of the red border. After these fixes, have two or three people who use screen readers or magnification try the whole flow.
