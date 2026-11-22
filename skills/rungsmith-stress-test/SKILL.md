---
name: rungsmith-stress-test
description: "A view works with ideal demo data but breaks in real conditions. A reproducible defect report with data cases and native test evidence."
metadata:
  status: draft
  native-verification: pending
---

# Stress-test a view

A reproducible defect report with data cases and native test evidence.

## Build cases from the view contract

Find the field, view parameter or binding that feeds the suspect component. Capture one representative input and the client dimensions where it works. In an isolated fixture, change one input at a time so a failure can be reproduced. Use values the contract can actually deliver.

| Case | What to check |
| --- | --- |
| Long equipment path, with the distinguishing identifier at the end | Compare two similar rows at the narrowest supported width. Can the operator still tell them apart with keyboard or touch? |
| Zero rows after a successful query, then a failed query | Verify that only the successful empty result can communicate that there are no records. |
| Valid zero, missing value, then restored quality | Follow the same field through all three states. Check the unit, quality indication and recovery without reopening the view. |
| Two embedded instances with different equipment parameters | Change the selection in one fixture and check the other for unintended changes. |

Choose cases relevant to the request. Where a failure depends on zoom, reconnect or simultaneous updates, replay the smallest failing case under that condition. Record the resource, fixture value or transition, client dimensions, steps, expected result and observed result. A suspicious binding found during static review is a hypothesis until reproduced. Use simulated command targets for interaction tests.

## Identify the boundary that failed

When a long suffix clips, open the child view standalone and then embed it at the same width as the failing host. Inspect the parent position and embedded sizing before blaming the text component. Include the failing input and first divergent resource in the report so another developer can replay the defect without reconstructing the entire page.

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A reproducible defect report with data cases and native test evidence. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Stress-test this alarm table with long names, huge values and empty history. Report the breaks first.
