# Lantern Row kiosk type plan

**Assumptions:** Latin script, a 1920×1080 panel (about 0.18 mm per pixel), and an unknown OS image, so the stacks below name only common system fonts. Please check the real pixel pitch and which fonts the image has before you sign off.

## Families: one sans, plus mono for shelf codes only

| Job | Face | Why |
|---|---|---|
| Everything: search, titles, authors, dates, buttons, receipt | System UI sans, weights 400, 600 and 700 | System UI sans faces are sturdy, open and tuned for the OS renderer. Hierarchy comes from size and weight, so there is no second text family to match. |
| Shelf codes (`QB 412.7`) | System mono, semibold | The code is an identifier people match letter for letter against a spine label. Mono keeps every character distinct and the same width, and its zero is usually slashed or dotted. |

I rejected a serif for titles. Everything here is short and glanceable, and a serif would add a second voice with no job to do.

```css
:root {
  --font-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "DejaVu Sans", sans-serif;
  --font-code: ui-monospace, "SF Mono", Menlo, Consolas, "Liberation Mono", "DejaVu Sans Mono", monospace;
}
body { font-family: var(--font-ui); font-synthesis: none; font-variant-numeric: tabular-nums; }
```

## Sizes

These are starting points, sized so cap height is about 4 mm or more at half a metre. Test them on the real panel. If the pitch differs, use `px = mm ÷ pitch`.

| Role | Size | Weight |
|---|---|---|
| Screen heading ("Search the catalogue", "Checked out") | 56px | 700 |
| Search field text | 40px | 400 |
| Result title | 40px | 700 |
| Author, due date, availability | 32px | 400 for author, 600 for due date and availability |
| Shelf code | 48px | 600, mono, letter-spacing 0.04em |
| Buttons | 36px | 600 |
| Receipt body | 32px | 400 |
| Smallest text anywhere (hints, footer) | 28px | 400 |

- Use 400 as the lightest weight anywhere. Keep light and thin cuts off the screen, since older readers and glare will lose them.
- Don't use italics or small caps. Emphasis comes from weight and size.
- Don't set text in all caps, apart from the code letters themselves.

## Shelf codes

- **Make them the largest text on the card.** They are the answer a patron walks away with. Set them at 48px, semibold mono, in a bordered chip with generous padding, with the words "Shelf" in 28px above.
- **Never break or wrap a code.** Use `white-space: nowrap`. The space in `QB 412.7` should be a real space at full width.
- **Keep the code in one place.** Put it on the same side of every card and on the receipt, so people learn where to look.
- **Check the ambiguous glyphs** (Q/O/0, I/1/l) in the real mono. Do this with actual codes from your catalogue, not made-up ones.

## Due dates

- **Spell the month and add the weekday:** `Due Fri 23 Oct 2026`. Numeric dates like 23/10 and 10/23 are ambiguous for a mixed audience.
- **Use tabular figures** (`font-variant-numeric: tabular-nums`) so dates and counts line up down a list.
- **Set the due date in 600 weight.** It is the fact people forget. On the confirmation and receipt, make it the largest line after the title.
- **Write copies in words:** `2 of 3 available`, or `None available`. Don't rely on a bare "2". Reinforce the state with an icon or label as well as colour.

## Screens

- **Search:** a 40px field with a 56px heading above it. Put the on-screen keyboard keys at 36px, weight 600.
- **Result cards:** the title is 700, then the author, then a row with the shelf chip, the due date and the availability. Keep the same order on every card.
- **Check-out confirmation:** the heading, the title, and the due date at 40px, 600.
- **Receipt:** the same sans at 32px, with titles and dates in tabular figures. Put the shelf code in mono. Keep the layout to a single column.

## Caveats

- **The same stack renders differently on each OS.** A Linux image might give DejaVu Sans, which is wide and sturdy, so check that titles don't wrap badly. A Windows image gives Segoe UI.
- **If the stack looks generic or uneven on the kiosk,** ask IT to install one open-licensed, high-legibility family in the OS image. Atkinson Hyperlegible, designed for low-vision readers, is a good candidate. Confirm its licence and that it covers the characters in your catalogue before relying on it. Keep the system stack after it as the fallback.
- **Long titles:** test the longest title in the catalogue at 40px and decide how many lines a card allows before it truncates. Truncate with an ellipsis and never shrink the type.
