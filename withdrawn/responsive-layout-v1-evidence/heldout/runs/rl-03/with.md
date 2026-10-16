Here are the problems, most damaging first. Each has the replacement for that line.

**1. Fixed-pixel page widths (`.page`, `.content`, `.intro`)**
`.page` is 1100px, and the media queries only swap it for other fixed widths (740px, 460px). Any screen narrower than the current width scrolls sideways. A 360px phone is narrower than the 460px "mobile" width, and so is a 320px one. `.intro` at 900px is wider than `.content` at 780px, so it overflows its parent even on a desktop.
```css
.page  { inline-size: min(100% - 2rem, 70rem); margin-inline: auto; }
.intro { max-inline-size: 65ch; }   /* readable line length; no fixed width */
```
Delete every `.content` width. It should fill whatever space the sidebar leaves.

**2. `float` on a flex child (`.sidebar`)**
Float has no effect on flex items, so it does nothing here. It also suggests the layout was patched rather than designed. Remove it. Give the sidebar a basis and let the content take the remaining space:
```css
.layout  { display: flex; flex-wrap: wrap; gap: 2rem; }
.sidebar { flex: 1 1 15rem; }
.content { flex: 999 1 30rem; min-inline-size: 0; }
```
Both columns now stack on their own when there isn't room, so you don't need a breakpoint for this. `min-inline-size: 0` stops long strings in the content from forcing overflow.

**3. The sidebar is hidden on small screens (`display: none`)**
Whatever is in the sidebar (hours, location, insurance, contact details?) disappears for phone users, who are likely a large share of clinic visitors. With the wrapping layout above, it stacks instead of vanishing. If it's long, put it after the booking content or collapse it into a `<details>`.

**4. Slots that can't wrap (`.slots`, `.slot`)**
`.slots` is a flex row with no wrap and fixed 120px items. Eight slots can't fit on a phone, and they overflow or get squashed. The 80px width at the smallest size also makes the tap targets too narrow. Text zoom clips the fixed `height: 48px`. The right-margin spacing also looks wrong in right-to-left languages and leaves a stray gap at the end of each row.
```css
.slots { display: flex; flex-wrap: wrap; gap: 0.5rem; }
.slot  { min-inline-size: 7.5rem; min-block-size: 3rem; padding-inline: 0.75rem; }
```
This drops the `.slot` widths from all the media queries. At 320px it gives two or three slots per row, and it keeps each tap target at least 48px tall.

**5. Fixed-size doctor photo (`.doctor-photo`)**
320×320 forces a square crop and overflows narrow containers. The 200px override only helps at one breakpoint. If a `<img>` is stretched this way, the photo also distorts.
```css
.doctor-photo { inline-size: min(100%, 20rem); block-size: auto; aspect-ratio: 1; object-fit: cover; }
```

**6. Pixel font size (`.intro`)**
`font-size: 15px` ignores the reader's browser text-size setting, which matters for an older patient population. It's also small for body copy. Use `1rem` (or more), and set no `px` sizes on text anywhere else in the file.

**7. The media queries themselves**
All three blocks are device-width patches (768, 480) that swap one fixed number for another. With the changes above they have nothing left to do, so I'd delete them all. The one query worth keeping would be a real viewport question, such as hiding decorative content or changing the primary navigation, and nothing here needs it yet.

**What I'd keep:** `margin: 0 auto` for centering (now `margin-inline: auto`), and the basic idea of a two-column layout with a flex row of slots.

**Missing globals:** I don't see these in the snippet, so check the rest of the stylesheet for them:
```css
*, *::before, *::after { box-sizing: border-box; }
img { max-inline-size: 100%; }
```
Without `border-box`, any padding you add will push the widths past what you set.
Also confirm the HTML has `<meta name="viewport" content="width=device-width, initial-scale=1">` without `user-scalable=no`. A missing viewport tag alone would make phones render this as a zoomed-out desktop page.

**Widths I checked by reasoning (not in a browser):**
- At 320px, the page is 288px wide, the sidebar and content stack, and slots wrap two or three per row, with no sideways scroll.
- At 768px, the sidebar and content fit side by side if the content's 30rem basis fits (about 480px plus the sidebar's 240px). Otherwise they stack.
- At 1440px, the page stops at 70rem, and the intro stops at 65ch.

I haven't seen your HTML. If the sidebar holds something other than what I guessed, or `.doctor-photo` isn't an `<img>`, tell me and I'll adjust points 3 and 5.
