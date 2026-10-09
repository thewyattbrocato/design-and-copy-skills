**Ship (c), the interactive setup.** It's the only option that teaches by doing, and the mistake you describe happens at the point of doing.

- **Users get the settings wrong because they're abstract.** "2–4 ft swell, wind within 45° of offshore, 5am–9am" means little until you see it applied to a beach. A live preview shows today's actual swell and wind next to each setting, so the user can see whether the alert would have fired today and adjust.
- **(a) and (b) explain without connecting to the user's beach.** A video or carousel can be passed without absorbing anything, and a 90-second video on first launch is a lot to ask before the user has seen any value. Carousels also tend to be read once and forgotten by the time the user reaches the setup screen.
- **(c) produces a working alert.** Its output is the thing you care about: a valid alert on the user's first session. The other two only produce a user who has been told about alerts.

Risks to plan for:
- **Live data must be available during setup.** If conditions fail to load, the preview needs a graceful state, and setup should still let the user finish.
- **It takes longer to build** than a video or carousel, so keep the scope tight: one beach, the four settings, one preview.
- **Some users will want to skip it.** Offer a "use suggested defaults" path that still creates an alert.

Because you have no data, I'd treat this as a bet you can check cheaply. Track first-alert completion rate, the share of users whose first alert has settings you'd consider valid, and whether those users keep their alert after a week. If you want a low-cost hedge, add a short inline explanation under each field in the setup flow. That gives you most of (b)'s clarity without building a separate carousel.
