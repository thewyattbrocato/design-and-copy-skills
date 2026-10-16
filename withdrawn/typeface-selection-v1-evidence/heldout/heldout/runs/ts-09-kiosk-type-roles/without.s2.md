# Type plan: Lantern Row kiosk

## Families: two

| Job | Face | Why |
|---|---|---|
| Everything: search, titles, authors, buttons, confirmation, receipt text, due dates | One system sans, regular and bold only | One family keeps the screens consistent and easy to scan. At 0.5 m on a touchscreen, a serif adds nothing. |
| Shelf codes only (plus the receipt's copy of them) | A system monospace | The code is something a patron copies by eye onto a shelf label. `QB` has a Q that mustn't read as O, and `412.7` has digits that mustn't read as letters. Monospace faces generally have a slashed or dotted zero and distinct 1/l/I. The fixed width also makes codes line up down a list of results. |

I wouldn't add a third family for headlines or branding. Weight and size give you enough hierarchy.

## Weights

Use **400 and 700 only**. System fonts often lack intermediate weights, and the browser fakes them unevenly. Skip light weights entirely, since thin strokes break up at distance on a 15" panel. Skip italics too. Synthesized slants on system fonts look rough, and the hierarchy doesn't need them.

## Stacks

```css
:root {
  --sans: system-ui, "Segoe UI", "SF Pro Text", Roboto, "Noto Sans",
          "DejaVu Sans", Verdana, sans-serif;
  --code: ui-monospace, Consolas, Menlo, "SF Mono", "DejaVu Sans Mono",
          "Liberation Mono", monospace;
}
```

I left Courier New and Lucida Console out of the monospace stack on purpose. Courier is thin and poor at distance, so it's better to fall through to the generic `monospace`. I can't see your OS image. Ask whoever builds it for the installed font list, then test both stacks on the real kiosk. Confirm which face actually renders, and especially that the `0` and `O` are distinguishable.

## Sizes

I'm assuming roughly 1920×1080 on 15", about 147 ppi. Please confirm the real resolution. The rule I'm working from is that the smallest text should have a cap height of about 3 mm or more, which works out to about 22–24 px at that density. Define sizes in `rem` so you can scale the whole system with one root value if the panel differs.

| Element | Size | Weight |
|---|---|---|
| Screen headline (confirmation, "Your receipt") | 48 px | 700 |
| Book title on a card | 32–36 px | 700 |
| Shelf code | 36–40 px (mono) | 700 |
| Due date | 28–32 px | 700 for the date, 400 for the label |
| Author, copies available, body text | 24–26 px | 400 |
| Button labels, search input | 28–32 px | 700 / 400 |
| Floor for anything (labels, hints) | 22 px | 400 |

Set line-height to about 1.3–1.4 and use true black or near-black on white or very light grey for contrast. Don't use grey for secondary text. Make it smaller or regular weight instead.

## Shelf codes

- Set them in the monospace at the largest size on the card, bold, in caps.
- Put them in a bordered or filled tag so they read as "the thing to take to the shelf".
- Keep the space between the class and the number (`QB 412.7`) and render it as two groups. Add a little extra letter-spacing, about 0.05em, so the period in `412.7` doesn't disappear.
- Never wrap or truncate a code. If the card is tight, shrink the title, not the code.
- Repeat the code on the receipt in the same face.

## Due dates

- Spell out the month and include the weekday, e.g. **Tue 4 Nov 2026**. Never use `04/11/26`, which is ambiguous between day-first and month-first readers.
- Format with `Intl.DateTimeFormat` using the kiosk's locale, with `{ weekday: 'short', day: 'numeric', month: 'short', year: 'numeric' }`.
- Apply `font-variant-numeric: tabular-nums` so dates align in lists and on the receipt.
- Use a regular-weight label ("Due back") with the date in bold beside or below it.
- On the confirmation and receipt screens, the due date should be the largest non-headline element. It's the one fact people need to remember.

## Other card details

- **Titles:** allow two or three lines and wrap them, rather than cutting them off with an ellipsis. Titles are what people are matching against. If you must clamp, make the full title available on tap.
- **Copies available:** write it out, e.g. "2 of 3 available" or "None available". Don't rely on a bare number or on color alone to show status.
- **Search field and on-screen keyboard:** use the same sans, with key labels in bold 28 px or larger. Keep letter keys in caps and let the typed text show as typed.
- **All caps:** use it only for shelf codes and short key labels, never for titles or sentences.

## Receipt

The receipt uses the same two faces, so it matches the screen. If you print it on a thermal printer, the printer's own font takes over. In that case, check that the shelf code and due date are still easy to tell apart on paper.

If you tell me the actual panel resolution and the OS, I can tighten the stacks and sizes. I can also turn this into a CSS file with the type tokens and a sample result card for you to test on the device.
