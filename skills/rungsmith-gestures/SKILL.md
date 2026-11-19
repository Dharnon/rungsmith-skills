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

## Perspective constraints

Read the actual native view contract and target-version APIs. Keep process state, command permission and interlocks owned by the host. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A gesture contract with tested native behavior. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Review this scrubber for release outside the bar, cancellation and keyboard adjustment.
