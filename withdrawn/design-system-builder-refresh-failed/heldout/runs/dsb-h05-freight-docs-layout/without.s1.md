# Docs layout for a two-person design system team

Treat every component page as a landing page. Most readers arrive from search or Slack, so each page has to work with no context. The top-level navigation matters less than that.

## Site structure

Order the top-level nav by how often people need each section.

1. **Home**: a one-screen page with a component search box, the 5-6 most-visited components, and a "what's new" link. It shouldn't explain the system.
2. **Components**: an alphabetical index with a search filter. Group by category only if you have more than ~30 components. Designers and devs both look things up by name, and categories like "Molecules" make people guess.
3. **Foundations**: color, typography, spacing, iconography, elevation, motion. Each gets a page that covers tokens and when to use them.
4. **Patterns**: multi-component recipes specific to freight brokerage. Examples are a load-search filter bar, a rate table with inline editing, a shipment status timeline, and form validation and error handling. These are where your docs add the most value over a generic library, and a README can't hold them.
5. **Getting started**: two short pages, one for developers (install, setup, theming, a first component) and one for designers (Figma library, how to use tokens, how to request changes). Keep them separate because the audiences share nothing here.
6. **Contributing and support**: how to request or propose a component, where to ask questions (Slack channel), your release cadence, and the changelog and migration guides.

Put the changelog and the "what's new" feed in one visible place. With 19 consumers, upgrade pain is your biggest recurring support cost.

## What goes on a component page

Put these in order, with the most-needed content at the top.

1. **Title, one-sentence description, and status badge** (stable, beta, deprecated). Deprecated components should point to their replacement at the very top.
2. **Live example, interactive.** Make it the first visual element, with controls for the main props.
3. **Install and import snippet**, plus the minimal usage code. A dev from Slack should be able to copy and paste within 10 seconds.
4. **When to use, and when not to**, including links to the neighboring component people confuse it with (for example Select vs. Combobox vs. Radio group). This is often the most useful section.
5. **Variants and states**: sizes, types, disabled, loading, error, empty. Show them as a visual gallery, not prose.
6. **Props/API table**, ideally generated from the TypeScript types so it can't drift.
7. **Design guidance**: anatomy, spacing, content and labeling rules, and a few do/don't pairs. Designers will read this section most.
8. **Accessibility**: keyboard behavior, ARIA roles, focus handling, and contrast notes. Keep it short and specific.
9. **Related patterns and components**, plus a **Figma link** so designers can jump straight to the matching component.
10. **Footer**: last-updated date, version introduced, a changelog link, and a "report an issue" link. The date tells readers whether to trust the page.

To keep a page from being overwhelming, use tabs or anchored sections, such as **Usage / Design / Code / Accessibility**. Deep-link anchors matter too, because people paste a link to "the props table" into Slack.

## Practical advice for a team of two

- **Use a template, and enforce it.** A component page that can't be built from the template isn't ready to ship. Consistency is what lets people find things on pages they've never seen.
- **Generate what you can.** Props tables, the changelog, and example code should come from the source (Storybook, TypeScript types, MDX). Hand-written copies go stale.
- **Make the URLs stable and guessable**, like `/components/button`. Slack links and search results depend on it.
- **Make search good.** Include synonyms in each page's metadata ("dropdown" for Select, "modal" for Dialog, "toast" for Snackbar). This is probably the highest-value small investment.
- **Migrate in priority order.** Don't rewrite everything. Start with the 10 most-used components, which you can find from import counts or Slack mentions. Then do Getting started and Foundations. Link the old README to the new site and shrink it to a pointer.
- **Add a feedback loop.** A "Was this helpful?" widget or an issue link on every page tells you what to fix next.

If it would help, I can draft the component page template as MDX, with the sections above as stubs.
