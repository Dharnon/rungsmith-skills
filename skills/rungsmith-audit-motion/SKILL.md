---
name: rungsmith-audit-motion
description: "Several screens have inconsistent or unreliable transitions. Audit motion across views and produce small repair tasks."
metadata:
  status: draft
  native-verification: pending
---

# Plan motion repairs

Audit motion across views and produce small repair tasks.

Practice this workflow in a development project: [Find a shared transition defect](RECIPES.md).

## Workflow

1. Inventory transitions by trigger, surface and frequency.

2. Reproduce the important failures and rank operator impact before visual polish.

3. Write independent repair tasks with resources, expected behavior and verification steps.

## Sample a complete operator route

Follow a route such as overview to equipment popup to trend tab and back. Log the resource that owns each transition, its trigger and how often the trigger fires. Separate an opening transition from one that restarts on every tag update. A shared style class may explain identical symptoms across several views.

Rank by consequence. A hidden acknowledgment control during a fade merits attention before inconsistent easing on a maintenance panel. Group failures by shared cause and record one representative reproduction plus another consumer to regression-test. Produce one repair task per cause with its scope, expected final state and native replay.

## Decide how widely a defect propagates

Inventory by owning resource as well as by screen. The same transition can appear in ten faceplates through one named style, or in one faceplate through several independent bindings. Inspect one affected consumer, another consumer of the same class and one unaffected neighbor. Look for an inline override, conditional class or a different mounting path before proposing a project-wide edit.

Write each repair around a repeatable event such as switching assets while a trend loads. Name the visible consequence, the suspected owner and the second consumer to check after the repair. Keep a cosmetic timing disagreement below findings that obscure a live state change, delay a repeated action or leave focus inside a dismissed surface.

## Sample by trigger and ownership

Choose a route used repeatedly during a shift, one exceptional path and one automatic refresh. For each transition record what starts it, what resource owns it and which operator decision is pending. A single shared class can affect dozens of views, while two similar animations can have unrelated causes. Sample both a consumer that fails and a consumer that behaves correctly.

Separate prevalence from impact. A rarely opened blocking dialog can matter more than a ubiquitous decorative fade. Document whether the defect hides equipment identity, delays a next action, causes input to miss, or merely feels inconsistent. Estimate prevalence from inspected consumers. Avoid multiplying one shared cause into one finding per screen.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| An effect appears across unrelated views | Identify the shared class and check one unaffected consumer. | Scope one repair to the owner and test its consumers. |
| Only one client exhibits the interruption | Compare client build, reduced-motion settings and input path. | Record the client-specific replay before changing global timing. |

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A prioritized plan that another agent can execute. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Audit motion in these views and give me independent fixes ordered by operator impact.
