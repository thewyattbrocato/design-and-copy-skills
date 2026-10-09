# Dispatchly first-run copy

Placeholders in `{braces}` are filled in by the app.

## 1. Welcome screen

| String | Where it appears |
|---|---|
| **Welcome to Dispatchly** | Headline on the first screen after install. |
| Scheduling for small plumbing and electrical crews. | Subhead under the headline. |
| **Get started** | Primary button, starts onboarding. |

## 2. Onboarding steps

| String | Where it appears |
|---|---|
| Step 1 of 3 | Progress label on the first step. |
| **Add your crew** | Step 1 title. |
| Add the people who'll be doing the jobs. You can have up to 25 crew members. | Step 1 body. |
| **Add crew** | Step 1 button. |
| Step 2 of 3 | Progress label on the second step. |
| **Add a job** | Step 2 title. |
| Every job needs an address, a date and a time window. | Step 2 body. |
| **Add a job** | Step 2 button. |
| Step 3 of 3 | Progress label on the third step. |
| **Assign a job** | Step 3 title. |
| Pick a crew member for the job. You can reassign it any time before it's marked complete. | Step 3 body. |
| **Assign job** | Step 3 button. |
| Skip | Text link on every step; leaves onboarding. |
| Next | Secondary button on steps 1 and 2 if the user has already done the action. |

## 3. Jobs tab empty state

| String | Where it appears |
|---|---|
| **No jobs yet** | Title, shown when the Jobs tab has no jobs. |
| Add your first job with an address, a date and a time window. | Body text under the title. |
| **Add a job** | Button below the body. |

## 4. Crew tab empty state

| String | Where it appears |
|---|---|
| **No crew members yet** | Title, shown when the Crew tab has no members. |
| Add the people you'll assign jobs to. Your plan includes up to 25. | Body text under the title. |
| **Add crew member** | Button below the body. |

## 5. Toast: job assigned

| String | Where it appears |
|---|---|
| Job assigned to {crew_name}. | Brief toast right after a successful assignment. |

## 6. Toast: assigned to someone who already has a job at that time

| String | Where it appears |
|---|---|
| Job assigned to {crew_name}, who already has a job at that time. | Toast after an assignment that overlaps one of their existing jobs. Shown instead of #5, not with it. |

## 7. Error: can't reach the server

| String | Where it appears |
|---|---|
| **Can't reach the server** | Error title, shown when a request fails because of connectivity. |
| Check your connection and try again. You can still view your job list offline, but assigning a job needs a connection. | Error body. |
| **Try again** | Primary button; retries the request. |

## 8. Error: assigning to a removed crew member

| String | Where it appears |
|---|---|
| **Can't assign this job** | Error title. |
| {crew_name} has been removed from your crew. Choose someone else to assign this job to. | Error body, shown when the assignment targets a removed member. |
| **Choose someone else** | Primary button; reopens the crew picker. |

## 9. Dialog: remove a crew member

| String | Where it appears |
|---|---|
| **Remove {crew_name}?** | Dialog title, after tapping Remove on a crew member. |
| They'll be removed from your crew. Their past jobs won't be deleted. | Dialog body. |
| **Remove** | Destructive confirm button. |
| Cancel | Dismiss button. |

## 10. Notification: job assigned to a crew member

| String | Where it appears |
|---|---|
| **New job assigned** | Notification title, sent to the crew member's phone. |
| {address} · {date}, {time_window} | Notification body. |

## 11. Confirmation: job marked complete

| String | Where it appears |
|---|---|
| Job marked complete. | Confirmation shown right after the user marks a job complete. |

## Notes for the developers

- **Placeholders:** `{crew_name}`, `{address}`, `{date}`, `{time_window}`. The date and time formats should follow the device's locale.
- **Assumption in #6:** I wrote it as the assignment still going through, with a heads-up about the overlap. If the app blocks the assignment or asks for confirmation first, this string needs to change.
- **Not covered, because I didn't have the facts:** what happens to a removed member's open or upcoming jobs, whether a removed member can be re-added, and what happens at the 25-member limit. I kept all of these out of the copy. They will probably need strings later, especially the removal dialog and the limit.
