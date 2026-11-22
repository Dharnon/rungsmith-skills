---
name: rungsmith-perspective-motion
description: Design or repair native Perspective transitions, hover feedback and drag responsiveness. Use for janky morphs, excessive motion, delayed feedback and interruption behavior; do not substitute arbitrary client JavaScript for native components.
metadata:
  status: preview
  native-verification: pending
---

# Motion for operational interfaces

Identify what changed and what motion helps the operator understand. Keep frequent commands fast and alarm significance immediate. Remove decorative movement that competes with process values or hides delayed data.

Inspect native event frequency, bindings, script execution and layout work before adjusting easing. Distinguish Gateway latency, client rendering and animation duration. A CSS transition cannot repair an event backlog. Avoid sleeps and artificial delays in command handlers.

Use scoped opacity/transform transitions where supported and appropriate. Keep final layout stable before showing overlays. Avoid animating large layout dimensions or expensive blur over continually updating tables without measuring the target client. Honor prefers-reduced-motion in the stylesheet; preserve state information without animation.

Design rapid reversal and interruption. Repeated navigation must end in the last requested state, without stacked timers or stale callbacks. Close/reopen should start from correct current state. Keep transient animation state isolated per instance.

For a morph requiring DOM measurement or browser physics unavailable to native Perspective, explain the limitation and implement a supported approximation only when it fits the requested scope. Do not present approximate timing as exact parity. A custom module is a separate implementation choice.

Measure drag feedback, input-to-visible response and session/CPU behavior using the real native client. Test repeated navigation, active data updates, narrow layout and reduced motion. Report observed behavior and tested environments, not a generic 60fps promise.

Practice this workflow in a development project: [Give a filter button local press feedback](RECIPES.md).

## Diagnose a faceplate that flashes on data updates

Trace the class or style binding back to the event that changes it. Separate opening the native view from changes in process data and from the arrival of history. If a live binding rebuilds the container or toggles its entrance class, watch the title and controls over several updates to locate the first element that restarts.

Drive a stable simulated tag, then a burst of changing readings while opening and closing the faceplate. Observe the shell, number formatting and input availability independently. Restrict transition ownership to the intended change. Replay with reduced motion and record the interruption result on the deployed client.

## Select the animation owner before tuning timing

Trace the visual property to its owner. A native Button handles its own activation, a project style can provide press feedback and a host binding can report the eventual result. Giving all three independent visual transitions can make a single press appear to issue multiple requests. Keep presentation tied to its source and make pending or confirmed states persist long enough to read when the process requires it.

Compare the interaction with the stylesheet effect disabled and the command simulated. If response is still late, inspect the event or binding path. If disabling the effect immediately restores usability, tune the owning rule and replay the action under rapid repeats. Include a keyboard path and a no-motion path that communicate the same functional state.
## Build motion from stable native states

First make the resting states correct with all transitions disabled. Verify the native component's enabled state, binding ownership, final geometry and focus. Then identify the single visual property that should interpolate. A change to transform or opacity can convey local continuity while layout and process information remain stable. Inspect the actual client before claiming a rendering performance benefit.

For a reversible interaction, define what happens when the state changes halfway through the effect. Compare direct retargeting with a fresh entrance. If the framework cannot expose the needed geometry, a persistent selection cue plus a local reveal can preserve the operator's sense of place. Keep command acknowledgment and process quality tied to their authoritative signals throughout.

## Use one persistent indicator with two resting states

For a fixture disclosure row, keep the equipment label stationary and rotate only its direction indicator as the detail expands. Give the indicator a stable project class and bind an additional state class to the actual expanded flag. Preserve the native activation control and visible focus cue. The expanded region must remain operable when transitions are disabled.

A project stylesheet can transition transform on the base indicator class and set rotation on the expanded class. In the reduced-motion rule remove the transition while keeping the final orientation. Rapidly expand, collapse and expand during a delayed detail update. If the indicator restarts from its initial orientation every time a value arrives, inspect whether the element is being recreated. Keep the cue tied to expansion, not process refresh.

```css
.psc-detailChevron {
  transition: transform 120ms ease-out;
}
.psc-detailChevron.psc-expanded {
  transform: rotate(90deg);
}
@media (prefers-reduced-motion: reduce) {
  .psc-detailChevron {
    transition: none;
  }
}
```

Tune in the target client.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| A delayed result restarts the entrance | Trace class changes and content mounting at result arrival. | Tie the entrance to the navigation event and update the result in place. |
| The animation looks smooth but the operator cannot continue | Exercise the next action before the effect settles. | Fix hit targets, focus or control availability at the actual native boundary. |
