Your cofounder is right. The page reads like a generic SaaS template, and a boatyard manager can't tell from it what Slipway does or why it's for them. Here's what's causing the "off" feeling.

**1. The copy could describe any product.** "Work smarter, not harder," "all-in-one platform," "unlock their full potential," and "streamline their workflow" are filler. Boatyard owners are practical people who've probably been burned by software that promised too much. Lead with the specific problem: the travel lift is double-booked, a launch slips because nobody knew the boat was ready, and the phone is ringing all morning.

**2. The features are adjectives, not capabilities.** "Powerful," "Simple," and "Secure" give no reason to believe anything. "Built with cutting-edge technology" is a red flag for this audience. Name the things Slipway actually does:
- See every haul-out, launch, and yard move on one schedule
- Assign the travel lift and crew, and catch conflicts before they happen
- Tell customers when their boat is coming out or going in

**3. The testimonial undermines trust.** "John Doe, CEO at Acme Inc." is an obvious placeholder, and it's the first thing a skeptical buyer will notice. Until you have a real quote from a real yard, remove the section rather than fake it. A specific, real line from a yard manager does more than any feature grid.

**4. The CTA claims something you may not be able to back up.** "Join thousands of happy customers" is a strong claim. If it's not literally true, cut it. It's also a credibility problem if the number is small.

**5. Three different asks compete.** The page says "Get Started," "Learn More," and "Sign Up Free," and "Sign Up Free" appears only at the bottom. Pick one primary action and make it consistent. Consider a second, lower-commitment action such as "See how a haul-out schedule works."

**6. There's no picture of the product.** For a scheduling tool, a screenshot or short clip of the yard schedule is the single most persuasive element. Right now the page has no evidence the product exists.

**7. Some accessibility and markup issues.** The `<a>` tags have no `href`, so they aren't keyboard-focusable and won't behave as links. Give them real hrefs (`href="#"` as a placeholder is fine for now). Wrap the main content in `<main>`.

**A direction for the hero** (adjust to your real positioning):

```html
<section class="hero">
  <h1>Know where every boat is in the yard.</h1>
  <p>Slipway puts haul-outs, launches, and travel lift time on one schedule, so your crew knows what's next and customers get an honest pickup date.</p>
  <a class="btn" href="#signup">Start your yard's schedule</a>
  <a class="btn-secondary" href="#demo">See a sample week</a>
</section>
```

The main test for every line: could a competitor say this word for word? If yes, make it more specific to boatyards.

If you tell me what Slipway does today (whether it's live, in beta, or pre-launch) and whether you have any real customers or pilot yards, I can rewrite the features and CTA section to match what you can honestly claim.
