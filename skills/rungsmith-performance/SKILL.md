---
name: rungsmith-performance
description: "Slow loading, janky interactions or high session load. A before/after observation and the actual bottleneck."
metadata:
  status: draft
  native-verification: pending
---

# Native performance

A before/after observation and the actual bottleneck.

## Workflow

1. Reproduce with one client and record input-to-feedback timing.

2. Inspect bindings, script frequency, layout churn and heavy hidden views before adjusting CSS.

3. Apply the smallest supported change and repeat the same measurement.

## Perspective constraints

Read the actual native view contract and target-version APIs. Keep process state, command permission and interlocks owned by the host. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A before/after observation and the actual bottleneck. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Find why opening this faceplate is slow. Measure before changing animations.
