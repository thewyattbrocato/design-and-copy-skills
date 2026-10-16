Here's the updated CSS. It uses a 4px scale (4, 8, 16) and keeps your markup and content as they are.

```css
.notice {
  box-sizing: border-box;
  width: 320px;
  padding: 16px;
  border: 1px solid #ccc;
  border-radius: 8px;
  font: 14px/1.4 system-ui;
}

.notice h3 {
  margin: 0 0 8px;
  font-size: 17px;
  line-height: 1.3;
}

/* name, items and location are one group, so they sit close together */
.who,
.items,
.where {
  margin: 0;
}

.items,
.where {
  margin-top: 4px;
}

.who { font-weight: 600; }
.where { color: #555; }

/* the extra space above the actions is what separates them from the details */
.notice button {
  height: 36px;
  margin: 16px 16px 0 0;
  padding: 0 16px;
}

.notice a {
  font-size: 13px;
}
```

What changed:
- **Padding:** it went from 7px to 16px, which fixes most of the squashed look. I added `box-sizing: border-box` so the notice stays 320px wide.
- **Line height:** it went from 1.1 to 1.4, so lines no longer crowd each other.
- **Details group:** the name, items and shelf location are one group. They had random gaps of 9, 11, 2, 1 and 13px, which caused the uneven look. They now sit 4px apart.
- **Group spacing:** the heading sits 8px above the details, and there are 16px above the actions. That makes the heading, the details and the actions read as three groups, with less space inside a group than between groups.
- **Button:** it's 36px tall with 16px side padding, up from 24px tall with 5px. The link now sits 16px away from it.
- **Link size:** I raised the link from 12px to 13px so it doesn't look tiny next to the button. Revert it if you'd rather keep 12px.
- **Corner radius:** I raised it from 5px to 8px to suit the extra padding. You can drop that line if you'd rather keep 5px.
