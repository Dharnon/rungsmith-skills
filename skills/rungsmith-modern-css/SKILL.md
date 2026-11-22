---
name: rungsmith-modern-css
description: "A layout needs modern sizing, container queries or better overflow behavior. Apply newer CSS where it improves the view and the deployed client supports it."
metadata:
  status: draft
  native-verification: pending
---

# Modern CSS

Apply newer CSS where it improves the view and the deployed client supports it.

## Workflow

1. Look up the specific capability in Modern Web Guidance and authoritative compatibility data.

2. Classify whether the native view exposes the necessary layout or owned selector.

3. Use a scoped enhancement with a usable fallback; verify the actual Workstation or browser rather than assuming latest Chrome.

## Diagnose the boundary before writing a selector

For a clipped embedded faceplate, trace available width from the host container through the Embedded View to the child root. Inspect the parent's position settings and the embedded component's useDefaultViewWidth and useDefaultViewHeight. A child stylesheet cannot recover width already consumed by a fixed host layout.

For a container-query enhancement, identify the project-owned wrapper that establishes the query container and the descendants it controls. Keep the default arrangement usable on the deployed client with the enhancement disabled. Compare one standalone view and two embedded instances with different widths on the same page. Record the tested client build, breakpoint behavior and fallback.

In Designer, assign the project Style Class by name. For a top-level class named panel, its CSS selector is `.psc-panel`. On Ignition 8.1 the optional Advanced Stylesheet is available from 8.1.22. Check the installed version and whether the resource is enabled before choosing where the CSS belongs. [Perspective Style Classes](https://www.docs.inductiveautomation.com/docs/8.1/ignition-modules/perspective/styles/style-classes)

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A supported CSS change with compatibility and fallback notes. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Can container queries improve these embedded panels? Check the actual client and native layout first.
