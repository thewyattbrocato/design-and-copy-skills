# Who it is for, how state shows, and how long things take

Load when choosing density or a device approach, adding modes, handling waits, or deciding what gets a notification.

## Match behavior to how it is used

Name how long and how attentively people use it, and whether it stays open. Then set size, density, help and loudness together.

| Use | Behavior |
|---|---|
| Long daily sessions (editors, consoles, back office) | Use the full screen, dense and calm, small accents, status in the margins, several routes to a command (menu, shortcut, palette), frequent controls close, rare or view-changing ones tucked away |
| One-job, occasional (checkout, a share sheet, a settings dialog, most phone apps) | One view, large labeled controls with a verb and an object, instructions on the surface, few demands on the hand, remembered last settings |
| Glance or background (widget, status, notification) | Silent until something needs attention; an indicator appears only if it shows useful state; tapping a problem goes straight to the fix |
| Public or first-time (kiosk, ticketing, shared screens) | Big targets, no hidden steps, progress in the flow, an escape from every step |
| TV, car, voice, appliance | Visible focus, flat navigation, a few big items, glanceable; physical controls can beat a screen; no modes; do not import desktop idioms |

One product often holds several. A rarely used builder inside an editor behaves like a one-job tool. Phones and small windows lean one-job. Density is earned by consistent landmarks, not by cramming.

For control order: constant use within reach, daily within a click or two, rare deeper, risky or view-wrecking hard to hit by accident. Hide rare features rather than deleting them.

Teaching newcomers: a skippable overview of five to seven short cards at most, relaunchable, plus help written in the person's words; permanent training wheels get in the way of the practiced. A tour is for invisible gestures or structure, not for things the first task shows. See `teaching-interfaces` if installed.

## Where state shows

- In the main view, at a glance: counts, badges, progress rings, presence dots, a freshness note on live data. Detail on hover, focus or tap.
- Normal operation is silent. Success needs at most a quiet cue; failure stays until noticed. Anything worth interrupting stays visible, and anything that is not goes in ambient state, not a vanishing popup.
- Toasts are for events with an action or link (Undo, View). Keep a notification list people can review.
- Optimistic and offline states are visible: pending, failed with retry, queued.
- Modes: indicator at the point of attention (cursor, highlighted tool, banner such as "Editing" or "Selecting 3"), Esc or a clear control to leave. Reserve modifier-key chains for experts, and never as the only route.

## Response ladder (starting values)

- Up to about 0.1 s feels instant: no feedback needed.
- Up to about 1 s: keep the flow unbroken; press feedback within 100 ms, and an inline loader only after about 300 ms, kept about 400 ms once shown.
- Up to about 10 s: progress with text; a determinate bar when the length is known, a skeleton when the shape is known.
- Beyond that: move it to the background, show remaining time or steps, allow cancel (and pause for transfers), keep the interface usable, and notify when done.
- Disable the trigger only to stop a double submit, and say why.
- Motion that carries feedback follows `ui-motion` if installed: short, interruptible, with reduced-motion handling.

## Controls tell the truth

Anything that looks pressable shows hover, focus and pressed states and does what its label says. Links go somewhere, buttons act. A faint link beside a loud button must not hide the person's real alternative. A toggle's label states the current state. Do not use editable-looking fields for read-only output. Every function reached by hover or right-click also has a visible, focusable route.

## Cheap checks for a spec

- Which of these screens would still work for the least practiced realistic user, and for the most practiced?
- What does the person see within a second of acting, and after ten?
- What happens offline, on failure, and when two people edit at once?
