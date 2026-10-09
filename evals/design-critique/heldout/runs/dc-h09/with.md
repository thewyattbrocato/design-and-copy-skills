**Verdict:** nothing on the page is ranked. Every element is styled at nearly the same level, so a visitor can't tell what matters first. That is what reads as amateur.

**Findings, in order of fix priority**

1. **The type scale has no hierarchy (major).** The headline is 28px, the date is 26px, and the intro's first sentence is 24px, all bold. They differ by 2px each, which looks like a mistake rather than a choice. Bolding only the first sentence of a paragraph also makes a heading and a body line fight each other. Fix: make the headline clearly dominant (about 40px or more). Make the date a distinct secondary element, such as a smaller, lighter-weight line under the headline. Set the intro in plain 16–18px.

2. **The buttons have no priority and no consistent system (major).** There are four buttons in four styles: outlined, filled, a text link in a pill, and filled in a second red. "Get tickets" is probably the main goal, yet it's the outlined one, which looks weaker than "Vendor list". Fix: one primary style (filled) for "Get tickets" only, one secondary style (outlined) for "Vendor list" and "Map", and "Subscribe" as a quiet tertiary. Drop the second red.

3. **Everything is boxed, so nothing is grouped (moderate).** All five sections get the same 1px border and drop shadow. Tickets, the main action, looks the same as parking. Boxes and shadows also add visual noise. Fix: remove the borders and shadows and separate sections with spacing and headings. If you keep any container, use it only for tickets.

4. **There's one color for everything (moderate).** Headline, date, body text, and borders are all #8b0000 on pink. Without a text/accent split, color can't signal what's important. Contrast is probably fine, since dark red on a pale background should be well above 4.5:1 (my rough estimate is 8–10:1, but I wasn't given the exact pink). Fix: use near-black or dark neutral for body text and keep the red as the accent for the headline and the primary button.

5. **The vendor photos are different sizes (moderate).** Ragged sizes look unfinished and make the grid hard to scan. Fix: crop to one aspect ratio and size, such as 4:3 or square, and use one consistent gap.

6. **Everything is centered (minor, partly taste).** Centering works for the headline and date. For the multi-line paragraphs and the vendor, food, and parking details, a ragged left edge makes reading harder. Fix: center the hero and left-align the content below it.

**What to keep**
- A single brand red gives the page an identity, and a winter-market feel suits the pink. Use it with more restraint.
- Splitting the content into five clear sections (about, vendors, food, parking, tickets) matches what visitors need to know.
- The date and the headline sit up top, where visitors will look first.

**Not checked:** exact contrast, mobile layout, and the real copy. I judged from your description, not a screenshot. If you send a screenshot or the HTML, I can check these.
