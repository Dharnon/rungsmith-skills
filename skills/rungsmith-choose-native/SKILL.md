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

## Compare candidates against a real binding

For equipment selection, write down the input identity, display label, empty selection and output the host consumes. Inspect the installed Dropdown and any registered selector against those requirements in Designer. Duplicate labels, a disabled item or keyboard-only operation can change the choice even if the candidates look identical.

Embed the leading candidate in a small host with two identically named fixture items that have distinct IDs. Select each, reorder the options and inspect the host value. Record the chosen component or view path, any adapter it needs and the requirement that ruled out the runner-up. If neither candidate preserves identity, expose the gap before designing a replacement.

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A component choice with its path, contract and reason. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Pick the right native control for choosing equipment. Compare keyboard support, filtering and instance state.
