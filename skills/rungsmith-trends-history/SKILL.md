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

## Perspective constraints

Read the actual native view contract and target-version APIs. Keep process state, command permission and interlocks owned by the host. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A chart/data contract and evidence that controls change the selected range. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Make this history chart respond to range selection and explain gaps without inventing readings.

## Research references

Original Rungsmith adaptation; upstream implementations are not bundled.
