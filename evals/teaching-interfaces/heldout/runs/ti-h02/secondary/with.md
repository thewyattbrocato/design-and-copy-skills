## Why people skip it

- **Step 1 asks for time before giving anything.** "Let's take a quick tour" is a promise of nothing. Users skip because they don't yet know whether the tour is worth their time, and an overlay that blocks the dashboard makes that choice feel like a toll.
- **It's a tour of labels, not of jobs.** Steps 2 and 3 list nav items and top-bar icons. A new user can read a sidebar. Nobody needs a list of nine menu names read aloud.
- **It describes things that are empty.** Step 4 talks about revenue, overdue invoices, and a cash-flow chart. A new account has none of that, so the step describes a screen they aren't looking at yet.
- **The one useful step is buried.** Step 5, creating an invoice, is the thing a freelancer actually came to do. It's fifth of seven, after the user has already been told to wait.
- **Step 6 is a setup task inside a tour.** Connecting a bank needs credentials and a few minutes. Nobody does that mid-tour, and it's where the most value is.
- **Step 7 is a dead end.** "You're all set!" tells the user nothing about what to do next.

The 80% skip rate on step 1 mostly tells you the overlay is blocking. It doesn't tell you the content is wrong.

## What I'd change

1. **Remove the blocking tour.** Don't show it on first login.
2. **Replace it with a setup checklist on the empty dashboard.** Each item is one action, and it checks itself off:
   - Create your first invoice (press N)
   - Add a client
   - Connect your bank so payments match automatically
   - Send an invoice with a payment link
   
   The dashboard's stat cards can stay, but show a short "this fills in as you invoice" line instead of pretending to have data.
3. **Use coach marks at the point of use.** The first time someone opens Invoices, point at the + button and mention N. Inside the editor, annotate the actual fields (line items, tax, discounts, due date, payment link) when the user first reaches them. Each mark appears once, in context, and explains only what's on screen.
4. **Move bank connection to where its value is obvious.** Prompt for it after the first invoice is sent, or when the checklist reaches that item, with one line of copy: "Payments you receive will be matched to invoices automatically." That line is the reason to do it.
5. **Keep a tour only as an opt-in.** If you want one, make it two steps at most, start it from a "Show me around" link in the help menu, and give "Not now" the same visual weight as the primary button. Don't hide the skip option to push completion.
6. **Measure the right thing.** Skip rate on step 1 isn't the goal. Track whether new accounts send their first invoice within 24 hours and 7 days, and whether they connect a bank. Run the checklist version against the current tour and compare those numbers.

One caveat: I'm working from the copy you pasted, not from your flow or your analytics breakdown. If you can see where people drop off after step 1 (do they leave the app, or just dismiss the overlay and keep going?), that would tell you whether the fix is the format or the content.
