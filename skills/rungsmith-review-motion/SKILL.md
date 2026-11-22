---
name: rungsmith-review-motion
description: "A transition is implemented and needs a targeted review. Check an existing transition against its purpose and actual behavior."
metadata:
  status: draft
  native-verification: pending
---

# Review motion

Check an existing transition against its purpose and actual behavior.

## Workflow

1. Read the changed stylesheet, bindings and event flow.

2. Check frequency, interruption, reduced motion and whether animation masks slow state.

3. Report before, proposed after and reason; separate native observations from static risks.

## Review a single transition against a replay

Start with one changed resource and one trigger. Trace the binding that applies its class and any action responsible for cleanup. Review entry and exit independently: a popup can open smoothly yet leave an invisible layer after rapid dismissal. Check the effect at normal speed before slowing a recording to inspect individual frames.

Exercise opening, reversal and a second activation while data arrives. Observe whether a value update restarts the motion and whether interaction begins before the display settles. Record the client, trigger sequence and end state for each finding. A stylesheet duration establishes intent; use session observations for claims about actual latency.

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A focused review with actionable findings. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Review the morph in this diff. Flag delays and stale final states before changing code.
