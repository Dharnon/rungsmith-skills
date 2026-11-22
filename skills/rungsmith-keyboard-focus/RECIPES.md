# Return from a popup after filtering its opener

## Set up the case

Open a detail popup from the second keyboard-reachable row. While it is open, remove that row in the fixture. Close using the supported dismissal action.

## Exercise the interaction

Record where the next Tab lands. If the original row disappeared, choose a stable list or filter control as the logical destination and inspect the target version's supported focus behavior.

## Acceptance and evidence

Repeat with the opener still present and with backward traversal. Report the first key that loses context.

## Recover from invalid text without a pointer

Open a fixture editor from the keyboard, enter an out-of-range value and activate Apply. Observe whether the user can locate the error, return to the field, correct the value and submit once. Close the popup using its supported keyboard route. Record focus and visible indication at every transition where they diverge.
