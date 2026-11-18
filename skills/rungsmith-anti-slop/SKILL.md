---
name: rungsmith-anti-slop
description: "A screen looks generated, over-separated or full of ornamental cards. Remove decoration and structure that do not help the operator task."
metadata:
  status: draft
  native-verification: pending
---

# Remove generic UI

Remove decoration and structure that do not help the operator task.

## Workflow

1. Read existing project design decisions and identify the actual operator decision.

2. Flag repeated containers, redundant headings, fabricated charts and accent colors without semantic purpose.

3. Simplify the affected surface while preserving branding, critical alarms and working controls; explain each removal.

## Perspective constraints

Read the actual native view contract and target-version APIs. Keep process state, command permission and interlocks owned by the host. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A smaller interface with a clear operational hierarchy. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Simplify this faceplate. Remove unnecessary cards and separators while keeping state and commands clear.

## Research references

Original Rungsmith adaptation; upstream implementations are not bundled.

- https://github.com/miqdadbadjuber/anti-slop/tree/main/skills/antislop-ui
