# Page and focus access

Load when the fix pass has the page's code in hand and the ask touches access, keyboard use, "accessibility pass" or "before we ship". The component floor (names, focus, contrast, zoom) is in [states-and-checks.md](states-and-checks.md); this file checks the page as a document and the focus details generated code gets wrong. Each entry is a default with an exception. Read the markup, fix what fails, leave what passes. Do not add ARIA to markup that already works, and do not turn the answer into an audit list.

## The page as a document

Default: when more than about three tab stops come before the main content, the first focusable element is a link to the main region. It becomes visible on focus, and its target exists and can take focus. Change when one or two stops precede the content: a skip link only adds a stop.

Default: every page and every view has its own title, page-specific words first and the product name last, and the title changes when the state changes the page (step 2 of 4, 3 errors, 12 results). Change nothing when the titles already differ and track state.

Default: one h1 that names this page, not the product on every page. Levels follow the structure and never skip going down; a region people would jump to without a visible heading gets one. Pick a level for its place in the outline, not its size. Language is set on the root element; the detail is in responsive-layout.

Default: after script swaps the content of a single-page view, update the title, then move focus to the new view's main heading (made focusable by script with `tabindex="-1"`) or announce the new view in a short polite message. Never leave focus on an element that was removed. Change when only a region inside the view changed: keep focus where the person was and announce the result.

Test: read the page with styles off, then with the title and headings alone. Could you tell where you are?

## Order and focus

Default: source order, visual order and tab order agree. CSS that reorders interactive items (flex or grid `order`, explicit grid placement, absolute positioning, reversed rows) is fixed in the markup, not patched with `tabindex`. Change when the reordering is only decorative and nothing in the area takes focus.

Default: no positive `tabindex`. Use `0` only on a custom element that must take focus, and `-1` only on a target that script focuses (a view heading, a dialog, an error summary).

Default: nothing fixed to the bottom of the viewport (consent bar, chat tab, sticky action bar, toast stack) covers the focused element. Reserve space or scroll margin, dock the bar, or let it scroll away. Sticky headers are handled in responsive-layout and data-tables.

Test: tab through the main task with the bars in place; the focus ring is never behind one.

## Names and hiding

Default: a control's accessible name contains the words visible on it, at the start, so someone using voice control can say what they see. A hidden label never replaces visible text with different words, and a name does not repeat the role ("Save button" is read as "button, Save button"). An icon-only control is named by its action and object.

Default: nothing focusable is hidden from assistive technology. `aria-hidden="true"` or a presentation role on a link, button or input, or on a container that holds one, is a defect. Text meant only for screen readers uses a visually-hidden class, not `display: none`. Content hidden from everyone is also out of the tab order: a menu hidden with opacity or a transform that still takes focus needs `hidden`, `inert` or `visibility: hidden`.

Test: search the markup for `aria-hidden`, `role="presentation"` and `tabindex`; each hit has a reason.

## Pointers and focus styles

Default: a custom control acts when the pointer is released, moving off before release cancels, or the action can be undone. Native buttons already do this; a handler on `mousedown` or `touchstart` is the usual failure. Change when the action is a drawing or drag gesture, where the press is the point.

Default: the focus ring is an outline, not only a background, border or shadow, so it survives forced colors. A shadow-style ring gets a transparent outline beneath it. Selected and focused look different, so a person can tell where they are from what they chose.

Test: turn on forced colors or inspect the computed outline; a ring that vanishes is a fail.

## Text and third parties

Default: headings, prices, dates and calls to action are live text, not pixels inside an image, and no meaning lives only in a CSS background image. An image that carries information has its alternative in the markup. Change when the text is the logo or a work of art.

Default: consent banners, chat and feedback widgets, and embedded players get the same dialog and focus checks as first-party code. An overlay injected on load has no opener to return focus to, so prefer a non-modal banner placed in the reading order. A third-party overlay widget that claims to fix access is not a fix; fix the markup.

## Say what was only read

Default: the closing note names which probes were not run, as a short line: keyboard walk of the main task, 200% text and 320 px width, forced colors, reduced motion, a screen-reader pass. Reading code finds present or absent attributes; it does not show that the order makes sense or that a name is the right one. Never call the result accessible.

## Keep proportion

- Fix what the code shows is broken, in order of harm; a clean page gets one sentence saying so.
- A short ask gets a short answer. Apply an entry only when its situation exists in the code in front of you.
