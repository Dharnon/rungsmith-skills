---
name: rungsmith-scrubbers
description: "Dragging pauses, bounds conflict or lock only changes appearance. A consistent value contract and latency observations in the native client."
metadata:
  status: draft
  native-verification: pending
---

# Scrubbers & setpoints

A consistent value contract and latency observations in the native client.

Practice this workflow in a development project: [Round and reconcile a draft setpoint](RECIPES.md).

## Workflow

1. Identify value ownership, units, step, bounds and commit event.

2. Inspect supported native update modes and round trips; distinguish visual feedback from process writes.

3. Test pointer capture where available, keyboard steps, cancellation and actual interlock behavior.

## Separate the draft, emitted intent and confirmed setpoint

Inspect the slider's supported update mode, numeric input range, engineering unit and host binding direction. Determine who rounds a draft and what should happen when a value falls between steps or the configured bounds change mid-edit. Use a fixture host that records emitted values and can delay confirmation.

For a fractional increment, edit once with the keyboard and once by dragging near the upper bound. Compare the displayed draft, emitted request and host-confirmed value in the same units. Cancel mid-drag, change the lock state and repeat with a second instance. On rejection restore or identify the authoritative setpoint. Record how many intents each edit produced.

## Handle revisions to range and unit during editing

Capture the editing context when a draft starts: asset, unit, valid range and step. If the host switches engineering units, the displayed number may change meaning while the pointer remains down. Reconcile or cancel the draft according to the host contract before emitting another value. Do the same when selection changes to an asset with different limits.

In a fixture, begin at a legitimate near-limit value and narrow the range during editing. Examine the draft, the host-confirmed value and the eventual request independently. A clamped thumb position can hide an invalid numeric payload. Test both a rejected commit and a valid retry so the control remains usable after the first failure.

## Write down the numeric contract before binding the thumb

List display unit, host unit, low and high bounds, allowed increment, reference point for rounding and the owner of the accepted value. A step of 0.5 with a minimum of 0.25 permits 0.25, 0.75 and 1.25 when the contract anchors steps at the minimum. Rounding to multiples of 0.5 from zero would produce a different set. Check the installed control and host validation with boundary examples.

Separate preview from commit. A continuously updating numeric label can follow the draft without requiring a process request for every movement. A rejected request must leave an intelligible accepted value and permit another valid edit. If conversion and rounding occur at different layers, trace an example in both directions. Format for readability only after establishing the numeric value used by the host.

## Test display units against host units

Suppose a fixture host stores kPa while the edit surface displays bar, with 1 bar equal to 100 kPa. The host supplies 250 kPa. The editor displays 2.50 bar. Increasing by 0.05 bar should produce a draft of 2.55 bar and a single intended host value of 255 kPa. Trace the value at the native control, conversion boundary, emitted request and host-confirmed readback.

Confirm that an incoming 255 kPa does not re-enter the conversion path as 255 bar or generate another edit intent. Compare drag and keyboard paths and repeat after a rejected request. Inspect where rounding occurs. Rounding the engineering value early can change the accepted step grid; rounding the formatted string should affect presentation only. Confirm the displayed unit changes together with its numeric representation.

Fixture expectations: 250 kPa → 2.50 bar → one increment → 2.55 bar → one request for 255 kPa → confirmed display 2.55 bar.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| Pointer and keyboard yield different accepted setpoints | Compare minimum, step origin, unit conversion and commit timing. | Use one numeric contract across input methods. |
| The thumb is within bounds but the host rejects the request | Inspect raw payload, display rounding and the current host limits. | Validate the emitted numeric value and reconcile rejection with authoritative state. |

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A consistent value contract and latency observations in the native client. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Diagnose this setpoint scrubber under fast dragging. Preserve units, limits and lock behavior.
