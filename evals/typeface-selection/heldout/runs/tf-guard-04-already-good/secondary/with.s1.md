This is a solid setup. Charter for long-form body text and a system sans for headings, metadata, and tables is a sensible pairing, and the stacks end in generic fallbacks. A few small things to consider:

1. **Platform-dependent look.** Charter ships with macOS but not Windows, so body text falls back to Cambria there. `system-ui` also resolves to a different sans on each OS (SF on macOS, Segoe UI on Windows, Roboto or DejaVu on Linux). That's usually what you want for a system stack, but if the newsletter needs one consistent look, pick a specific sans you bundle as a web font.

2. **Tabular numerals depend on the font.** `tabular-nums` only does something if the resolved font has tabular figures. SF, Segoe UI, and Roboto do; some Linux fallbacks may not. Check the tide table on a Linux machine if you can. If alignment matters a lot, you could also set `text-align: right` on the numeric cells.

3. **Headings only.** `h1, h2, h3` are covered, but `h4`–`h6` inherit the serif. Add them to the selector if they appear in articles.

4. **Bold availability.** `font-weight: 700` will be synthesized (faux-bold) if the resolved sans lacks a bold face on some Linux setups. That's rare, and it's a minor issue.

Nothing here blocks shipping. If the site is meant to look the same on every machine, item 1 is the one worth deciding on before launch.
