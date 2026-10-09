Changes, most important first. Where the spec conflicts with these, I'd treat the existing design system as the tiebreaker.

1. **Keep the Pay button pressable and explain problems after the press.** A button that is disabled until everything is valid gives no reason, is often unreachable by keyboard, and can cost you sales. Disable it only while a payment request is in flight, to block double submits.

2. **Validate on submit, then re-check live only fields that have already shown an error.** Fields turning red while someone types flags the first characters of a valid value as wrong. Live re-checking after an error lets the message clear the moment it's fixed.

3. **Make errors specific.** Put a message beside each field that names the fix, with an icon or text cue as well as color. Red alone fails colorblind users and says nothing about what to change. With two or more errors, add a summary at the top that links to each field.

4. **Make phone number optional, or drop it, unless you can print a reason beside it.** Demanding a phone number with no stated need is a common reason people abandon checkout. If delivery or fraud checks really do need it, keep it required and add a one-line explanation under the label.

5. **Replace floating labels with static labels above the fields.** Floating labels shrink the label and crowd out hints. A visible label that stays put while typing is easier to read and to associate with the field. Placeholders should only show examples. (If your design system mandates floating labels, keep them and report the gap.)

6. **Drop the asterisks.** If every field is required, say so once at the top, or mark nothing. An unexplained asterisk on every field adds noise and no information. After the phone change, mark the few optional fields with the word "optional" in their labels.

7. **Name the button for its action and place it under the last field.** Use something like "Pay $24.00" rather than "Pay". Aligning it with the fields keeps it visible when the window is narrow or magnified.

8. **Add a review step before payment, and keep what people typed after any error.** Payment can't be undone, so people should be able to check and edit first. Clearing the form after a server error forces them to redo work.

9. **Check input types, autofill, and size.** Use the right keyboard and autofill tokens for card, name, address and phone, with 16px or larger text. Accept spaces and dashes in card and phone numbers and normalize them in code. This is smaller than the items above, but it noticeably speeds up completion on phones.
