---
name: rungsmith-review-motion
description: "A transition is implemented and needs a targeted review. Check an existing transition against its purpose and actual behavior."
metadata:
  status: draft
  native-verification: pending
---

# Review motion

Check an existing transition against its purpose and actual behavior.

Practice this workflow in a development project: [Review a transition under interruption](RECIPES.md).

## Workflow

1. Read the changed stylesheet, bindings and event flow.

2. Check frequency, interruption, reduced motion and whether animation masks slow state.

3. Report before, proposed after and reason; separate native observations from static risks.

## Review a single transition against a replay

Start with one changed resource and one trigger. Trace the binding that applies its class and any action responsible for cleanup. Review entry and exit independently: a popup can open smoothly yet leave an invisible layer after rapid dismissal. Check the effect at normal speed before slowing a recording to inspect individual frames.

Exercise opening, reversal and a second activation while data arrives. Observe whether a value update restarts the motion and whether interaction begins before the display settles. Record the client, trigger sequence and end state for each finding. A stylesheet duration establishes intent; use session observations for claims about actual latency.

## Separate a style finding from a state defect

Replay the transition at normal speed and note the first incorrect observation. A panel that displays the previous asset for one frame may have correct easing and an incorrect order of state updates. Disable the visual transition in development and repeat. If the wrong identity remains, route the repair to the host or binding that selects the asset.

For a genuine motion defect, include which edge fails: entry, exit, reversal or repeated update. Describe what should remain stationary, which cue should lead and when controls become usable. Judge the behavior in the surrounding operator task. A close affordance that cannot be reached during a brief transition can matter more than a longer decorative effect in an idle area.

## Write findings a developer can reproduce

Begin with a trigger, initial state and interaction sequence. “Slow transition” leaves the next developer guessing. “Open B while A's history is pending, dismiss B before its shell settles, then Tab” identifies when to observe the fault. Name the visible consequence and state whether it was observed in a native session or inferred from a resource.

Choose the smallest repair consistent with the cause. Remove a redundant entrance, correct an incorrect trigger, narrow a shared rule or repair native cleanup before adjusting a curve. Give a counterexample that must continue working. A change that fixes reversal for a popup but removes the only visible focus cue in the underlying view is incomplete.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| A transition masks a stale equipment label | Disable the effect and inspect identity at the same milestone. | Raise a state ownership finding if the stale label persists. |
| A timing complaint occurs only under continuous updates | Compare a frozen fixture with the normal update rate. | Trace repeated triggers before prescribing a different duration. |

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A focused review with actionable findings. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Review the morph in this diff. Flag delays and stale final states before changing code.
