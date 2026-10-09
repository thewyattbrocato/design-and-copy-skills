The reviewer is right in general but wrong for this board. Keep the cards.

**Why cards fit here**
- **Each task is a discrete object people move.** A card's border and shadow tell users "this whole thing is draggable and moves as one unit." Plain space can't signal that.
- **The shadow does real work during a drag.** A lifted card needs to read as sitting above the columns. Without a container edge, the dragged item blends into the items it passes over.
- **Dense, repeated items need clear boundaries.** Tasks stack tightly, and each has a title, assignee, labels and so on. Whitespace alone makes it hard to tell where one task ends and the next begins, especially with variable-length titles.

**Where the reviewer has a point**
Cards get overused when they wrap content that isn't an independent, movable object. Examples are a card around each column, a card inside a card, or cards on a settings page. If the board does any of that, drop the extra containers.

**Practical suggestions**
- Keep one card level: the task card. Leave columns as plain space, or give them a subtle background tint with no border or shadow.
- Use a light border at rest and save the stronger shadow for hover and drag. That makes the shadow mean "lifted", and the board looks quieter overall.
- If the reviewer's real complaint is visual noise, soften the borders and shadows rather than removing the cards.
