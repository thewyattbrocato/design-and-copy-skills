# Pre-Launch Test Checklist: Dental Booking Site

**Priority principle:** The site exists to get patients to book. Test the booking path first, everything else second.

## 1. Core booking flow (highest priority)
Run end to end, on a phone and a desktop, as a new patient and as a returning one:
- [ ] Pick a service, date and time, then submit. Confirm the appointment lands in your scheduling system or inbox.
- [ ] Confirmation email and/or SMS arrives, isn't in spam, and has correct date, time, address, and cancel/reschedule link.
- [ ] Reschedule and cancel both work.
- [ ] Double-booking: two people try the same slot at once. Only one should succeed.
- [ ] Edge inputs: apostrophes and hyphens in names (O'Brien), `+` in emails, international phone formats, blank required fields, very long text, emoji.
- [ ] Time zones and DST: the slot shown is the slot booked.
- [ ] Error states: what does a user see if the server fails or they lose connection mid-submit? There should be a clear message and no silent failure.
- [ ] Double-click the submit button. It should not create two bookings.
- [ ] Back button and refresh mid-flow don't lose data or duplicate submissions.

## 2. Device and browser coverage (no lab needed)
**Free options:**
- **Your own devices:** every phone, tablet, and laptop in the office, plus staff and family phones. Aim for at least one iPhone, one Android, and one desktop browser each of Chrome, Safari, and Firefox/Edge.
- **Browser dev tools:** Chrome/Edge DevTools device mode (Cmd/Ctrl+Shift+M) for layout at common sizes (360, 390, 768, 1280 px). It simulates screens, not real browser engines, so treat it as a first pass.
- **Safari matters:** iOS Safari is the most common source of "works on my machine" bugs (form inputs, date pickers, 100vh, autofill). Test on a real iPhone if at all possible.
- **Free tiers of cloud testing:** BrowserStack and LambdaTest have free trials or open-source plans. Use them for a one-time sweep of older iOS/Android versions.
- **Analytics-driven scope:** if you have an existing site, check which browsers and devices your current visitors use, and prioritize those.

**What to look for:** layout breaks, text cut off, tap targets too small, sticky headers covering form fields, keyboard covering inputs, date/time pickers behaving oddly, and horizontal scrolling.

## 3. Performance (mobile, on a slow connection)
- [ ] Run **Lighthouse** (in Chrome DevTools) and **PageSpeed Insights** on the home page and booking page. Target mobile performance ≥ 80 and LCP under 2.5 s.
- [ ] Throttle to "Slow 4G" in DevTools and complete a booking.
- [ ] Compress images and set explicit image dimensions to avoid layout shift.
- [ ] Check that third-party scripts (chat widgets, trackers, maps) aren't blocking the page.

## 4. Accessibility
Dental patients skew older, and accessibility is also a legal exposure (ADA lawsuits against small practices' sites are common).
- [ ] Complete the whole booking flow using **only the keyboard** (Tab, Shift+Tab, Enter, Space). Focus must be visible and in a logical order.
- [ ] Run **axe DevTools** (free extension) and Lighthouse accessibility audits, then fix every issue they flag.
- [ ] Every form field has a visible label (not placeholder-only), and errors are announced in text, not by color alone.
- [ ] Color contrast meets WCAG AA (4.5:1 for body text).
- [ ] Zoom to 200% and on mobile bump system font size. Nothing should break or overlap.
- [ ] Quick screen reader pass: VoiceOver (built into Mac/iPhone) or TalkBack (Android) on the booking flow.

## 5. Privacy, security, and compliance
This is the section most often skipped, and it matters most for a healthcare business.
- [ ] **HTTPS** everywhere, with HTTP redirecting to HTTPS and a valid certificate (check with SSL Labs).
- [ ] **HIPAA:** if the form collects anything health-related (reason for visit, symptoms, insurance, medical history), you are likely handling PHI. Confirm that your form tool, email delivery, hosting, and scheduling vendor will sign a **BAA**. Plain email, Google Forms, and most free form plugins will not. Ask your compliance contact or attorney if unsure.
- [ ] Don't put PHI in emails or SMS notifications. Keep them to "You have an appointment on X at Y."
- [ ] No sensitive data in URLs or analytics. Check that Google Analytics, Meta Pixel, and similar trackers aren't capturing form contents or page URLs that reveal health info. This is a known enforcement area.
- [ ] Cookie/consent banner and privacy policy are in place and accurate.
- [ ] Basic security: rate limiting or CAPTCHA on forms (to prevent spam bookings), server-side validation (not just browser-side), and no admin pages or API keys exposed. Test by submitting a form with the browser's JavaScript disabled, or by editing the request.
- [ ] Spam: submit the form 20 times quickly. Check that it doesn't flood the schedule.

## 6. Content and local-business basics
- [ ] Phone numbers are tap-to-call links (`tel:`) on mobile.
- [ ] Address links open maps. Hours, insurance accepted, and emergency instructions are correct.
- [ ] Every link and button works (use a free link checker like Broken Link Checker).
- [ ] Proofread everything, including doctor names and credentials.
- [ ] Custom 404 page and a visible fallback ("Can't book online? Call us at…").
- [ ] Page titles, meta descriptions, favicon, and social share preview look right.
- [ ] Google Business Profile points to the new URL, with the same name, address, and phone as on the site.

## 7. Operational readiness
- [ ] Staff know where bookings arrive, who checks them, and how fast they respond.
- [ ] Do a **dry run with real staff** booking real-looking appointments, then delete the test data.
- [ ] Set up **uptime monitoring** (UptimeRobot free tier) and a **form-failure alert**, so you hear about a broken form before patients do.
- [ ] Set up analytics with a **booking-completed** event so you can see where people drop off.
- [ ] Confirm backups exist and that someone has the hosting/domain/DNS logins.
- [ ] Have a rollback plan: know how to revert to the previous site or switch to a "call us to book" page within minutes.
- [ ] Check that email deliverability is configured (SPF, DKIM, DMARC) for confirmation emails.

## 8. Suggested order for a part-time dev
1. **Day 1:** Booking flow on real phone and desktop, plus error and edge cases (Sections 1 and 7 dry run).
2. **Day 2:** Privacy and security review (Section 5), because these items can force changes to vendors or tooling.
3. **Day 3:** Cross-browser and device pass, accessibility, and performance fixes (Sections 2–4).
4. **Day 4:** Content sweep, monitoring, final dry run, then launch (Sections 6–7).

**Launch-day tip:** Launch early in the week and during office hours, so someone is there to catch problems. Keep the old booking method (phone) available for the first couple of weeks.

If you tell me what the site is built on (WordPress, Squarespace, a custom app, a third-party scheduler like Zocdoc or NexHealth), I can tailor this. For example, which items are the vendor's responsibility and which are yours.
