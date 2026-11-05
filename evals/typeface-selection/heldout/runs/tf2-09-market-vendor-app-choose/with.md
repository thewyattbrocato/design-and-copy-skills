**Use one family, bundled inside the app: Nunito Sans.** Use Regular for body, SemiBold for labels and buttons, and Bold for headings and amounts.

I'm assuming a Latin-script audience, so tell me if you need other scripts. That would change the pick, because the harder script comes first.

**Why this works for your users**
- **Friendly and modern:** Nunito Sans has soft, open shapes and a warm tone, but it is still a sturdy sans. It stays clear at small sizes on mid-range screens, and the founder gets the look they asked for.
- **One family:** The hierarchy comes from weight and size, so there's no second font to download or to clash with the first. A second family has no role here.
- **Offline and prepaid data:** Bundle the font files in the APK or app bundle and never load them over the network. Ship only the three weights above, subset to the languages you support. Don't use a CDN or Google Fonts links, because they would fail offline and spend the vendors' data.
- **Fallback:** Use `Roboto` (the Android system font) as the fallback. If a file fails to load, the app still looks sensible.

**Rules to keep it legible on those phones**
- Use 16sp as the minimum for body text and 14sp for the smallest labels.
- Don't use Light or Thin weights. They get spindly on low-density screens.
- Money and counts need tabular figures, so columns of amounts line up. Check that your chosen build of Nunito Sans supports them. If it doesn't, use a different family rather than faking it.
- Test the smallest text on a real mid-range device. Check that 1, l, I, 0 and O can be told apart, since these will be amounts and member IDs.
- Don't rely on synthetic bold or italic. Only bundle weights the family actually provides.

**Licensing:** Nunito Sans is listed on Google Fonts as an open-license family, but confirm the terms yourself for app embedding before you ship.

**Backup option:** If APK size or time matters more than the look, use plain Roboto. It costs nothing, always works offline, and is familiar to your users. A friendlier feel then has to come from color, spacing and rounded UI shapes.
