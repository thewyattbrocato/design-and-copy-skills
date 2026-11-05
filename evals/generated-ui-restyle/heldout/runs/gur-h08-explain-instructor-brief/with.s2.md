Paste everything between the lines. Afterwards, check the two things in the notes below it.

---

**Design brief: Clutchpoint**

Clutchpoint is a working tool for independent driving instructors. They use it on a phone, parked at the roadside between lessons, often in glare, sometimes with one hand. Learners and parents use the same product to book and pay. It should look like a well-made instructor's diary or logbook, not like a SaaS dashboard. Follow this brief over any default styling you would normally reach for.

**Don't do any of these**
- No purple, indigo or blue-to-violet gradients anywhere.
- No gradients, glows, glassmorphism or soft drop shadows.
- No stack of identical rounded cards with an icon on top. Don't build a "feature grid" or a hero with an illustration.
- No emoji as icons. No stock photos or illustrated people. No avatar circles with a status dot.
- No invented stats, ratings, testimonials or learner names that look real. Label any sample data "Sample".

**Layout**
- The instructor's home screen is today as a timeline. It is a list of rows separated by 1px hairlines, not cards. Each row has:
  - the start time on the left, large, in tabular figures;
  - the learner's name;
  - the pickup point and the lesson length;
  - whether it is paid.
- The next or current lesson is the one focal point. Give it a heavier rule, a tinted band and larger type. Everything else is quieter.
- Put the primary action in the thumb zone, as a full-width bar fixed to the bottom of the screen. It is one action per state: "Start lesson", then "Mark done", then "Take payment".
- Use a single column. Don't use side-by-side panels on the phone.

**Logging a lesson**
- "What they practised" is tap-to-select chips using the vocabulary instructors already use: moving off and stopping, junctions, roundabouts, reversing, parking, emergency stop, dual carriageways, and so on. Let the instructor edit the list.
- Each skill chip can be marked with a progress level, such as seen, practised or competent. This is the learner's record.
- Add an optional free-text note with voice dictation.
- Finishing a note should take under 20 seconds.

**Payment**
- Show the amount in large tabular figures.
- Make the state unmistakable: "Paid" or "Owed £__".
- Cash needs a one-tap "Record as cash" option next to card.
- Never put a payment state in a tiny grey label.

**Learners and parents**
- Use the same system, but calmer.
- Booking is a plain list of available slots grouped by day, not a calendar widget.
- The learner's progress reads like a logbook: a ruled list of skills with their levels and the instructor's notes by date.
- A parent paying sees what they are paying for, with the date, length and amount, before they pay.

**Colour (light theme by default, because it must work in sunlight)**
- Paper background: warm off-white `#F4F1EA`. Surfaces are the same paper, separated by rules, not by shadows.
- Ink for all text and borders: `#14161A`. Body text contrast must be at least 7:1.
- One accent: road-marking yellow `#F2B705`, used only for the current lesson and the primary action. Text on it is always ink.
- Status colours carry meaning only: green `#1E7A4F` for done or paid, red `#B3261E` for owed or cancelled. Never use them decoratively.
- Add a true dark theme only if asked.

**Type**
- Use a sturdy grotesque with a slightly condensed feel, like road signage. Archivo is a good fit. Don't use Inter or the system default for headings.
- All times and money use tabular figures.
- Body text is at least 16px. Times and amounts are 28px or larger. Use at most two weights.
- Sentence case. Write labels in plain trade words: "Pick-up", "Mark done", "Owed", "Practised today".

**Shape and detail**
- Corner radius is 0–4px everywhere. Never use pill-shaped buttons.
- Use 1.5px ink borders and hairline rules for structure.
- Tap targets are at least 48px tall, with generous spacing between them so mis-taps are rare.
- Use few icons, in a consistent 2px stroke, and always with a text label. Don't use icons alone.
- The logo is the wordmark "Clutchpoint" set in the heading face. Don't draw a mark.

**States to design**
- Today with no lessons.
- A lesson in progress.
- A card payment that fails.
- Poor signal. Show "Saved on phone, will sync" instead of a spinner or an error. The instructor must never lose a note.
- A cancelled or no-show lesson.

**Motion**
- Only short transitions that confirm a change, such as a row flipping to done. No loops, no entrance animations.

**Check before you finish**
Put a different business's name on the screen. If it still looks right, the design is too generic. Go back and use more of the driving-instructor vocabulary and layout above.

---

**Check these two things:**
- **Jargon and currency.** I guessed at everyday instructor terms and used "£" as an example. Swap in your country's lesson, test and skill terms.
- **Colours and font.** The hex values and Archivo are my proposals. If Clutchpoint already has a brand colour or font, say so in the brief and it will override these.

I haven't built or rendered anything. Once you have a first build, send me a screenshot and I'll tell you where it has drifted back toward the generic look.
