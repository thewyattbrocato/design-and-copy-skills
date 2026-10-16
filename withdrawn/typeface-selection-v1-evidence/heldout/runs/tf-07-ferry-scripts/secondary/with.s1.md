**Use one face per script, not one family for everything.** Each script needs its own face, and the stack picks the right one per character. Assumed: a web app, Latin-script UI chrome, system fonts as fallback, and no locked brand face.

**Recommended stacks (open Noto families; confirm license and coverage for your use):**

```css
:root {
  --font-latin: "Noto Sans", system-ui, sans-serif;
  --font-arabic: "Noto Sans Arabic", "Noto Naskh Arabic", "Geeza Pro", Tahoma, sans-serif;
  --font-ja: "Noto Sans JP", "Hiragino Sans", "Yu Gothic", sans-serif;
  --font-ui: var(--font-latin), var(--font-arabic), var(--font-ja);
}
```

- **Alert card (headline and body):** Use semibold for the headline and regular for the body, in each script's sans. Keep the body at a size where Arabic and Japanese read as large as the Latin, since Arabic and CJK often look smaller at equal point size.
- **Departures list:** Use the Latin sans with tabular figures for times and platform numbers, so columns align. Stop names and destinations use the script of their own text.
- **Display (optional):** Use a Naskh or Kufi face for a large Arabic heading only if it matches the sans weight. Otherwise keep one sans per script.

**Mixed text, the part that breaks most often:**

- **Set `lang` on every element.** Use `lang="ar"` and `lang="ja"`. The browser uses it to choose glyph variants and line-breaking rules. Without it, Japanese can render with the wrong regional forms.
- **Isolate Latin stop names inside Arabic.** Wrap each one: `<bdi lang="en" dir="ltr">Harbour Quay</bdi>`. Without isolation, punctuation and word order around the name can flip in the RTL paragraph.
- **Keep Latin stop names in Japanese in the Latin face.** Wrap them in `<span lang="en">` and leave the spaces between words in place. Japanese fonts draw Latin acceptably, but the Latin run reads better in the Latin sans.
- **Give tall scripts room.** Arabic marks and Japanese kana need about 1.5 to 1.7 line-height. Test a two-line alert at the smallest size you ship.

**Loading and fallbacks:**

- Subset each Noto family by script with `unicode-range`, and self-host two to four files. Preload only the file the alert card needs first.
- Set `font-display: swap` and fallback metrics (`size-adjust`, `ascent-override`) so the card does not jump when the web font arrives.
- Test offline: with no web fonts, the system fallbacks above should still look intentional. Check this on a real device with Arabic and Japanese data, not only in English.

**Two notes:**

- I have not verified the current Noto coverage or license terms for your use. Check both with the font project before shipping.
- If you have a locked brand face, tell me and I'll rework the stacks around it.
