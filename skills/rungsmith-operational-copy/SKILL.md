---
name: rungsmith-operational-copy
description: "Messages are verbose, vague or inconsistent across equipment views. Make labels, errors and status text specific enough to act on."
metadata:
  status: draft
  native-verification: pending
---

# Operational copy

Make labels, errors and status text specific enough to act on.

## Match each message to evidence

Trace the displayed string to its trigger, translation key and available equipment context. For command feedback, distinguish the user action, the request result and the observed equipment state. Those signals can arrive separately. Choose the most specific wording supported by the signal that actually fires.

| Evidence available | Example operator-facing text |
| --- | --- |
| The host confirms submission of the start request | “Start request sent for P-204.” |
| A valid running indication arrives for that pump | “P-204 running.” |
| The history query succeeds with no matching records | “No events for P-204 in this time range.” |
| The history query fails | “Event history unavailable for P-204.” |

Use the site's names for equipment and actions. Include a recovery action only when the operator can perform it in this state. Preserve the diagnostic detail needed by maintenance. When a shared translation key appears in several views, inspect those contexts before changing it.

Review the message in place with a long equipment name and the longest supported translation available. Check what remains visible when status changes twice in succession. Hand off the original text, replacement and trigger together so a reviewer can verify each claim against the binding.

## Check shared labels in their real hosts

Inspect whether the displayed text comes from a component property, expression, translation lookup or host-supplied view param. If both an overview and a popup use the same key, check that each supplies enough equipment context. Replay a missing or delayed parameter on popup open so a newly selected asset cannot inherit the last asset's success message.

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

Concise messages and a consistent state vocabulary. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Rewrite these command and error messages. Keep the equipment identity and actual failure cause.
