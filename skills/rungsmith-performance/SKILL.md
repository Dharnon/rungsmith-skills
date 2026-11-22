---
name: rungsmith-performance
description: "Slow loading, janky interactions or high session load. A before/after observation and the actual bottleneck."
metadata:
  status: draft
  native-verification: pending
---

# Native performance

A before/after observation and the actual bottleneck.

Practice this workflow in a development project: [Separate mounting cost from query latency](RECIPES.md).

## Workflow

1. Reproduce with one client and record input-to-feedback timing.

2. Inspect bindings, script frequency, layout churn and heavy hidden views before adjusting CSS.

3. Apply the smallest supported change and repeat the same measurement.

## Measure the milestone the operator experiences

Split a slow faceplate opening into launcher activation, visible shell, first valid reading and usable history tab. Record a cold and a repeated open with the same project revision, equipment and client. A slow history query can coexist with a responsive control tab. Measure their timings independently.

Inspect which embedded views and bindings are active before the user selects history. Check repeated instances for duplicate subscriptions, query executions or script transforms using diagnostics available on the target system. Change one suspected cause in development and repeat under the same conditions. Report the observations and any remaining uncertainty about network or Gateway load.

## Check whether a repair merely moves the wait

Lazy loading a trend can improve time to the first faceplate reading while making the first history visit slower. Measure both milestones and record which task the operator performs most often. Include repeated opens because a growing number of subscriptions or active bindings may only become visible after navigating away and back several times.

When a hidden surface is expensive, verify whether it remains mounted and continues querying in the actual native implementation. Visibility alone is insufficient evidence of suspended work. Compare repeated navigation with the same simulated data volume and client count. A useful performance report includes what became faster, what became slower and the observation that links the difference to the resource changed.

## Choose an experiment that isolates a cost

Record the operator-visible milestone before inspecting implementation. Slow first content, sluggish input and delayed confirmation involve different paths. Build a comparison that changes one factor: replace a history source with an equivalent cached fixture, reduce repeater instance count or remove a visual transition while keeping native actions intact. Keep the time range and data volume comparable.

Interpret the result narrowly. A faster chart with fewer points implicates a data-volume-dependent cost; it does not establish whether the bottleneck is query, transformation, transport or rendering. Time those boundaries using available project diagnostics. Preserve the smallest reproducible case and compare cold, repeated and post-navigation runs before claiming a durable improvement.

## Interpret a measured comparison without overclaiming

Illustrative recordings: live binding gives shell at 180 ms and first plot at 1,450 ms. An equal-sized local dataset gives shell at 175 ms and first plot at 430 ms. The difference implicates work on the live-data path. It does not isolate database time. Query execution, result transfer and transforms still need separate observations. Retain the same point count and chart settings across runs.

Next feed the actual returned values through the normal transform, then compare a fixture already in chart-ready form. If the gap persists with the same local input, inspect transformation or repeated work. If it disappears, follow the acquisition path. Run repeated trials and report the spread, client build and cold/warm status. Measurements from this example are illustrative rather than target budgets.

Report a milestone table with trial count, shell time, first usable time, fixture difference and the narrowest causal conclusion supported by the comparison.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| Warm opens are fast but each cold open is slow | Measure first shell and first valid data separately on cold runs. | Investigate the milestone that remains slow in the operator's real route. |
| Opening and closing repeatedly gets slower | Observe active work and resource count after each close. | Find retained subscriptions or repeated work before changing transition timing. |

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A before/after observation and the actual bottleneck. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Find why opening this faceplate is slow. Measure before changing animations.
