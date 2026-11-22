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

## Diagnose a faceplate that flashes on data updates

Trace the class or style binding back to the event that changes it. Separate opening the native view from changes in process data and from the arrival of history. If a live binding rebuilds the container or toggles its entrance class, watch the title and controls over several updates to locate the first element that restarts.

Drive a stable simulated tag, then a burst of changing readings while opening and closing the faceplate. Observe the shell, number formatting and input availability independently. Restrict transition ownership to the intended change. Replay with reduced motion and record the interruption result on the deployed client.
