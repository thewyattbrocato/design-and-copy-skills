A fixed spacing scale, such as 4, 8, 12, 16, 24 and 32px, gives you three things.

- **Consistency:** Eyeballed values drift. If one card uses 14px and another 15px, the UI looks slightly off, and nobody can say why.
- **Faster decisions:** You pick from six steps instead of re-deciding every gap, and code review stops arguing over pixels.
- **Visible hierarchy:** Distinct steps make grouping obvious. Related items sit close together and unrelated ones sit far apart. Near-identical values blur those groups.
- **Easier change:** If spacing lives in tokens, you can retune density across the whole app in one place.
- **Designer-developer alignment:** Both sides use the same vocabulary, so handoffs match without pixel-measuring.

The scale constrains your choices on purpose, and that's what makes the UI feel coherent.
