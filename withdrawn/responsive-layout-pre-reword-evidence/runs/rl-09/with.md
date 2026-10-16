# Pre-launch test checklist: dental booking site

Booking is the thing that makes money, so test that first. Everything else is secondary.

## 1. The booking flow (highest priority)
Run these end to end on a real phone and a real desktop browser.
- [ ] Book a new-patient appointment from the homepage to the confirmation screen.
- [ ] Book as a returning patient, if that path is different.
- [ ] Reschedule and cancel.
- [ ] Confirmation email and SMS arrive, and the links in them work. Check spam folders too.
- [ ] The appointment shows up in the practice's calendar or software (Dentrix, Eaglesoft, etc.) with the right time and **time zone**.
- [ ] Double-booking is blocked. Open two browsers and try to grab the same slot.
- [ ] Edge cases: booking at the end of the day, on a holiday, and across a daylight-saving change.
- [ ] Error paths: invalid phone, invalid email, an empty required field, a slot that's taken mid-booking, and a double-click on Submit.
- [ ] Check what happens if the user hits Back, refreshes, or loses connection mid-flow.

## 2. Devices and browsers without a lab
- **Cover the real traffic.** Check analytics from the old site if you have it. If not, assume mobile is 60–70% of visitors, mostly iPhone Safari and Android Chrome.
- **Use free cloud devices.** BrowserStack and LambdaTest both have free trials, and BrowserStack has a free tier for open-source projects. Spend an afternoon on real iOS Safari and a mid-range Android.
- **Use desktop emulation for layout checks.** Chrome DevTools device mode is good for this. Safari's Responsive Design Mode on a Mac and Firefox's are also useful. Emulation is not reliable for touch behavior, keyboards, or Safari quirks.
- **Borrow devices.** Ask staff and patients to try it on their own phones. Include an older phone and someone over 60.
- **Minimum browser matrix:** iOS Safari (current and one version back), Chrome Android, desktop Chrome, Safari, Edge, Firefox.
- **Widths to check:** 320, 375, 414, 768, 1024, and 1440 px.
- [ ] Check landscape orientation, 200% browser zoom, and large system font settings.
- [ ] Forms: the right keyboard appears (`type="tel"`, `type="email"`), autofill works, and nothing gets hidden behind the on-screen keyboard.
- [ ] Tap targets are at least 44×44 px, and there are no hover-only interactions.

## 3. Accessibility
Dental patients skew older, and accessibility lawsuits against healthcare sites are real.
- [ ] Run Lighthouse and axe DevTools (both free) on every key page, then fix what they flag.
- [ ] Complete a booking using only the keyboard (Tab, Enter, Space, Esc). Focus must be visible and in a sensible order.
- [ ] Do one pass with VoiceOver (Mac/iOS) or TalkBack (Android). Check that the form labels, errors, and calendar picker make sense.
- [ ] Text contrast meets WCAG AA (4.5:1). Don't use color alone to show errors or availability.
- [ ] Calendar and time-slot pickers are the usual trouble spot. Check them closely.

## 4. Speed and reliability
- [ ] Run Lighthouse or PageSpeed Insights in mobile mode and aim for 80+. Test on throttled "Slow 4G" in DevTools too.
- [ ] Compress images and use modern formats (WebP/AVIF).
- [ ] Check that the site works on a weak connection and that failed requests show a message instead of a blank screen.
- [ ] Set up free uptime monitoring (UptimeRobot) on the homepage and the booking endpoint.

## 5. Privacy and security
This is healthcare-adjacent, so it's the part not to skip.
- [ ] HTTPS everywhere, with HTTP redirecting to HTTPS and a valid certificate that auto-renews.
- [ ] Confirm whether the site collects PHI (symptoms, insurance, treatment reasons). If so, you may need HIPAA-compliant hosting and a BAA with every vendor that touches the data: form provider, email, SMS, analytics, scheduler. Ask your lawyer or compliance contact.
- [ ] **Check analytics and ad pixels** (Meta Pixel, Google Analytics). They must not capture health details from booking pages. This is an enforcement area for the HHS and FTC.
- [ ] Rate-limit or CAPTCHA the booking form to stop spam bookings.
- [ ] Test input handling with `<script>` and quote characters in the form fields, and make sure the server validates input as well as the browser.
- [ ] Admin logins use strong passwords and MFA. There are no default credentials, and no secrets in the code repo.
- [ ] Privacy policy, terms, and cookie notice are published and accurate.

## 6. Content and SEO basics
- [ ] Office address, phone, hours, and insurance information are correct. Test every `tel:` link and map link.
- [ ] No placeholder text, broken links, or missing images. A free link checker such as Broken Link Checker handles this.
- [ ] Page titles, meta descriptions, and local business schema are in place.
- [ ] Your Google Business Profile points to the new URL.
- [ ] Old URLs redirect to the new ones if you're replacing an existing site.
- [ ] A custom 404 page exists, and `robots.txt` doesn't accidentally block the whole site (a common launch mistake, since staging sites often have it blocked).

## 7. Launch-day steps
- [ ] Do a full test booking on the **production** site, then delete or cancel it.
- [ ] Brief front-desk staff on how bookings arrive and what to do when something looks wrong.
- [ ] Write down a rollback plan and a phone-booking fallback.
- [ ] Watch the first few days of real bookings closely. Compare the number of site bookings with the number of appointments that show up on the schedule.

## Suggested time budget for a part-time dev
| Block | Time |
|---|---|
| Booking flow, desktop and phones | 3–4 hrs |
| BrowserStack pass (iOS Safari, Android Chrome) | 2 hrs |
| Accessibility audit and fixes | 3 hrs |
| Performance and monitoring | 1–2 hrs |
| Privacy/security review | 2 hrs, plus any legal follow-up |
| Content, links, SEO | 1–2 hrs |

If time runs short, cut in this order: sections 1, then 5 (PHI and tracking), then iOS Safari and Android Chrome from section 2, then 3. Section 5 is the one that can cause legal trouble, so it shouldn't be the one that gets cut.

I can turn this into a GitHub issue template or a spreadsheet for tracking, if that would help.
