**No, I wouldn't buy it as a compliance or lawsuit-protection measure.** I'm not a lawyer, but the claim doesn't hold up.

**Why the pitch doesn't work**
- **No script can make a site compliant.** Automated engines can only detect and fix a minority of WCAG problems, roughly a third by common estimates. Things like meaningful alt text, logical reading order, clear form errors and a keyboard-usable checkout need a person to get right.
- **The toolbar part adds little.** Text size, contrast and spacing controls duplicate what browsers and operating systems already do. Users who need them usually have them set up already.
- **The "automatic rewrite" part is the risky one.** Overlays that patch the page in the browser often conflict with the screen readers and keyboard setups that disabled users rely on. Many users and advocacy groups actively dislike them.
- **It doesn't protect you from lawsuits.** Businesses running overlays have still been sued, and plaintiffs' lawyers often treat an overlay as a sign the site has underlying problems. The FTC also took action against a leading overlay vendor, accessiBe, in early 2025 over deceptive claims that its product made sites compliant. Check the current details yourself, but "this makes you compliant" is exactly the kind of claim regulators have called misleading.

**What I'd do with the $49 a month, and more, instead**
1. **Check your platform first.** Hosted shops often have accessibility settings or themes that are already decent. Ask your platform what WCAG 2.1/2.2 AA support they offer.
2. **Run free automated checks** (axe DevTools, WAVE, Lighthouse) on the key pages: home, a category page, a product page, cart and checkout.
3. **Test by hand.** Put your mouse aside and tab through a purchase. Turn on VoiceOver (Mac) or NVDA (Windows, free) and try the same flow.
4. **Fix the common problems.** These are missing or useless alt text on product images, unlabeled form fields, low contrast, missing focus outlines, and unclear error messages. With sixty pages, most of this is template-level and not sixty separate fixes.
5. **Consider a one-time professional audit** of the templates and checkout if you can afford it. It's often cheaper than a year of an overlay, and it gives you documentation of good-faith effort.
6. **Publish an accessibility statement** with a contact method for reporting problems, and respond to reports promptly.

If you want legal assurance, talk to a lawyer who handles ADA cases. A vendor's one-pager isn't a substitute.

I can also draft questions to put to the sales rep, or help you build a checklist for the audit. Good questions for the rep would be whether they'll guarantee compliance in writing and indemnify you, and what happens to your pages if the script fails to load.
