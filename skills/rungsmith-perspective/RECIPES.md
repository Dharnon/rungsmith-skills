# Trace a repeater instance into its detail view

## Set up the case

Give two development instances distinct equipment IDs and readings. Follow one instance from the repeater array through matching child params into the rendered label.

## Exercise the interaction

Reverse the array, then open details from the same equipment. Compare the ID in the source row with the ID received by the detail host. An array index can become stale on sort.

## Acceptance and evidence

Capture the repeater path, child parameter name and selected ID at the first divergence.

## Trace a new optional field through an older host

Add a fixture consumer that supplies the previous parameter shape and one that supplies the new field. Observe the child defaults, transformed value and any emitted output. Switch equipment after mount and repeat. Accept the extension when both consumer shapes retain their documented behavior without relying on fabricated registry arguments.
