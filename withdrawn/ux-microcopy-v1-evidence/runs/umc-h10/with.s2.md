**1. Welcome screen**
- Title: "Welcome to Dispatchly". *Heading on the first screen after sign-up.*
- Body: "Schedule your plumbing or electrical crew in three steps: add your crew, add a job, assign it." *Text under the heading.*
- Button: "Get started". *Primary button, opens onboarding step 1.*

**2. Onboarding steps**
- Step 1 title: "Add your crew". *Heading of step 1.*
- Step 1 body: "Add the people you send out on jobs. Your plan includes up to 25 crew members." *Text under the step 1 heading.*
- Step 1 button: "Add crew member". *Primary button on step 1.*
- Step 2 title: "Add a job". *Heading of step 2.*
- Step 2 body: "Every job needs an address, a date and a time window." *Text under the step 2 heading.*
- Step 2 button: "Add job". *Primary button on step 2.*
- Step 3 title: "Assign the job". *Heading of step 3.*
- Step 3 body: "Pick a crew member for the job. You can reassign it any time before you mark it complete." *Text under the step 3 heading.*
- Step 3 button: "Assign job". *Primary button on step 3.*
- Skip link: "Skip for now". *Secondary link on every onboarding step.*

**3. Jobs tab, empty state**
- Title: "No jobs yet". *Heading in the empty Jobs tab.*
- Body: "Jobs you add show up here. Each one needs an address, a date and a time window." *Text under the heading.*
- Button: "Add job". *Primary button in the empty state.*

**4. Crew tab, empty state**
- Title: "No crew members yet". *Heading in the empty Crew tab.*
- Body: "Add the people you want to assign jobs to. Your plan includes up to 25 crew members." *Text under the heading.*
- Button: "Add crew member". *Primary button in the empty state.*

**5. Toast: job assigned**
- "Job assigned to {name}." *Brief toast right after a successful assignment.*

**6. Toast: assigned to someone who already has a job then**
- "Job assigned to {name}, who already has a job at that time." *Toast after an assignment that overlaps another job for the same crew member.*
- Action: "Reassign". *Button on that toast, opens the crew picker for the job.*

**7. Error: can't reach the server**
- Title: "We couldn't reach the server". *Error banner or dialog when a request fails because of connection.*
- Body: "The job wasn't assigned. Assigning needs a connection, so try again once you're back online. Your job list still works offline and will sync later." *Text under the title when the failed action was an assignment.*
- Button: "Try again". *Retries the request.*

**8. Error: assigning to a removed crew member**
- Title: "{name} has been removed from your crew". *Error dialog when the chosen crew member no longer exists on the crew.*
- Body: "The job wasn't assigned. Choose another crew member." *Text under the title.*
- Button: "Choose crew member". *Reopens the crew picker.*

**9. Dialog: remove a crew member**
- Title: "Remove {name} from your crew?" *Confirmation dialog title, opened from the Crew tab.*
- Body: "{name} will no longer be on your crew. Their past jobs won't be deleted." *Text under the title.*
- Confirm button: "Remove {name}". *Destructive button.*
- Decline button: "Keep {name}". *Neutral button, same weight, closes the dialog.*

**10. Notification to the crew member's phone**
- Title: "New job assigned". *Push notification title.*
- Body: "{address}, {date}, {time window}". *Push notification body, opens the job.*

**11. Confirmation: job marked complete**
- "Job marked complete. Complete jobs can't be reassigned." *Toast right after the job is marked complete.*

Notes:
- `{name}`, `{address}`, `{date}` and `{time window}` are variables the developers fill in.
- Two things your facts didn't cover, so I left them out. String 6 assumes the job is still assigned despite the overlap. String 9 doesn't say what happens to a removed member's upcoming jobs. If either has a rule, tell me and I'll add it.
