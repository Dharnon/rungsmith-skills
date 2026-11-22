---
name: rungsmith-prototype
description: "You need to choose density, information hierarchy or an interaction model. Compare different solutions to one operator task before integrating a winner."
metadata:
  status: draft
  native-verification: pending
---

# Prototype alternatives

Compare different solutions to one operator task before integrating a winner.

## Workflow

1. Create isolated development views with the same realistic sample data.

2. Vary a meaningful axis such as density, navigation or progressive disclosure, not just color.

3. Make the relevant controls work in each variant and present trade-offs; integrate only the chosen version.

## Compare two native layouts with the same task

Build isolated development views around one fixture contract with equipment identity, operating state, measurement quality and units. For a density decision, compare an always-visible summary with a selectable overview plus detail view. Feed both the same normal, faulted and missing-data examples. Keep edits and command feedback simulated.

Ask the reviewer to locate the faulted asset and read its last reliable measurement at the target workstation size. Record mistaken selections, unnecessary navigation and clipped qualifiers. Use these observations to choose which layout to integrate. List the host view, reusable child and bindings needed to carry the chosen design into the project.

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

Working alternatives and a decision table. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Prototype three motor panel layouts using the same values. Keep live tag writes disconnected.
