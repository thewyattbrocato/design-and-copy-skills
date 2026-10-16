# Pre-launch test checklist: dental booking site

**Priority:** The booking flow is the product. If someone can't book, nothing else matters. Test it deeply on a few browsers rather than shallowly on many.

## 1. Free "device lab"

| Need | Free option |
|---|---|
| Real phones | Staff, family and patients' own phones. Aim for at least 1 iPhone, 1 Android (Chrome), and 1 older/cheap phone. |
| Layout at many sizes | Chrome/Edge DevTools device toolbar (Cmd+Shift+M). Test 360px, 390px, 768px and 1280px wide. |
| Safari/iOS engine | Safari on any Mac, or Playwright's WebKit build (free). iOS Safari is the most common source of "works on my machine" bugs. |
| Other browsers | Firefox and Edge, installed locally. |
| Anything else | BrowserStack or LambdaTest free trials or free tiers. Use them for a one-time spot check, not as the main plan. |
| Slow network | DevTools → Network → "Slow 4G" and CPU 4x slowdown. |

DevTools emulation checks layout, not real touch or keyboard behavior. Do at least one full booking on a real iPhone and a real Android phone.

## 2. Booking flow (the critical path)

Run each of these on mobile and desktop:

- [ ] New patient books, with each appointment type offered.
- [ ] Existing patient books.
- [ ] Booking appears in the practice's scheduling system or calendar, with the correct time, provider and service.
- [ ] Confirmation email and/or SMS arrives. Check the spam folder in Gmail, Outlook and iCloud.
- [ ] Reschedule and cancel work, and the slot is freed.
- [ ] Two people can't book the same slot (open two browsers and submit at the same time).
- [ ] Time zones and daylight saving time: slots display in the office's local time even if the visitor's device is set elsewhere. Test a booking across a DST change date.
- [ ] Closed days, holidays, lunch blocks and lead-time rules (e.g. no same-day booking after 3pm) are enforced.
- [ ] Back button, refresh mid-flow and closing the tab don't lose data or create duplicate bookings.
- [ ] Double-clicking Submit creates only one booking.
- [ ] Server errors show a friendly message with the office phone number, not a blank page.
- [ ] The site has a phone fallback ("Call us") that is a tappable `tel:` link.

## 3. Forms and input

- [ ] Names with apostrophes, hyphens, accents and spaces (O'Brien, José, Mary-Jane).
- [ ] Phone formats: `(555) 123-4567`, `555-123-4567`, `+1…`.
- [ ] Email typos and plus-addressing (`a+b@gmail.com`).
- [ ] Date of birth entry, including the date picker on iOS.
- [ ] Autofill works (browser and password-manager autofill of name, email, phone).
- [ ] Correct mobile keyboards (`type="email"`, `type="tel"`, `inputmode`).
- [ ] Error messages sit next to the field and say how to fix it.
- [ ] Spam protection (honeypot, rate limit, or CAPTCHA) is on, and real users aren't blocked by it.
- [ ] Insurance and reason-for-visit fields are optional where possible.

## 4. Privacy, security and compliance

Do not skip this section, because it's dental data.

- [ ] HTTPS everywhere. HTTP redirects to HTTPS, and there are no mixed-content warnings.
- [ ] **HIPAA check:** confirm with whoever owns compliance which vendors (hosting, form tool, scheduler, email/SMS, analytics) will touch patient information. Each one that does needs a signed BAA.
- [ ] Don't put health details (symptoms, procedures) in URLs, analytics events, or plain unencrypted email bodies.
- [ ] Analytics, Meta Pixel and ad tags don't receive form contents or appointment details. Check the Network tab during a booking.
- [ ] Privacy policy and notice of privacy practices are linked, and the consent checkbox is not pre-ticked.
- [ ] Admin and staff logins use strong passwords and 2FA. There are no default or shared credentials.
- [ ] Test or demo data is removed from production.
- [ ] Backups exist, and someone has confirmed one can be restored.

## 5. Accessibility

Patients include older adults and people with disabilities, and inaccessible sites are a legal risk.

- [ ] Complete a whole booking using only the keyboard (Tab, Shift+Tab, Enter, Space). Focus is always visible and there are no keyboard traps.
- [ ] Run the axe DevTools extension or Lighthouse accessibility audit on every booking step. Fix all critical issues.
- [ ] Color contrast meets WCAG AA (4.5:1 for body text).
- [ ] Every input has a visible label. Placeholder text isn't the only label.
- [ ] Text zooms to 200% without breaking layout.
- [ ] A quick screen reader pass: VoiceOver on Mac (Cmd+F5) or iPhone, through the first two booking steps.
- [ ] Tap targets are at least 44×44px.

## 6. Performance and mobile

- [ ] PageSpeed Insights (mobile) on the home page and booking page. Aim for roughly 80+ performance, and LCP under 2.5s.
- [ ] Images are compressed and sized properly, since stock dental photos are often huge.
- [ ] The site is usable on throttled Slow 4G.
- [ ] No horizontal scrolling at 360px.
- [ ] Sticky headers and cookie banners don't cover the Submit button on small screens.
- [ ] Phone number, address and hours are tappable and correct.

## 7. Content and SEO basics

- [ ] Office name, address, phone number and hours match the Google Business Profile exactly.
- [ ] No placeholder text, broken links or missing images. Run a free link checker.
- [ ] Each page has a title, a meta description, and a social share image.
- [ ] `robots.txt` isn't blocking the whole site, and staging has no leftover `noindex` on production.
- [ ] A custom 404 page exists.
- [ ] Favicon and mobile browser tab appearance look right.

## 8. Launch-day checks

- [ ] DNS, SSL certificate and the `www`/non-`www` redirect are working.
- [ ] A real booking is made on the live site, end to end, then cancelled.
- [ ] Notification emails come from the real domain and have SPF/DKIM set up, so they don't land in spam.
- [ ] Staff know where bookings show up and who checks them each day.
- [ ] Uptime monitoring is on (free UptimeRobot or similar), alerting a real person.
- [ ] Error logging is in place (e.g. free-tier Sentry), and someone is assigned to watch it for the first week.
- [ ] A rollback plan is written down.
- [ ] Review the first 10–20 real bookings by hand, then check analytics for step-by-step drop-off in the flow.

## Suggested order for a part-time dev

1. Sections 2 and 3 on real phones (about half a day).
2. Section 4, especially the vendor BAAs and the analytics check, which are the highest-stakes items.
3. Sections 5 and 6 with the automated tools (Lighthouse, axe).
4. Sections 7 and 8, then launch.

If you tell me the stack (WordPress, custom code, a scheduling vendor like Zocdoc, NexHealth or Calendly), I can tighten this list and write a short Playwright script to automate the main booking flow for regression checks.
