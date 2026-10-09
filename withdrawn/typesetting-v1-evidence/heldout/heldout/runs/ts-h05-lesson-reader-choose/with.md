**Pick B.** It's the only one of the three that is already well set for 600-word reading on tablets and laptops.

**Why B works**
- **Size:** 1.125rem body is right for long-form reading, and it follows the user's browser setting.
- **Measure:** 40rem at 18px is about 720px, which is roughly 65–70 characters per line. That's in the comfortable range.
- **Leading:** a 1.6 body line height, with tighter 1.2–1.3 headings that still have room if they wrap.
- **Scale:** the sizes are 18px, 22px and 32px. That's a clear ramp with one size per role.
- **Spacing:** h2 has 2rem above and 0.5rem below, so the heading groups with the text that follows it. h1 and paragraph gaps are sensible.
- **Color:** #1f2328 on white has strong contrast without being harsh pure black.

**Why not A or C**
- **A:** 14px gray (#444) text on a 1100px container gives 150+ characters per line. The 1.3 leading and 4px paragraph gaps make it a wall of text, and the h1 is barely bigger than the body. It's the pattern that fails on tablets.
- **C:** 24px text on a 28rem (448px) column gives about 30 characters per line, which breaks sentences into fragments. The 2.1 leading is so loose that lines stop reading as a block, and the 3.2rem h1 (about 51px) will wrap awkwardly on a narrow column. Its h1 also has no line-height set, so it inherits 2.1. A 600-word lesson would also take many screens of scrolling. Its instinct toward larger type is good for accessibility, but it overshoots.

**Small tweaks to B**
```css
.lesson { max-width: 40rem; margin-inline: auto; padding-inline: 1rem; font: 1.125rem/1.6 system-ui; color: #1f2328; }
.lesson h1, .lesson h2 { text-wrap: balance; }
.lesson h1 { font-size: clamp(1.75rem, 5vw, 2rem); line-height: 1.2; margin: 0 0 1.5rem; }
```
- **`margin-inline: auto` and `padding-inline`:** center the column on laptops and keep text off the screen edge on tablets. Without them it sits flush left, and on narrow screens it touches the edges.
- **`text-wrap: balance`:** avoids a one-word last line in wrapped headings.
- **`clamp()` on h1:** scales the title down on small tablets in portrait. It uses a rem floor, and the measure stays fixed.
- **Optional, only if learners are older or testing shows strain:** raise body to 1.25rem. Test it before committing, since B already passes without it.

I'd leave everything else alone.
