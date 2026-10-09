# Validation and errors

Load this when you write validation logic, error summaries or error copy, or handle server errors and timeouts.

## Timing

Default: check on submit. After a field has shown an error, re-check it as the person edits so the message clears the moment it is true.

Why not earlier: a half-typed value is not wrong yet, so an early message is false. Waiting for it to become valid means the message never helps. Checking when focus leaves a field fires when a password manager fills the field or when the person switches windows, so it is both early and late.

Exceptions that stay:

- A password checklist shown above the field before typing, ticking rules off as they are met.
- An availability check (a username, a booking slot) that runs after a short pause in typing.
- A character limit counter that appears near the limit.

If errors keep happening often, the form is too long or the hints are too weak. Fix those instead of adding earlier alarms.

Run every check again on the server. Scripts fail and clients can be changed.

## The summary pattern

Use a summary when there are two or more problems, or on any long form. A one-field form gets an inline message only.

Structure, in prose:

1. After a failed submit, show a box at the top of the form with a heading in plain words ("There is a problem" or "Fix 2 things to continue").
2. List each problem as a link. Each link goes to its field.
3. Move focus to the box so a screen reader announces it first. The box is made focusable by script, without joining the normal tab order.
4. Prefix the page title with the count ("2 problems - Book a table") so it shows in the tab and is announced.
5. At each field, repeat the same message above the input, with an icon or text cue as well as color, and mark the input as invalid for assistive technology.
6. Clear previous errors before each new check.
7. Keep everything the person typed.

Markup sketch (illustrative):

```html
<div id="summary" tabindex="-1" role="alert">
  <h2>There is a problem</h2>
  <ul>
    <li><a href="#date">Choose a date that is today or later</a></li>
    <li><a href="#phone">Your phone number needs 10 digits. It has 8.</a></li>
  </ul>
</div>
<label for="phone">Phone number</label>
<p id="phone-error" class="error"><span aria-hidden="true">&#9888;</span> Your phone number needs 10 digits. It has 8.</p>
<input id="phone" type="tel" aria-invalid="true" aria-describedby="phone-error" value="555 0142">
<script>
  document.title = "2 problems - " + document.title;
  document.getElementById("summary").focus();
</script>
```

Server and client failures share one summary and one look.

## Writing the message

Write one sentence that says what is wrong and how to fix it. Make it readable when separated from its field, because it also appears in the summary.

- Name the field in the message ("Your phone number needs 10 digits"), not "this field".
- Describe the fix in words the person uses. Skip "invalid", "illegal", "mandatory", "please", jokes and blame.
- State the rule you enforce and the person's current state when that helps ("10 digits, it has 8").
- Use the same tone and punctuation for every message in the form.
- An empty submit produces similar sentences for each field. That is fine.

Before and after:

| Before | After |
|---|---|
| Invalid input | Enter your date of birth, like 03 14 1988 |
| Date not allowed | Choose a pickup date that is today or later |
| Code rejected | Your voucher code has 8 letters or numbers. This one has 6. |
| Oops! You forgot something :( | Enter a delivery postcode |
| Phone number format incorrect | Enter a phone number with the area code, like 555 010 0199 |

Accept reasonable variants before complaining. Strip spaces and dashes from a phone or card number in code instead of asking the person to retype it.

## Server errors and timeouts

- A failed save says so at the top, says what is safe ("Nothing was charged"), and offers a way to retry. Do not clear the form.
- If a session can expire during a long form, warn a minute or two ahead and keep a draft so the answers survive.
- Name the field when the server rejects a value (an email already registered), and offer the next step ("Sign in instead").
- Network failures read as the network's fault ("We couldn't reach the server"), not the person's.

## Honesty about security

Sign-in errors may stay a little general, but a message that only says "Error" fails both the person and the goal. "The email and password do not match" is clear enough and does not reveal which was wrong.
