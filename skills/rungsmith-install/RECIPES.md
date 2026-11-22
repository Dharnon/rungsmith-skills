# Reinstall an unchanged revision

## Set up the case

Capture the installed view paths, consuming host parameters and scoped stylesheet rules. Import the same authorized package into a development copy twice.

## Exercise the interaction

Compare the second import to the first. Duplicate selectors, reset example params or an overwritten local override identify a merge problem even when the example still renders.

## Acceptance and evidence

Report which resources changed on the second pass and reopen an existing consumer to check its behavior.

## Handle an update that changes a default

Use a development consumer that intentionally omits an optional param. Compare its old and new rendered behavior, then explicitly supply the previous value. If that restores the expected behavior, document the changed default and affected consumer. Verify that consumers already supplying the new value retain their existing behavior.
