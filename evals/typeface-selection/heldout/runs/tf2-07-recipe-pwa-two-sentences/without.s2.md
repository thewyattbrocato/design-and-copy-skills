Use a system font stack so nothing has to be downloaded and text renders instantly offline:

```css
font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

If you want a custom typeface, self-host it and precache the font files in your service worker, and keep the system stack as the fallback.
