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

Practice this workflow in a development project: [Catch one click reaching two handlers](RECIPES.md).

## Trace an intent across an embedded view boundary

For a row action, map the activating component, child parameter or message payload, receiver scope and final host action. Page-scoped messages can reach several matching handlers. Inspect the filter at each recipient and use stable instance identity when equipment identity alone cannot distinguish two panels for the same asset. [Ignition component message handlers](https://docs.inductiveautomation.com/docs/8.1/ignition-modules/perspective/scripting-in-perspective/component-message-handlers)

Run two copies on one page and activate just one. Record which handlers received the message, which acted and which public outputs changed. Reorder the rows and repeat with keyboard activation. A single visible popup is insufficient evidence of a single action when both handlers target the same popup ID.

## Distinguish selection changes from activation

In tables, trees and equipment pickers, a user can move focus, change selection or activate a detail action. Inspect which supported native event the implementation consumes. If a data refresh also updates a selection binding, opening a popup from every value change can trigger navigation without a new operator action.

Use a fixture with two entries sharing a label. Select the second, reorder the dataset, update the selected ID from the host and finally activate it explicitly. Log which steps emit an intent and which merely reconcile displayed state. Keep the public output narrow enough that the parent can distinguish a user request from a restored selection.
## Design the boundary between event and state

Write down the public event in operator terms, such as “open this equipment detail”. Then identify the state changes that can occur without that intent: sorting, initial hydration, restoring selection or an external update from the host. If every selected-value change opens a popup, these distinct transitions can become indistinguishable. Inspect the supported activation event and current consumer expectations before changing the contract.

For message-driven views, record the sender, message type, configured scope, instance discriminator and side effect. Two components can receive a message while only one should act. A log at the sender cannot establish single execution at the recipient. Exercise same-equipment duplicate instances as well as different equipment instances to reveal filters that rely on asset ID alone.

## Trace two views of the same equipment

Place an overview mini-panel and a maintenance panel for the same fixture asset on one page. Give each a distinct local instance key. For an interaction meant for the initiating panel, carry enough recipient context in the project's existing payload to distinguish the two. The asset ID answers which equipment is involved; the instance key answers which UI recipient owns this reaction.

For a development message, a payload might contain equipmentId P-204, instanceKey maintenance-right and selectedTab history. Inspect sender scope and each recipient filter. A page-scoped event may be intentionally observable by both views, while only one should open its history tab. Record reception separately from action. Broader updates genuinely intended for every representation of the asset can keep asset-level targeting.

Expected replay: both matching handlers may observe the event; only maintenance-right opens history. The overview keeps its previous selection.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| A programmatic host update opens details | Compare the selection binding with the native activation event. | Separate value reconciliation from the intent that opens detail. |
| A second instance acts on the same message | Capture scope, instance discriminator and recipient-side filtering. | Select the correct recipient before producing the side effect. |
