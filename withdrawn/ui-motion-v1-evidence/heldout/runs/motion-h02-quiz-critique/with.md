The main problem is that several things are always moving, and they run longer than the action that caused them. Over 20 questions that adds up to constant motion around a screen where kids are trying to read.

## What's causing the "busy and exhausting" feel

1. **`.star-reward` and `.answer-btn.correct` loop forever.** The infinite spin and bounce keep pulling peripheral attention while the child reads the next question. This is probably the biggest cause. Looping motion should be rare, and it shouldn't run next to reading text.
2. **`.question-card` takes 0.9s and travels 120px with ease-in-out.** The child pays that wait on all 20 questions, which is about 18 seconds of sliding per session. Content that arrives should ease out, and 120px is far more travel than a card swap needs.
3. **`transition: all 1.2s` on the buttons.** Feedback to a tap takes over a second to finish, so the interface feels laggy and dreamy. `all` also animates properties you didn't intend to animate.
4. **The hover effect scales 1.12 and rotates.** The button moves under a finger or cursor that is aiming at it. On touch screens, `:hover` also sticks after a tap, so the tapped button stays tilted and enlarged.
5. **The progress bar takes 2s with linear easing.** It is still crawling when the next card has already arrived, so a third thing is moving. Linear easing is meant for continuous progress, and this is a discrete step. It also animates `width`, which forces layout.
6. **There is no `prefers-reduced-motion` handling.** Some kids will be sensitive to this motion, and nothing lets them turn it off.

At the moment a child answers correctly, four things move at once: a bouncing button, a spinning star, a crawling bar, and the card sliding in. Nothing is the primary motion.

## What I'd change

The feel I'd aim for is calm and decisive: quick, no overshoot, and one thing moving at a time.

```css
.answer-btn {
  /* hover/press feedback ~120ms, only the properties that change */
  transition: background-color 120ms ease-out, transform 120ms ease-out;
}
@media (hover: hover) {
  .answer-btn:hover { background: #ffd166; }   /* color only, no movement */
}
.answer-btn:active { transform: scale(0.97); } /* confirms the tap */

/* Correct: one short pop, then still. The check icon or green color carries the meaning. */
.answer-btn.correct {
  animation: pop 250ms ease-out 1;
}
@keyframes pop {
  50% { transform: scale(1.04); }
}

.question-card {
  animation: slideIn 250ms cubic-bezier(0.2, 0, 0, 1) both;
}
@keyframes slideIn {
  from { opacity: 0; transform: translateX(-16px); }
  to   { opacity: 1; transform: none; }
}

.progress-bar-fill {
  transform-origin: left;
  transform: scaleX(var(--progress));            /* set --progress to 0–1 from JS */
  transition: transform 300ms cubic-bezier(0.2, 0, 0, 1);
}

/* Reward: one celebratory moment, then static */
.star-reward {
  animation: starPop 400ms cubic-bezier(0.2, 0, 0, 1) 1 both;
}
@keyframes starPop {
  from { opacity: 0; transform: scale(0.6) rotate(-20deg); }
  to   { opacity: 1; transform: none; }
}

@media (prefers-reduced-motion: reduce) {
  .question-card   { animation: fadeIn 150ms ease-out both; }
  .answer-btn.correct,
  .star-reward     { animation: none; }
  .answer-btn:active { transform: none; }
  .progress-bar-fill { transition-duration: 1ms; }
}
@keyframes fadeIn { from { opacity: 0; } }
```

If you use `--progress`, `scaleX` will stretch any rounded ends or content inside the fill. That's fine for a plain bar. For rounded caps, keep `width` and shorten it to 300ms instead.

## Spec in numbers

| Element | Duration | Easing | Notes |
|---|---|---|---|
| Button hover/press | 120ms | ease-out | Color on hover, scale 0.97 on press |
| Correct feedback | 250ms, once | ease-out | Scale 1.04 at most, plus color and icon |
| Card enter | 250ms | cubic-bezier(0.2, 0, 0, 1) | 16px travel, so a 20-question session spends about 5s here instead of 18s |
| Progress fill | 300ms | same ease-out | Starts when the answer is submitted |
| Star reward | 400ms, once | same ease-out | Static afterward |
| Reduced motion | 150ms fade | n/a | Movement and loops removed |

Two timing notes beyond the CSS:

- **Don't make kids wait on the animation.** Let them tap "next" at any moment, and don't disable the answer buttons while the card slides. Fifth-graders will tap fast, and a locked screen feels broken.
- **Hold the right/wrong state long enough to read it.** The pause should come from a deliberate hold, such as 600–800ms before advancing or an explicit Next button, not from slow animation.

You didn't include the wrong-answer state. Keep it quiet too: a color change plus text, and at most a 150ms nudge of a few pixels. A shake that repeats across 20 questions would add to the tiredness.

I haven't seen this running, so I'd check it on a real tablet. If it still feels heavy, look for long tasks or input latency in the quiz logic before adding or removing motion.
