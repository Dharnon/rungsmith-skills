# Prove a pump popup is bound to the selected pump

## Set up the case

Create two simulated instances with different identifiers and opposite running indications. Open the first faceplate, switch to history, close it and open the second.

## Exercise the interaction

Read the title, running indication and history series together. Change only the first fixture while the second is open. If the second moves, inspect host params, message targeting and reused popup identity.

## Acceptance and evidence

Record the first mismatched field and its source binding before editing the shared faceplate.

## Adapt the same family to two instrumentation levels

Provide one pump fixture with speed feedback and one without that channel. Add a third state where the channel exists but its quality is bad. Inspect the declared params and show how the host represents all three states. Verify the compact view and modal presentation agree about availability and that switching between them preserves equipment identity.
