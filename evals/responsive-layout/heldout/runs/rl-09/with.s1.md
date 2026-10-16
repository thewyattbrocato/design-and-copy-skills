# Pre-Launch Test Checklist: Dental Booking Site

Priority order: what costs you patients if it breaks comes first.

## 1. The booking flow (most important)
Test end to end, on a phone and a desktop, at least 3 times each:
- [ ] Book a new appointment with valid data and get a confirmation on screen, by email and by text (if you use them)
- [ ] The appointment appears in the office's scheduling system or calendar, with the right time, time zone, provider, and service
- [ ] Cancel and reschedule work, and the freed slot reopens
- [ ] **Double-booking:** two people try the same slot at once (two browsers, click at the same moment)
- [ ] Bad input: empty fields, a bad email or phone number, a name with an apostrophe or accent (O'Brien, José), very long text, a date in the past
- [ ] Edge cases: same-day booking, a slot at closing time, daylight saving changeover, holidays and closed days
- [ ] Back button, refresh mid-form, and double-clicking Submit don't create duplicates or lose data
- [ ] Error paths: the booking service is down or slow, and the user sees a clear message plus the office phone number
- [ ] Confirmation and reminder emails aren't going to spam (test Gmail, Outlook, and Yahoo; check SPF/DKIM/DMARC with a free tool like mail-tester.com)

## 2. Privacy and security (dental data is health data)
- [ ] HTTPS everywhere, with HTTP redirecting to HTTPS and a valid certificate
- [ ] No patient data in URLs, analytics events, console logs, or error messages
- [ ] Confirm your booking vendor, host, and email/SMS provider will sign a **HIPAA BAA** if you're in the US. Ask your lawyer or compliance contact if unsure.
- [ ] Analytics and ad pixels (Meta, Google Ads) aren't firing on booking or form pages with health details. This is a common source of HIPAA trouble.
- [ ] Cookie or consent banner meets your region's rules
- [ ] Forms have spam protection (honeypot or CAPTCHA), and rate limiting if you can add it
- [ ] Admin logins use strong passwords and 2FA, and there are no default credentials
- [ ] Run a free scan: Mozilla Observatory and SSL Labs (A-grade target)
- [ ] Privacy policy and the notice of practices are linked and accurate

## 3. Device and browser coverage on a zero budget
You don't need a lab. Cover these:
- **Your own devices:** every phone, tablet, and laptop in the office, plus staff and family. Ask 5 to 10 real patients or friends to book and send screenshots of problems.
- **Browsers on a laptop:** Chrome, Safari, Firefox, Edge. Safari matters most because all iPhone browsers use its engine.
- **Chrome DevTools device mode** (F12, then the phone icon): quick layout checks at 360, 390, 768, and 1280 px widths. It's an emulator, so it won't catch real touch or Safari bugs.
- **Free tiers:** BrowserStack Live and LambdaTest have free trials or limits. Use them for the one or two real devices you don't own (an older iPhone, a Samsung).
- **Safari on Mac** can mirror a real iPhone through Web Inspector.
- **Minimum matrix:** iOS Safari (current and one version back), Android Chrome, desktop Chrome, Safari, Edge. Check your analytics or ask the office who their patients are. Older patients may be on older devices and larger text.

## 4. Mobile and usability checks
- [ ] Most bookings will come from phones, so do the whole flow one-handed
- [ ] No horizontal scrolling at any width. Rotate to landscape too.
- [ ] Tap targets are at least 44×44 px, with space between them
- [ ] Inputs use the right keyboard (`type="tel"`, `type="email"`) and autofill works
- [ ] Date and time pickers are usable on touch screens
- [ ] Phone number is click-to-call, and the address opens maps
- [ ] Sticky headers and cookie banners don't cover the Submit button
- [ ] Browser text size set to 200% and page zoom at 200% both still work

## 5. Accessibility (legal risk and many older patients)
- [ ] Complete the booking with **keyboard only** (Tab, Shift+Tab, Enter, Space). Focus is always visible.
- [ ] Run Lighthouse (in Chrome DevTools) and axe DevTools (free extension). Fix everything critical.
- [ ] Try a screen reader for 10 minutes: VoiceOver (built into Mac and iPhone) or NVDA (free on Windows)
- [ ] Every form field has a visible label, not just placeholder text
- [ ] Error messages are specific and announced, not shown by color alone
- [ ] Text contrast is at least 4.5:1
- [ ] Target WCAG 2.1 AA

## 6. Performance
- [ ] Run PageSpeed Insights on the home page and booking page (mobile score)
- [ ] Throttle to "Slow 4G" in DevTools. The booking page should be usable in under 5 seconds.
- [ ] Compress images and test on a real phone on cellular, not just office Wi-Fi
- [ ] Third-party widgets (chat, reviews, maps) don't block the booking form

## 7. Content and SEO basics
- [ ] Hours, address, phone, insurance accepted, and prices are correct everywhere
- [ ] Every link and button works (a free crawler like Screaming Frog, up to 500 URLs, can check this)
- [ ] Custom 404 page, favicon, and page titles and meta descriptions on each page
- [ ] Google Business Profile links to the live site. Add LocalBusiness schema markup if you can.
- [ ] Make sure the staging site is not indexed and the live site is (check `robots.txt` and `noindex` tags)
- [ ] Analytics and conversion tracking record a booking, without sending patient details

## 8. Launch readiness
- [ ] Backups exist, and you've done a test restore
- [ ] Uptime monitoring is set up (UptimeRobot free tier) and alerts go to a real person
- [ ] Domain and SSL auto-renew, with a renewal reminder on a calendar
- [ ] A rollback plan: who can revert, and how, in under 15 minutes
- [ ] The front desk is trained, knows how new bookings appear, and has a fallback if the site is down (phone number visible, plus a paper process)
- [ ] Launch on a weekday morning, not Friday evening, and have the dev available for the first 48 hours
- [ ] Watch the first week of real bookings closely. Compare the site's records with the office's schedule daily.

## Suggested order for the dev
1. Booking flow and double-booking tests (a day)
2. Privacy, security, and BAA confirmations (half a day, plus waiting on vendors)
3. Real-device pass with the minimum matrix (half a day)
4. Accessibility and performance tools (half a day)
5. A patient or staff trial with 5 to 10 people, then fix what they find
6. Content and launch checklist

If you tell me the booking platform (custom, Calendly-style, or a dental-specific vendor like Dentrix or NexHealth) and your country, I can tighten the privacy and integration sections.
