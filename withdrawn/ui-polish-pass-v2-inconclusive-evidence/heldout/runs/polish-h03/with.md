Your description covers the happy path. I haven't seen any code or run the app, so everything below is inferred from your list. Some of these may already exist and just not be on it.

What reads as solid: the core objects (list, editor, send, dashboard, settings) are there, and the default sort by due date is the right one for this audience.

**Ranked by harm**

1. **What the client receives.** You list a send modal but nothing about the thing being sent. Check that there's an email or a client-facing page or PDF with business name, logo, line items, tax, due date and how to pay. Check the invoice number too, since many jurisdictions require sequential numbers. If this is thin, it's the biggest gap, because it's the part your customer's customers see.
2. **Marking an invoice paid.** "Paid this month" implies a paid status, but no control for it is listed. Without a way to mark paid (and ideally partial or reopen), the dashboard numbers can't be trusted. Also check that "overdue" is derived from the due date rather than set by hand.
3. **Send and Save failures.** Check what happens when the send fails (bad address, offline, server error). It needs a busy state on the button so it can't double-send, a plain-words error that keeps the typed email and offers retry, and a visible "Sent to x@y.com" result. Double-sending an invoice to a client is the most embarrassing bug available to you. Also check:
   - email validation
   - a status change to "Sent" after sending
   - whether the Send button in the editor saves first
4. **Editor validation and lost work.** Check these cases:
   - no client selected
   - no line items
   - negative or non-numeric amounts
   - rounding of tax
   - leaving with unsaved changes

   Errors should sit beside the field and persist until fixed.
5. **Removing things.** I see no delete, void or duplicate for invoices. Customers will make mistakes in invoices they've already sent. Decide what editing a sent invoice does. For anything destructive, name the consequence on the button ("Delete invoice").
6. **Empty states.** A new customer's first view is an empty list and a dashboard of zeros. They should say what the place is for and offer "Create your first invoice". The same goes for the client picker with no clients, and for a search with no results (say what was searched, offer to clear it).
7. **Currency and locale.** Your list doesn't mention which currencies, number formats or date formats are supported. Hard-coded USD is a common launch-week surprise for freelancers.
8. **Access and devices.** Chrome on a laptop is the only tested setup. Before paying customers, check:
   - keyboard-only use of the modal (focus moves in, Escape closes, focus returns)
   - visible focus rings
   - labelled inputs
   - the table at narrow widths (phones are likely, since people check invoices on the go)
   - Safari and Firefox
   - a very long client name and hundreds of invoices
9. **Settings edge cases.** Check logo file type and size limits with a readable error, a logo that fails to upload, and whether a changed default payment term affects existing invoices.

**Left alone on purpose:** light-only is a legitimate choice, so I wouldn't add a dark theme for launch.

**Outside what I can judge from your list:** account sign-in and password reset, billing and plan handling for paying customers, data export, and privacy and terms pages. These matter for a paid release, but you didn't mention them, so I can't tell whether they exist.

**Not checked:** I haven't run the app or looked at its code. Paste the code or point me at the repo and I can verify items 3 to 6 and 8 directly and fix them.
