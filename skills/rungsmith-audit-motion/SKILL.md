---
name: rungsmith-audit-motion
description: "Several screens have inconsistent or unreliable transitions. Audit motion across views and produce small repair tasks."
metadata:
  status: draft
  native-verification: pending
---

# Plan motion repairs

Audit motion across views and produce small repair tasks.

## Workflow

1. Inventory transitions by trigger, surface and frequency.

2. Reproduce the important failures and rank operator impact before visual polish.

3. Write independent repair tasks with resources, expected behavior and verification steps.

## Sample a complete operator route

Follow a route such as overview to equipment popup to trend tab and back. Log the resource that owns each transition, its trigger and how often the trigger fires. Separate an opening transition from one that restarts on every tag update. A shared style class may explain identical symptoms across several views.

Rank by consequence. A hidden acknowledgment control during a fade merits attention before inconsistent easing on a maintenance panel. Group failures by shared cause and record one representative reproduction plus another consumer to regression-test. Produce one repair task per cause with its scope, expected final state and native replay.

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A prioritized plan that another agent can execute. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Audit motion in these views and give me independent fixes ordered by operator impact.
