# Handle a late response after navigation

## Set up the case

In a development host, submit a simulated request for A. Open B before releasing A's response. Then issue a request for B and deliver the results in reverse order.

## Exercise the interaction

Inspect the recipient and correlation evidence for each message. If the contract supplies no correlation ID, avoid attributing a late success to the most recent request.

## Acceptance and evidence

The message must name the correct equipment. Retain the authoritative result separately from temporary notification visibility.

## Resolve two outcomes arriving out of order

Submit two simulated intents with distinct fixture identities. Release the second result first and dismiss its message. Release the first result later. Verify each outcome is still attributable, that dismissing one does not erase the other and that reopening the panel reports only what the authoritative state supports.
