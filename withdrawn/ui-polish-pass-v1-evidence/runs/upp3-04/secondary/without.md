The hover rule sets a pale background but leaves the text white, so the label disappears. Changing the hover background to a darker shade of the same green keeps white text readable:

```css
.save:hover { background: #185c4d; }
```

If you want the pale hover look, change the text color on hover too:

```css
.save:hover { background: #e8f3f0; color: #1f6f5c; }
```

I haven't run this in your app because the CSS is only inline here. I'd go with the darker option, since it keeps the button's original look and the white text contrast.
