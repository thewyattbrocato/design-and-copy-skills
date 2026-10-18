Change the hover background to a darker shade of the green, so the white text stays readable:

```css
.save:hover { background: #17564a; }
```

`#17564a` against `#fff` has a contrast ratio of roughly 8:1, which is well above the 4.5:1 AA minimum. The original `#1f6f5c` is about 5.8:1, so hover reads as a slight darkening, which is the usual feedback.

If you'd rather keep the pale hover look, flip the text color too:

```css
.save:hover { background: #e8f3f0; color: #1f6f5c; }
```

That gives about 5.2:1, which also passes. I'd go with the darker background, since it matches the button's resting state more closely.

You may also want a `:focus-visible` style, so keyboard users get the same feedback:

```css
.save:hover,
.save:focus-visible { background: #17564a; }
```

I haven't touched any files, since the CSS was pasted inline. Tell me where it lives if you'd like me to edit it directly.
