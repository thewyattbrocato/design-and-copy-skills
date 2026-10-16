The main culprit is the justified text in a narrow column. The all-caps label is a close second.

**What makes it look cheap**

1. **Justified text with hyphenation off.** At 260px and 15px Verdana you get roughly 30 characters per line. With so few words per line and no hyphenation, justification has to stretch the word spaces, which leaves gaps and rivers. Use `text-align: left`. If you want justified text, you need `hyphens: auto`, a `lang` attribute, and a wider column, and left-aligned is still the safer choice.
2. **Verdana at 15px in a narrow column.** Verdana is very wide, which is part of why the measure is so short. A narrower face (system UI, Georgia, or whatever the newsletter body uses) at 14–15px fits more per line and looks less default.
3. **The label is a long, untracked, bold all-caps string.** "UPCOMING WORKSHOPS AND COMMUNITY GATHERINGS" will wrap to about three lines of dense 12px bold capitals. Caps need letter-spacing (about 0.06–0.1em), and a lighter or colored treatment works better than bold. Shorten it too, for example "Upcoming events".
4. **The caps are typed into the HTML.** Write it in normal case and use `text-transform: uppercase`. Screen readers and copy/paste then behave better, and `text-transform: none` is doing nothing.
5. **The spacing has no rhythm.** The label has an 8px gap, but the paragraphs fall back to browser-default 1em margins. Set the spacing explicitly.
6. **The label is a `div`.** Use a real heading (`h2` or `h3`) so the structure is meaningful.
7. **There's no container.** With no padding, border, or background, the sidebar reads as loose text rather than a deliberate panel.

**Content gap:** neither item says when it happens. The bookbinding intro has no date or time. In a sidebar about upcoming events, those details are what people will scan for. Consider bolding the date or putting it on its own line above each blurb.

**Suggested rewrite**

```html
<aside class="side">
  <h2 class="tag">Upcoming events</h2>
  <p><strong>Bookbinding intro</strong> at the Fernwood Library. Materials are provided, but please bring an apron.</p>
  <p><strong>Repair café</strong> returns to the community hall on the first Saturday of the month. Volunteers will help you mend small appliances, clothing and bicycles, free of charge.</p>
</aside>
```
```css
.side {
  width: 260px;
  padding: 16px 18px;
  border-top: 3px solid #2f5d50;   /* pick your newsletter's accent */
  background: #f7f5f0;
  font: 15px/1.5 Georgia, serif;
  text-align: left;
  hyphens: auto;
}
.tag {
  margin: 0 0 12px;
  font: 600 12px/1.3 system-ui, sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #2f5d50;
}
.side p { margin: 0 0 12px; }
.side p:last-child { margin-bottom: 0; }
```

I trimmed the copy a little to suit the narrow column. Keep your original wording if you prefer, and add the dates once you have them. The colors are placeholders, so swap in your palette.
