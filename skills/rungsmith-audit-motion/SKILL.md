---
name: rungsmith-audit-motion
description: "Several screens have inconsistent or unreliable transitions. Audit motion across views and produce small repair tasks."
metadata:
  status: draft
  native-verification: pending
---

# Plan motion repairs

Audit motion across views and produce small repair tasks.

## Workflow

1. Inventory transitions by trigger, surface and frequency.

2. Reproduce the important failures and rank operator impact before visual polish.

3. Write independent repair tasks with resources, expected behavior and verification steps.

## Perspective constraints

Read the actual native view contract and target-version APIs. Keep process state, command permission and interlocks owned by the host. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A prioritized plan that another agent can execute. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Audit motion in these views and give me independent fixes ordered by operator impact.

## Research references

Original Rungsmith adaptation; upstream implementations are not bundled.

- https://github.com/emilkowalski/skills/tree/main/skills/improve-animations
