---
name: rungsmith-remove-motion
description: "Frequent navigation or refreshing values keep animating. Subtract animation that slows work or competes with process information."
metadata:
  status: draft
  native-verification: pending
---

# Remove excess motion

Subtract animation that slows work or competes with process information.

## Workflow

1. Inspect visibility and cleanup code that depends on the animation.

2. Remove or shorten unnecessary motion without adding a different effect.

3. Verify final styles, close behavior and reduced motion; retain documented operational feedback.

## Untangle presentation from popup cleanup

Find the style class, visibility binding and event or timer that actually closes the popup. Record the final state first. If removing a fade leaves an invisible overlay intercepting input, repair the native close path so cleanup completes even when animation duration is zero.

Replay frequent refreshes with stationary process values and then one genuine state change. Confirm the refresh no longer retriggers decoration and the state change still reads clearly. Close and reopen rapidly, then tab through the area previously covered. Verify it returns to the expected interaction state with reduced motion enabled.

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

Less motion with no invisible or stranded content. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Remove decoration from this alarm screen. Preserve meaningful acknowledgment feedback.
