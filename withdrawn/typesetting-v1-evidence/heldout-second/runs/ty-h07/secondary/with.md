The sidebar looks cheap mainly because of the justified text in a narrow column. Three things cause it.

1. **Justified text with no hyphenation.** At 260px, justification stretches word gaps unevenly, so lines show visible holes and rivers. `hyphens: none` makes it worse, because nothing can break a long word to even out the spacing. Set the text flush left and ragged right, which is the right choice on screen.

2. **The measure is too narrow for Verdana.** Verdana is a wide face. At 15px, 260px fits only about 30 characters per line, so the text breaks into short, choppy lines. Widen the column to about 300px, which gives roughly 38 characters.

3. **The label is a tiny all-caps line with no tracking.** Capitals at 12px with `letter-spacing: 0` read as cramped. The `text-transform: none` line does nothing, and the caps are typed into the HTML, so they can't be restyled. Keep the HTML in sentence case, add the caps and tracking in CSS, and shorten the label so it doesn't wrap onto several lines.

Revised CSS:

```css
.side { width: 300px; max-width: 100%; font: 15px/1.5 Verdana, sans-serif; text-align: left; hyphens: none; text-wrap: pretty; }
.tag { font-size: 12px; font-weight: bold; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 8px; }
```

Revised label, with the caps moved to CSS:

```html
<div class="tag">Upcoming workshops and gatherings</div>
```

Two smaller notes:
- The paragraphs get their gap from the browser's default `p` margin, which is fine. Leave it.
- If Verdana's width still feels heavy, a narrower sans such as system-ui would look lighter. That is a typeface choice, so I haven't changed it.
