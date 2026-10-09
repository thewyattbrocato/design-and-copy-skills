No real problems. The spec matches what works for a settings reference, and I only have a few things to check.

**What's fine**
- **Left alignment:** The Default column holds mixed values like `true`, `30s` and `"auto"`, so it should be treated as text and left-aligned.
- **Row separation:** A hairline under each row is one device, which is enough. Don't add zebra stripes or vertical rules on top of it.
- **Header:** Bold text on a light gray background reads clearly. Eight rows don't need sorting or a sticky header.
- **Text size:** 14px is the minimum I'd use.

**What to check**
1. **Row height:** 8px of vertical padding on 14px text gives rows about 38px tall. That's slightly under the usual 40–48px for general use. It's fine for a dense reference table, but 10–12px vertical padding would read more comfortably if the Meaning text wraps to several lines.
2. **Missing defaults:** If any setting has no default, show an em dash or "none" rather than a blank cell. Don't show an empty string where a real default is `""`, or write `0` or `false` unless that is the actual default.
3. **Wrapping:** Let only the Meaning column wrap. Keep Setting and Default on one line (`white-space: nowrap`) so names and values never break mid-token. Use a monospace face for setting names and literal defaults, since people copy them.
4. **Markup:** Use a real `<table>` with a `<caption>` (it can be visually hidden if the heading already names the table), `<th scope="col">` in the header, and ideally `<th scope="row">` for the Setting cells.
5. **Narrow screens:** At 360px the Meaning column will get cramped. Wrap the table in a horizontally scrollable container, or let Meaning wrap freely and keep the first two columns intact. Don't let the setting names or defaults wrap.
6. **Header contrast:** Make sure the gray background still gives the bold header text enough contrast in dark mode, if your docs have one.

I didn't see the real CSS or markup, so this is from your description only. If you paste them, I can check the specifics.
