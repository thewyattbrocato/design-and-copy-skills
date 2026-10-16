Your instinct is right. Several settings are fighting each other. Here they are, most damaging first.

**1. Line length is far too long (`.post { width: 1100px }` with 14px type)**
At 14px Georgia, 1100px fits about 160 characters per line. Comfortable reading is 45–75. Long lines make it hard for the eye to find the start of the next line, and this is probably the main cause of the cramped feeling. Cap the measure instead: `max-width: 65ch` (or about 680px) for text.

**2. Line-height is too tight (`1.15`)**
Body text wants roughly 1.5–1.65. Combined with the long lines, 1.15 makes paragraphs look like dense gray slabs.

**3. Body letter-spacing is positive (`0.04em`)**
Tracking out lowercase text hurts readability and makes serif type look stiff. Set it to `0` (or leave it unset) for body copy.

**4. `text-align: justify` without hyphenation**
With no `hyphens: auto`, justification creates uneven word gaps and "rivers" of white space. That is a big part of the cheap, word-processor look. Use `text-align: left`, or keep justify only if you add `hyphens: auto` and a `lang` attribute on `<html>`.

**5. Body size is small (`14px`)**
Go for 17–19px for long-form reading. For a recipe blog people read on phones and in kitchens, bigger is better.

**6. The h1 is off in both directions**
- `line-height: 1.5` at 56px leaves big gaps when a title wraps. Headings want about 1.1–1.2.
- `letter-spacing: 0.06em` on a large bold serif looks loose. Large display type usually wants slightly negative or zero tracking (`-0.01em`).
- 56px against 14px body is a ratio of 4:1, which is jarring. Once body is about 18px, something like 40–44px is plenty.

**7. The `h2.tag` is backwards**
Small uppercase text is the one case that needs extra tracking, and it has `letter-spacing: 0`. Use about `0.08em`. At 11px it is also too small. Go to 12–13px and raise the weight to 600 so it holds up.

**8. The blockquote stacks too many effects**
Italic, bold and all-caps together are hard to read and look shouty. Pick one. Italic alone, at a slightly larger size, is the classic choice. Avoid uppercase for anything longer than a few words.

**9. Links have no affordance**
`color: inherit; text-decoration: none` makes links invisible until hover, and hover doesn't exist on touch screens. Keep an underline, using `text-decoration-thickness: 1px; text-underline-offset: 0.15em`, and optionally tint the color.

**10. `.price, .qty` redeclare Georgia**
This is redundant. If these are meant to be numbers in ingredient lists, add `font-variant-numeric: tabular-nums` so the columns align, which is the more useful change.

**Suggested rewrite**

```css
body {
  font-family: Georgia, serif;
  font-size: 18px;
  line-height: 1.6;
  letter-spacing: 0;
  text-align: left;
  color: #333;
}
.post { max-width: 65ch; margin: 0 auto; padding: 0 1rem; }
h1 { font-size: 42px; line-height: 1.15; letter-spacing: -0.01em; font-weight: 700; }
h2.tag {
  font-size: 12px; text-transform: uppercase;
  letter-spacing: 0.08em; font-weight: 600;
}
a { color: inherit; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 0.15em; }
a:hover { color: #c0392b; }
.price, .qty { font-variant-numeric: tabular-nums; }
blockquote { font-style: italic; font-size: 1.1em; }
```

If you apply only two things, make them the narrower column and the 1.6 line-height. Those will fix most of the problem. I can also suggest a heading and body font pairing if you want something less default than Georgia.
