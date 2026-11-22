# Port a controlled selector contract

## Set up the case

Extract the reference selector's public value, display label and dismissal behavior. Build a native fixture host with a selected ID and two duplicate display labels.

## Exercise the interaction

Open, change the highlighted option, cancel and inspect the host value. Reopen after an external host value change. Map each observed transition to the actual native parameter or supported event.

## Acceptance and evidence

Deliver the contract mapping and identify any keyboard behavior that still requires native verification.

## Map a picker with an unavailable selected option

Supply a previously selected value whose option later becomes unavailable. Observe the reference contract for display, clearing and keyboard behavior. Run the same case in a native fixture. Document whether to retain a read-only label, require reselection or use an existing host policy. Verify that opening and closing alone emits no unintended selection intent.
