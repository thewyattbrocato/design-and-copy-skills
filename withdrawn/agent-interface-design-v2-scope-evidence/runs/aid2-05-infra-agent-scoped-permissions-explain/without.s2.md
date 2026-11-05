# Redesigning Tidewater approvals

## The problem
Approval only protects you if the approver reads the prompt. At 60+ prompts a day, nearly all of them for harmless commands, the one dangerous prompt looks like the other 59. The namespace deletion shows that the current system has stopped working as a control.

The fix has two parts:
1. Stop asking humans about things that don't need a human.
2. Make the remaining prompts rare, different from each other, and backed by controls that don't depend on someone reading carefully.

## 1. Classify commands deterministically, in tiers

Classification must be code, not an LLM judgment. Parse each command into structured fields (verb, resource kind, namespace, cluster, selector, flags). Don't pattern-match on shell strings. **Anything that doesn't parse or isn't in the table defaults to the highest tier.**

| Tier | Examples | Behavior |
|---|---|---|
| **0: Auto-allow** | `get`, `describe`, `logs`, `top`, `events` on allowlisted kinds and namespaces | Runs immediately and is logged. `get secret` is excluded, because reading is not harmless there. |
| **1: Auto-allow with guardrails** | Delete a single pod owned by a controller, `rollout restart`, scale a deployment within bounds | Runs immediately and posts a one-line notice to a channel with an Undo button where possible. |
| **2: Approve** | Scale beyond bounds, scale to 0, cordon or drain, anything in prod outside Tier 1, selector-based deletes | A one-tap approval with a rich summary (see section 2). |
| **3: Hard gate** | Delete namespace, PVC/PV, CRD, or node. Anything with `--all`, `-A`, `--force`, or `--grace-period=0`. Arbitrary `apply` or `patch`. | A typed confirmation plus a second person. Better still, Tidewater never gets the permission (section 3). |

**Tier 1 guardrails** are part of the tier definition, not suggestions:
- The target must resolve to a bounded set, for example ≤3 pods.
- Scaling is capped, for example at 2× current replicas, a hard max, and never to 0 in prod.
- Rate limits apply, for example no more than 2 restarts per deployment per 15 minutes. This stops a looping agent from turning a "safe" action into an outage.
- Respect PodDisruptionBudgets.

**Resolve blast radius before classifying.** Run a server-side dry run, or a `get` with the same selector, and count what the command will touch. The count can escalate the tier. For example, a delete whose label selector matches 40 pods is Tier 3, whatever the verb looks like.

## 2. Make the prompts that remain hard to skim past

- **Lead with the effect, not the command.** Show "DELETE namespace `payments-staging`: 14 deployments, 31 pods, 6 PVCs (200 GiB), last deploy 2h ago". Put the raw command underneath.
- **Look different by tier.** Tier 2 and Tier 3 should differ in color, layout, and header. A Tier 3 prompt should never resemble a Tier 2 prompt.
- **Tier 3 needs friction that can't be done on autopilot.** The approver types the namespace or resource name. The approver must be a different person from the requester, and in prod must be on a defined approver list. Consider a short delay, such as 60 seconds, before the confirm button enables.
- **Don't batch.** A dangerous command is never bundled with safe ones under one "Approve all".
- **Bind approval to the exact action.** An approval covers a hash of the parsed command plus the resolved target set. It is single-use and expires in about 10 minutes. If the resolved set changes between approval and execution, re-prompt.

## 3. Don't rely on the prompt alone

This is what lets the design be at least as safe as today. Humans will occasionally approve the wrong thing.

- **Least-privilege RBAC for Tidewater's service account.** If it should never delete namespaces, it shouldn't hold that permission. Tier 3 operations that you want truly rare should go through a separate break-glass path with a human's own credentials.
- **Admission policy** (Kyverno or ValidatingAdmissionPolicy). Examples are a `protected=true` label that blocks namespace deletion, and rejecting deletes of PVCs that have no recent backup. These apply even if someone approves.
- **Environment scoping.** Prod gets stricter Tier 1 bounds than staging. Some Tier 1 actions might be Tier 2 in prod at first.
- **Full audit log** of every command, tier, approver, and outcome.

## 4. Why this is at least as safe

- Everything auto-allowed is either read-only or bounded, rate-limited, and reversible.
- Every dangerous action still needs a human, and now with a stronger gate (typed confirmation, second approver, RBAC and admission backstops).
- Today's real protection from approval is close to zero, because people approve without reading. The new design adds layers that don't depend on attention.

The risk is a misclassified command landing in a lower tier than it should. The default-to-highest-tier rule, the blast-radius check, and the RBAC and admission backstops are there to cover that.

## 5. Measure whether it works
- **Prompts per engineer per day.** Target is under 5, and nearly all Tier 2.
- **Time-to-approve for Tier 2 and 3.** Median approvals under 2 seconds suggest rubber-stamping, so alert on it.
- **Tier 2 approval rate.** If a command type is approved 100% of the time over a month, review it for promotion to Tier 1. A human should make that change, never an automatic one.
- **Escalation and denial rates**, and **Undo usage** on Tier 1.

## 6. Rollout
1. **Shadow mode.** Run the classifier against 30 or more days of past Tidewater commands. Check the tier distribution, and read every command that would have been Tier 0 or 1 to find misclassifications.
2. Ship RBAC trimming and admission policies first. They help immediately, whatever happens with the prompts.
3. Enable the new flow in staging, then prod.
4. Review the metrics after two weeks and tune the tier table.

## Questions that would change the design
- Does Tidewater issue raw `kubectl` strings, or can it call structured APIs? Structured calls make the parsing much safer.
- Is there an on-call or approver roster to enforce "second person" against?
- Which namespaces and clusters are prod-critical? That determines the Tier 1 bounds.
- Can Tidewater's service account permissions be changed today, or does that belong to another team?

I can draft the tier table as a policy file, mock up the Slack prompt layouts, or write the classifier next. Tell me which one you want, and point me at the Tidewater code if you want me to work in it.
