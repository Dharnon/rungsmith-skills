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

## Trace a complete path without a pointer

Choose a real route, such as selecting equipment, opening details, editing a filter and closing the popup. Record the focus target before and after each step in a launched session. Inspect the component configuration and enabled state when focus skips an item. A visible outline, reachable control and successful activation are separate observations.

Repeat after filtering out the trigger row. Check where focus lands when the original opener no longer exists and choose an available logical return target if the platform supports it. Verify backward traversal, Escape while editing and a second open/close cycle. Report the first failing keystroke and resource path.

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A keyboard interaction matrix and supported native fixes. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Walk through this equipment popup using only the keyboard. Record every blocked action.
