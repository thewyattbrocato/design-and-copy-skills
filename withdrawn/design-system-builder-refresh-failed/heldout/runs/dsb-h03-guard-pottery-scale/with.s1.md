No, you don't need that. A component library with versioning, a docs site and a review board is built for many teams shipping many products. You have two people, one site and maybe a second one next year. That setup would eat your whole day or two and then become upkeep you'd have to maintain.

You do need a small version of it. Two people building the same site will drift apart on button styles and spacing unless the shared decisions are written down once.

**What to do in a day or two**

1. **Design tokens in one CSS file (2–3 hours).** Use CSS custom properties for:
   - Color roles, named by purpose (`--color-bg`, `--color-text`, `--color-accent`, `--color-danger`) rather than by hue.
   - A type scale of about 6 sizes, plus font families.
   - A spacing scale (4, 8, 12, 16, 24, 32, 48, 64).
   - Radii, shadows, and a max content width.

   Everything else references these and never uses raw hex or pixel values. If the second site comes along, it can import the same file and override a few values.

2. **A short list of components (about half a day).** Build only what the 12 pages need. For a booking site that's probably:
   - Button (primary, secondary, disabled, loading)
   - Form inputs with error states
   - Card (class or session)
   - Date or time slot picker
   - Nav and footer
   - Modal or confirmation message

   Build them as real components in the codebase, in whatever framework you're using. Don't build them as a separate package.

3. **A single living page (1–2 hours).** Make a `/styleguide` route in the site itself that renders the tokens and each component in all its states. That's your docs site. It also makes visual regressions easy to spot.

4. **A one-page README of rules (30 minutes).** Cover:
   - Naming conventions.
   - "Use tokens, never raw values."
   - "If you need a new component, check the styleguide first."
   - "Changes to tokens need a quick ping to the other person."

   That ping is your review board.

5. **Keep design and code aligned.** If you're designing in Figma, mirror the token names there (color styles, text styles, spacing variables). That's what stops design and code from drifting.

**What to skip for now**
- Publishing the library as a versioned package. Use git history. Revisit this if the classes site becomes a separate repo that needs the shared pieces.
- Storybook or a standalone docs site. The styleguide route covers it.
- Formal review process. At two people, a PR review is enough.
- Components you only think you'll need.

**When to revisit:** when the classes site starts, extract the token file and any shared components into a shared folder or package at that point. By then you'll know what's reusable.

If you tell me your stack (plain HTML/CSS, React, Astro, etc.), I can sketch the token file and folder structure.
