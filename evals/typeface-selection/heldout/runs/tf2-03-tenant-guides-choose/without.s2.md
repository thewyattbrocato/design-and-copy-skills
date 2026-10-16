**Recommendation: use one free, highly legible family for the whole guide, and make sure it still looks fine when it falls back to a system font.**

**Body text**
- **Print handouts:** Use **Atkinson Hyperlegible** or **Source Sans 3**. If you prefer a serif, **Charter** or **Source Serif 4** works well at 11–12 pt.
- **Web pages:** Use the same family, with a fallback stack that works on any device.

**Headings**
- Use a bold weight of the same family. One family keeps the guides consistent, cuts file weight, and gives you only one font to manage.

**Why these**
- **Atkinson Hyperlegible** was designed by the Braille Institute for low-vision readers. Its letterforms are easy to tell apart (I/l/1, O/0), which helps with dates, dollar amounts, and case numbers. It's free under the SIL Open Font License.
- **Source Sans 3 / Source Serif 4** are free, open-licensed, and well hinted. They render cleanly on older Android and on Windows library machines. They also have good weight ranges, so you can build clear hierarchy in a long guide.
- Both are on Google Fonts, so there's no licensing cost for web or print.

**Web setup for older devices and library computers**
1. **Self-host the font files** (WOFF2) instead of loading from Google. Library networks sometimes block or slow third-party requests, and self-hosting also avoids privacy concerns for your readers.
2. **Load only the weights you need.** Regular, italic, and bold is usually enough. Keep the total under about 100–150 KB for slow connections.
3. **Use `font-display: swap`** so text shows immediately in a fallback font, then switches.
4. **Set a fallback stack that matches the look:**
   - Sans: `"Atkinson Hyperlegible", "Source Sans 3", Roboto, "Segoe UI", Arial, sans-serif`
   - Serif: `"Source Serif 4", Charter, Georgia, "Times New Roman", serif`

   Roboto is on nearly every Android phone, and Arial and Segoe UI are on nearly every Windows machine.
5. **Test with the font blocked.** The guide should still read well in Roboto or Arial, because some readers will see exactly that.

**Sizing and layout**
- **Web:** Use at least 18 px (about 1.125 rem) body text, a line height of about 1.5, and a line length of 60–75 characters. Small screens and older eyes both benefit from this.
- **Print:** Use 12 pt body text if you can afford the page count. Use 14 pt or larger for key warnings and deadlines.
- Avoid light weights, all-caps paragraphs, and long stretches of italic. Use bold for deadlines and actions, sparingly.
- Use real text, not images of text, so screen readers, translation tools, and browser zoom work.

**What to avoid**
- Decorative or script fonts.
- Ultra-thin weights, which wash out on low-quality screens and photocopies.
- Commercial fonts you'd have to license, such as Helvetica Neue or Proxima Nova, when free options do the job.
- Many different fonts. Two weights of one family is plenty.

**If you only do one thing:** pick Atkinson Hyperlegible or Source Sans 3 and use it everywhere. That choice will do more for readability than any further tuning.

If you tell me which tools you use to produce the guides (Word, Canva, InDesign, a CMS like WordPress), I can give you specific setup steps. For example, some of these fonts need to be installed on the machine that exports the PDF.
