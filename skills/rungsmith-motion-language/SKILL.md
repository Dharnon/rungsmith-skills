---
name: rungsmith-motion-language
description: "You can describe the effect but not its name or intended behavior. Name an interaction precisely so the implementation request is clear."
metadata:
  status: draft
  native-verification: pending
---

# Motion vocabulary

Name an interaction precisely so the implementation request is clear.

## Workflow

1. Translate the description into terms such as crossfade, morph, origin-aware transition or direct manipulation.

2. Explain the distinction using one operational example.

3. Identify whether the effect is native CSS, a supported approximation or a custom-module requirement.

## Turn an effect description into a Perspective request

For “the details should grow out of the selected row”, determine whether the user needs a visual relationship, literal geometric continuity or simply clear selection. A stable selected-row cue plus a panel reveal may express the relationship when the row and popup are separate native view instances.

Write the request with its trigger, owning resource, start and final states, interruption behavior and reduced-motion outcome. Distinguish an opacity transition on one owned element from a shared-element transition requiring geometry across two surfaces. Verify the latter's required hooks before promising it. Include a short replay such as switching rows halfway through opening.

## Evidence and handoff

A precise term and an implementation boundary. Cite the project evidence behind the recommendation and identify any behavior that still needs a session test.

## Example request

What should we call the transition between Home and Process? Explain the native options.
