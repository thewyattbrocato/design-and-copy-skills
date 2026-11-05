# Touch input and sensitive fields

Load this when the form is used on a phone or tablet, or when it asks for personal, identity, health, location or contact data, or for consent and tracking choices. Entries are defaults with a stated exception. A design system, platform convention or explicit instruction wins.

## Touch: fewer things to type, easier things to hit

**Replace typing with a tap where a tap can carry the answer.** Default: a short or near-term set becomes one-tap options with a "Choose another" route (the next seven days, three delivery slots, the last two addresses used); a long set becomes a text field with suggestions, not a select; a small count becomes a stepper with its limits. Change when the exact value matters and is unpredictable (a reference number): a plain field with the right keyboard.

**Suggest from what is already known.** Default: pre-offer the likely answer from location, history or the device (nearest airport, saved address) as a visible, changeable value or a chip. A camera scan of a card or ID is an optional shortcut beside the typed field, never the only route, and says what happens to the image. Change when the suggestion would rest on a sensitive trait: leave it out.

**Card entry.** Default: one numeric field for the number (the brand shows from the first digits, so never ask for card type), then expiry as month and year in one field, then the security code with a hint for where it sits, then the billing postal code. Use the card autofill tokens and a numeric keypad, and format with spaces as the person types. Month and year selects are the failure to avoid. Change when a payment provider supplies its own hosted fields: use them and keep the labels and hints.

**Where the primary button lives.** Default: directly under the last field and aligned with it. With the keyboard open, the focused field and the submit stay visible, so scroll or pin the button above the keyboard on long forms. Leave the system gesture area and browser toolbar clear: bottom padding for the safe area, and no two targets stacked against the screen edge. Change on tablets and touch laptops, where thumbs rest at the sides.

**Do not put feedback under the finger.** Default: labels and hints above their field, error text and pressed or selected state above or beside the control, since the hand covers what lies below it. A confirmation that appears under the thumb is not seen.

**Target size and gap.** Default: about 44 px tall and wide, at least 8 px between neighbors, and the hit area may exceed the drawn control. Make destructive or irreversible controls larger (about 56 px) and at the corners or far edge too. If space is short, keep one side at 44 and the other at 30 or more. Never go under the 24 px floor. Radios and checkboxes get a label that is itself the target. Inline links in a sentence need padding or line spacing so two lines do not share a tap.

**Destructive steps.** Default: do it and offer Undo when the action is reversible. For an irreversible step (delete an account), use its own screen that states what is lost, with a verb button ("Delete account"), the cancel route more prominent and away from the destructive one, and a deliberate act such as typing a word. Not a generic "OK / Cancel". Place the destructive control away from where the thumb rests. Change for a trivial, reversible action: no confirmation.

**Gestures need a button.** Default: swipe, long press and drag shortcuts are extras. A swipe to remove a row also has a visible remove button; drag-to-reorder also has move up and down controls; a hold-to-confirm also has a plain alternative. Use only gestures people already know (tap, swipe, long press, pinch), and never override the browser's back swipe, pull to refresh or zoom. Change when the gesture is the whole point of the screen (a signature pad).

**Keyboards and focus.** Default: one keypad per field, an enter-key label that fits (Next inside a form, Go or Done on the last field), and autofocus only on a single-purpose screen, since an opened keyboard hides half the form. Do not use a spin-button number input for IDs (see [field patterns](field-patterns.md)).

**Test for touch, not for width.** Default: enlarge targets with a coarse-pointer query rather than a viewport breakpoint, because a large screen can be touch and a small window can have a mouse. A hover tip is never the only place a hint lives.

## Sensitive fields

**Per-field question check.** Default: for each personal field, name who uses the answer and for what; no named use, drop it. Title, gender, relationship status, date of birth, occupation, city and income are the usual reflex fields. Date of birth asked only to confirm an age becomes "I am 18 or older". Change when the answer sets price, eligibility, safety or a legal record: ask it, early, with the reason.

**Identity fields.** Default: if a use is real, free text with suggestions beats a short fixed list. A title or gender field that drives something downstream (a locker, a greeting, a product) is a bug in the downstream: fix that rather than keep the field. Separate how to address someone ("What should we call you?") from the name on a legal record. Several answers allowed where several can be true (heritage, language). Change when a rule demands a closed list (a regulated category): show the required list, say why, and keep the display name free-form.

**Say why, in one or two sentences, beside the field.** Default: what it is used for and who sees it ("Used to match you to a clinic. Only your care team sees it."). If the explanation needs more than two sentences, reconsider the field. A privacy page link is for detail, not the explanation. This line is part of the form, not an extra note.

**Optional is not neutral.** Default: a sensitive field is optional, skippable without penalty, and offers "Prefer not to say" only where a blank would look like a wrong answer. A required sensitive field produces made-up answers, and those poison your data. Change when it is truly required: say so in words with the reason.

**Place and pace.** Default: ask sensitive questions after the person has a reason to trust the product and in the step where the answer is used, never in the opening screen of a sign-up. For hard topics (health, abuse, money trouble) give a non-typing route: ask in person, by phone, or skip for now. Do not assume a story: no "partner" field with only two options, no goal list that presumes one life event.

**Names and verification.** Default: accept unusual names, one field, no resemblance tests. Where a policy says "real name", define it as the name the person is known by and give an explanation route. A flag-this-profile flow asks the reporter for a reason and detail, tells the flagged person what is asked and invites them to confirm, and waits a grace period before any lockout.

**Ranges and enums.** Default: widen beyond the sample you imagined: ages past the ones in your customer base, household sizes beyond four, addresses without a street, names without a surname. A range starts below and ends above any real value.

**Permissions for location, camera, contacts.** Default: ask at the moment the feature needs it, with your own sentence first saying what it unlocks, and make the feature work, if more slowly, when the person says no. Change when the whole task needs it (a map): say so before the system prompt.

## Consent and choice screens

Default: the first layer offers Accept and Reject with the same size, style, position and number of taps. Every optional purpose (analytics, ads, sharing, marketing email) is a separate unchecked choice; required terms are separate and stated as required. Granular settings sit behind a "Manage" route that does not replace the first-layer Reject. Do not bundle consent into the terms or reask after a refusal within the same visit. Withdrawing is as easy as giving: a settings entry and the same kind of control. Labels say what is agreed ("Email me offers"), not "I agree" alone, and name what declining costs, if anything, truthfully.

Change when the rule of a platform or region fixes the wording or layout: follow it. Consent rules differ by region and change; have the text and defaults checked by someone who knows your markets.

Before: one green "Accept all", a gray text link "Options", pre-ticked partner boxes. After: "Accept all" and "Reject all" as equal buttons, "Manage choices" beside them, every purpose off until switched on, and a "Privacy choices" link in the footer that reopens the same panel.

## Checks

- Each personal field has a use you can name; a field with none was dropped.
- Identity answers are free text, multiple where they can be, and optional.
- A sensitive field shows its one-sentence reason beside it.
- On a phone, each target measures about 44 px with a gap, and the destructive one is larger and away from the primary one.
- Every swipe or long-press shortcut has a visible button route.
- Accept and reject match in weight; nothing optional is pre-ticked; withdrawal has an entry point.
