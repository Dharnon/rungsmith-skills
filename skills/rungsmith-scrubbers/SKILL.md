---
name: rungsmith-scrubbers
description: "Dragging pauses, bounds conflict or lock only changes appearance. A consistent value contract and latency observations in the native client."
metadata:
  status: draft
  native-verification: pending
---

# Scrubbers & setpoints

A consistent value contract and latency observations in the native client.

## Workflow

1. Identify value ownership, units, step, bounds and commit event.

2. Inspect supported native update modes and round trips; distinguish visual feedback from process writes.

3. Test pointer capture where available, keyboard steps, cancellation and actual interlock behavior.

## Separate the draft, emitted intent and confirmed setpoint

Inspect the slider's supported update mode, numeric input range, engineering unit and host binding direction. Determine who rounds a draft and what should happen when a value falls between steps or the configured bounds change mid-edit. Use a fixture host that records emitted values and can delay confirmation.

For a fractional increment, edit once with the keyboard and once by dragging near the upper bound. Compare the displayed draft, emitted request and host-confirmed value in the same units. Cancel mid-drag, change the lock state and repeat with a second instance. On rejection restore or identify the authoritative setpoint. Record how many intents each edit produced.

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A consistent value contract and latency observations in the native client. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Diagnose this setpoint scrubber under fast dragging. Preserve units, limits and lock behavior.
