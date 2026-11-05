**Ship (c), the interactive setup.** It's the only option that teaches the thing new users get wrong. They don't lack a definition of "swell height." They don't know what a good range is for their break, or how their wind limit interacts with that break's exposure. A carousel or video explains the settings, but the user still has to guess their values afterward. The interactive flow lets them pick values against today's real conditions.

For example, the setup could show: "Today at Pleasure Point: 4–6 ft swell, wind W at 12 kt. Your alert would have fired at 3 PM." The user sees what each setting does while making the choice, and they leave with a working alert, which is the outcome you care about.

The other two options are weaker for this specific problem:

- **(a) Intro video:** The most expensive to make and maintain. It goes stale as the app changes, and first-launch users skip videos. It also can't show live conditions.
- **(b) Carousel:** Cheap, and a reasonable fallback. But it's passive. Users swipe through four cards and still face the same blank form.

**Risks of (c) to plan for:**
- **Dependence on live data.** If a spot has no current forecast, the preview breaks. Fall back to typical conditions for that spot and label them as such.
- **Dropout mid-flow.** Pre-fill sensible defaults for each step (e.g., the spot's typical swell range) and offer a "use suggested" button, so the flow is quick to finish.
- **Build cost.** It's more work than (b). Reuse the carousel's copy as the step-level helper text so the cheap version isn't wasted.

**Measuring it, since you have no data yet:** Track first-session alert creation rate, alerts still enabled at 7 days, and how often an alert actually fires. The last one matters most. An alert that never fires is a sign the user set it wrong. If you can't build the full flow, run a prototype test with 5–8 surfers before committing to the whole sprint.
