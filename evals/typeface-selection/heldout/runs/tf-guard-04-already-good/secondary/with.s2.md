**Verdict: sound. Ship it.** I reviewed this by reading the CSS, not by rendering it, so the checks below are still open.

**What works**
- **Roles are separate.** Serif for article body, sans for headings, metadata and the tide table. Each role has one clear job.
- **Both stacks end in a real generic fallback**, and no web fonts are loaded, so the page looks the same offline.
- **The tide table gets `tabular-nums`**, which is the right tool for aligned times and heights.
- **Serif body with sans headings** is a pairing with fixed roles and clearly different categories, so it reads as intentional.

**Worth checking before you ship**
1. **Tabular figures in the sans stack.** `tabular-nums` fails silently if the resolved face lacks `tnum`. Render `.tide-table` on macOS (system-ui/SF), Windows (Segoe UI) and Linux (Roboto or whatever `system-ui` resolves to), and confirm the columns line up. This is the one place a platform difference would show up as a visible bug.
2. **Italic in the serif stack.** Article text will probably use `em`. Confirm the italic on each platform's first match (Charter, Bitstream Charter, Sitka Text, Cambria) looks right. Don't rely on synthesized italics.

**Optional**
- Consider `font-variant-numeric: tabular-nums` only on `.tide-table`, not `.meta`, unless `.meta` also holds aligned numbers. It's a minor cleanup, not a bug.
