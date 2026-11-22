# Find which box owns unwanted scrolling

## Set up the case

Open a child standalone, then embed it at the same measured width. Outline the host, Embedded View and child root temporarily in development.

## Exercise the interaction

Inspect position and default-size flags at the first boundary that exceeds available width. Remove the diagnostic outline and exercise a long label before changing overflow.

## Acceptance and evidence

One intended surface scrolls and every control remains reachable. Repeat with another consumer of the same view.

## Keep a footer reachable as validation text grows

Use a native layout with header, scrolling content and action footer. Add a long translated validation message inside the body, then narrow the host. Identify which area now scrolls and whether the footer or last field disappears. Test keyboard navigation to the final field, zoom and dismissal before applying a scoped sizing change.
