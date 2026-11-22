---
name: rungsmith-faceplates
description: Select, embed and verify Rungsmith glass equipment faceplates and their modal hosts. Use for tank, PID, analog sensor, motor, pump and valve panels with native Perspective state.
metadata:
  version: "1.0.0"
---

# Native equipment faceplates

Discover the exact equipment entry with search_components and list_catalog_examples. The current glass family contains glass-tank-faceplate (TK-101), glass-pid-faceplate (FIC-101), glass-sensor-faceplate (TT-201), glass-motor-faceplate (M-401), glass-pump-faceplate (P-501) and glass-valve-faceplate (FV-301). These are independent resources; equipment-faceplates is the older classic panel. Glass Compact is a workspace that opens equipment panels as dialogs.

Read the available contract before editing. Premium preview access does not grant source access. Never infer hidden params or scripts from captures. Preserve named styles and shared dependencies when an authorized native package is provided.

For a modal, let the host choose the equipment instance, populate its declared params and open the native popup. Reserve its final geometry from the beginning. Render the Control tab first; create heavy history or maintenance content when needed, if the existing native implementation supports this. Avoid arbitrary multi-second delays or animation of width/height to mask layout problems. Show meaningful readiness based on essential data and retain a stable shell while waiting.

Keep each equipment instance's commands and state isolated. Confirm input/output/inout directions and close-popup identifiers. Display disconnected/bad-quality values distinctly, preserve command interlocks, and distinguish sample state from real tags. Only bind live commands within the user's explicitly requested equipment scope.

Verify open, close, reopen, tab switching, two different equipment instances, command feedback, alarm states and container resizing. A loaded iframe or a JSON parse is not runtime verification. Report measurements or observations of initial render rather than claiming zero loading from a static screenshot.

Practice this workflow in a development project: [Prove a pump popup is bound to the selected pump](RECIPES.md).

## Commission the display contract with fixture equipment

For each displayed channel, record the declared parameter, host binding, engineering unit and behavior on quality loss. For a pump, trace requested start and observed running indication separately. For a PID faceplate, trace setpoint, process variable and output independently so a formatting change cannot silently swap quantities.

Embed two instances with different fixture identities. Open a detail panel from each, switch between Control and History, then reopen the first. Verify the panel header, history source and command intent all resolve to the selected fixture. Test one instance with a valid zero while the other has a missing measurement. Save the mapping and observations with the resource path.

## Handle optional channels without changing their meaning

Read the contract for the specific equipment family before reusing a tab or field from another faceplate. A pump with no speed feedback, a pump reporting zero speed and a pump whose feedback has bad quality require different presentations. Determine which conditions the host can distinguish from the supplied parameters. Preserve that distinction through formatting and conditional visibility.

For an optional channel absent by design, inspect the resulting layout and tab order. For an installed channel that stops updating, keep its identity visible with the project's quality treatment. Exercise both cases inside the modal host as well as the embedded overview. Confirm that neighboring process units, state labels and command targets still refer to the displayed equipment.
## Separate the reusable equipment contract from its host

Sketch the child inputs, host-owned selections and outputs on a single equipment example. Record the engineering meaning of each displayed value. For a motor, command requested, permissive status, feedback running and fault are different signals. Decide which are present in the installed contract before assigning indicators. A single green button cannot stand in for all four.

Walk through cold open, asset change and reopen. On cold open, defaults may be visible before binding results arrive. On asset change, the header may update before asynchronous history returns. On reopen, a stored tab can select content that the new equipment does not support. Specify which part of the shell stays stable and when each dependent region can display meaningful data.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| A badge says running as soon as Start is pressed | Trace requested command and running feedback to separate fixture signals. | Bind running to actual feedback and present pending intent separately. |
| A tab persists on an asset with no matching instrumentation | Inspect stored selection and the new asset's available sections. | Choose a valid visible tab as part of context reconciliation. |
