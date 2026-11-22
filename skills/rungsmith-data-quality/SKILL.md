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

## Preserve meaning through transforms

Start at the displayed label and trace its binding, transform chain, source timestamp and quality. Locate the first point where a null, invalid quality or conversion failure becomes a plausible number. Keep formatting and unit conversion downstream of the validity check. Use the project's sampling rules when deciding whether a timestamp is stale: an unchanged event-driven value can still be healthy.

Drive a simulated pressure reading through valid zero, bad quality with a retained last value, then valid recovery. Record value, quality cue, timestamp and unit at each step. If retained values are shown, the presentation must make their age and status evident. Switch equipment during recovery and confirm the old reading cannot appear under the new identity.

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A documented state map and bindings that preserve data meaning. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Review sensor readings for stale, bad-quality and disconnected states.
