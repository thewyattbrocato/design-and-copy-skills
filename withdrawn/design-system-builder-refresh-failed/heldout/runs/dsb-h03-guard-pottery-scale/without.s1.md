No, you don't need that. A component library with versioning, a docs site and a review board is built for many teams shipping many products. With two people and one 12-page site, it would eat your whole budget and give you almost nothing back. You do need a *small* design system, though. Here's what that looks like in a day or two.

**Do this (about 1.5 days)**

1. **Design tokens (2–3 hours).** Put these in one file, either CSS custom properties or a Tailwind config:
   - Colors: 1 brand color, 1 accent, neutrals, and success/error. Pick a warm, earthy palette that suits a pottery studio.
   - Type: 2 fonts at most, plus a size scale of about 6 steps.
   - Spacing: a 4 or 8px scale.
   - Radius and shadow: 2–3 values each.

   This gives you most of the consistency you need, and it's what lets you and the contractor work without stepping on each other.

2. **A short list of core components (4–6 hours).** Build only what the booking site needs:
   - Button (primary, secondary, and a text-link style)
   - Form inputs: text, select, date picker, and error states
   - Card (for classes and workshops)
   - Nav and footer
   - Modal or dialog, if the booking flow uses one
   - Section and container layout helpers

   Build them in the real codebase as normal components. Don't build a separate library package.

3. **Design the 3–4 key pages first (3–4 hours).** These are the home page, the class listing, the booking flow, and the confirmation page. Design them in Figma, or straight in the browser if that's faster for you. Pull out any component you use twice. Let the rest of the pages follow from those.

4. **A one-page README (1 hour).** Cover the tokens, the component list, naming conventions, and "how to add a new component." Your contractor will actually read it, which is the only audience a docs site would have here.

5. **A lightweight review habit.** Open PRs and have the other person look at anything that touches tokens or shared components. Skip any formal board.

**Skip for now**
- Separate package publishing and semantic versioning. Git history is enough.
- A Storybook or docs site. Add Storybook later only if the component count grows and you want a visual catalog. It's optional even then.
- Governance and review boards. Your "board" is the two of you talking.
- Over-engineered variants. Build a variant when a real page needs it.

**Plan for the second site**
Keep the tokens and shared components in a clearly separated folder, such as `/styles/tokens` and `/components/ui`, apart from booking-specific code. Next year, when the classes site comes up, you can copy that folder over or move it into a shared package. At that point you'll know what's actually reusable. Extracting it now means guessing.

**When to revisit**
Reconsider a fuller system if you add more people, if you end up running three or more sites, or if you notice the two sites drifting apart visually and it's costing real time. None of those apply today.

If you tell me your stack (React, Next, plain HTML/CSS, Tailwind?), I can sketch the token file and folder structure for you.
