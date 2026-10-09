# Dispatchly first-run copy

Placeholders are in {curly braces}. Keep them as variables.

## 1. Welcome screen

| ID | Text | Where it appears |
|---|---|---|
| welcome.title | Welcome to Dispatchly | Headline on the first screen after install |
| welcome.body | Schedule your plumbing or electrical crew and get the right job to the right person. | Subtext under the headline |
| welcome.cta | Get started | Primary button, starts onboarding |

## 2. Onboarding steps

| ID | Text | Where it appears |
|---|---|---|
| onboard.progress | Step {current} of 3 | Progress indicator on each onboarding step |
| onboard.skip | Skip | Secondary text button on each step |
| onboard.next | Next | Primary button on steps 1 and 2 |
| onboard.crew.title | Add your crew | Step 1 headline |
| onboard.crew.body | Add the people who do the work. You can have up to 25 crew members. | Step 1 body |
| onboard.job.title | Add a job | Step 2 headline |
| onboard.job.body | Every job needs an address, a date and a time window. | Step 2 body |
| onboard.assign.title | Assign a job | Step 3 headline |
| onboard.assign.body | Pick a crew member for the job. They'll get a notification on their phone. You can reassign the job any time before it's marked complete. | Step 3 body |
| onboard.done | Done | Primary button on step 3, ends onboarding |

## 3. Jobs tab, empty state

| ID | Text | Where it appears |
|---|---|---|
| jobs.empty.title | No jobs yet | Heading when the Jobs list is empty |
| jobs.empty.body | Add a job with an address, a date and a time window. | Body under the heading |
| jobs.empty.cta | Add a job | Button in the empty state |

## 4. Crew tab, empty state

| ID | Text | Where it appears |
|---|---|---|
| crew.empty.title | No crew members yet | Heading when the Crew list is empty |
| crew.empty.body | Add the people you'll assign jobs to. You can add up to 25. | Body under the heading |
| crew.empty.cta | Add a crew member | Button in the empty state |

## 5. Toast: job assigned

| ID | Text | Where it appears |
|---|---|---|
| toast.assigned | Job assigned to {name}. | Toast right after a successful assignment |

## 6. Toast: assigned to someone with a job at that time

| ID | Text | Where it appears |
|---|---|---|
| toast.assigned.overlap | Job assigned to {name}. They already have a job at this time. | Toast after an assignment that overlaps one of that person's existing jobs |

## 7. Error: can't reach the server

| ID | Text | Where it appears |
|---|---|---|
| error.offline.title | Can't reach the server | Error title when an action needs the server and the connection fails |
| error.offline.body | Check your connection and try again. Your job list is still available offline, but assigning a job needs a connection. | Error body |
| error.offline.retry | Try again | Button on the error |

## 8. Error: assigning to a removed crew member

| ID | Text | Where it appears |
|---|---|---|
| error.removed.title | Can't assign this job | Error title when the chosen crew member has been removed |
| error.removed.body | {name} has been removed from your crew. Choose someone else for this job. | Error body |
| error.removed.cta | Choose another crew member | Button that returns to the crew picker |

## 9. Dialog: remove a crew member

| ID | Text | Where it appears |
|---|---|---|
| dialog.remove.title | Remove {name}? | Confirmation dialog title, opened from the Crew tab |
| dialog.remove.body | {name} will be removed from your crew. Their past jobs won't be deleted. | Dialog body |
| dialog.remove.confirm | Remove | Destructive button |
| dialog.remove.cancel | Cancel | Cancel button |

## 10. Notification: job assigned to a crew member

| ID | Text | Where it appears |
|---|---|---|
| push.assigned.title | New job assigned to you | Title of the phone notification sent to the assigned crew member |
| push.assigned.body | {address} · {date}, {time_window} | Body of the same notification |

## 11. Confirmation: job marked complete

| ID | Text | Where it appears |
|---|---|---|
| toast.complete | Job marked complete. | Toast or inline confirmation after someone marks a job complete |

## Open questions for the developers and you

- **String 6:** I wrote it as "assigned, with a heads-up", because you described it as a toast. If the assignment is blocked or needs a confirm, the copy has to change.
- **String 9:** Your facts don't say what happens to a removed person's upcoming or open jobs, so the dialog says nothing about them. If those jobs become unassigned, the dialog should say so.
- **String 11:** Your facts imply a completed job can't be reassigned. I left that out of the copy because you didn't state it outright.
- **String 7:** It says "Your job list is still available offline." That's based on your offline fact. It doesn't promise that edits to jobs sync, because you only said the job list syncs.
- **String 10:** Date and time-window formatting (for example "Tue, Oct 13, 8–10 AM") should follow the device locale.
- **The 25-member limit:** It appears in strings 2 and 4 only. If a crew ever hits the limit, the app will need a separate message, which I haven't written.
