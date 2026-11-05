# Presenting the add-to-cart motion to the panel

Reviewers skim because a still can't show motion and a 12-second clip asks them to find the point themselves. So put the clip at the very top, then add three short sections, each making one claim with its own slowed-down proof.

## 1. First screen: the clip and one sentence

Put these in the first viewport, with no backstory above them:

- **Title:** "Add to cart, in three moves"
- **One sentence:** "Tapping Add morphs the button into a quantity stepper (250ms), flies the item thumbnail to the cart icon in an arc (400ms), and bounces the cart badge when the count updates. Bakery ordering app, [iOS / Android / web]."
- **The clip, inline.** Upload the video natively, because a link-out gets skipped. It should autoplay muted, loop, and have a replay control. Trim the 12 seconds to the single best tap, about 3 to 4 seconds, and use that as the hero. Keep the full 12 seconds further down.
- **The ask, in one line:** "Feedback wanted on: [e.g. is the flight too long when adding several items quickly?]". A specific question gets more replies than a general request for thoughts.

If the platform won't autoplay, make the poster frame the finished state: stepper showing 1 and badge showing 1. Don't use a mid-transition frame.

## 2. The three decisions

Give each decision a section titled with the decision. Each has a short claim of about 15 to 60 words, followed directly by its proof.

**A. The button becomes the stepper, so there's no second control to find (250ms)**
- Claim: why morphing in place beats opening a sheet or navigating to a new control. Your reason goes here, in your own words.
- Proof: a crop of just the button at 0.25x speed, where 250ms stretches to about 1 second. Put a **with/without pair** next to it, with the stepper snapping in instantly on the left and the morph on the right.
- Caption: "Same tap, same layout; the morph keeps your thumb on the control that now adjusts quantity."

**B. The thumbnail travels to the cart, so you see where the item went (400ms)**
- Claim: the flight confirms the action and teaches where the cart lives.
- Proof: a slowed clip with the arc path drawn over it as a faint line. This is the one place a static overlay helps. Add a with/without pair here too.
- Caption: one fact the claim lacks, such as the easing, or what happens if the cart icon is off-screen.

**C. The badge bounces on update, so the count change registers**
- Claim: the bounce lands when the thumbnail arrives, which ties cause to effect.
- Proof: a slowed crop of the corner only.
- Caption: the timing relationship, for example "Bounce starts as the thumbnail lands, [Xms] after tap."

## 3. A filmstrip as the still

Show 6 to 8 frames across the 650ms in one row, labeled with timestamps (0, 100, 250, 400, 500ms and so on). It's the only still that conveys motion, and skimmers will read it even if they never press play. Place it right after the hero or after section C.

## 4. Figma: show it, don't just link it

- Embed or link the prototype with a prompt: "Tap Add. Try it twice quickly."
- Include one spec frame listing duration, easing and delay for each of the three animations. Easing values are `[curve for each]`, which you fill in from the file.
- Put the link after the clips, not before. The clips make the argument and the prototype lets people check it.

## 5. The ending

Finish with these three things, and be candid about the limits:

- **What's unresolved:** rapid repeated taps, a cart icon that isn't visible, and what the animation does under reduced-motion settings. Reviewers trust you more when you name these. Whatever you've decided for reduced motion, state it, for example "the flight is replaced by a fade".
- **Evidence, if you have any:** `[result: how it was measured, and the number]`. If you haven't tested it, say "not yet tested with users" instead of implying otherwise.
- **The one action:** repeat the feedback question from the top.

## Production checklist

- Export the clip at full speed plus a 0.25x version. Label the slow one "0.25x" so nobody thinks the animation is sluggish.
- Crop tightly. Three small focused crops beat the whole screen three times.
- Keep the full 12 seconds as the last item, labeled "full flow".
- Test on the panel's actual platform to confirm the video plays inline.
- Keep the text short. If a section runs past a short paragraph, cut it.

## Material you still need to supply

- `[feedback question]`: your real open question.
- `[platform]`: where the app runs.
- `[reasoning for A, B and C]`: why each choice beats the alternative.
- `[easing and delay values]`: from your Figma file.
- `[result]`: any measurement or test, or an explicit "untested".
- `[credits: names and roles]`: if others contributed.

I can draft the actual post text once you send your reasoning for each of the three decisions.
