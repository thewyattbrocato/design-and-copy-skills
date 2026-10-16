Use a system stack so it renders identically offline with no font files to cache. For a recipe app, a UI stack works well:

```css
font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

If you want a warmer feel for the recipe text, use `font-family: Charter, "Iowan Old Style", Georgia, serif;` for the body and keep the UI stack for buttons and labels.
