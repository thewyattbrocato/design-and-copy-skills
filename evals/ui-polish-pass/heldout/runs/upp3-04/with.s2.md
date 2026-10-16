Change the hover background to a darker shade of the green instead of the pale tint:

```css
.save:hover { background: #17564a; }
```

`#17564a` is a darker version of `#1f6f5c`, so the white text stays readable (contrast is about 8:1). Nothing else needs to change.

If you'd like keyboard users to get the same feedback, use `.save:hover, .save:focus-visible { background: #17564a; }`.
