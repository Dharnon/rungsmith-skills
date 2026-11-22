---
name: rungsmith-keyboard-focus
description: "Controls reachable by pointer but difficult to operate without a mouse. A keyboard interaction matrix and supported native fixes."
metadata:
  status: draft
  native-verification: pending
---

# Keyboard & focus

A keyboard interaction matrix and supported native fixes.

Practice this workflow in a development project: [Return from a popup after filtering its opener](RECIPES.md).

## Workflow

1. Map focus order and native component keyboard support for the target version.

2. Check activation, Escape, focus recovery and visible focus as separate behaviors.

3. Exercise the complete flow including disabled controls and repeated popup opening.

## Trace a complete path without a pointer

Choose a real route, such as selecting equipment, opening details, editing a filter and closing the popup. Record the focus target before and after each step in a launched session. Inspect the component configuration and enabled state when focus skips an item. A visible outline, reachable control and successful activation are separate observations.

Repeat after filtering out the trigger row. Check where focus lands when the original opener no longer exists and choose an available logical return target if the platform supports it. Verify backward traversal, Escape while editing and a second open/close cycle. Report the first failing keystroke and resource path.

## Separate focus loss from a missing visual cue

When Tab appears to stop, inspect the next observable activation using a harmless fixture action. If Enter activates the expected control, focus may have moved successfully while its indicator is clipped, obscured or the same color as the background. Inspect the assigned style, parent overflow and selected theme before altering navigation order.

If focus actually skips the control, inspect its native enabled state, rendering conditions and supported keyboard interaction. A decorative label over a native input may obscure its focus outline. Test at the narrowest host width with a validation message showing. Record the focused target, the visible cue and the activation result as three separate observations.

## Build a key-by-key interaction contract

Record the focus target on entry, the key that activates it, the target after activation and what should happen when the action is cancelled. Do this for one complete task including its error path. Focus visibility, actual focus, selection and activation are separate properties. A selected equipment row can remain highlighted while focus moves to a popup.

Treat dynamic changes as part of the route. Validation text can resize the panel, filtering can remove the return target and a disabled submit action can alter traversal. Check the native control's documented keyboard behavior before inventing custom key handlers. Preserve familiar activation behavior and avoid handling the same key in both a parent and its child.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| Enter works but no outline appears | Inspect focus state, outline contrast, parent overflow and overlay layering. | Repair the cue while preserving the functioning activation path. |
| Escape closes both an inner picker and its parent | Trace which supported handlers observe the dismissal. | Assign the intended dismissal owner and verify two successive Escape presses. |

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A keyboard interaction matrix and supported native fixes. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Walk through this equipment popup using only the keyboard. Record every blocked action.
