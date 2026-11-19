---
name: rungsmith-web-to-native
description: "A web interaction needs an honest native implementation plan. A feasibility map, native resource plan and explicit limits."
metadata:
  status: draft
  native-verification: pending
---

# Web pattern to Perspective

A feasibility map, native resource plan and explicit limits.

## Workflow

1. Identify the behavior separately from the React component and visual decoration.

2. Classify each part as native properties/events, scoped CSS, website-only, custom module or unverified.

3. Prototype the supported contract and verify it on the target client; disclose approximations.

## Perspective constraints

Read the actual native view contract and target-version APIs. Keep process state, command permission and interlocks owned by the host. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A feasibility map, native resource plan and explicit limits. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Map this UI SDK pattern to native Perspective. Explain supported behavior and what needs a module.
