---
name: rungsmith-choreograph
description: "A panel and its contents animate separately or several parts compete for attention. Make related changes read as one event without queuing visual delays."
metadata:
  status: draft
  native-verification: pending
---

# Coordinate motion

Make related changes read as one event without queuing visual delays.

Practice this workflow in a development project: [Coordinate a detail header and a late-loading trend](RECIPES.md).

## Workflow

1. Identify the lead change and what must remain still.

2. Keep related changes together; remove nested entrances and delays on frequently used controls.

3. Test rapid reversal and preserve access to visible controls during the transition.

## Coordinate a popup shell and its contents

Trace the equipment selection, native popup opening, child view mounting and arrival of bindings as separate events. Assign the shell to the opening event. Let the tag binding update its own value or quality indicator without replaying the entrance. Keep the title and close control available while a trend loads.

Open A, close it before the entrance completes and immediately open B. Observe the popup identifier, equipment label and final visibility. If an old completion handler hides B, fix ownership of that cleanup before tuning easing. Replay with reduced motion and with slow fixture data.

## Handle exits when the next asset is already selected

Trace what screen readers, keyboard users and pointer users can interact with during the overlap. If the outgoing detail remains visible, decide whether it can still receive focus or respond to a command. An outgoing panel labelled A beside a newly selected B creates a period in which ownership is ambiguous. Prefer a single stable shell with a clear pending state when the native host cannot keep this overlap unambiguous.

Make the equipment identifier and data change as a coherent unit. Let decorative content arrive later if useful. Test switching A to B to A before either history result arrives. After each switch inspect the visible asset, current data and reachable controls. A visually smooth sequence still fails if a late result can populate the wrong shell.

## Choose the relationship between surfaces

Use simultaneous change when two fields describe one fact: the asset identifier and its quality cue should agree on every visible frame. Use a staged change when the later element genuinely depends on a result, such as a history plot awaiting data. Use a persistent anchor when the operator must compare before and after, such as leaving the equipment header visible during a tab switch. Make each timing choice answer to a data or navigation relationship.

Inspect the intermediate state as carefully as the final one. During a crossfade, both panels can be legible and interactive for a moment. A native popup may have a separate focus lifecycle from its trigger. Try a single stable shell first when overlapping equipment panels would make identity ambiguous. Check the reduced-motion version with the same sequence of state updates.

## Describe a timeline with observable milestones

Sketch four lanes: launcher, stable shell, equipment fields and history. Mark trigger accepted, shell visible, first valid reading and history resolved. Put each cue on its owning lane. Shell visibility can follow navigation. The reading must follow a valid sample for the selected asset. The chart follows the matching history response. A fixed animation delay cannot establish either data dependency.

Replay the same sketch with two launch orders. In a warm open, history may be available before the shell finishes entering. In a cold open, it may arrive much later. Both paths should converge on the same layout without briefly showing a previous asset. If the chart is already available, display it directly instead of forcing a staged loading performance. Use waits only for observed data states.

Write a milestone timeline for cold, warm and interrupted opens. Mark the first moment the operator can dismiss or switch equipment in each.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| Opening a panel makes existing controls shift twice | Observe shell geometry before and after data arrival. | Reserve the final content region or defer just the dependent content. |
| Reversing midway briefly exposes both equipment identities | Trace the outgoing content, input ownership and new selection. | Keep one stable identity boundary and permit only the intended surface to act. |

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A motion relationship map and a supported transition change. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Simplify the motor panel transition. Keep status and commands immediately readable.
