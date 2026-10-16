```css
.notice {
  box-sizing: border-box;
  width: 320px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  font: 14px/1.45 system-ui;
}

.notice h3 {
  margin: 0 0 12px;
  font-size: 18px;
  line-height: 1.25;
}

.notice p {
  margin: 0;
}

.who {
  font-weight: 600;
}

.items {
  margin-top: 4px;
}

.where {
  margin-top: 12px;
  color: #555;
}

.notice button {
  min-height: 40px;
  margin: 20px 12px 0 0;
  padding: 0 16px;
}

.notice a {
  display: inline-block;
  margin-top: 20px;
  padding: 10px 0;
  font-size: 13px;
}
```

What I changed:

- **Spacing scale:** the old values (7, 9, 11, 13, 2, 3, 1px) were all slightly different, which made it look uneven. Everything now uses 4, 12 and 20px steps.
- **Grouping:** the name and items sit close together (4px). The location is a bit further off (12px). The actions are set apart (20px).
- **Padding:** the card padding goes from 7px to 20px, so the text no longer touches the border. I added `box-sizing: border-box` so the card stays 320px wide.
- **Line height:** it goes from 1.1 to 1.45, which fixes most of the squashed look. The heading gets a tighter 1.25.
- **Button and link:** the button is 40px tall with 16px side padding, which is easier to tap on a pickup screen. The link now lines up with it and has 12px of space between them.

I used a `.notice p` reset so the paragraphs don't pick up browser default margins. If you'd rather keep the button at 24px, change `min-height` back and the rest of the spacing still works.
