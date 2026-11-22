---
name: rungsmith-motion-language
description: "You can describe the effect but not its name or intended behavior. Name an interaction precisely so the implementation request is clear."
metadata:
  status: draft
  native-verification: pending
---

# Motion vocabulary

Name an interaction precisely so the implementation request is clear.

Practice this workflow in a development project: [Translate “make it glide” into a testable request](RECIPES.md).

## Workflow

1. Translate the description into terms such as crossfade, morph, origin-aware transition or direct manipulation.

2. Explain the distinction using one operational example.

3. Identify whether the effect is native CSS, a supported approximation or a custom-module requirement.

## Turn an effect description into a Perspective request

For “the details should grow out of the selected row”, determine whether the user needs a visual relationship, literal geometric continuity or simply clear selection. A stable selected-row cue plus a panel reveal may express the relationship when the row and popup are separate native view instances.

Write the request with its trigger, owning resource, start and final states, interruption behavior and reduced-motion outcome. Distinguish an opacity transition on one owned element from a shared-element transition requiring geometry across two surfaces. Verify the latter's required hooks before promising it. Include a short replay such as switching rows halfway through opening.

## Distinguish direct manipulation from a pending request

For “the slider should follow my hand”, separate the pointer-to-thumb relationship from the requested setpoint and confirmed process value. Name the first as direct manipulation. Describe any wait for acknowledgment as pending feedback. Calling the whole interaction a spring or a smooth transition can send the implementer to tune easing while a binding round trip remains the actual cause.

Specify what should happen when the operator reverses direction, releases early or loses permission. A useful brief names what follows the pointer, what is allowed to lag, what ends the interaction and what remains visible with motion reduced. Tie each behavior to the installed native control or mark it for feasibility testing.

## Translate a visual reference into an implementable brief

Describe the visible relationship in nouns and verbs before naming a technique. Which element persists, which one changes, where is the operator looking, and what decision comes next? A crossfade means two visual states overlap in time. A reveal means content becomes visible within a stable context. A shared-element transition implies correspondence between two representations and may require geometry that the native host does not expose.

Finish the brief with an interruption rule. If the operator selects B while A opens, does the presentation retarget, close A first, or update one stable shell? Include the expected state when motion is reduced and when the data arrives late. That description gives the implementer a testable target even when the original reference uses a different rendering technology.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| The requester says “spring” but the value arrives late | Compare pointer-to-thumb feedback and request-to-confirmation timing. | Describe local tracking and pending feedback as separate behaviors. |
| A requested morph crosses a popup boundary | Locate the geometry owner for both surfaces. | Specify a native approximation and the exact relationship it preserves. |

## Evidence and handoff

A precise term and an implementation boundary. Cite the project evidence behind the recommendation and identify any behavior that still needs a session test.

## Example request

What should we call the transition between Home and Process? Explain the native options.
