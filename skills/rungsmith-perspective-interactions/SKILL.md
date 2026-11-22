---
name: rungsmith-perspective-interactions
description: Implement and debug native Perspective menus, dialogs, tooltips, selection, keyboard controls and scrubbers using declared parameters, bindings and events. Use for stuck overlays, stale selection, drag feedback and state isolation.
metadata:
  status: preview
  native-verification: pending
---

# Perspective interaction engineering

Read the view contract and target-version component properties/events before choosing an implementation. Identify host-owned value, transient UI state, process state and output events. Keep requested native work native; web behavior libraries are references, not executable native view definitions.

Follow delegated project-script functions, message handlers and popup views before concluding that behavior is absent. Distinguish a declared parameter direction from an observed host-binding result. An input parameter assigned by a script needs a host propagation test; it is not automatically a proven broken contract.

When a native slider is overlaid with decorative labels, inspect pointer-events, stacking, enabled state and keyboard focus. Opacity or an invisible native thumb does not establish whether the control remains keyboard accessible. Test native focus and the visible focus cue together.

Describe expected pointer, keyboard, dismissal, blur and reopen behavior before editing. Selection, focus and hover are distinct states. Use semantic native controls where available; do not turn a label into a button without keyboard behavior and accessible naming supported by the component.

For popups, reserve final geometry, select one close owner and restore focus where supported. Test Escape, outside click if enabled, trigger reactivation and close/reopen. A tooltip follows hover/focus and should not remain merely because its trigger was selected. Verify native API support rather than inventing focus methods.

For selects and trees, test value propagation and identity under reordered items, empty data, disabled options and duplicate labels. Keep stable keys separate from display text. Filter without mutating shared input data unexpectedly.

For scrubbers, separate visual feedback from committed values. Inspect native update modes and supported pointer/keyboard events. Apply bounds, units, increments and actual enabled/interlock state. Measure drag continuity and Gateway round trips; avoid queuing a script for every visual frame. Do not claim browser-local behavior for a server-driven implementation.

Scope messages and popup identifiers to the view/equipment instance. Test two instances simultaneously. A disabled appearance must correspond to blocked interaction; a hidden control is not command authorization. Bind real tag writes only within the user's requested scope and preserve authorization at the command boundary and existing controller interlocks.

Check internal popup routing and the public output event separately: an internal recipient token does not make a page-scoped host event distinguishable. Inspect option count limits and per-option disabled handling, not just the component-level disabled flag. Test invalid ranges, nonpositive steps and externally supplied out-of-range values; clamping a percentage does not validate the underlying contract.

Classify findings as confirmed static defects, risks requiring native verification, or positive evidence. Separate focusability, keyboard activation and visible focus instead of treating them as one property.

Verify click, keyboard, repeated activation, cancellation, rapid changes, disconnected state and reopen. Record outputs and affected instance identity. A screenshot does not establish an interaction pass.

## Trace an intent across an embedded view boundary

For a row action, map the activating component, child parameter or message payload, receiver scope and final host action. Page-scoped messages can reach several matching handlers. Inspect the filter at each recipient and use stable instance identity when equipment identity alone cannot distinguish two panels for the same asset. [Ignition component message handlers](https://docs.inductiveautomation.com/docs/8.1/ignition-modules/perspective/scripting-in-perspective/component-message-handlers)

Run two copies on one page and activate just one. Record which handlers received the message, which acted and which public outputs changed. Reorder the rows and repeat with keyboard activation. A single visible popup is insufficient evidence of a single action when both handlers target the same popup ID.
