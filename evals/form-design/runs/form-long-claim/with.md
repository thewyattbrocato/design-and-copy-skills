# Online insurance claim: structure

The claim should be a task list, not one long form. Each task is short enough for one sitting. Progress saves automatically, so a two- or three-day completion time is expected and nothing is lost.

## 0. Before the first question: readiness page
- Say what the person needs: policy number, date and place of the incident, photos, the police report (or its reference number), and contact details for any other party involved.
- Give an honest time estimate: about 40 questions, 20–30 minutes of active work, and it can be finished over several days.
- Say that progress saves and how long drafts are kept.
- Offer sign-in or an emailed resume link. Make the "Start claim" button the one primary action.

## 1. Claim task list (the hub)
Every visit starts here. It has:
- Verb-named tasks, each with a status (not started, in progress, done) and a time estimate.
- A claim reference number from the start, so people can quote it.
- A "Review and submit" item at the bottom. It stays locked-looking in text ("Finish the tasks above first"), but the button itself is never disabled without an explanation.
- A visible "Saved on [date/time]" note and a "Resume later" link.

Suggested tasks (about 6–7, roughly equal in size):

1. **Confirm your policy and contact details** (~3 questions)
   - Policy number, full name, email, phone (with the reason printed: "We call if we need more detail").
   - Ask eligibility questions early (is the policy active, type of claim), because they decide which branches follow.
2. **Tell us what happened** (~8 questions)
   - Type of incident (radios), date and time, location, a short description in free text.
   - Branching questions, one topic per page.
3. **Add details about the damage or loss** (~8 questions)
   - Branches by claim type: vehicle, property, injury, theft.
   - Photos are requested here, in the task that uses them.
4. **Other people and vehicles involved** (~6 questions, repeating)
   - Ask "Anyone else involved?" first. If yes, give each person their own page, then ask "Add another?"
   - List the people already added above the form, with change and remove links.
5. **Add the police report** (~4 questions)
   - "Was the incident reported to police?" (yes/no radios).
   - If yes, ask for the report number, the agency, and an upload of the report if they have it.
   - If it isn't ready, offer "I'll add this later". The task stays in progress, and the claim can still be submitted if the report isn't mandatory.
6. **Repair, replacement and payment details** (~6 questions)
   - Estimates or receipts, preferred payout method, bank details (asked last, after commitment).
7. **Review and submit**
   - See section 3.

## 2. Inside a task
- Each step has a heading with its name and count, such as "What happened, step 2 of 4".
- One topic per page. A visual progress bar is optional here, because the task list already shows progress.
- Branching:
  - Answers that change what comes next are radios.
  - Dependent questions appear on the next page, not as a hidden-then-revealed block.
  - If a person edits an earlier answer, keep later answers that still apply. If the edit changes the path, say which questions will be asked again.
- **Photos**
  - Before the choice, say what's needed ("Wide shot, close-up of each damaged area") and the accepted types and size limit.
  - Support several files, list them by name with a remove link, and show per-file progress.
  - Accept camera capture on phones.
  - On a failed upload, keep the other files.
- **Police report**
  - Ask for the report number in the same task as the file upload.
  - Accept PDFs and photos of the paper copy.
- Validate on submit of each page, then re-check fixed fields live.
- Show an error summary at the top with links to each field when a page has more than one problem.
- Keep what was typed, including after server errors and timeouts.
- Back always works and keeps answers.

## 3. Review and submit
- Show all answers grouped by task, each group with a "Change" link, with uploaded files listed by name.
- Flag anything incomplete with a link to fix it.
- Add a declaration of truthfulness as a single required checkbox, in plain words.
- The final button names the act: "Submit claim".
- Submitting is irreversible, so this is the one place where a review step is justified.

## 4. Confirmation
- Say that the claim was received and give the reference number.
- Say what happens next and when: the adjuster's contact window, and what they might ask for.
- Say what to do if there's no contact by then, and give a phone number or email.
- Send the same details by email.
- Offer a way to add documents or photos later to the submitted claim.

## 5. Across-the-process support
- **Reminders:** one email after a day or two of inactivity, with the resume link and what's left.
- **Shared work:** if someone else (a spouse, a repair shop) has to supply parts of the claim, let a task be assigned to them by email link, and show who owns it.
- **Help:** a plain-language hint under questions people commonly misread, plus a contact option that doesn't leave the claim.
- **Mobile first:** photos come from phones, so each step needs to work on a small screen with 16px+ text and large touch targets.

If you'd like, I can turn this into a page-by-page question map (which of the 40 questions go on which page, and which answers trigger which branches).
