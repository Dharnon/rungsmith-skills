# Resolve drag versus scroll on touch

## Set up the case

Place the control inside its real scroll container. Use a simulated numeric target and log the requested value. Start with a vertical swipe from the control label.

## Exercise the interaction

Repeat with a horizontal drag and a release outside the control. If release is lost, compare the installed native slider and an explicit Apply interaction before adding handlers.

## Acceptance and evidence

One gesture has one owner. Record scrolling, draft value, emitted intent and cancellation for each path.

## Cancel after the surrounding view changes

Begin a drag on equipment A in a fixture and change the selected asset before releasing. Repeat with a popup close and a range change. Count the resulting intents and inspect the associated identity. If the gesture cannot be completed in its original context, demonstrate the supported cancellation behavior and the value shown on the next open.
