---
name: rungsmith-web-platform
description: "A web API is proposed for a native view or embedded preview. Separate modern browser capabilities from what native Perspective can control."
metadata:
  status: draft
  native-verification: pending
---

# Web platform feasibility

Separate modern browser capabilities from what native Perspective can control.

Practice this workflow in a development project: [Check a browser API at the deployment boundary](RECIPES.md).

## Workflow

1. Search the exact capability and read its current guidance.

2. Map it to native events, scoped CSS, website code or a custom module.

3. Return supported implementation choices with lifecycle, security and browser limits; do not inject arbitrary JavaScript into native views.

## Determine who owns the browser capability

For a request such as copying an equipment ID to the clipboard, first identify the surface: Perspective component, separately hosted preview or installed custom module. Check the target version's supported native action, the client's browser capability and any relevant user-gesture or embedding restrictions. Evidence from a standalone web page applies only to that surface.

Describe the native outcome when the capability is unavailable, such as a selectable identifier that the operator can copy manually. Verify success and fallback in the actual deployment context. Return the resource owner, API evidence, client tested and observable result. A browser compatibility table alone cannot establish that a Perspective view exposes the API.

A Perspective component event script runs on the Gateway even when a click in the browser triggers it. A Python event handler therefore cannot call browser objects such as `navigator.clipboard`. Inspect the documented component action or client integration that would perform the operation. [Scripting in Perspective](https://www.docs.inductiveautomation.com/docs/8.1/ignition-modules/perspective/scripting-in-perspective)

## Evaluate a web feature across the actual embed boundary

For popovers, fullscreen behavior or clipboard access, identify the document that owns the initiating element. A button on a catalog page and a control inside an embedded Perspective session can look adjacent while running in separate documents. Determine whether the capability needs browser-local code, a supported native action, an embedding permission or a project stylesheet.

Test the relevant surface directly and then through its deployment wrapper. If the direct test succeeds and the embed fails, inspect the wrapper configuration before modifying the child view. If the native component exposes no supported hook, describe an equivalent operator outcome using a native component. Document which part of the original request remains unsupported on the installed client.

## Identify what the native surface exposes

For a proposed capability, distinguish browser support, an accessible integration point and the actual deployment context. The first can be true while the native component supplies no property, action or event for using it. Inspect the version-matched component contract. Then consider a project-owned stylesheet, existing native component, hosted page or module according to the required lifecycle and the user's scope.

Design the fallback as an operator task. If a browser convenience is unavailable, can the user still identify, select or dismiss the item through a supported native interaction? Test failure explicitly, including embedding conditions where relevant. Report which surface and client were tested; success in a standalone demo cannot establish availability through a native view or embedded deployment.

## Separate native capability from preview delivery

Test the same operator task in three contexts when available: the native session directly, the hosted preview page and the embedded session inside that page. Record the actual URL context or route, client type and visible result. If the direct native view works while the embed loses keyboard access, examine the embed boundary and how focus enters or exits it. Editing the child binding will not fix a host that never passes focus inward.

For a CSS-only change, inspect which document owns the element. A host stylesheet can affect the iframe element's outer size without restyling the remote child document. A native project rule can change inner layout while the host continues clipping it. Compare each boundary before attributing the result to browser compatibility. Offer the supported standalone route when the embedding constraint is unresolved.

Deliver three observations tagged direct, host and embedded, plus the first boundary where behavior diverges and the resource owner able to change it.

## Diagnose by observation

| Observation | Evidence to inspect | How to act on it |
| --- | --- | --- |
| A feature works in a standalone demo only | Identify the execution surface, target client and embed restrictions. | Report the capability at the tested boundary and verify the native fallback. |
| A browser API is available but the native event has no hook | Inspect the installed component's actions and properties. | Choose a supported interaction or document the remaining integration requirement. |

## Perspective constraints

Read the actual native view contract and target-version APIs. Bind displayed process state to its authoritative source. Keep command authorization in the existing command path and preserve controller interlocks. Use supported native properties/events and scoped CSS; web libraries, DOM APIs and React adapters are not executable view definitions. Preserve unrelated resources and local customizations. Do not queue per-frame Gateway scripts to imitate browser-local feedback.

## Evidence and handoff

A capability map and a realistic implementation recommendation. Record the resource paths and tested client/state. Distinguish static checks, import and native interaction verification. Mark unsupported or untested behavior explicitly.

## Example request

Assess CSS anchor positioning and the Popover API for this Perspective tooltip. Explain what is actually controllable.
