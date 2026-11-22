---
name: rungsmith-trends-history
description: "Charts look interactive but ignore range controls or missing data. A chart/data contract and evidence that controls change the selected range."
metadata:
  status: draft
  native-verification: pending
---

# Trends & history

A chart/data contract and evidence that controls change the selected range.

Practice this workflow in a development project: [Distinguish an aggregated excursion from a missing interval](RECIPES.md).

## Workflow

1. Trace chart series, time zone, sample interval and historical query.

2. Wire time-window and series controls to actual data; label sample data.

3. Check gaps, quality, aggregation, loading, empty results and request frequency.

## Trace the selected window into returned samples

Start at the range control and follow the selected asset, start/end timestamps, time zone and aggregation into the actual history binding or query. Compare the query bounds and returned timestamps with the axis bounds. A changing axis with unchanged data can conceal a disconnected range control.

Use fixture history with a short excursion, a known gap and a flat interval. Compare short and long windows and inspect whether aggregation obscures the excursion or interpolation bridges the gap. Switch assets during a pending load and confirm the legend and samples belong to the same selection. For local-time labels, include an interval near a clock change when relevant.

## Make range and aggregation choices inspectable

For a time window that hides a known excursion, inspect the raw fixture interval, requested sample density and aggregation configured by the binding. Compare the returned series with the plotted points before choosing a chart change. A coarser series may legitimately hide short peaks, but its label and intended operating task must still be appropriate for that aggregation.

Check the boundaries between successive windows with a fixture event exactly at a boundary. Look for an omitted or duplicated sample according to the actual query contract. Repeat with a gap and a time-zone change relevant to the deployment. Record timestamps with their zone and the selected equipment ID so a later reviewer can reproduce the apparent shift.

## Choose a sampling strategy for the operator's question

Ask whether the chart is used to see a long-term pattern, locate a short excursion or compare simultaneous readings. An average may serve the first task and conceal the second. Inspect the historian query, aggregation, return interval and chart treatment of missing intervals. Preserve units and time zone with the series identity. A legend alone cannot establish that the currently plotted samples belong to the selected asset.

Trace a known fixture excursion through raw input, returned samples and the plot. If the query already omits the excursion, changing line interpolation will not recover it. If the returned samples contain a gap while the line appears continuous, inspect the chart configuration. Document what the chosen window and aggregation allow the operator to infer about the underlying process.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| The range selector changes but samples do not | Compare the query input and returned bounds with displayed axis bounds. | Repair the range binding before adjusting chart styling. |
| A spike disappears only on wide windows | Inspect returned samples and aggregation for both intervals. | Explain the sampling trade-off or choose an aggregation appropriate to the task. |

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A chart/data contract and evidence that controls change the selected range. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Make this history chart respond to range selection and explain gaps without inventing readings.
