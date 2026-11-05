The flow is a copy of a store checkout. The structure is fine for a request, but the payment step, the purchase wording, and the "confirmed" wording all tell the boater they've paid and booked. I changed only text, one step label, and one button label, and left the structure, names, and IDs alone.

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
  <h2>Request a guest slip</h2>
  <label>Arrival <input type="date" name="a"></label>
  <label>Departure <input type="date" name="d"></label>
  <button>Continue to review</button>
</section>

<section id="s3">
  <h2>Review your request</h2>
  <p>Please check your details. The harbormaster will review your request. It is not a booking until it is approved.</p>
  <dl><dt>Name</dt><dd>Sea Wren</dd><dt>Length</dt><dd>9</dd><dt>Arrival</dt><dd>2025-07-04</dd><dt>Departure</dt><dd>2025-07-06</dd></dl>
  <button>Submit request</button>
</section>

<section id="s4">
  <h2>Request submitted</h2>
  <p>Your slip request has been sent to the harbormaster. You will be notified when it is approved. No payment is due now.</p>
</section>
```

**What changed**
- **Step 3:** "Payment" → "Review". Nothing is paid in this flow.
- **S2 heading and button:** "Choose your slip" → "Request a guest slip"; "Continue to payment" → "Continue to review".
- **S3 heading:** "Review & confirm" → "Review your request". Added a line saying it isn't a booking until approved.
- **S3 button:** "Place order" → "Submit request". "Place order" implies a purchase.
- **S4 heading and body:** "Thank you for your purchase!" / "Your booking is confirmed" → "Request submitted", with a note that the harbormaster must approve it and no payment is due.

**Not changed, but you should look at these**
- **The review table is hardcoded.** The `<dl>` shows "Sea Wren", "9", and the dates no matter what the boater entered. It needs to be filled from the s1 and s2 inputs, or the boater will submit wrong data without noticing. This is a script change, so I didn't make it in markup.
- **No date check.** Nothing stops a departure date before the arrival date.
- **Length has no unit.** "9" could mean feet or meters. Consider adding "ft" or "m" to the label.
- **Info isn't on the review screen.** The notes the boater typed in s1 disappear before submission.
- **The request isn't saved anywhere yet.** The Submit button only changes the screen, so the harbormaster never sees the request unless the submit handler sends it to a backend.
