Use a system font stack so nothing has to be downloaded and it works offline from the first load:

```css
font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

If you want a custom typeface, self-host it as a WOFF2 file and precache it in your service worker. Use `font-display: swap`, and don't load it from Google Fonts' CDN.
