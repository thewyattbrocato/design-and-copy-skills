The CSS has two problems. Several things move at once, and most of them are slow, looping, or both. A child doing about 20 questions sits through that motion every time, which fits "busy and a little exhausting."

## What's causing it

1. **`.star-reward` spins forever.** This is probably the biggest culprit. A constant 1s linear spin pulls the eye back every time they try to read. Rewards should happen once and then settle.
2. **`.answer-btn.correct` bounces forever.** It bounces for as long as the question is on screen, and the next question has to compete with it. It also overrides the hover `transform`, because animations beat transitions. A correct answer should get one celebration, not a loop.
3. **Everything is slow, and the timings stack.** After a tap, the button takes 1.2s to transition, the bounce runs 1.5s per cycle, the card takes 0.9s to slide in, and the progress bar takes 2s to fill. Nothing finishes together, so the screen is always mid-motion. Over 20 questions, the 0.9s slide-in alone adds about 18 seconds of waiting.
4. **The slide-in is large.** Moving 120px sideways with symmetric ease-in-out is a big, sweeping move for something that happens every question. The card also starts slowly, which feels sluggish.
5. **The hover effect is too strong and too slow.** A 1.12 scale with rotation will crowd neighboring buttons and look wobbly. At 1.2s it lags behind the pointer. `transition: all` also animates properties you didn't intend to animate. On tablets, hover states can stick after a tap, so the rotated, scaled button may stay that way.
6. **The progress bar animates `width` over 2s.** That's slow, it triggers layout, and it keeps moving after the next question has appeared.
7. **There's no `prefers-reduced-motion` handling.** This matters for kids with vestibular or attention sensitivities.

## What I'd change

```css
.answer-btn {
  transition: transform 150ms ease-out, background-color 150ms ease-out;
}
@media (hover: hover) {
  .answer-btn:hover {
    transform: scale(1.03);
    background-color: #ffd166;
  }
}
.answer-btn:active { transform: scale(0.98); }

/* One-shot feedback, then still */
.answer-btn.correct {
  animation: pop 350ms ease-out 1;
}
@keyframes pop {
  0%   { transform: scale(1); }
  40%  { transform: scale(1.08); }
  100% { transform: scale(1); }
}

.question-card {
  animation: slideIn 250ms ease-out both;
}
@keyframes slideIn {
  from { opacity: 0; transform: translateX(24px); }
  to   { opacity: 1; transform: none; }
}

.progress-bar-fill {
  transform-origin: left;
  transition: transform 400ms ease-out;  /* set scaleX(n) from JS instead of width */
}

.star-reward {
  animation: starPop 500ms cubic-bezier(.2, 1.4, .4, 1) 1 both;
}
@keyframes starPop {
  from { transform: scale(0) rotate(-90deg); opacity: 0; }
  to   { transform: scale(1) rotate(0);      opacity: 1; }
}

@media (prefers-reduced-motion: reduce) {
  .answer-btn, .progress-bar-fill { transition: none; }
  .answer-btn.correct, .question-card, .star-reward { animation: none; }
}
```

## Design notes beyond the CSS

- **Pick one focal point per moment.** After a tap, the answer feedback should be the only thing that draws attention. Let the progress bar update quietly, and keep the star reward for milestones, such as every 5 correct answers or the end of the session. Don't show it on every question.
- **Don't rely on motion for wrong answers.** Use a color and icon change, plus a short text hint. If you want motion, use a very small, brief shake, not a bounce.
- **Add a short pause before the next card.** About 600–900ms after feedback lets the child read the result. Right now the slide-in competes with the feedback.
- **Keep motion durations in the 150–400ms range.** Anything longer should be rare, such as the end-of-session celebration.

I can't see the screen, so I'm inferring from the CSS that the loops and long durations are the problem. A quick test is to turn off the two infinite animations and shorten the slide-in. If the teacher still finds it busy, look at the layout and color density next.
