Here's the tidied copy. I changed very little, because the copy is already short and clear.

**Screen 1: Add your first walk**
Pick a dog, a day and a time. That's all a walk needs.
Button: **Next**

**Screen 2: Set your walking area**
Drag the circle over the area where you walk. We'll only offer you walks inside it.
Button: **Next**

**Screen 3: You're ready**
Your first walk is on the calendar. Tap it any time to change or cancel.
Button: **Go to calendar**

**What I changed**
- **Screen 2 text:** The circle is already placed on the map, so "Draw a circle" doesn't match what people see. "Drag the circle over…" does. I also changed the title from "Add your walking area" to "Set your walking area", since the area is already there and users are adjusting it.
- **Screen 1 and 3:** I left them as they are. The comma-free "a dog, a day and a time" is fine and consistent with the rest.

**Things to check before shipping (these are bigger than copy)**
1. **Skip can make screen 3 untrue.** If someone skips on screen 1, they have no walk, but screen 3 says "Your first walk is on the calendar." Either show a different final message when no walk exists, or make sure Skip never lands on that screen with that text.
2. **Skip on screen 3 is redundant.** "Go to calendar" already finishes the flow, so I'd hide Skip there.
3. **Does Next on screen 1 require a completed walk?** The Dog field is highlighted, but the copy doesn't say whether Next works with an empty form. If it does, the same false claim on screen 3 can happen without Skip.
4. **Skipping the walking area:** If someone skips screen 2, check what "inside it" means for them. Does the app offer walks everywhere, or none?

I don't have the app code in this directory, so I haven't checked any of these. If you point me at the onboarding source, I can check items 1 to 4 and apply the copy edits directly.
