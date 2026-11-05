# Presenting the add-to-cart motion

Skimmers won't read a description of motion. Make the motion the first thing they see, play it without a click, and tell them where to look. Everything else supports that.

## What to show, in order

**1. Hero loop (first thing in the post, no click needed)**
- Trim your 12s recording to a tight 4–6s loop of one complete add: tap, morph, fly, badge bounce.
- Export as an autoplaying, muted, looping MP4 or GIF. If the platform only shows a link or player, put the video above any text.
- Crop to the phone and the cart icon. Cut the OS chrome and dead time.

**2. Slow-motion breakdown (second)**
At real speed, 250ms and 400ms are hard to see. Reviewers will say "looks nice" and move on without registering what you designed.
- Make a 0.25× version of the same clip, about 10–12s.
- Burn in simple labels that appear on each beat: "1. Button → stepper (250ms)", "2. Thumbnail arcs to cart (400ms)", "3. Badge bounce".
- Put the real-speed and slow-mo versions side by side if the platform allows it. Otherwise stack them, with real speed on top.

**3. Before/after (third, if there is a "before")**
- Show the old interaction (instant swap, no feedback) next to the new one, same device frame, same tap.
- This is the most persuasive frame for skimmers because the difference is visible without explanation.

**4. Three short isolated clips (fourth)**
Cut one 2–3s loop per beat, each with one sentence of text next to it. This lets someone comment on "the arc feels too floaty" without having to describe a timestamp.

**5. Figma (last, as backup)**
- Link the prototype, but don't depend on it. Prototype playback in Figma often can't reproduce an arc or a bounce faithfully, so say so: "Prototype approximates the timing; the video is the source of truth."
- Include a static spec frame with keyframe strips (4–5 frames per beat laid out left to right), durations, easing curves, and start and end positions.

## What to write

Keep the written part short enough to read in about 30 seconds. Put it directly under the hero loop.

1. **One-line summary:** "Adding an item now confirms itself in three connected moves, so users never wonder whether the tap registered."
2. **The problem:** one sentence on what was wrong before. Use real evidence if you have it, such as users double-tapping or missing that the cart updated.
3. **What to watch for:** a numbered list matching the labels in the slow-mo clip:
   - Button morphs into the stepper (250ms, ease-out): *the control the user needs next appears where their finger already is.*
   - Thumbnail flies in an arc to the cart (400ms): *it shows where the item went.*
   - Badge bounces on count update: *it confirms the change at the destination.*
4. **Why the timings:** one line on why the whole sequence takes roughly 400ms total (the beats overlap) and stays under the point where it would slow a user adding several items.
5. **Edge cases you handled (or didn't):** rapid repeated taps, a count of 10 or more, reduced-motion setting. If you haven't handled reduced motion, say what you plan to do, such as a fade or an instant swap with the badge still updating.
6. **The specific feedback you want:** this matters most for getting engagement. Ask pointed questions:
   - "Does the arc feel natural or distracting?"
   - "Is the badge bounce noticeable enough without being annoying on repeat adds?"
   - "Is 400ms too long if someone adds five items in a row?"

A vague ask like "thoughts?" gets skimmed. A specific question gets answered.

## Practical details

- **Name the files clearly,** for example `add-to-cart_realtime.mp4` and `add-to-cart_0.25x.mp4`, so reviewers know which is which if they download them.
- **Add captions,** since some reviewers will watch muted, but don't rely on audio.
- **Check autoplay** in the actual tool the panel uses. If it doesn't autoplay, open with a thumbnail that has a play icon and the text "6s – watch this first."
- **Show the recording on a real device** if you can. If the 12s recording is a simulator capture, consider re-recording at 60fps. Dropped frames will make good easing look janky.
- **If you have an hour,** re-record the cart tap a few times in a row. A short clip of three rapid adds in a row shows the interaction holds up under repeat use.

## If you're presenting live

Play the real-speed loop once without commentary and ask what they noticed. Then play the slow-mo version and walk through the three beats. People remember what they noticed themselves, and this order lets them find your intent before you explain it.

If you tell me where the post will live (Figma comments, Slack, Notion, a slide deck), I can tailor the layout and give you exact export settings for the clips.
