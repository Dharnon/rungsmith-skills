---
name: rungsmith-notifications
description: "Commands have no feedback, duplicate messages or claim success too early. Represent pending, success and failure without confusing a notification with an alarm."
metadata:
  status: draft
  native-verification: pending
---

# Command feedback

Represent pending, success and failure without confusing a notification with an alarm.

## Workflow

1. Trace the command request and actual acknowledgment or failure source.

2. Use one feedback owner per instance and distinguish requested, accepted and confirmed state.

3. Test duplicate actions, timeouts, dismissal and reconnect; retain persistent alarm information in the alarm system.

## Perspective constraints

Read the actual native view contract and target-version APIs. Keep process state, command permission and interlocks owned by the host. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A feedback lifecycle tied to real outcomes. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Fix duplicate command notifications and keep equipment acknowledgments separate from alarms.
