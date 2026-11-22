---
name: rungsmith-stress-test
description: "A view works with ideal demo data but breaks in real conditions. A reproducible defect report with data cases and native test evidence."
metadata:
  status: draft
  native-verification: pending
---

# Stress-test a view

A reproducible defect report with data cases and native test evidence.

Practice this workflow in a development project: [Break a repeated equipment row with distinguishing suffixes](RECIPES.md).

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

## Find the smallest combination that reproduces a failure

Start with the exact deployed host context: asset, viewport, input method, locale and data state. Reproduce the report before changing several axes at once. If a row breaks only with a long translated label and an open page dock, keep both conditions and remove unrelated complexity. A standalone screenshot of the label misses the failing combination.

Classify the failure by consequence. Truncating a redundant description is different from truncating the only character that distinguishes two assets. Prioritize a wrong selection or misleading quality over a cosmetic wrap. Record the minimum fixture and the nearest passing case, such as a slightly wider host or the same data with the dock closed, so the repair has a precise boundary to test.

## Build fixtures from failure boundaries

Inspect the component's real input shape before choosing values. An equipment path can fail at its distinguishing suffix, a measurement at the transition through zero, a query at the difference between empty and failed, and a table at a refresh that reorders selected rows. For each boundary construct a nearest passing input and one failing candidate. Keep the fixture portable enough that another developer can replay it in the same host.

Combine cases only after each single-variable case is understood. An unusually long translated label plus an expanded dock may be the smallest trigger for clipping. Adding simultaneous quality loss and sorting too early makes diagnosis ambiguous. Preserve the smallest failing combination and test it against a different consumer to identify whether the fault belongs to data, child layout or host layout.

## Build a reversible fixture selector

In an isolated development host, define a case selection local to the view and map it to named records. For an equipment summary use nominal, distinguishing-suffix, good-zero, missing-quality and delayed-old-result. Keep the child contract identical across cases. If the real child is hardwired to a source, use an existing simulation or development adapter and document the boundary you exercised.

Make reset restore selection, active fixture and pending simulated responses. Otherwise the fifth test can inherit the fourth test's late data and produce an irreproducible report. Run nominal, failing case, nominal, then the same failing case again. Record the smallest named sequence that reproduces the defect and whether returning to nominal fully recovers the screen.

Provide the fixture name, input record, host dimensions, simulated response ordering, expected result and first divergence. Include a reset path that another developer can repeat.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| A failure disappears outside the popup | Repeat at the same measured width standalone and embedded. | Record the minimum host configuration that reproduces it. |
| A test produces a dramatic but impossible value | Check the component's actual data contract and upstream transformation. | Replace with the nearest deliverable boundary case or label it as robustness exploration. |

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A reproducible defect report with data cases and native test evidence. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Stress-test this alarm table with long names, huge values and empty history. Report the breaks first.
