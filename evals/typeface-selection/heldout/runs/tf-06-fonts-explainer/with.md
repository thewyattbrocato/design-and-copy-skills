**What a variable font is**

A normal font family is a stack of separate files: Regular, Bold, Light, Italic and so on. A variable font puts all of those into one file. It also lets the website pick any weight in between, such as 350 or 620, instead of only the preset ones. Think of a dimmer slider versus a light switch with a few fixed settings.

**Is it better?**

It depends on how many styles you use.
- **Where it's better:** if your site uses several weights (a light body, a medium subheading, a bold headline), one variable file is usually smaller and faster than three or four separate files. You also get finer control over the look.
- **Where it makes no difference:** if you only use one or two weights, a regular font is just as good.
- **Where it can be worse:** the file can be larger than a single static weight, so it's not automatically faster.

Your designer chose it, so it's fine to use. You don't need to change anything.

**Are you allowed to put it on your website?**

I can't tell from the file, and I don't want to guess. Having a font file doesn't mean you have web rights. Many fonts are licensed for desktop use, such as print and design software, but not for websites. Web use is often a separate license, and it sometimes depends on traffic.

I don't recognize "Marlowe" well enough to say who owns it or what its terms are. Ask your designer these questions:
1. Where did the font come from? Is it open-source (for example, the SIL Open Font License, which allows web use), purchased, or custom-made for you?
2. Does the license cover **web embedding** (self-hosting on your site)? Ask for the license document or receipt.
3. Is the license in **your bakery's name**, or in the designer's? Some licenses don't transfer to clients.
4. Are there limits on monthly visitors?

If it was custom-made for you, ask for that in writing too.

If the answers are murky, you have a safe fallback. Ask the designer for a font that's open-licensed, or buy the web license from the foundry that makes Marlowe.

**Practical notes for the build**
- A `.ttf` file works on the web, but the usual practice is to convert it to `.woff2`. That's a smaller file that loads faster. Many font licenses allow this, but check yours first. Some prohibit modifying or converting the file.
- Your developer or site builder should also set a fallback font. If Marlowe fails to load, visitors then see something reasonable instead of a default Times-style font.

If you tell me how you're building the site (Squarespace, Shopify, custom code), I can say how to add the font. Squarespace and Shopify both have their own steps for uploading custom fonts.
