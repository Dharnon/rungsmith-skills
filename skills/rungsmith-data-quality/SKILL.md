---
name: rungsmith-data-quality
description: "Missing or stale readings look like valid live values. A documented state map and bindings that preserve data meaning."
metadata:
  status: draft
  native-verification: pending
---

# Data quality & states

A documented state map and bindings that preserve data meaning.

## Workflow

1. Trace value, quality, timestamp and connection sources.

2. Represent missing, stale, disconnected and uncertain states without coercing them to zero.

3. Test reconnection, changing quality and large values with units.

## Perspective constraints

Read the actual native view contract and target-version APIs. Keep process state, command permission and interlocks owned by the host. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A documented state map and bindings that preserve data meaning. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Review sensor readings for stale, bad-quality and disconnected states.

## Research references

Original Rungsmith adaptation; upstream implementations are not bundled.
