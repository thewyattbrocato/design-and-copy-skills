**1. Welcome screen**
- Title: Welcome to Dispatchly. *Heading.*
- Body: Schedule jobs and assign them to your plumbing or electrical crew. *Under the heading.*
- Button: Get started. *Primary button; opens onboarding step 1.*

**2. Onboarding steps**
- Step 1 title: Add your crew. *Step 1 heading.*
- Step 1 body: Add the people you assign jobs to. Your plan includes up to 25 crew members. *Step 1 body.*
- Step 1 button: Add crew member. *Primary button on step 1.*
- Step 2 title: Add a job. *Step 2 heading.*
- Step 2 body: Every job needs an address, a date and a time window. *Step 2 body.*
- Step 2 button: Add job. *Primary button on step 2.*
- Step 3 title: Assign the job. *Step 3 heading.*
- Step 3 body: Choose a crew member for the job. You can reassign it any time before it's marked complete. *Step 3 body.*
- Step 3 button: Assign job. *Primary button on step 3.*
- Skip link: Skip for now. *Secondary link on every step.*

**3. Jobs tab, empty state**
- Title: No jobs yet. *Empty-state heading.*
- Body: Add a job with an address, a date and a time window. Then assign it to a crew member. *Empty-state body.*
- Button: Add job. *Empty-state button.*

**4. Crew tab, empty state**
- Title: No crew members yet. *Empty-state heading.*
- Body: Add the people you assign jobs to. You can have up to 25 crew members. *Empty-state body.*
- Button: Add crew member. *Empty-state button.*

**5. Toast: job assigned**
- Job assigned to [Name]. *Toast after a successful assignment.*

**6. Toast: assigned to someone with a job at that time**
- Job assigned to [Name]. They already have a job at this time. *Toast after an assignment that overlaps another of their jobs.*

**7. Error: can't reach the server**
- Title: We couldn't reach the server. *Error banner or dialog title.*
- Body: The job wasn't assigned. Assigning needs a connection, so check yours and try again. *Error body when an assignment fails for connectivity.*
- Button: Try again. *Retry button.*
- Offline banner, for the job list: You're offline. You can still use the job list, and it will sync when you're back online. *Persistent banner on the Jobs tab while offline.*

**8. Error: crew member was removed**
- Title: [Name] is no longer on your crew. *Error dialog title.*
- Body: This job wasn't assigned. Choose another crew member. *Error dialog body.*
- Button: Choose crew member. *Primary button; returns to the crew picker.*

**9. Dialog: remove a crew member**
- Title: Remove [Name] from your crew? *Dialog title.*
- Body: [Name] will no longer be on your crew. Their past jobs stay in Dispatchly. *Dialog body.*
- Buttons: Remove [Name] / Keep [Name]. *Confirm and decline buttons, equal weight.*

**10. Notification to the crew member's phone**
- Title: New job: [address] *Push notification title, so the address survives truncation.*
- Body: [Date], [time window]. Tap to see the details. *Push notification body.*

**11. Confirmation: job marked complete**
- Job marked complete. *Toast after the user marks a job complete.*

**Notes**
- **Open question on string 9:** you didn't say what happens to a removed person's open (not yet complete) jobs. Add that sentence to the body once the developers confirm it. I left it out rather than guess.
- **Assumptions to confirm:**
  - String 6 assumes the assignment goes through and the overlap is only a warning.
  - String 10 assumes tapping the notification opens the job.
  - String 11 deliberately doesn't say the job can no longer be reassigned. Your facts imply it, but add it only if that's confirmed.
