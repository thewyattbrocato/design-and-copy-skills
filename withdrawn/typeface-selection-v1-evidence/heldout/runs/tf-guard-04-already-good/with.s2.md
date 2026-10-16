This setup is sound. I'd ship it with two small changes.

**What works**
- The roles are clear: serif for long reading, sans for headings, the table and metadata.
- It's only two families, and they differ plainly in category.
- Charter, then Sitka Text, then Cambria is a good reading stack for macOS/iOS, Windows and older Windows.
- `tabular-nums` on the tide table keeps the digit columns aligned.
- Every stack ends in a generic fallback.

**What I'd change**
1. **Add a fallback between `Cambria` and `serif`.** Android and most Linux machines have none of the named faces, so they get the bare `serif` default, which is often Times-like. Add `Georgia` (or `'Noto Serif'`) before `serif`:
   ```css
   --serif: Charter, 'Bitstream Charter', 'Sitka Text', Cambria, Georgia, serif;
   ```
   Georgia is wider and has a larger x-height than Charter. Line breaks will shift slightly on those platforms, which is fine.

2. **Set bold and italic explicitly.** `h1, h2, h3` use `font-weight: 700` in the sans. That's fine, but the body serif relies on whichever bold and italic each system face supplies. Charter, Sitka and Cambria all ship real ones, so nothing is synthesized. I'd still add `font-synthesis: none;` on `body`. If a fallback ever lacks italic, you'd then get upright text instead of a skewed fake.

**Optional**
- `.meta` and `.tide-table` share the sans, which is right. If the table has a time column that must line up, `tabular-nums` handles it. You don't need a mono face.
- If you later want a distinctive masthead, add one display face for the title only. The body and table don't need it.

**Assumptions:** you're using system fonts only, with no web fonts loaded, and the audience reads Latin script. If you plan to add a web font, tell me and I'll adjust the loading and fallback advice.
