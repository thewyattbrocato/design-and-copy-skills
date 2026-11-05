**No, I wouldn't buy it as a compliance or lawsuit-protection measure.** The rep's pitch is the part to distrust.

**Why the pitch doesn't hold up**
- **No script can make a site compliant.** An automatic engine can't reliably write meaningful alt text for your bike photos, fix a confusing checkout flow, or repair keyboard traps and unlabeled form fields. It also can't tell whether a screen reader user can finish a purchase. Automated tools of any kind catch only a minority of real accessibility problems.
- **Overlays often don't prevent lawsuits.** Plaintiffs' firms regularly sue sites that already run overlays, and the overlay's presence doesn't count as a defense. In January 2025 the FTC fined one of the biggest overlay vendors, accessiBe, $1M for deceptive claims that its tool made sites compliant. "Compliant and protected from lawsuits" is exactly the kind of claim regulators have gone after.
- **The toolbar features are mostly redundant.** Text size, contrast and spacing controls duplicate what browsers and operating systems already do, and people who need them have usually set them up already.
- **Overlays can make things worse.** Screen reader and keyboard users often report that these scripts conflict with their own assistive tools. Many of them dislike overlays and say so publicly.

**What I'd do with the $588 a year, and more**
1. **Test your key paths by hand.** Use only a keyboard, then a screen reader (VoiceOver on a Mac is free), on the home page, a category page, a product page, the cart and checkout. This usually surfaces the worst problems quickly.
2. **Run free scanners** such as axe DevTools, WAVE or Lighthouse on a sample of pages. Sixty pages is small enough to cover the templates (product, category, cart, checkout, content) and fix issues at the template level.
3. **Fix the common problems:**
   - Alt text on product images.
   - Color contrast.
   - Visible focus outlines.
   - Labeled form fields.
   - Descriptive link and button text.
   - Captions or transcripts for any videos.
4. **Check your platform.** Ask your host whether your theme is accessibility-tested, and consider switching to a better theme. Also check that the payment widget is keyboard-usable.
5. **Consider a one-time professional audit** of the main purchase flow, which often costs a few thousand dollars. It gives you a real remediation list, and a documented good-faith effort helps if you ever receive a demand letter.
6. **Publish a short accessibility statement** with a contact email or phone number for people who hit barriers, and respond when they do.

If you've already received a demand letter, or you're worried about legal exposure, talk to a lawyer who handles ADA web claims. I can't give legal advice, but I can say that fixing the site is a stronger position than owning a widget.

If you want, I can help you build a checklist for the audit, or review your theme's HTML for common issues if you can share the files.
