# Dispatchly first-run copy

Placeholders are in `{braces}`. Each string has a one-line note on where it appears.

## 1. Welcome screen

| Text | Where it appears |
|---|---|
| **Welcome to Dispatchly** | Headline on the first screen after install. |
| Scheduling for plumbing and electrical crews. Add your crew, add jobs, and assign them in a few taps. | Subhead under the headline. |
| **Get started** | Primary button. It starts onboarding step 1. |

## 2. Onboarding steps

**Step 1: Add your crew**

| Text | Where it appears |
|---|---|
| Step 1 of 3 | Progress label at the top of the screen. |
| **Add your crew** | Step headline. |
| Add the people you schedule. Your plan includes up to 25 crew members. | Step body text. |
| **Add crew member** | Primary button. It opens the add-crew form. |
| **Next** | Secondary button. It advances to step 2. |

**Step 2: Add a job**

| Text | Where it appears |
|---|---|
| Step 2 of 3 | Progress label. |
| **Add a job** | Step headline. |
| Every job needs an address, a date, and a time window. | Step body text. |
| **Add job** | Primary button. It opens the add-job form. |
| **Next** | Secondary button. It advances to step 3. |

**Step 3: Assign a job**

| Text | Where it appears |
|---|---|
| Step 3 of 3 | Progress label. |
| **Assign a job** | Step headline. |
| Pick a job, then choose who's doing it. Their phone gets a notification. You can reassign it any time before it's marked complete. | Step body text. |
| **Done** | Primary button. It ends onboarding and opens the app. |

## 3. Jobs tab empty state

| Text | Where it appears |
|---|---|
| **No jobs yet** | Empty-state headline on the Jobs tab. |
| Add your first job with an address, a date, and a time window. | Empty-state body text. |
| **Add job** | Button under the body text. |

## 4. Crew tab empty state

| Text | Where it appears |
|---|---|
| **No crew members yet** | Empty-state headline on the Crew tab. |
| Add the people on your crew so you can assign jobs to them. You can add up to 25. | Empty-state body text. |
| **Add crew member** | Button under the body text. |

## 5. Toast: job assigned

| Text | Where it appears |
|---|---|
| Job assigned to {name}. | Toast shown after a successful assignment. |

## 6. Toast: assigned to someone with a job at that time

| Text | Where it appears |
|---|---|
| Assigned to {name}. They already have a job at this time. | Toast shown after assignment when the person has an overlapping job. |

## 7. Error: can't reach the server

| Text | Where it appears |
|---|---|
| **Can't reach the server** | Error title. It appears when an assign attempt fails for lack of a connection. |
| Assigning a job needs a connection. Check your internet and try again. Your job list is still available offline and will sync when you're back online. | Error body text. |
| **Try again** | Primary button. It retries the assignment. |
| **Cancel** | Secondary button. It dismisses the error. |

## 8. Error: assigning to a removed crew member

| Text | Where it appears |
|---|---|
| **Can't assign this job** | Error title. |
| {name} has been removed from your crew. Choose someone else to assign this job to. | Error body text. |
| **Choose someone else** | Primary button. It reopens the crew picker. |

## 9. Dialog: remove a crew member

| Text | Where it appears |
|---|---|
| **Remove {name}?** | Dialog title. It opens from the crew member's profile or menu. |
| {name} will be removed from your crew. Their past jobs won't be deleted. | Dialog body text. |
| **Remove** | Confirm button. It should use the destructive style. |
| **Cancel** | Cancel button. |

## 10. Notification to the crew member

| Text | Where it appears |
|---|---|
| **New job assigned** | Push notification title on the crew member's phone. |
| {address} · {date}, {time window} | Push notification body on the crew member's phone. |

## 11. Confirmation: job marked complete

| Text | Where it appears |
|---|---|
| Job marked complete. | Toast shown after the user marks a job complete. |

## Questions for you or the developers

I only used the facts you gave me, so these gaps affect the copy:

- **String 6:** I assumed the assignment still goes through when there's a time overlap, so it's a toast and not a block. If it should ask for confirmation first, I'll write a dialog instead.
- **String 9:** I said nothing about the person's upcoming or open jobs, or whether they can be re-added later. If you give me those rules, I'll add a line.
- **String 11:** I left out any mention of undo, and of the fact that completed jobs can't be reassigned. You only told me reassignment is allowed before completion, and I didn't want to imply more.
- **String 7:** The offline line says the job list syncs "when you're back online". I didn't promise how fast it syncs.
- **Plan limit:** The "up to 25" line is in strings 2 and 4. If you ever sell another plan, those two strings will need to be dynamic.
