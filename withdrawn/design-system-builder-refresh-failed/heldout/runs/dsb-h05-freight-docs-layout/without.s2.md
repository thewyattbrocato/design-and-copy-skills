# Recommended docs structure

Most visitors land on one component page from search or Slack, so build the site around that page. Everything else is secondary.

## Site map, in order

1. **Home**: one screen. A search box, links to the 5-6 most-used components, and a "what's new" link. It shouldn't explain the system's philosophy.
2. **Get started** (two short pages, one for devs and one for designers)
   - Devs: install, set up the theme/provider, render one component, and what to do when something's missing.
   - Designers: where the Figma library lives, how to use tokens and variants, and how to request changes.
3. **Foundations**: color, typography, spacing, elevation, iconography, and tokens. Each page should be a reference table with token names, values, and usage guidance.
4. **Components**: an alphabetical index with a one-line description and a status badge (stable, beta, deprecated) per component. Alphabetical works because people search by name. Add light grouping tags (Inputs, Navigation, Feedback, Data display) as filters rather than as a nested tree.
5. **Patterns**: multi-component recipes tied to your domain. For a freight broker that likely means shipment tables with filtering, quote/booking forms, status timelines, and error and empty states. Patterns are where the system's value shows, and they're often the pages people most need.
6. **Content & accessibility**: voice and tone, and terminology such as "load" vs. "shipment". Add shared a11y rules (focus, contrast, keyboard) that component pages link to instead of repeating.
7. **Contributing & support**: how to request a component, how to report a bug, your release cadence, and who to ask. With two of you, a clear intake path protects your time.
8. **Changelog & migration guides**: versioned, with a "breaking" label. Link to it from each component page.

## What goes on a component page

Use the same template for every component, in this order. The top has to answer the question that brought the visitor there.

1. **Header**: name, one-sentence description, status badge, and links to the Figma file and source code.
2. **Live example**: an interactive default with a props/variant playground, directly under the header.
3. **Install and import**: a copy-paste snippet, with the package name and version.
4. **When to use / when not to use**: include the neighbor to use instead (for example, "Use Select for more than 5 options, not RadioGroup"). This does the most to prevent misuse.
5. **Variants and examples**: each with a short caption and code, such as sizes, states, and with-icon. Show the real states: loading, error, disabled, empty.
6. **Do / Don't**: 2-4 visual pairs, only for mistakes you actually see in practice.
7. **API reference**: a props table generated from the TypeScript types, so it can't drift.
8. **Accessibility**: keyboard behavior, ARIA roles, and screen reader notes. Keep it specific to this component.
9. **Design specs** (mainly for designers): anatomy, spacing, and token usage.
10. **Related components and patterns**.
11. **Changelog for this component**, plus "Edit this page" and "Report an issue" links.

Put a sticky right-hand table of contents on the page. Give each section a stable anchor so Slack links can point at "Accessibility" or "API" directly.

## Practical suggestions for a team of two

- **Generate what you can.** Build the props tables from types and the examples from Storybook or MDX files that sit next to the component code. Docs that live in the same PR as the component stay current.
- **Pick a docs tool that supports this.** Storybook Docs, Docusaurus, or Astro Starlight all work. Choose whichever your devs already know.
- **Use a template and a checklist.** Don't allow a component to be marked stable until its page is complete.
- **Make search a priority.** Check that "dropdown" finds Select, and add aliases for the names people actually use.
- **Migrate in stages.** Split the README by moving the top 5-10 most-used components first, then foundations. Replace the README with a short pointer to the site. Don't wait for full coverage before launching.
- **Check your analytics.** After launch, see which pages get hits and which searches return nothing. Those results should set your priorities.

If you share the README or the component list, I can turn it into a page inventory with a migration order.
