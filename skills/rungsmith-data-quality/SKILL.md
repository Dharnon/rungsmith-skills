---
name: rungsmith-data-quality
description: "Missing or stale readings look like valid live values. A documented state map and bindings that preserve data meaning."
metadata:
  status: draft
  native-verification: pending
---

# Data quality & states

A documented state map and bindings that preserve data meaning.

Practice this workflow in a development project: [Distinguish a live zero from a lost reading](RECIPES.md).

## Workflow

1. Trace value, quality, timestamp and connection sources.

2. Represent missing, stale, disconnected and uncertain states without coercing them to zero.

3. Test reconnection, changing quality and large values with units.

## Preserve meaning through transforms

Start at the displayed label and trace its binding, transform chain, source timestamp and quality. Locate the first point where a null, invalid quality or conversion failure becomes a plausible number. Keep formatting and unit conversion downstream of the validity check. Use the project's sampling rules when deciding whether a timestamp is stale: an unchanged event-driven value can still be healthy.

Drive a simulated pressure reading through valid zero, bad quality with a retained last value, then valid recovery. Record value, quality cue, timestamp and unit at each step. If retained values are shown, the presentation must make their age and status evident. Switch equipment during recovery and confirm the old reading cannot appear under the new identity.

## Reconcile fields with different update rates

Treat a faceplate assembled from several bindings as multiple observations. A fresh motor status does not establish that its temperature or flow reading is fresh. Trace each field to the timestamp and quality actually supplied by its source. If the contract supplies only an aggregate health signal, document that scope before applying it to every numeric value.

Decide what the user needs when one channel fails. Retaining a last known temperature can support troubleshooting if its age is visible. A status summary may instead need an explicit unavailable state. Test a partial failure while the other readings continue to change and then reconnect only the failed channel. Its recovery should not clear a quality warning belonging to another field.

## Define what the binding can actually prove

Map each displayed assertion to a source. The raw numeric value establishes magnitude. The quality code can describe validity. The timestamp may describe a change, poll or recorded sample depending on the source. Before displaying “stale”, identify which interpretation applies and what update behavior the project expects. An event-driven sensor can remain unchanged for hours while communications stay healthy.

Follow every transform that merges these signals. A formatter that substitutes zero for conversion failure destroys information needed later. Preserve a reason for unavailable data until presentation, then choose a display consistent with the site's conventions. Consider accessibility: a grayed-out number with its old unit still looks like a measurement to a user who cannot distinguish the color.

## Distinguish source time, query time and display time

Record which timestamp a user sees. A historian sample can have its own acquisition time, a query can finish seconds later and the session can render later still. Refreshing a label with the current clock makes old data appear newly sampled. In a simulated case, hold a sample at 10:00, return it from a query at 10:05 and reopen the panel at 10:07. The sample timestamp should still identify the 10:00 observation.

When building a historical fixture, inspect the binding's result shape. The Tall shape exposes value, quality, timestamp and path per row. Preserve their association when sorting or formatting; sorting one list of timestamps independently of its values corrupts the evidence. A display of last retrieval time can be useful, but label it as such and keep it distinguishable from the measurement timestamp.

Show an example row before transformation and its rendered counterpart, with source identity, value, quality, timestamp and time zone.

[Ignition manual — Tag History Bindings](https://www.docs.inductiveautomation.com/docs/8.1/ignition-modules/perspective/working-with-perspective-components/bindings-in-perspective/tag-history-bindings-in-perspective)

## Separate expected initialization from broken quality

Perspective Tag Bindings expose **Overlay Opt-Out** and an option for the initial uncertain value; neither is a general license to turn unknown source health into a plausible process value. In the exact target version, inspect the [official Tag Binding options](https://docs.inductiveautomation.com/docs/8.3/ignition-modules/perspective/working-with-perspective-components/bindings-in-perspective/tag-bindings-in-perspective). Make two fixtures: (a) transient initial Uncertain_InitialValue before first good subscription value, and (b) Bad quality after a previously good reading. Confirm that any initialization-only suppression does **not** suppress genuine connection failures.

Compare a good numerical zero with bad quality carrying the last known zero. They may render similar digits but have different operator meaning. If the fallback is a formatted dash or retained last value, show a quality/freshness cue independent of color. Never use §coalesce§ to erase the only evidence of invalid source quality. For the reusable-view acceptance matrix, read [Perspective engineering verification](../rungsmith-perspective-engineering/references/verification.md).

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| A disconnected source still displays a plausible last reading | Inspect pre-transform quality, raw payload and displayed age. | Retain or suppress the last sample according to the host policy and make its validity explicit. |
| A steady good sensor is marked stale | Identify what its timestamp measures and how that source reports updates. | Use a freshness rule compatible with the source's update behavior. |

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A documented state map and bindings that preserve data meaning. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Review sensor readings for stale, bad-quality and disconnected states.
