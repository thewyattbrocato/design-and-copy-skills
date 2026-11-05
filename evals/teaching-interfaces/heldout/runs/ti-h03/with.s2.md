**Ship (c): the interactive setup, where the first alert is built step by step with a live preview of today's conditions.**

You have no data, so this rests on how people learn, not on a measured result.

**Why (c)**
- **It teaches by doing.** After it, a user can say, "I can set an alert that fires on days I'd want to surf." The user finishes with a real alert, not a memory of one. (a) and (b) end with the user still facing the blank form.
- **The settings are hard to understand in the abstract.** Is 3–5 ft too small? Does "wind limit" mean offshore or onshore? A live preview shows the answer: "With these settings, today would be a yes/no at [your beach]." Users see what each setting does as they change it.
- **It limits what users must remember.** Build the alert one setting at a time, in the order beach, swell, wind, then time window. Each step shows the earlier choices and its own preview. That keeps new ideas to about one per screen.
- **It's the better choice when you can't measure.** The video and carousel risk the same failure. Users skip them, forget them, or finish them and still misconfigure the alert. (c) puts the setup in the path they're already taking, and its result is the thing you want, a correct first alert.

**Why not the others**
- **(a) Video:** It runs 90 seconds before the user can do anything. It's passive, and users will have forgotten the wind setting by the time they reach the form. It also needs captions and a re-record whenever the UI changes.
- **(b) Carousel:** It's the cheapest option, but it's a benefits-style carousel shown before the app opens. It explains four settings at once, which is more than people retain, and it's far from the moment they use them.

**Make it work**
1. **Fix the form first.** If "wind direction limit" confuses people, rename it or show it as a small compass or offshore/onshore choice at that step. Do that before you add teaching.
2. **Offer a starting point.** Prefill sensible defaults for the chosen beach. Label them as suggested, and let users change them with one tap.
3. **Show the preview at each step.** Use real conditions for today and say why it passes or fails, for example "Wind is onshore at 18 kt, so this would not alert."
4. **Add a visible skip.** Experienced users should get the plain form, and a "how this works" link should stay available later.
5. **Show what the alert will do.** End on a short confirmation, such as "You'll be alerted when [conditions] at [beach], [time window]." Don't use celebration screens.

**Risks**
- It costs the most to build. If today's conditions are calm or unusual, the preview may show nothing useful. Consider also previewing the last few days or the next 48 hours.
- Scope it tightly. Four steps with one preview component is enough. Don't add branching or a tutorial layer.

**How to check it without existing data**
Don't judge by completion of the setup. Instrument two things:
- the share of new users who create an alert in their first session, and
- whether that alert fires and the user keeps it or edits it within about two weeks.

Edits or deletions after the first alert suggest users set it up wrongly. If you can, run 5 to 6 quick usability sessions on the prototype before you build it fully.

**Assumption:** I assumed you can get live or forecast conditions for the spot at setup time. If you can't, (c) loses most of its advantage, and a trimmed (b) with inline hints on the form would be the fallback.
