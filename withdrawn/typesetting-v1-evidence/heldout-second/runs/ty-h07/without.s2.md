The main problem is that the type settings are fighting a 260px column. Here are the causes, most damaging first.

1. **Justified text with hyphenation off.** At 260px, Verdana 15px fits only about 30 characters per line. With no hyphenation and no way to break words, the browser can only stretch the word gaps, which leaves uneven spacing and visible rivers. This is probably most of the cheap look. Switch to `text-align: left`. If you want justified, you need `hyphens: auto` and `lang="en"` on the page, and even then it's marginal at this width.

2. **A long all-caps label with no tracking.** "UPCOMING WORKSHOPS AND COMMUNITY GATHERINGS" is typed in capitals at 12px bold, with `letter-spacing: 0`. Tight bold caps are hard to read, and the label will wrap to two or three cramped lines. Caps need about `0.06–0.1em` of tracking. Better still, write it in sentence case ("Upcoming workshops and gatherings") and let the CSS decide the styling. Shortening it also helps.

3. **Verdana at 15px.** Verdana is very wide, which makes the line-length problem worse and gives a dated, default look. A 14–15px system or humanist sans-serif fits more characters per line and looks more current.

4. **The label isn't a heading.** A `div.tag` gives screen readers nothing to navigate by. Use an `h2` or `h3`.

5. **No spacing system.** The paragraphs use browser-default margins, and the label has an arbitrary 8px. Set these deliberately so the label sits closer to its content than the paragraphs sit to each other.

Here's a starting point:

```html
<aside class="side">
  <h2 class="tag">Upcoming workshops and gatherings</h2>
  <p>…</p>
  <p>…</p>
</aside>
```
```css
.side {
  width: 260px;
  font: 15px/1.55 system-ui, -apple-system, "Segoe UI", sans-serif;
  text-align: left;
  hyphens: manual;
}
.tag {
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  line-height: 1.3;
  margin: 0 0 12px;
}
.side p { margin: 0 0 1em; }
```

If it still feels flat after that, the content may be the cause. Both paragraphs are dense prose with the key facts buried: "first Saturday," "Fernwood Library," and "community hall." For a sidebar, pulling the date and place out as a bold lead-in or a short list would help more than any more styling.
