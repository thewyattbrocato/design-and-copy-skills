**Use one family, bundled in the app: Figtree.** It's friendly and modern without being thin or fussy, and it has a weight range, so the founder's look comes from weight and size rather than a second font.

```css
--font-ui: "Figtree", Roboto, system-ui, sans-serif;
```

Use it for everything: Regular for body, Medium or SemiBold for labels and buttons, Bold for headings and amounts. The one-line reason for the pick: a geometric-humanist sans with open shapes holds up better at small sizes than a purely geometric face, and it's open-source.

**Offline and prepaid data**
- **Bundle the font files in the app.** Don't use a Google Fonts link or any CDN. It fails with no connection and costs vendors data.
- **Ship one variable file or three static weights** (Regular, SemiBold, Bold), as WOFF2 if it's a web or PWA build. Subset to the languages you actually use.
- **Keep Roboto in the fallback.** It's already on every Android phone, so if the font fails to load, the app still looks fine and nothing breaks.
- **Don't add a second display font.** It's more download for no role the first font can't cover.

**Check these before committing**
1. **Money.** Confirm the font offers tabular figures and that your currency symbol is in it. If either is missing, amounts won't align in columns and the symbol will fall back to a different font.
2. **Look-alike characters.** Set `1 l I` and `0 O` at your smallest size, on a real mid-range phone. Vendors will be reading balances and contributions at a glance.
3. **Languages.** I assumed Latin script. If you need Swahili, Vietnamese, Hindi, Arabic or others, check Figtree's coverage and tell me. The harder script should drive the choice.
4. **License.** I believe Figtree is under the SIL Open Font License, but confirm that on the font's source page before shipping.
5. **Weights.** Use real weights only. If you use italics, make sure the family includes them, and set `font-synthesis: none` so the browser doesn't fake bold or italic.

If the founder wants something rounder and warmer, **Nunito** is the alternative. Its rounded ends read as "friendly" more obviously. The same offline and bundling advice applies.

If this is a native or React Native app rather than web, tell me and I'll translate this into the font-loading setup for that platform.
