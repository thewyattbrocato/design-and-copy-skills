## Dispatchly First-Run Copy

**Welcome Screen**
- Heading: "Schedule your crew"
- Subheading: "Dispatch jobs, track who's working when, stay in sync on the go"
- Button: "Set up your crew"

**Onboarding: Add Your Crew**
- Heading: "Add your crew"
- Description: "Enter names of the people you'll assign jobs to. You can add up to 25 team members."
- Input label: "Name"
- "Add another" button: "Add another member"
- Next step button: "Next"

**Onboarding: Add a Job**
- Heading: "Add a job"
- Description: "You'll assign this to a team member in the next step."
- Address field label: "Job address"
- Date field label: "Date"
- Time field label: "Time window" 
- Button: "Next"

**Onboarding: Assign a Job**
- Heading: "Assign this job"
- Description: "Pick who will handle this one."
- Dropdown label: "Crew member"
- Button: "Finish"

**Jobs Tab Empty State**
- Heading: "No jobs yet"
- Description: "Add a job to get started."
- Button: "Add a job"

**Crew Tab Empty State**
- Heading: "No crew yet"
- Description: "Add team members so you can assign them jobs."
- Button: "Add a member"

**Toast: Job Assigned**
- "[Address] assigned to [crew member name]" — appears briefly after assigning a job

**Toast: Crew Member Already Has a Job**
- "[Name] already has a job then. Reassign their other job, or pick another team member." — appears if user tries to assign a job during an existing time window

**Error: Can't Reach Server**
- "We couldn't reach the server. Your jobs are saved on this phone. You can view them, but you won't be able to assign new ones until you're back online." — appears when attempting an action that requires a connection

**Error: Can't Assign to Removed Crew Member**
- "[Name] has been removed from your crew. Pick another team member." — appears if a crew member was deleted after jobs were created for them

**Remove Crew Member Dialog**
- Heading: "Remove [name]?"
- Body: "Their past jobs will stay in your system."
- Button 1: "Remove [name]"
- Button 2: "Keep [name]"

**Notification Sent to Crew Member's Phone**
- "[Address], [date] at [time window]" — appears on crew member's phone after you assign them a job

**Confirmation After Job Marked Complete**
- "[Address] marked complete" — appears briefly after clicking the completion button

---

One note: for the phone notification, you'll need to decide whether the crew member needs to open the app to see more detail, or if the notification should prompt an action (like "View" or "Confirm"). This assumes notification-as-informational; if you want them to confirm receipt, the copy stays the same but the interaction changes.
