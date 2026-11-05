Your page wasn't saved in the working directory, so here are the changed pieces for you to paste in. I haven't run any of this.

**1. In `<head>`.** Your snippet starts at `<body>`. If these are missing, phones render the page zoomed out, which could be much of the "hard on phones" problem.
```html
<!doctype html>
<html lang="en">
<head>
 <meta charset="utf-8">
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Appointment reminder – Riverside clinic</title>
</head>
```

**2. Body.**
```html
<img class="banner" src="reminder-banner.png"
     alt="Your appointment: Tuesday 14 May, 10:40, Riverside clinic, 22 Mill Lane">
<main>
 <h1>Appointment reminder</h1>
 <p>Please arrive ten minutes early and bring your referral letter.</p>
 <p><a href="/appointments/manage">Change or cancel your appointment</a></p>
 <p>Need directions? <a href="/clinics/riverside">Riverside clinic page</a></p>
</main>
<script src="https://chat-vendor.example/widget.js"></script>
<!-- removed: the load handler that called ChatWidget.open() -->
```

**3. CSS.**
```css
.banner{width:100%;height:auto;display:block}
main{padding:16px;font-size:1rem;line-height:1.5}
main a{display:inline-block;padding:8px 0}
```

**What changed, and why**
- **Banner alt text:** the date, time and address existed only inside the image, and the alt said just "banner". Screen reader users got none of the appointment details. The alt now carries the full text.
- **Chat auto-open:** the load handler opened the vendor dialog on every visit. It grabbed focus from screen reader users and covered the page on a phone before anyone could read the reminder. Opening it is our code, not the vendor's, so I removed it. The widget's own launcher should still work, if it has one.
- **"Click here":** this link text means nothing when a screen reader lists links, and "click" is wrong on touch screens. It now reads "Change or cancel your appointment".
- **Text size:** 13px was too small on a phone. It's now 16px with slightly more line spacing.
- **Link tap targets:** links get vertical padding so they're easier to hit with a thumb.

**Still open**
- The banner text shrinks with the screen width, so it's hard to read on a phone even with the better alt. The real fix is to show the appointment details as HTML text, with the image purely decorative. That's a design decision, so I left it.
- I didn't check the vendor widget's own accessibility (focus trap, labels, launcher size). I also didn't test with a screen reader or on a real device.
