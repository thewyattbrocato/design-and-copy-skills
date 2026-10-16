```css
.notice {
  box-sizing: border-box;
  width: 320px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  font: 14px/1.45 system-ui;
}

/* reset default paragraph/heading margins so spacing is set in one place */
.notice h3,
.notice p {
  margin: 0;
}

.notice h3 {
  margin-bottom: 12px;
  font-size: 18px;
  line-height: 1.25;
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
  height: 36px;
  padding: 0 16px;
  margin: 20px 12px 0 0;
  vertical-align: middle;
}

.notice a {
  font-size: 13px;
  vertical-align: middle;
}
```

What changed:
- **Padding:** 7px is now 20px, so the content has room inside the border. I added `box-sizing: border-box` so the card stays 320px wide.
- **Line height:** 1.1 is now 1.45, which was the main cause of the squashed look.
- **Spacing scale:** the margins were an arbitrary mix (9, 2, 11, 1, 13). They're now 4, 12 and 20, which gives a steady rhythm. The name and items sit close together as one group. The pickup location, the heading and the actions each get a larger gap.
- **Margin reset:** `h3` and `p` margins are zeroed first, so browser defaults no longer add uneven gaps.
- **Button and link:** the button is 36px tall (was 24px) with 16px side padding, which makes it an easier tap target. The link is vertically aligned with it, and there's a 12px gap between them.
