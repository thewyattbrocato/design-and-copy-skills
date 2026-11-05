Paste this in as is. It's written as instructions to the tool, and it gives reasons as well as rules, because tools follow reasons better.

---

**DESIGN BRIEF: Clutchpoint**

Clutchpoint is a tool for independent driving instructors. It should look like something made for people who work from a car, not like a generic SaaS app. Follow the decisions below. Where I haven't specified something, choose the plainer option, not the decorative one.

**Where it's used**
- The instructor uses it on a phone, one-handed, parked at the roadside between lessons. There is often glare, they have a few minutes, and they might be wearing sunglasses or have a thumb over half the screen.
- Design that case first. The main instructor screens must work in direct sunlight, with big targets and no fiddly gestures.
- Learners and parents use it at home, calmly, to book, pay and check progress. It's the same visual system with more room to breathe.

**Visual identity: road paperwork, not app chrome**
The reference is road markings, signage and an instructor's paper logbook or timetable. It should feel like tarmac, paint and ruled paper: functional, high-contrast and slightly utilitarian.

- **Colour:**
  - Background: warm paper `#F3F0E8`.
  - Text and primary surfaces: asphalt `#17191B`.
  - One accent: road-line yellow `#F5C400`, always with asphalt text on top, never white.
  - Status colours are used only for status: done is green `#1F7A4D`, owed or unpaid is red `#C23B22`.
  - No purple, no violet-to-blue gradients, no gradients at all. Text contrast must be at least 7:1 for everything the instructor reads outdoors.
  - Dark mode is asphalt background with paper text, with the same yellow.
- **Type:**
  - Headings, times and amounts: Barlow Semi Condensed, semibold, in a signage style.
  - Body: Atkinson Hyperlegible.
  - Use tabular figures for all times and money.
  - Body text is at least 17px. Times and amounts are large, because they are the main content.
- **Shape and surface:**
  - Corners are 2–4px. No pill buttons and no big rounded cards.
  - No drop shadows and no glassmorphism.
  - Separate things with hairline rules, solid blocks of colour and whitespace, the way a printed timetable does.
  - Avoid putting every item in its own card. A lesson is a row in a ruled list with the time in a left column, not a floating tile.
- **Iconography:** Keep it minimal. Use plain, thick-stroke icons only where a word wouldn't fit. Prefer words. No emoji, no mascots, no abstract blob illustrations.
- **Motion:** Short and functional (under 150ms). Use it to confirm an action, such as a row settling to "done". Don't use it for decoration.

**Instructor screens (phone-first)**
1. **Today:**
   - A vertical timeline of the day's lessons: time, learner name, pickup place, lesson length.
   - The current or next lesson is visually dominant: a solid asphalt block with yellow time text. Everything else is quieter.
   - Gaps between lessons are shown as gaps, with the length of the break.
2. **Finish lesson:**
   - One big full-width control at the bottom of the screen, in thumb reach. Use press-and-hold or slide to complete so it can't be hit by accident.
   - It leads straight into the notes step, and nothing else is in the way.
3. **Notes:**
   - Tappable chips for the things instructors actually log: junctions, roundabouts, parallel park, bay park, reverse around a corner, hill start, emergency stop, mirrors, dual carriageway, independent driving.
   - Each chip cycles through states such as "introduced / needs work / good / test-ready".
   - Below the chips, an optional free-text or voice note.
   - Pre-fill from the previous lesson so the instructor only changes what's different.
   - Nothing here should need more than a few taps.
4. **Take payment:**
   - The amount is huge. The choices are card or tap to pay, send a payment link, or mark as cash/bank transfer, as three big buttons.
   - Outstanding balances are shown in red on the learner's row. They're visible but not alarming.

**Learner / parent screens**
- Same type, colour and shape rules, but calmer and with more spacing.
- **Booking:** the learner picks from the instructor's real available slots, shown as a plain weekly list or grid. No carousels.
- **Progress:** show the skills list from the instructor's notes as a simple checklist-style table, like a progress card. Don't use rings, scores or gamified badges.
- **Payment:** the amount, what it covers and one button. A parent paying for someone else should never have to guess what they're paying for.

**Voice and copy**
Plain and direct, like a good instructor. Use "Lesson done", "Take payment", "Add notes". Don't use "Awesome!", "Let's get started!", exclamation marks or cutesy empty states. Empty states say what's missing and what to do.

**Don't do any of these (they're the usual AI-app defaults)**
- Purple or indigo accents, or gradient buttons or backgrounds
- Large rounded cards with soft shadows
- Pill-shaped buttons and tags
- Hero sections with a big headline and a gradient blob
- A bottom nav with five icons when there are only three real destinations
- Stock illustrations, emoji as decoration, or sparkle icons
- Dashboards full of stat tiles when a list would do

**How to work**
Before writing UI code, list the colour tokens, type scale, spacing scale and component rules you'll use, based on this brief. Build the instructor "Today", "Finish lesson", and "Take payment" screens first and check them at 375px wide. If a choice isn't covered here, pick whichever option is more legible in sunlight on a phone.

---

Two things to adjust before you paste:
- If you're in the UK, "dual carriageway" and "independent driving" are right. In the US, swap them for "highway merging" and similar terms.
- If you already have a logo or brand colour, add it to the colour section. Keep the rule of one accent colour, and let the logo colour be that accent.
