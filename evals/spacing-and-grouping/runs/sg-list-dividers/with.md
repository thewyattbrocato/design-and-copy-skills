**Use hairline dividers.**

With about 30 uniform rows, each holding a title, a time and a small action, you want scannable rows. You don't need 30 separate objects.

- **Cards:** these add borders, padding and surface to every item. That costs rows per screen and makes the list look busy. Cards fit when each item is a discrete object, such as something draggable or comparable. Notifications aren't.
- **Space only:** this works for a short list. At 30 tightly packed rows, space alone makes the row edges blur, and the small action button makes that worse.

**Details:**
- Use one quiet 1px rule color.
- Give each row the same vertical padding on both sides of the rule.
- Let the container own the spacing, not per-item margins.
- Keep the action buttons at least 8px apart vertically.
- Group the rows under time headings such as "Today" and "Earlier". Use extra space for those breaks.
