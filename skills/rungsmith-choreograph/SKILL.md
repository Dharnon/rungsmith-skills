---
name: rungsmith-choreograph
description: "A panel and its contents animate separately or several parts compete for attention. Make related changes read as one event without queuing visual delays."
metadata:
  status: draft
  native-verification: pending
---

# Coordinate motion

Make related changes read as one event without queuing visual delays.

## Workflow

1. Identify the lead change and what must remain still.

2. Keep related changes together; remove nested entrances and delays on frequently used controls.

3. Test rapid reversal and preserve access to visible controls during the transition.

## Perspective constraints

Read the actual native view contract and target-version APIs. Keep process state, command permission and interlocks owned by the host. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A motion relationship map and a supported transition change. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Simplify the motor panel transition. Keep status and commands immediately readable.

## Research references

Original Rungsmith adaptation; upstream implementations are not bundled.

- https://github.com/emilkowalski/skills/tree/main/skills/choreograph
