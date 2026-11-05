Paste the block below. It's built from what you told me: roadside use, glare, one hand, short gaps between lessons. I left out brand colors you haven't chosen, so check the one flagged item at the end.

````markdown
# Clutchpoint: design direction

Clutchpoint is a phone app for independent driving instructors. They use it in a parked car at the roadside between lessons, often one-handed, in daylight glare, with a few minutes to spare. Learners and their parents use the same app to book and pay. Every design decision should serve that instructor in that car. It should look like a well-kept instructor's diary and a road sign, not a SaaS dashboard.

## Do not produce
- Cards with large rounded corners and soft drop shadows. Do not put every item in a card.
- Purple, indigo or violet anywhere. No gradients, glassmorphism, glows or blurred blobs.
- A centered hero, a row of three equal feature tiles, or "Welcome back, [name]!" greetings.
- Emoji, or decorative icons beside every label. Use a word where a word works.
- Invented stats, ratings, testimonials or "trusted by" claims. Mark any sample data as sample.
- Gray-on-white low-contrast secondary text. It cannot be read in sunlight.

## Look
- **Light theme only, built for glare.** Paper background `#F5F2EA` (warm off-white). Text `#16160F` (near-black ink). Hairline rules `#CFC9BA`.
- **One accent: road-marking yellow `#F5B800`.** Use it only as a fill for the primary action and the "current lesson" marker, always with ink-colored text on it (not white). Success and error states use text plus a shape or label, never color alone. Keep any extra status colors muted and rare.
- **Shape:** square and sturdy. Corner radius 2–4px everywhere, buttons included. Separate things with hairline rules and spacing, not shadows or boxes. Use heavy 2px ink rules only to mark the start of a section.
- **Type:** a condensed, signage-style grotesque for times, amounts, learner names and headings (Barlow Condensed or similar, semibold to bold). A plain, sturdy sans for body text (Barlow or IBM Plex Sans). Do not use Inter, Poppins or system defaults. Use tabular figures for all times and money. Body text is at least 16px, and anything the instructor must read at a glance is 20px or larger.
- **No decoration.** No illustrations, stock photos or hero art. Motion is limited to short state changes (a lesson marked done, payment confirmed). No loops, no entrance animations.

## Instructor screens
- **Today** is a ruled diary page, not a list of cards. Each lesson is one row: start time very large in the left column, then learner name, pick-up place and lesson length. The current or next lesson is the only element with the yellow marker and extra size. Past lessons fade to a quiet but still legible state with a done mark. Show unpaid lessons with a plain text label such as "Unpaid £45". Do not add a badge or a color dot.
- **Thumb zone:** primary actions sit in the bottom third of the screen, full width, at least 56px tall. Only one primary action per screen: "Start lesson", then "Mark done", then "Take payment". Never put a destructive or secondary action next to it.
- **Mark done and note what was practised:** it should take under ten seconds with one thumb. Show tappable skill chips (for example reversing round a corner, parallel park, roundabouts, hill start, emergency stop, dual carriageway) that the instructor can multi-select, with a rating for each (needs work / getting there / confident). Pre-select what was practised last time. A free-text note is optional and sits below the chips. Make the chip list editable, because instructors will have their own skills. Do not assume a country or test format.
- **Take payment:** the amount in huge condensed figures, the learner's name above it, and one button. Offer card, cash and "already paid" as plain labeled options. Confirmation is a full-width ink band with the amount and "Paid", not a confetti or checkmark animation.
- **Offline-tolerant:** signal at the roadside is poor. Say plainly when something is saved on the phone but not yet synced, in words, not as a spinner.

## Learner and parent screens
- Same type, colors and rules. Quieter, with more space.
- **Booking** looks like picking a free line in the instructor's diary: days across the top, times as a ruled list, and the chosen slot gets the yellow marker. Show the instructor's name and the pick-up place before the pay step.
- **Paying** shows what the money covers (one lesson, or a block), the total, and one button. A parent paying for a learner should see the learner's name and the lesson date clearly.
- A learner's progress is a plain list of skills with the instructor's ratings. No rings, no gauges, no gamified badges.

## Copy
Plain and short, in an instructor's own words: lesson, learner, pick-up, block of 10, test day, unpaid. Buttons are verbs ("Mark done", "Take payment", "Book this lesson"). No exclamation marks and no marketing language inside the app.

## Check before finishing
Put a rival's name in the header. If the screen still works as theirs, it isn't finished. Then check three things. Can the current lesson be spotted at arm's length in sunlight? Can the instructor mark a lesson done and log skills with one thumb? Are all text and accent pairs at least 4.5:1 contrast?
````

**Why these choices.** The diary and road-sign look comes from the work itself: lessons are time slots, and the roadside means glare and one hand. That is what keeps it from looking like a template. The yellow fill with ink text stays readable in sunlight, and yellow text on white would not.

**To check:**
- If you already have a logo, brand color or company name styling, say so in the brief. It should replace the yellow, not sit alongside it.
- I didn't specify currency or country. The brief shows £ in one example, so change that if it's wrong.
- The skill list is a starting set. Replace it with how you and your instructors actually talk about lessons.
