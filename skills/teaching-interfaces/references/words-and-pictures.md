# Words and pictures

Load for explainer cards, diagrams, instructional video or animation, and narration or caption decisions. Starting values; change them when the content says otherwise.

## When a picture earns its place

- Use one when it shows the relationship the words describe: parts and how they connect, branches, nesting, hand-offs, a before and after. Skip it when it only sets a mood or repeats a model the reader already holds.
- A straight run of steps with no parts, branches or hand-offs is a numbered list. Default to the list; draw it only when the picture adds what a list cannot, such as where something sits on a screen or a machine.
- If the confusion comes from a missing word, a poor label or a skipped step, fix that instead of drawing around it.
- A picture for experts adds little; for newcomers it carries most of the explanation. Design for the newcomer and keep the words short enough that an expert can skim.
- If a photo or illustration would be the thing remembered instead of the idea, cut it or shrink it.

## Decide before drawing

- Settle three things first: who reads it, what they can say or do afterwards, and what stays out. The heading carries the takeaway. Mention an omission only when leaving it out could mislead, in one short line.
- Default to one question per diagram. A second question gets a second diagram or a build-up step; change this when two answers must be read together, such as a request and its reply.
- List what the reader will ask ("what if the payment fails?") and make sure a part answers each. Cut any part whose removal leaves the takeaway intact.
- If you would need to walk someone through it, it is not finished. Detail kept for a guided tour belongs in the tour, not the picture.
- Say whether it shows how things are or how they could be. Show both only when they are separated (dashed outlines, a labelled band) and the label wording keeps tense: today's parts and planned parts in identical solid boxes read as promises.
- A schematic that looks like the final screen reads as decided. Mark open parts as open.

## Pick the form by the question

Word the reader's question, then choose. Hybrids are fine; two questions get two drawings.

- How does it happen, who does what: a flow for one actor's logic; swim lanes when several parties hand off (start with whoever begins it). One person's experience with feelings over time is a map: use `journey-and-service-mapping` if installed.
- What is it made of, where does it sit: nesting or a tree for levels and types; a block diagram for parts joined together; a layout sketch for a screen or object.
- Which, why, how do these compare: a two-axis grid for comparison; a scale between two ends, worded neutrally so both are valid; cause and effect with + or - on each arrow, checked by flipping one sign and seeing that the system still makes sense; overlapping sets for what is shared, with every overlap labelled.
- Numbers on a scale are a chart: `chart-design` if installed.

## Arrange first, connect last

- Start with the things (people, places, systems) as plain rectangles with throwaway labels, and place them before drawing lines. Position already says something: a row reads as sequence, an indent as a child. Rectangles forgive long labels; circles and fancy shapes do not.
- One arrangement per relationship: part-of nests inside; type-of branches under a parent; leads-to takes an arrow; relates-to takes a plain line with a word on it; same-as shares a box, which helps when two teams use different words for one thing.
- Collapse many of the same into one stacked shape marked as many. Spread out only the instance that behaves differently.
- A decision is a diamond or a split with the condition written on each exit ("card on file", "no card"). Keep the common path straight and send exceptions to the side.
- One line style per meaning. An unlabelled line must be obvious; otherwise it is a guess.

## Reading order and crossings

- Give an obvious start and one direction that fits the surface: left to right on a wide card or slide, top to bottom on a phone or long page, clockwise for a cycle. Mark the start when there is doubt.
- Rearrange before accepting crossings: swap sides, flip direction, split in two. Line-jump bumps are a last resort. Auto-layout tangles quickly: group nodes into labelled regions, or split by sub-question.
- Default to two to four parts for a first explanation. For a reference diagram that readers already know the system for, about ten nodes is the point to split.
- Align to a grid, and make lines touch the shapes they join.

## Labels, icons and the key

- Put each label on or touching the part it names. A lettered or numbered legend makes the eye travel and the memory hold a code. In inline SVG, place `<text>` beside its shape, or add a short leader line; do not park names in a key.
- Keep a sentence next to the part it explains. On a narrow screen a caption stacked far below the figure recreates the split: reveal the text on the part, or put each step's sentence directly above its picture.
- A hover label is acceptable only when it does not cover the part, only one is needed at a time, and the same text is reachable by keyboard and touch.
- Keep labels to about 25 characters and one grammar (all nouns, or all verb phrases). What does not fit goes in a caption, not a smaller font.
- Give every icon a word. Each reader decodes a bare icon differently; test whatever you cannot label.
- No rotated labels; if one must tilt, run it along its line and never upside down. Shorten it first.
- Give every color meaning a second channel: a word, a line style, a shape. The diagram should still read in grayscale, and red against green alone fails. Differences too small to notice read as noise, but any visible difference reads as meaning, so style equal things equally.
- A key may hold three things: what the symbols mean, where the facts come from and as of when, and a line on how to read it. A key that looks like a decoder ring means too many ideas in one picture. With one or two entries, label directly and drop it.

## Size and access

- Check the smallest width. Labels in a scaled-down SVG shrink with it; keep rendered label text near body size (about 12px at the least). If it falls below, restack, split or shorten; do not shrink type to fit.
- Text and lines meet the current contrast standard (about 4.5 to 1 for text) in both themes; do not hard-code dark strokes.
- When position carries the meaning, give a short text alternative that names the parts and links in reading order, including the words inside. When that runs past two sentences, put the same content as a list beside the figure and keep the alternative short and pointing to it.
- Stand-alone test: hide the paragraph around it. Can a reader state the takeaway from heading and labels? If anyone would need a narrator or a pointer, a label or arrow is missing.

## Fixing an existing diagram

Work in this order and stop when it reads:

1. Wrong reader or too many questions: split it, or cut to the parts that answer one.
2. Wrong form for the question: redraw in the form above.
3. Legend, letters or bare icons: move words onto the parts.
4. Mixed states of time or unmarked plans: separate and relabel.
5. Color alone, tiny text, crossings: second channel, larger text, rearrange.
6. Still needs a narrator: add the missing label, arrow or start mark.

## Stills, motion and segments

- For conceptual steps, a sequence of stills (with the change marked) usually teaches better than a movie, and can be read at the reader's own speed, copied and printed.
- Use motion when the motion is the content: how something moves, flows or reacts. Keep it short, repeatable and pausable; honor reduced-motion by falling back to stills.
- Cut long explanations into segments of ten to thirty seconds or a few sentences, each ended by a visible continue. Do not rely on people to pause a continuous clip.
- Show the parts and their names before the process that uses them.

## Narration, captions and text

- Over a graphic, short narration beats a paragraph beside it, because eyes and ears carry different channels.
- Do not play narration and its identical full text at once. Offer captions as a mode: on, they replace the spoken track's role for those who need them; off, the screen stays clean. A few keywords next to the matching part are fine.
- Add on-screen text when people need to see a word spelled or cannot listen. With no audio at all, text carries the explanation; keep it short and put it by the picture.
- Provide a transcript for any video and captions that match the speech. Nothing essential may live only in the animation.
- Use a human, plain voice. Skip background music and filler lines added for interest.
- For video inside a product, prefer a short clip for a motion-heavy step and an annotated step list for everything the person must do while following along; the list can be scanned, copied from, and used with the product open beside it.
