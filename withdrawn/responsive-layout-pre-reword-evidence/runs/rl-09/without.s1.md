# Pre-Launch Test Checklist: Dental Booking Site

Priority order: if time runs short, do top to bottom and stop where you must.

## 1. Core booking flow (most important)
Test the whole path as a patient would: choose service → pick date/time → enter details → confirm → receive confirmation.
- [ ] New patient and existing patient paths both work
- [ ] Every service type can be booked
- [ ] Double-booking is impossible (two browsers, same slot, submit at the same time)
- [ ] Cancel and reschedule work, and the slot is freed
- [ ] Confirmation email/SMS arrives, with correct date, time, location, and timezone
- [ ] Reminder emails/SMS fire (if offered)
- [ ] Staff actually see the booking in their calendar or system, with all fields intact
- [ ] Edge cases: past dates, holidays, office-closed days, lunch breaks, same-day cutoff, daylight-saving changeover dates
- [ ] Error handling: empty fields, bad email, bad phone, very long names, apostrophes and accents (O'Brien, José)
- [ ] Back button, refresh mid-flow, and double-clicking Submit don't create duplicates or lose data

## 2. Devices and browsers (free options)
You don't need a lab. Cover these:
- **Chrome DevTools device mode**: quick layout checks at 360, 390, 768, and 1280px widths. It's good for layout, but not for touch quirks or real keyboards.
- **Real devices you already have**: staff and family phones. Get at least one iPhone (Safari) and one Android (Chrome). Most of your patients will be on these.
- **Desktop**: latest Chrome, Safari, Edge, Firefox. Check your analytics or ask the front desk what patients use.
- **Free tiers**: BrowserStack and LambdaTest offer free trials or free plans for open source. Use them for one targeted pass on an older iPhone/iOS version.
- **Older devices**: dental patients skew older. Test with browser zoom at 200% and with larger system font sizes.

On each, check: tap targets are comfortably large, the date picker works, the on-screen keyboard doesn't cover fields, and nothing scrolls sideways.

## 3. Accessibility (legal risk and an older patient base)
- [ ] Run **Lighthouse** (in Chrome DevTools) and **axe DevTools** (free extension) on every page in the flow. Fix all critical issues.
- [ ] Complete a booking using only the keyboard (Tab, Shift+Tab, Enter, Space). Focus must be visible and in a logical order.
- [ ] Turn on a screen reader for one pass: VoiceOver (built into Mac/iPhone) or TalkBack (Android). Form labels and errors should be announced.
- [ ] Text contrast is at least 4.5:1; errors don't rely on color alone
- [ ] Zoom to 200% without losing content or function

## 4. Privacy, security, and compliance
Dental practices in the US are typically HIPAA-covered, so check with your counsel or compliance contact. Practical items:
- [ ] HTTPS everywhere, with a valid certificate, and HTTP redirects to HTTPS
- [ ] Don't collect more health information than you need. Free-text "reason for visit" fields can capture sensitive details.
- [ ] Booking vendor, form tool, email/SMS provider, and hosting each have a signed BAA if they handle patient data
- [ ] No patient data in URLs, browser console logs, or analytics. Check that Google Analytics, Meta Pixel, and similar trackers don't receive form contents or appointment details. This is a real enforcement area.
- [ ] Confirmation emails contain minimal detail (no treatment info)
- [ ] Try obvious abuse: view another booking by changing an ID in the URL (should fail), submit forms with `<script>` in the name field, and submit rapidly many times (rate limiting or CAPTCHA)
- [ ] Admin and staff logins use strong passwords and 2FA, and there are no default credentials
- [ ] Privacy policy and consent text are present and accurate
- [ ] Run a free scan: **Mozilla Observatory** or **securityheaders.com**

## 5. Performance
- [ ] Run **PageSpeed Insights** on the home and booking pages (mobile score). Aim for the "good" range on LCP, CLS, and INP.
- [ ] Throttle to "Slow 4G" in DevTools and complete a booking
- [ ] Compress images, especially hero and team photos
- [ ] Load test lightly. Have 5–10 people book at once, since the common failure is a spike after an email blast or ad launch.

## 6. Content and local discovery
- [ ] Address, phone, hours, and insurance info are correct everywhere, and the phone number is tap-to-call
- [ ] Map link opens correctly on phones
- [ ] Every link and button works (use a free broken-link checker)
- [ ] Spelling and names of dentists and staff are right
- [ ] Page titles, meta descriptions, and a favicon are set. Share a link in iMessage or Slack and check the preview.
- [ ] Google Business Profile points to the right booking URL
- [ ] Custom 404 page, plus a visible "call us" fallback if booking fails

## 7. Operations and launch readiness
- [ ] Email deliverability: send confirmations to Gmail, Outlook, and Yahoo, and check that they don't land in spam. Set up SPF, DKIM, and DMARC on your sending domain (test at mail-tester.com).
- [ ] Analytics or conversion tracking works on the final confirmation step, without capturing personal data
- [ ] Error monitoring is in place (free tiers of Sentry or UptimeRobot) with alerts going to someone who will see them
- [ ] Backups exist, and someone has confirmed a restore works
- [ ] Domain and SSL auto-renewal are set up, with expiry reminders
- [ ] Rollback plan: who can disable the site or switch it to "call to book," and how fast
- [ ] Staff trained: they know where bookings appear, how to cancel or move one, and what to do if a patient says "the site didn't work"

## 8. Soft launch
1. Have 5–10 staff, friends, and existing patients book real appointments (then cancel them) on their own devices, with no coaching.
2. Watch one or two do it in person or over screen share. Confusion shows up quickly.
3. Launch quietly for a few days before any email or ad push.
4. For the first week, check bookings, errors, and email delivery daily.

## Suggested handoff
Give the dev sections 1, 4, and 7 as the "must pass" items. Have the front desk or office manager own sections 6 and 8. Record each issue with the device, browser, steps, and a screenshot, so fixes are quick.

One caveat: I've written this without seeing your site or booking platform. If you use a hosted tool (Dentrix, NexHealth, Calendly, etc.), much of section 4 shifts to vendor review, and sections 1 and 7 get lighter. Tell me which platform you're using and I can tighten the list.
