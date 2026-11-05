Most of this is worth fixing, but not all of it. "Members" stays as is.

## Term table

| What it is | Today | Pick | Why |
|---|---|---|---|
| A scheduled slot with a Member | Appointments, Bookings, Visits, Session | **Appointment** | It's the word clinics and Members already use. "Booking" is the act of making one. "Session" and "Visit" suggest different things, so people will assume there are different objects. |
| Ending your login | Log off, Exit, Sign in | **Sign in / Sign out** | They're true opposites. "Exit" doesn't say what it ends. |
| Removing an appointment | Cancel | **Cancel appointment** | The appointment stays on record as cancelled, so this is a different action from deleting. |
| Removing a note | Remove | **Delete note** | "Remove" is vague about whether the note is gone for good. |
| Removing a record | Delete | **Delete record** | Keep it, and name the object. |
| Removing unsaved work | Discard | **Discard draft** | Keep it. Nothing was saved, so this word is accurate. |
| The clinician | Practitioner (staff), Your therapist (patient app) | **Practitioner** in both | The audiences differ, but it's the same person. Check it's consistent wherever staff preview or send Member-facing text. |
| The person being treated | Patient / Members | **Member**, everywhere | See the second note below. |

## Strings

**Navigation and titles**
- Main nav: `Appointments`
- Page title: `Appointments`
- Calendar tooltip: `Appointment` followed by the details, for example `Appointment · [Member name] · [time]`
- Email: replace "session" with "appointment" everywhere it appears.

**Signing out**
- Menu item: `Sign out` (replaces "Log off")
- Settings button: `Sign out` (replaces "Exit"). If that button only leaves the settings page, call it `Back to calendar` instead. Please check which it is.

**Removing things**
Each action keeps its own verb. The decline button names what you'd be keeping, so it doesn't clash with "Cancel".

| Where | Heading | Buttons |
|---|---|---|
| Appointment | `Cancel this appointment?` Body: `[Member name]'s appointment on [date, time] will be marked as cancelled. [Say whether the Member is notified.]` | `Cancel appointment` / `Keep appointment` |
| Note | `Delete this note?` Body: `It will be deleted from [Member name]'s record. [Say whether this can be undone.]` | `Delete note` / `Keep note` |
| Member record | `Delete [Member name]'s record?` Body: `[Say what is deleted, who is affected, and whether it can be undone.]` | `Delete record` / `Keep record` |
| Draft | `Discard this draft?` Body: `Unsaved changes will be lost.` | `Discard draft` / `Keep editing` |

- **Placeholders:** I've left brackets where I don't know your behaviour (notifications, undo, retention). Fill those in with the real consequences. Deleting a Member's record deserves the most careful wording, since it's the most serious action.
- **"Members":** I'd treat the founder's decision as covering every string, not only the Member-facing app. That includes "patient record", "patient app" and "patient email", which are the phrases you used in your message. Staff at clinics that say "clients" will see "Member" in the interface, so make sure your help pages and support replies use it too.
