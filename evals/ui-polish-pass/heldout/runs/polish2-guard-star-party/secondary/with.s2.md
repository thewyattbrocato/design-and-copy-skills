**What already works:** labels are tied to inputs, the error is linked with `aria-describedby`, focus moves to the bad field, the status line is a live region, text colors and the button text meet contrast, and the page has a dark theme and reduced-motion handling.

**Findings, ranked by harm:**

1. **Nothing is saved.** The submit handler only shows a message. "Save my place" is false, and the club's sign-ups go nowhere. Before sending, decide where responses go (a form service, a Google Form, or an email address) and tell me which. Until then, the page needs a placeholder like `<form action="[sign-up endpoint]">` and an honest success message.

2. **A blank name is accepted.** `required` is ignored because of `novalidate`, so an empty name shows "You are on the list: , party of 2". Fix: check `f.name.value.trim()` the same way as the number, and show a short error such as "Enter your name" with `aria-invalid` on the field.

3. **Fractions pass the number check.** "2.5" shows "party of 2.5". Fix: `const bad=!(Number.isInteger(v)&&v>=1&&v<=8);`

4. **The page has no event details.** It says "Saturday" but gives no date, time, location, what to bring, or what happens if the weather is bad. Today is Wednesday 4 November 2026, so "Saturday" could mean the 7th or a later date. Add those facts and a contact line, using placeholders for anything you have not confirmed.

5. **No way to change or cancel.** Add a line such as "To change or cancel, email [contact]."

6. **Input borders fail contrast.** `#c9ced8` on the light background is about 1.5:1, and `#3a3f4b` on the dark background is about 1.7:1. WCAG asks for 3:1 for field borders. Fix: set `--line:#6b7280` in both themes. That gives about 4.8:1 on light and 3.9:1 on dark.

7. **The 8-person limit and the "two parts" message need your confirmation.** The message is confusing as written. Confirm the limit before sending.

8. **Minor:** the hint text sits inside the label, so screen readers read the whole hint as the field name. Moving it to its own element linked by `aria-describedby` would fix that.

**Notes:** I only read the code. I did not run it in a browser or test it with a screen reader. I did not change the file.
