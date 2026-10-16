**1. Welcome screen**
- Heading: `Welcome to Dispatchly` (top of the welcome screen)
- Body: `Schedule jobs and assign them to your crew, all in one place.` (under the heading)
- Button: `Get started` (starts onboarding)

**2. Onboarding**
- Step 1 title: `Add your crew` (onboarding step 1 heading)
- Step 1 body: `Add the people you send out on jobs. Your plan includes up to 25 crew members.` (under the step 1 heading)
- Step 1 button: `Add crew member` (step 1 primary action)
- Step 2 title: `Add a job` (onboarding step 2 heading)
- Step 2 body: `Enter the address, the date and a time window.` (under the step 2 heading)
- Step 2 button: `Add job` (step 2 primary action)
- Step 3 title: `Assign the job` (onboarding step 3 heading)
- Step 3 body: `Pick a crew member for the job. They'll get a notification on their phone. You can reassign the job any time before you mark it complete.` (under the step 3 heading)
- Step 3 button: `Assign job` (step 3 primary action)
- Skip link: `Skip for now` (on every onboarding step, secondary)

**3. Jobs tab, empty state**
- Heading: `No jobs yet` (center of the empty Jobs tab)
- Body: `Jobs you add show up here. Each one needs an address, a date and a time window.` (under the heading)
- Button: `Add job` (primary action in the empty state)

**4. Crew tab, empty state**
- Heading: `No crew members yet` (center of the empty Crew tab)
- Body: `Add the people you want to assign jobs to. Your plan includes up to 25.` (under the heading)
- Button: `Add crew member` (primary action in the empty state)

**5. Toast: job assigned**
- `Job assigned to {Name}.` (bottom toast after a successful assignment)

**6. Toast: assigned to someone with a job at that time**
- `Job assigned to {Name}, who already has a job at that time.` (toast after assignment when the time windows overlap)

**7. Error: can't reach the server**
- Title: `We couldn't reach the server` (banner or dialog when a request fails)
- Body: `You can still use your job list. Changes will sync later. Assigning jobs needs a connection, so try again once you're back online.` (under the title)
- Button: `Try again` (retries the request)

**8. Error: assigning to a removed crew member**
- Title: `{Name} is no longer on your crew` (dialog when the chosen person has been removed)
- Body: `The job wasn't assigned. Choose another crew member.` (under the title)
- Button: `Choose crew member` (reopens the assign picker)

**9. Dialog: remove a crew member**
- Title: `Remove {Name} from your crew?` (confirmation after tapping Remove on a crew member)
- Body: `{Name} will no longer be available for new assignments. Their past jobs are not deleted.` (under the title)
- Confirm button: `Remove {Name}` (destructive action)
- Decline button: `Keep {Name}` (closes the dialog, same visual weight as the confirm button)

**10. Notification to the crew member**
- Title: `New job assigned to you` (push notification on the crew member's phone)
- Body: `{Address} · {Date}, {Time window}` (push notification body, so the details show without opening the app)

**11. Confirmation: job marked complete**
- `Job marked complete.` (toast after the user marks a job complete)

Two notes for the developers:
- **Overlap toast (6):** I wrote it as "assigned, with a heads-up". Your brief reads that way, but please confirm the assignment goes through. If it doesn't, the string needs to change.
- **Facts left out on purpose:** you didn't say whether a removed crew member can be re-added or what happens to their upcoming jobs. The removal dialog (9) says nothing about either. Add a line once you know. The same goes for whether reassigning sends a new notification.
