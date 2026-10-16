Assumption: a web product with one brand, and components that exist in both Figma and code.

## Principle

Treat every page as a landing page. Someone arrives at `/components/button` from a search or Slack, so that page has to work with no context. The site is a set of self-sufficient component pages with a thin layer around them, not a book read in order.

## Site layout, in order

1. **Home**: one screen. It has a search box, the 6–8 most-visited components, "I'm a developer" and "I'm a designer" start links, and where to ask for help. It has no marketing copy.
2. **Get started**, two short pages, one for devs and one for designers:
   - Devs: install, import, theme setup, one working example.
   - Designers: where the Figma library is, how to enable it, how to report a mismatch.
3. **Foundations**: one page each for color, typography, spacing, elevation/radius, and motion. Each page lists the tokens, what they're for, and which to use when. Include a "Tokens" reference page with a searchable table of semantic roles.
4. **Components**: an index grouped by job (Actions, Inputs, Navigation, Feedback, Data display, Layout), not alphabetically. Each component links to its own page.
5. **Patterns**: only for combinations that have repeated use, such as forms with validation or tables with filters and bulk actions. For a freight broker, this might include a shipment status display or a rate/quote table. Add one only after a second team needs it.
6. **Contribute and governance**: how to request a component or change, what gets admitted (the second-real-use rule), the deprecation policy, and who to ask.
7. **Changelog and migration**: dated entries, breaking changes called out at the top, and a migration step for each deprecation.

Keep the nav to those seven items. Search is the main way in, so make it prominent and index component aliases and old names (for example "dropdown" should find `select`).

## Component page template

Put the answer to "can I use this, and how?" at the top. Put the edge cases below.

1. **Header**: name, one-sentence purpose, status badge (stable / beta / deprecated), and links to Figma and source code. Add the package version if you can.
2. **Live example with code**: the default case, editable, with a copy button. This is what most visitors came for.
3. **When to use / when not to use**: 3–4 bullets each. "Not" bullets name the alternative and link to it ("for navigation, use `link`"). This stops most mix-ups between similar components.
4. **Variants and options**: a props or variants table with a live example of each.
5. **States**: default, hover, focus, pressed, selected, disabled, loading, error, and empty, wherever they apply. A component documented only in its default state is half documented.
6. **Content and edge cases**: label length and truncation, translation, and empty or very long values. These come up often in freight data (long consignee names, many-leg routes).
7. **Accessibility**: keyboard behavior, focus handling, accessible name, minimum target size, and any ARIA the dev must supply themselves.
8. **Design guidance**: spacing, sizing, and placement rules, with a few "do / don't" image pairs. This section is mostly for designers.
9. **Related**: sibling components and patterns that use this one.
10. **Footer**: last-updated date, an owner, a "report a problem" link, and a changelog excerpt for this component.

The two sections that are easiest to skip but matter most are #3 and #5. The "when not to use" bullets prevent wrong component choices, and the states list is what separates a spec from a screenshot.

## Practical notes for two people

- **Generate what you can.** Build the props table, token list, and version from the code, and write only the guidance by hand. Hand-maintained tables are the first thing to drift.
- **Use one template.** Every component page has the same headings in the same order. People who landed on one page then know where to look on the next.
- **Make each section linkable.** Slack links to `#accessibility` or `#states` are common, so every heading should have a stable anchor.
- **Migrate in priority order.** Don't port the README all at once. Start with your top 10 components by usage (`[count from your repo]` or search analytics if you have them), and put a "docs coming" stub on the rest with the Figma and code links.
- **Retire the README.** Cut it down to a few lines that point at the docs site, so there is only one source.

I can draft the page template as an MDX or Markdown skeleton, or write a full example page for one of your components, if you tell me which framework you use for the docs site (Storybook, Docusaurus, or something else).
