---
name: rungsmith-prototype
description: "You need to choose density, information hierarchy or an interaction model. Compare different solutions to one operator task before integrating a winner."
metadata:
  status: draft
  native-verification: pending
---

# Prototype alternatives

Compare different solutions to one operator task before integrating a winner.

Practice this workflow in a development project: [Build a native A/B switch for a maintenance task](RECIPES.md).

## Workflow

1. Create isolated development views with the same realistic sample data.

2. Vary a meaningful axis such as density, navigation or progressive disclosure, not just color.

3. Make the relevant controls work in each variant and present trade-offs; integrate only the chosen version.

## Compare two native layouts with the same task

Build isolated development views around one fixture contract with equipment identity, operating state, measurement quality and units. For a density decision, compare an always-visible summary with a selectable overview plus detail view. Feed both the same normal, faulted and missing-data examples. Keep edits and command feedback simulated.

Ask the reviewer to locate the faulted asset and read its last reliable measurement at the target workstation size. Record mistaken selections, unnecessary navigation and clipped qualifiers. Use these observations to choose which layout to integrate. List the host view, reusable child and bindings needed to carry the chosen design into the project.

## Control the variables between design alternatives

Use the same equipment selection, quality transitions and timestamps across variants. An inline history view with cached data can look faster than a popup that starts a fresh query even if the layout itself offers no advantage. For a layout comparison, hold query readiness constant. For a loading-strategy comparison, make readiness the intentional variable and measure it explicitly.

Replay a recovery task as well as a happy path: select the wrong equipment, return to the overview and find the correct asset. Record lost selection, repeated navigation and mistaken interpretation of unavailable values. Choose the variant based on the target operator task. Preserve useful individual findings even when neither complete variant is ready for integration.

## Choose variants that test competing hypotheses

Write the decision before building the comparison. “Inline trends help operators compare pumps” and “separate details preserve room to scan the whole line” are competing hypotheses. Two nearly identical cards with different colors rarely answer that question. Use the same equipment fixture and comparable working interactions. Limit each variant to differences that materially affect the chosen task.

Run an ordinary task and a recovery task. Ask the reviewer to locate an exception, inspect its last reliable value and return to the same point in the overview. Then introduce a wrong selection or missing reading. Record navigation steps, loss of context and mistaken interpretations. Avoid declaring a winner from a visual preference when the measured operator task points elsewhere.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| Reviewers choose different variants on each run | Check fixture parity, task wording, starting state and cached data. | Repeat the comparison with the relevant variable controlled. |
| The selected prototype cannot fit the real host | Compare standalone preview dimensions with the production embedding context. | Repeat the decisive task inside the intended host before integrating. |

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

Working alternatives and a decision table. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Prototype three motor panel layouts using the same values. Keep live tag writes disconnected.
