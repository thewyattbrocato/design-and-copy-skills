I only have the spec, not the build. The spec is strong on visual basics, so most of my points are behavior and edge cases it doesn't mention.

## Fix before Friday

1. **Day buttons are ambiguous.** "Mon" doesn't say which Monday. Show the date ("Mon 13") and keep the same date on the confirmation screen. Also decide what happens to a selected time when the day changes. Clear it, and say so.
2. **Empty and failure states for slots.** Cover a day with no openings, slots still loading, and a slot taken between selecting it and submitting. Each needs plain-language copy with a path forward, such as "No openings Tuesday. Try another day or call us."
3. **The confirmation must say "request," not "booked."** The button says "Request this time," so the confirmation should say who will contact them, how soon, and from what number. Repeat the practice's address and phone number too. Without those, people will wonder if they're booked and call anyway.
4. **Text-message consent.** You're collecting a mobile number. If you'll text it, you need consent wording near the field, and the legal exposure is real. If you'll only call, label it "Phone number" and drop the SMS implication.
5. **Error handling on submit.** Move focus to the first invalid field or an error summary. Tie each error to its field with `aria-describedby`. Handle network failure and double-taps, with the button disabled and a busy state while sending.
6. **Confirmation-screen focus.** Move focus to the new heading and update the page title. Otherwise screen reader users get no signal that anything happened.

## Worth doing

- **Phone links.** Make the header number and "Call us instead" real `tel:` links. On desktop, where `tel:` does nothing, show the number as text. Give "Call us instead" a 44px tap area and an underline.
- **Dental emergencies.** Add one line, like "Tooth pain or injury? Call us now," near the top. A request form that gets answered tomorrow is the wrong path for those people.
- **Hours.** If the phone is the fallback, show when someone will pick up.
- **Input details.**
  - Use `type="tel"`, `autocomplete="name"` and `autocomplete="tel"`.
  - Set inputs to at least 16px so iOS doesn't zoom.
  - Accept any phone format and normalize it server-side instead of rejecting "555 0142".
- **Reason-for-visit note.** Add "Please don't include medical details." Free text in a dental form often turns into health information. Confirm the transport and storage are appropriate.
- **Segmented day control.** Treat it as a radio group with arrow-key support. Make the selected state clear without relying on color alone. Check that five buttons plus gaps still hold a 44px target at 320px.
- **Focus ring.** Confirm it reaches at least 3:1 against both the white page and the blue button. Use an offset so it doesn't blend into the button.
- **Spam.** Use a honeypot, rate limiting and server-side checks. Avoid a CAPTCHA, which hurts older and assistive-tech users.

## Testing gaps

360px is one data point. Also check:
- 320px, and 200% text zoom (the header name and phone number must not collide)
- Landscape orientation
- The on-screen keyboard covering the button
- Real iOS Safari and Android Chrome
- A keyboard-only pass
- VoiceOver or TalkBack through the whole flow, including the collapsed note and the confirmation screen

## Leave alone

- The type scale and contrast.
- The single column and the 8px spacing.
- Visible labels and inline errors with an icon.
- The one primary action and the header with no other nav.

Questions that affect the list above: Are you texting patients? Do you want new-versus-existing patient or insurance fields? Skipping them is fine for a fast request form, but decide on purpose.
