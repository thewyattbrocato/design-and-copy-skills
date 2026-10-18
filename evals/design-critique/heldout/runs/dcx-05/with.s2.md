**Not ready to ship as is.** Each screen reads fine alone, but together they contradict each other in a few places. The first two are visible bugs.

**1. Blocker: the progress counter changes mid-flow.**
- Screen 1 says "Step 1 of 4". Screens 2, 3 and 4 say "of 5". Every user sees the total change on the second screen.
- Screens 1–4 are four steps, and the finish screen has no bar. So "of 4" is the likely right answer. I'm inferring that, so check what the design file intends.
- Fix: make the total 4 on all four screens, and drive it from one constant so it can't drift again.

**2. Major: a user who skips the plant gets a false "all set".**
- Screen 4 offers "Skip" and warns that reminders can't start without a plant. Screen 5 then says "Your sanctuary is ready" to everyone. A skipper just told you they have nothing set up, and nothing will remind them.
- Fix: give screen 5 a skip variant, for example "You're in. Add a plant whenever you're ready and reminders will start." Its button should go to add-plant, not just "Done".
- The footer is honest and should stay, but it sits under a Skip link, so it reads as a scolding. Move it up as part of the body copy, or make it a quiet note.

**3. Major: the vocabulary drifts.**
- The same thing is called garden (1), spaces and rooms (2), plant (4), plot (4) and sanctuary (5).
- "Plot" appears only in the footer on screen 4, right where the user is deciding whether to skip. It's the most likely word to confuse, since the screen asks for a plant.
- Fix: use "plant" for the item and "garden" for the collection. Cut "plot" and "sanctuary".

**4. Moderate: screen 1 overpromises.**
- "So we can take care of the rest" implies the app waters the plants. It only reminds you.
- Fix: something like "Let's set up your garden so we can tell you what needs doing and when."

**5. Minor, and they add up.**
- **Button labels:** "Continue" on screen 1 but "Next" on screens 2 and 3. Pick one.
- **Screen 2:** "rooms" and "spaces" are mixed, and Balcony isn't a room. Say "spaces" in both places. The copy doesn't say whether you can continue with nothing selected. If you can, say so. If you can't, disable the button and explain why.
- **Screen 3:** "Choose a time that suits you" adds nothing, since the time picker already shows that. Cut it.
- **Screen 4:** "work out how thirsty it is" covers watering only. Feeding and repotting are half the pitch, so mention them somewhere before the flow ends.

**What works and should stay:**
- The screens are short, and each asks one question.
- "One nudge per day with everything that needs attention" sets expectations about notification volume, which is what people worry about at that point.
- The 8:00 AM default means the screen can be passed with one tap.
- Offering both photo and search on screen 4, with a way out, keeps a reluctant user in the flow.

**Fix order:** 1 (a one-line change), then 3 (a copy pass), then 2 (needs a new screen state), then 4 and 5.

**Not checked:** visuals, contrast, tap-target sizes and the actual layout, since I only saw copy. Also check when the notification permission prompt appears. It should come right after the time is chosen on screen 3, and the camera prompt should come only when "Take photo" is tapped.
