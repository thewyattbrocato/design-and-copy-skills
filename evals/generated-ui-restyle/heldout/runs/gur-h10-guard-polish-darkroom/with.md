I'd change very little here. Your friend's "plain" is partly right, but the page doesn't have the usual AI look. It has a warm paper ground, ink text, Charter, hairline rules, and a red safelight dot that comes from the darkroom itself. There are no gradients, glows, icon cards, centered hero or invented proof. A heavy restyle would make it worse.

**What gives it away (ranked)**
1. **Tracked all-caps labels**: `.name` and every `h2`. They read as a template habit (cause 4), and they clash with a page that otherwise sounds like a handwritten notice board.
2. **Table header row** (`th`): the same weight as the data, so the table is flat.
3. **`.join` button**: it has no hover or active state. It's the only action on the page and it feels inert.

I left everything else alone. That includes the layout, the wording, the safelight dot, the £18 and the section order.

**Changed CSS** (the HTML stays the same):

```css
.name{font:700 1.3rem/1 Charter,Georgia,serif;letter-spacing:0;text-transform:none}
h2{font:700 1.2rem/1.2 Charter,Georgia,serif;letter-spacing:0;text-transform:none;margin:0 0 .5rem}
th{font-weight:400;color:var(--soft);font-size:.82rem}
.join{transition:background-color .15s}
.join:hover{background:var(--safe)}
.join:active{background:#7f1d14}
.join:focus-visible{outline:2px solid var(--ink);outline-offset:3px}
```

**Decision notes**
- **Headings**: set in the serif the body already uses, in sentence case. The copy reads like a notice on the wall, not a dashboard label.
- **Hover on the button**: it goes safelight red. Red is already the page's only accent, tied to "someone is printing", so no new color comes in.
- **Table header**: set quieter, so the hours and enlarger counts are what you read first.

**To confirm**
- If you want it to feel less plain, the next step is adding real content, such as a photo of the room or a scanned contact sheet. I didn't draw one in CSS, because it would be decoration. I also haven't checked how it renders in a browser.
