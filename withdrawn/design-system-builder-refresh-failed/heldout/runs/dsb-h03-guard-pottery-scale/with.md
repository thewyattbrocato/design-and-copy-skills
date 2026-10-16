No, you don't need that. Your friend is describing what a large organization with many teams needs. For two people building one 12-page site, a component library with versioning, a docs site and a review board would cost more time than it saves.

You still need the part of a design system that stops the site drifting. That's about a day of work.

**Do this (a day, maybe less)**

1. **Design tokens in one CSS file.** Use CSS custom properties for:
   - colors, named by role (`--color-bg`, `--color-text`, `--color-accent`, `--color-border`) rather than by appearance
   - a type scale (5–7 sizes)
   - a spacing scale (4/8/12/16/24/32/48/64)
   - radii and a shadow or two

   Both of you use only these values. This is the part that makes a second site cheap later.

2. **A short list of real components.** Build only what the booking site needs: button (primary, secondary, disabled, loading), form fields with error states, a class or session card, a date/time slot picker, nav, footer, and a modal or toast if you use them. Put them in your framework's normal components folder. If you aren't using a framework, use plain HTML/CSS partials with a consistent class naming scheme.

3. **A Figma file that mirrors the tokens.** Use the same names for color styles, text styles and spacing, and build the 6–10 components above with their states. The goal is that you and the contractor can say "primary button" and mean the same thing. It doesn't need to be exhaustive.

4. **A single-page README or a Storybook-free "kitchen sink" page.** One route, such as `/styleguide`, that renders every component and state. It works as your docs site, takes about an hour, and is the first place you'll look when something seems off.

5. **A lightweight review habit.** Open PRs for each other's work and check them against the tokens and components. You don't need a board. Add a rule that if you need a new color, size or component, you add it to the system first and then use it.

**Skip for now**
- Semantic versioning and a published package
- A separate docs site (Storybook, Zeroheight and the like)
- A review board or formal governance
- Exhaustive component coverage
- Multi-brand or theming infrastructure

**The second site next year**
Keep the tokens and components in a spot you can extract later. A `/styles/tokens.css` file and a `/components` folder with no booking-specific logic inside is enough. If the classes site really happens, that's when to turn it into a shared package. By then you'll know what's actually reused, so you won't be guessing today.

**When to revisit**
Consider more structure if you get more contributors, you start seeing the same component implemented three ways, or the second site is going ahead and sharing code is becoming painful.

If you'd like, I can draft the token file and a starter component list for Glazeworks. For that I'd need the brand colors and fonts, or I can propose a palette that suits a pottery studio.
