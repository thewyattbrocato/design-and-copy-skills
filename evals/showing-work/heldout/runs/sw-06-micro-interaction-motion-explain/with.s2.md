# Presenting the add-to-cart motion

Reviewers skim because the first thing they see is a still or a wall of text. Put the motion in the first screen, then slow it down so each 250ms and 400ms beat can be seen.

## What to show, in order

**1. The clip, first, with one sentence above it.**
- Example: "Add to cart for a bakery ordering app (iOS): the button becomes a quantity stepper, the item flies to the cart, and the badge bounces to confirm. Total motion is under half a second."
- The clip autoplays muted and loops. It needs a replay control and a 0.25× option.
- Trim your 12 seconds to one clean add, about 3 to 4 seconds. The first poster frame should show the finished state (stepper, badge at 1), not a mid-transition frame.

**2. Why, in two or three lines.** State the problem the old interaction had, such as "[old behavior: e.g. no feedback that the tap registered]". Only include what's true. This is your brief.

**3. Three short sections, one per decision, each with its own loop.** Title each with the decision, not "Motion" or "Process". Suggested titles, which you should adjust to your real reasoning:
- **The button becomes the stepper, so quantity changes without leaving the spot** (250ms)
- **The thumbnail flies to the cart, so you see where the item went** (400ms, arc)
- **The badge bounces, so the count change gets noticed** (bounce)

Under each title, give one claim sentence and then its loop:
- Run the loop at 0.25× or as a frame-by-frame filmstrip of 5 to 6 frames. A filmstrip is especially useful for the arc and the bounce, because it lets someone point at a frame.
- Caption it with the facts a viewer can't read from the clip: duration, easing, and the trigger. Example: "250ms, [easing curve]; stepper appears under the tap point."

**4. With vs. without.** Show the same flow side by side at the same width, labeled "Before" and "After" (or "Motion off"). This is the strongest proof that the motion helps. Pin each fault on the old version with a few words, like "no sign the tap registered."

**5. Try it.** Link the Figma prototype, set up so Add is the only tappable thing and it resets itself. Many reviewers will click if it takes one tap and no setup.

**6. Limits and ask.**
- Say what's unresolved. Examples: reduced-motion behavior, what happens on rapid repeat taps, or what the flight looks like when the cart icon is off-screen.
- State exactly what feedback you want. Example: "Is 400ms too long for the flight on repeat adds?" A specific question gets specific replies.

## What to put in writing

- Keep every paragraph to one claim, roughly 15 to 60 words, with the proof (clip or filmstrip) directly after it.
- Don't repeat the paragraph in the captions. Captions carry the numbers and conditions.
- Add a small spec line or table: durations, easing, delay between beats, and whether the flight starts before the stepper finishes. Reviewers can then critique the timing and not only the vibe.
- Use first person and be candid about the tradeoffs.
- Under reduced motion, show the still with a play button, and say what the reduced-motion version does.

## Practical points

- Export a short MP4 per beat, not one long clip. GIFs are fine as a fallback, but MP4 supports pause and speed control.
- Make the slowed version a visible toggle. Don't bury it in a link.
- If the post platform only allows one embed, put the full clip first and the filmstrip image right below it. Link the prototype in the first line.
- Record a second pass at the real device frame rate if your current recording is low-fps. A choppy 400ms arc will look worse than the real thing.

## Placeholders to fill

- `[old behavior and what was wrong with it]`: your brief.
- `[easing curves and exact timings]`: from Figma or code.
- `[result]`: any test, feedback, or measurement, and how it was measured. If you have none, say what reviewers can verify by tapping.
- `[credits: names and roles]`
- `[the specific question you want reviewers to answer]`

If you paste your Figma frame names or the raw prototype settings, I can draft the actual captions and the section copy.
