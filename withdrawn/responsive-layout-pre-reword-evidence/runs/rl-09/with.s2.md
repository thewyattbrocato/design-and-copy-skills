# Pre-launch test checklist: dental booking site

## 1. Cover devices without a lab (about 1 hour setup)

- **Browser DevTools device mode** (Chrome/Edge/Firefox). It's good for layout and breakpoints, but it isn't a real phone. Use it for the first pass only.
- **Your own phones and friends' or staff phones.** Aim for at least one iPhone (Safari) and one Android (Chrome). Have 5–10 staff do a real booking on whatever they own. That's your free device lab.
- **Free or cheap cloud browsers.** BrowserStack and LambdaTest have free trials and free tiers for open source. Use them for a single focused session on older iOS Safari and a low-end Android.
- **Browser coverage target.** Latest Chrome, Safari (iOS and macOS), Edge, Firefox, and Samsung Internet. Check your analytics or ask the dev to look at your existing site's traffic. Don't chase IE or very old browsers.

## 2. The critical path (test this the most)

Run the full flow on mobile and desktop, start to finish:

1. Land on the home page, then find "Book appointment."
2. Choose a service, provider and date/time.
3. Enter patient details, new vs. existing patient, and insurance if asked.
4. Submit, then see the confirmation page.
5. Receive the confirmation email/SMS, and check that it isn't in spam.
6. Reschedule and cancel (if supported), including the links in the email.

Also test the unhappy paths:
- Required fields left blank, bad phone/email formats, and names with apostrophes, hyphens or accents (O'Brien, José).
- Double-clicking Submit, which must not create two bookings.
- Picking a slot that was just taken by someone else.
- Back button and refresh mid-flow.
- Slow network. In DevTools, throttle to "Slow 4G" and confirm the form still works and shows loading states.
- JavaScript-heavy pieces failing, like the calendar widget not loading. Check that the page shows a phone number as a fallback.

## 3. Mobile-specific checks

- No horizontal scrolling at 320, 375, 390 and 414 px widths.
- Tap targets are at least about 44×44 px and not crowded.
- Correct keyboard types: `type="tel"`, `type="email"`, and `autocomplete` attributes so autofill works.
- Input font size of at least 16px, otherwise iOS Safari zooms in on focus.
- The sticky header, cookie banner or chat widget doesn't cover the submit button or the on-screen keyboard.
- Date and time pickers are usable on iOS and Android. Native pickers are often more reliable than custom ones.
- Landscape orientation and 200% text zoom still work.
- Click-to-call and map links open the right apps.

## 4. Accessibility (also a legal risk for healthcare sites)

- Navigate the whole booking flow by keyboard only (Tab, Shift+Tab, Enter, Space). Focus must be visible and in a logical order.
- Run Lighthouse and axe DevTools (both free) on each page of the flow. Fix everything they flag.
- Every field has a real label, and error messages are text, not just red color.
- Contrast is at least 4.5:1 for body text.
- Spot-check with a screen reader: VoiceOver on a Mac or iPhone, TalkBack on Android. Do one booking.
- Test with the browser zoomed to 200%.

## 5. Performance

- Run Lighthouse in mobile mode, plus PageSpeed Insights on the live URL. Targets: LCP under 2.5s, and no layout jumping.
- Compress images and use modern formats (WebP/AVIF).
- Check total page weight on the booking pages, since patients are often on cellular.

## 6. Privacy, security and compliance

- **HTTPS everywhere**, with HTTP redirecting to HTTPS and no mixed-content warnings.
- **HIPAA (if you're in the US).** Confirm where form data goes and that every vendor touching patient info (scheduling tool, email/SMS, hosting, form handler) will sign a BAA. Don't put health details in URLs, analytics events or plain email bodies.
- **Analytics and tracking pixels.** Make sure Meta Pixel, Google Analytics and similar tools aren't capturing appointment or health info. Regulators have acted on this.
- Cookie and consent banner works if your region requires it.
- Basic hardening: spam protection (CAPTCHA or honeypot) on forms, rate limiting, and no admin pages publicly guessable.
- Check that error pages don't reveal stack traces.

## 7. Content and integration checks

- Office hours, address, phone and insurance info are correct everywhere, including the Google Business Profile.
- Time zones and daylight saving are handled correctly in booked slots and emails.
- Bookings land in your practice management or calendar system correctly, with the right provider, length and patient data. Do this with several test bookings, then delete them.
- Holidays and blocked-off times don't show as available.
- Email/SMS templates render properly in Gmail, Apple Mail and Outlook. Test the SPF/DKIM/DMARC setup so confirmations don't go to spam.
- 404 page, favicon and meta tags are set. Social share preview and the page title for search results are right.

## 8. Launch-day plan

- Staging or soft-launch period: have staff book real-looking appointments for a few days.
- Back up the site and know how to roll back.
- Set up uptime monitoring (UptimeRobot has a free tier) and an alert if the booking form fails.
- Make sure someone is assigned to check the booking inbox or calendar on day one.
- Keep the old booking method (phone) visible for the first couple of weeks.
- Confirm analytics goals fire on the confirmation page, without capturing patient data.

## Suggested priority if time is short

1. The full booking flow on a real iPhone and Android phone.
2. Confirmation emails and calendar integration.
3. HIPAA/vendor and tracking review.
4. Keyboard and Lighthouse accessibility pass.
5. Slow-network and error-case testing.
6. Everything else.

Ask the dev to record which items passed, with dates and device/browser, in a shared sheet. Failures then become a clear to-do list, and you have a record if questions come up later.
