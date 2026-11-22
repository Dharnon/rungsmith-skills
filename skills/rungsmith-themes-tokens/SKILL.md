---
name: rungsmith-themes-tokens
description: "Inconsistent palettes, dark/light themes or duplicated style values. A token map, scoped style changes and theme verification notes."
metadata:
  status: draft
  native-verification: pending
---

# Themes & tokens

A token map, scoped style changes and theme verification notes.

## Workflow

1. Inventory theme files, named styles and the component scopes consuming them.

2. Map surface, text, border, focus and process-state roles; preserve color meaning across themes.

3. Change shared tokens in an opt-in scope and verify contrast, native chrome and neighboring views.

## Trace a semantic role to its consumers

Pick one visible mismatch and follow the component style, applied style classes and inherited theme variables in the target session. Determine which declaration wins before introducing another token. Map normal text, secondary text, focus and alarm priority separately. Record any native component states with their own styling surface.

Exercise one equipment summary under each supported theme with normal, unavailable, focused and active-alarm fixtures. Check adjacent components sharing the class and verify that the focus cue remains legible over alarm styling. Deliver the token name, defining resource, consuming class and state pairs actually checked.

Identify the resource owner before editing a shared color. A custom theme is Gateway-scoped. The Advanced Stylesheet and Style Classes belong to a project. For a change requested for one equipment family, inspect its assigned project class before modifying a theme consumed by other projects. [Perspective style scope](https://www.docs.inductiveautomation.com/docs/8.1/ignition-modules/perspective/styles/style-classes)

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A token map, scoped style changes and theme verification notes. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Unify the themes in these faceplates without changing alarm or command semantics.
