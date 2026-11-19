---
name: rungsmith-web-platform
description: "A web API is proposed for a native view or embedded preview. Separate modern browser capabilities from what native Perspective can control."
metadata:
  status: draft
  native-verification: pending
---

# Web platform feasibility

Separate modern browser capabilities from what native Perspective can control.

## Workflow

1. Search the exact capability and read its current guidance.

2. Map it to native events, scoped CSS, website code or a custom module.

3. Return supported implementation choices with lifecycle, security and browser limits; do not inject arbitrary JavaScript into native views.

## Perspective constraints

Read the actual native view contract and target-version APIs. Keep process state, command permission and interlocks owned by the host. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A capability map and a realistic implementation recommendation. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Assess CSS anchor positioning and the Popover API for this Perspective tooltip. Explain what is actually controllable.
