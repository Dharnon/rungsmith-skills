---
name: rungsmith-native-ui-quality
description: Design or review native Ignition Perspective interaction, layout and motion for operator-facing HMI screens. Use for focus, menus, tooltips, scrubbers, alarm clarity and generic UI cleanup; distinguish native components from website or module implementations.
metadata:
  status: preview
  native-verification: pending
---

# Native HMI quality pilot

Establish the target Ignition version, project, operator task and implementation surface. Native Perspective views use component contracts, bindings, styles and server-side scripting. Website React code, browser DOM APIs and custom Perspective modules are different surfaces; do not silently substitute one for another.

Practice this workflow in a development project: [Review the route from alarm to equipment detail](RECIPES.md).

## Interaction contract

Before editing a control, identify its input value, output event, local transient state and process state reported by the equipment. Specify what click, drag, keyboard activation, Escape, blur and reopening do where applicable. Verify supported native properties/events against the target version instead of inventing APIs.

Use native semantics when available. Make keyboard focus visible with the project's palette. Keep a tooltip tied to hover/focus and dismiss it when its trigger is activated; selected state is not tooltip state. A modal must restore focus, handle dismissal and preserve instance identity. Do not use global message state that lets one equipment panel modify another.

During dragging, distinguish immediate visual feedback from the committed process value. Inspect supported native slider/scrubber update modes and measure round-trip effects. Do not promise browser-local smoothness from a stream of Gateway scripts. Keep bounds, units, steps, keyboard adjustment and lock conditions coherent. Apply actual enabled/interlock behavior, not just faded styling.

## Translate web guidance

For each proposed pattern, classify it: native property/layout; scoped stylesheet; website-only; custom module; unsupported or unverified. Prefer native Flex/Coordinate/container behavior appropriate to the view contract. Check browser/Workstation support for CSS features on actual deployed clients. Native runtime support is a separate requirement from modern browser availability.

Use project-scoped tokens and styles. Avoid DOM-index selectors and blanket global overrides. For embedded previews, inspect both host and child scroll ownership; eliminate accidental nested scrolling while retaining access to long content, keyboard scrolling and high-contrast preferences. Hiding all scrollbars is not a repair for overflow.

## Industrial craft and anti-slop

Arrange information around the operator's next decision. Show equipment identity, units, freshness/quality and state before decoration. Give alarms consistent priority/state semantics; reserve strong color for meaningful states. Do not use a single accent color for start, stop, alarm and disabled states.

Choose density from the task and viewport. Avoid gratuitous KPI cards, repeated gradients, decorative graphs and fabricated precision. Test long equipment names, empty/history states, translated labels, large values and narrow layouts. A live chart must respond to its data/window controls; label sample data honestly.

Animate a change only when it helps explain continuity or feedback. Prefer small scoped opacity/transform transitions where supported, honor reduced motion, and keep repeated operational actions fast. Verify rapid reversal and interruptions. Do not delay a command or animate alarm significance away to match a web effect. Native morphs that cannot reproduce browser measurement should be documented as approximations.

## Prioritize faults when a screen has several kinds of debt

Start from the operator's next consequential decision. A misleading value, wrong equipment identity or action directed to a different instance deserves investigation before visual inconsistency. Distinguish an unavailable operation from a visually disabled control whose host action still runs. Follow the actual binding or action to establish which problem exists.

For each finding give the smallest reproduction and the resource that owns it. A popup header can belong to the launcher, a reading to the child view and a repeated color to a shared style. Group repairs only when they share an owner. Re-run the operator journey after the smallest fix to see whether downstream symptoms still exist before expanding the change.

## Review the relationship between the overview and the detail

Begin at the overview with a concrete question such as “Which pump needs attention and what evidence supports that?” Follow identity, quality, state and available actions into the detail and back. A view can be individually attractive while the route fails because units change without a label, colors change meaning or the popup opens a different asset after sorting.

Inspect the actual ownership of each failure. A header can be composed by the popup host, a unit supplied through a view param and a quality badge derived by a local transform. Give the implementer the first incorrect value and its owner. Combine findings only when a shared change can fix them without altering other consumers.

## Review the same screen in three operating conditions

Capture normal production, one exceptional piece of equipment and partial data loss at the intended client size. Use realistic asset names and nonuniform values. In normal production, evaluate alignment and scanning across assets. In the exceptional state, identify how quickly the affected equipment and condition can be read. In partial data loss, verify that the interface preserves uncertainty rather than offering a deceptively clean summary.

Record the first decision each picture supports. If a normal screen is covered in equally prominent badges, reduce prominence where the semantic role permits. If an alarmed screen becomes one undifferentiated red block, separate priority, equipment identity and next available action. If uncertainty is visible only in a detail tooltip, bring an accessible cue to the overview. Check the revised three states as a set.

Deliver three annotated observations with the responsible resource, the intended visual emphasis and one existing convention the edit must preserve.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| A polished popup shows a different unit from the overview | Trace the conversion source and both label bindings. | Repair unit/value agreement before revising visual hierarchy. |
| The disabled control still acts from keyboard | Inspect the component's real enabled state and the existing action boundary. | Align the presentation and supported activation behavior; preserve existing authorization. |

## Evidence

Test actual keyboard and pointer behavior, lock/disconnect states, two equipment instances and close/reopen. Measure interaction latency and avoid spawning repeated sessions for visual checks. Report changed resources, target version, observed behavior and remaining limitations. Static validation, screenshots, browser interaction and Designer import are different evidence.

## Sources and experimental scope

This is original Rungsmith guidance informed by the public behavior and design domains of [Vercel UI SDK](https://github.com/vercel-labs/ui), [Modern Web Guidance](https://github.com/GoogleChrome/modern-web-guidance) and [Emil Kowalski's skills](https://github.com/emilkowalski/skills). It is not an exhaustive translation or a claim of upstream endorsement. Consult the requested source at a pinned revision when adapting a specific behavior.

Catalyst is a separate, version-dependent exploration. Check the installed version/modules and current official docs before proposing an integration. Record the specific capability and supported release when Catalyst is relevant to the request.

## Prioritize findings in one operator journey

Walk from an overview row into its equipment detail, inspect a measurement and return to the overview. At each step record the selected equipment, current data quality and next available action. Review with a narrow embedded host and one unavailable reading. A polished detail panel that labels stale data as live takes priority over an inconsistent shadow.

Assign each finding to its actual resource: host layout, child binding, shared style class or interaction handler. Give the developer a reproduction and one observable acceptance condition. For example, reopening the second pump must display that pump's identifier and quality before any reading can be interpreted as current. Indicate the native client used or the fixture still required.
