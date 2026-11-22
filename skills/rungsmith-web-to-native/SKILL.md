---
name: rungsmith-web-to-native
description: "A web interaction needs an honest native implementation plan. A feasibility map, native resource plan and explicit limits."
metadata:
  status: draft
  native-verification: pending
---

# Web pattern to Perspective

A feasibility map, native resource plan and explicit limits.

Practice this workflow in a development project: [Port an equipment sheet with a long maintenance note](RECIPES.md).

## Workflow

1. Identify the behavior separately from the React component and visual decoration.

2. Classify each part as native properties/events, scoped CSS, website-only, custom module or unverified.

3. Prototype the supported contract and verify it on the target client; disclose approximations.

## Extract the interaction before selecting components

For a web equipment drawer, inventory opening trigger, asset identity, displayed readings, keyboard dismissal, scroll ownership and return focus. Map the shell to a native popup or dock based on whether the operator must continue working in the parent view. Carry identity through the declared view params and inspect the source of each displayed reading.

Prototype with two fixture assets, a long maintenance note and a missing reading. Switch assets mid-load and verify the heading, values and dismiss action agree. Record any reference effect that depends on browser geometry or lifecycle hooks unavailable on the chosen host. Give the implementer a view path, binding plan and observable acceptance cases.

## Decide how a port behaves when the reference assumes local state

Trace when the reference control changes its visual state and when it persists a result. A web prototype may show a local selection instantly, then save asynchronously. In Perspective, binding that draft directly to a command target can turn every intermediate interaction into a request. Separate the native component's displayed draft, the host's intent handler and the authoritative confirmation using the project's established contract.

Test delayed confirmation, dismissal without applying and a host update from another instance. Compare what the operator can still do while waiting, including reopening the same equipment. Describe any loss of immediacy or different dismissal semantics explicitly so the native implementation is evaluated against an agreed behavior rather than a screenshot of the web reference.

## Port the task in vertical slices

Choose one end-to-end behavior from the reference, such as selecting a pump and seeing its detail. Map the selected identifier, launch action, child params, displayed measurement and dismissal. Build that slice in a development host before adding visual treatments. Repeat for keyboard use, responsive layout and delayed data. Each slice should leave a native resource or a documented capability gap.

Classify visual matches according to their dependency. A scoped color or spacing change may translate directly. A shared-element morph based on DOM measurement may require a different native solution. Preserve the operational purpose through stable identity and clear selection when geometry cannot be reproduced. Report which differences affect the user's task and which affect appearance alone.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| The reference interaction depends on DOM measurement | Identify which operator relationship the measurement supports. | Prototype that relationship with native layout and disclose the visual difference. |
| The port emits writes while the reference only previews | Trace input changes to draft state and intent emission. | Restore the intended commit boundary using a simulated consumer before integrating. |

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A feasibility map, native resource plan and explicit limits. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Map this UI SDK pattern to native Perspective. Explain supported behavior and what needs a module.
