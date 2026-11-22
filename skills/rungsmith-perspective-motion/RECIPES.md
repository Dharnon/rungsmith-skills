# Give a filter button local press feedback

## Set up the case

Create a top-level Style Class named filterPress and assign it to a native Button used to open a filter. In the project stylesheet, target its pressed state. Keep the native action attached to the Button.

## Exercise the interaction

Use the CSS example below. Verify that holding shows a local cue, releasing restores the button and rapid presses leave the label legible. Never use the pressed appearance as confirmation of process state.

## Acceptance and evidence

Compare pointer and keyboard activation, disabled appearance and reduced motion. Check the actual client before tuning the example timing.

```css
.psc-filterPress:active {
  transform: translateY(1px);
}
@media (prefers-reduced-motion: reduce) {
  .psc-filterPress:active {
    transform: none;
    outline: 2px solid currentColor;
    outline-offset: -2px;
  }
}
```

The one-pixel offset is a starting point for the fixture. The example changes only the pressed state. Preserve the project's existing focus styling.

## Reveal history without delaying the faceplate

Assign the opening cue to an existing project-owned content wrapper. Display the equipment name, quality indication and close control immediately. Use a reserved chart area while the history binding resolves. If the query returns after the entrance, update only the contents of that area. Give the empty, failed and loading states different text.

To isolate a flash, freeze the selected asset and change the simulated value several times. A flash synchronized with each value change implicates a binding or remount. A flash appearing only when history becomes available points to a different owner. Apply reduced motion and repeat with the popup half open when dismissed.

## Pick the repair by observed failure

| Observation | First place to inspect | Acceptance replay |
| --- | --- | --- |
| The whole panel enters twice | Parent visibility, popup launch count and child mounting | One launch with a delayed first reading |
| The close affordance moves under the pointer | Shell sizing as content arrives | Keep the pointer stationary through history arrival |
| The panel closes but the page is blocked | Popup lifecycle and remaining overlay | Tab and activate the original opener twice |

## Separate hover, focus and press feedback

Use a native fixture button with a project-owned class. Tab to it, hold a pointer press, release outside and then use touch. Check that focus remains visible without hover, a cancelled press produces no action, and touch does not leave a sticky hover state. Examine reduced motion and disabled appearance in the same deployed theme.
