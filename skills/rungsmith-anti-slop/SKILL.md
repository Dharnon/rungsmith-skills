---
name: rungsmith-anti-slop
description: "A screen looks generated, over-separated or full of ornamental cards. Remove decoration and structure that do not help the operator task."
metadata:
  status: draft
  native-verification: pending
---

# Remove generic UI

Remove decoration and structure that do not help the operator task.

## Decide what earns its space

Read the view and one comparable project screen. Name the decision an operator makes here, then trace the visible cues used to make it. For each candidate removal, identify what the border, heading, color or chart currently communicates. Keep a repeated enclosure when it binds an equipment identity to its own controls. A second enclosure around a lone value usually adds little.

For example, consider two adjacent pump faceplates. A border around every pressure reading competes with the boundary between pumps. Try removing the inner borders and aligning the readings with their units. Keep each pump identifier beside its controls and retain the project's alarm and quality indicators. Trace a displayed trend to its data source before deciding whether it carries information.

Compare the original and revised view at the intended client width with both pumps normal, then with one in alarm and the other showing unavailable data. Can the operator identify the affected pump, distinguish the two conditions and associate each control with the right equipment? Restore or revise any grouping whose removal makes that harder. Report the changed resource and the decision each edit supports.

## Check the actual cost of removing a wrapper

Inspect the selected container in the Designer tree before deleting it. It may own a visibility binding, style class or event handler. Also inspect any bindings that refer to the container by component path. View parameters belong to the view. If its grouping is meaningful but its border adds noise, change the scoped style first. Compare sibling instances of the shared view before making the change project-wide.

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A smaller interface with a clear operational hierarchy. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Simplify this faceplate. Remove unnecessary cards and separators while keeping state and commands clear.
