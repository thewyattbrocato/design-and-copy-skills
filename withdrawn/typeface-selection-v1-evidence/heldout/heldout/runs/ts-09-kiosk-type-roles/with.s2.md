# Lantern Row kiosk type plan

**Assumptions:** 1920×1080 on the 15" panel, about 50 cm viewing distance, Latin script, and an OS image whose fonts I haven't seen. Check the sizes against the real panel.

## Families: one

Use a single system UI sans for everything. Nothing on these screens is long reading, so a serif would add a second family with no job. Hierarchy comes from size and weight: 400, 600 and 700. A bare sans at one weight would flatten the cards, so the weights are fixed per role below.

```css
:root {
  --font-kiosk: system-ui, -apple-system, "Segoe UI", Roboto, "Noto Sans",
                "Helvetica Neue", Arial, "Liberation Sans", sans-serif;
}
body {
  font-family: var(--font-kiosk);
  font-synthesis: none;              /* no faked bold or italic */
  font-variant-numeric: lining-nums tabular-nums;
}
```

- **Fallbacks:** the stack resolves to San Francisco on macOS and Segoe UI on Windows. On Linux or ChromeOS it resolves to Roboto or Noto Sans, then Liberation Sans. These are all sturdy, open-aperture sans faces. I can't see your image, so tell me the OS and I'll trim the stack to what it actually has.
- **Check before sign-off:** render `Oo0 Il1`, `QB 412.7` and your longest real title on the kiosk itself. If `0/O` or `I/l/1` look alike in whatever face wins, that's the one reason to change the stack.
- **No light cuts.** Never go below weight 400. Distance and glare thin out strokes.

## Sizes by role (starting points)

| Role | Size | Weight |
|---|---|---|
| Screen heading | 56px | 700 |
| Search field text and placeholder | 36px | 400 |
| Book title on card | 36px | 600 |
| Author | 28px | 400 |
| **Shelf code** | **44px** | **700** |
| Due date and copies available | 28px | 600 |
| Buttons | 32px | 600 |
| Receipt body | 26px | 400 |
| Floor for any text | 24px | 400 |

At 50 cm, 24px text has a cap height of about 3 mm, which is the practical minimum. Don't shrink text to fit a long title. Wrap it to two lines and truncate after that, and make the card taller if needed. Older readers should be able to read everything without leaning in.

## Shelf codes

The shelf code is what sends someone to the right shelf, so it should be the biggest thing on the card.

- Set `QB 412.7` in the same sans at 44px, weight 700, with `letter-spacing: 0.04em`. Put it in a bordered or tinted chip so it reads as a label rather than prose.
- Keep the letters uppercase and the space between letters and number exactly as shelved.
- Use tabular figures so a column of codes lines up.
- Don't use monospace unless the specimen test shows your system sans confuses `0/O` or `1/I`. Monospace is for aligned code, and here it would add a second family for little gain.
- If the codes carry more structure than `QB 412.7` (volume, cutter), keep the same chip and scale the extra part down by one step. Don't change the face.

## Due dates

- Spell out the month so nobody has to guess day or month order: **Due Tue 4 Nov** (add the year on the receipt, e.g. "Due Tue 4 Nov 2026"). Avoid `04/11/26`, which readers will interpret differently.
- Use 28px at weight 600 on the card, with tabular figures so dates line up down the receipt.
- Put "Due" in weight 400 and the date in 600. That gives emphasis without a second face or italics.
- Write the copies line in words: **2 of 3 copies available**, or **None available**. Don't rely on a bare `2/3`.

## Per screen

- **Search:** the field text is 36px with a visible caret. Keep the keyboard keys at 32px, weight 600, with uppercase letters on the keycaps.
- **Results:** use the card layout above. Order is title, author, shelf code chip, then due date and copies.
- **Check-out confirmation:** the heading is 56px. Repeat the title and the due date at card sizes, and keep the button labels to a single verb ("Check out", "Cancel").
- **Receipt:** 26px floor, tabular figures, and a right-aligned due-date column. The same family works if the receipt is also printed.

## Open question

Which OS image is the kiosk running? I've assumed only stock system fonts. Once I know, I can cut the stack to one or two real names and say exactly what each screen will render in.
