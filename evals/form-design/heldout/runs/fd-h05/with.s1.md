1. **Country:** Use a searchable select (autocomplete) with `autocomplete="country-name"`. It's a long, known list, and typing a few letters is faster than scrolling 190 entries. It also lets browser autofill work.

2. **Delivery speed:** Use three visible radios. Show the speed and price on each row, for example "Express, 2 days, $18". There are only three options and people compare them on price and time, so they should all be visible at once. Preselect Standard.

3. **Gift note:** Use a multi-line textarea. Label it "Gift note (optional)" and show a live counter such as "42 / 200". Set `maxlength` to 200 so the counter and the limit agree and nobody loses text silently.
