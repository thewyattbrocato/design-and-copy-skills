# Type plan: Lantern Row self-service kiosk

**Assumptions:** The screen is 1920×1080 at 1× (about 147 ppi at 15 inches). The text is Latin script, and you haven't said which OS the image runs. Everything below depends on that OS, so first check which system fonts it ships.

## Families: one sans, plus mono for two jobs

| Job | Face | Why |
|---|---|---|
| Everything: search, titles, authors, buttons, due dates, confirmation, receipt prose | **System UI sans**, 400 / 600 / 700 | Every screen is scanning text read at a glance. One family with real weights gives the hierarchy through weight and size, and kids and older readers don't have to adjust to a second voice. |
| **Shelf codes** and the receipt's aligned columns | **System mono**, bold | The shelf code is an identifier that people copy by eye and carry to a shelf. Mono gives each character the same width and a distinct 0/O, so QB 412.7 can't be misread. |

I'm not adding a serif or a display face. There's no long reading and no brand moment, and a second text family would be a face with no job.

```css
:root {
  --font-ui:   system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-code: ui-monospace, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
}
body {
  font-family: var(--font-ui);
  font-synthesis: none;            /* no faked bold or italic */
  font-variant-numeric: tabular-nums;
}
:lang(en) { }                      /* set <html lang> so glyph variants are correct */
```

## Starting sizes

These are for 1080p at about 0.5 m. Scale them by the real pixel density, then check on the device.

| Role | Size / weight |
|---|---|
| Screen heading | 56px, 700 |
| Search field text | 36px, 400 |
| Book title on card | 36px, 600 |
| Author | 28px, 400 |
| **Shelf code** | **44px, mono 700** |
| Due date | 28px, 600 |
| Copies available, labels, buttons | 28px, 600 |
| Receipt body | 26px |
| Absolute floor, anywhere | 24px, never below weight 400 |

Don't use light weights anywhere. They break up at this distance, and on a touchscreen with a protective film they look worse.

## Shelf codes

- Put each code in its own chip, set in mono bold at the largest size on the card. It's the one thing people leave the kiosk to act on, so it should be the biggest text on the card. Add generous letter-spacing (about 0.04em).
- Keep the letters uppercase and the space between letters and number fixed: `QB 412.7`. Use a real non-breaking space so it never wraps mid-code.
- Check that the mono has a slashed or dotted zero. Menlo, Consolas and DejaVu Sans Mono do. If the OS image has none of them, the generic `monospace` fallback decides, so test it.
- Print the same code in the same mono on the receipt, so what people see on screen matches what they hold.

## Due dates

- Spell the month and include the weekday: **Due Tue 27 Oct**. Never use `27/10/26` or `10/27/26`, because kids and visitors will read the numerals differently.
- On the confirmation and receipt, give the due date its own line at 600 weight, with the label ("Due back") smaller and in regular weight above it.
- Use `tabular-nums`. When several loans are listed, the dates then line up in a column.
- Write copies as words with numbers: **2 of 3 available**. When none are left, show "None available" in 600 weight, with an icon or label so the status doesn't depend on color alone.

## Receipt

Use the sans for titles and the due date, and the mono for the shelf code and any column of figures. Keep a title that wraps to two lines at the same size rather than shrinking it. Cap the title at two lines on result cards, with the full title on the confirmation screen.

## Before sign-off

1. **Confirm the OS image's fonts.** `system-ui` resolves to Segoe UI on Windows, SF on macOS and whatever the distribution chose on Linux. On a stripped Linux image it may become DejaVu Sans, which is wider and changes how titles wrap. If the image is yours to choose, ask for one humanist or grotesque sans with a 600 weight installed, and I can name a specific one once I know what's available.
2. **Set a specimen on the device.** Use the longest title in the catalogue, an author name with diacritics, `QB 412.7` next to `OB 4l2.7`-style lookalikes, and a due date. Read it standing at half a metre.
3. **Have a child and an older reader test it.** Ask them to read the shelf code aloud. If either hesitates, raise its size or its weight before touching anything else.
