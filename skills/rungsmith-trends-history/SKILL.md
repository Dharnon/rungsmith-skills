---
name: rungsmith-trends-history
description: "Charts look interactive but ignore range controls or missing data. A chart/data contract and evidence that controls change the selected range."
metadata:
  status: draft
  native-verification: pending
---

# Trends & history

A chart/data contract and evidence that controls change the selected range.

## Workflow

1. Trace chart series, time zone, sample interval and historical query.

2. Wire time-window and series controls to actual data; label sample data.

3. Check gaps, quality, aggregation, loading, empty results and request frequency.

## Trace the selected window into returned samples

Start at the range control and follow the selected asset, start/end timestamps, time zone and aggregation into the actual history binding or query. Compare the query bounds and returned timestamps with the axis bounds. A changing axis with unchanged data can conceal a disconnected range control.

Use fixture history with a short excursion, a known gap and a flat interval. Compare short and long windows and inspect whether aggregation obscures the excursion or interpolation bridges the gap. Switch assets during a pending load and confirm the legend and samples belong to the same selection. For local-time labels, include an interval near a clock change when relevant.

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A chart/data contract and evidence that controls change the selected range. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Make this history chart respond to range selection and explain gaps without inventing readings.
