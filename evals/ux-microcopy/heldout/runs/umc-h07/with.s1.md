**Term table**

| Concept | Today | Pick | Why |
|---|---|---|---|
| A scheduled slot with a patient | Appointments (nav), Bookings (page title), Visits (tooltip), Session (patient email) | **Appointment** everywhere | It's the word patients and clinics already use. The nav and page title must match the screen they open. |
| End your login | Log off, Exit, Sign in | **Sign in / Sign out** | These are true opposites. "Exit" doesn't say what it does, and it could mean leaving the page. |
| People who use the clinic | Practitioners (staff), Your therapist (patient app) | **Practitioner** on staff screens. "Your practitioner" in the patient app. | Use one noun. The possessive in the patient app is fine because it's personal. |
| The patient | Members | **Member**, as the founder decided | See the note below. |
| Remove | Cancel, Remove, Delete, Discard | Split by what happens (below) | These are different actions, so they shouldn't all share one word. |

**What to fix**

1. **Appointment / Bookings / Visits / Session.** This is the biggest problem. Four names for one thing will make people assume there are four things. Use "Appointment" in the nav, page title, tooltip and patient email. Don't keep "Session" for treatment sessions unless you really have a second concept. If you do, define it and use it only for that.
2. **Log off / Exit / Sign in.** Change "Log off" to **Sign out**. Change the settings "Exit" button to **Sign out** if that's what it does. If it only closes settings, call it **Close** or **Back to calendar**. Keep "Sign in" on the login screen.
3. **Therapist / Practitioner.** Change "Your therapist" to **Your practitioner**. Don't drop the possessive. It reads well in the patient app.
4. **Removing things.** Leave the four verbs distinct, because each means something different. Make sure each one matches what happens:

| Object | Verb | Rule |
|---|---|---|
| Appointment | **Cancel appointment** | The appointment stops happening. Pair it with a neutral decline, **Keep appointment**. Plain "Cancel" is ambiguous because it also means "close this dialog". |
| Note | **Delete note** | Use "Delete" for anything permanently removed. Change "Remove" to "Delete" unless the note is only detached and still exists elsewhere. |
| Patient record | **Delete record** | This is the most serious one. Name the member and the consequence, for example what happens to their appointment history. Say whether it can be undone. |
| Draft | **Discard draft** | "Discard" is fine here. It's the standard word for unsaved work and it's low stakes. |

The key decision is "Remove" versus "Delete". Pick one meaning for each and keep it. I'd use "Delete" for permanent and "Remove" only for taking something out of a list while it still exists. Appointments are the exception, because "Cancel" tells the patient and the clinic it won't happen.

**On "Members"**

I'm treating this as settled. Use **Member** consistently in the product. The only open question is how to handle clinics that say "clients". Keep the product word fixed, and don't mix "client" into some screens. If clinics push back, the cleanest fix is for the brand to appear in the product but for clinic-facing patient communications to be controlled by the clinic. That's a product decision for you and the founder, not something I'd decide here. Since "Members" is the brand, check that it reads naturally in clinical contexts, like "Member record", before you ship it.

**Next step**

If you share the real strings, including the confirmation dialogs for the four removal actions, I can rewrite them in full with the consequence text. The delete-record dialog needs the most care. I'd also check that the patient email says "Appointment" to match the app.
