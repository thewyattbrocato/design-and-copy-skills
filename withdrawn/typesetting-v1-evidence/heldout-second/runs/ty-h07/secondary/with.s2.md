Your instinct is right. The sidebar has four problems, and the justified text is the main one.

**What fails**

- **Justified text in a narrow column.** At 260px with `hyphens: none`, the browser can only stretch word gaps, so lines show uneven spacing and rivers. Ragged-right is the right setting for a screen column.
- **Measure is too short.** Verdana is a wide face, so 260px at 15px holds only about 30 to 33 characters per line. That chops the copy into many short lines, and the justification gaps get worse.
- **The label is a long all-caps line.** "UPCOMING WORKSHOPS AND COMMUNITY GATHERINGS" is 42 capitals with no tracking. Capitals read slowly, and this is a sentence-length label. It also sits at 12px, the smallest size on the page, so it looks like fine print rather than a heading.
- **Spacing is off.** The 8px gap under the label is tight for a 15px body, and the paragraphs have no defined gap between them.

**Fix**

```html
<aside class="side">
  <h2 class="tag">Upcoming workshops and community gatherings</h2>
  <p>Join us at the Fernwood Library for an introduction to bookbinding, led by volunteer instructors who have been teaching the craft to neighbours for over a decade. Materials are provided, but please bring an apron.</p>
  <p>On the first Saturday of the month, the repair cafe returns to the community hall, where skilled volunteers will help you mend small appliances, clothing and bicycles free of charge.</p>
</aside>
```

```css
.side { width: min(100%, 22rem); font: 1rem/1.5 Verdana, sans-serif; text-align: left; text-wrap: pretty; }
.side p { margin: 0 0 0.75em; }
.tag { font-size: 1.125rem; font-weight: bold; line-height: 1.25; text-wrap: balance; margin: 0 0 0.5em; }
```

**Why these values**

- `22rem` (about 352px) gives roughly 38 to 42 characters per line in Verdana, which is within the narrow-column range.
- Ragged-right removes the uneven word gaps without any hyphenation.
- The label becomes a sentence-case heading at 18px, so it reads as a section title. The 1.25 line height suits a heading, and `balance` keeps a two-line title from leaving one word alone.
- The paragraph gap is 0.75em, and the heading has about half that space below it.

**Notes**

- I changed the label text to sentence case. If the all-caps look is a house style, keep it only for short labels (one or two words) with `letter-spacing: 0.08em` at 12px or more.
- I assumed a screen layout on a light background. The Verdana stack is kept as you had it.
