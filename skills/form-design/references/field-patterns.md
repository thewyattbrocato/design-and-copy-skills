# Field patterns

Load this when a specific kind of field is involved. Each entry gives the control, the input type and mode, the autofill token, a width hint and a typical error message. Treat the entries as defaults: a design system or platform convention wins.

## Names

- Control: one text field labeled "Full name" unless the system needs parts (a printed badge, a legal document, a sorted directory).
- Type: text; autofill `name`. If split, `given-name` and `family-name`.
- Width: wide enough for about 30 characters.
- Do not assume two parts, a capital letter, or no apostrophes and hyphens. Never reject a name for its length or characters you did not expect.
- Error: "Enter your name."

## Email

- Control: single text field. Type `email`, autofill `email`, no auto-capitalize, no auto-correct, no spellcheck.
- Width: wide (about 30 to 40 characters).
- Say why you need it when the reason is not obvious ("We send your receipt here").
- Do not ask twice. A typed-twice confirmation field slows people more than it catches typos.
- Error: "Enter an email address with an @, like name@example.com."

## Phone

- Ask only with a printed reason ("The courier texts you on the day"). Mark it optional when the reason is a convenience.
- Type `tel`, autofill `tel`. Accept spaces, dashes, brackets and a leading plus; strip them in code.
- Width: about 20 characters.
- Error: "Enter a phone number, including the area code."

## Postal address

- One field per line of the address as people say it: street, optional second line, town or city, region where the country has one, postal code, country. Order and labels vary by country, so choose the country first when you ship internationally and adapt the rest.
- Autofill `street-address` (or `address-line1`, `address-line2`), `address-level2`, `address-level1`, `postal-code`, `country`.
- Postal code width matches its length. Offer lookup or autocomplete before asking for every line. Do not make region required where countries lack one.
- Error: "Enter the postal code for your address."

## Dates

- Known dates (birthdays, card expiry): three short labeled fields (day, month, year) or a month-and-year pair, with numeric keypad. A calendar picker is slow for dates far from today.
- Nearby dates (a booking next week): a calendar picker is fine, but keep a typed entry route.
- Say the format in a hint ("For example, 03 14 1988"). Accept both "3" and "03".
- Error: "Enter a date of birth in the past, like 03 14 1988."

## Money and quantities

- Money: text field with decimal input mode, currency shown next to the field rather than inside the typed value. Accept "12", "12.5" and "12.50".
- Quantities: a small numeric field, or a stepper with a typed field beside it. A bare slider is a poor choice when the exact number matters.
- Show the total and its parts before payment.
- Error: "Enter an amount between 5 and 500."

## Passwords

- Show rules in a hint above the field before typing. Prefer a length minimum (twelve or more) over composition tricks; allow spaces and pasting so password managers work.
- Include a "Show password" control. Use the `new-password` token at registration and `current-password` at sign-in.
- A live checklist that ticks off as rules are met is a good exception to submit-time checking.
- Error: "Your password needs at least 12 characters. It has 9."
- Sign-in failures: say that the email and password do not match, without naming which was wrong and without echoing the password back.

## Sign-in

- Labels match the ones used at registration, and the product uses one wording ("Sign in" or "Log in") on every button and link.
- Offer "Forgot password" beside the password field, not after a failed attempt only.
- Do not clear the email field after a failed attempt.

## One-time codes

- One field, labeled with where the code came from ("6-digit code from your text message"). Autofill `one-time-code`, numeric keypad, no auto-advance, paste works.
- Width for the expected digits plus a little room.
- Say how to get a new code and when the old one expires.
- Error: "That code isn't right. Check the latest message, or ask for a new code."

## File upload

- A native file input works for one file. State accepted types and the size limit before the choice, not in the error.
- For several files, list uploaded files above the control with a remove link on each row, and show progress per file.
- Confirm what arrived by name. Do not make the person re-select after a failed submit if you can keep it.
- Error: "That file is 14 MB. Choose a file under 10 MB."

## Consent and agreement checkboxes

- A single checkbox with a label that states the agreement in plain words and links to details. Do not pre-check a box that opts someone into messages or sharing.
- Separate required agreements (terms of service) from optional ones (event emails). Optional ones go last and are marked optional.
- Error: "Tick the box to accept the terms, or go back."

## Search

- A labeled field and a button named "Search" (a visible label, or a hidden label plus an icon button with a text name). Say what is searched when it is not everything ("Search help articles").
- Keep the typed query after results load. Empty results say so and offer a next step.

## Free-text fields

- Use a textarea only when sentences are expected, and size it for the expected length. Show a live character count only when a limit exists, and show it as remaining characters near the limit.
- Do not set a maximum length shorter than what people reasonably write.
