---
name: rungsmith-notifications
description: "Commands have no feedback, duplicate messages or claim success too early. Represent pending, success and failure without confusing a notification with an alarm."
metadata:
  status: draft
  native-verification: pending
---

# Command feedback

Represent pending, success and failure without confusing a notification with an alarm.

Practice this workflow in a development project: [Handle a late response after navigation](RECIPES.md).

## Workflow

1. Trace the command request and actual acknowledgment or failure source.

2. Use one feedback owner per instance and distinguish requested, accepted and confirmed state.

3. Test duplicate actions, timeouts, dismissal and reconnect; retain persistent alarm information in the alarm system.

## Assign feedback to the request that produced it

Trace the button action, host command handler and result binding or message. Record equipment ID and any request identifier the actual contract provides. If two presses are allowed, determine how a late result is associated with its originating request. When the contract cannot disambiguate concurrent requests, keep the UI from claiming a specific outcome.

Simulate submission, delayed acceptance, failure and a late reply after navigation. Open two embedded faceplates on the same page. Check which instance renders each message and whether both the host and child announce the same event. A timeout describes missing confirmation. Show the authoritative result when it arrives and retain any active alarm in its own surface.

## Define what survives dismissal and reconnect

Decide what a temporary message owns. Dismissal can remove the message from the page while an equipment request is still pending. Inspect where the durable request state lives and how a reopened panel can rediscover its outcome. If the host cannot recover a result after a disconnect, describe the outcome as unknown until an authoritative signal resolves it.

Test one deliberate resubmission with fixture targets. Distinguish a duplicate notification for one request from two real submissions with similar text. Grouping by label alone can conceal the second request. Use the actual correlation evidence when available and keep persistent alarm conditions visible through the project's alarm surfaces independently of temporary feedback.

## Design the lifecycle of a feedback message

Identify what created the message, what event may update it and what makes it obsolete. In a request-driven faceplate these events can be submission, acceptance and observed equipment change. Use the signals the host actually exposes. When only submission is known, do not manufacture a confirmation. Give uncertainty a visible end state if confirmation is delayed or unavailable.

Choose scope deliberately. A transient panel message belongs to an instance. A notification that should survive navigation needs an existing owner with the required lifetime. A process alarm has its own lifecycle. For simultaneous requests, inspect the correlation evidence before coalescing messages. Similar wording or the same equipment ID may still describe independent requests.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| A late success appears under the next asset | Compare request identity, selected asset and message recipient at delivery. | Associate feedback with its originating request or show uncertainty. |
| A single action creates two notices | Count actual submissions separately from notification producers. | Consolidate feedback ownership only after establishing how many requests occurred. |

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A feedback lifecycle tied to real outcomes. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Fix duplicate command notifications and keep equipment acknowledgments separate from alarms.
