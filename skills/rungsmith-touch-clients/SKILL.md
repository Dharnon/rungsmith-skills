---
name: rungsmith-touch-clients
description: "A desktop view behaves badly on a tablet, phone or touch HMI. Make native views usable on touch screens without sticky hover or clipped content."
metadata:
  status: draft
  native-verification: pending
---

# Touch clients

Make native views usable on touch screens without sticky hover or clipped content.

Practice this workflow in a development project: [Keep Apply reachable with the software keyboard open](RECIPES.md).

## Workflow

1. Identify the actual client viewport, browser and input method.

2. Check target size, hover media queries, scrolling ownership, safe areas and on-screen keyboard.

3. Test on the intended device; keep critical actions available without hover and document any device-only gaps.

## Test at the deployed viewport with the keyboard open

Trace the layout from page docks through the parent container to the embedded control. Capture the effective viewport with an on-screen keyboard open. For a docked filter above a scrollable table, determine which surface scrolls and whether the focused field, Apply and dismissal remain reachable without trapping the page.

Try tapping two adjacent equipment rows, scrolling from a control label and dismissing a popup using touch alone. Check that the first tap selects the intended target instead of merely exposing a hover affordance. Repeat after rotating the actual device when rotation is supported. Record client type, orientation and any gesture that could only be evaluated on hardware.

## Handle accidental activation while scrolling a list

Test the actual route an operator uses on a tablet. Start a vertical scroll over a row label, then over a trailing action. Check which interaction selects a row, opens a popup or simply scrolls. A successful tap on a stationary control says little about what occurs when the finger starts moving and crosses a neighboring target.

Prefer a distinct supported activation target when selection and navigation compete with scrolling. Keep contextual actions discoverable without a hover-only reveal. Repeat with the popup dismissed and the list restored to its prior scroll position. Record the device, orientation and first action after dismissal; these expose stale hover and misplaced focus that a desktop pointer simulation can miss.

## Design the whole touch route, including recovery

Inspect the physical target device, effective viewport, orientation and input method. A touch HMI may have ample nominal pixels while a dock, browser chrome or software keyboard substantially reduces usable space. Walk the task from scrolling to selection to editing and dismissal. Measure the reachable area in the actual context instead of assuming desktop hover and a smaller viewport approximate touch behavior.

Check neighboring targets together. A large touch surface can overlap a secondary action or make scrolling from the row difficult. Keep primary selection, scrolling and explicit commands distinguishable. Offer visible routes to functions previously exposed by hover. After dismissing a popup, verify the list returns to a recognizable position and the next tap acts on the equipment under the finger.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| The first tap reveals an action and the second activates it | Inspect whether availability depends on hover. | Provide a discoverable touch interaction and verify one deliberate activation. |
| The popup footer disappears only while typing | Measure the effective viewport and actual scrolling region with the keyboard open. | Restore access to the field, validation and dismissal at that height. |

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

Touch-specific fixes and the tested client dimensions. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Adapt this equipment panel for touch. Check keyboard overlap and access without hover.
