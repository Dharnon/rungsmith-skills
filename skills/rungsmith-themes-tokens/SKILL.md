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

## Perspective constraints

Read the actual native view contract and target-version APIs. Keep process state, command permission and interlocks owned by the host. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A token map, scoped style changes and theme verification notes. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Unify the themes in these faceplates without changing alarm or command semantics.
