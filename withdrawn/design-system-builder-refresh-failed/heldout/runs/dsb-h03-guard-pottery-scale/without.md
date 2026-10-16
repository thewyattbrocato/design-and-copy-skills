No, you don't need that. A component library with versioning, a docs site and a review board is built for many teams shipping many products. For two people, one 12-page site and a maybe-later second site, it would eat the time you should spend building the booking flow.

What you need is a lightweight design foundation. You can do it in a day:

**1. Design tokens (1-2 hours)**
Put these in one CSS file of custom properties, or in your Tailwind config if you use it:
- Colors: a brand palette, neutrals, and semantic colors (error, success, focus)
- Type: 1-2 font families and a size scale of about 6 steps
- Spacing: a scale such as 4/8/12/16/24/32/48/64
- Radius, shadow and breakpoints

This is the part that will carry over to the classes site. Both sites can import the same file.

**2. A small set of real components (3-4 hours)**
Build only what the booking site needs:
- Button (primary, secondary, disabled)
- Form fields (text, select, date, error state)
- Card (class or session listing)
- Nav and footer
- Modal or dialog, if the booking flow uses one

Build them in your actual codebase, in whatever framework you're using. Don't build them in a separate package. A `components/` folder is enough. If the classes site happens next year, extract what you need then, when you know what is actually shared.

**3. One page of conventions (1 hour)**
A single README or Notion page covering:
- Where the tokens live and the rule "don't hard-code colors or spacing"
- Naming conventions
- How to add a new component
- Link to the Figma file

This is what keeps you and the contractor consistent. It's your docs site.

**4. Figma setup (1-2 hours)**
Use Figma variables for the same tokens, and build the same components in Figma. Name them to match the code.

**5. Review process**
Skip the board. Use pull requests: the contractor reviews your work and you review theirs. Add a rule that any new UI goes through the existing components first. That's all the governance you need.

**What to skip for now:**
- A separate versioned package
- Storybook or a docs site (you can add Storybook later if the component count grows)
- Formal contribution and review processes

**When to revisit:** when the second site starts, or when you notice you're rebuilding the same thing twice. At that point, pull the shared tokens and components into a shared package. By then you'll know what belongs in it.

Your friend isn't wrong that design systems matter. The mistake is the scale. You need the small version of one, and you can build it as you go.

If you tell me your stack (React, Next, plain HTML/CSS, Tailwind?), I can help set up the token file and a starter component structure.
