Because people land on one component page from search or Slack, build the docs as a site where each component page works on its own. Don't build it as a book read in order.

## Site layout

Keep the top-level navigation to five sections, in this order:

1. **Start** (one page). What the system is, how to install it, how to get the Figma library, where to ask questions (the Slack channel), and how to request a change. A new dev should be able to use it in 10 minutes.
2. **Foundations**. These are short pages: Color roles, Typography, Spacing, Radius and elevation, Motion, Iconography. Document semantic roles (`text-secondary`, `surface-raised`), not raw ramps. Each page has a table of tokens, what each is for, and one misuse example.
3. **Components**. This is the bulk of the site. It's a flat alphabetical list, not grouped by your internal taxonomy. People search by name, so grouping by category slows them down. Add a filterable index with a one-line purpose per component.
4. **Patterns**. These are recipes that combine components: forms with validation, data tables with filters and bulk actions, empty and error states, and page layouts. For a freight broker, the likely ones are load search/filter, shipment status, and quote entry forms. Write one only after two teams have needed it.
5. **Contribute and changelog**. How to propose something, the admission rule (a second real use), deprecations with migration steps, and release notes. Put the changelog in front of devs, since breaking changes are what they most need to find.

Accessibility doesn't need its own section. Put it on each component page, and add one short page of shared rules (focus, contrast, target size, keyboard).

## Component page

Order the sections by how often they're needed. Most visitors want a live example and the code, and then leave.

1. **Name, one-sentence purpose, and status** (stable / beta / deprecated). Add a "Use X instead" link when status is deprecated.
2. **Live example, then the import and a minimal code snippet.** These go above the fold, with the Figma link beside them.
3. **When to use / when not to use.** Link to the neighbor component for each "not". Most mistakes are picking the wrong one of two similar components.
4. **Variants and props.** Show each variant rendered, and give a props table with defaults.
5. **States.** Show default, hover, focus, pressed, selected, disabled, loading, and error where they apply. A page that shows only the default state is half a spec.
6. **Content guidance and edge cases.** Cover label length and truncation, long or translated strings, and empty values. Add a short do/don't for copy.
7. **Accessibility.** Cover the role and accessible name, keyboard behavior, focus handling, and anything the dev must supply (such as an `aria-label` on an icon-only button).
8. **Design notes.** Cover spacing, sizing, and the tokens the component reads. Designers will want this section, and devs can skip it.
9. **Related components and changelog for this component.** The changelog is a few lines.

Each section needs a stable anchor (`/components/button#states`), because Slack links will point at sections as well as pages. Put a sticky in-page table of contents on the page so people can jump to a section.

## Making it work with two people

- **Generate what can drift.** Build the props table and token tables from the code and token files. Hand-write only the purpose, usage guidance, and edge cases.
- **Use a template and a done checklist.** A component isn't released until every section above is filled in or marked "n/a".
- **Don't write every page now.** Start with the 5–8 components most often asked about in Slack, plus Start and Color. Migrate the rest of the README as pages when someone asks about them. Delete migrated README content and leave a pointer to the site, so there's only one source.
- **Make Slack the feedback loop.** When someone asks a question the docs should have answered, fix the page and reply with the anchor link. After a few weeks, your most-asked questions will show you where the docs are weakest.
- **Search is part of the docs.** Use Algolia DocSearch or your docs tool's built-in search, and add alias keywords, such as "dropdown" on Select and "modal" on Dialog.

I assumed a web product with React components and a Figma library. If you tell me the docs tool (Storybook, Docusaurus, or something else), I can say how to wire up the generated tables and the template.
