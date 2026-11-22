---
name: rungsmith-remove-motion
description: "Frequent navigation or refreshing values keep animating. Subtract animation that slows work or competes with process information."
metadata:
  status: draft
  native-verification: pending
---

# Remove excess motion

Subtract animation that slows work or competes with process information.

Practice this workflow in a development project: [Remove an entrance without stranding a popup](RECIPES.md).

## Workflow

1. Inspect visibility and cleanup code that depends on the animation.

2. Remove or shorten unnecessary motion without adding a different effect.

3. Verify final styles, close behavior and reduced motion; retain documented operational feedback.

## Untangle presentation from popup cleanup

Find the style class, visibility binding and event or timer that actually closes the popup. Record the final state first. If removing a fade leaves an invisible overlay intercepting input, repair the native close path so cleanup completes even when animation duration is zero.

Replay frequent refreshes with stationary process values and then one genuine state change. Confirm the refresh no longer retriggers decoration and the state change still reads clearly. Close and reopen rapidly, then tab through the area previously covered. Verify it returns to the expected interaction state with reduced motion enabled.

## Decide what replaces the information an effect carried

Before deleting a pulse, fade or moving indicator, name the information it conveys at its start and end. If a flashing border is the only cue that a value is pending, removing it can leave an apparently confirmed value. Introduce the project's persistent pending label or another supported state cue before removing the redundant movement.

Trace completion dependencies separately. Check whether a callback, timer or visibility binding also clears the draft, releases input or resets selection. Exercise the interaction with zero visual duration and an intentionally delayed host response. The final state should follow the actual operation and remain readable after the motion is gone.

## Remove the right layer of the effect

Locate the resource that creates motion and the resource that performs the underlying action. A stylesheet transition, timed visibility change and native close operation can all contribute to a single exit. Remove the presentation layer in a fixture and observe which state transitions still occur. Preserve meaningful pending or selected cues when a decorative effect was their only visible representation.

Check for indirect dependencies before deleting a duration or timer. Another event may rely on the same timing to restore focus, clear a local draft or dispose of an embedded view. Move necessary cleanup to the native lifecycle supported by the project. Verify immediate dismissal and a delayed host response independently so changes to appearance do not alter command semantics.

## Distinguish removal, reduction and retention

Inventory three effects on a development route: repeated value-entry fade, panel reveal and a pending indicator. Remove a repeated fade when it hides current readings. Reduce a reveal if the spatial relationship helps but the delay interferes with fast navigation. Retain the pending signal when it is the only evidence that the fixture request is unresolved, or replace it with an equally clear static state.

For each choice identify the mechanism that still performs necessary work. Closing must still close, selection must still be visible and pending must still resolve on actual confirmation. Remove unused classes or timers only after identifying their consumers. Check at least one consumer that intentionally retains the shared effect. This prevents a local simplification from silently changing the whole equipment family.

Example handoff: removed refresh fade on the value label; shortened the detail reveal pending client review; retained request status until acknowledgment. Include one successful reversal and a failed-request replay.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| A zero-duration exit leaves a transparent panel | Trace cleanup ownership and any timer-dependent removal. | Use the supported close lifecycle and verify the underlying input target. |
| Removing a pulse makes pending indistinguishable from complete | Inspect what persistent text or state cue remains. | Restore a static pending indicator tied to the host signal. |

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

Less motion with no invisible or stranded content. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Remove decoration from this alarm screen. Preserve meaningful acknowledgment feedback.
