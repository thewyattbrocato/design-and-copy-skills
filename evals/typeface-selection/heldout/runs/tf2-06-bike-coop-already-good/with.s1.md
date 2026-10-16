Your type setup is already sound, so I'd leave it mostly alone.

**What works**
- The system stack suits a volunteer-run portal. It loads instantly, needs no licensing, and looks native on each device.
- Body text at 17px with 1.55 line height is comfortable for reading.
- Headings are a heavier weight of the same family, with tight leading and slight negative tracking, which keeps the hierarchy clean.
- `tabular-nums` and right alignment on number cells keep dues and counts lined up.
- Monospace is used only for `code`, with a real fallback list.

**One change I'd make**

Add `font-synthesis: none` to `body`:

```css
body { font-family: var(--font-body); font-size: 1.0625rem; line-height: 1.55; font-weight: 400; font-synthesis: none; }
```

The 650 heading weight is a variable-font value. Some fallback fonts, such as Roboto or Segoe UI, only come in fixed weights. Normally the browser picks the nearest real weight, which is fine. This line stops it from ever faking a bold or italic, which looks smeared.

**Optional tidy-up:** `font-family: var(--font-body)` on the headings is redundant, because they inherit it from `body`. It's harmless, so remove it only if you want less to maintain.

I assumed a screen-only, English-language portal. If members use other scripts, such as Arabic or Vietnamese, tell me. The system stack handles those well, but line height may need a small increase.
