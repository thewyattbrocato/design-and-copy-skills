# Docs layout for a two-person design system team

Since most people land on one component from search or Slack, design for that first. Treat each component page as a standalone landing page, and treat everything else as supporting material.

## Site structure (in nav order)

1. **Home / Getting started**: What the system is, and one install-and-render-a-Button path for devs. A short "start here" for designers (library link, how to enable it). Keep it to one screen.
2. **Foundations**: Color, typography, spacing, layout/grid, elevation, iconography, motion. Each has tokens with names, values, and when to use them. Designers and devs both use these, so show the token name next to the Figma style name.
3. **Components**: A filterable index (search, plus categories like Inputs, Navigation, Feedback, Data display, Layout). Each entry has a thumbnail and a one-line description. Show status badges (stable, beta, deprecated).
4. **Patterns**: Multi-component recipes tied to your domain. For a freight broker, that could be a load search form, a rate table, shipment status timeline, quote flow, and error and empty states. This is where you answer "how do I build X", which isn't a component question.
5. **Content / voice** (short): Labels, error message style, number/date/currency/weight formatting, and terminology (load vs. shipment, carrier vs. driver). Logistics apps tend to have many inconsistencies here.
6. **Contributing & support**: How to request a component, how to report a bug, what you will and won't take, office hours, and the Slack channel.
7. **Changelog / migration**: Versioned release notes, breaking changes, and codemods or upgrade steps. Link to it from the deprecated badges.

Put accessibility inside each component page and a short a11y principles page under Foundations, not in a separate silo that no one visits.

## Component page template

Use the same order every time, so people learn where to look. Put the most-needed info at the top, since search arrivals leave quickly.

1. **Header**: Name, one-sentence description, status badge, and links to Figma, source, and Storybook (or similar). Add the package name and version introduced.
2. **Live example + code**: An interactive demo with a copyable snippet right under the title. This is the first thing most people want.
3. **Install/import**: One line.
4. **When to use / when not to use**: Short bullets, with links to the alternatives ("For 2–3 options, use RadioGroup instead").
5. **Variants and states**: Size, emphasis, disabled, loading, error, and so on, each shown visually with a snippet.
6. **Props/API table**: Generated from the TypeScript types so it can't drift. Include defaults and types.
7. **Usage guidelines (Do / Don't)**: Visual pairs for layout, labeling, and placement. Keep it to the real mistakes you've seen in review.
8. **Accessibility**: Keyboard behavior, ARIA roles/labels, focus handling, and contrast notes. Say what's built in and what the consumer must provide.
9. **Content guidance**: Label length, casing, and examples. Skip it if it's not relevant.
10. **Related components and patterns**: Cross-links.
11. **Changelog for this component**: The last few changes, with a link to the full history.

You can split this into tabs, such as **Overview / Code / Design / Accessibility**. That's fine if the default tab holds items 1–5 and 7 and the tabs keep stable URLs. If tabs would cost you extra build work, one scrolling page with an in-page table of contents is also fine.

## Things that matter more than the structure

- **Stable, linkable URLs and anchors**, such as `/components/button#accessibility`. Slack links are your main distribution channel, so make sure the unfurl preview shows the component name and description (set OG metadata).
- **Good search**: Index component names, common aliases ("modal" for Dialog, "dropdown" for Select, "toast" for Snackbar), and prop names. Aliases will do more for you than any layout choice.
- **Generate what you can**: Props tables from types, token tables from token files, and a changelog from release tooling. With two people, anything hand-maintained will go stale.
- **Make the page template enforce itself**: Use an MDX template or a lint check so a new component can't ship without the required sections.
- **Show status honestly**: A "beta" or "deprecated" badge with a migration link saves more support questions than extra prose.

## Rollout suggestion

Don't migrate the whole README at once. Start with the template and your 5–8 most-used components (probably Button, Input, Select, Modal, Table, and Form-related). Then add Getting started and Foundations, and finally Patterns. Check Slack questions each month. Whatever you get asked repeatedly is the next page or section to write, and each answer should link to that page.

If you tell me what your docs tooling is (Storybook, Docusaurus, Zeroheight, something custom), I can adapt this to it. I can also draft the MDX component page template if you want to see one.
