---
name: rungsmith-motion-opportunities
description: "The interface feels static but frequent actions must remain fast. Identify the few changes where motion would clarify feedback."
metadata:
  status: draft
  native-verification: pending
---

# Find useful motion

Identify the few changes where motion would clarify feedback.

## Workflow

1. Inspect the operator task and transitions in state or location.

2. Propose motion only where it clarifies cause, continuity or feedback.

3. Also list what must stay immediate, especially alarms and repeated commands; leave implementation for an accepted proposal.

## Perspective constraints

Read the actual native view contract and target-version APIs. Keep process state, command permission and interlocks owned by the host. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A small opportunity list with reasons and exclusions. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Where would motion help this maintenance flow? Also explain what should remain instant.
