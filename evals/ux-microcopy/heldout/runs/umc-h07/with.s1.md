**Standardise on these terms**

| Concept | Use | Replace |
|---|---|---|
| The thing you book | **Appointment** | "Bookings", "Visits", "Session" |
| Starting access | **Sign in** | (already consistent) |
| Ending access | **Sign out** | "Log off", "Exit" |
| The person receiving care | **Member** | "patient" anywhere in the UI |
| The person giving care | **Practitioner** | "Your therapist" |

**Strings to fix**

- Page title "Bookings" → **"Appointments"**, to match the nav.
- Calendar tooltip "Visits" → **"Appointments"**, for example "3 appointments".
- Member email "Session" → **"Appointment"**, for example "Your appointment is confirmed".
- Menu item "Log off" → **"Sign out"**. It should pair with "Sign in".
- Settings button "Exit" → **"Sign out"** if it ends the session. If it only leaves the page, use **"Back"** or **"Close"**. "Exit" fails either way because it doesn't say what it exits.
- Member app "Your therapist" → **"Your practitioner"**. Staff and members see the same person under the same name.
- Anything reading "patient" in the UI → **"member"**, for example "Member record" and "Delete member". The brand decision covers the whole product, and your own descriptions of the strings still say "patient". Clinics that say "clients" can keep saying it in conversation. The interface stays on "Member".

**Removal verbs: keep them different, but make each one exact**

These are different actions with different consequences, so one verb for all four would mislead. The fix is to define each verb and always pair it with its object:

| Action | Button | Keep option |
|---|---|---|
| Cancel an appointment | **Cancel appointment** | Keep appointment |
| Delete a note | **Delete note** | Keep note |
| Delete a member record | **Delete member** | Keep member |
| Discard a draft | **Discard draft** | Keep editing |

- **Cancel** is for appointments only, because they can be cancelled and the member is notified.
- **Delete** means permanent, so use it only when that's true.
- **Discard** is only for unsaved drafts.
- **Remove** goes away, because it's vague. If removing a note is permanent, call it "Delete". If the note is only detached or archived, call it "Archive" or "Remove from [place]".
- A bare "Cancel" shouldn't be a dialog's dismiss button. It collides with "Cancel appointment", so use "Keep appointment".

**Notes**
- Check what "Delete" does on a member record. If clinical records must be retained, "Archive member" may be the accurate verb. I haven't assumed a policy.
- Pick one term list, put it in a short glossary, and search the codebase and email templates for the old words. Emails and tooltips are where drift usually hides.
