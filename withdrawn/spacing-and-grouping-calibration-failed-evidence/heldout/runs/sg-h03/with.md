Here's the updated CSS. The markup is unchanged.

```css
.notice {
  display: grid;
  grid-template-columns: auto 1fr;
  row-gap: 4px;
  column-gap: 16px;
  align-items: center;
  width: 320px;
  padding: 24px;
  border: 1px solid #ccc;
  border-radius: 8px;
  font: 14px/1.4 system-ui;
}

.notice h3,
.notice p {
  grid-column: 1 / -1;
  margin: 0;
}

.notice h3 { margin-bottom: 12px; font-size: 18px; line-height: 1.25; }  /* 4 + 12 = 16 below heading */
.who   { font-weight: 600; }
.where { margin-bottom: 20px; color: #555; }                              /* 4 + 20 = 24 before actions */

.notice button { height: 40px; padding: 0 16px; }
.notice a      { font-size: 14px; justify-self: start; }
```

What changed:
- **Groups:** The heading, the order details (name, items, shelf) and the actions (button and link) are now three clear groups.
- **Spacing:**
  - The details sit 4px apart.
  - The heading has 16px below it.
  - The actions start 24px after the details.
  - Every value is a multiple of 4.
- **Cramped feel:** The line-height was 1.1, which squashed the lines. It's now 1.4, and the padding is 24px instead of 7px.
- **Uneven margins:** The one-off margins (9, 2, 11, 1, 13 and so on) are gone. A single grid `row-gap` now owns the spacing.
- **Actions row:** The button is 40px tall with 16px side padding, and the link sits beside it with a 16px gap. The link is now 14px instead of 12px so it matches the rest of the text.
