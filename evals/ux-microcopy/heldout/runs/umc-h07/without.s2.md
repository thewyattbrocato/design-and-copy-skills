Most of these should be fixed, but the removal words are partly legitimate. They describe different actions, so I wouldn't collapse them into one word.

## Fix and standardise

| Concept | Today | Use | Notes |
|---|---|---|---|
| Scheduled thing | Appointments / Bookings / Visits / Session | **Appointment** everywhere | Use "Book appointment" for the action. This covers the nav, page title, tooltip and email. |
| Ending your login | Log off / Exit / Sign in | **Sign in** / **Sign out** | "Log off" becomes "Sign out" so it pairs with the login screen. |
| Staff vs patient-app wording | Practitioners / Your therapist | **Practitioner** everywhere | In the member app, use "Your practitioner". "Therapist" is wrong for clinics that employ osteopaths or chiropractors, and one noun is easier to translate and support. |
| People receiving care | patient (record, email) / Member | **Member** everywhere | This follows the founder's decision. Your list still has "patient" in the delete wording, the email and "patient app". Search the UI strings, emails and error messages for "patient" and "client". |

Two points need checking:

- **"Exit" on the settings page:** I can't tell what it does. If it signs the user out, use "Sign out". If it leaves settings, use "Back" or "Close". Either way, "Exit" is vague.
- **"Session" in the email:** if you ever distinguish a clinical session from a booked slot, keep that distinction. If it's just the appointment, change it to "Appointment".

## Removal: keep distinct, but make the rules explicit

- **Cancel appointment:** keep this. The appointment still exists with a cancelled status. Always write "Cancel appointment" in full, never a bare "Cancel", because "Cancel" is also the usual label for dismissing a dialog. Label the dismiss button "Keep appointment" or "Go back" on that dialog.
- **Delete:** use this for permanent removal. "Remove" on a note should become "Delete" if it's permanent. Keep "Remove" only for detaching something that still exists elsewhere, for example removing a practitioner from a clinic.
- **Discard:** keep this for drafts, since it's the standard word for unsaved work.
- **Member records:** consider whether "Delete member" is really what happens. Clinics often have to retain health records, so "Archive member" may be more accurate than "Delete member". That's a product and legal question, not just wording.

## Next step

Write these decisions into a short glossary (term, definition, banned alternatives) and keep it where the team writes copy. Then grep the codebase for the old terms. I can do that if you point me at the repo. The working directory I'm in right now isn't a Kneeline project.
