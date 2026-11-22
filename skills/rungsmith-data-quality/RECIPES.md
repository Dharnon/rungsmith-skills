# Distinguish a live zero from a lost reading

## Set up the case

Supply a simulated pressure of 0 kPa with good quality. Change quality while retaining the numeric payload, then restore a good sample of 12 kPa.

## Exercise the interaction

Inspect the bound property before the transform and the formatted label afterwards. If both invalid and valid zero render identically, repair the first transform that discarded quality.

## Acceptance and evidence

Capture the three rendered states with units, freshness cue and asset identity.

## Verify an asset switch while quality recovers

Display A at a valid zero, switch to B with missing feedback, then deliver a late good sample for A. Check the selected ID, value, quality cue and timestamp together. Advance only B to good quality. Document the first binding where A and B become indistinguishable if the reading or timestamp crosses equipment boundaries.
