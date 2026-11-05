Paste the block below. It works because it gives the tool concrete values and a ban list. "Make it distinctive" gets you the default look, but specific tokens and a list of things to avoid don't.

I made some choices for you: the road-signage direction, the amber accent and the font. Change any that don't fit your brand or country. If you already have a logo or colour, put it in place of the amber.

```
# Clutchpoint: visual design direction

Clutchpoint is a working tool for independent driving instructors, used on a
phone, often parked at the roadside in daylight, between lessons, sometimes one-handed.
Learners and parents use it to book and pay. It should look like road signage
and a well-kept instructor's logbook: flat, high-contrast, blunt, trustworthy.
It should NOT look like a generic SaaS or wellness app.

## Do not use (these make it look generic)
- Purple, indigo or violet anywhere. No blue-to-purple gradients.
- Cards with large radii (16px+) and soft drop shadows. No glassmorphism, blurred blobs or gradients.
- Light-grey text on white, pastel tints, or low-contrast "subtle" labels.
- Emoji as icons, stock illustrations, mascot characters, confetti.
- Cheerful filler copy ("You're all set!", "Awesome!"). Write plain, short, practical text.
- Centered hero layouts, floating pill buttons, bottom sheets for everything.

## Colour (light theme is the default; it must read in direct sun)
- Paper:   #F3F0E6 (warm off-white background)
- Ink:     #121517 (text, borders, icons). Body text contrast is at least 7:1.
- Signal:  #FFC20E (road-works amber). The ONE accent. Used for the primary action
           and the "next lesson" highlight. Always with Ink text on top, never white.
- Done:    #1F6B3A (green)   Owing/overdue: #B3261E (red)
  Status colours are for state only, never decoration, and always paired with a
  word or icon so they work without colour.
- Rules/dividers: 1.5px Ink, or Ink at 20% for secondary lines.
- Dark theme: only as a user setting, same structure, Signal stays amber.

## Type
- Typeface: Barlow (or Overpass if Barlow is unavailable). Both come from
  road-sign lettering. No Inter, no system-default look.
- Times, money and registration/plate numbers use tabular figures.
- Sizes: body 17px minimum. Lesson time 28-32px bold. Section labels
  uppercase, 13px, letter-spaced, bold, in Ink (not grey).
- Hierarchy comes from weight and size, not from colour tints.

## Shape and surface
- Corners 0-4px. Borders, not shadows: 2px Ink outlines on buttons and inputs.
  No shadows, except possibly a hard offset block (4px 4px 0 Ink) on the primary button.
- Do not wrap everything in cards. Use full-width rows separated by
  rules, like a timetable or logbook page.
- Dense but not cramped: 16px side margins, 12-16px vertical rhythm.

## Instructor app: Today screen
- A vertical timetable. Each row: big start time on the left, learner name,
  pickup location, lesson length. Rows are separated by rules.
- The next lesson is the dominant element: full-width Signal background, larger type.
  Finished lessons collapse and show a green "Done" mark. Don't hide them.
- One primary action per screen, fixed to the bottom, in the thumb zone,
  at least 56px high and full width. All other tap targets are at least 48px.
- "Mark done" is one tap, with a 5-second Undo. No confirmation dialogs.
- Practice notes: a grid of tappable skill chips (Reverse park, Roundabouts,
  Hill start, Junctions, Dual carriageway, etc.), each with a 3-step rating
  (Introduced / Improving / Solid), plus an optional free-text or voice note.
  Notes must be quick to enter and need no typing.
- Take payment: the amount in very large tabular figures, then one button.
  States are clearly labelled: Unpaid, Paid, Cash, Part-paid.
- The app must work with bad signal: show saved/unsaved state plainly.

## Learner and parent side
- Same system, calmer. Booking is a plain list of available slots (date, time,
  length, price), not a calendar widget.
- The learner's progress reads like a logbook page: skills listed down the left,
  ratings on the right, lesson dates in a ruled table.
- Payment: show what it's for, the total, and the one button.

## Motion and details
- Minimal. Instant state changes and short (120ms) transitions. No bouncy animation.
- Icons: simple 2px-stroke, square-ended, from one consistent set.
- Empty states are one plain sentence and one action.

## Process
1. Before building screens, define these values as design tokens (colour,
   type scale, spacing, radius, border) in one file and use only those.
2. Build the instructor Today screen first and show it to me before continuing.
3. Check every screen against the "Do not use" list before calling it done.
```

Two things to do on your side:

- **Look at the first screen before it builds the rest.** If it drifts back toward rounded cards or soft grey text, quote the specific line from the brief back at it.
- **Test it outdoors.** Open it on your phone in direct sun. Contrast that looks fine on a monitor often fails there.
