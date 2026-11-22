# Open two detail popups on one page

## Set up the case

Use two distinct fixture assets. Record each launcher's popup ID, view path and params. Decide whether this design intends reuse or concurrent popups.

## Exercise the interaction

For concurrent popups, close A while B remains open. For reuse, switch A to B while A's history is pending. Inspect title, current values and close target after the switch.

## Acceptance and evidence

Record the intended lifecycle and the result of reopening the same asset. Distinguish stale child state from misrouted host parameters.

## Dismiss while a validation error is visible

Open a fixture editor, produce a validation error and close using each supported path. Reopen for the same asset, then a different asset. Check draft, error text, selected tab and return focus independently. Document any deliberate persistence and its owner. Clear state that cannot safely be carried into the next context.
