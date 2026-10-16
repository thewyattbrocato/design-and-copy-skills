Here's a tidied version. The copy is close, but three things need fixing before it ships.

| Screen | Now | Proposed |
|---|---|---|
| 1. Title | Add your first walk | Add your first walk *(keep)* |
| 1. Text | Pick a dog, a day and a time. That's all a walk needs. | Pick a dog, a day and a time. That's all a walk needs. *(keep)* |
| 1. Button | Next | Next *(keep)* |
| 2. Title | Add your walking area | Set your walking area *(optional; keep if you prefer)* |
| 2. Text | Draw a circle on the map where you walk. We'll only offer you walks inside it. | Drag the circle over the area where you walk. We'll only offer you walks inside it. |
| 2. Button | Next | Next *(keep)* |
| 3. Title | You're ready | You're ready *(keep)* |
| 3. Text | Your first walk is on the calendar. Tap it any time to change or cancel. | Your first walk is on the calendar. Tap it any time to change or cancel. *(only if they completed screen 1; see below)* |
| 3. Button | Go to calendar | Go to calendar *(keep)* |

**Fixes that matter:**

1. **Screen 2 says "Draw," but the circle is already placed and draggable.** Someone will look for a drawing tool and not find one. "Drag the circle over the area where you walk" matches what's on screen.
2. **Screen 3 assumes a walk exists.** If someone taps Skip on screen 1, "Your first walk is on the calendar" is false. Show this line only when a walk was created. Otherwise use something like "You're set up. Add a walk any time from the calendar." (wording for that case is yours to confirm).
3. **Screen 2 promises filtering the user may never have set.** If someone taps Skip here, the default circle over their city still decides which walks are offered. Either the default is a sensible starting area and the copy is fine, or Skip should say what happens to walk offers.

**Smaller points:**

- Skip on screen 3 is redundant, since the only action there is "Go to calendar." Remove it on the last screen.
- "Skip" is ambiguous for a help flow. If the person can get back to this help later, "Skip for now" says so. I don't know whether a way back exists, so I haven't changed the label. Tell me and I'll update it.

I only had the copy you pasted, not the screens or app code, so I haven't checked the layout or whether the default circle behaves as described. Those two checks are the ones to run before tomorrow.
