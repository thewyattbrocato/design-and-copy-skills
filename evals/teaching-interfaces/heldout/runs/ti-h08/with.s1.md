You're right. Don't teach all forty on day one. Experts pull help when they want it, and a mandatory forty-step walkthrough fails for three reasons:

- **It's too much at once.** People retain two or three new things before they act. Forty is noise, and most of it is gone by the next morning.
- **It isn't tied to their work.** Nobody needs "jump between matters" until they have two matters open. Shortcuts learned without a task don't stick.
- **It costs this audience more than most.** They're in the app eight hours a day and already have habits. A forced tour delays billable work and feels like a tax.

## What to do instead

**1. Day one: one small win, plus an exit.**
Skip the walkthrough. Let them start working, and teach two or three shortcuts on a real first task. Candidates are the command palette (if you have one), quick-cite, and the shortcut to open the reference sheet. The goal sentence is: *"Afterwards they can find and run any action from the keyboard."* The command palette does most of that, because it makes the other thirty-odd discoverable. Make it skippable, and leave a way back to it.

**2. Put the shortcut at the moment of action.**
This does most of the teaching.
- Show the shortcut beside the menu item, button tooltip, and palette entry, such as "Split view ⌘\\". Use your real bindings.
- After someone clicks something that has a shortcut, show a quiet, dismissible hint: "Next time: [shortcut]". Limit it to one hint at a time, and stop after they've used the shortcut once or dismissed it twice.
- Base hints on behavior. Someone who opens the matter switcher with the mouse ten times a day is the person who should hear about the jump shortcut.

**3. Give them a reference they can pull.**
- A searchable shortcut sheet, opened by `?` or from the help menu, grouped by task (matters, citing, layout, editing) rather than alphabetically.
- A printable or pinnable version. Lawyers like paper cheat sheets.
- Let them rebind keys. Power users will want to, and it avoids conflicts with habits from Word or Westlaw.

**4. Release the rest over time, through real work.**
- After a week or so, a "what's new for you" note can point out one or two shortcuts that match what they actually do. Tie it to activity, not the calendar, and don't use streaks or nagging.
- Announce each new shortcut in the release notes where it's relevant, with a one-line "try it now" action.

**5. Fix it where you can.**
If a shortcut needs heavy explanation, ask whether the binding is mnemonic (⌘K for quick-cite, say) or whether the action should be more discoverable. Consistent, guessable keys beat any tutorial. Cluster the forty into families (all split-view keys share a modifier, for example), so people learn a pattern instead of forty items.

## How to pitch it to the PM

The PM's goal is probably that people actually adopt the shortcuts, and day-one completion is only a proxy for that. Propose measuring adoption directly:
- the share of users who use at least one shortcut unaided at day 14 and day 30
- the number of distinct shortcuts used per active user over time
- the day-one skip and abandon rate for the current plan, if you can test it

You could run both approaches as an A/B test: the full walkthrough against the contextual approach above. I'd expect the contextual one to win on later usage. Because I haven't tested it, I'd treat that as a prediction until the data shows it.

I assumed you have a command palette and a help menu. If you don't, the palette is probably the highest-value thing to add first. I can sketch the day-one first-task screen or the shortcut sheet layout next if you'd like.
