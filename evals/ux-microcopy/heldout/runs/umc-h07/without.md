Most of these are real inconsistencies, but the removal verbs mostly aren't.

## Fix these

| Concept | Today | Standardise on | Why |
|---|---|---|---|
| The thing you book | Appointments / Bookings / Visits / Session | **Appointment** | One noun in the nav, page title, tooltip and email. It's the standard word in clinic software. Retire "Bookings", "Visits" and "Session". |
| Ending access | Log off / Exit / Sign in | **Sign in / Sign out** | They're a pair, so "Sign in" settles it. "Exit" is also ambiguous because it sounds like closing a screen. |
| The clinician | Practitioner (staff) / Your therapist (member app) | **Practitioner** in both, "Your practitioner" in the member app | Staff and members are looking at the same person. "Therapist" also won't fit clinics that employ other roles. |

If "Session" in the email means the treatment itself rather than the booking, you could keep it. But then use it deliberately and consistently, not as a synonym for "appointment".

## Keep the removal verbs, mostly

These are different actions, so different verbs are correct. The goal is that each verb always means one thing:

- **Cancel** is for an appointment. The record stays, and its status changes.
- **Discard** is for a draft. It's unsaved work being thrown away.
- **Delete** is for permanent removal.
- **Remove** is for detaching something from a container. It's not destroying it.

Two things to change:
1. **Note: "Remove" vs "Delete".** If the note is permanently gone, call it **Delete**. Use "Remove" only if it's just detached.
2. **"Cancel" is overloaded.** It also usually means "close this dialog". Label the appointment action **Cancel appointment**. Make the dialog's dismiss button something like **Keep appointment** or **Close**.

One question on the patient record: you may have retention obligations for clinical records. If so, "Delete" may be the wrong action, and **Archive** might fit better. Check with whoever handles compliance.

## Members

I'll treat "Member" as settled. The practical step is to search every string, including emails, empty states, error messages and the "Delete" confirmation on the record, for "patient" and "client". Replace them with "Member" so the brand term appears everywhere. If the clinic-facing side is free to be configurable, "client" can be a per-clinic label later. That's optional and doesn't conflict with the founder's call.

Once you've settled these, put them in a short glossary (term, definition, banned synonyms) so new strings stay consistent. I can draft one, or search the codebase for the strings, if you point me at the repo.
