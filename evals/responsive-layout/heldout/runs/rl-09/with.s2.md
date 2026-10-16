# Pre-launch test checklist: dental booking site

Booking is the thing that has to work, so test that first and everything else second.

## 1. Free device coverage

- **Your own phones.** Have the dev, the front desk and the dentists each test on whatever they own. You'll cover a mix of iPhone/Android and old/new for free.
- **Desktop browser dev tools.** Chrome DevTools device mode (Cmd/Ctrl+Shift+M) covers layout at different sizes and throttles the network (set it to "Slow 4G"). It does not replace a real phone for touch, keyboards or date pickers.
- **Browsers to cover.** Safari on iPhone, Chrome on Android, and Chrome, Safari, Edge and Firefox on desktop. Safari on iPhone is where bugs most often hide.
- **Free tiers of cloud testing.** BrowserStack and LambdaTest both offer free trials or free open-source plans. Use them for a one-day check on a few older or odd devices, such as an older iPhone and a Samsung.
- **Ask patients.** Send the staging link to 5–10 friendly patients, including a few older ones, and ask them to book. This is often the most valuable test.

## 2. Critical path (do on a real phone and on desktop)

1. Land on the home page, find "Book," and pick a service, provider, date and time.
2. Enter patient details and submit.
3. Confirm the success screen appears, the confirmation email or SMS arrives, and the appointment shows up in your scheduling system.
4. Cancel or reschedule, if you offer it.

Also try these failure cases:
- Double-booking the same slot from two browsers at once
- Booking a past date, or a slot outside office hours
- Empty required fields, bad email, bad phone format
- Back button and page refresh mid-flow (nothing should duplicate or lose data)
- Slow or dropped connection at the submit step (airplane mode just before clicking)
- Time zones, if anyone books from out of area or your system stores UTC

## 3. Forms and mobile usability

- Tap targets are big enough, and nothing is hidden behind the keyboard.
- Input types are right (`tel`, `email`) so phones show the correct keyboard.
- Autofill works (name, phone, email).
- Date and time pickers work on iOS and Android.
- Error messages are visible, specific and next to the field.
- Text is readable without zooming, and there is no sideways scrolling.
- The click-to-call phone number, map link and address work.

## 4. Accessibility (matters legally and for older patients)

- Complete the whole booking using only the keyboard (Tab, Enter, Space, arrow keys), with a visible focus indicator.
- Run Lighthouse (built into Chrome) and axe DevTools (free extension). Fix everything they flag as serious.
- Check color contrast and that every form field has a real label, not just placeholder text.
- Zoom to 200% and check nothing breaks.
- Do a 10-minute pass with VoiceOver (Mac/iPhone) or TalkBack (Android).

## 5. Performance

- Run Lighthouse or PageSpeed Insights on the home and booking pages, mobile mode.
- Check that images are compressed and correctly sized.
- Test on real cellular data, not just office Wi-Fi.

## 6. Privacy and security (health-adjacent data)

- The site is HTTPS only, HTTP redirects to HTTPS, and the certificate isn't close to expiring.
- Don't collect clinical details in the booking form unless you need to. Ask your lawyer or compliance contact whether HIPAA applies to your form, email and hosting setup. If it does, make sure your form, email and scheduling vendors will sign a BAA.
- Don't put patient details in confirmation emails or SMS beyond what's necessary.
- Check that analytics, ad pixels (Meta, Google) and chat widgets aren't sending form contents or health information to third parties.
- Test that the form can't be spammed (CAPTCHA or rate limiting), and that bots don't flood your calendar.
- Check that the admin login uses strong passwords and 2FA, and that no staging or test pages are public.
- Confirm the privacy policy and consent text are accurate and linked.

## 7. Content, SEO and basics

- Hours, address, phone, insurance info and provider names are correct everywhere.
- Every link works, and there are no placeholder text or images left.
- Page titles and descriptions are set, and the Google Business Profile matches the site.
- A custom 404 page exists, and old URLs redirect if you're replacing an existing site.
- The favicon and social share preview look right.
- Analytics and conversion tracking record a completed booking (test it).

## 8. Launch-day readiness

- Email and SMS deliverability: send test confirmations to Gmail, Outlook and Apple Mail, and check they don't land in spam (SPF/DKIM/DMARC set up).
- A staff phone fallback shows if booking is down ("Call us at…").
- Uptime monitoring is on (UptimeRobot has a free tier) with alerts going to a real person.
- Backups are enabled, and you know who to contact if the site goes down.
- The front desk has been walked through how bookings arrive, and how to handle changes or cancellations.
- Do a soft launch: give the link to a limited group first, and watch the first day of real bookings closely.

## Triage rule for the dev

- **Must fix before launch:** anything that blocks or corrupts a booking, any privacy or security problem, and broken contact info.
- **Fix within a week:** minor layout bugs on less common devices, and performance polish.
- **Log and defer:** cosmetic issues that don't affect use.

Have the dev record every issue with the device, browser, steps and a screenshot, so fixes are quick to verify.
