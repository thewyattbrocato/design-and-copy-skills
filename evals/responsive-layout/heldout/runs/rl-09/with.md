# Pre-launch test checklist: dental booking site

## 1. The booking flow (80% of the value)
Test the whole path end to end, on a real phone and a laptop:
- [ ] Book each appointment type (new patient, cleaning, emergency, etc.) as a brand-new visitor
- [ ] Confirmation page appears, **confirmation email/SMS actually arrives** (check spam too), and the office's calendar/system receives the booking
- [ ] Reschedule and cancel work, and the links in the emails work
- [ ] Error paths: double-booking the same slot, past dates, empty or invalid fields, bad phone/email formats, back button mid-flow, refresh mid-flow, double-clicking Submit (should create one booking, not two)
- [ ] Time zones and daylight saving: slots show in the office's local time, including around the next DST change
- [ ] Closed days, holidays, and lunch blocks aren't bookable
- [ ] Insurance, DOB, and reason-for-visit fields behave sensibly

## 2. Devices and browsers without a lab
- **Real devices you already have:** your own phone, staff phones, a family member's older phone. Aim for at least one iPhone (Safari), one Android (Chrome), and one desktop each of Chrome, Safari, and Edge or Firefox.
- **Browser dev tools:** Chrome DevTools device mode for quick checks of widths (320, 375, 390, 768, 1024, 1440) and throttled network. It doesn't replace real Safari, so don't skip a real iPhone.
- **Free or cheap cloud testing:** BrowserStack and LambdaTest have free trials or free tiers for real-device sessions. Use them for the gaps, like an old Samsung or an iPad.
- **Check on each:** layout doesn't overflow or scroll sideways, tap targets are big enough (about 44px), date pickers and keyboards behave (right keyboard for phone/email fields), sticky headers don't cover buttons, and text stays readable when the OS font size is increased.

## 3. Speed and mobile experience
- [ ] Run Google PageSpeed Insights / Lighthouse on the home and booking pages (mobile mode). Target roughly 90+ performance, and fix anything red.
- [ ] Test on cellular with Wi-Fi off, and with DevTools set to "Slow 4G"
- [ ] Compress images; make sure no giant hero photo loads on phones

## 4. Accessibility (patients include older and disabled people, and there's legal exposure)
- [ ] Run Lighthouse and the free axe DevTools extension. Fix every flagged issue.
- [ ] Complete a booking using only the keyboard (Tab, Enter, Space, Esc). Focus must be visible and logical.
- [ ] Turn on VoiceOver (Mac/iOS) or TalkBack (Android) and try the booking form for 5 minutes. Fields need labels, and errors must be announced.
- [ ] Check color contrast (4.5:1 for body text) and zoom the page to 200% with nothing breaking
- [ ] Form errors don't rely on color alone

## 5. Privacy, security, and compliance
This is a healthcare context, so treat it seriously.
- [ ] HTTPS everywhere, and HTTP redirects to HTTPS. Certificate auto-renews.
- [ ] **HIPAA:** if the form collects health info, confirm that the form tool, hosting, email, and any SMS provider will sign a BAA. Don't send health details in plain email or SMS. Keep reason-for-visit out of notifications.
- [ ] No patient data in URLs, analytics, or error logs. Check that Google Analytics, Meta Pixel, and chat widgets aren't capturing form contents (tracking pixels on health pages are a known enforcement area).
- [ ] Spam and bot protection on the form (reCAPTCHA, hCaptcha, or Turnstile) and rate limiting
- [ ] Basic security headers (check at securityheaders.com) and SSL grade (ssllabs.com)
- [ ] Privacy policy and consent text are present and accurate; cookie banner if you have EU/California visitors
- [ ] Admin logins use strong passwords and 2FA. Software and plugins are up to date.

## 6. Content and discoverability
- [ ] Office name, address, phone, and hours are correct everywhere and match your Google Business Profile
- [ ] Phone numbers are tap-to-call, and the address opens maps
- [ ] Click every link and button; check for broken links (free tools: Screaming Frog free tier, or W3C link checker)
- [ ] Page titles, meta descriptions, and a favicon exist; social share preview looks right
- [ ] 404 page is helpful, `robots.txt` doesn't block the whole site, and there is **no leftover `noindex` tag** from staging
- [ ] Spelling and proofreading pass, especially on services and pricing

## 7. Launch-day and operations
- [ ] Staff walk through the booking from the office side, and agree on who monitors new bookings and how fast they respond
- [ ] Uptime monitor (UptimeRobot is free) and email alerts for form failures
- [ ] A backup or rollback plan, and a note of who has DNS and hosting access
- [ ] Fallback: "Call us at…" is visible near the booking button if the form fails
- [ ] Do a final **real booking** after DNS cutover on the live domain, then cancel it
- [ ] Soft launch: have 5-10 friendly patients or staff family members try it unprompted. Watch where they hesitate. This finds more problems than any tool.

## Suggested priority if time is short
1. Booking flow end to end on a real iPhone and a real Android
2. Confirmation emails/SMS and office-side receipt
3. HIPAA/BAA and tracking-pixel review
4. Keyboard and screen-reader pass plus Lighthouse
5. Soft launch with real people

Ask the dev to record results as pass/fail with a screenshot or short screen recording for each failure. That makes fixes quick to verify.
