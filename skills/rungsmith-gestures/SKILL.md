---
name: rungsmith-gestures
description: "A drag jumps, stops outside the target, or commits an unintended value. Define bounded drag, release and cancellation behavior for native controls."
metadata:
  status: draft
  native-verification: pending
---

# Drag & gestures

Define bounded drag, release and cancellation behavior for native controls.

## Workflow

1. Identify supported pointer and keyboard events in the target component.

2. Define bounds, units, cancellation and commit ownership before implementing.

3. Test leaving the hit area, touch scrolling, lock during interaction and two instances; disclose unsupported capture or momentum.

## Decide what owns a drag on a scrolling view

Inspect the native component's supported events and the enclosing scroll container on the deployed client. Sketch idle, editing, cancelled and committed states. Keep an uncommitted draft local to the view instance. For a horizontal control on a vertical list, verify that a vertical swipe starting on its label can still scroll the list.

Use a simulated host that records emitted intents. Drag outside the control, reverse direction, then release. Repeat with a permission change during the drag. Count intents, inspect their equipment identity and confirm cancellation restores the displayed authoritative value. When reliable release outside the control is unavailable, use a supported native input or explicit Apply action.

Record which parts of the gesture the installed component handles internally and which changes reach an event script. A view custom property can isolate a draft per instance, but script-driven updates still cross the client/Gateway boundary. Test release and cancellation in the launched session before attributing browser pointer-capture behavior to the component.

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A gesture contract with tested native behavior. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Review this scrubber for release outside the bar, cancellation and keyboard adjustment.
