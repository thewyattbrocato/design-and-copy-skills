Use a system font stack so nothing needs to be downloaded and text renders instantly offline:

```css
font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

If you want a custom typeface, self-host it as WOFF2 and precache it in your service worker, with `font-display: swap`. Skip Google Fonts CDN links, since they won't load offline unless cached.
