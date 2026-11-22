---
name: rungsmith-ui-sdk-contracts
description: "A UI SDK interaction needs an equivalent in a native component. Translate UI SDK behavior into native inputs, events and state."
metadata:
  status: draft
  native-verification: pending
---

# UI SDK behavior contracts

Translate UI SDK behavior into native inputs, events and state.

Practice this workflow in a development project: [Port a controlled selector contract](RECIPES.md).

## Workflow

1. Read the installed or upstream component documentation for selection, focus, popup and dismissal behavior.

2. Map each behavior to declared native parameters, supported events and per-instance state.

3. Test keyboard, Escape, reopen and propagation independently; mark browser-only behavior and never claim React adapters run in view JSON.

## Translate a selector contract one behavior at a time

Use the requested SDK version to extract selection identity, controlled value, open state, focus movement, dismissal and public change notification. For each, locate a declared Perspective parameter, supported native interaction or host handler. Document where the native component already owns the behavior so that a second handler does not emit a duplicate change.

In a fixture host, select between two options with the same label, cancel an uncommitted choice and reopen after the host changes the value. Record visible selection and emitted identity separately. If the reference relies on DOM focus management unavailable to the native view, specify the supported keyboard behavior and the remaining gap.

## Identify controlled and committed values at the boundary

Read the reference interaction from the consumer's perspective. Determine whether highlighting an option, selecting it and committing it are distinct events. Then inspect the installed Perspective component's available properties and events. A host binding may observe a selected value immediately even when the reference API reports only a later confirmation.

Where behaviors diverge, decide whether the host needs an explicit draft and Apply step or can use the native selection semantics directly. Exercise host-driven updates while the picker is open and cancellation after a change. Record the value the host sees at each transition. This mapping becomes the acceptance contract for the port and makes any remaining approximation visible.

## Translate ownership before translating appearance

Read the source component's public contract in the requested revision. Identify controlled value, default value, transient highlighted item, open state, public events and focus policy. In the native design, map each observation to a declared parameter, native component property, supported event or explicit host responsibility. Keep unknown mappings visible. A web hook or React adapter does not become an executable native resource simply because the names align.

For each mapped output specify what causes it and which transitions should stay silent. Hydrating an initial selection, receiving a host change and committing a user choice can all produce the same visible label. Exercise those transitions separately. If the native component deliberately differs, agree on the operator-facing contract before adding adapters that might create a second source of truth.

## Keep a behavior-level compatibility record

Pin the reference revision and the installed native component version when evaluating a port. Record the specific behavior tested rather than a blanket compatibility label. A selector may match value propagation and option identity while differing on Escape, focus recovery or keyboard navigation. Capture the input, trigger and visible or emitted result for each supported behavior.

On an upstream upgrade, compare the public interaction changes with this record before revising native code. A new web styling prop may require no native change. A change to whether clearing emits a public selection event may affect every consumer. Replay the smallest affected native test, then check an existing host that still expects the original behavior. Keep the adapter scoped to the agreed native contract.

Example compatibility entry: external selection update → label changes once → zero user-commit intents. Record the tested upstream revision and the native fixture output count.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| Highlighting an option commits it unexpectedly | Trace transient highlight, selected value and host output in both implementations. | Give draft and committed selection explicit owners where required. |
| A host-driven change generates an extra public event | Count outputs during hydration, external update and user commit. | Align the emission policy with the declared consumer contract. |

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A behavior mapping and native acceptance tests. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Map UI SDK selection and popup behaviors to this native equipment picker.
