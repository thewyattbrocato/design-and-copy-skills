```css
.notice {
  box-sizing: border-box;
  padding: 16px;
  width: 320px;
  border: 1px solid #ccc;
  border-radius: 8px;
  font: 14px/1.45 system-ui;
}

.notice h3 {
  margin: 0 0 12px;
  font-size: 17px;
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
  margin-top: 4px;
  color: #555;
}

.notice button {
  height: 40px;
  padding: 0 16px;
  margin: 16px 12px 0 0;
}

.notice a {
  display: inline-block;
  padding: 8px 0;
  font-size: 12px;
}
```

What changed:

- **Line height:** It was 1.1, which made the text feel squashed. It's now 1.45.
- **Padding:** The container padding went from 7px to 16px, so the content has room from the border. I added `box-sizing: border-box` so the notice stays 320px wide.
- **Spacing scale:** The odd margins (9, 2, 11, 1, 13, 3) are replaced with a 4/8/12/16 scale. The name, items and location lines now sit 4px apart. The title has 12px below it, and the button has 16px above it.
- **Button:** It's now 40px tall with 16px side padding, which is easier to tap on a pickup screen. It has 12px of space before the "Report a problem" link.
- **Link:** I gave it vertical padding so it has a bigger tap target and lines up better with the button.
