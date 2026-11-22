# Verification protocol: claims need evidence

This checklist applies to authoring, code review, imports and testing. Do not silently upgrade one evidence level to another.

## Evidence levels

| Level | Required artifact | What you can claim |
| --- | --- | --- |
| L0 Proposal | Target version, assumptions, view contract, risk | Plan only |
| L1 Static | Real source, resource list, semantic checks, source diff | Source inspected; shape and references checked |
| L2 Designer | Import/open result in the named Designer and version | Designer import succeeded |
| L3 Gateway | Dev Gateway sync/open, logs, view path and run ID | Resource is loaded in that Gateway |
| L4 Session | Browser/Workstation actions + screenshot/trace + measured value/quality | Selected behavior observed in the actual Perspective session |
| L5 Controlled action | Authorized command, audit trail, readback and rollback evidence | Only the *specific* tested process interaction is verified |

If only L0–L1 is available, do not say “runs in Ignition,” “importable,” “works,” or “operator-safe.” Mark L2–L5 not run.

## Blocking checks for native changes

- **Target:** exact Ignition version, project, resource path and source revision are stated, or marked unknown.
- **References:** every Embedded View path exists; params and direction match current declarations; prior consumers are not silently broken.
- **Data:** bad/null/stale quality cannot become a convincing healthy process value; units and source timestamps are represented.
- **Identity:** selection, popup, repeater instance and recipient agree on the intended asset even after reorder, fast reopen and two instances.
- **Safety:** no unapproved writes, unaudited command actions, invented permissions, or client-only interlock claims.
- **Native correctness:** no React/DOM APIs passed off as Perspective scripts; expressions, scripts and CSS belong to the right runtime.
- **Dependencies:** required style classes, modules, resource paths and component package versions are accounted for.
- **Integrity:** scoped changes with backup/diff and no unrelated project overwrite.

## Practical acceptance matrix

| Scenario | Setup | Action | Passing observation |
| --- | --- | --- | --- |
| Reusable contract | Two distinct host instances | Change second param after mount | Only second child follows second identity |
| Stale identity | Initial default is A, requested target B | Click immediately during load | No command/detail for A; action withheld until B valid |
| Repeater reorder | A and B rows | Sort descending then open B | Child, popup and data source all show B |
| Bad tag quality | Bad/unavailable reading | Render overview and detail | Distinct unavailable/quality state; not plausible zero |
| Fault | Running + Fault in fixture | Open panel | Fault is legible without hiding equipment identity |
| No history | Empty time range | Open trends | Empty-state label, no invented line/sample |
| Disabled action | Permission/interlock off | Click + keyboard activation | No command event emitted |
| Reopen/duplicate | Two instances of same equipment | Close/reopen one | Only intended instance reacts; no leaked selection |
| Responsive | Desktop + configured touch viewport | Resize/open overlay | No clipped action, focus or units |
| Performance | Fixed viewport, points and Gateway load | 3 cold and 3 warm runs | Comparable timing table, no unverified root-cause claim |

## Report template

```text
Target: [Ignition x.y.z / project / view paths / revision]
Mode: proposal | source-only | Designer | dev Gateway | session
Resources changed: [...]
Inputs and owners: [equipmentId, instanceKey, params direction, quality]
Checks: [PASS with artifact | FAIL with evidence | NOT RUN with reason]
Measurements: [trial count, cold/warm, viewport, sample size]
Known risk: [...]
Rollback / original resource snapshot: [...]
Result: BLOCKED | PROVISIONAL | VERIFIED IN NAMED ENVIRONMENT
```

**Provisional** is the default if native session verification is unavailable. “Verified” must name *what* was actually checked, not imply complete plant validation.

## Repeatability

Store a minimal fixture definition, original source revision, exact touched paths and before/after screenshots or logs where available. Inductive Automation publishes [Perspective session testing helpers](https://github.com/inductiveautomation/ignition-automation-tools), but this repository is not a guarantee of support or of coverage for every third-party component. Choose Playwright, Selenium or other browser automation only when it can actually observe the relevant Perspective behavior; screenshots alone do not verify server-side actions.
