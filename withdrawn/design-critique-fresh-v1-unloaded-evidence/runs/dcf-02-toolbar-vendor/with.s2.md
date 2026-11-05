**I wouldn't buy it.** Overlay toolbars like this don't deliver what the pitch promises.

**Why the claims don't hold up**
- **"Fixes your site automatically":** Automated tools can catch only a portion of accessibility problems. They can't write meaningful alt text for your bike photos, fix a confusing keyboard flow, or make a size-chart table usable with a screen reader. Many overlays also interfere with the assistive tech people already use.
- **"Compliant":** No plugin can make you compliant. Compliance is about how your site actually works for people, usually measured against WCAG 2.1 AA.
- **"Protects from lawsuits":** Sites running overlays still get sued, and plaintiffs' lawyers often cite the overlay as evidence of known problems. The FTC fined one of the largest overlay vendors (accessiBe) in early 2025 for misleading compliance claims. "Legal protection included" is the line to be most skeptical of. Ask for the contract and see what it actually covers. It's usually far narrower than the email implies.
- **"Trusted by thousands":** That tells you about their sales, not whether it works. Many accessibility professionals and disability advocacy groups publicly oppose overlays.

I haven't looked at this specific vendor's product or contract, and I'm not a lawyer. If legal exposure worries you, a short consult with an attorney who handles ADA web cases is worth more than $588 a year on a widget.

**What I'd do instead (doable with you plus a part-time freelancer)**
1. **Check your theme.** On a hosted platform, a well-built, current theme gets you much of the baseline: semantic structure, focus states, and so on. Fixing a bad theme matters more than adding anything on top.
2. **Run free scans** on your homepage, a category page, a product page, cart, and checkout. Use WAVE, axe DevTools, or Lighthouse. Fix what they flag, especially low color contrast, missing form labels, and unlabeled buttons or links.
3. **Do the manual basics, which a scan can't catch:**
   - Write real alt text for product images. This is tedious across sixty pages, but it's a good job for your freelancer.
   - Try tabbing through the site with only your keyboard, including the full checkout.
   - Make sure videos have captions and that text can be resized.
4. **Publish an accessibility statement** with a contact email or phone, and respond promptly if someone reports a problem. Good-faith effort and a responsive contact path count for a lot.
5. **If you want outside help,** a one-time professional audit of your key templates (home, product, cart, checkout) is often a few hundred to a couple thousand dollars. It gives you a prioritized fix list, which is more useful than a subscription.

Also check whether your platform's checkout is already accessible. Hosted checkouts often are, which means your main work is the storefront pages and product content.

If you tell me which platform you're on, I can suggest where to look for theme and checkout accessibility details.
