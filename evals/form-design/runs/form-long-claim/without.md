# Structure for a multi-day online insurance claim

The core design problem is that this is not a form but a **case that people return to over days**. Structure it around resuming, not around finishing in one sitting.

## 1. Entry and orientation
- **Start screen:** what the claim involves, how long it takes (be honest: "most people finish in 2–3 days"), and a checklist of what to gather up front (policy number, police report number or document, photos, dates, contact details of other parties).
- **Account or magic-link sign-in at the start**, so progress is tied to the person from the first answer. Offer to email or text a resume link.
- **Early triage questions** (3–5) that set the path: type of incident, injuries, other vehicles or parties, whether police attended. These drive which later sections appear.

## 2. Sections (about 6–7, roughly 5–8 questions each)
1. **About you and the policy:** identity, policy, contact preferences.
2. **The incident:** when, where, what happened, in plain language.
3. **People and parties involved:** other drivers, passengers, witnesses. Repeating group ("add another person").
4. **Police and official reports:** whether police attended, report number, upload.
5. **Damage and loss:** description, photos, estimates, items lost.
6. **Injuries / other losses** (shown only if triage says relevant).
7. **Review and submit:** summary, declaration, signature.

Order from easiest and most factual to the hardest, so early momentum comes quickly and the slow parts (documents, photos) sit in the middle where people can pause.

## 3. Conditional logic
- **Document the dependencies in a map** before building: each dependent question, the answer that triggers it, and what appears (a question, a whole section, or an upload requirement).
- **Show follow-ups inline,** directly below the triggering answer, so cause and effect are visible.
- **Keep the progress indicator honest:** it recalculates when answers add or remove sections, and it says so ("2 questions added based on your answer").
- **If an earlier answer is changed,** warn what will be removed, and keep the hidden answers for a while so changing back isn't punishing.

## 4. Photos and police report
- **Make these separate, labeled steps,** not buried in questions. Each has a clear list: which photos (overall damage, close-ups, other vehicle, scene), with example images.
- **Allow upload now or later.** A "I'll add this later" option, which marks the item as outstanding without blocking progress.
- **Handle the police report two ways:** upload a document, or enter the report number and let the insurer retrieve it. Include "not available yet" with an expected date.
- **Support phone use:** camera capture, large files, slow connections, and upload progress with retry. Show thumbnails and let people remove or replace.
- **Accept common formats** (including phone-native image formats) and give plain-language errors.

## 5. Save, resume, and re-engagement
- **Autosave on every answer,** with a visible "saved" confirmation.
- **A claim dashboard** on return: status per section (not started / in progress / complete), what's outstanding, and a single "Continue where you left off" button.
- **Reminders** by email or text: after 24 hours of inactivity, then at sensible intervals, each listing exactly what's left. Include an opt-out.
- **Session handling:** long timeouts or silent re-authentication, so no one loses work. Show draft expiry (for example, 30 days) up front.
- **Allow switching devices** (answers on desktop, photos from phone), possibly via a QR code or text link for uploads.

## 6. Support and reassurance
- **Inline help** on tricky questions ("Why we ask this").
- **Visible contact options:** phone, chat, callback, and the ability to hand the claim to an agent mid-way.
- **Tone:** these users may be stressed or injured. Short, plain language, with an acknowledgment at the start.
- **Accessibility:** keyboard and screen reader support, clear error messages, and readable on mobile.

## 7. Review, submit, and after
- **Review page** grouped by section, with edit links and flagged missing items.
- **Allow submission with outstanding documents** where policy allows, and track them as follow-ups.
- **Confirmation:** claim number, summary copy by email, what happens next, expected timeline, and how to add documents afterward.
- **Status tracking** replaces the form: the same dashboard now shows progress of the claim.

## 8. Measure and refine
- Track **drop-off by question and by day,** time per section, upload failures, resume rate, and which reminders bring people back.
- **Test with people mid-incident** or recently through a claim, and watch the photo and police-report steps in particular. They are the likeliest causes of the multi-day delay.
