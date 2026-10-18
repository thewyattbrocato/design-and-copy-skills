The flow is a checkout flow with a request flow underneath it. The "Payment" step, "Place order" button, and "Thank you for your purchase!" all suggest money changes hands, and the last screen says the booking is confirmed before the harbormaster has approved anything. Those are the wording and step labels to fix. The structure and field names can stay.

```html
<ol class="steps"><li class="on">Boat</li><li>Dates</li><li>Review</li><li>Done</li></ol>

<section id="s1">
  <h2>Vessel information</h2>
  <label>Name <input name="n"></label>
  <label>Length <input name="len"></label>
  <label>Info <textarea name="info"></textarea></label>
  <button>Next</button>
</section>

<section id="s2">
  <h2>Choose your slip</h2>
  <label>Arrival <input type="date" name="a"></label>
  <label>Departure <input type="date" name="d"></label>
  <button>Review request</button>
</section>

<section id="s3">
  <h2>Review &amp; submit</h2>
  <p>Please check your details. This is a request only. The harbormaster must approve it before it becomes a booking.</p>
  <dl><dt>Name</dt><dd>Sea Wren</dd><dt>Length</dt><dd>9</dd><dt>Arrival</dt><dd>2025-07-04</dd><dt>Departure</dt><dd>2025-07-06</dd></dl>
  <button>Submit request</button>
</section>

<section id="s4">
  <h2>Request submitted</h2>
  <p>Your slip request has been sent. It is not a booking yet. The harbormaster will review it and confirm.</p>
</section>
```

**What changed (6 text edits, no structural changes):**
- Step 3: "Payment" → "Review", since there is no payment step.
- s2 button: "Continue to payment" → "Review request".
- s3 heading: "Review & confirm" → "Review & submit", so it doesn't imply a final purchase.
- s3 paragraph: added that this is a request and needs harbormaster approval.
- s3 button: "Place order" → "Submit request".
- s4 heading and paragraph: replaced "Thank you for your purchase!" and "Your booking is confirmed" with wording that says the request is pending.

**Not changed, but you'll need to handle these in the app code:**
- The `<dl>` on s3 is hardcoded ("Sea Wren", 9, and the dates). It should be filled from the s1 and s2 inputs. It also leaves out Info, so add it there if the harbormaster should see it.
- Nothing checks that Departure is after Arrival. A `min` attribute on the date inputs, or a check on submit, would catch that.
- The `on` class on the step list is static, so the app has to move it as the user goes through the screens.
