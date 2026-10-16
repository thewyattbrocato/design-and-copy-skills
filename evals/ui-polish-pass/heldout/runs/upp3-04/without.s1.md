The hover background (`#e8f3f0`) is nearly white, so the white text disappears. Here's the fix, which darkens the button on hover and keeps the text readable:

```css
.save:hover { background: #17584a; }
```

`#17584a` is a darker shade of the base green (`#1f6f5c`). White text on it has a contrast ratio of about 8:1, which is better than the base state.

If you'd rather keep the light hover look, change the text color too:

```css
.save:hover { background: #e8f3f0; color: #1f6f5c; }
```

That gives the green text about 5.5:1 contrast on the pale background. You may also want a visible border in that version so the button doesn't blend into the white card.

I didn't edit any files, since the CSS was pasted inline and I don't know which file it lives in. Tell me the path and I'll apply it.
