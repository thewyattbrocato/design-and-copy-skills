# Purpose and budget

Load this before adding motion. It decides whether to animate; the other files decide how.

## The four-question test

Animate only when the motion answers a question the person is asking right then:

- **Where did it go?** Show where something came from or went, so the layout stays a map.
- **What changed?** Draw the eye to the one thing that changed.
- **Did it work?** Tell people an action registered or finished, or connect an action to its result.
- **How do I use it?** Preview what a gesture will do, or teach a gesture or control once.

If a motion answers none of these, it is decoration. Decoration and brand motion (carrying a trait the brand has named, such as calm or energetic) are allowed only when the brief asks for them, and then only off frequent paths and out of the way of reading.

## The frequency rule

Cost is duration times how many times it is paid. A 300 ms entrance on a menu opened fifty times a day costs more than a 1.5 s intro seen once.

| How often | Spend |
|---|---|
| Constant (hover, press, typing, scrolling) | Instant or about 100 to 150 ms; no travel. |
| Many times a session (menus, tabs, toggles, list changes) | About 150 to 250 ms, one simple property or two. |
| A few times a session (overlays, panels, toasts) | About 200 to 300 ms, a little direction. |
| Rare or first run (onboarding, empty-to-first-item, a launch moment) | Up to about 500 ms, richer, and skippable. |

If a step is blocking (people cannot continue until it ends), halve the budget.

## Motion to cut or shrink

- Fades on content that is already in view when the page loads.
- Entrances that repeat on every navigation.
- Hover motion that moves the target away from the pointer.
- Looping attention-getters on a persistent control.
- Counting up a number people came to read; show the number, and animate only if the change itself is the news.
- Background motion behind text.
- Delays added "so it feels like something is happening".

## Motion worth keeping

- A panel that slides from the edge it belongs to.
- The same object traveling to its new place.
- A short press response on every tappable control.
- A brief highlight where a value changed behind the person's back.
- Skeletons or progress for waits people will feel.

## When someone just says "more delightful"

Do not add motion everywhere. Find the two to four moments that matter, such as a completed task, a first success or a rare celebration, give each a job and a budget, and leave frequent paths quiet. State what you will not animate.
