# Choosing a structure

Load this at the start of a layout. It turns the intake answers into a structure and gives outlines you can adapt. All widths are starting points; adjust against the real content.

## Intake worksheet

Answer each in one line before drawing anything.

- **Material:** continuous prose, comparable peers, separate chunks, bands of different content, or a mix?
- **Volume:** how many items or paragraphs now, and how many in a year?
- **Worst case:** the longest title, the longest word, an empty state, a single item, a thousand items, a translation that runs 30 to 40 percent longer, text enlarged by the user.
- **Reader:** who arrives, in what state, and what do they look for first?
- **Format:** reflowing screen, or fixed (slide, poster, print, social card)?

If the answer to any of these is "I don't know", make a reasonable assumption, say it, and design so the structure survives the opposite assumption.

## Worst-case checklist

- Does a long title wrap cleanly, or push other things out of place?
- What does the page look like with zero items? With one?
- At a hundred items, is there paging, filtering, or sorting, and where does it sit?
- Does a column still work when the text inside it grows by half?
- At narrow width, what moves first, and does the primary action stay close to the top?

## Material to family

| Material | Family | Why |
| --- | --- | --- |
| Prose read start to finish | Single reading column | The eye needs a steady line length and a steady return edge. |
| Peers compared against each other | Equal-cell grid that wraps | Equal cells make differences in content, not in box size, the thing the eye finds. |
| Prose plus figures, notes, or captions | Column grid with a narrow secondary column | Secondary material stays near its reference without crowding the text. |
| Several kinds of content in sequence | Horizontal bands sharing one content edge | Each band can have its own inner layout, and the page still reads as one thing. |
| A tool the reader works inside | Shell with navigation and a main region | Regions persist while content changes. |
| Records with many fields | Table or list at full available width | Comparison across fields needs width; add frozen identifying columns. |

When two families fit, take the one that needs fewer exceptions for the worst case.

## Worked outlines

Short sketches for invented products. Draw the structure first, then style.

### Long article (a field journal)

- One column, text about 60 to 68ch wide, centered or flush-left on a wide screen with generous side margins.
- Figures and pull quotes may be wider than the text, up to the container width; captions sit under or beside the figure.
- Optional narrow secondary column (about 12 to 16rem) for notes or a section list on wide screens only; it drops below the text when narrow.

### Browsable listing (a used-book marketplace)

- Narrowing controls (filters, sort) on the leading side at a fixed rail width, or in a row above; on narrow screens they collapse behind one button.
- Equal cells that wrap. Choose the minimum cell width from the content, and let the column count follow.
- One image ratio and one content order in every cell, with room for the longest title.
- Plan the zero-result state and the thousand-item state (paging or loading more) before styling.

### Marketing page of repeated sections (a note-taking app)

- A first band that states what it is, what to do, and why here, with the main action visible.
- Each later band takes the shape its content wants (a sequence for steps, side by side for a comparison, one large statement for a claim). If every band is the same heading over the same row of cards, vary the shape or merge bands. See the pacing reference.
- All bands share one content edge so the page reads as one object.

### Reference page with side navigation (a command-line tool manual)

- Shell of three regions: section navigation on the leading side (about 14 to 17rem), the article in the middle, an outline of the current page on the trailing side (about 12 to 15rem), visually quieter than the navigation.
- Article prose capped near 65ch. Wide blocks such as code stay inside the article region and scroll sideways rather than wrap.
- Navigation and outline stay in view while the article scrolls. On narrow screens the navigation becomes a menu and the outline folds into a collapsible list at the top.
- The header shares its edges with the shell, not with the viewport.

### App shell (Fieldnote)

- Navigation on the leading side or the top; main region with its own page header and content area.
- At least one alignment is shared by all regions, for example the baseline of the page title with the first nav item, or the left edge of the content with the header logo.
- The main region decides its own measure: prose settings get a cap, tables and canvases fill the width.

### Settings page (Fieldnote preferences)

- A short list of sections as local navigation or tabs; the form column about 40 to 60ch wide, labels above fields.
- Each section is a heading, a sentence of purpose, then its controls; the save control sits where it is always visible.
- Do not fill a wide screen with a narrow form's worth of controls stretched across; leave the space empty.
