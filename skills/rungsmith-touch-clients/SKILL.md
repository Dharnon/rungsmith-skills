---
name: rungsmith-touch-clients
description: "A desktop view behaves badly on a tablet, phone or touch HMI. Make native views usable on touch screens without sticky hover or clipped content."
metadata:
  status: draft
  native-verification: pending
---

# Touch clients

Make native views usable on touch screens without sticky hover or clipped content.

## Workflow

1. Identify the actual client viewport, browser and input method.

2. Check target size, hover media queries, scrolling ownership, safe areas and on-screen keyboard.

3. Test on the intended device; keep critical actions available without hover and document any device-only gaps.

## Perspective constraints

Read the actual native view contract and target-version APIs. Keep process state, command permission and interlocks owned by the host. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

Touch-specific fixes and the tested client dimensions. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Adapt this equipment panel for touch. Check keyboard overlap and access without hover.

## Research references

Original Rungsmith adaptation; upstream implementations are not bundled.

- https://github.com/emilkowalski/skills/tree/main/skills/animate-expo
- https://github.com/emilkowalski/skills/tree/main/skills/mobile-native
