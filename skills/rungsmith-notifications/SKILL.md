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

## Assign feedback to the request that produced it

Trace the button action, host command handler and result binding or message. Record equipment ID and any request identifier the actual contract provides. If two presses are allowed, determine how a late result is associated with its originating request. When the contract cannot disambiguate concurrent requests, keep the UI from claiming a specific outcome.

Simulate submission, delayed acceptance, failure and a late reply after navigation. Open two embedded faceplates on the same page. Check which instance renders each message and whether both the host and child announce the same event. A timeout describes missing confirmation. Show the authoritative result when it arrives and retain any active alarm in its own surface.

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A feedback lifecycle tied to real outcomes. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Fix duplicate command notifications and keep equipment acknowledgments separate from alarms.
