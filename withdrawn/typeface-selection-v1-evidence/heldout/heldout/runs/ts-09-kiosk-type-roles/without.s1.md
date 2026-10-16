# Type plan: Lantern Row self-service kiosk

## Families: two, each with one job

| Role | Family | Used for |
|---|---|---|
| **Interface sans** | `system-ui, "Segoe UI", "Noto Sans", "Helvetica Neue", Arial, sans-serif` | Everything except shelf codes: titles, authors, buttons, labels, dates, receipt text |
| **Shelf-code face** | `ui-monospace, "SF Mono", Consolas, "DejaVu Sans Mono", "Liberation Mono", monospace` | Shelf codes only (e.g. `QB 412.7`) |

- I'd skip a serif. System serifs vary too much between OS images, and a serif title at 0.5 m on a touchscreen adds nothing.
- Check which OS the image is. If it's Windows, Segoe UI is first in the stack. If it's Linux, make sure Noto Sans or DejaVu is actually installed, because `system-ui` on a bare Linux image can fall to something thin and ugly.
- Use only regular (400) and bold (700). Locked-down images often lack 500 and 600, and the browser then fakes them with inconsistent results.
- Don't use light weights, italics, or all-caps for anything longer than a label.

## Size scale

These sizes assume a 1920×1080 panel at 100% scaling, which is about 140 ppi, so 1 px is about 0.18 mm. At 500 mm viewing distance that makes 28 px about 5 mm, or roughly 0.6° of visual angle. **Measure on the real panel**, since the OS scaling setting changes everything. Keep the ratios and rescale if needed.

| Element | Size | Weight |
|---|---|---|
| Screen heading ("Find a book") | 56 px | 700 |
| Search input text | 40 px | 400 |
| Book title on card | 36 px | 700 |
| **Shelf code** | **48 px** | 700, mono |
| Author, due date, availability | 28 px | 400 (date value 700) |
| Button labels | 32 px | 700 |
| Floor for anything on screen (hints, fine print) | 24 px | 400 |

Set line-height to 1.3–1.4 and align text left. Keep lines under about 45 characters. Never go below 24 px, even for "minor" text, because older readers will hit it first.

## Book result cards

Read order: **title → shelf code → author → availability → due date.** The shelf code is the thing someone physically walks off with, so it gets the biggest type on the card, bigger than the title.

- Show the shelf code in the mono face inside a bordered chip with high contrast. Monospace keeps `0`/`O`, `1`/`I` and the decimal point distinct, and the even spacing suits a code that people read character by character.
- Always uppercase the letters. Put a no-break space between the letters and the number, and set `white-space: nowrap` so a code never splits across two lines.
- Add `font-variant-numeric: tabular-nums slashed-zero`. It's harmless where the font doesn't support it.
- Write availability as words with a number: **"2 of 3 available"** or **"None available"**. Never use color alone, and never a bare "2/3".

## Due dates

- Use an unambiguous format with the weekday and a spelled-out month: **Due Tue 4 Nov**. Add the year on the check-out confirmation and receipt: **Tue 4 Nov 2026**.
- Never use all-numeric dates like 04/11/26. Readers disagree on day/month order, and a wrong guess means a late fee.
- Generate the string with `Intl.DateTimeFormat` using `{weekday:'short', day:'numeric', month:'short'}`, so the format follows the locale and isn't hand-built.
- Style "Due" as the regular-weight label (28 px) and the date as bold, so the date is what the eye lands on.

## Per-screen summary

- **Search:** large heading, a 40 px input, and an on-screen keyboard with 32 px bold key labels. The query echo sits in the same 40 px face as the input.
- **Results:** the cards above. Show 3–4 per screen at these sizes and paginate. Don't shrink the type to fit more.
- **Check-out confirmation:** title at 56 px, then one line, **"Due Tue 4 Nov 2026"**, at 40 px bold. The shelf code isn't needed here, so leave it out. Two buttons, "Confirm" and "Cancel", at 32 px bold with plain-verb labels.
- **Receipt:** the sans family at 28 px for every row (title, due date), with the due-date column right-aligned and tabular figures. Use the mono face only if the receipt also shows shelf codes. If a thermal printer produces a paper copy, its built-in font governs that, and you only choose the size and layout.

## Things to test on the real kiosk

1. Stand at 50 cm and read the 24 px floor text. If it's a struggle, raise the whole scale.
2. Check that the fallback fonts you'll actually get render the `0/O` and `1/I` distinction in shelf codes.
3. Try a long title like "The Strange Case of Dr. Jekyll and Mr. Hyde" and a long author name. Titles should wrap to two lines and clamp at three, and the shelf code should never move.
