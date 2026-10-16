The printer is half right. Calling it a cop-out is also half right, because "just how print works" isn't an answer to your problem.

**What's true:** #ff6a1a is a fully saturated screen orange. Screens make color with emitted light, and print makes it with ink on paper, which can't get as bright. Standard CMYK can't reach that orange, so some dulling is unavoidable.

**What's not an excuse:** Orange normally survives CMYK as a clearly orange color, not a brown one. Brownish usually means something avoidable went wrong. The likely causes are:
- The file was converted automatically, and cyan or black crept into the mix. Any cyan or black in an orange makes it muddy.
- The proof used an uncoated or cream stock, or a profile for one. Uncoated paper absorbs ink and dulls everything.
- The file was converted with the wrong color profile.

I can't tell which it is without seeing the file and proof. The printer can tell you in a minute.

**What to do:**
1. **Ask the printer three things:** the CMYK values in the file for that orange, the paper stock, and the color profile they converted to. If the orange has more than a trace of cyan or black, that's the fix.
2. **Set the CMYK values by hand.** Don't rely on auto-conversion. A reasonable starting point is about C0 M70 Y100 K0, with cyan and black kept at zero. Treat those numbers as a starting guess and adjust them on a new proof.
3. **Consider a spot ink.** Pantone 1585 C is close to your orange, and an ink mixed to a formula can be much brighter than CMYK. It costs more, since it's an extra plate or press run. For a menu, it may be worth it if the orange is the brand's signature. Check the number against a physical swatch book, because I'm going from memory. Use the coated or uncoated version that matches your paper.
4. **Judge a physical proof.** Don't judge on a screen or a photo of the proof. Ask for a hard proof on the real stock, or a press check. Look at it in the light where the menus will actually be used.
5. **Accept a small remaining gap.** Even done right, print orange and screen orange won't match exactly. Pick the printed version you like and treat it as the print version of the brand color. If the web orange is slightly brighter, that's normal.

If you send me the proof's CMYK values and the stock, I can tell you more about what went wrong.
