It's mostly sound. The single capped column, the subheads, and the hanging pull quotes with a clear job are all right for a long read. Here is what I'd change or check before shipping.

**Worth fixing**
1. **Pull quote overflow.** A 66-character column at 18px is roughly 600 to 650px wide. On a 800 to 900px viewport, each margin is only about 80 to 125px. A quote hanging 80px into it will touch or clip at the screen edge. Only hang quotes when each side margin is at least 80px plus about 24px of breathing room. Below that width, keep them inside the column. Test at 768, 900, and 1024px.
[...]
3. **Top bar edge.** A logo pinned to the far left over a centered column gives you two unrelated vertical edges. Either align the bar's inner container with the lead image width (or the text column), or keep it full-width on purpose, as many sites do. Pick one deliberately. If the bar stays full-width, it's a minor issue.
[...]
**Leave as is**
- 66 characters at 18px with generous leading.
- Subheads about every 300 words.
- A lead image wider than the text, since it is the one deliberate break.
- The order after the article: more from this issue, then the subscribe box, then the footer. It stacks fine on a phone.

None of this is a redesign. Fix the pull quote breakpoint and define the phone behavior, and it's ready to ship.
