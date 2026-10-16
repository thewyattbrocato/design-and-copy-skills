## Term table

| Concept | Today | Pick | Why |
|---|---|---|---|
| The scheduled thing | Appointments / Bookings / Visits / Session | **Appointment**, everywhere | It's already the nav label. Four names look like four different things. |
| Starting | Sign in | **Sign in** | Keep. |
| Ending | Log off / Exit | **Sign out** | It's the true opposite of "Sign in". "Log off" and "Exit" break the pair. |
| Undo a future appointment | Cancel | **Cancel appointment** | Name the object. A bare "Cancel" also means "close this dialog". |
| Remove a note | Remove | **Delete note** | "Remove" is unclear about whether the note is gone for good. |
| Remove a patient record | Delete | **Delete member** | See the Members decision below. |
| Throw away unsaved work | Discard | **Discard draft** | Keep. It's a different act from deleting something saved. |
| Staff | Practitioner / Your therapist | **Practitioner**, in both apps | Staff already see it, and it covers every discipline a clinic might have. |
| Patients | Patient / Members | **Member**, in both apps | The founder's decision. |

The removal verbs can stay different, because the acts are different: cancelling something scheduled, deleting something saved, discarding something unsaved. Each verb should mean one thing every time it appears.

## Rewritten strings

| Where | Now | Change to |
|---|---|---|
| Main nav | Appointments | Appointments (no change) |
| Page title | Bookings | Appointments |
| Calendar tooltip | Visits | Appointment (for example "Appointment · 10:30, [practitioner]") |
| Patient email | "Session" | "Your appointment" |
| Sign-out menu item | Log off | Sign out |
| Settings page button | Exit | See note 1 |
| Login screen | Sign in | Sign in (no change) |
| Appointment action | Cancel | Cancel appointment, with the decline **Keep appointment** |
| Note action | Remove | Delete note, with the decline **Keep note** |
| Member record action | Delete | Delete member, with the decline **Keep member** |
| Draft action | Discard | Discard draft, with the decline **Keep editing** |
| Patient app | Your therapist | Your practitioner |

Each confirmation should name the object and say what happens, and the decline should be neutral and equal in weight. For example: "Delete this note? It will be removed from [member name]'s record. [can/can't be undone]". Fill in the undo part from how the app actually behaves.

## Notes

1. **"Exit" on settings:** I don't know what it does, so I can't pick a word. If it signs the person out, use "Sign out". If it only leaves the page, use "Back to [previous screen]" or "Close settings". Don't keep "Exit".
2. **Members and "clients":** I've taken the founder's decision as final. If clinics keep asking for "clients", treat that as a separate product question. It isn't a naming inconsistency. Use "member" on the staff side too, so staff and patient screens match.
