## Principle: design every page as a landing page

Most people arrive from a search or a Slack link, so each component page has to work on its own. Navigation matters less than that. The README fails because it's one page that assumes a top-to-bottom read.

## Site layout (in order)

1. **Home / Start here.** One screen with a search box, the 5–6 most-used components, and "I'm a developer" and "I'm a designer" links. Add a short note on what the system is for and how to ask for help.
2. **Getting started.** Two short pages, one for devs (install, import, theme setup, a working "hello button") and one for designers (the library file, how to enable it, where tokens come from).
3. **Foundations.** Pages for color roles, typography, spacing, radius/elevation, and motion (if you have it). Each page lists the semantic tokens with the "use this for…" guidance. Components should link to these, not repeat them.
4. **Components.** An alphabetical index with one-line purposes, grouped by job (Actions, Inputs, Navigation, Feedback, Data display, Layout). The one-line purposes matter most for search. Add the old or common names people use as aliases. A designer who searches "dropdown" should find `Select`.
5. **Patterns.** Combinations that people build repeatedly, such as forms with validation, tables with filters and bulk actions, and empty and error states. For a freight broker, a rate table or shipment status flow may be good candidates. Only document ones that have shown up in at least two places.
6. **Contributing and governance.** How to request a component or change, what gets accepted and why, response time, and the deprecation policy.
7. **Changelog and migration.** A scannable list of changes, with deprecations that name the replacement and the removal date.

Start with 1, 3 (color and spacing only), and 4. Those cover most of the traffic. Everything else can follow.

## Component page template

Order matters. The top has to answer "is this the right thing, and how do I use it?" without scrolling.

1. **Header:** name, aliases, one-line purpose, status (stable, beta, or deprecated), and links to the Figma component and the source code.
2. **When to use / when not to use.** Name the alternative component for each "not". This is the section that stops people from misusing the component.
3. **Live example with the code snippet.** Use the real production component, not a screenshot, and make the default usage copy-pasteable.
4. **Variants and sizes.** Include only those that differ in behavior or hierarchy, and say when to pick each.
5. **States.** Default, hover, focus, pressed, disabled, loading, error, and empty, as they apply. Show each one.
6. **Content guidelines.** Label length and tone, truncation or wrapping rules, and what happens with long text or missing values. For logistics, think long carrier names, addresses, and empty lanes.
7. **Accessibility.** Accessible name, keyboard behavior, focus handling, and contrast checks.
8. **Props / API table.** Put it below the examples. People scan to it when they need it, and it shouldn't push the examples down.
9. **Design specs.** Anatomy and the tokens each part uses, for designers and for anyone debugging a visual mismatch.
10. **Related components and patterns.**
11. **Footer:** owner, last changed, and a "report an issue" link.

Use anchor links for each section (`/button#states`) so Slack links can point to the exact part.

## Habits that keep it working

- **One source.** Generate the props table and token lists from code. Pages that are hand-copied will go stale.
- **Search comes first.** Include aliases and old names, and check that the top 10 things people ask about in Slack actually find the right page.
- **Split the README now.** Move each README section to the page above that matches it before you write anything new. Then fill the gaps, starting with the most-asked components.
- **Keep a gap log.** Record patterns found in products that aren't in the system yet. It shows what to build next.

I assumed a web product with one brand, so I left out theme and multi-brand pages. If you have dark mode or a second brand, add a "Theming" page under Foundations.
