---
name: form-design
description: Use when designing, building, reviewing or fixing a form or input flow - sign-up, sign-in, checkout, settings, booking, contact, search and filter panels, long applications and claims - or one field, control, button or error state inside one. Covers which fields to ask, labels and hints, input types and autofill, which control fits a question (radios, select, checkboxes, free text), required marking, when errors should appear and how to word them, whether the submit button may be disabled, steps and progress, review and confirmation. Also for questions about form behavior and for form markup or CSS fixes. Not for non-form widgets (tabs, menus, toasts), whole-app polish, editable data grids, or marketing copy around a form.
---

# Form design

A form is a conversation where the person wants to be done. Ask only what you need, name every field plainly, say what went wrong in words, and never make the person redo work.

## When to use

- Building or restyling a form: account, payment, preferences, booking, contact, application.
- Reviewing a form spec, mockup or markup for usability problems.
- Writing validation rules, error messages, button labels or confirmation screens, or answering a question about them.
- Structuring a flow that spans several steps or several sittings.

## When not to use

- Tabs, dialogs, menus, toasts and toggles that are not part of a form; a full pre-release sweep of an app; editable data grids; onboarding that teaches the product. Use a dedicated skill for those if one is installed.
- Pages that contain a form only incidentally (a pricing table, a landing hero): do not add fields, validation or error machinery the brief did not ask for.
- Marketing copy around a form, and back-end validation code beyond the reminder that the server must check everything again.

An explicit instruction, an existing design system or a platform convention beats every default below. If the team already has form components, use them and report gaps instead of replacing them. A native desktop or mobile dialog follows its platform: label placement, button order and corner included.

## Procedure

1. Decide what to ask (default: less).
2. Choose one page or several steps.
3. Lay out each field: label, hint, control, width.
4. Pick control and input type, with autofill.
5. Mark required or optional.
6. Plan validation and error display.
7. Name and place the button.
8. Finish the flow: review, confirmation, recovery.

Scale the work to the task. A one-field newsletter box needs steps 3, 4 and 7 only. A fix to one error message needs only step 6.

## Judgment calls

**What to ask.** Default: for each field, name the step that needs it right now; otherwise drop it, defer it, or infer it (a postal code implies a city). One "full name" field unless the system truly needs the parts. Ask for a phone number only when a reason you can print beside the field exists, and then print it. Change when the answer affects price, eligibility or safety: ask early, do not defer.

**One page or steps.** Default: a short form on a single topic (about eight fields or fewer) stays on one page. Change to one topic per page when the form is long, branches on earlier answers, takes payment on a phone, or must survive interruption. Group two questions only when the person treats them as one decision (a start and end date). Order questions by when they feel reasonable to answer: commitment before payment, easy facts before hard ones.

**Labels.** Default: a visible label above the field, outside it, still present while typing. Constraint hints go between the label and the field. A placeholder shows an example and never carries the field's name. Floating labels shrink the label and crowd out the hint, so skip them. Change when a design system or platform convention says otherwise, and in compact rows such as a footer sign-up, where a visually hidden label plus a clear button is enough.

**Size and spacing.** Default: field width previews the expected length (a short postal code is not full width); input text at 16 CSS pixels or more so phones do not zoom on focus; touch targets about 44 pixels or larger; clearly more space between field groups than between a label and its field; the focus outline stays visible. Change when a design system fixes these metrics: follow it, but keep the 16-pixel floor where phones are in scope.

**Controls.** Default: two to about seven exclusive options people should compare get visible radios; a long known list gets a select or autocomplete; several-of-many gets checkboxes. Round means one, square means many. A yes/no question is two radios, or one checkbox for a single agreement. A switch is for settings that act instantly. A dropdown picks a value, never runs a command. Change when space is truly scarce and the options are familiar (a month): a select is fine. See [choice controls](references/choice-controls.md).

**Input types.** Default: the type and input mode that summon the right keyboard, plus standard autofill tokens for name, email, address, postal code, one-time code and new or current password. Turn off auto-capitalize, auto-correct and spellcheck on email, usernames and codes. Do not use a spin-button number input for identifiers such as card or phone numbers. Accept human formatting (spaces, dashes) and normalize it in code instead of rejecting it. See [field patterns](references/field-patterns.md).

**Required or optional.** Default: after cutting questions, most remaining fields are required, so mark the optional minority with the word "optional" in the label. Change when most fields are optional: mark the required ones in words instead. Never leave an asterisk unexplained, and never use color alone. If all fields are required, say so once at the top or mark nothing.

