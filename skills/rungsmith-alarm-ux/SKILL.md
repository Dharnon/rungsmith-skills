---
name: rungsmith-alarm-ux
description: "Priority, acknowledgment and history are hard to distinguish. An alarm state matrix and specific UX changes with verification gaps."
metadata:
  status: draft
  native-verification: pending
---

# Alarm UX

An alarm state matrix and specific UX changes with verification gaps.

Practice this workflow in a development project: [Two alarms with one display label](RECIPES.md).

## Workflow

1. Read alarm data fields and existing acknowledgment flow.

2. Separate priority, active/cleared and acknowledged state using text and color.

3. Verify empty results, filters, history and authorized acknowledgment feedback.

## Read one alarm through its lifecycle

Use a simulated alarm configured for manual acknowledgment. Run two occurrences from the same source and capture each EventId.

| Occurrence | Sequence | Observation |
| --- | --- | --- |
| A | Activate, acknowledge while active, then clear | After acknowledgment the process condition is still active. |
| B | Activate, clear before acknowledgment, then acknowledge | After clearing, the event still requires acknowledgment. |

Record the status table filters at each step. A row can disappear when its state leaves the filter. Correlate journal transitions by EventId within each occurrence. [Ignition alarm event properties](https://docs.inductiveautomation.com/docs/8.1/platform/alarming/configuring-alarms/alarm-event-properties-reference)

Repeat with two sources sharing a display label. Select one fixture event, record its EventId, then reorder the rows. Check that the selected event identity survives the sort and that an acknowledgment applies only to the intended selection. Compare the live table with the configured Alarm Journal Table over a range containing the fixture event. Record journal availability and filter settings when explaining missing history.

## Investigate an apparently empty alarm list

An empty status table has several plausible causes. Capture the selected source, display path, state filters and shelf visibility before changing the view. Use a known simulated event in the requested scope. Broaden one filter at a time in the development session and record which change makes the event visible. A count elsewhere on the page may cover a different area or priority range.

Choose empty-state wording from the evidence the view actually has. A successful filtered result can say that no events match the current filters. A failed or unavailable source needs its own indication. Replay the case with a restrictive filter left active after navigation. The area and filter must remain discoverable before an operator interprets the empty table.

## Design the row around three independent questions

Read one row aloud. Which equipment is affected? Is its condition active now? Has someone acknowledged this occurrence? Priority answers a fourth question about significance. A red badge labelled “acknowledged” conflates at least two of these facts. Sketch the row with text first, assign each fact a stable place, then map site-approved colors to the appropriate dimension. Check the same row with color removed.

If a banner and table disagree, compare their scopes using the same instant, area and definition of outstanding. One might count active conditions while the other includes cleared events awaiting acknowledgment. Document the two predicates in operator language. Change the label when the scopes are intentionally different; change the data selection when the view promises the same population.

## Separate shelving from acknowledgment

During a simulated maintenance window, consider an active alarm that an authorized user shelves. Capture the EventId, active state, acknowledgment state and shelving indication from the configured alarm data. Inspect the active and shelved surfaces with the same area filter. The disappearance of the row from the ordinary list establishes what the list shows; it does not establish that the process condition cleared.

Exercise expiry separately from a manual return. While the fixture is shelved, first leave the condition active, then run a second occurrence where it clears. Observe each after the shelf ends. Derive the caption from the returned state. For a count such as “3 active”, document whether shelved items contribute and check the drill-down against that definition. Preserve the site's existing alarm policy; this exercise concerns what the view communicates.

Maintenance replay: source, EventId, shelf state, active state, acknowledgment, list membership and count predicate.

[Ignition manual — Alarm Event Properties](https://docs.inductiveautomation.com/docs/8.1/platform/alarming/configuring-alarms/alarm-event-properties-reference)

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| Status count decreases on acknowledgment | Compare the count predicate with active and acknowledgment flags for the same EventId. | Correct the caption or filter according to whether the count promises active conditions or outstanding acknowledgments. |
| History is empty but live rows exist | Check journal profile, selected period, source filter and whether the fixture produced a transition in that period. | Expose unavailable history separately from a successful empty search. |

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

An alarm state matrix and specific UX changes with verification gaps. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Review this alarm screen for active, cleared, unacknowledged and empty states.
