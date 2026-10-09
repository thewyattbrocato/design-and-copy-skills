Four things make it look cheap, and they all come from the CSS.

**1. Justified text in a 260px column.** This is the biggest problem. At about 35 characters per line, with `hyphens: none`, justification opens large uneven gaps between words. Switch to ragged-right, which is the screen default for a narrow card.

**2. A long all-caps label with no tracking.** "UPCOMING WORKSHOPS AND COMMUNITY GATHERINGS" is a whole phrase in bold capitals at 12px, and it wraps to several lines. Tight caps are slow to read. Use sentence case, and make it a little larger than 12px. If you want to keep caps, shorten the label to something like "Workshops" and track it at 0.05–0.1em.

**3. Fixed px sizes, and a label with no relation to the body.** The 15px body and 12px bold label don't follow a scale. Use rem so the text respects user font settings. Bold at 12px beside 15px regular is a weak step, so drop the caps and make the label larger.

**4. Verdana at 15px with 1.5 leading.** Verdana is wide, with a big x-height. That's part of why a 260px column fits so few characters. 1.5 is fine for body text, but the label needs tighter leading. If you can, use a narrower face. Otherwise keep Verdana and accept the short lines.

There are two smaller points. Add `text-wrap: pretty` to avoid orphaned words. The gap above the label should be bigger than the gap below it.

```css
.side {
  width: 260px;
  font: 1rem/1.5 Verdana, sans-serif;
  text-align: left;
  hyphens: manual;
}
.tag {
  font-size: 1.125rem;
  font-weight: bold;
  line-height: 1.25;
  text-wrap: balance;
  margin: 0 0 0.5rem;
}
.side p { margin: 0 0 0.75em; text-wrap: pretty; }
```

```html
<div class="tag">Upcoming workshops and community gatherings</div>
```

I changed the label's wording to sentence case only. The paragraphs are untouched.

I assumed a screen and a light background. The label should ideally be a real heading (`<h2>`) for accessibility. I left it as a `div` because you didn't ask for that change.
