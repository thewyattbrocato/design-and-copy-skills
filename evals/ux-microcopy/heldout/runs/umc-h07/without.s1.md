Most of these are real inconsistencies. The removal verbs are the exception: they're mostly fine.

| Area | Today | Standardise on | Notes |
|---|---|---|---|
| The thing being scheduled | Appointments / Bookings / Visits / Session | **Appointment** | Use it in the nav, page title, tooltip and email. Keep "book" only as the verb, as in "Book appointment". "Session" is the riskiest one because it can mean a treatment session or the booking itself. |
| Ending access | Log off / Exit / Sign in | **Sign in / Sign out** | Use these as a pair. Change "Log off" to "Sign out". Check what "Exit" does on the settings page. If it signs the user out, rename it. If it leaves settings, call it "Back" or "Done". |
| Removing things | Cancel / Remove / Delete / Discard | Mostly **keep**, with the fixes below | The verbs describe different outcomes, so don't merge them. |
| Staff vs. patient-app wording | Practitioners / Your therapist | **Practitioner** | In the member app, use "Your practitioner". Two words for one role will confuse people when a clinic's staff and members talk to each other. |
| Patients | Members | **Member** | Settled, so no action on "clients". It's a clinic's own speech, not our interface. |

**Removal verbs**
- **Cancel** is right for an appointment because it changes the appointment's status and probably notifies the member. Label the button "Cancel appointment". On the confirmation dialog, use "Keep appointment" to dismiss it. That way "Cancel" doesn't also mean "close this dialog".
- **Discard** for drafts is fine. It means throwing away unsaved work.
- **Remove** and **Delete** need one rule. Use "Delete" when the item is permanently gone. Use "Remove" when it's detached but still exists elsewhere. Decide which one a note is, then label it to match. A member record is health data, so label it "Delete member record" and ask for confirmation.

**Wording to check**
- You wrote "patient email" and "patient record" and "patient app". If those words appear in the interface, change them to "Member". If you only used them to describe the screens to me, there's nothing to fix.
- Once you've settled the terms, write them down in a short glossary, one line per term with what to avoid. A glossary stops the drift from coming back.

If you can point me at the code or the strings file, I can list every place these terms appear and prepare the changes.
