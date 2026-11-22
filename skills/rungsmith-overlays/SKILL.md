---
name: rungsmith-overlays
description: "Floating panels jump, fail to dismiss or reopen with stale context. A stable overlay contract and observed lifecycle results."
metadata:
  status: draft
  native-verification: pending
---

# Popups & tooltips

A stable overlay contract and observed lifecycle results.

## Workflow

1. Trace the popup host, instance identity, parameters and close owner.

2. Reserve geometry and define hover, focus, activation, dismissal and reopen state.

3. Verify two equipment instances, Escape and focus return where supported.

## Reproduce stale context across popup instances

Trace the launcher's event, popup ID, target view and parameters into the child binding. Determine whether the project intends one reusable detail popup or one popup per equipment item. For a reusable popup, make the equipment identity and displayed channels change together. For independent popups, ensure the close action addresses the instance that initiated it.

Open A, switch to B while A's data is loading, dismiss B, then reopen A. At each step inspect title, displayed value, selected tab and close target. Record which properties should reset and which should persist. Repeat at the smallest supported viewport and verify the close control remains reachable when content overflows.

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A stable overlay contract and observed lifecycle results. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Fix the stuck tooltip without changing selected navigation state.
