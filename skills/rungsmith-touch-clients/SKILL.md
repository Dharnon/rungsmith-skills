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

## Test at the deployed viewport with the keyboard open

Trace the layout from page docks through the parent container to the embedded control. Capture the effective viewport with an on-screen keyboard open. For a docked filter above a scrollable table, determine which surface scrolls and whether the focused field, Apply and dismissal remain reachable without trapping the page.

Try tapping two adjacent equipment rows, scrolling from a control label and dismissing a popup using touch alone. Check that the first tap selects the intended target instead of merely exposing a hover affordance. Repeat after rotating the actual device when rotation is supported. Record client type, orientation and any gesture that could only be evaluated on hardware.

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

Touch-specific fixes and the tested client dimensions. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Adapt this equipment panel for touch. Check keyboard overlap and access without hover.
