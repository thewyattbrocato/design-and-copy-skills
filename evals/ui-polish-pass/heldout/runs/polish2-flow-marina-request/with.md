The flow is written like a checkout, but what you're building is a request. The "Payment" step, "Place order" and "Thank you for your purchase! Your booking is confirmed." all promise things that don't happen. The last one is the worst, because a boater would think they have a slip when the harbormaster hasn't approved anything.

Only the copy needs to change. The structure and the number of steps stay the same.

```html
<ol class="steps"><li class="on">Boat</li><li>Dates</li><li>Review</li><li>Done</li></ol>

<section id="s1">
  <!-- unchanged -->
</section>

<section id="s2">
  <h2>Choose your dates</h2>
  <label>Arrival <input type="date" name="a"></label>
  <label>Departure <input type="date" name="d"></label>
  <button>Continue</button>
</section>

<section id="s3">
  <h2>Review your request</h2>
  <p>Please check your details.</p>
  <dl><dt>Name</dt><dd>Sea Wren</dd><dt>Length</dt><dd>9</dd><dt>Arrival</dt><dd>2025-07-04</dd><dt>Departure</dt><dd>2025-07-06</dd></dl>
  <button>Send request</button>
</section>

<section id="s4">
  <h2>Request sent</h2>
  <p>The harbormaster will review it. Your slip is not booked until it's approved.</p>
</section>
```

What changed and why:
- **Step 3 label:** "Payment" is now "Review". Nobody pays online, and this step is a summary.
- **Screen 2:** the heading said "Choose your slip", but boaters only pick dates, so it's now "Choose your dates". The button no longer says "Continue to payment".
- **Screen 3:** "Review & confirm" is now "Review your request". "Confirm" implies the booking is final. "Place order" is now "Send request".
- **Screen 4:** the "purchase" and "confirmed" wording is replaced with a plain statement that the request was sent and is pending approval.

I left a few things alone because they're outside the fewest-changes scope, but you may want to fix them:
- **Length unit:** the Length field has no unit (feet or meters), which matters for slip assignment.
- **Info label:** "Info" is vague.
- **Contact details:** the form collects no email or phone number, so the harbormaster has no way to tell the boater the outcome. That's probably the biggest gap.
