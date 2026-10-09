# Components and governance

## Component spec template

- **Purpose** in one sentence, and when not to use it (name the component to use instead).
- **Anatomy**: parts, each tied to tokens (surface, text role, border, radius, space).
- **Variants**: only those that differ in behavior or hierarchy (primary, secondary, quiet, destructive), not in decoration.
- **Sizes**: a small set tied to target size; the smallest still meets touch and pointer targets.
- **States**: default, hover, focus (visible ring, not color alone), pressed, selected, disabled, loading (keeps size, blocks double submit), error, empty where relevant. Each state names the tokens it changes.
- **Content**: label length and tone, truncation or wrapping rule, icon placement, translation growth, empty or missing values.
- **Accessibility**: accessible name, role, keyboard, focus order and return, announced changes, contrast per theme, reduced-motion behavior.
- **Examples**: one or two on real screens, one with worst-case content; where it is used.

## Documentation page

Principles with reasons, then components, then patterns that combine them, then misuse (a short gallery of "not like this" with the fix). Every page names an owner and the last change. Prefer live examples drawn from the same code as production over screenshots.

## Governance

| Change | Rule |
|---|---|
| Add | Second real use, an owner, spec and states, accessibility checked |
| Modify | Say whether it is visual only or behavior-changing; list affected places |
| Deprecate | Announce, give a replacement and a removal date, keep the alias |
| Remove | Only after usage reaches zero or the date passes |

Version with a changelog readers can scan. Provide a contribution path with a short template and a response time. Decide who can refuse a request and write down why. Small teams: one owner, one page, review in the normal pull request.

## Rollout checklist

Ship internally first. List every place the old values live (code, design files, email templates, charts, docs, marketing pages) and tick them off. Measure adoption by what shipped on tokens, not by opinion; if you have no measurement, say it is unmeasured.
