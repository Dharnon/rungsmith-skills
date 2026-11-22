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

## Measure the milestone the operator experiences

Split a slow faceplate opening into launcher activation, visible shell, first valid reading and usable history tab. Record a cold and a repeated open with the same project revision, equipment and client. A slow history query can coexist with a responsive control tab. Measure their timings independently.

Inspect which embedded views and bindings are active before the user selects history. Check repeated instances for duplicate subscriptions, query executions or script transforms using diagnostics available on the target system. Change one suspected cause in development and repeat under the same conditions. Report the observations and any remaining uncertainty about network or Gateway load.

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A before/after observation and the actual bottleneck. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Find why opening this faceplate is slow. Measure before changing animations.
