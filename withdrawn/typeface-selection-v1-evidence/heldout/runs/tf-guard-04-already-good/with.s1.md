This is sound, so I'd ship it.

**What works**
- The roles are clear. Serif is for long reading, sans is for headings and data, and nothing else is added.
- It's a system stack, so there's no web font to fail, no layout shift, and no licensing question. Each stack ends in a real generic fallback.
- `tabular-nums` on `.tide-table` is the right call, because the heights and times will line up in columns.
- Charter, Sitka Text and Cambria are all text-oriented serifs with real bold and italic. Nothing gets faux-styled.

**One thing to check, not change**
The body will look different by platform. Charter ships with macOS and iOS, Windows uses Sitka Text, and Android and most Linux systems fall through to the generic `serif`. Glance at a long article and the tide table on Windows and Android before launch. If the Android fallback looks too light or too small, that's the only place I'd consider adding a loaded web font.

I'm assuming this is screen-only and Latin script. If you add other scripts later, check that the stack covers them.
