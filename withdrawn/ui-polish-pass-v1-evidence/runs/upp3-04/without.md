Change the hover background to a darker shade of the same green so the white text stays readable:

```css
.save:hover { background: #17584a; }
```

`#17584a` against `#fff` has a contrast ratio of about 8:1, which is higher than the default state's roughly 6:1. The button gets darker on hover and the text stays legible.

The original rule set the background to `#e8f3f0`, a pale tint, while `color: #fff` stayed the same. That made the white text nearly invisible. If you'd rather have a light hover state, also set `color: #1f6f5c` in the same rule.

I didn't edit any files, since the CSS was pasted inline and I don't know where it lives in your project.
