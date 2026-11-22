---
name: rungsmith-ask-rungsmith
description: "You know something feels wrong but not whether the cause is layout, latency or behavior. Turn an unclear UI request into the right focused skill."
metadata:
  status: draft
  native-verification: pending
---

# Choose a workflow

Turn an unclear UI request into the right focused skill.

Practice this workflow in a development project: [Triage a slow popup with three timestamps](RECIPES.md).

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

## Resolve competing explanations without a full audit

When two workflows seem plausible, choose a small observation that separates them. For “the trend shows the old pump”, compare the selected equipment ID with the history query input and the returned series. An old input points to selection or popup context. A correct input followed by an old result points to history request ownership. A correct series under an old title points to a separate label binding.

Carry the exact resource path and divergent pair of values into the selected workflow. If only a screenshot is available, mark the diagnosis provisional and specify the one interaction that would distinguish the causes. Avoid commissioning three broad audits when opening B immediately after A would settle the routing decision.

## Choose a diagnostic experiment before choosing a specialist

Start from the verb in the report. “Opening”, “waiting”, “choosing”, “sending” and “reading back” refer to different parts of a Perspective interaction. Build one short event trace from the available evidence. Stop at the first discrepancy between the intended and observed sequence. Later symptoms frequently disappear when that earlier transition is fixed.

Choose between two plausible owners using one reversible substitution. Replace a slow live source with an equivalent fixture while keeping the view and selection constant. Change the client width while keeping the asset and data fixed. Disable a decorative transition while retaining the host action. Hand the specialist the discriminating observation and the parts of the setup that must remain constant.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| The action works in the first panel only | Compare params and recipient identity in two mounted instances. | Route to interactions with the observed sender and recipients. |
| The same view works standalone but clips in a popup | Compare host size and embedded sizing before inspecting text formatting. | Route to Perspective CSS with the first overflowing boundary. |

## Evidence and handoff

A short diagnosis and the next skill to use. Cite the project evidence behind the recommendation and identify any behavior that still needs a session test.

## Example request

This faceplate feels slow and confusing. Which workflow should we use first, and what evidence do you need?
