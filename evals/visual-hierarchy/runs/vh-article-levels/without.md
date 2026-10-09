# Hierarchy for a Long-Form Article Page

Five levels, from the first thing the eye lands on to the last. Each level should differ from its neighbors by at least two properties (size, weight, color, typeface, space), so the order reads even when squinting.

## Level 1: Title
- **Role:** Names the piece and sets the tone. It is the single dominant element on the page.
- **Treatment:** Largest type on the page (roughly 40–64px desktop, 30–36px mobile). Display serif or a heavy weight of the brand face. Tight line-height (1.1–1.15) and slight negative tracking. Highest contrast, with near-black on white. Limit it to 2–3 lines and a measure of about 20–25 characters per line-equivalent, so it wraps deliberately. Generous space above (80–120px).

## Level 2: Standfirst
- **Role:** Explains why to read, in one or two sentences. It bridges the title and the body.
- **Treatment:** Roughly 20–26px, about 40% of the title's size. Use a lighter weight than the title, or the same serif in regular. Slightly softened color (e.g., 80–85% black). Line-height of 1.35–1.45. Keep it to 2–3 lines at a measure of about 50–60 characters. Place it 16–24px below the title. Do not italicize it or put it in a box, since neither adds any hierarchy.

## Level 3: Body text and its structural markers
This level holds the reading experience. Body text is the baseline the rest are measured against, and subheads and pull quotes are its interruptions.

**Body text**
- 18–21px serif, or a sans with a generous x-height. Line-height of 1.55–1.7. Measure of 60–75 characters (about 640–700px column). Full-contrast but not pure black (#1a1a1a on white). Left-aligned and ragged-right, with 1–1.25em between paragraphs and no first-line indents when using space between. Optionally add a drop cap or small-caps lead-in on the first paragraph only.

**Subheads**
- **Role:** Wayfinding that lets a skimmer see the argument's structure.
- **Treatment:** 26–32px, about 1.5× body size, bold or semibold. Use the sans if body is serif, or a heavier weight of the same family. Tight line-height (1.2). Space above of about 2× the space below (e.g., 48px above, 16px below), so the head binds to the text it introduces. Never more than two lines. If you need a sub-subhead (H3), use body size or slightly larger in bold, with no color change.

**Pull quotes**
- **Role:** Editorial emphasis and a visual pause that rewards scrolling. They are decorative and repeat text from the body, so they rank below it in importance.
- **Treatment:** Larger than body (28–36px) in the display serif, often italic or light. Set apart by a thick rule above or a left border in an accent color, with a larger gap above and below (48–64px). Break out of the text column into the margin or span wider than the column on desktop. Mark them `aria-hidden` or use `<aside>`, so screen readers don't read the text twice. Use at most one per 800–1000 words, and never two in a row.

## Level 4: Byline and date (metadata)
- **Role:** Credibility and context. Readers want it available, not prominent.
- **Treatment:** 14–16px sans, regular weight, with the author name in medium or semibold and the date in a muted gray (about 60% contrast, still at least 4.5:1). Format as `By Name · 4 October 2026`, using a `<time datetime>` element. Place it between the standfirst and the body, or directly under the title if there is no standfirst. Separate it from the body with a hairline rule or 24–32px of space. Add an optional small avatar (32–40px) and link the author name. If there's an update date, show it in the same style, labeled "Updated".

## Level 5: Related links
- **Role:** Offers next steps after the reader has finished. It must not compete with the article while they read.
- **Treatment:** Placed after the body, below a clear divider with a small label such as "Related reading" (12–14px, uppercase, tracked, muted). Each link is a headline at 18–20px semibold in sans, with an optional 12–13px metadata line (section, read time). Use a list or 2–3-column card grid, with thumbnails only if they have a purpose. Links are underlined or accent-colored, with a clear hover and focus state. Don't place them inside the article column mid-read. If you need an inline link to a related piece, treat it as an ordinary body link.

## Summary Table

| Level | Element | Size (desktop) | Weight / style | Color | Space around |
|---|---|---|---|---|---|
| 1 | Title | 40–64px | Bold display serif | Near-black | Large above, 16–24px below |
| 2 | Standfirst | 20–26px | Regular, serif or sans | ~85% black | 16–24px below |
| 3a | Subheads | 26–32px | Semibold/bold | Near-black | 48px above, 16px below |
| 3b | Body | 18–21px | Regular | #1a1a1a | 1–1.25em between paragraphs |
| 3c | Pull quotes | 28–36px | Light or italic serif | Accent or near-black | 48–64px above and below |
| 4 | Byline, date | 14–16px | Name medium, date regular | Muted gray | Hairline rule or 24–32px |
| 5 | Related links | 18–20px | Semibold, with a small caps label | Accent for links | Below a divider, grid or list |

## Principles
1. **Title and body set the poles.** Everything else is positioned between them by size and weight. Pull quotes are the exception, because they borrow display styling to act as an interruption.
2. **Use few type styles.** Two typefaces and four to five sizes are enough. Vary weight and color before adding another size.
3. **Reading flow beats decoration.** The body column should stay consistent in width and rhythm, so subheads and pull quotes mark pauses without breaking the reader's place.
4. **Check on mobile.** Scale the title and pull quotes down more aggressively than the body (which stays at 17–18px). Pull quotes lose their breakout and become full-width with an accent rule.
