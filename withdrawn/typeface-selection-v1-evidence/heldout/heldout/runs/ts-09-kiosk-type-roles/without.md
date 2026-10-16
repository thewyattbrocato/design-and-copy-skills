# Type plan for the Lantern Row kiosk

## Families: two
1. **A system sans for all interface text**: search, titles, authors, buttons, confirmation copy.
2. **A system monospace for "codes"**: shelf codes and the receipt.

I wouldn't add a third family or a serif for titles. You can't ship a display face, and a system serif adds nothing at this viewing distance. Hierarchy should come from size and weight (400 and 600 only). Avoid thin, light, and italic styles, which break up on a touchscreen viewed at arm's length.

## Which face for which job

| Job | Face | Notes |
|---|---|---|
| Search field and keyboard keys | Sans 600 | Large, with the placeholder at 400 |
| Book title | Sans 600 | Wrap to 2 lines; don't truncate silently |
| Author | Sans 400 | One step smaller than the title |
| Shelf code (`QB 412.7`) | Mono 600 | See below |
| Due date | Sans 600 | See below |
| Copies available | Sans 400, plus a number in 600 | "2 of 3 available", never colour alone |
| Confirmation headline | Sans 600 | Biggest text on the screen |
| Receipt | Mono 400, with 600 for totals and due date | Echoes a printed receipt |

## Sizes
I'm assuming a 1920×1080 panel, which is about 140 ppi, so 1 CSS px ≈ 0.18 mm. Check this against the real screen. If it's lower resolution, the pixel values change but the physical sizes should stay the same.

- **Floor for any text:** 24 px, about 4.3 mm em. That's roughly 14 pt in print terms, which suits half a metre and older eyes. Nothing smaller, including legal or footer text.
- **Body, author, due date, copies:** 24–26 px
- **Title:** 32–34 px
- **Shelf code:** 30 px (mono looks smaller at the same size)
- **Search input:** 36–40 px
- **Screen headlines:** 48 px
- **Line height:** 1.3–1.4. Keep the lines short, because nobody reads paragraphs at a kiosk.

Test on the real panel with a ruler and a few real users. Standing at 50 cm is different from sitting at a laptop.

## Shelf codes
The code is the thing a patron has to carry to the shelf, so it should look different from the prose around it.
- **Set it in mono, uppercase, and put it in a bordered or tinted tag.** That separates it from title and author and signals "copy this exactly".
- **Mono helps with lookalikes:** 0/O, 1/I/l, 8/B, Q/O. Where the font supports it, turn on a slashed or dotted zero (`font-variant-numeric: slashed-zero`).
- **Never let it wrap.** Use `white-space: nowrap` and a non-breaking space between `QB` and `412.7`.
- **Add a small label above or beside it**, such as "Shelf" at 24 px/400, so kids and first-timers know what it is.
- **Make it as large as the title or nearly so**, since finding the book is the point of the card.

## Due dates
- **Use an unambiguous format:** "Due Thu 12 Nov", with the weekday and a spelled-out month. Never `12/11/26`, which reads differently to different patrons.
- **Add the year only on the receipt and confirmation:** "Thu 12 Nov 2026".
- **Use tabular figures** (`font-variant-numeric: tabular-nums`) so dates line up when cards stack in a list.
- **Weight 600, same size as body.** The label "Due" stays 400, so the date stands out without needing colour.
- **Optional relative hint** on the confirmation screen: "That's 3 weeks from today."
- **On the receipt**, use mono, one item per line, with the due date on its own line under the title.

## Font stack
The OS image decides what's available, so please find out which OS it is. Keep the stack short, because every fallback has different metrics and a surprise fallback can break line wraps.

```css
--sans: system-ui, "Segoe UI", "Helvetica Neue", Arial, sans-serif;
--mono: ui-monospace, "SF Mono", Menlo, Consolas, "DejaVu Sans Mono", monospace;
```

- If the image is Windows, Segoe UI and Consolas are solid.
- On macOS, SF and Menlo are fine.
- On a Linux or kiosk image, check for DejaVu or Noto before you rely on anything. If you can choose, Verdana is a strong sans for distance reading, with a large x-height and open spacing.
- Whichever it is, lock the stack to what's installed and screenshot every screen on the actual image. Check that tabular figures and the slashed zero actually render, because some system fonts ignore those OpenType features.

## Open question
Which OS is the image? Once I know, I can narrow the stacks to a single named font per role and adjust the sizes for the actual panel resolution.
