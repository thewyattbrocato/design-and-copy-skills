**Use a 1px line between rows.** Make it a hairline in a quiet color, inset to align with the text edge, and omit it after the last row.

**Why it wins for 30 dense rows**
- **Scanning:** Each row has three fields (date, merchant, amount). People scan across them and down the list. A rule gives the eye a clear horizontal track, so the amount stays matched to its merchant.
- **Density:** Space between rows spends vertical room. With 30 rows, you'd scroll much further, and the rows would start to look like separate cards. A hairline costs about 1px.
- **Pairing:** Add a little vertical padding inside each row, about 12 to 16px. The rule then has room on both sides, so it doesn't crowd the text.

**Why not the others**
- **Alternating backgrounds (zebra stripes):** These work in wide tables with many columns, where the eye can lose its row. Three fields don't need that help. Stripes also add visual noise, and they fight with other states such as pending, selected, pressed, or a highlighted new transaction. In dark mode, subtle tints often vanish or look muddy.
- **Extra space only:** This works when there are few items. At 30 rows, the gaps get large enough that rows start to look like separate objects. Using space alone also makes it harder to tell where one row ends and the next begins when the rows are tightly packed.

**Details**
- **Date grouping:** Put a date header (for example "Today" or "Oct 27") above each day's rows. Use more space above the header than below it, and keep the date out of each row. The headers do the coarse grouping, and the hairlines separate rows within a day.
- **Alignment:** Right-align amounts, ideally with tabular numerals, so the digits line up in a column.
- **Touch targets:** If rows open a detail view, keep each row at least 44px tall. The padding above covers this.
- **Rule color:** Keep it low contrast. If the line is as prominent as the text, it adds noise.

Use space only to group (between days), a rule to divide (between rows), and skip stripes unless you later add many more columns.
