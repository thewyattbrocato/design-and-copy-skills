Paste the block below into the tool. It's built from how Clutchpoint is used: a parked car in daylight, one thumb, and a few minutes between lessons. It also borrows from the things instructors already use, like the paper diary, the learner's logbook and road signage. If you already have a logo, brand colour or typeface, swap those in and keep the rest.

````
DESIGN BRIEF: CLUTCHPOINT

Clutchpoint is a working tool for independent driving instructors. They use it on a phone, parked at the roadside between lessons, often in daylight glare, with one hand and a few minutes. Learners and parents use the same product to book and pay. It should look like a well-made instructor's diary or logbook, not a generic SaaS app.

DO NOT DO (the usual generated look)
- No stack of equal rounded cards with soft drop shadows.
- No purple/indigo/blue-violet accent, no gradients, no glassmorphism, no glow.
- No emoji as icons, no decorative illustrations, no stock photos of cars or smiling people.
- No invented stats, ratings, testimonials, learner counts or "trusted by" claims. Sample data must be plausible and marked as sample.
- No centered hero-style layouts inside the app. The app opens straight onto today's lessons.

LOOK AND FEEL
- Reference points: a paper lesson diary (a time column, ruled lines), a learner logbook (skills ticked off as they progress), road signs (heavy, plain, legible at a glance).
- Flat and ruled. Structure comes from hairline rules, spacing and type weight, not from boxes and shadows. No shadows anywhere except the one thing that floats above a screen (a bottom sheet).
- Corners are nearly square (2-4px radius, one value everywhere). Buttons and inputs are rectangular slabs, not pills.

COLOUR (adjust if there is a brand, but keep the roles)
- Paper: warm off-white #F3F0E8 background. Ink: near-black #15130F for text and rules.
- One accent: road-marking yellow #FFC400, used only as a fill with ink text on it (the primary action, the current lesson marker). Never use yellow as text on paper.
- Status is shown with words and shape first, colour second. "Paid" and "Owed" are written out; done is a solid ink tick.
  Use a muted green #1F6B3A and a brick red #B3261E only for small status text and marks, never as large fills.
- Everything must pass WCAG AA in bright sunlight conditions: body text at 7:1 or better against its background. Light theme is the default; a dark theme can follow later.

TYPE
- One sturdy, slightly condensed grotesque with road-sign character (Barlow / Barlow Semi Condensed, or Overpass). Heavy weights for times, names and amounts; regular for notes.
- Tabular, lining figures for all times and money so columns align.
- Minimum 16px for anything the instructor reads; primary figures (time, amount) 24-32px. Sentence case, no all-caps blocks of text.

LAYOUT: INSTRUCTOR APP (phone first, thumb reach)
- Home = Today. A ruled timeline: time in a left column, learner name and pickup/lesson type to the right, one row per lesson, separated by hairlines, not cards.
- The current or next lesson is the single focal point: larger, with the yellow marker on its time and its actions directly beneath. Later lessons are quiet rows. Finished lessons collapse to one line with a tick and "Paid" / "Owed".
- The main action sits in a full-width bar at the bottom of the screen, in thumb reach. It changes with the state of the lesson: Start -> Mark done -> Take payment.
- Mark done is one tap with an Undo for a few seconds. No "Are you sure?" dialog.
- Notes on what was practised: a tappable list of skills (reversing, junctions, roundabouts, parking, etc., editable by the instructor) plus a free-text line that works with phone dictation. Each skill has a logbook-style progress mark per learner (introduced / practising / confident) shown as a short row of ticks, not a coloured pill. Last lesson's notes show above the input so the instructor can see where they left off.
- Take payment: the amount is the largest thing on screen. Offer card, payment link to the learner/parent, and "record cash". The result is a plain written statement ("Paid 14:52"), not a confetti moment.
- Weak signal is normal at the roadside. Marking done and saving notes work offline, and the row shows "Saved on this phone" until it syncs.
- Tap targets are at least 48px high, with generous spacing between destructive and primary actions.

LAYOUT: LEARNER / PARENT SIDE
- Same system, calmer and more spacious. Booking works like choosing a slot in the instructor's diary: days across or down, open times as plain ruled slots, taken times left blank.
- Pay screen: who is paying (learner or parent), what for, how much, one button. After a lesson the learner sees what was practised, in the same logbook style.

COMPONENTS AND DETAILS
- Icons: a small consistent set, one stroke weight, always with a text label for anything important. Words over icons where there's room.
- Progress motif: a thin horizontal rule with a small notch marking the current point (the "bite point"). Use it for learner progress and nowhere else.
- Wordmark: "Clutchpoint" set in text in the heavy weight of the chosen face, no symbol until a real logo exists.
- Empty states say what to do next in plain words ("No lessons today. Add one."). No illustrations.
- Motion: only to show something changed (a row collapsing when marked done, a bottom sheet rising). Short and functional, no looping or decorative animation.

SAMPLE DATA
- Use realistic first names, times, amounts and skills, labelled "Sample" in any preview or demo.

CHECK BEFORE FINISHING
- Replace the Clutchpoint name with a competitor's. If the screen still fits, it's too generic, so push it further toward the diary/logbook/road-sign references.
- Test the Today screen at 360px wide, in bright light, with one thumb: can the lesson be marked done and paid for without scrolling or two-handed use?
````

Before you hand it over, check three things:
- **Colours and font:** the hex values and Barlow are my suggestions, not facts about your business. Replace them if you have a brand, and keep the role of each colour.
- **Payments:** the card, payment link and cash options assume that's how you take payment. Change that line if it isn't.
- **Offline use:** I added offline saving because roadside signal is unreliable. It's a real feature for the tool to build, so drop it if you don't want it in version one.
