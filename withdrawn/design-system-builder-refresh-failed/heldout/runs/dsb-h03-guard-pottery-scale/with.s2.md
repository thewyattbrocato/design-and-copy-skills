No, that's overkill for your situation. A component library with versioning, a docs site and a review board solves coordination problems across many teams and products. You have two people, one site and maybe a second one later, so you'd spend your whole budget on process and ship nothing.

You do still want a small, shared set of design decisions. Two people building 12 pages will otherwise drift: slightly different buttons, three grays, inconsistent spacing. That's about a day of work.

**What to do in the next day or two**

1. **Design tokens in one file.** Put CSS custom properties in a single `tokens.css`:
   - Color roles (`--color-bg`, `--color-text`, `--color-accent`, `--color-border`), not raw names like "terracotta-2".
   - A type scale of 5–7 sizes, plus font families.
   - A spacing scale (4/8/12/16/24/32/48/64).
   - Radii and one or two shadows.

   Both of you use these and never hardcode values. This is the most valuable part.

2. **Roughly 8–10 real components, built as you need them.** Don't build them upfront. Likely candidates are button, link, form field, card (class or session), nav, footer, a date/slot picker, a modal and a notice or alert. Give each one its states (hover, focus, disabled, error). Put them in a `components/` folder in the same repo as the site.

3. **A one-page style reference.** Make a single `/styleguide` route or HTML page that renders the tokens and every component in its states. It doubles as your docs and as a visual check when something changes. A README of rules is enough beyond that, such as "no hardcoded colors" and "add a component only when used twice".

4. **Light review.** Use pull requests, with the other person looking at anything that touches `tokens.css` or `components/`. That's your review board.

5. **Skip versioning.** Both sites can live in one repo, or the second can copy or import the tokens. Git history is your versioning.

**When to revisit it**

Extract a real shared package when the second site starts and you're copying components between repos. Add a docs tool like Storybook only if the component count or team grows past what a single style page handles. At that point you'll know what the system needs, instead of guessing now.

If you want, I can draft the `tokens.css` structure and the styleguide page skeleton. Tell me your stack (plain HTML/CSS, React, Astro, etc.) and any brand colors or fonts Glazeworks already has.
