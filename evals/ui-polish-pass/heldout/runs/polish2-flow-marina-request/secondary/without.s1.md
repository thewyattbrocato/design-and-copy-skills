The flow treats this as a purchase, but it's a request that the harbormaster has to approve. The markup has four problems:

1. **Step 3 is a payment step.** The "Payment" label and "Continue to payment" button send the boater to a payment screen that shouldn't exist.
2. **Step 3 says "Place order."** That implies a purchase. It should say the boater is submitting a request.
3. **Step 4 says "Thank you for your purchase!" and "Your booking is confirmed."** Both are false until the harbormaster approves, so a boater would believe they have a slip they don't have yet.
4. **Step 2 is headed "Choose your slip," but there's no slip choice on it.** It only collects dates.

Here is the fixed markup. The structure is unchanged, and only the text is different:

```html
<ol class="steps"><li class="on">Boat</li><li>Dates</li><li>Review</li><li>Requested</li></ol>

<section id="s1">
  <h2>Vessel information</h2>
  <label>Name <input name="n"></label>
  <label>Length <input name="len"></label>
  <label>Info <textarea name="info"></textarea></label>
  <button>Next</button>
</section>

<section id="s2">
  <h2>Choose your dates</h2>
  <label>Arrival <input type="date" name="a"></label>
  <label>Departure <input type="date" name="d"></label>
  <button>Continue to review</button>
</section>

<section id="s3">
  <h2>Review &amp; submit request</h2>
  <p>Please check your details. Submitting sends a slip request to the harbormaster. It is not a booking until approved.</p>
  <dl><dt>Name</dt><dd>Sea Wren</dd><dt>Length</dt><dd>9</dd><dt>Arrival</dt><dd>2025-07-04</dd><dt>Departure</dt><dd>2025-07-06</dd></dl>
  <button>Submit request</button>
</section>

<section id="s4">
  <h2>Request submitted</h2>
  <p>Thanks! The harbormaster will review your request and contact you. You are not booked until your request is approved.</p>
</section>
```

Two things the markup can't fix, and you'll need to handle in the code behind it:

- **The review values are hardcoded.** "Sea Wren", "9", and the dates are placeholders. The `<dd>` values need to be filled from the inputs on screens 1 and 2 before the review step is shown. Otherwise every boater sees the same details.
- **The submission needs a pending status.** The request should be saved as "pending" and not as a confirmed booking. Screen 4 should only ever show after that record is saved.

I didn't add a slip picker or a length unit, since you asked for the fewest changes. If boaters are supposed to choose a specific slip, that would need a new field on screen 2. Also, "Length" should probably say feet or metres, but I don't know which unit your marina uses.
