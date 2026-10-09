# Reading text

Load this when setting a reading page, defining a scale, or handling dark and small text. Every number is a starting point; adjust by eye on the real content.

## Ranges by context

| Context | Characters per line | Line height |
| --- | --- | --- |
| Long article or documentation | 60 to 70 (45 to 75 allowed) | 1.5 to 1.6 |
| Interface paragraph, help text | 50 to 75 | 1.4 to 1.5 |
| Narrow column or card | 35 to 50 | 1.4 to 1.5 |
| Mobile body | 30 to 45 | 1.45 to 1.55 |
| Caption, label, metadata | not capped | 1.3 to 1.4 |
| Large display, few words per line | not capped | 1.05 to 1.15 |
| Code, logs, data cells | not capped | per the tool |

`ch` is a good proxy for characters. Cap the text, not the container:

```css
article p, article li { max-width: 65ch; }
article figure, article table, article pre { max-width: none; }
body { font-size: 1rem; line-height: 1.5; }
h1, h2, h3 { line-height: 1.2; text-wrap: balance; }
```

Check leading on a paragraph, a list, a heading that wraps and a block of mixed sizes, not on one paragraph. With a long-form reading page, 1.125rem body and 1.6 leading is a comfortable start.

## Scale

List the roles first: display, title, section heading, body, small, label, code. One size per role; merge roles that look fine at the same size.

Dense interface (about 1.2): title 1.75rem, section 1.25rem, body 1rem, small 0.875rem, metadata 0.75rem.
Editorial or marketing (about 1.4 at the top): display 3.5rem, title 2.25rem, section 1.5rem, body 1.125rem, small 0.875rem.

If the product already has a scale, use it. Fluid display type: `clamp(2rem, 1.2rem + 3vw, 3.5rem)` with a rem floor so zoom works; keep the measure in `ch` so it does not grow with the viewport; lower leading as size rises. Body rarely needs to be fluid.

Heading levels follow the document outline, without skipping; the look comes from a class or token. Deeper than three levels, distinguish with weight or space rather than a new size.

Auditing a messy stylesheet: list every size in use, group near-duplicates (13, 14 and 15px are usually one role), pick the body group, set the rest relative to it, replace the groups with tokens, then re-check headings that wrap.

## Vertical rhythm on screens

A shared spacing unit near the body line height helps; a strict baseline grid usually does not. Make gaps simple multiples of the unit, let headings and images break the rhythm when they must, and keep about twice as much space above a heading as below. In print, slides and other fixed formats, align lines across columns and keep leading shared across sizes.

## Dark grounds

Light text on dark can look heavier because bright strokes glow into the dark space, or thinner if the face is light and the size small. Compare the same paragraph in both themes at the same zoom and match how heavy it feels.

- Off-white on soft dark gray, not pure white on black. Contrast still has to meet the product's accessibility floor.
- If body looks swollen, drop one weight step or use a lighter grade; if strokes thin out or break up, raise it back.
- Open small text by 0.01 to 0.02em; add about 0.05 leading if it still looks dense. Keep sizes and measure as in light mode.
- Dim secondary text by value, not by lowering the opacity of white; recheck metadata, placeholders, links and code colors on the dark ground.
- Reversed text on a button, banner or image needs the same care, and a scrim or panel behind busy images.

## Small text

Keep functional text at body size. About 12px is for metadata, timestamps and captions, never long passages. Small text wants a slightly open spacing, a little more leading, regular or medium weight and a face that holds up at that size. Use an optical-size axis or a text cut if the face has one. Zoom to 200% and narrow the window: text should reflow, not clip.
