No. For two people, one 12-page site, and maybe a small second site later, a full design system with a versioned component library, a docs site, and a review board would cost more than it saves. Your friend's advice fits teams of 10 or more working across several products. It doesn't fit yours.

You do need a small amount of shared structure so you and the contractor don't build the same button two ways. That's about a day of work.

**Day 1: foundations**
1. **Design tokens (1–2 hours).** Put colors, type scale, spacing, radii, and shadows in one place, as CSS custom properties or a Tailwind config. Use semantic names like `--color-surface`, `--color-accent`, and `--space-4` instead of raw hex values. This is the part that lets a second site reuse the look later.
2. **A short list of components (3–4 hours).** Build only what the 12 pages need. For a booking site that's probably:
   - button, link, input, select, and date/time picker
   - card (class or workshop)
   - nav and footer
   - modal
   - form error and success states
   - a section/container layout

   Write them in whatever framework you're already using, and keep them in a `components/` folder in the same repo.
3. **Figma matches the code (1–2 hours).** Make a single Figma page with the tokens as styles or variables and those same components. Use the same names as the code so you and the contractor can talk about them without confusion.

**Day 2: the working agreements**
4. **A one-page README (about an hour).** Cover how to add a component, the naming conventions, and where the tokens live. That's your docs site.
5. **A lightweight review habit.** Work through PRs, and have the other person look at anything that touches tokens or shared components. That's your review board.
6. **Optionally, a Storybook or a single `/styleguide` page** that renders every component. It's useful if the contractor works asynchronously, but skip it if you're short on time.

**What to skip for now**
- Versioning and publishing a package. If the classes site comes next year, either keep both in one repo or copy the tokens and components over.
- A standalone docs site.
- A formal governance process.
- Building components "just in case" before a page needs them.

**When to do more:** if the classes site actually happens and you're copying components between repos often, that's the point to extract a shared package. By then you'll know which components are stable.

If you tell me your stack (plain HTML/CSS, React, Astro, and so on) and whether you're using Tailwind, I can suggest a specific folder structure and token setup.
