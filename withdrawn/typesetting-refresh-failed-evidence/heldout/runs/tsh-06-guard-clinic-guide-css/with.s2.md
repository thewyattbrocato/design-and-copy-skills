This stylesheet is sound, so I changed nothing.

- **Size and measure:** Body is 1.125rem in rem units, which suits a long reading page. The 38rem column gives about 65 characters per line.
- **Leading:** Body is 1.6 and headings are 1.12 to 1.25, so headings are tighter than body text.
- **Scale:** The sizes are 2–2.75rem, 1.5rem, 1.125rem, 0.875rem and 0.75rem. Each has a clear job and neighbors differ by at least 1.25×.
- **Heading space:** h2 has 2.5rem above and 0.75rem below, so it clearly belongs to the text that follows.
- **Paragraphs:** They are separated by gaps only, with no indent.
- **Small text and labels:** Small text is 14px in `--muted` (about 5.9:1 contrast on white). The caps label is 12px, tracked at 0.08em, and short.
- **Tables and links:** Tables use tabular figures with right-aligned number columns. Links are underlined, with a visible focus ring.

Two optional things to check before launch:
1. `hyphens: auto` only works if the page has `<html lang="en">` (or the right language). Without it, browsers skip hyphenation. This matters for a legal aid site, so confirm it's set.
2. You could add `text-wrap: pretty;` to `p` to avoid single-word last lines. It's a nicety, not a fix.
