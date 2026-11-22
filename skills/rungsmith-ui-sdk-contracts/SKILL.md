---
name: rungsmith-ui-sdk-contracts
description: "A UI SDK interaction needs an equivalent in a native component. Translate UI SDK behavior into native inputs, events and state."
metadata:
  status: draft
  native-verification: pending
---

# UI SDK behavior contracts

Translate UI SDK behavior into native inputs, events and state.

## Workflow

1. Read the installed or upstream component documentation for selection, focus, popup and dismissal behavior.

2. Map each behavior to declared native parameters, supported events and per-instance state.

3. Test keyboard, Escape, reopen and propagation independently; mark browser-only behavior and never claim React adapters run in view JSON.

## Translate a selector contract one behavior at a time

Use the requested SDK version to extract selection identity, controlled value, open state, focus movement, dismissal and public change notification. For each, locate a declared Perspective parameter, supported native interaction or host handler. Document where the native component already owns the behavior so that a second handler does not emit a duplicate change.

In a fixture host, select between two options with the same label, cancel an uncommitted choice and reopen after the host changes the value. Record visible selection and emitted identity separately. If the reference relies on DOM focus management unavailable to the native view, specify the supported keyboard behavior and the remaining gap.

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A behavior mapping and native acceptance tests. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Map UI SDK selection and popup behaviors to this native equipment picker.
