The base is solid: a ~65-character measure, a sensible serif stack, good contrast, and tabular numerals with right-aligned number columns. These are the changes I'd make:

1. **Table headers:** `th` defaults to centered, so headers won't line up with left-aligned text cells. Give them `text-align: left` and a stronger bottom rule.
2. **Table on mobile:** a wide table will overflow a ~375px screen and force horizontal page scroll. Letting the table scroll on its own fixes that. Also add vertical margin, since right now it butts against the paragraphs.
3. **Headline wrapping:** add `text-wrap: balance` on headings to avoid one-word last lines. Add `text-wrap: pretty` on paragraphs to avoid widows. Both degrade gracefully.
4. **H1 size on small screens:** 2.25rem is heavy at 320–375px, so use `clamp()`. A slight negative letter-spacing helps at display size.
5. **Blockquote:** the last paragraph inside it keeps its bottom margin, which leaves extra space under the quote. Zero it out.
6. **Missing elements:** an article will almost certainly hit links, lists, `hr`, `figure`/`figcaption` and `code`. Without styles they fall back to browser defaults, which clash with your type. I added restrained versions.
7. **iOS landscape:** add `-webkit-text-size-adjust: 100%` so text doesn't get auto-inflated.
8. **Font fallback:** Charter ships on Apple platforms but not Windows or Android, where readers get Georgia. That's acceptable, and I kept it. Georgia has old-style numerals by default, which looks odd in a money newsletter. The `font-variant-numeric: lining-nums` on body text fixes it.

```css
body {
  margin: 0;
  background: #fbfaf7;
  color: #1c1c1c;
  font-family: Charter, 'Iowan Old Style', Georgia, serif;
  font-variant-numeric: lining-nums;
  -webkit-text-size-adjust: 100%;
  -webkit-font-smoothing: antialiased;
}
article { max-width: 38rem; margin: 0 auto; padding: 3rem 1.25rem; font-size: 1.125rem; line-height: 1.6; }

article h1 { font-size: clamp(1.875rem, 5vw + 1rem, 2.25rem); line-height: 1.15; letter-spacing: -0.01em; margin: 0 0 0.5rem; text-wrap: balance; }
article .byline { font: 0.875rem/1.4 system-ui, sans-serif; color: #5b5b5b; margin: 0 0 2rem; }
article h2 { font-size: 1.5rem; line-height: 1.25; margin: 2.5rem 0 0.75rem; text-wrap: balance; }
article p { margin: 0 0 1.1rem; text-wrap: pretty; }

article a { color: inherit; text-decoration-color: #b8892b; text-decoration-thickness: 0.08em; text-underline-offset: 0.18em; }
article a:hover { text-decoration-thickness: 0.15em; }

article ul, article ol { margin: 0 0 1.1rem; padding-left: 1.5rem; }
article li { margin: 0 0 0.4rem; }

article table { display: block; overflow-x: auto; width: 100%; margin: 1.5rem 0; border-collapse: collapse; font: 0.9375rem/1.4 system-ui, sans-serif; font-variant-numeric: tabular-nums; }
article th, article td { padding: 0.5rem 0.75rem; border-bottom: 1px solid #e3e0d8; text-align: left; }
article th { font-weight: 600; border-bottom-color: #1c1c1c; white-space: nowrap; }
article td.num, article th.num { text-align: right; }

article blockquote { margin: 1.5rem 0; padding-left: 1rem; border-left: 3px solid #b8892b; font-style: italic; }
article blockquote > :last-child { margin-bottom: 0; }

article figure { margin: 1.5rem 0; }
article figcaption { font: 0.8125rem/1.4 system-ui, sans-serif; color: #5b5b5b; margin-top: 0.5rem; }
article hr { border: 0; border-top: 1px solid #e3e0d8; margin: 2.5rem 0; }
article code { font-size: 0.9em; }
```

Two caveats:

- `display: block` on the table is the simplest fix for mobile overflow, but it drops table semantics for some screen readers. If accessibility matters here, wrap the table in a `<div style="overflow-x:auto">` instead and remove `display: block; overflow-x: auto` from the CSS.
- I haven't rendered this. Look at one real article with a table and a blockquote on a phone before it goes live.
