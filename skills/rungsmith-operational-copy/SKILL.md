---
name: rungsmith-operational-copy
description: "Messages are verbose, vague or inconsistent across equipment views. Make labels, errors and status text specific enough to act on."
metadata:
  status: draft
  native-verification: pending
---

# Operational copy

Make labels, errors and status text specific enough to act on.

## Workflow

1. Map each message to its audience, trigger and next action.

2. Replace generic success claims with the actual confirmed state; preserve equipment identity, units and error context.

3. Check translations, long labels and empty states; do not hide uncertainty or invent recovery actions.

## Perspective constraints

Read the actual native view contract and target-version APIs. Keep process state, command permission and interlocks owned by the host. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

Concise messages and a consistent state vocabulary. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Rewrite these command and error messages. Keep the equipment identity and actual failure cause.

## Research references

Original Rungsmith adaptation; upstream implementations are not bundled.

- https://github.com/miqdadbadjuber/anti-slop
