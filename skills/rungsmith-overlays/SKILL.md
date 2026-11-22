---
name: rungsmith-overlays
description: "Floating panels jump, fail to dismiss or reopen with stale context. A stable overlay contract and observed lifecycle results."
metadata:
  status: draft
  native-verification: pending
---

# Popups & tooltips

A stable overlay contract and observed lifecycle results.

Practice this workflow in a development project: [Open two detail popups on one page](RECIPES.md).

## Workflow

1. Trace the popup host, instance identity, parameters and close owner.

2. Reserve geometry and define hover, focus, activation, dismissal and reopen state.

3. Verify two equipment instances, Escape and focus return where supported.

## Reproduce stale context across popup instances

Trace the launcher's event, popup ID, target view and parameters into the child binding. Determine whether the project intends one reusable detail popup or one popup per equipment item. For a reusable popup, make the equipment identity and displayed channels change together. For independent popups, ensure the close action addresses the instance that initiated it.

Open A, switch to B while A's data is loading, dismiss B, then reopen A. At each step inspect title, displayed value, selected tab and close target. Record which properties should reset and which should persist. Repeat at the smallest supported viewport and verify the close control remains reachable when content overflows.

## Choose a reset policy for each piece of popup state

Classify equipment identity, selected tab, scroll position, unsaved edits and query results separately. An operator may expect a layout preference to persist across openings while an unfinished setpoint draft should remain associated only with its original asset. Inspect whether each value lives on the child view, on its host or in a broader session property.

Reopen the same asset, open a different asset and open two panels for the same asset. Record which values are deliberately restored and which are initialized. If two panels share a value accidentally, trace the storage or message recipient before assigning a new popup ID. A distinct popup ID resolves lifecycle targeting but cannot isolate a shared session property.

## Define dismissal by cause

Map each way the overlay can end: explicit close, Escape where supported, selection, parent navigation and reopening through another launcher. Decide what happens to transient edits and focus for each path. A tooltip, picker and equipment detail popup can have different dismissal contracts even when they share the same visual shell. Inspect the native launch configuration and close owner before changing presentation.

For asynchronous content, capture the asset and context when starting the request. When results arrive, verify they still belong to the visible surface. A stable popup ID can intentionally serve several assets over time. That makes stale responses possible even when there is only one popup on screen. Exercise delayed success and failure after dismissal as separate cases.

## Select the interaction surface by what must remain possible

Use a modal workflow when the operator must finish or dismiss a decision before proceeding in the parent. A modeless detail or dock suits comparing a selected item with its neighbors. Anchored help suits short explanations when keyboard and touch access are supported. A tooltip is a poor home for required input, scrolling history or the only explanation of unavailable equipment.

Compare the candidate surfaces in the actual page layout. Open an equipment detail and ask the reviewer to select an adjacent row. If doing so is essential and the chosen popup blocks it, the issue is the surface contract. If a dock leaves the overview too narrow to compare rows, inspect an explicit compact layout or dedicated detail route. Test close affordance and recovery within each viable surface.

Write one line for each surface considered: parent task while open, focus ownership, space consumed, supported dismissal and the reason it fits or fails.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| Closing popup A also closes popup B | Inspect popup ID choice and the close action's target. | Use identities consistent with the intended coexistence policy. |
| Reopening the same asset unexpectedly restores an old error | Trace error state to child, opener or session storage. | Reset or preserve it at the lifecycle boundary required by the host. |

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A stable overlay contract and observed lifecycle results. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Fix the stuck tooltip without changing selected navigation state.
