Two small things are worth fixing. The rest is fine.

1. **Body size is in pixels.** `17px` ignores the user's browser font-size setting. Use `1.0625rem`, which renders the same by default but scales with their setting.
2. **The h2 inherits `line-height: 1.6`.** That's loose for a heading and looks gappy if it wraps. Headings want about 1.1 to 1.25.

```css
article {font: 1.0625rem/1.6 system-ui; max-width: 66ch; margin: 0 auto;}
article h2 {font-size: 1.5rem; line-height: 1.25; margin: 2rem 0 .5rem;}
article p {margin: 0 0 1rem;}
```

These parts are fine:
- The unitless 1.6 body line height.
- The 66ch measure, which sits on the text container.
- The heading spacing, with more space above than below so the heading attaches to what follows.
- The paragraph gap.

I didn't find a file with this CSS in the working directory, so the corrected version is above for you to paste in. If the h2 will often wrap to two lines, you could also add `text-wrap: balance`, but that's optional.
