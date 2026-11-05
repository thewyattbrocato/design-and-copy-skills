This type setup is already sound, so I'd leave it almost untouched.

**What works**
- The system font stack gives each person a native font that loads instantly, with no web font to host or license. It ends in `sans-serif`, so there's a real fallback.
- The 17px body size and 1.55 line height are comfortable for reading.
- Headings use the same family at a heavier weight. That's the right amount of hierarchy for a member portal.
- `tabular-nums` on right-aligned number columns keeps dues, counts and dates lined up.
- Monospace is used only for `code`, and the slightly smaller size stops it looking oversized next to body text.

**One optional tweak**
- Weight `650` only works on fonts with variable weights, such as recent macOS and Windows system fonts. On static fonts like Roboto or Arial it snaps to regular bold (700). That's harmless and nothing gets faked. If you'd like every member to see identical headings, use `font-weight: 700`.

**Tidying, not polish**
- `font-family: var(--font-body)` on the headings is redundant because they inherit it from `body`. You can delete it or leave it.

I'd only make the weight change if consistency across devices matters to you. I assumed the portal is Latin-script, screen-only text with no web fonts. If you need other languages, or want a distinct look for the co-op, tell me and I'll suggest a heading font to pair with this body font.
