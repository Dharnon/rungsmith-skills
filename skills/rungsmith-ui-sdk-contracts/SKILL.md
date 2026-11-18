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

## Perspective constraints

Read the actual native view contract and target-version APIs. Keep process state, command permission and interlocks owned by the host. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A behavior mapping and native acceptance tests. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Map UI SDK selection and popup behaviors to this native equipment picker.

## Research references

Original Rungsmith adaptation; upstream implementations are not bundled.

- https://github.com/vercel-labs/ui/tree/main/packages/core/skills/ui-sdk
