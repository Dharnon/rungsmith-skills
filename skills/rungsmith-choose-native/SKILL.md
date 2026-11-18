---
name: rungsmith-choose-native
description: "You need a select, chart, table or notification and are unsure what to reuse. Choose a native control or registered resource before building a new one."
metadata:
  status: draft
  native-verification: pending
---

# Choose a component

Choose a native control or registered resource before building a new one.

## Workflow

1. Inspect existing project resources and their actual contracts.

2. Match the task to an available native component; compare access, dependencies and interaction support.

3. Recommend one choice and its trade-offs; do not replace an installed solution just for stylistic preference.

## Perspective constraints

Read the actual native view contract and target-version APIs. Keep process state, command permission and interlocks owned by the host. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A component choice with its path, contract and reason. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Pick the right native control for choosing equipment. Compare keyboard support, filtering and instance state.

## Research references

Original Rungsmith adaptation; upstream implementations are not bundled.

- https://github.com/emilkowalski/skills/tree/main/skills/pick-ui-library
