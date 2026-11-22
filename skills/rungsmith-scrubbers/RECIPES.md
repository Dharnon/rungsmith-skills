# Round and reconcile a draft setpoint

## Set up the case

Configure a simulated host with range 0 to 10 and step 0.25. Start at 4.50, take one keyboard increment and delay host confirmation.

## Exercise the interaction

Check that the draft reads 4.75 and that the emitted value uses the same unit. Reject it in the fixture, then change the allowed range while editing. Observe the authoritative value and any explanatory state.

## Acceptance and evidence

Count emitted requests for one edit and repeat at the upper bound. Verify that cancellation produces no unintended request.

## Verify a range whose end is off the step grid

Use a fixture range 0.25 to 1.40 with a 0.50 step. Ask which values the host accepts at the upper end and inspect the native control's actual behavior. Test pointer, keyboard End where supported and a typed equivalent if present. Record draft, emitted value, confirmation and rejection. Make the displayed limit and accepted contract agree.
