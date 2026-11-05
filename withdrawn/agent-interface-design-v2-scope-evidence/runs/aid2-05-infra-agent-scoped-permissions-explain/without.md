# Tidewater permission redesign

Prompts are only useful if each one carries information. Today a stuck-pod restart and a namespace delete look the same, so people stop reading. The fix is to remove most prompts and make the remaining ones look and behave differently from each other.

## 1. Enforce limits in the credentials, not only the prompts

The approval dialog shouldn't be the only thing standing between Tidewater and `delete namespace`.

- Give Tidewater separate Kubernetes identities per tier, using scoped service accounts or short-lived tokens. The read-only identity can't mutate anything.
- The routine-fix identity can only patch or delete pods, patch `deployments/scale`, and create rollout restarts, and only in namespaces you allowlist.
- No Tidewater identity can delete namespaces, PVCs, CRDs or nodes, or read Secrets. Those requests go to a human, who runs them with their own credentials.

The staging incident would then have failed at the API server even if someone had tapped Approve.

## 2. Classify actions deterministically

- **Use structured actions, not shell strings.** Tidewater should emit `{verb, resource, namespace, selector, args}`. Don't classify strings like `kubectl ... && ...`, because chaining and quoting make them easy to misread.
- **Resolve the real blast radius before classifying.** Run a server-side dry-run or a selector query to find out how many objects are affected. `delete pod -l app=x` might match 1 pod or 400.
- **Use an allowlist, with no LLM in the decision.** Anything that doesn't match a known rule is Tier 3 or denied. The model can propose actions but can't set their risk level.

## 3. Tiers

| Tier | Examples | Behavior |
|---|---|---|
| **0: Auto** | `get`, `describe`, `logs`, `events`, `top` on non-Secret resources in allowlisted namespaces | No prompt. Logged. |
| **1: Auto with notice** | Staging only: delete one pod owned by a Deployment with >1 ready replica; `rollout restart`; scale within a bounded range (e.g. ±50% of the current count, never to 0) | No prompt. Posts a thread message saying what ran, with an undo hint. Capped at N per hour, after which it drops to Tier 2. |
| **2: One-tap approve** | The same actions in prod; anything touching more than N pods; StatefulSets or pods with PVCs; scale to 0 in staging | A compact card with the resolved blast radius. The approver can't be the requester for prod. |
| **3: Hard confirm** | Scale to 0 in prod, `exec`, deleting anything cluster-scoped or stateful, and anything unclassified | The approver types the target name (e.g. the namespace). Prod also needs a second approver. The card looks visibly different. |
| **Deny** | Namespace, PVC, CRD or node deletion; Secret reads; RBAC changes | Tidewater refuses and tells the user to do it by hand. |

Reads and routine staging fixes are most of the 60+ daily prompts, so this should cut the volume sharply. This is only as safe as today if the Tier 0 and 1 rules are narrow and the identities in section 1 are enforced.

## 4. What a prompt shows

- **Environment first:** a banner such as `PROD · payments-api`.
- **Plain-language effect:** "Will delete 3 of 3 running pods in `checkout`. Service will be down until they reschedule." Don't show the raw command as the main content, though it can sit in an expandable section.
- **Resolved blast radius:** the object count, whether the objects are stateful, and whether the action is reversible.
- **Why Tidewater wants to do it:** one line, linked to the alert or ticket.
- **Binding:** the approval is tied to a hash of the exact structured action and expires in about 10 minutes. If the action changes, a new approval is required.
- **Different controls per tier:** Tier 2 has a plain Approve button. Tier 3 has no one-tap button at all, only the typed confirmation.

## 5. Guarding against rubber-stamping

- Flag approvals of Tier 2 or 3 actions that take under about 2 seconds, and review them.
- Track the approval rate per approver and per action type. A rate near 100% on a type means the tier is wrong. Either automate it or make it harder.
- Keep prompts rare enough to matter. A target of fewer than 5 per engineer per day is reasonable.
- Alert in a separate channel on every Tier 3 approval and every denied request.

## 6. Rollout

1. **Shadow mode:** replay the last 30 to 60 days of Tidewater commands through the classifier. Check the tier distribution and look for anything auto-allowed that shouldn't be.
2. **Tighten the credentials** (section 1), which is the biggest safety gain and needs no UX change.
3. **Turn on Tier 0, then Tier 1 in staging.** Wait a couple of weeks before expanding to prod.
4. **Ship the new Tier 2 and 3 cards** and start tracking approval latency.

## Open questions

- Do you have prod and staging in the same clusters or separate ones? Separate clusters make the scoping in section 1 much easier.
- Is there an existing audit log of past Tidewater commands I could use for the shadow-mode replay?
- Are there on-call or ownership rules, such as "only the service owner can approve prod"? Those would slot into Tier 2.

I can turn this into a concrete rules file (YAML tier definitions and a classifier skeleton) once I know where Tidewater's code lives. The working directory is empty, so I haven't seen it.
