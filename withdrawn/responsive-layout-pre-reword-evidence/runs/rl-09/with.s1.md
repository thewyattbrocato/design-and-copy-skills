# Pre-launch test checklist: dental booking site

Priority order: the first sections protect revenue and patient trust. Do them first.

## 1. Core booking flow (most important)
Run end to end, on a phone and a desktop, as a brand-new patient and as a returning one.
- [ ] Book, confirm, and receive the confirmation email/SMS. Check spam too.
- [ ] Reschedule and cancel. Confirm the slot reopens.
- [ ] Double-booking: two browsers try to book the same slot at once. Only one should succeed.
- [ ] Edge inputs: apostrophes and hyphens in names (O'Brien), `+` in emails, international phone formats, and a blank optional field.
- [ ] Time zones and daylight saving: the displayed time matches the office's local time. Test a booking across a DST change date.
- [ ] Error states: a taken slot, a network drop mid-submit, a double-click on Submit (should not create two bookings), and back-button behavior.
- [ ] Emergency and same-day paths: a clear phone number and a click-to-call link.
- [ ] Hand it to 2–3 real people (staff, a parent, someone over 60) with no instructions. Watch where they hesitate. This finds more problems than any tool.

## 2. Devices and browsers on a zero budget
- **Real devices you already have:** staff phones, family phones, and an old tablet. Cover at least one iPhone, one Android, and one desktop each of Chrome, Safari and Edge.
- **Free emulation:** Chrome DevTools device mode (Cmd/Ctrl+Shift+M) for sizes and throttling. It does not replace real Safari on iOS, so test on a real iPhone at least once.
- **Free cloud testing:** BrowserStack Live and LambdaTest have free trials or free tiers for open-source use. Use them for a short pass on the oldest iOS and Android versions you can find.
- **Analytics-driven:** if the old site has analytics, test the top 5 browser/device combos from it. Otherwise assume iOS Safari and Android Chrome dominate.
- Check at 320px wide, in landscape, and with browser zoom at 200%.
- Test the date picker, keyboard behavior (the right keyboard for the email and phone fields), and autofill.

## 3. Performance
- [ ] Run Lighthouse (in Chrome DevTools) on the home page and the booking page, on mobile settings. Aim for 80+ on performance.
- [ ] Test on throttled "Slow 4G". Booking must be usable.
- [ ] Compress images and check for layout shift while loading.
- [ ] Run [PageSpeed Insights](https://pagespeed.web.dev), which gives real-world data once there's traffic.

## 4. Accessibility
Dental patients skew older, and accessibility lawsuits against small practices do happen.
- [ ] Complete the entire booking flow using only the keyboard (Tab, Enter, Space, Esc). Focus should always be visible.
- [ ] Run axe DevTools (free extension) or Lighthouse accessibility on every page. Fix all critical issues.
- [ ] Check that every form field has a visible label and that error messages are specific and announced.
- [ ] Contrast of at least 4.5:1 for text. Body text should be 16px or larger.
- [ ] Try the flow once with VoiceOver (Mac/iOS) or TalkBack (Android).
- [ ] Don't rely on color alone, and make sure nothing times out too quickly.

## 5. Security and privacy (health-adjacent data)
- [ ] HTTPS everywhere, with HTTP redirecting to HTTPS and a valid certificate (test at ssllabs.com).
- [ ] Don't collect more than you need. Avoid asking for symptoms or insurance details in the open form unless required.
- [ ] If the site stores or transmits patient health information, check HIPAA obligations (if you're in the US). That means a signed BAA with your booking vendor, host and email/SMS provider. Ask a compliance professional if unsure. This is the one item not to guess on.
- [ ] Confirm that confirmation emails and SMS don't include treatment details.
- [ ] Spam protection (honeypot or CAPTCHA) on forms, and rate limiting on booking and login.
- [ ] Basic test: try `<script>alert(1)</script>` in every text field. Nothing should execute.
- [ ] Confirm admin pages require login, that there are no default passwords, and that error pages don't show stack traces.
- [ ] Run a free scan with Mozilla Observatory or securityheaders.com.
- [ ] Cookie banner and privacy policy, if required in your region.

## 6. Content and SEO
- [ ] Verify the address, phone, hours, insurance list and holiday closures on every page. Compare them to Google Business Profile.
- [ ] Click every link and button. Test the contact form and phone links.
- [ ] Check the page titles and meta descriptions, a `robots.txt` that **doesn't** block the whole site (a common launch mistake), and a sitemap.
- [ ] Remove staging noindex tags and test content.
- [ ] Set up redirects from old URLs if you're replacing an existing site.
- [ ] Check the 404 page.
- [ ] Add local business structured data (Schema.org `Dentist`) and test it with Google's Rich Results Test.

## 7. Operations and launch readiness
- [ ] Check that notifications reach the right staff inbox and that someone owns replying to them.
- [ ] Set up uptime monitoring (UptimeRobot free tier) and error tracking (Sentry free tier).
- [ ] Set up analytics with conversion tracking on "booking completed".
- [ ] Take a backup and do a test restore.
- [ ] Prepare a rollback plan and know who to call if the site goes down. Also decide the fallback: "call us" must always work.
- [ ] Test the DNS, www and non-www versions, and email deliverability (SPF/DKIM/DMARC, using mail-tester.com).
- [ ] Launch early in the week and during office hours, not on a Friday evening.
- [ ] Watch the first 48 hours: real bookings, form errors, and the first calls from confused patients.

## Suggested time budget
For a part-time dev, a realistic split is about 40% on section 1, 25% on sections 2–3, and the rest on sections 4–7. If time runs out, cut from the bottom of sections 3 and 6, never from 1 or 5.

If you tell me what platform the site is built on (WordPress, Squarespace, a custom stack, or a vendor like Zocdoc or NexHealth), I can tailor this. For example, I can drop checks that the vendor already covers and add the ones they commonly miss.
