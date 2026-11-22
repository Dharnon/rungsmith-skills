---
name: rungsmith-motion-opportunities
description: "The interface feels static but frequent actions must remain fast. Identify the few changes where motion would clarify feedback."
metadata:
  status: draft
  native-verification: pending
---

# Find useful motion

Identify the few changes where motion would clarify feedback.

## Look for a moment when the operator loses context

Walk through one real task in the target view. Record the initiating action, what changes on screen and what the operator must locate next. A candidate earns motion only if you can name a specific ambiguity a transition could resolve. If a persistent label or a clearer selection state solves it, record that finding and finish the review there.

For example, expanding a maintenance row may move the selected equipment out of sight. Inspect the final layout first. If the identifier stays visible but the relationship to the new details is unclear, propose a brief reveal anchored to that row. If the identifier disappears, address that layout issue first. Specify what a second tap during the reveal should do and how the same relationship stays clear with reduced motion.

Keep alarm onset, command availability and changing measurements immediately readable. For each proposed transition, give the resource, trigger, ambiguity, proposed behavior and a way to judge it in the target client. Replay the task twice in quick succession: the operator should be able to continue as soon as the control is available. Leave implementation for an accepted proposal.

## Locate the trigger in the native resource

Inspect whether the proposed cue follows a one-time operator action or a frequently changing property binding. For a selected repeater item, track the stable equipment identity across refreshes. If refresh reorders the list, test whether the same equipment remains identifiable before proposing a transition. Name the view or style class that would own the cue.

## Evidence and handoff

A small opportunity list with reasons and exclusions. Cite the project evidence behind the recommendation and identify any behavior that still needs a session test.

## Example request

Where would motion help this maintenance flow? Also explain what should remain instant.
