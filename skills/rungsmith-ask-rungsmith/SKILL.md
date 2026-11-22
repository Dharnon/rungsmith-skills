---
name: rungsmith-ask-rungsmith
description: "You know something feels wrong but not whether the cause is layout, latency or behavior. Turn an unclear UI request into the right focused skill."
metadata:
  status: draft
  native-verification: pending
---

# Choose a workflow

Turn an unclear UI request into the right focused skill.

## Workflow

1. Identify the operator task and the observable symptom.

2. Distinguish broken behavior, excess motion, missing feedback and inconsistent styling.

3. Recommend the narrowest matching workflow and required evidence; explain when two workflows are needed.

## Route from the first observable mismatch

For a report such as “the pump popup feels slow”, ask which milestone is late: first visible shell, equipment identity, first valid reading or response to the next click. Inspect the opener action, target view path and first bound value. A prompt shell with a late value points toward bindings or query timing. A ready panel hidden behind an entrance points toward motion review.

Give the next reviewer the view path, the action to reproduce, the first divergent milestone and the matching skill name. If the screen opens immediately with the previous pump selected, start with rungsmith-overlays. Investigate performance only if a measured delay persists after the identity issue is understood.

## Choose between overlapping workflows

| Reproducible symptom | Start here | Evidence to carry forward |
| --- | --- | --- |
| A previously selected asset appears on reopen | rungsmith-overlays | Popup ID, opener params and first displayed asset |
| An interaction is visibly delayed with transitions disabled | rungsmith-performance | Time to first feedback and first valid data |
| One existing transition jumps on reversal | rungsmith-review-motion | Owning class and exact interruption sequence |
| The same entrance repeats on many screens | rungsmith-audit-motion | Shared style and two affected consumers |
| A displayed zero follows a failed binding | rungsmith-data-quality | Source quality and first transform producing zero |

## Evidence and handoff

A short diagnosis and the next skill to use. Cite the project evidence behind the recommendation and identify any behavior that still needs a session test.

## Example request

This faceplate feels slow and confusing. Which workflow should we use first, and what evidence do you need?
