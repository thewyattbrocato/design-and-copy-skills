**Ship (c), the interactive setup.** It's the only option that teaches the thing new users actually get wrong, which is choosing values. The other two explain settings. Neither helps someone pick a 2-4 ft swell range or a westerly wind limit that fits their break.

**Why (c)**

- **People learn by doing a configuration, not by watching one.** A video or carousel is seen once and then forgotten, usually before the user reaches the settings screen. Building the alert in the flow is where the learning happens.
- **The live preview grounds abstract values.** "Swell 2-4 ft, wind offshore only" means little until the user sees "Today at this beach: 3 ft SW swell, wind 8 kt onshore, so this alert would not fire." That shows what each setting does and why the defaults are sensible.
- **It ends with a working alert.** Passive intros end when the user taps "Got it." An interactive setup ends with the thing you wanted them to have, so you can measure whether it worked.
- **The explanation can be cut down.** A short run of four steps (beach, swell, wind, time) with a sensible default at each step covers most of what the carousel would say.

**Risks and how to reduce them**

- **Drop-off mid-flow.** Keep it to four steps, pre-fill every field with a reasonable default, and allow "Set up later." Users should be able to get an alert with two taps.
- **Build cost.** (c) is the most work. Reusing the existing live-conditions data for the preview keeps it manageable. Don't build a bespoke simulator.
- **Experienced surfers may skip it.** That's fine. The defaults and "Skip" cover them, and they're less likely to be the ones who get the setup wrong.

**Measure it, since you have no baseline**

- Share of new users who create at least one alert in their first session.
- Step-by-step drop-off within the setup flow.
- Whether the alert fires and gets opened in the first week, and whether it's still on after 30 days. This matters more than creation alone, because a badly chosen alert that never fires will be deleted.

**What would change my answer:** if most users already know their surf spot's conditions, or if a well-chosen default alert could be created in one tap, the problem is less about teaching and more about defaults. In that case, put the effort into the defaults and the preview, not a longer tutorial.
