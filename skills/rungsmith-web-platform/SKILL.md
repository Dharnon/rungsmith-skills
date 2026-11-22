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

## Determine who owns the browser capability

For a request such as copying an equipment ID to the clipboard, first identify the surface: Perspective component, separately hosted preview or installed custom module. Check the target version's supported native action, the client's browser capability and any relevant user-gesture or embedding restrictions. Evidence from a standalone web page applies only to that surface.

Describe the native outcome when the capability is unavailable, such as a selectable identifier that the operator can copy manually. Verify success and fallback in the actual deployment context. Return the resource owner, API evidence, client tested and observable result. A browser compatibility table alone cannot establish that a Perspective view exposes the API.

A Perspective component event script runs on the Gateway even when a click in the browser triggers it. A Python event handler therefore cannot call browser objects such as `navigator.clipboard`. Inspect the documented component action or client integration that would perform the operation. [Scripting in Perspective](https://www.docs.inductiveautomation.com/docs/8.1/ignition-modules/perspective/scripting-in-perspective)

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A capability map and a realistic implementation recommendation. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Assess CSS anchor positioning and the Popover API for this Perspective tooltip. Explain what is actually controllable.
