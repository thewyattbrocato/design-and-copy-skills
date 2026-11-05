**No, I wouldn't buy it as your accessibility solution.** It won't deliver what the email promises.

**Why not**
- **Overlays don't make a site compliant.** A script that runs in the visitor's browser can't reliably fix missing alt text, broken keyboard navigation, unlabeled form fields, or a confusing checkout. Those problems live in your content and your theme.
- **The FTC has acted on claims like this one.** In January 2025 it fined accessiBe $1 million for misrepresenting that its tool made sites WCAG-compliant. "One line of code, fixes it automatically" is the kind of claim regulators and plaintiffs' lawyers distrust.
- **Overlays haven't prevented lawsuits.** Sites running them are still sued, and the overlay is sometimes cited in the complaint. Many blind users also find these tools get in the way of the screen readers they already use.
- **"Legal protection included" is vague.** Ask for the contract language. Usually it's a limited indemnity with conditions, or just marketing. It's very unlikely to cover your legal costs or a settlement.
- **"Trusted by thousands of stores" is not evidence of compliance.** It only tells you they sell a lot of subscriptions.

**What I'd do instead with your size and budget**
1. **Run free audits.** Use WAVE (wave.webaim.org), the axe DevTools browser extension, and Lighthouse on your home page, a category page, a product page, the cart, and checkout. Those five templates cover most of your sixty pages.
2. **Check your platform and theme first.** Hosted platforms often have accessibility-ready themes, and fixing the template once fixes every product page.
3. **Have the freelancer fix the common problems:**
   - Add alt text to product images. Sixty pages is a manageable amount.
   - Fix low-contrast text and buttons.
   - Make sure everything works by keyboard alone, with a visible focus outline.
   - Label form fields and use descriptive link text.
   - Add captions to any videos.
4. **Test the purchase path yourself.** Go from product to checkout using only the keyboard, then try a screen reader (VoiceOver is built into your Mac).
5. **Publish a short accessibility statement** with an email or phone number for people who hit problems, and respond to them promptly.
6. **Consider a one-time manual audit.** It usually costs far less than years of subscription fees and gives you a documented list of fixes.

Your target is WCAG 2.1/2.2 AA. Nobody can promise lawsuit immunity, but a documented good-faith effort with real fixes puts you in a much stronger position than an overlay does. If you sell to the EU, the European Accessibility Act has applied to online shops since June 2025, so real fixes matter even more.

**If you still want to talk to the rep, ask:**
- Will you put the legal protection in writing, and what exactly does it cover?
- Does it fix problems in the source code, or only change the page in the browser?
- Will you guarantee WCAG AA conformance in the contract?

I expect vague answers. If they do guarantee it in writing, that would change my view, but I doubt they will.

I can draft an audit checklist for your freelancer or an accessibility statement if you'd like.
