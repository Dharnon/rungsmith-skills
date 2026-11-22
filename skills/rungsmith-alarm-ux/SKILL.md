---
name: rungsmith-alarm-ux
description: "Priority, acknowledgment and history are hard to distinguish. An alarm state matrix and specific UX changes with verification gaps."
metadata:
  status: draft
  native-verification: pending
---

# Alarm UX

An alarm state matrix and specific UX changes with verification gaps.

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

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

An alarm state matrix and specific UX changes with verification gaps. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Review this alarm screen for active, cleared, unacknowledged and empty states.
