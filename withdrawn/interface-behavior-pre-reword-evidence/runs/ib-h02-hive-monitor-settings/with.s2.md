**Assumptions:** The users are hobbyist beekeepers on phones, often outdoors at the hive. They open settings rarely, mostly after adding a hive or when an alert fires. Nobody has tested any of this, so I've favored changes that are low-risk and easy to reverse.

## Changes, in priority order

**1. Apply changes immediately and drop the Save button and the "Discard changes?" popup.**
- When someone toggles a setting or edits a field, save it right away and show a small "Saved" state next to the control.
- Keep a quiet "Undo" toast for a few seconds after each change. Announce it to screen readers.
- Why: the popup exists only because of the Save button, and it's the likeliest place people lose work. Everything on this page can be reversed, so a batch Save adds nothing.
- Exceptions: number fields (alert thresholds) should commit on blur or Done, with range limits. If the value is out of range, say so next to the field and keep the last valid value. A sync-account change that could disrupt data can keep an explicit Apply.

**2. Remove "Are you sure?" on the temperature unit.**
- Switch the unit immediately and convert displayed values.
- Why: it's fully reversible. Make sure thresholds are stored in one canonical unit, so toggling back and forth doesn't round them into drift. Show "Thresholds converted: 35 °C is 95 °F" inline if that helps.

**3. Give new hives sensible alert defaults.**
- A new hive starts with the core alerts on (for example temperature out of range, humidity out of range, and sensor offline). Show them as "Recommended" with a one-line note beside them, plus an "Edit" link.
- Why: all-off means the product silently does nothing until someone finds 38 toggles. The cost of a wrong guess is a few extra notifications, and that is easy to turn off.
- Also, ask "Copy settings from another hive?" when adding a second hive or later. Remembering the last choice beats asking again.
- The exact threshold values need input from your beekeeping or sensor people. I won't invent them.

**4. Regroup the page by how often people touch things, not by when engineering added them.**
- Top level, with about five rows: **Hives** (one entry per hive), **Notifications**, **Units**, **Sync & account**, **Advanced**.
- Per-hive alerts live inside each hive's own screen, since that's where people look when an alert fires. Within a hive, show one row per sensor with a single master toggle. Thresholds expand only when you tap in.
- Group Advanced under a collapsed section: low-level thresholds, sync intervals, diagnostics.
- Add search at the top if the page still has more than about 15 visible rows afterwards.
- Why: 38 undifferentiated controls force people to scan everything. Grouping by frequency and by hive means most visits touch one screen.
- Label each setting as per device (notifications, units) or per account/hive (thresholds, sync). Today that's probably ambiguous.

**5. Make "Reset everything" rare, specific and recoverable.**
- Move it to the bottom of Advanced, away from any primary control. Right under Save is where misclicks happen.
- Replace it with narrower resets, for example "Reset this hive's alerts to recommended" and "Reset units and notifications". They're less scary and more useful.
- If a full reset stays, make it undoable. Keep the prior settings for a short window, with an "Undo reset" toast or banner. If that's not feasible this release, use one specific confirmation: "This resets alerts and units for all 3 hives. Hive names and sensor history are kept." It should say what's affected, name the action on the button ("Reset settings", not "OK"), and not be red-by-default for non-destructive cases.
- Why: this is the one action here that is hard to reverse, so it's the one worth a confirmation if undo isn't available.

## What I'd skip this release
Search, copy-from-hive, and the full regrouping are bigger changes. If time is tight, ship in this order: 1, 2, 3, 5, then 4. The first three are mostly deletions or default changes, and together they remove most of the friction you described.

## Since you can't test with users
- Ship behind a flag or staged rollout, if possible, and watch for support contacts about settings, alert-opt-in rate on new hives, and how often people reach the undo toast. I don't have numbers for any of these, so set your own baselines from current data.
- Reviews are a cheap signal. Tag "confusing" reviews before and after the release.
- Do a quick internal check with someone who has never seen the app: ask them to add a hive and get notified when it's too hot, and watch where they stall.
