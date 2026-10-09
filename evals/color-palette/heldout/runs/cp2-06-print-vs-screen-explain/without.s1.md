It's partly a cop-out. Print can't perfectly match a bright screen orange, but "dull and brownish" usually means something fixable.

**What's true**
- Your screen makes color with emitted light, and #ff6a1a is very saturated. Standard CMYK ink on paper can't reproduce all of it, so some dulling is unavoidable.
- Paper reflects light instead of emitting it. Uncoated stock soaks up ink and mutes color even more.

**Why yours is probably worse than it should be**
- A good CMYK orange of this kind is roughly magenta ~65–70% and yellow 100%, with no cyan and no black. It should look vivid, not brown.
- Brown means the mix has contamination, most likely cyan or black in the orange. That usually comes from an automatic RGB-to-CMYK conversion with the wrong color profile, or from the file being converted twice.
- The paper stock may also be a mismatch with how the proof was set up.

**What to do**
1. **Ask for the CMYK values in the file.** Open the menu file and check what the orange is actually built from. If there's cyan or black in it, that's the problem.
2. **Set the orange by hand in CMYK.** Start near C0 M68 Y100 K0 and tune it on a proof.
3. **Consider a spot color.** Pantone 1585 C is very close to your orange. A spot ink is mixed to match instead of built from CMYK, so it's much more vivid and consistent. It costs more because it's an extra plate and ink, but for a brand color it's often worth it.
4. **Ask which paper and profile the proof used.** Coated stock gives brighter results than uncoated. The file should be converted with the profile that matches the press and paper, such as FOGRA39 or GRACoL, depending on your region.
5. **Get another proof on the real stock before the full run.** Approve it in daylight, not on a screen.

**Questions to put to the printer**
- What CMYK values did you print this orange with?
- Can you proof it as a Pantone 1585 C spot color?
- Which ICC profile and paper stock were used?

If the printer can't answer those, consider getting a quote from another one. A good printer will work with you on this.

If you can tell me what software made the menu (Canva, InDesign, Word, etc.), I can give you specific steps for setting the color.
