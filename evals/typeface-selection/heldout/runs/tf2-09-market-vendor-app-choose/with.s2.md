**Use one family, bundled in the app: Nunito Sans.** It's friendly without being childish, and it holds up at small sizes. Use Regular, SemiBold and Bold for everything. Hierarchy comes from weight and size, not a second font.

I'm assuming a Latin-script audience, an installed app (not a website), and no brand font yet. If your vendors read Devanagari, Arabic, Amharic or another script, tell me. Then you should choose for that script first, because Nunito Sans won't cover it.

**Why this fits your constraints**
- **Offline and prepaid data:** bundle the font files in the app package. Don't fetch fonts at runtime. Ship a variable file or three static weights, subset to the languages you support. Skip italics unless you use them.
- **Mid-range screens:** it has open letterforms and a generous x-height, so 14–16sp text stays readable. Fully rounded faces like Nunito, Quicksand or Poppins look friendlier but blur at small sizes on lower-density screens. Save those for a logo or splash screen, not UI text.
- **Money:** amounts and contribution counts need digits of equal width so columns line up. Turn on tabular figures (`tnum`). Check this on the exact build you ship, because I haven't verified feature support in the specific files.
- **License:** I believe it's open (OFL), but confirm that on the font's source page before shipping.

**Fallback:** if the bundled font fails to load, fall back to Roboto, which is already on every Android phone. In CSS or a webview that's `"Nunito Sans", Roboto, system-ui, sans-serif`. In a native app, set the fallback in your theme.

**Starting sizes**
- Body: 16sp.
- Labels and captions: 14sp minimum.
- Money and key numbers: 20–24sp SemiBold or Bold.
- Screen titles: 22–28sp Bold.

**If you want zero font weight in the app:** use Roboto only. It costs nothing, renders crisply on every Android device, and still looks modern. You can get most of the "friendly" feel from rounded corners, color and illustration. The tradeoff is that it looks like every other Android app.

Before you commit, put a real screen on a cheap phone, in sunlight, at the smallest size you use. Check that a balance like "1,250.00" and a name like "Ilona" read clearly. If they do, you're done.
