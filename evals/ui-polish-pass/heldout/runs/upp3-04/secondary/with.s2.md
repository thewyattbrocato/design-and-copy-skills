The hover rule changes the background to a pale green but leaves the text white, so the label becomes unreadable. Use a darker green on hover so the white text stays readable:

```css
.save:hover { background: #185a4b; }
```

If you'd rather keep the pale hover, set the text color in the same rule so the two change together:

```css
.save:hover { background: #e8f3f0; color: #1f6f5c; }
```

I went with the darker option because it keeps the button's identity and white-on-green contrast. I haven't edited any file, since the CSS was pasted inline and I don't know where it lives in your project.
