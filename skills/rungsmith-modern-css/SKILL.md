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

## Perspective constraints

Read the actual native view contract and target-version APIs. Keep process state, command permission and interlocks owned by the host. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A supported CSS change with compatibility and fallback notes. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Can container queries improve these embedded panels? Check the actual client and native layout first.
