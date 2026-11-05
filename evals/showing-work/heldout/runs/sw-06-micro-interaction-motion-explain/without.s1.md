# Presenting the add-to-cart motion

Reviewers skim because a still or a single looping clip makes them do the work. Your job is to tell them what to watch for, show it at a speed they can follow, and make the first few seconds worth their attention.

## What to show, in order

**1. Lead with the 12-second recording, autoplaying, with no setup above it.**
Put it at the very top, uploaded as a native video or GIF/MP4 that autoplays and loops inline. Don't make it a link. If the platform makes people click to play, most of them won't.

**2. Directly under it, a slowed-down version (25-35% speed) with labeled beats.**
At real speed, 250ms and 400ms are too fast for anyone to judge. Put these overlays on the slow version:
- **0-250ms:** "Button morphs to stepper"
- **~100-500ms:** "Thumbnail arcs to cart" (it can overlap the morph, so label the actual overlap)
- **~500ms onward:** "Badge bounces on count update"

Use a simple timecode or timeline strip at the bottom so the sequencing is visible. Sequencing is probably the main thing they're judging. Does the badge bounce land when the thumbnail arrives, or before?

**3. Three short isolated clips, one per motion.**
Each should be 2-3 seconds and loop, with the other two motions removed. If you can't re-record, crop and loop segments of your existing recording. Reviewers can then critique each motion without it competing with the other two. You can fake these as frame-by-frame stills with ghosted trails (the thumbnail's arc path drawn as a dotted line, the button's start and end states side by side).

**4. A before/after comparison, if there was a previous version.**
Show the old interaction and the new one side by side, both looping. This is often the most persuasive part, because it shows what problem the motion solves.

**5. Figma as the supporting spec, not the main event.**
Link the file, and show the static states in a row: default, stepper, and badge at count N and N+1. Include the prototype link if the Smart Animate version is close to the real thing. Say explicitly that the recording is the source of truth if they differ.

## What to put in writing

Keep the text short and put it after the video. People who read at all will read the first lines only.

**Opening line (the framing):**
> "Tapping Add now confirms the action in three coordinated motions, so users don't have to look away from the item to check it worked."

Adjust that to whatever your real rationale is. The key is to state the *purpose* of the motion, not just describe it.

**Then a short spec table or list:**

| Element | Duration | Easing | Purpose |
|---|---|---|---|
| Button → stepper | 250ms | *(your curve)* | Lets the user adjust quantity without leaving the card |
| Thumbnail flight | 400ms | *(your curve)* | Shows where the item went |
| Badge bounce | *(ms)* | *(your curve)* | Confirms the count changed |

Fill in the easing and badge duration. Reviewers who work in motion will look for them, and missing values look like gaps in your thinking.

**Then 2-3 specific questions for the panel:**
- "Is 400ms too long for repeat adds, such as someone adding six items in a row?"
- "Does the badge bounce read as confirmation, or as noise when the thumbnail has already arrived?"
- "Should the flight shorten or skip after the first add in a session?"

Specific questions get specific feedback. "Thoughts?" gets skimmed past.

**Also state:**
- Reduced-motion behavior (what happens with the OS setting on). If you haven't designed it, say that and flag it as an open question. The panel will likely ask.
- Any constraints you know of, such as engineering feasibility of the arc or performance on lower-end devices.

## Format tips

- **Lead with the verb, not the process.** Start with "Add now confirms in 3 motions", not "Here's what I worked on".
- **Keep videos under ~15 seconds each** and make sure they play muted.
- **Frame the device.** Crop tight on the phone or card so the motion fills the viewport.
- **Offer a live walkthrough.** If the review format allows it, 5 minutes of you tapping through the prototype will land better than any post. Ask for that slot.
- **Don't bury the video** under a long intro or a Figma screenshot. That's the pattern that's getting you skimmed.

## If you can only do one extra thing

Make the slowed-down, labeled version. It turns "a fast thing happened" into "I can see the three beats and judge them," and it's the step that makes reviewers engage with the motion itself.
