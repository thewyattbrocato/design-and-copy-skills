The layout mostly holds. The order is clear, the steps between levels are visible, and the page has no decoration without a job. Leave the type scale, the dividers, the section spacing and the no-icons, no-cards approach as they are. These are the changes I'd make, most important first:

1. **Cap the content width.**
   - You didn't mention a max width. If rows stretch across a wide screen, the switch ends up far from the setting name, and the eye loses its row.
   - Fix: limit the content column to about 640–720px, with the switch at its right edge. Left-align the title, sections and button to that same column.

2. **Make sure Save still stands out when the page is mostly teal.**
   - Teal is reserved for switches and the button, which is good. But if most defaults are "on", the page will have many teal switches and the button won't pop.
   - Fix: check this by squinting at a realistic state. The solid, larger button should win. If it doesn't, use a darker teal for the button or increase its padding. Don't add anything else to it.

3. **Don't rely on color alone for on and off.**
   - Teal versus grey can look the same in grayscale or for color-blind users.
   - Fix: the knob position (left or right) must carry the state. Each switch also needs an accessible name and state, taken from the setting name.

4. **Check the grey text contrast.**
   - Grey 14px text is the usual place for contrast to fail, and it's what separates the explanation from the setting name.
   - Fix: use a darker grey, not a lighter weight. It should clear 4.5:1 against white. The same applies to the description under the page title.

5. **Keep Save reachable and 'Reset to defaults' safe.**
   - Save sits at the bottom of a long page. Users may toggle something and never scroll down to it.
   - Fix: make Save visible once something changes, for example in a sticky footer that keeps the same left alignment. Give 'Reset to defaults' a clear gap from the button and a confirm step or an undo. It stays a plain link, because it shouldn't compete with Save.

Two assumptions: I took the 18px headings to be the right size for settings groups, since the 16px regular rows below them carry the page. I also assumed every section has several rows. If "Weekly summary" has only one, the divider lines and generous spacing may be more than it needs.
