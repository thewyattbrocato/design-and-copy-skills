**Term table**

| Concept | Today | Pick | Why |
|---|---|---|---|
| A scheduled slot | Appointments (nav), Bookings (page title), Visits (tooltip), Session (patient email) | **Appointment** everywhere | It's the word clinics and patients already use. The nav and the page title it opens must match. "Booking" describes the act of making one, not the thing. |
| End your login | Log off, Exit, Sign in | **Sign in / Sign out** | Keep the pair as true opposites. "Exit" is also ambiguous because it could mean closing a screen, so use "Sign out" for that settings button. |
| Remove an appointment | Cancel | **Cancel appointment** | Cancelling is a real event with consequences for the clinic and the patient. Keep this verb for appointments only. |
| Remove a note | Remove | **Delete note** | See the split below. |
| Remove a patient record | Delete | **Delete patient record** | Same verb as notes. This one needs the strongest confirmation. |
| Remove a draft | Discard | **Discard draft** | Keep it. The draft was never saved, and "discard" is the natural word for that. |
| Clinician | Practitioners (staff) / Your therapist (patient app) | **Practitioner** in both, with a possible exception below | The same person has two names. |
| Patient | Members (founder's decision) | **Member** | Settled. See the note below. |

**Which ones to fix**

1. **Appointments, Bookings, Visits, Session.** This is the worst problem. One object has four names, so users will assume there are four things. Standardise on "Appointment" in the nav, page title, tooltip and email.
2. **Log off, Exit, Sign in.** Change them to "Sign in" and "Sign out". Don't use "Log off" or "Exit" for this.
3. **Practitioner and "Your therapist".** Pick one. Not every clinician in a physio clinic is a therapist, so "Practitioner" is safer. In the patient app, "Your practitioner" keeps it personal and matches what staff see. If you want a warmer patient-side word, choose it deliberately and use it consistently there. Don't leave it as an accident.

**Removing things: mostly keep, tighten two**

These four are not the same action, so four verbs can be fine. Use this rule:

- **Cancel**: an appointment only. It's the real-world event.
- **Discard**: unsaved work, such as a draft.
- **Delete**: saved content that is gone for good. Use it for notes and patient records, and change "Remove" on notes to "Delete note". "Remove" implies you can bring it back or that it's only detached.

Each button should name its object, for example "Delete patient record" or "Cancel appointment". For destructive confirmations, make the decline neutral and equal in weight, for example "Delete patient record" / "Keep record" or "Cancel appointment" / "Keep appointment". Don't use "OK / Cancel". On a cancellation dialog, "Cancel" as the decline is confusing, which is another reason to use "Keep appointment".

**Members and "clients"**

Use "Member" for the product's own strings, as the founder decided. If some clinics want "clients", the option is a per-clinic label setting, which is a product decision for you and the founder to make. Until then, don't mix "client" into any strings. Two things to check:

- "Member" and "Practitioner" are different kinds of word (one is a brand term, the other is a job). That's fine, but make sure every mention of a patient says "Member". Look for stray "patient" in the UI, since "Delete patient record" above would then need to become "Delete member record".
- Clinical or legal contexts, such as records, consent and notes, may be where "patient" is needed for compliance. I can't tell from what you've given me, so check that with the founder or whoever handles compliance.

**Next step**

If you send me the actual strings (or the repo), I can find every instance and write the final copy for the confirmation dialogs.
