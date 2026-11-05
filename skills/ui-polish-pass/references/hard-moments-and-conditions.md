# Hard moments and conditions

Load when a nearly finished screen will be met by people who are hurried, upset, offline or using one hand, or when it touches money, health, loss, lockout or the person's own history. Entries are defaults with a stated exception. A design system, platform convention or explicit instruction wins. The happy-path states are in [states-and-checks.md](states-and-checks.md).

## Decide which moments apply

Default: before checking anything here, name the one to three situations this screen's people are really in, in the product's own nouns (someone whose delivery is late, whose card was refused, who is locked out before a deadline). Run only the sections that match. Change to technical conditions only when the screen is a calm leisure or expert surface with no urgent, money, health or personal-data moment, and then add nothing about the rest.

Scope; do not delete. A playful touch that works on a calm screen stays there. Take it out of the failure, payment, loss and lockout states and put the personality into the visuals, not the sentence. Do not turn a calm screen into an emergency screen.

## The urgent visitor

Default: a service that people reach in a hurry (clinic, utility, bank, carrier, transit, support) puts the answer to "what do I do now" on the first mobile screen, ahead of the hero image and the mission statement: the urgent route (call, status, report, directions, hours) as a real link or button, one line of current status, and a plain contact for a person. It works without signing in and without script-dependent content. Missing numbers stay visible placeholders ([phone number], [after-hours line]).

Change when the page serves a non-urgent purpose only (a portfolio, a menu). Then the first screen can open on the offer.

Test: at about 360 by 640, the urgent route is on screen without scrolling, is text and not part of an image, and no promotion sits above it.

Before: a full-bleed photo, a welcome line, a login button. After: "Sailing cancelled? [Rebook or refund] [Today's status] [Call the port office: number]", the photo below.

## Hard states: refused, locked, lost, late

Default for a declined payment, a locked account, repeated failed sign-ins, a lapsed plan, a failed or late delivery, a removed item: four parts in plain words. What happened. What is kept or not done (only what is true; otherwise a placeholder such as [how long the order is held]). The next step as a button. A route to a person. No blame ("you entered"), no exclamation marks, no emoji, no mascot, no red alarm banner with a spinner.

For a lockout also say how it clears (a wait, a reset link) in the same place, and that nothing was lost.

Change for low-stakes inline validation, which keeps the product's usual voice.

Before: "Oops! Card not feeling it 🙃", a retry button. After: "Your card was declined. [Nothing was charged / the order is held for [time]]. [Try another card] [Contact support]."

Test: each such state has what happened, what is safe, a next action and a person route, and the text has no joke or exclamation.

## Personal history shown back

Default for year summaries, memories, streaks, milestones, birthdays, recommendations and reminders built from the person's data: neutral wording and visuals (no confetti, no verdict such as "You crushed it" on a year you have not seen), the person's own figures stated without judgment, share text empty or editable and stating only facts, and no personal photo or detail inside a promotion. Every such card gets "Not now" and a lasting "Don't show these", with a plain acknowledgement after.

Design the bad case on purpose: zero, negative, a long gap, a missed day. A counter that resets in red with "broken" language becomes the number reached plus a calm restart.

Change when the person wrote the text or opted into celebration: keep the warmth.

Test: read each line as someone whose year went badly; if it would sting, reword it. A hide control exists, and the empty and negative cases render in words.

## One route is not enough

Default: every step that works by one ability or condition has a second route on the same screen. Hover, swipe, long-press, a timed hold, a sensor wave, sound only, color only, voice only, a camera scan, tap-to-pay only: each gets a visible button, text, a caption, another way to pay or start, or a "Get help" control that reaches a person. On shared or public screens the help route is always visible and idle timeouts warn first.

One hand: primary actions sit within thumb reach (lower half, away from the corners), nothing needs two fingers or a drag with the other hand, and targets keep their gaps. Change when the gesture is the whole point (a signature pad): give the surrounding step a second route instead.

Test: list every interaction on the screen and name its second route; a blank is the defect.

## Changed controls

Default when something is renamed, moved or merged: the old name still finds it (a search alias or a redirect), a one-time pointer sits where it used to be and dismisses itself, the focus order and the accessible name follow the move, and bookmarks and links keep working. A "What's new" line says where it went, once. Change for a brand-new feature with nothing to move.

Before: "Billing" quietly becomes "Payments" under a menu. After: searching "billing" reaches Payments, the old spot shows a one-line pointer until dismissed, and the old link redirects.

Test: someone looking for the old name reaches the new place in one search or one click.

## Bad connection, no script, low battery

Default: the key content and action survive a slow or failing network. Core text and the primary link are in the page itself and do not wait for script or large images. A submit that cannot be sent keeps the input and says "Not sent yet. We'll retry, or [Retry now]". Heavy media does not autoplay and has a fixed frame with text beside it. Polling and animation are light. A state that has timed out is shown, not left as a spinner.

Do not add an offline mode or a service worker the request did not name. Make the failure honest.

Change when the product is only used on a fast wired desk and says so.

Test: with images and script off, the headline, the urgent or primary link and the form are still there; submitting offline loses nothing.

## Keep proportion

- The fixes are edits to wording, defaults, order and a missing route, not new features or pages.
- If none of these moments exist on the screen, say nothing about them.
