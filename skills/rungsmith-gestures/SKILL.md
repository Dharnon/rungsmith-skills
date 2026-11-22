---
name: rungsmith-gestures
description: "A drag jumps, stops outside the target, or commits an unintended value. Define bounded drag, release and cancellation behavior for native controls."
metadata:
  status: draft
  native-verification: pending
---

# Drag & gestures

Define bounded drag, release and cancellation behavior for native controls.

Practice this workflow in a development project: [Resolve drag versus scroll on touch](RECIPES.md).

## Workflow

1. Identify supported pointer and keyboard events in the target component.

2. Define bounds, units, cancellation and commit ownership before implementing.

3. Test leaving the hit area, touch scrolling, lock during interaction and two instances; disclose unsupported capture or momentum.

## Decide what owns a drag on a scrolling view

Inspect the native component's supported events and the enclosing scroll container on the deployed client. Sketch idle, editing, cancelled and committed states. Keep an uncommitted draft local to the view instance. For a horizontal control on a vertical list, verify that a vertical swipe starting on its label can still scroll the list.

Use a simulated host that records emitted intents. Drag outside the control, reverse direction, then release. Repeat with a permission change during the drag. Count intents, inspect their equipment identity and confirm cancellation restores the displayed authoritative value. When reliable release outside the control is unavailable, use a supported native input or explicit Apply action.

Record which parts of the gesture the installed component handles internally and which changes reach an event script. A view custom property can isolate a draft per instance, but script-driven updates still cross the client/Gateway boundary. Test release and cancellation in the launched session before attributing browser pointer-capture behavior to the component.

## Resolve a change arriving during a drag

Choose a policy for external updates before implementing visual smoothing. In a simulated host, start dragging and change the confirmed value from another fixture input. Inspect whether a binding immediately snaps the thumb back, silently overwrites the draft or leaves two conflicting labels. Keep the latest accepted value available for cancellation and decide how a conflict is communicated according to the host contract.

Repeat with a range reduction and then a lost permission while the pointer is down. Recheck validity at commit time through the existing command path. A release must not replay a draft that was valid only at drag start. Compare the same sequence with keyboard adjustment so the two input methods follow the same ownership and validation rules.

## Specify the gesture as state transitions

Define the start surface, permitted direction, point at which the interaction counts as editing, and what ends it. A small movement on a scrollable touch list may be the beginning of a scroll. Determine what the native control handles before adding a script. If the installed component cannot reliably distinguish the two gestures, a separate editing surface may serve the task better.

During editing, keep visual feedback, transient value and host-confirmed value distinguishable. At release, consult the existing command contract for commit and rejection. On cancellation, recover the current authoritative value, which might have changed since the gesture began. Observe the actual native behavior when the pointer leaves the component; browser examples that depend on pointer capture require explicit support.

## Choose a path for fine adjustment

A touch slider that spans a large engineering range may offer fewer usable positions than the requested increment. Compare the usable track length at the deployed size with the count of distinct steps. For a 0–100 range in 0.1 increments there are 1,001 distinct values. A narrow track can still be useful for coarse exploration, while a native numeric input or supported step controls may serve precise entry better.

Build both paths against the same fixture draft and commit contract. Set a value near a bound by touch, refine it by one increment, then cancel. Repeat using the numeric path alone and verify the host receives the same unit and rounded value when committed. If the two controls remain visible simultaneously, keep their draft synchronized without feeding programmatic synchronization back as a second user intent.

Specify the coarse gesture, precise alternative and cancellation route. Include an example value that is difficult to acquire by drag at the deployed width.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| The thumb jumps back during a held drag | Compare latest confirmed value with the local draft and incoming updates. | Resolve the ownership conflict before changing visual easing. |
| Releasing outside occasionally commits twice | Record native release and parent action in a fixture with intent counts. | Choose one supported commit owner and verify cancellation separately. |

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A gesture contract with tested native behavior. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Review this scrubber for release outside the bar, cancellation and keyboard adjustment.
