I'd use a simple list of stacked rows on phones, and a real table on wide screens. If you can only build one, build the list.

**Why not a plain table**

Four fields and 14 rows is a small, light dataset. A table pays off when people compare values across rows or sort and filter. Volunteers don't do that. They scan for a shift that fits their day, then sign up. On a 360px screen, four columns with a date, a location name and a role will wrap or force horizontal scroll, and that's the failure I'd most want to avoid.

**Why not cards**

Cards take too much vertical space. Fourteen of them means a lot of scrolling, and it's hard to compare dates down the page. Cards earn their space when each item has an image, long text or several actions. These shifts have none of those.

**What I'd build**

Each shift is one row, with the date as the anchor.

```
Sat 12 Oct · 9:00–12:00            [Sign up]
Riverside Food Bank
Sorter · 3 spots left
```

- **Date:** bold, on the first line. Sort by date by default, and group under month or week headings if the shifts span more than a couple of weeks.
- **Location and role:** plain text on the next lines. Let the location wrap, and don't truncate it.
- **Spots left:** write it as words ("3 spots left"). When it's low, say "Only 1 spot left". When it's full, say "Full" and disable the action. Don't rely on color alone.
- **Action:** one button per row, at least 44px tall, on the right or below the text.
- **Markup:** use a `<ul>` of `<li>` items, or a `<dl>` inside each item if you want label and value semantics.

**Wide screens**

At about 700px and up, switch the same data to a real `<table>`. Use a `<caption>`, `<th scope>`, and columns ordered Date, Location, Role, Spots left, Action. Left-align the text, right-align the spots count, and give the table a hairline under each row. Sorting on date and location is enough. That way people who do want to compare get a proper table, and phone users never see one.

**Check**

Test at 360px. The date, the location and the sign-up button should all be visible with no horizontal scroll.

I haven't looked at your codebase, so tell me the stack and where this list lives, and I can build it.
