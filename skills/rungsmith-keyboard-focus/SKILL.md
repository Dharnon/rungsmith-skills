---
name: rungsmith-keyboard-focus
description: "Controls reachable by pointer but difficult to operate without a mouse. A keyboard interaction matrix and supported native fixes."
metadata:
  status: draft
  native-verification: pending
---

# Keyboard & focus

A keyboard interaction matrix and supported native fixes.

## Workflow

1. Map focus order and native component keyboard support for the target version.

2. Check activation, Escape, focus recovery and visible focus as separate behaviors.

3. Exercise the complete flow including disabled controls and repeated popup opening.

## Perspective constraints

Read the actual native view contract and target-version APIs. Keep process state, command permission and interlocks owned by the host. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A keyboard interaction matrix and supported native fixes. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Walk through this equipment popup using only the keyboard. Record every blocked action.
