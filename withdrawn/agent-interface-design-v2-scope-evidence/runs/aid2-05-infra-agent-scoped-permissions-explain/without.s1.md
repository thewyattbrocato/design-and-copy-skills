# Tidewater permission redesign

## Core idea
Approval fatigue comes from asking too often. The fix is to ask less often, and make each prompt you do send look and feel different depending on the danger. Today every command gets the same dialog, so a namespace delete looks like `kubectl logs`.

The design has four parts:
1. A deterministic risk classifier.
2. Tiered handling: auto-run, light confirm, hard confirm.
3. Server-side limits that don't depend on anyone reading anything.
4. Metrics to check that people are actually reading.

## 1. Structured actions and a deterministic classifier
- **Don't classify shell strings.** Have the agent emit structured actions (`verb`, `resource`, `name`, `namespace`, `cluster`, flags) and build the `kubectl` call yourself. This avoids pipes, `;`, `$(...)` and alias tricks sneaking past a parser.
- **Use a plain rules table, not an LLM, for the tier decision.** The model can write the justification text, but it must not decide the risk level. A prompt-injected log line shouldn't be able to talk its way into auto-approval.
- **Default to the highest tier for anything unrecognized** (fail closed).
- The inputs are verb, resource kind, environment (prod/staging/dev), blast radius (how many objects the command touches), and reversibility.

## 2. Tiers

| Tier | Examples | Behavior |
|---|---|---|
| **0: Auto-run, logged** | `get`, `describe`, `logs`, `top`, `events` on non-secret resources in any env | No prompt. Posted to an audit thread. |
| **1: Auto-run in non-prod, one-tap in prod** | Delete a single pod owned by a controller, `rollout restart`, scale within ±50% or a set bound | Non-prod: runs, with a rate cap (e.g. 10/hour/cluster). Prod: compact prompt. |
| **2: Explicit review** | Scale to zero, `patch`/`apply`, cordon/drain, delete of non-pod resources, PVC or ConfigMap changes | Full prompt (see below). Requires a dry-run diff. |
| **3: Hard gate** | Delete namespace, CRD, PV, node; anything with `--all`, `-A`, or label selectors matching more than N objects; RBAC changes | Typed confirmation, a second approver in prod, and a cool-off delay. In staging the typed confirmation is still required. |
| **Never** | `exec`, `cp`, `port-forward`, `proxy`, `debug`, `get secret`, `auth can-i --as` | Not available to the agent. Humans do these with their own credentials. |

**Watch these "reads":**
- `get secret -o yaml`, and logs that contain tokens, can leak credentials.
- `exec` is arbitrary code execution, not a read.
- Both are carved out above.

## 3. What the prompts look like
Prompts for Tier 2 and 3 are short and tailored to the action, not a copy of the command.

- **First line:** the effect in plain language, with the environment prominent.
  `PROD · payments-cluster-2 · Scale checkout-api 6 → 0 (all traffic will drop)`
- **Concrete impact:** what is affected and what it affects. For example: "Deletes namespace `staging-foo`: 14 deployments, 3 PVCs (2 GiB data), 2 ingresses."
- **Why the agent wants this:** one sentence, linked to the triggering alert or ticket.
- **Dry-run or diff** for mutations.
- **Reversibility:** "Recoverable: rollout undo" or "Irreversible: data is deleted."
- **Friction scales with severity:**
  - Tier 3 requires typing the target name (like GitHub's repo-delete dialog). It can't be approved by a reflex tap.
  - The Approve button is on a different color and layout for Tier 3, with no one-tap option.
- **Approval is bound to the exact action.** Hash the structured action and the resolved target set. If the agent's command changes, or the set of objects it resolves to changes, the approval is void.
- **Approvals expire** (e.g. 10 minutes). The approver's identity is recorded, and approvers can't approve their own agent session in prod.

## 4. Safety that doesn't depend on human attention
This is what makes the design "at least as safe as today". Today the human is the only control, and it has already failed.
- **Scope the agent's service account with RBAC.** Give it no delete on namespaces, CRDs, PVs or nodes at all. Tier 3 actions run through a separate, short-lived identity issued only after approval.
- **Use admission policies** (Kyverno or OPA Gatekeeper) to block deletion of namespaces carrying a `protected=true` label, and to cap replica changes.
- **Set budgets per session:** a limit on mutations per hour and on total objects touched. Hitting the limit escalates to a human.
- **Fail closed.** If the classifier, policy service or Slack is unavailable, nothing runs.

## 5. Check that people actually read
- **Prompt volume target:** about 3–5 human prompts per engineer per day, mostly Tier 2 or 3.
- **Track time-to-approve** per tier. Approvals under about 2 seconds on Tier 2 or 3 are a red flag.
- **Track the approval rate.** A rate near 100% over a long period suggests rubber-stamping, or that the tier boundary is wrong.
- **Review every Tier 1 auto-run weekly** to tune boundaries. Any incident should lead to a rule change.
- **Optionally, send occasional canary prompts** in staging: a harmless but deliberately wrong-looking action that should be rejected. Use it to measure attentiveness, not to punish people.

## Rollout
1. **Replay the last 30–60 days of Tidewater commands** through the classifier offline. Check the tier distribution. You should see roughly 80%+ in Tier 0 and 1. Also check that the staging namespace delete lands in Tier 3.
2. **Shadow mode for 1–2 weeks:** keep the current approvals, but log what the new tier would have done. Look at disagreements.
3. **Ship the RBAC and admission guardrails first.** They protect you even if the classifier has bugs.
4. **Enable Tier 0, then Tier 1 non-prod, then the new prompts.** Keep a kill switch that puts everything back to approve-all.

## Open questions that would change the details
- What's in the 60+ daily commands? The replay will answer this, and it decides where the Tier 1/2 line goes.
- Do you have a second approver available in prod around the clock? If not, Tier 3 needs an on-call fallback.
- Can Tidewater use separate identities per tier, or does it run as one service account today? That's the biggest implementation cost.

I can draft the rules table and the structured-action schema, or the Slack message layouts for each tier, if you want either.
