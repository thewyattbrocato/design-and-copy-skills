Paste everything below the line into the tool. Swap any specific choice you disagree with, but keep the rest as concrete as it is. Vague words like "clean" or "modern" are what produce the generic look.

---

**Design brief: Clutchpoint**

**What this is and where it's used**
Clutchpoint is for independent driving instructors. They use it on a phone, parked at the roadside between lessons, often in glare, often one-handed, with about 90 seconds before the next learner gets in. Learners and parents use it to book and pay. Design the instructor side first. The learner and parent side is calmer and simpler, but it should clearly be the same product.

**Design principle**
It should look like something that belongs in a car: road signage, a tidy lesson logbook, a number plate. It should not look like a SaaS dashboard. Every screen should be readable at arm's length in sunlight, and the next action should be obvious without reading.

**Colour**
Light theme by default, because dark UIs wash out in glare. Don't add a dark mode yet.
- Paper (background): `#F3F0E8`, a warm off-white, never pure white
- Tarmac (text, borders, primary surfaces): `#17191B`
- Road-marking yellow (the single accent, used for the main action on each screen): `#FFC500`, always with Tarmac text, never white text
- Done / paid: `#1F7A4A`
- Owing / problem: `#C73A1E`
- Mid grey for secondary text: `#5B5F63`. Don't go lighter, or it disappears outdoors.
- No purple, no gradients, no translucent or glass effects. Aim for 7:1 contrast on all body text.

**Typography**
- Barlow Condensed (600/700) for headings, times, prices and numbers. It's based on road-sign lettering. Set times large, for example "14:30" at 32px or more.
- Barlow (400/500) for everything else.
- Body text is never below 16px. Labels are never below 13px. Use sentence case, not all caps, except for tiny status tags.

**Shape and surface**
- No floating rounded cards and no soft drop shadows anywhere.
- Structure comes from 2px Tarmac rules and flat blocks of colour, like a printed timetable or logbook page.
- Corner radius is 4px at most on buttons and inputs, and 0 on list rows.
- Elevation, where needed, is a hard 2px offset border, not a blur.
- The lesson list is a ledger of full-width rows separated by rules, not a stack of cards. Each row shows time (big), learner name, pickup location and a status mark.

**Layout for the instructor on a phone**
- Primary actions sit in the bottom third of the screen where the thumb reaches. They are full-width blocks at least 56px tall.
- Tap targets are at least 48px, with generous space between destructive and constructive actions.
- The home screen is today's lessons in time order. The current or next lesson is expanded, with a big yellow **Mark done** button. The others stay as compact rows.
- Marking a lesson done is one tap, then straight into "What did they practise?" That screen is a grid of large toggle chips (parallel parking, roundabouts, hill starts, junctions, and so on) plus an optional free-text note, with dictation encouraged. It should be quick to complete with gloves or one thumb.
- Taking payment is a separate, obvious step with the amount in huge type. Offer card, tap, and "mark as paid in cash". The confirmation shows the amount, the learner's name and a clear green "Paid" state.
- Never hide core actions behind menus, swipes, or hover. Don't use a hamburger menu. Use a bottom bar with at most 3 items: Today, Learners, Money.

**Learner / parent side**
- Same type, colour and rules, but with more white space and one task per screen: pick a slot, confirm, pay.
- A learner's progress appears as a logbook-style skills list with ticks, not a gamified dashboard. No confetti, streaks or badges.
- Parents see what they're paying for and when, in plain language.

**Motion**
Minimal. State changes are instant or take under 150ms. No bouncing, no skeleton shimmer, no animated gradients. A completed action is confirmed by a clear colour change and a short text message.

**Voice**
Plain and brisk, like a good instructor. Say "Lesson done", "£40 paid", "Next: Sam, 15:30". Don't write "Awesome!", "Oops!" or "Let's get started!". Error messages say what happened and what to do next.

**Avoid, specifically**
Purple or indigo accents, gradient buttons, rounded cards with soft shadows, pastel tinted backgrounds, emoji as icons, stock illustrations of people, generic hero sections, "glassmorphism", decorative blobs, and centred empty-state cartoons. Icons should be a heavy-stroke (2px), simple, sign-like set, used only when they speed up recognition.

**Before you build anything**
First build only the instructor "Today" screen and the "Mark done → what they practised" flow, and show me. Don't build the rest until I've approved the look.

---

Two things will help the result beyond the brief:

- **Give the tool something real to look at.** Attach your logo, if you have one, and a photo of a paper lesson logbook or a road sign. The tool will anchor to those far more than to adjectives.
- **Check it on a real phone outdoors.** Test it in daylight, not just in the browser. If you can't read it at arm's length, tighten the contrast or enlarge the type, and tell the tool exactly which screen failed.
