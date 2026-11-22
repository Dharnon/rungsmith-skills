---
name: rungsmith-anti-slop
description: "A screen looks generated, over-separated or full of ornamental cards. Remove decoration and structure that do not help the operator task."
metadata:
  status: draft
  native-verification: pending
---

# Remove generic UI

Remove decoration and structure that do not help the operator task.

Practice this workflow in a development project: [Remove one box without losing equipment grouping](RECIPES.md).

## Decide what earns its space

Read the view and one comparable project screen. Name the decision an operator makes here, then trace the visible cues used to make it. For each candidate removal, identify what the border, heading, color or chart currently communicates. Keep a repeated enclosure when it binds an equipment identity to its own controls. A second enclosure around a lone value usually adds little.

For example, consider two adjacent pump faceplates. A border around every pressure reading competes with the boundary between pumps. Try removing the inner borders and aligning the readings with their units. Keep each pump identifier beside its controls and retain the project's alarm and quality indicators. Trace a displayed trend to its data source before deciding whether it carries information.

Compare the original and revised view at the intended client width with both pumps normal, then with one in alarm and the other showing unavailable data. Can the operator identify the affected pump, distinguish the two conditions and associate each control with the right equipment? Restore or revise any grouping whose removal makes that harder. Report the changed resource and the decision each edit supports.

## Check the actual cost of removing a wrapper

Inspect the selected container in the Designer tree before deleting it. It may own a visibility binding, style class or event handler. Also inspect any bindings that refer to the container by component path. View parameters belong to the view. If its grouping is meaningful but its border adds noise, change the scoped style first. Compare sibling instances of the shared view before making the change project-wide.

## Recover information hierarchy in a dense overview

Read the overview at its deployed size with realistic data. Mark the first place an operator can identify the equipment, determine whether intervention is needed and find the corresponding detail action. A repeated title may be redundant on a standalone panel yet essential when that panel appears several times in a Flex Repeater. Inspect both contexts before removing the label from the shared child.

For a wall of visually identical cards, group by the decision the operator makes. Align comparable measurements and units across rows. Move stable metadata into a quieter position while retaining the identity next to the value. Review the normal screen and then a single fault among normal neighbors. Check whether the operator can locate the exception and still read its context.

## Edit the reading order before editing the palette

Take a screenshot of a populated overview at normal operator distance. Hide the decorative backgrounds in a development copy. If the screen becomes unreadable, identify which job the removed surfaces were doing: separating machines, grouping a measurement with its unit, or locating commands. Restore a cue for that specific relationship. Empty space or aligned labels may work for values; adjacent command groups may need a stronger boundary.

Build hierarchy from an actual sequence. For a pump comparison the repeated sequence might be identifier, running state, pressure, quality, detail action. Align those items in the same order across pumps. Preserve intentional departures such as a persistent alarm marker. A card is worth retaining when it makes the association between a control and its equipment unmistakable at a glance.

## Design the comparison column

Put three pressure values in the actual overview: 9.8, 10.0 and 101.2 kPa. Alternate the first two in a development fixture. Watch whether the units or neighboring status icons move. Align quantities with the same meaning on a common edge; reserve space for the sign and quality treatment. If the deployed font supports tabular numerals, compare them at actual station size. Decide decimal precision from the measurement contract.

Try placing the unit in the column heading for a single-unit table. Then inspect a mixed-unit row, compact breakpoint and detail popup. Repeat the unit beside the value wherever the heading no longer supplies reliable context. This is a more useful density improvement than reducing every padding value: it removes repeated text precisely where the relationship remains obvious.

Deliver an annotated before/after of one populated column, including zero, a negative value if valid, the longest value and unavailable quality.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| Everything still looks equally important after removing borders | Trace the scan from asset identity to measurement and abnormal condition. | Adjust order, alignment and weight before removing another grouping cue. |
| The simplified view is ambiguous only in a repeater | Compare the standalone child with adjacent instances showing the same value. | Restore an instance-local identity cue at the point where confusion starts. |

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A smaller interface with a clear operational hierarchy. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Simplify this faceplate. Remove unnecessary cards and separators while keeping state and commands clear.
