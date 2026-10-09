---
name: design-system-builder
description: Use whenever shared design decisions are being created, cleaned up or extended, in any language and at any length - "create a design system", "our tokens are a mess", "the same button looks different on every page", "add dark mode or a second brand", "design and code have drifted", "should this join the system", "naming for colors and spacing". Covers design tokens, type, spacing, color roles, radii, elevation, motion and layout values, themes, components and their states, documentation, change rules, in CSS, JSON or specs. Not for styling one page (the focused skills), drawing a brand (brand-identity), or auditing a product without building (design-critique).
---

# Design system builder

A system is a small set of decisions made once and reused: values, names, components, rules for change. Unguided, it dumps every value from a mockup into tokens (dozens of near-identical grays, spacing in one-pixel steps), names tokens by color or page, gives every property its own token, builds dark mode by inverting, documents only the default state, names components after where they first appeared, and lets design files and code drift apart.

## When to use

- Starting a system, extracting one from existing screens, or adding tokens, a component, a theme, a density or a brand to one.
- Cleaning a token file or component set, deciding whether a pattern joins the system, naming things, writing the guide or the change process.
- A short request ("what should our spacing tokens be?") gets the same rules at sketch size.

## When not to use

- One page or screen: use the focused skills (typesetting, color-palette, spacing-and-grouping, layout-structure) if installed and do not build a system around it. A weekend flyer needs a page, not tokens.
- An established system already exists (an open-source kit, the company's own): theme and extend it; add a token or component only for a real gap and say how overrides are governed. Rebuilding needs a stated reason.
- Creating the brand itself: brand-identity if installed. Auditing without building: design-critique if installed. Build tooling beyond token formats: out of scope.

## Rules that change the output

1. **Inventory before inventing.** List what exists with counts (colors, sizes, spacings, radii, component variants) grouped by purpose. Near-duplicates are the first finding: three grays one step apart are an unresolved conflict, not a palette. Count content types and templates, not pages. With nothing to inventory, start from the product's real screens or ask for them; do not make up an inventory.
2. **Short scales, chosen by constraint.** Fix each scale in advance (spacing, type, radius, shadow, border, opacity, duration); neighbors at least about a quarter apart, closer at the small end, wider at the large end. A new value replaces or merges with one; it is not added. Choose by comparing with each neighbor, not by calculating. Typical sizes: type 4 to 6 roles, spacing 8 to 10 steps, radii 2 to 4, elevations 2 to 4, motion 3 to 4 durations and 3 easings. These are the same thresholds the focused skills use; take the craft from them.
3. **Three tiers, no more by default.** Raw values (ramps, scales) feed semantic roles (`text-secondary`, `surface-raised`, `border-subtle`, `accent`, `danger`, `space-inset-md`); components read semantic roles. Add a component-level token only when that component needs an independent knob; one-off values stay local and marked as exceptions. Mechanics in [token architecture](references/token-architecture.md).
4. **Name by role and structure.** `color.text.secondary`, not `gray-600` in components and never `homepage-hero-blue`. Components are named for what they are (`media-card`), not where they live or what they show. Two things that look alike but behave differently (a navigation disclosure and a command menu) are two components; two that behave alike share one.
5. **Themes remap semantics.** Light, dark, high contrast and brands swap what each role points to; raw values are never inverted. Dark surfaces get lighter as they rise, accents are re-tuned for the ground, and every text and component pair is checked in every theme. Honor the system color-scheme setting, allow an override, and test forced-colors.
6. **Promote on second real use.** A pattern enters the system when a second team or screen needs it; generalize its interface by structure, document it, and check it is not a copy of an existing component's behavior. No speculative components because "systems have a carousel".
7. **Components are built from tokens and finished.** Variants follow behavior. Design every state that can occur (default, hover, focus, pressed, selected, disabled, loading, error, empty), plus names, keyboard, focus, target size, and edge content (long labels, translation, empty values). A spec with only a default state is half a spec. Template in [components and governance](references/components-and-governance.md).
8. **Expressive outside, calm inside.** A brand's personality lives in neutrals, type and a few accents; transactional screens keep conventional, predictable patterns. Separate content from design the same way for charts: palette, text sizes and grid weight are tokens, the data mapping is not.
9. **One source.** Tokens and components are defined once and consumed by design files and code (a token file exported to both). Any divergence is a defect with an owner, not a note.
10. **Govern in proportion.** Four change types (add, modify, deprecate, remove), named owners, a changelog, deprecation announced before removal with a migration, someone allowed to say no. A guide states principles with reasons and shows misuse; it enables more than it polices. A one-squad system needs a page, not a committee.

## Missing facts

If the product, platform, brand colors, existing tokens or team size are not given, assume a web product with one brand and a small team, say so in one line, and deliver. Ask once, with a default, only when interactive and the answer changes the structure (an existing system, native platforms, many brands). Never invent the user's current tokens, usage counts, adoption figures, owners or components; when a count is needed, mark it `[count from your repo]` and continue. Hex values you propose are proposals; say they are checked for contrast only if you checked them.

## Do not produce

- A palette of one-step-apart grays or a spacing scale in 1px steps; twelve type sizes.
- Components referencing raw ramps (`blue-500`) or tokens named by page, color or mood.
- A token for every property of every component; a speculative component library.
- Dark mode as inverted values, or a theme that was never contrast-checked.
- A button, input or card documented only in its default state.
- A rebuild of an established system the team already uses.
- Invented inventories, metrics ("saves 40% of design time"), adoption numbers, owners or review dates.

## Output discipline

Deliver the requested artifact first: the token set, the naming table, the spec, the verdict, the cleanup plan, with no history of design systems and no preamble. When a count or set is asked for, deliver exactly that (three durations, four roles) and verify it. Honor any word cap by dropping the lowest-value point, and count rather than assert. A cleanup names the merge map (old value to new token) and the migration order. After the work, at most two one-line notes (an assumption, the one trade-off), unless more is asked.

## Quick checks

- Every value in use maps to a token, or is a marked exception.
- Scale counts are within the ranges above and no two neighbors are close enough to confuse.
- Components read semantic roles; names say what and why, not where or what color.
- Each theme remaps roles; text pairs pass in each.
- Each component lists its states and edge content.
- One source, an owner, and a way to deprecate are named.

## References

- [references/token-architecture.md](references/token-architecture.md): load when writing or cleaning a token set; tiers, naming grammar, CSS and JSON formats, theme mechanics, a cleanup method.
- [references/components-and-governance.md](references/components-and-governance.md): load when specifying a component, writing the guide, or setting up change rules and rollout.
