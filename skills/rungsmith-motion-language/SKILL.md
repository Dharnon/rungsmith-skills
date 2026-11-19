---
name: rungsmith-motion-language
description: "You can describe the effect but not its name or intended behavior. Name an interaction precisely so the implementation request is clear."
metadata:
  status: draft
  native-verification: pending
---

# Motion vocabulary

Name an interaction precisely so the implementation request is clear.

## Workflow

1. Translate the description into terms such as crossfade, morph, origin-aware transition or direct manipulation.

2. Explain the distinction using one operational example.

3. Identify whether the effect is native CSS, a supported approximation or a custom-module requirement.

## Perspective constraints

Read the actual native view contract and target-version APIs. Keep process state, command permission and interlocks owned by the host. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A precise term and an implementation boundary. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

What should we call the transition between Home and Process? Explain the native options.
