---
name: rungsmith-themes-tokens
description: "Inconsistent palettes, dark/light themes or duplicated style values. A token map, scoped style changes and theme verification notes."
metadata:
  status: draft
  native-verification: pending
---

# Themes & tokens

A token map, scoped style changes and theme verification notes.

Practice this workflow in a development project: [Check focus and alarm priority together](RECIPES.md).

## Workflow

1. Inventory theme files, named styles and the component scopes consuming them.

2. Map surface, text, border, focus and process-state roles; preserve color meaning across themes.

3. Change shared tokens in an opt-in scope and verify contrast, native chrome and neighboring views.

## Trace a semantic role to its consumers

Pick one visible mismatch and follow the component style, applied style classes and inherited theme variables in the target session. Determine which declaration wins before introducing another token. Map normal text, secondary text, focus and alarm priority separately. Record any native component states with their own styling surface.

Exercise one equipment summary under each supported theme with normal, unavailable, focused and active-alarm fixtures. Check adjacent components sharing the class and verify that the focus cue remains legible over alarm styling. Deliver the token name, defining resource, consuming class and state pairs actually checked.

Identify the resource owner before editing a shared color. A custom theme is Gateway-scoped. The Advanced Stylesheet and Style Classes belong to a project. For a change requested for one equipment family, inspect its assigned project class before modifying a theme consumed by other projects. [Perspective style scope](https://www.docs.inductiveautomation.com/docs/8.1/ignition-modules/perspective/styles/style-classes)

## Preserve meaning when semantic states overlap

List the independent states that can appear on one component. A selected equipment row may also be in alarm, focused by keyboard and displaying an unavailable auxiliary channel. Giving each state a background color makes their combination depend entirely on the winning declaration. Choose separate cues for states that need to remain visible together, using the project's established conventions.

Verify combinations in the actual active theme rather than checking isolated swatches. Inspect which class owns each cue and how the native component renders its selected and disabled states. Change the narrowest token or class that restores meaning. Recheck another consumer that uses the same semantic role on a different surface.

## Organize tokens by meaning and ownership

Inventory the actual consumers before renaming a color. A shared accent can currently mean selection in one view, acknowledgment in another and a decorative border elsewhere. Split roles only when the project needs them to change independently. Determine whether the correct owner is a local component style, project class, stylesheet variable or Gateway theme. The intended scope determines how many unrelated screens could change.

Review combinations against real backgrounds, including focus on an alarmed row and disabled text over a selected surface. Inspect the actual winning declaration in each supported theme. When changing a token, select a second consumer with a different surrounding surface as a regression case. Document the role and affected states so later changes preserve equipment semantics.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| Focus vanishes only on selected alarm rows | Inspect the winning focus and selected-state declarations together. | Use independent cues that remain visible in combination. |
| A color correction changes multiple projects | Determine whether the edited resource is a Gateway theme. | Use the intended scope and check a representative second consumer. |

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A token map, scoped style changes and theme verification notes. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Unify the themes in these faceplates without changing alarm or command semantics.
