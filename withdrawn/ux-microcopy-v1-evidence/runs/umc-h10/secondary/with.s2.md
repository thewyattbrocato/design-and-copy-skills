## 1. Welcome Screen
- **Heading**: "Keep your crew on schedule" — main headline
- **Subheading**: "Assign jobs to your team in one place." — description text
- **Button**: "Get started" — primary CTA to begin onboarding

## 2. Onboarding Step 1: Add Your Crew
- **Heading**: "Add your crew" — screen title
- **Description**: "List your team members so you can assign jobs to them. You can add up to 25 people." — explanation including max members
- **Button**: "Add crew member" — action to add first person
- **Toast**: "[Name] added" — confirmation after each add

## 3. Onboarding Step 2: Add a Job
- **Heading**: "Create a job" — screen title
- **Description**: "Every job needs an address, date, and time window." — what's required
- **Address field label**: "Address" — form field
- **Date field label**: "Date" — form field
- **Time field label**: "Time window" — form field (e.g. "9 AM–12 PM")
- **Button**: "Save job" — action button

## 4. Onboarding Step 3: Assign a Job
- **Heading**: "Assign this job" — screen title
- **Description**: "Choose who will handle it." — instruction text
- **Button**: "Assign to [name]" — action when crew member selected
- **Toast**: "[Job] assigned to [name]" — confirmation message

## 5. Empty State: Jobs Tab
- **Heading**: "No jobs yet" — title when list is empty
- **Description**: "Create a job and assign it to someone on your crew." — explanation of what to do
- **Button**: "Create a job" — primary action

## 6. Empty State: Crew Tab
- **Heading**: "No crew members yet" — title when list is empty
- **Description**: "Add your team so you can assign jobs to them." — explanation of what to do
- **Button**: "Add crew member" — primary action

## 7. Toast: Job Assigned Successfully
- **Text**: "[Job] assigned to [name]" — confirmation when assignment succeeds

## 8. Toast: Job Assigned with Time Conflict
- **Text**: "[Name] already has a job at that time—still assigned [Job]." — alerts to the overlap while confirming the action succeeded

## 9. Error: Can't Reach Server
- **Heading**: "Can't reach the server" — error title
- **Description**: "You can still view jobs and your crew offline. You'll need to be online to assign jobs." — explains what works and what doesn't
- **Button**: "Try again" — retry action

## 10. Error: Crew Member Was Removed
- **Heading**: "[Name] is no longer on your crew" — describes what went wrong
- **Description**: "They were removed before you could assign this job. Choose someone else." — explains why and what to do
- **Button**: "Choose another person" — next action

## 11. Dialog: Confirm Remove Crew Member
- **Heading**: "Remove [name]?" — names who will be removed
- **Description**: "They'll be off your crew, but their past jobs will stay on your records." — clarifies the consequence
- **Decline button**: "Keep them" — neutral equal-weight option
- **Confirm button**: "Remove" — what will happen

## 12. Notification: Job Assigned to Crew Member
- **Text**: "[Your company/you] assigned you [Job] on [date] at [time]." — sent to crew member's phone; lead with the fact

## 13. Confirmation: Job Marked Complete
- **Heading**: "Done" — simple success indicator
- **Description**: "[Job] is marked complete." — confirms the action
- **Button**: "Back to jobs" — next action

---

**Note on fact consistency**: Strings about offline/online sync (error #9) match your stated constraint that sync works for job list only, not for assigning. Dialog #11 clarifies the removal behavior you specified.
