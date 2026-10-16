I'll organize this by screen/state with placement notes for the developers to implement.

---

**WELCOME SCREEN**
- Headline: "Dispatch jobs to your crew, in real time"
  *(main heading on the welcome screen)*
- Subheading: "Manage your small team's schedule all in one place"
  *(supporting text below headline)*
- Primary button: "Get started"
  *(call-to-action button)*

**ONBOARDING STEP 1: Add Your Crew**
- Step indicator: "Step 1 of 3"
  *(progress indicator at top)*
- Heading: "Add your crew"
  *(screen title)*
- Description: "Add up to 25 team members to your crew"
  *(explanatory text)*
- Input label: "Crew member name"
  *(form field label)*
- Helper text: "We'll send them notifications when jobs are assigned"
  *(clarification below input)*
- Add button: "+ Add another"
  *(button to add multiple members)*
- Primary button: "Next"
  *(advance to next step)*

**ONBOARDING STEP 2: Add a Job**
- Step indicator: "Step 2 of 3"
- Heading: "Add a job"
- Description: "Fill in the job details so you can assign it to your crew"
- Address field label: "Address"
- Date field label: "Date"
- Time field label: "Time window (start and end)"
- Example text: "e.g., 9:00 AM – 11:00 AM"
  *(shown below time field)*
- Primary button: "Next"

**ONBOARDING STEP 3: Assign a Job**
- Step indicator: "Step 3 of 3"
- Heading: "Assign this job"
- Description: "Pick a crew member to send the job to"
- Dropdown label: "Assign to"
- Primary button: "Done"
  *(completes onboarding)*

**EMPTY STATE: Jobs Tab**
- Illustration placeholder: *(icon or image area)*
- Heading: "No jobs yet"
- Subheading: "Create your first job to get started"
- Primary button: "+ New job"

**EMPTY STATE: Crew Tab**
- Illustration placeholder:
- Heading: "No crew members yet"
- Subheading: "Add your first team member to assign jobs"
- Primary button: "+ Add crew member"

**TOAST: Job Assigned (Success)**
- Message: "[Crew member name] is assigned to the job at [address]"
  *(appears briefly at bottom of screen after assignment)*

**TOAST: Job Assigned to Unavailable Member (Conflict)**
- Message: "[Crew member name] already has a job at that time"
  *(appears when user attempts to assign overlapping job)*
- Action button: "Assign anyway"
  *(allows override if desired)*

**ERROR: Server Unreachable**
- Heading: "Can't connect to the server"
  *(error dialog or alert)*
- Message: "The app works offline, but you can only view your jobs. Try again when you have a connection to assign new ones."
  *(explains limitation and next step)*
- Button: "Got it"
- *(dismiss button)*

**ERROR: Crew Member Removed**
- Heading: "Can't assign this job"
- Message: "This crew member was removed from your team. Pick someone else to assign it to."
  *(error when assigning to a removed member)*
- Button: "OK"

**DIALOG: Remove Crew Member**
- Heading: "Remove [crew member name]?"
  *(confirmation dialog title)*
- Message: "Their past jobs will stay on the schedule. They won't receive new assignments."
  *(explains outcome)*
- Cancel button: "Cancel"
- Destructive button: "Remove"

**NOTIFICATION: Job Assigned (Push to Crew Member's Phone)**
- Title: "[Your manager name] assigned you a job"
  *(notification heading)*
- Body: "[Address] on [date] at [time]"
  *(job details in notification body)*

**CONFIRMATION: Job Marked Complete**
- Heading: "Job completed"
  *(confirmation dialog title)*
- Message: "Marked complete on [date] at [time]"
  *(shows when it was marked)*
- Button: "Done"
  *(dismiss)*

---

All copy avoids over-committing to features outside the scope you described, stays action-focused, and acknowledges key constraints (the 25-member limit, offline limitations, the permanence of past job history).