**Validation timing.** Default: check on submit. Once a field has shown an error, re-check it as the person edits so the message disappears as soon as it is true. Do not show errors while a first attempt is still being typed; the first characters of a valid value are not yet valid. Be wary of checking on blur: autofill and switching windows trigger it at odd moments. Change for a password checklist shown before typing that ticks off rules as they are met, and for an availability check (such as a username) that runs after a pause. Always run the same checks on the server.

**Submit availability.** Default: keep the submit button pressable at all times and explain problems after the press. A button disabled until the form is valid gives no reason and is often unreachable by keyboard. Change when a request is in flight: show progress and block a double submit.

**Errors.** Default: the message sits with the field, in words, with an icon or text cue as well as color, and names the fix ("Enter an email address with an @, like name@example.com"). With two or more problems, or on a long form, also put a summary at the top that lists each problem as a link to its field, move focus to the summary, and prefix the page title with the count. Change for a form with one field: one inline message, no summary. Write each message so it reads well in both places. Avoid "invalid", "please", jokes and blame. Keep everything the person typed, including after a server error. See [validation and errors](references/validation-and-errors.md).

**The button.** Default: a verb phrase in the product's own words ("Create account", "Pay $24.00"), one primary action per form, placed directly under the last field and aligned with it so magnification and narrow windows do not lose it. Secondary actions look quieter. Change for native dialogs: use the platform's order and corner.

**Finishing.** Default: show a review with edit links before anything the person cannot undo (payment, sending, deleting). Offer guest checkout and invite an account after success. The confirmation says what happens next, when, and what to do if it does not. Going back keeps answers. Change for a reversible, low-stakes form: no review step. See [multi-step and long forms](references/multi-step-and-long-forms.md).

**Progress.** Default: put the step in the page heading ("Delivery, step 2 of 4"). Change to add a visual bar only for long or multi-session forms, or when people get lost. Do not use unnamed dots, and do not count steps that some paths skip.

**Passwords, codes, sign-in, search.** Default: follow the field patterns reference: password rules shown before typing, paste allowed, a show-password control, one field for a one-time code with its autofill token, one sign-in wording used everywhere, a search box that says what it searches. Change when the platform or an identity provider dictates the sign-in flow: follow it. See [field patterns](references/field-patterns.md).

## Common failures

- **Placeholder or floating label is the only name** → a static visible label above the field; the placeholder becomes an example or goes.
- **Errors appear after one character; submit is grayed out until valid** → check on submit, re-check fixed fields live, keep the button pressable.
- **Red border and nothing else, or "Invalid email"** → a message at the field (and in a summary when there are several) with a cue besides color, saying how to fix it.
- **"Submit" parked at the far right** → a specific verb button under the last field.
- **Asterisks everywhere with no legend** → mark the minority in words.
- **Three name fields for a newsletter; a phone number demanded with no reason** → one field, or none.
- **One box per digit of a code, jumping focus** → one field with code autofill.
- **The form clears after a server error** → keep all values and explain the failure at the top.
- **A dozen unnamed progress dots; tabs splitting one form** → step name and count in the heading; one form per page or one page of fields.
- **A select for Yes/No, or radios for pick-many** → two radios; checkboxes.
- **Heavy machinery on a tiny form** (summary panel, stepper, extra fields on a footer sign-up) → match the pattern to the size of the job.
- **A written answer that runs past a length limit the user gave** → keep to it; cut material before the limit.

## Quick checks

- Every field has a visible, associated label that is not a placeholder, and earns its place.
- Optional or required is marked in words, with no unexplained asterisk.
- Input types, keyboards and autofill tokens fit each field; text is 16px or larger.
- Nothing shows an error before the first submit, except the named exceptions; the submit button is always pressable and names its action.
- An error state exists and shows a message with a fix, at the field and in a summary when there are several; values survive an error, a back press and a reload where practical.
- Irreversible actions have a review step; the confirmation says what happens next.
- Existing design system, platform and brief constraints are followed.

## References

- [field-patterns.md](references/field-patterns.md): load when a specific field is involved (names, email, phone, address, dates, money, quantities, passwords, one-time codes, files, consent).
- [validation-and-errors.md](references/validation-and-errors.md): load when writing validation logic, error summaries or error copy, or handling server errors and timeouts.
- [multi-step-and-long-forms.md](references/multi-step-and-long-forms.md): load when a form spans steps or sittings, or when designing checkout, review and confirmation.
- [choice-controls.md](references/choice-controls.md): load when choosing between radios, checkboxes, selects, autocomplete and switches, or when building filter panels.
