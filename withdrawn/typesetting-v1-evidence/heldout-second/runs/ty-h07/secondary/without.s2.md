The main problem is **justified text in a narrow column**. At 260px, justification stretches word spacing unevenly from line to line, which creates visible gaps (rivers). That's the most likely reason it looks cheap. Several smaller issues compound it:

1. **Justified body text at 260px.** Switch to left-aligned (ragged-right). It's the standard for narrow columns and reads more naturally.
2. **The label is set in all caps with no letter-spacing.** Capitals are wide and need tracking (about 0.06–0.1em) to read well. The long label also reads as a shout. Shorten it, and use a real heading with a rule under it.
3. **No structure between items.** Two paragraphs run together. Each item needs its own title, and ideally a when/where line, which is the most useful information for a workshop listing.
4. **Missing dates and times.** "Upcoming" with no dates undercuts the purpose. The placeholders below are for you to fill in.
5. **Cramped line length and loose spacing.** Verdana at 15px in 260px gives only about 30 characters per line. Widening the column slightly and tuning the vertical rhythm helps.

Revised version:

```html
<aside class="side">
  <h2 class="tag">Upcoming workshops &amp; gatherings</h2>

  <article>
    <h3>Introduction to bookbinding</h3>
    <p class="meta">Fernwood Library · [date and time]</p>
    <p>Volunteer instructors who have taught the craft to neighbours for over a decade will guide you through the basics. Materials are provided; please bring an apron.</p>
  </article>

  <article>
    <h3>Repair café</h3>
    <p class="meta">Community Hall · First Saturday, [time]</p>
    <p>Skilled volunteers will help you mend small appliances, clothing and bicycles, free of charge.</p>
  </article>
</aside>
```

```css
.side {
  width: 280px;
  font: 15px/1.5 Verdana, sans-serif;
  text-align: left;
  color: #222;
}

.tag {
  font-size: 12px;
  font-weight: bold;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin: 0 0 12px;
  padding-bottom: 8px;
  border-bottom: 1px solid currentColor;
}

.side h3 {
  font-size: 16px;
  margin: 16px 0 2px;
}

.meta {
  font-size: 13px;
  color: #666;
  margin: 0 0 6px;
}

.side p {
  margin: 0 0 12px;
}
```

Notes on the changes:

- I kept Verdana, since that was your choice. If you want a warmer newsletter feel, Georgia at 16px pairs well with the sans heading. Verdana is wide, so it's a reasonable candidate to change.
- Use `<h2>`/`<h3>` instead of `<div>`. It gives screen readers and the document outline the structure, and it costs nothing visually because the CSS sets the styles.
- If you later reintroduce `text-align: justify` for print, add `lang="en"` to the `<html>` element and `hyphens: auto`. Otherwise hyphenation won't work.
