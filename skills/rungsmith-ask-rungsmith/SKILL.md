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

## Perspective constraints

Read the actual native view contract and target-version APIs. Keep process state, command permission and interlocks owned by the host. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A short diagnosis and the next skill to use. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

This faceplate feels slow and confusing. Which workflow should we use first, and what evidence do you need?
