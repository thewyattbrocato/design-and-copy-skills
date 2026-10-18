The hover rule sets the background to `#e8f3f0`, a pale tint, but the text stays white. Make the hover background a darker shade of the green so the white text keeps its contrast:

```css
.save:hover { background: #185a4b; }
```

`#185a4b` is a darker version of your `#1f6f5c`. White text on it has a contrast ratio of roughly 8:1, which is above the 4.5:1 AA minimum.

If you'd rather keep the pale hover look, change the text color on hover instead:

```css
.save:hover { background: #e8f3f0; color: #1f6f5c; }
```

I didn't find a stylesheet in the working directory, so I haven't edited any files. Paste the change into your CSS where `.save:hover` is defined.
