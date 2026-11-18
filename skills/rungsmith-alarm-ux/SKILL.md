---
name: rungsmith-alarm-ux
description: "Priority, acknowledgment and history are hard to distinguish. An alarm state matrix and specific UX changes with verification gaps."
metadata:
  status: draft
  native-verification: pending
---

# Alarm UX

An alarm state matrix and specific UX changes with verification gaps.

## Workflow

1. Read alarm data fields and existing acknowledgment flow.

2. Separate priority, active/cleared and acknowledged state using text and color.

3. Verify empty results, filters, history and authorized acknowledgment feedback.

## Perspective constraints

Read the actual native view contract and target-version APIs. Keep process state, command permission and interlocks owned by the host. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

An alarm state matrix and specific UX changes with verification gaps. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Review this alarm screen for active, cleared, unacknowledged and empty states.

## Research references

Original Rungsmith adaptation; upstream implementations are not bundled.
