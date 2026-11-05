# Presenting the add-to-cart motion

Reviewers skim past stills, so the motion has to play before they decide whether to keep reading. Put it first, make it autoplay, and give them a few specific things to look for.

## What to make from your 12s recording

1. **Hero loop (5-6s).** Trim to one clean add-to-cart. Crop tightly to the phone screen and cut any dead time. It should autoplay, loop, and play muted without a click. Use MP4/WebM if your platform supports inline video, since it's sharper and smaller than a GIF. Otherwise use a GIF under about 5 MB.
2. **Slow-motion breakdown (10-15s).** Replay the same clip at 25-50% speed. At real speed, 250ms is roughly a blink, so reviewers can't judge the morph or the arc. Add small on-screen labels that appear at each beat:
   - "1 · Morph 250ms"
   - "2 · Fly 400ms"
   - "3 · Badge bounce"
3. **Before/after, if you have the old version.** Put them side by side and in sync. This is the strongest argument you can make, because the improvement is visible without any explanation.
4. **A filmstrip still (5-6 frames).** Show the button, mid-morph, stepper, thumbnail at the arc's peak, landing, and badge bounce. Draw the arc path over it. This is for skimmers and for anyone viewing without video, and it gives people something to point at in comments.
5. **Figma prototype link.** This is for hands-on poking, not the main evidence. Smart Animate often can't reproduce an arc or a bounce faithfully. Say so in the post and call the recording the source of truth.

## Order in the post

1. Hero loop, above everything else
2. Two or three lines of text (below)
3. Slow-mo breakdown
4. Before/after (if you have it)
5. Filmstrip
6. Figma link and specs

## What to write

Keep the part above the fold to about 100-150 words.

- **Headline:** state the outcome, not the feature. For example: "Add-to-cart now confirms in under half a second without leaving the menu." Avoid "Redesigned add to cart."
- **Problem, one sentence:** what the old interaction got wrong, such as no clear confirmation, or users unsure whether the tap registered.
- **Three-beat table:** a short table or list with duration, easing, and the purpose of each beat:

  | Beat | Duration | Easing | Purpose |
  |---|---|---|---|
  | Button → stepper | ~250ms | *(yours)* | Confirms the tap, puts quantity control in place |
  | Thumbnail → cart | ~400ms | *(yours)* | Shows where the item went |
  | Badge bounce | *(yours)* | *(yours)* | Confirms the count changed |

  Fill in the easing and bounce duration from your file. The point is that reviewers can critique specifics instead of saying "feels nice."
- **Why the sequencing works:** say whether the beats overlap or run in series, and why. If the thumbnail launches before the morph finishes, call it out. That is the kind of detail reviewers miss at full speed.
- **Specific feedback requests:** this matters most for getting engagement. Ask two or three pointed questions, for example:
  - "Is 400ms too long for repeat orders, like someone adding six items in a row?"
  - "Does the badge bounce read as confirmation or as noise?"
  - "Does the arc feel natural or too playful for this brand?"
- **Edge cases and constraints:** one line each on what happens with rapid repeated taps, a reduced-motion setting (for example, crossfade with no flight), and a cart icon in a different position. Reviewers will ask, and answering up front shows you've thought about it.

## Practical tips

- Put a caption in the first line like "Watch the 6s clip, then read on." Some people won't see the video unless told it's there.
- Don't rely on audio. Keep the loop silent and self-explanatory.
- If the review has a live segment, play the loop on repeat while you talk, then go to the slow-mo. Open the Figma prototype only for questions.
- Before posting, send it to one person who hasn't seen it and ask what they noticed. If they don't mention the arc or the bounce, make those beats more prominent in the labels.

If you tell me the platform (Slack, Figma comments, Notion, a deck), I can tailor the format and file sizes. I can also draft the post text from your actual easing values.
