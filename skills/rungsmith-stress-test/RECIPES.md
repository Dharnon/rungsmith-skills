# Break a repeated equipment row with distinguishing suffixes

## Set up the case

Use two labels, Utilities/Water/Recirculation/P-204A and Utilities/Water/Recirculation/P-204B. Give A a good zero and B unavailable quality. Sort by label and reduce the host width.

## Exercise the interaction

Select B, reverse order, then open detail. If the wrong asset opens, trace selection identity. If the correct asset opens but cannot be identified, trace truncation and the quality display separately.

## Acceptance and evidence

Save the two fixture records, width and first failing step. Re-run the same values standalone and embedded.

## Test a history table with four distinct outcomes

Use the same time range and asset for each case. Change only the fixture response.

| Fixture response | Expected operator interpretation | First diagnostic if it fails |
| --- | --- | --- |
| Successful query, zero rows | No records match these filters | Inspect the empty-state binding |
| One valid row, value 0 | A recorded measurement of zero | Look for truthiness-based fallback |
| Query error | History unavailable | Inspect the transform that supplies a default dataset |
| Response for A arrives after selecting B | No A rows under B's header | Inspect the selection and result ownership |

Repeat the smallest failure with the native table on its own and then inside its usual container. Report whether the defect follows data transformation, selection or embedding. Preserve the fixture alongside the failure description so the repair can be checked against the exact same input.

## Check an apparent rounding collision

Display two valid measurements whose formatted labels are identical at the chosen precision while their underlying values differ. Sort and select each fixture row, then open detail. Verify identity survives formatting, the detail reports the project's intended precision and missing values have a distinct presentation. Capture raw input, formatted output and selected ID together.
