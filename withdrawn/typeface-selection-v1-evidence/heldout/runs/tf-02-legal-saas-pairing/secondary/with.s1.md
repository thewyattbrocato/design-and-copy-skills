**Recommendation:** Use system fonts in two roles. Keep the product UI on the system sans alone. On the marketing site, pair a Palatino-first serif for headings with that same system sans for body text.

**Product UI: one family, no serif**

Billing software needs calm, legible screens, and one family with a full weight range does that. Use tabular figures for amounts and counts so columns line up.

```css
--font-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;

body { font-family: var(--font-ui); font-synthesis: none; }
.amount, td.num { font-variant-numeric: tabular-nums; }
```

**Marketing site: serif headings, system sans body**

Palatino gives the heritage, measured tone that suits a law-firm audience. It is on Mac and Windows. Georgia is the fallback because it is the most widely available serif on Apple and Windows devices. Use the serif only for large, short headlines, and keep body copy in the system sans.

```css
--font-display: "Palatino Linotype", Palatino, Georgia, serif;

h1, h2 { font-family: var(--font-display); font-weight: 400; letter-spacing: -0.01em; }
```

**Checks before shipping**

- **Android:** Palatino and Georgia are not guaranteed there, so headings will fall to a generic serif. Look at a real phone before deciding this is acceptable.
- **Windows and Mac:** The system sans is Segoe UI and SF respectively. Check that the tabular figures and weights you use exist on both.
- **Coverage:** I have assumed a Latin-script audience. If you ship other scripts, the stacks need checking.

**Assumptions:** screen use only, no installed fonts beyond the OS defaults. I have not verified each platform's font list or license terms, so confirm both on the devices you target.
