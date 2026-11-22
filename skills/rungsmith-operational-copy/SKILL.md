---
name: rungsmith-operational-copy
description: "Messages are verbose, vague or inconsistent across equipment views. Make labels, errors and status text specific enough to act on."
metadata:
  status: draft
  native-verification: pending
---

# Operational copy

Make labels, errors and status text specific enough to act on.

Practice this workflow in a development project: [Write messages for states the host can distinguish](RECIPES.md).

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

## Handle precision, units and uncertain causes

Read each value together with its equipment identity, unit and source precision. A format change that adds decimals can imply measurement accuracy the source never supplied. Select wording and numeric formatting from the project's engineering conventions. When a value is unavailable, check whether the unit still clarifies the expected quantity or leaves an ambiguous fragment beside a placeholder.

For a rejected command, distinguish an explicit reason supplied by the host from an inference based on a disabled button. Present a permitted next action only when the current state supports it. Test the final message in its smallest real container using the project's longest relevant translation. Make sure wrapping preserves which asset, action and outcome belong together.

## Build a vocabulary from observed signals

Trace each sentence to the event that authorizes it. “Request submitted”, “accepted” and “running” describe different observations. For a screen that cannot distinguish the first two, choose wording supported by the weaker observation. For errors, distinguish an explicit reason returned by the host from a hypothesis inferred from adjacent indicators. Preserve useful diagnostic detail for maintenance without making an unsupported claim to the operator.

Read the sentence in context. A compact row may already identify the equipment and engineering unit, while a global notification must name them. Inspect the translation key's other callers before removing context. Test long translated messages with the actual popup width and with a state change occurring while the text wraps.

## Make time phrases verifiable

A label such as “updated just now” is ambiguous when the query returned an old sample. Decide what event the phrase refers to and trace the timestamp that drives it. A maintenance detail may need an absolute date and zone for correlation; the overview may benefit from a compact age cue. Both should describe the same event when they share wording.

Use a sample recorded just before midnight and display it shortly after midnight in the deployed locale. Inspect the translated day, date order and unit. Repeat with an unavailable timestamp. “Last sample unavailable” communicates a different fact from “no recent samples”. When space is tight, retain the critical qualifier near the number and move explanation to an accessible detail surface.

Example copy pair: overview “Last sample 12 min ago”; detail “Sampled 21:48, plant local time”. Populate from the same fixture instant and include the date when crossing a day boundary.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| “Saved” appears on a request that later fails | Identify which observable signal triggers the success string. | Use submission wording until confirmation exists. |
| The same translated message is clear in a row but vague in a popup | Inspect equipment context supplied by each host. | Separate keys or include the missing context according to the actual callers. |

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

Concise messages and a consistent state vocabulary. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Rewrite these command and error messages. Keep the equipment identity and actual failure cause.
