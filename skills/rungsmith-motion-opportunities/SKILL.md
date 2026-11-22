---
name: rungsmith-motion-opportunities
description: "The interface feels static but frequent actions must remain fast. Identify the few changes where motion would clarify feedback."
metadata:
  status: draft
  native-verification: pending
---

# Find useful motion

Identify the few changes where motion would clarify feedback.

Practice this workflow in a development project: [Decide whether a row reveal earns motion](RECIPES.md).

## Look for a moment when the operator loses context

Walk through one real task in the target view. Record the initiating action, what changes on screen and what the operator must locate next. A candidate earns motion only if you can name a specific ambiguity a transition could resolve. If a persistent label or a clearer selection state solves it, record that finding and finish the review there.

For example, expanding a maintenance row may move the selected equipment out of sight. Inspect the final layout first. If the identifier stays visible but the relationship to the new details is unclear, propose a brief reveal anchored to that row. If the identifier disappears, address that layout issue first. Specify what a second tap during the reveal should do and how the same relationship stays clear with reduced motion.

Keep alarm onset, command availability and changing measurements immediately readable. For each proposed transition, give the resource, trigger, ambiguity, proposed behavior and a way to judge it in the target client. Replay the task twice in quick succession: the operator should be able to continue as soon as the control is available. Leave implementation for an accepted proposal.

## Locate the trigger in the native resource

Inspect whether the proposed cue follows a one-time operator action or a frequently changing property binding. For a selected repeater item, track the stable equipment identity across refreshes. If refresh reorders the list, test whether the same equipment remains identifiable before proposing a transition. Name the view or style class that would own the cue.

## Estimate the cost of a cue at real update frequency

Watch one representative operating interval. Count operator-initiated transitions separately from value refreshes and automatic list reorders. A cue that feels informative on the first arrival can become the dominant visual event on a frequently refreshed screen. Ask which relationship the operator would lose without it and whether a stable label, selection marker or reserved space already conveys that relationship.

For each surviving candidate, identify the exact trigger that should start it and the updates that should leave it alone. Compare a static and a motion-enabled fixture during rapid changes. Recommend the cue only if it improves the intended task while the operator can still spot an unrelated abnormal state elsewhere on the screen.

## Decide where motion would earn its cost

Follow the operator's attention through an actual transition. Look for an object that changes location, a detail surface whose origin becomes unclear, or a request whose pending state is invisible. Determine whether the ambiguity persists after the layout, labels and data ownership are correct. Animating a wrong selection or an unlabeled loading region usually makes the underlying defect harder to diagnose.

Evaluate frequency, interruption and consequence together. A rare maintenance reveal may allow a short transition. A reading that refreshes repeatedly or an alarm onset needs immediate interpretation. Include a stationary equivalent for each proposed cue. If a static relationship already solves the task, capture that finding instead of adding an effect solely to make the view feel more active.

## Count how often the trigger really fires

Use the observed trigger, not the name of the feature, to estimate frequency. In a fixture with 12 visible readings updating every five seconds, a class reapplied per reading could initiate 144 cues per minute if every update restarts it. Opening the detail once initiates one cue. Verify whether the actual binding restarts the class before reporting either figure as observed.

Record exposure per surface and per operator task. A brief transition on opening a maintenance panel may preserve orientation; the same transition tied to every refreshed reading can compete with alarms elsewhere. In a comparison run, freeze the process values and repeat the operator action, then resume only the updates. Keep candidates whose intended trigger can be isolated and whose stationary alternative leaves a real ambiguity.

Candidate record: trigger, observed frequency, relationship explained, proposed owner, stationary alternative and consequence of rapid repetition.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| The screen feels static but the first reading is delayed | Compare time to usable data with and without a presentation cue. | Address data latency or pending state before recommending motion. |
| Operators lose a row after the list reorders | Check stable selection identity and a persistent selection cue. | Propose movement only if the correct item still becomes hard to locate. |

## Evidence and handoff

A small opportunity list with reasons and exclusions. Cite the project evidence behind the recommendation and identify any behavior that still needs a session test.

## Example request

Where would motion help this maintenance flow? Also explain what should remain instant.
