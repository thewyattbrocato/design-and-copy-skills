Yes, she's right. The page reads as generated within a second, before anyone reads a word. The one piece that's good is the feature copy: "Send sheet music and practice tracks," "who needs help before the big night." That's specific to choirs, and everything around it hides it.

## What gives it away, worst first

1. **The wording would fit any SaaS product.** This one hurts most with music teachers.
   - The headline "Supercharge your choir with intelligent rehearsals" and the subhead "all-in-one platform that empowers directors to streamline…" are stock phrases. "Supercharge," "intelligent," "empowers," "streamline" and "focus on what matters most" are the vocabulary of generated copy.
   - The headline doesn't name what a director gets: parts out, attendance taken, and a list of who hasn't learned their part before the concert.
   - "Lightning-fast," "Effortlessly" and "Smart attendance" are the same kind of filler.
2. **"Trusted by 1,800+ choirs worldwide" is a problem beyond looks.**
   - You have 38 pilot schools. If that number isn't true, remove it today. A director who asks around and finds out will stop trusting everything else on the page.
   - If it's true, show where it comes from. Otherwise say "38 schools in our pilot." That number is small, but it's real and specific.
3. **Glow and gradient everywhere.** Light is doing the work that design choices should do.
   - A blurred purple blob sits behind the hero (`bg-purple-600/30 blur-3xl`).
   - The headline text is clipped to a white→purple→pink gradient (`bg-clip-text`).
   - The primary button is a gradient with a purple glow (`shadow-purple-500/40`).
   - The cards are frosted glass (`bg-white/5 backdrop-blur`).
   - The icon tiles are indigo→pink gradients.
4. **Unchosen defaults.**
   - The indigo/purple/pink palette on slate-950 is what a generator reaches for. Nothing in it comes from choirs, paper, or scores.
   - The layout is the stock one: centered stack, pill badge, two buttons, then three equal cards.
   - Each card has an icon in a tinted square above the title.
   - The icons are arbitrary: a lightning bolt for sheet music, sparkles for attendance, a shield for insights. None of them means what it labels.
5. **A badge that makes a claim without proof.** "AI-powered choir management" in a sparkle pill. Unless AI really is central to the product, it's a weak lead for teachers, and some are skeptical of it. Your actual pitch is that it saves time at the start of rehearsal and before concerts.
6. **Everything is turned up.** There's one pill, one gradient headline, one gradient button, one glow and three gradient icons, so nothing is the focal point. Two buttons also compete, "Get started free" and "Book a demo."
7. **The hover lift (`hover:-translate-y-1`) is on cards that don't click.** It's a small thing, but it's another default.
8. **Nothing shows the product.** There's no part list, no attendance roll, and no "14 of 62 haven't learned Alto II." Your best material is what the screens actually show, and the page has none of it.

## What I'd change first

Do these in order, and stop wherever the page feels right.

1. **Rewrite the words.** It costs nothing, and it fixes the thing she's embarrassed about.
   - Write the headline for a director. For example: "Know who's learned their part before the concert." Put handing out parts and taking attendance underneath as supporting lines.
   - Cut the AI pill, or replace it with something true like "Used in 38 school choirs."
   - Fix or remove the 1,800 claim.
2. **Replace the dark purple-glow look with something drawn from the subject.** Use a light, paper-like ground, ink-dark text, and one accent chosen on purpose. A serif or text face for headlines fits music. Drop the blob, the gradient text, the blur and the glows.
3. **Show the product in place of the three icon cards.** Put a small, accurate rendering of a section roster or attendance sheet in the hero, with plausible sample names marked as sample. A director recognizes that immediately.

I haven't restyled any code, since you asked for a diagnosis. If you'd like, I can do the rewrite and restyle of this component, keeping the content and section order. Two things I'd need from you first: is the 1,800 figure real, and do you already have brand colors or a logo?
