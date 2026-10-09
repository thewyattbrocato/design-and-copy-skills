I'd push back on the hero stat and the bigger cards. With 40 to 60 trucks that can't scroll, anything large takes space from the trucks, and "most important" is hard to define on a fixed screen. The table's real problem is probably that it's a list: 60 rows at normal height won't fit on one display, so dispatchers are scanning for the one row that matters.

**Organize by status, not by truck importance.** Use five lanes across the screen, in workflow order:

```
ARRIVING (4) | WAITING (12) | LOADING (9) | UNLOADING (11) | READY TO LEAVE (6)
[card]       | [card]       | [card]      | [card]         | [card]
[card]       | ...          | ...         | ...            | ...
```

- Each lane is a column of compact cards, sorted by minutes on site, longest first. The top of each lane is always the thing that needs attention.
- Lane headers show the count, so the totals are the summary and you don't need a hero stat.
- Put "Ready to leave" at the right end, since that's where trucks finish.

**Use time, not size, to show urgency.** Set a dwell target per status (e.g., waiting over 45 min, loading over 90 min). Cards past target get a colored left edge or border, and the rest stay neutral. Keep cards the same size. Color should mark exceptions only, or the screen becomes the "overwhelming" thing they're complaining about.

**Card contents, in order of scan priority:**
1. Dock door as a bold badge (dispatchers think in doors)
2. Truck ID, bold
3. Minutes on site, large, tabular numerals
4. Carrier, smaller
5. Notes, one line, truncated; the full note on click or hover is fine since it isn't hiding a truck

Status doesn't need its own field because the lane already says it.

**Top strip, kept slim:** a single row with the lane counts (repeated for glanceability if you want), the current time, and maybe the longest current wait. That's the one thing that deserves a larger number.

**Things to verify before building:**
- **Uneven distribution.** The layout breaks if 25 trucks land in Waiting. Build the lanes to flex: card density should tighten automatically as a lane gets longer (compact rows past a threshold), and you should test the worst-case split, not the average.
- **Text size.** Dispatchers read this from a distance, so plan for 14px minimum for body text and larger for ID and minutes.
- **Screen size.** Test on the actual monitors in the yard, since 60 trucks fit very differently at 1080p and 4K.

If you want an alternative, a dock-door grid (one tile per door, with the truck in it) fits how some yards think, but it doesn't show the queue, so I'd keep it for a secondary view if you need one. I'd start with the status lanes.

I can build a quick HTML mockup with 60 sample trucks, including a skewed distribution, so you can check density on a real screen size. Want me to do that?
