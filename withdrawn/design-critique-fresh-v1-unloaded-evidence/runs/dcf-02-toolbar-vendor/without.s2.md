**I wouldn't buy it.** The claims in that email don't hold up.

**Why not**
- **No toolbar makes a site compliant.** Compliance means the underlying pages work with keyboards, screen readers and zoom. A script layered on top can't reliably fix missing alt text, unlabeled form fields, broken focus order or an inaccessible checkout.
- **Regulators have pushed back on this exact pitch.** In 2025 the FTC fined a leading overlay vendor, accessiBe, $1M for deceptive claims that its tool made sites compliant. Sites running overlays are also still sued regularly. Plaintiffs' lawyers often see an overlay as a sign the site hasn't been fixed.
- **Overlays can make things worse.** Many screen-reader users find them intrusive, and they can conflict with the assistive tech people already use. Some disability advocacy groups actively campaign against them.
- **"Legal protection included" is probably thin.** Ask for the contract language. It's usually a limited indemnity with conditions, caps or exclusions, or it's just marketing copy. Don't rely on it without a lawyer reading it.

**What I'd do instead, with you and the freelancer**
1. **Run free scans** on your homepage, a category page, a product page, cart and checkout. Use WAVE, axe DevTools or Lighthouse. They catch only about a third of issues, but they find the obvious ones.
2. **Test by hand.** Try the whole purchase flow using only the Tab, Enter and Space keys. Zoom the browser to 200%. Turn on VoiceOver (Cmd+F5 on a Mac) for ten minutes.
3. **Fix the common problems.** For a shop your size, these are usually:
   - Alt text on product images (the freelancer can do all sixty pages).
   - Color contrast.
   - Form labels and error messages.
   - Visible keyboard focus.
   - Descriptive link and button text.
   - Heading structure.
   - Captions or transcripts for any video.
4. **Check your platform and theme.** Hosted platforms like Shopify and BigCommerce publish accessibility info, and some themes are much better than others. Switching to an accessible theme may fix a lot at once. Ask your platform's support what they cover.
5. **Add an accessibility statement** with a way to reach a real person, such as an email or phone number. Reply to those messages quickly.
6. **Keep a record** of what you tested and fixed, and when. That shows good faith if a demand letter ever arrives.

If you want something to point to, aim for WCAG 2.1 AA. If you're worried about legal exposure, an hour with a lawyer who handles ADA cases is better value than $588 a year for a widget. It's also worth asking your business insurer what's covered.

The sixty product pages are a small site, so this is very doable without a developer. If you tell me your platform, I can suggest where to look for its accessibility settings and theme options.
