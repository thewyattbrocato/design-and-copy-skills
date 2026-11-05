Don't make the 12-second recording the whole post. Treat it as the hero, then break it into one short loop per motion, each with a one-line claim. Reviewers skim, so the first screen has to show the motion, and the text should tell them where to look.

## What to show, in order

**1. First screen: the full flow, looping and silent.**
- Put the 12s recording at the top, autoplaying muted on a loop, with pause, replay and a 0.25× or 0.5× speed control. If your platform won't allow that, export a GIF or MP4 under 10MB that loops cleanly.
- The poster frame should be the finished state: stepper showing, badge updated. Don't use a mid-transition frame.
- Above or beside it, write one plain sentence: *"Add to cart in a bakery ordering app: the button becomes a stepper, the item flies to the cart, and the badge confirms the count."* Add the facts: platform, the 250ms and 400ms timings, and what the user sees at each step.
- Follow with one short paragraph on why you redesigned it. Say what was wrong before, such as no feedback, a jarring jump, or the user losing track of where the item went.

**2. Three sections, one per motion, each titled with the decision.** Use the same pattern in each:
- Claim (15 to 60 words), then a looping clip of just that motion, then a one-sentence caption.
- Cut each clip from your recording and play it at half speed, or show it at normal speed next to a slowed copy.

| Section title | Claim to make | Caption adds |
|---|---|---|
| "The button becomes the stepper, so there's no second tap target" | Morphing in place keeps the thumb where it is and shows that the add worked. | 250ms, `[easing]` |
| "The thumbnail flies to the cart, so you see where it went" | The arc links the item to the cart without a toast. | 400ms, arc path, `[what happens if the cart icon is off-screen]` |
| "The badge bounces, so the count change is noticed" | A small bounce draws the eye to the number after the thumbnail lands. | Bounce starts when the thumbnail arrives, `[duration]` |

If the three motions are choreographed (the badge bounce fires on the thumbnail's landing), say so in one sentence. The sequencing is probably the part reviewers will care most about.

**3. With and without motion, side by side.** This is the strongest proof, because a claim that motion helps is only believable if people can see the alternative. Use your Figma file to make a no-motion version (instant state swap, no flight, no bounce). Put the two clips next to each other at the same size, labeled "Without" and "With", and play them in sync. If you have time, pair this with a before/after of your old interaction.

**4. Figma, as a supporting asset.**
- Link a playable prototype, and say which frame to click to start.
- Add a small spec table: element, duration, easing, delay, trigger. Use your real 250ms and 400ms, and leave `[easing curves]` bracketed until you've filled them in.
- Include a filmstrip of 5 or 6 keyframes of the flight arc. It works as a still that explains the path, which reviewers can read even if they never press play.

**5. End with limits and one ask.**
- Say what's unresolved. Possible items: reduced-motion behavior, a slow device, a rapid second tap while the thumbnail is still flying, or a cart icon that's off-screen.
- Add `[credits: names and roles]` if anyone else contributed.
- Make one request, for example *"Tell me if the 400ms flight feels too long, or if the badge bounce is redundant after the flight."* A specific question gets more replies than "thoughts?"

## What to put in writing

- **Title:** a result, not a project name. For example: "Add to cart: a button that turns into a stepper, with a thumbnail flying to the cart."
- **First line:** tell reviewers what to watch. For example: "Watch the button, the thumbnail, and the badge in that order. The whole flow takes about 0.7 seconds, so there's a slow version below."
- **Captions:** each should add a fact the clip can't show, such as duration, easing, trigger, or condition. Skip captions that just describe what's visible.
- **Reduced motion:** state what happens when it's on, even if the answer is "not designed yet". Reviewers will ask.
- **Results:** I haven't invented any. If you have a measured result, such as testing, an A/B test, or even a qualitative comment from a teammate, put it next to the motion it came from. If you have none, write `[result: how it was measured, and the number]` and delete it before posting. Don't leave it as filler.

## If the posting format is limited

- **Single post or thread:** the hero clip first, then three short loops, then the with/without pair. Keep the text to one claim line per clip.
- **Live review or slides:** use one slide per motion. The clip is the visual, and the title is the decision. Play each clip twice, once at normal speed and once slowed, before you speak.
- **Any format:** assume nobody will click away from the post. The motion has to be playing in the feed.

## What to prepare before next week

1. Export the hero loop, three isolated motion clips, and slowed versions of each.
2. Make the no-motion Figma version and export it to match the "with" clip.
3. Fill the spec table, including easing.
4. Decide your one specific question for the panel.

I can draft the post copy for any of these sections if you share your easing values, what the old interaction did, and which platform you're posting on.
