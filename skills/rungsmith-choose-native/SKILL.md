---
name: rungsmith-choose-native
description: "You need a select, chart, table or notification and are unsure what to reuse. Choose a native control or registered resource before building a new one."
metadata:
  status: draft
  native-verification: pending
---

# Choose a component

Choose a native control or registered resource before building a new one.

Practice this workflow in a development project: [Select by identity after filtering](RECIPES.md).

## Workflow

1. Inspect existing project resources and their actual contracts.

2. Match the task to an available native component; compare access, dependencies and interaction support.

3. Recommend one choice and its trade-offs; do not replace an installed solution just for stylistic preference.

## Compare candidates against a real binding

For equipment selection, write down the input identity, display label, empty selection and output the host consumes. Inspect the installed Dropdown and any registered selector against those requirements in Designer. Duplicate labels, a disabled item or keyboard-only operation can change the choice even if the candidates look identical.

Embed the leading candidate in a small host with two identically named fixture items that have distinct IDs. Select each, reorder the options and inspect the host value. Record the chosen component or view path, any adapter it needs and the requirement that ruled out the runner-up. If neither candidate preserves identity, expose the gap before designing a replacement.

## Account for the cost of ownership

Evaluate a reusable view in the context in which it will live. A selector that works as a standalone page can become expensive when embedded once per equipment row. Inspect the candidate's dependencies, query bindings, initialization scripts and supported parameter directions. Determine whether the host needs continuous updates or only a committed selection. Verify the installed component exposes that distinction.

Compare the smallest viable adaptations. A host-side mapping from an equipment ID to a label is usually easier to own than a replacement selection control with its own focus and dismissal logic. If the mapping loses disabled state or identity, describe that gap explicitly. Leave the project with a choice it can validate using its own data and client.

## Evaluate the consumer contract before the component catalog

Write the host's smallest meaningful example. What value will be supplied, what can change after mount, what output does the host consume, and what signals an empty or invalid selection? Use this example against a native component, then against an installed reusable view. Include disabled/read-only behavior and the input methods actually used at the station.

Estimate maintenance cost from concrete resources: extra bindings, scripts to adapt data shapes, duplicated focus behavior, additional style dependencies and repeated queries. A larger registered control can be a better fit when it already owns a difficult lifecycle. A simple native component can be preferable when the adapter would otherwise recreate a second source of selection truth.

## Decide between a table and repeated equipment views

Use a table when the primary task is comparing like fields across many records, sorting them and retaining a stable record identity. Consider a repeated equipment view when each item needs a richer local layout or independently owned interaction. Describe one real row before choosing: record ID, displayed fields, actions, quality and refresh frequency. Count subscriptions and embedded views for the expected population.

Make the decision with a fixture containing duplicate display names and one selected record outside the initial visible area. Sort, refresh and return from detail. In the repeated design, observe the cost of mounting the normal number of instances. In the table design, verify whether the target component exposes the required per-row behavior. Capture the first requirement either candidate cannot meet with its documented interface.

Decision example: choose the table for comparing 40 pressure readings; retain a separate detail faceplate for editing one selected asset. Verify identity survives a sort before wiring the launcher.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| An existing selector looks right but loses the selected item | Compare identity before and after option reorder, including duplicates. | Require stable IDs in the adapter or select a component whose contract preserves them. |
| A reusable view expands scope unexpectedly | Inventory scripts, styles and data subscriptions required per instance. | Compare total consumer cost with a native control using the same acceptance case. |

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A component choice with its path, contract and reason. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Pick the right native control for choosing equipment. Compare keyboard support, filtering and instance state.
