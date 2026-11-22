---
name: rungsmith-perspective-engineering
description: Build, repair or review actual Ignition Perspective views, bindings, parameters and interactions, with version-aware native implementation and repeatable verification. Use for reusable views, faceplates, dashboards, popup identity, dynamic tag paths, or Perspective JSON even when no Rungsmith catalog component is involved. For catalog discovery and downloadable Rungsmith resources use rungsmith-perspective.
metadata:
  status: preview
  native-verification: pending
---

# Engineer native Perspective, not a web mockup

The deliverable is a correct, maintainable **Ignition Perspective resource** and honest evidence about how it was checked. A browser illustration, screenshot, React component or valid-looking JSON is not proof of a working Perspective view.

**Scope:** This skill designs and inspects; it only edits files or runs checks if the user's available tools and authorization permit that. Rungsmith's hosted MCP is a read-only catalog, not a project writer or plant-control tool.

## Route before starting

- **Registered Rungsmith component, contract, source or ZIP:** use `../rungsmith-perspective/SKILL.md` first. Return here only for implementation work outside its catalog contract.
- **Generic native view, view JSON, bindings or view-to-view architecture:** continue here.
- **One specific issue:** use `../rungsmith-performance/SKILL.md` for measured latency, `../rungsmith-data-quality/SKILL.md` for stale/bad values, `../rungsmith-perspective-interactions/SKILL.md` for event/message behavior, and `../rungsmith-perspective-css/SKILL.md` for style/overflow.
- **Web reference to recreate:** classify feasibility with `../rungsmith-web-to-native/SKILL.md` before promising native parity.

Read only the relevant reference and recipe for the task, not every guide on every request: [contracts and bindings](references/contracts-and-bindings.md), [operator states and performance](references/operator-states-and-performance.md), [acceptance and evidence](references/verification.md), [practical recipes](RECIPES.md).

## The construction sequence

### 1. Identify the real surface and acceptance contract

Record the Ignition version and Perspective module version, target project, path, container layout, existing styles, active client type, and whether the source is a Designer export, project filesystem or Gateway API. Distinguish **project resource** changes from **Gateway configuration** changes. Name the operator task, screen dimensions and one realistic happy-path and failure-path use case. A version-sensitive API claim needs a link to the relevant **8.1 or 8.3 manual**, not a guessed path or a borrowed React API.

If version or source is unavailable, clearly mark assumptions and produce a proposal or local fixture only; do not invent a real view path, tag provider, schema or successful deployment.

### 2. Follow data and instance identity before drawing

Trace `operator action → host view → view params → embedded/repeated child → bindings/transforms → tag/query → displayed value`. For interactions, also trace `component event → script/message handler → recipient scope → host action/confirmation`. Record which owner holds **equipment identity**, **view instance identity**, **transient UI state**, and **process state**. Two panels can represent the same machine while remaining two different instances.

Property bindings do **not** cross instance boundaries directly; use declared view params for host-to-child data. Do not silently change an existing input/output/inout parameter, default, or public event. Read [contracts and bindings](references/contracts-and-bindings.md) when this boundary matters.

### 3. Choose the smallest native structure

Prefer native components and existing view/style resources, then a scoped stylesheet where necessary. Choose an appropriate Flex, Column, Breakpoint or Coordinate layout from the target-version component contract; do not assume all CSS layouts or React behavior can be pasted into view JSON. Minimize needless levels of Embedded Views, duplicate subscriptions, query work and per-event Gateway scripts. Use a small host with two realistic fixtures before generalizing a reusable faceplate.

Do not generate or overwrite full project resources solely from an illustrative snippet. Inspect real resource packaging, `view.json`, `resource.json`, dependencies and the target-version API or Designer format first. Preserve all unrelated files and local edits.

### 4. Design all operating states, not just the pretty one

The review must cover **normal**, **fault/alarm**, **bad or stale quality**, **loading**, **empty**, **disconnected** and **disabled/interlocked** where relevant. Identity, units, quality and freshness should remain readable even when the value is unavailable. Never convert missing or bad-quality data to a reassuring zero or “Running” state merely to remove a visual overlay. A quiet alarm screen does not by itself prove alarm health.

Prioritize alarm/state meaning and operator decisions over decorative animation, gradients or arbitrary cards. A visibly disabled control must actually be prevented from invoking its command path. Read [operator states and performance](references/operator-states-and-performance.md).

### 5. Treat process writes as a separate security boundary

Default fixtures and proposals are **read-only and simulated**. Do not add `system.tag.writeBlocking`, bidirectional bindings, alarm acknowledgement or equipment commands without explicit scope/authorization, verified target tag paths, existing roles/interlocks and a dedicated test plan. An animation, CSS class or hidden button is never a security control. Do not present a UI echo as confirmation of PLC state: a requested command and a validated process readback are separate facts.

### 6. Verify by evidence level

Run the cheapest available checks first:
- **Contract/static:** source known, native resource shape for that exact version, referenced view paths, params and bindings, expression and Jython compatibility, styles/dependencies and no unintended writes.
- **Designer/import:** only mark if actually opened/imported successfully in the target Designer.
- **Gateway/session:** only mark if actually synchronized in an authorized dev Gateway and observed in a Perspective session; collect logs, viewport and tag quality.
- **Interaction:** test two instances, reorder/reopen, keyboard and touch where appropriate, wrong/stale identity, missing data and command-disabled scenarios.
- **Performance:** measure cold/warm times and work triggered by navigation at a fixed client, dataset and view revision. No invented milliseconds.

Use [acceptance and evidence](references/verification.md) for pass/block criteria. Inductive Automation's [Perspective automation tools](https://github.com/inductiveautomation/ignition-automation-tools) are a useful testing reference, but are not a support-guaranteed or universal test harness.

### 7. Report like an engineer

Use this review table where applicable:

| Finding | Severity | Exact resource / evidence | Smallest fix | Verification |
| --- | --- | --- | --- | --- |
| Wrong equipment after row reorder | Block | `Host/Repeater → Child.params.assetId`; second click targets old ID | Bind stable asset ID; stop using position index as identity | Reorder A/B, reopen B and assert B throughout |

Severity: **Block** = wrong asset, misleading quality/state, unauthorized/ambiguous writes, missing critical contract; **Major** = broken supported path, unusable focus, repeatable regression; **Minor** = stylistic inconsistency without operational impact.

Conclude with **changed resources**, **known dependencies**, **evidence actually obtained**, **checks not run**, and **remaining risk**. Never convert a planned check into “verified.”

## Reference authority

Version-matched [8.3 Views](https://www.docs.inductiveautomation.com/docs/8.3/ignition-modules/perspective/views-in-perspective), [Property Bindings](https://www.docs.inductiveautomation.com/docs/8.3/ignition-modules/perspective/working-with-perspective-components/bindings-in-perspective/property-bindings-in-perspective), [Tag Bindings](https://docs.inductiveautomation.com/docs/8.3/ignition-modules/perspective/working-with-perspective-components/bindings-in-perspective/tag-bindings-in-perspective), [Style Classes](https://www.docs.inductiveautomation.com/docs/8.3/ignition-modules/perspective/styles/style-classes), and [Scripting](https://docs.inductiveautomation.com/docs/8.3/ignition-modules/perspective/scripting-in-perspective) override generic design advice about platform behavior. Forum observations are reproducible hypotheses, **not hard compatibility limits**.

Practice the regression drills in [RECIPES.md](RECIPES.md); use [EVALS.md](EVALS.md) to test whether an agent applying this skill really rejects unsafe shortcuts.
